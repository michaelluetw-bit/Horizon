export { FallbackDayGate } from "./fallback-day-gate.js";
export { HandoffRegistry } from "./handoff-registry.js";

import { MAX_INVOCATION_LAG_MS, validateScheduledInvocation, WATCHDOG_CRON } from "./contracts.js";
import {
  decideFallbackRuns,
  decidePrimaryRuns,
  dispatchWatchdogFallback,
  GITHUB_API_HEADERS,
  listWorkflowRuns,
  taipeiCreatedRange,
  WORKFLOW_FILE,
} from "./github-runs.js";
import { verifyGithubOidc } from "./github-oidc.js";
import { ASSERTION_AUDIENCE, createAssertion, verifyAssertion } from "./provenance.js";
import { createReceipt } from "./receipt.js";

function randomJti() {
  const bytes = crypto.getRandomValues(new Uint8Array(32));
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

function registryRequest(path, payload) {
  return new Request(`https://handoff.internal${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
}

async function claimFallbackDay(env, targetDate) {
  if (!env.FALLBACK_DAY_GATE) throw new Error("FALLBACK_DAY_GATE_UNAVAILABLE");
  const stub = env.FALLBACK_DAY_GATE.get(env.FALLBACK_DAY_GATE.idFromName(targetDate));
  const response = await stub.fetch(registryRequest("/claim", { target_date: targetDate }));
  if (response.status === 201) return true;
  if (response.status === 409) return false;
  throw new Error("FALLBACK_DAY_GATE_UNAVAILABLE");
}

function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
}

function rejectProvenance(reason, status = 403) {
  return jsonResponse({ decision: "PROVENANCE_REJECTED", reason }, status);
}

function handoffRoute(request) {
  const { pathname } = new URL(request.url);
  const match = pathname.match(/^\/v1\/handoffs\/([A-Za-z0-9_-]{43})\/(assertion|redeem)$/);
  if (!match) return null;
  return { jti: match[1], action: match[2] };
}

function bearerToken(request) {
  const match = request.headers.get("Authorization")?.match(/^Bearer ([^\s]+)$/);
  return match?.[1] ?? null;
}

function sameJson(left, right) {
  if (left === right) return true;
  if (!left || !right || typeof left !== "object" || typeof right !== "object") return false;
  if (Array.isArray(left) || Array.isArray(right)) {
    return (
      Array.isArray(left) &&
      Array.isArray(right) &&
      left.length === right.length &&
      left.every((value, index) => sameJson(value, right[index]))
    );
  }
  const leftKeys = Object.keys(left).sort();
  const rightKeys = Object.keys(right).sort();
  return (
    leftKeys.length === rightKeys.length &&
    leftKeys.every((key, index) => key === rightKeys[index] && sameJson(left[key], right[key]))
  );
}

function toUtcIso(epochMilliseconds) {
  if (!Number.isInteger(epochMilliseconds)) return null;
  return new Date(epochMilliseconds).toISOString();
}

function watchdogAudit(controller, invocationStartedAt, timing) {
  return {
    configured_watchdog_schedule_expression: WATCHDOG_CRON,
    trigger_schedule_expression: typeof controller.cron === "string" ? controller.cron : null,
    scheduled_time: Number.isInteger(controller.scheduledTime) ? controller.scheduledTime : null,
    scheduled_time_utc: toUtcIso(controller.scheduledTime),
    invocation_started_at: Number.isInteger(invocationStartedAt) ? invocationStartedAt : null,
    invocation_started_at_utc: toUtcIso(invocationStartedAt),
    invocation_delta_ms: timing.invocationDeltaMs,
    max_invocation_lag_ms: MAX_INVOCATION_LAG_MS,
    target_date: timing.targetDate,
    workflow_selector: WORKFLOW_FILE,
    api_version: GITHUB_API_HEADERS["X-GitHub-Api-Version"],
  };
}

function withWatchdogAudit(audit, outcome) {
  const result = { ...audit, ...outcome };
  if (outcome.primaryRunId) result.primary_run_id = outcome.primaryRunId;
  if (outcome.workflowRunId) result.workflow_run_id = outcome.workflowRunId;
  if (outcome.runUrl) result.run_url = outcome.runUrl;
  if (outcome.htmlUrl) result.html_url = outcome.htmlUrl;
  if (outcome.httpStatus) result.http_status = outcome.httpStatus;
  return result;
}

async function getVerifiedAssertion({ stub, jti, claims, publicKeyJwk, nowMs }) {
  const response = await stub.fetch(
    registryRequest("/assertion", {
      github_run_id: claims.run_id,
      github_run_attempt: claims.run_attempt,
    }),
  );
  if (!response.ok) return { accepted: false, reason: "HANDOFF_NOT_ARMED" };
  let stored;
  try {
    stored = await response.json();
  } catch {
    return { accepted: false, reason: "HANDOFF_ASSERTION_INVALID" };
  }
  const verified = await verifyAssertion({
    jws: stored.assertion_jws,
    publicKeyJwk,
    nowMs,
  });
  if (!verified.accepted) return verified;
  if (verified.payload.jti !== jti || !sameJson(stored.assertion_payload, verified.payload)) {
    return { accepted: false, reason: "HANDOFF_ASSERTION_MISMATCH" };
  }
  return { accepted: true, assertionJws: stored.assertion_jws, assertionPayload: verified.payload };
}

export function requestContextMatchesClaims(payload, claims, jti) {
  return (
    payload?.jti === jti &&
    payload.github_run_id === claims.run_id &&
    payload.github_run_attempt === claims.run_attempt &&
    payload.github_repository === claims.repository &&
    payload.github_workflow_ref === claims.workflow_ref &&
    payload.github_sha === claims.sha &&
    payload.github_event_name === claims.event_name
  );
}

export async function handleHandoffRequest({
  request,
  env,
  nowMs,
  fetchImpl = fetch,
  verifyOidcImpl = verifyGithubOidc,
}) {
  if (request.method !== "POST") return jsonResponse({ reason: "METHOD_NOT_ALLOWED" }, 405);
  const route = handoffRoute(request);
  const token = bearerToken(request);
  if (!route || !token || !env.HANDOFF_REGISTRY || !env.HORIZON_ASSERTION_PUBLIC_KEY_JWK) {
    return rejectProvenance("HANDOFF_REQUEST_INVALID", 400);
  }
  const oidc = await verifyOidcImpl({ token, audience: ASSERTION_AUDIENCE, nowMs, fetchImpl });
  if (!oidc.accepted) return rejectProvenance(oidc.reason);

  let publicKeyJwk;
  let stub;
  try {
    publicKeyJwk = JSON.parse(env.HORIZON_ASSERTION_PUBLIC_KEY_JWK);
    stub = env.HANDOFF_REGISTRY.get(env.HANDOFF_REGISTRY.idFromName(route.jti));
  } catch {
    return rejectProvenance("HANDOFF_CONFIGURATION_INVALID", 500);
  }
  const assertion = await getVerifiedAssertion({
    stub,
    jti: route.jti,
    claims: oidc.claims,
    publicKeyJwk,
    nowMs,
  });
  if (!assertion.accepted) return rejectProvenance(assertion.reason);
  if (route.action === "assertion") {
    return jsonResponse({ assertion_jws: assertion.assertionJws, assertion_payload: assertion.assertionPayload });
  }

  let payload;
  try {
    payload = await request.json();
  } catch {
    return rejectProvenance("REDEMPTION_REQUEST_INVALID", 400);
  }
  if (!requestContextMatchesClaims(payload, oidc.claims, route.jti)) {
    return rejectProvenance("GITHUB_CONTEXT_MISMATCH");
  }

  let privateKeyJwk;
  try {
    privateKeyJwk = JSON.parse(env.HORIZON_ASSERTION_PRIVATE_KEY_JWK);
  } catch {
    return rejectProvenance("HANDOFF_CONFIGURATION_INVALID", 500);
  }
  const githubContext = {
    github_run_id: oidc.claims.run_id,
    github_run_attempt: oidc.claims.run_attempt,
    repository: oidc.claims.repository,
    workflow_ref: oidc.claims.workflow_ref,
    commit_sha: oidc.claims.sha,
  };
  const receipt = await createReceipt({
    privateKeyJwk,
    assertionPayload: assertion.assertionPayload,
    githubContext,
    redeemedAtMs: nowMs,
    receiptId: randomJti(),
  });
  const redeemed = await stub.fetch(
    registryRequest("/redeem", {
      github_run_id: oidc.claims.run_id,
      github_run_attempt: oidc.claims.run_attempt,
      github_metadata: {
        repository: oidc.claims.repository,
        workflow_ref: oidc.claims.workflow_ref,
        commit_sha: oidc.claims.sha,
        event_name: oidc.claims.event_name,
      },
      receipt_jws: receipt.receipt_signature,
      receipt_payload: receipt.payload,
    }),
  );
  if (!redeemed.ok) return rejectProvenance("REDEMPTION_REJECTED");
  return jsonResponse(receipt);
}

export async function evaluateScheduledInvocation({ controller, env, invocationStartedAt, fetchImpl }) {
  const timing = validateScheduledInvocation({
    controllerCron: controller.cron,
    scheduledTime: controller.scheduledTime,
    invocationStartedAt,
  });
  const audit = watchdogAudit(controller, invocationStartedAt, timing);
  if (!timing.accepted) {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: timing.decision,
      reason: timing.reason,
    });
  }

  let primaryRuns;
  try {
    primaryRuns = await listWorkflowRuns({
      fetchImpl,
      event: "schedule",
      targetDate: timing.targetDate,
    });
  } catch (error) {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: "CHECK_FAILED",
      reason: error.message,
    });
  }
  const primaryDecision = decidePrimaryRuns(primaryRuns, taipeiCreatedRange(timing.targetDate));
  if (primaryDecision.decision === "PRIMARY_PRESENT") {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: primaryDecision.decision,
      primaryRunId: primaryDecision.primaryRunId,
    });
  }
  if (primaryDecision.decision === "CHECK_FAILED") {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: primaryDecision.decision,
      reason: primaryDecision.reason,
    });
  }

  let fallbackRuns;
  try {
    fallbackRuns = await listWorkflowRuns({
      fetchImpl,
      event: "workflow_dispatch",
      targetDate: timing.targetDate,
    });
  } catch (error) {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: "CHECK_FAILED",
      reason: error.message,
    });
  }
  const fallbackDecision = decideFallbackRuns(fallbackRuns, taipeiCreatedRange(timing.targetDate));
  if (!fallbackDecision.mayDispatch) {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: fallbackDecision.decision,
      reason: fallbackDecision.reason,
      workflowRunId: fallbackDecision.workflowRunId,
    });
  }

  let dayClaimed;
  try {
    dayClaimed = await claimFallbackDay(env, timing.targetDate);
  } catch (error) {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: "CHECK_FAILED",
      reason: error.message,
    });
  }
  if (!dayClaimed) {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: "CHECK_FAILED",
      reason: "FALLBACK_DAY_ALREADY_CLAIMED",
    });
  }

  let privateKeyJwk;
  let stub;
  let assertion;
  const jti = randomJti();
  try {
    if (!env.HORIZON_GITHUB_TOKEN || !env.HORIZON_ASSERTION_PRIVATE_KEY_JWK || !env.HANDOFF_REGISTRY) {
      throw new Error("WATCHDOG_CONFIGURATION_INVALID");
    }
    privateKeyJwk = JSON.parse(env.HORIZON_ASSERTION_PRIVATE_KEY_JWK);
    assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: controller.cron,
      scheduledTime: controller.scheduledTime,
      issuedAtMs: invocationStartedAt,
      jti,
    });
    stub = env.HANDOFF_REGISTRY.get(env.HANDOFF_REGISTRY.idFromName(jti));
    const initialized = await stub.fetch(
      registryRequest("/initialize", {
        jti,
        assertion_jws: assertion.jws,
        assertion_payload: assertion.payload,
      }),
    );
    if (initialized.status !== 201) throw new Error("HANDOFF_INITIALIZATION_FAILED");
  } catch (error) {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: "CHECK_FAILED",
      reason: error.message,
    });
  }

  let dispatch;
  try {
    dispatch = await dispatchWatchdogFallback({
      fetchImpl,
      token: env.HORIZON_GITHUB_TOKEN,
      targetDate: timing.targetDate,
      handoffId: jti,
    });
  } catch {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      decision: "DISPATCH_FAILED",
      reason: "DISPATCH_REQUEST_FAILED",
    });
  }
  if (dispatch.decision !== "DISPATCH_CONFIRMED") {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      ...dispatch,
    });
  }

  try {
    const armed = await stub.fetch(
      registryRequest("/arm", {
        github_run_id: dispatch.workflowRunId,
        github_run_attempt: 1,
      }),
    );
    if (!armed.ok) throw new Error("HANDOFF_NOT_ARMED");
  } catch {
    return withWatchdogAudit(audit, {
      targetDate: timing.targetDate,
      scheduledTime: controller.scheduledTime,
      invocationStartedAt,
      invocationDeltaMs: timing.invocationDeltaMs,
      ...dispatch,
      decision: "CHECK_FAILED",
      reason: "HANDOFF_NOT_ARMED",
    });
  }
  return withWatchdogAudit(audit, {
    targetDate: timing.targetDate,
    scheduledTime: controller.scheduledTime,
    invocationStartedAt,
    invocationDeltaMs: timing.invocationDeltaMs,
    ...dispatch,
  });
}

export default {
  async scheduled(controller, env, ctx) {
    const work = evaluateScheduledInvocation({
      controller,
      env,
      invocationStartedAt: Date.now(),
      fetchImpl: fetch,
    }).then((result) => console.log(JSON.stringify(result)));
    ctx.waitUntil(work);
  },
  async fetch(request, env) {
    return handleHandoffRequest({ request, env, nowMs: Date.now(), fetchImpl: fetch });
  },
};
