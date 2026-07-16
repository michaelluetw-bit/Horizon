import { redeemWorkflowProvenance } from "./github-redemption.js";

const TAIPEI = "Asia/Taipei";
const PRIMARY_CRON = "17 20 * * *";
const OIDC_AUDIENCE = "urn:horizon:p0-b2r:redemption:v1";

export function taipeiToday(nowMs = Date.now()) {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: TAIPEI,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(new Date(nowMs));
  const values = Object.fromEntries(
    parts.filter(({ type }) => type !== "literal").map(({ type, value }) => [type, value]),
  );
  return `${values.year}-${values.month}-${values.day}`;
}

function isPrimaryScheduleOnTime(nowMs, targetDate) {
  const startsAt = Date.parse(`${targetDate}T04:12:00+08:00`);
  const endsAt = Date.parse(`${targetDate}T04:22:00+08:00`);
  return nowMs >= startsAt && nowMs <= endsAt;
}

export function required(env, name) {
  const value = env[name];
  if (!value) throw new Error(`PROVENANCE_REJECTED:MISSING_${name}`);
  return value;
}

export function githubContext(env) {
  const githubRunId = Number(required(env, "GITHUB_RUN_ID"));
  const githubRunAttempt = Number(required(env, "GITHUB_RUN_ATTEMPT"));
  const commitSha = required(env, "GITHUB_SHA");
  if (!Number.isInteger(githubRunId) || !Number.isInteger(githubRunAttempt) || !/^[a-f0-9]{40}$/i.test(commitSha)) {
    throw new Error("PROVENANCE_REJECTED:GITHUB_CONTEXT_INVALID");
  }
  return {
    github_run_id: githubRunId,
    github_run_attempt: githubRunAttempt,
    repository: required(env, "GITHUB_REPOSITORY"),
    workflow_ref: required(env, "HORIZON_GITHUB_WORKFLOW_REF"),
    commit_sha: commitSha,
    event_name: required(env, "GITHUB_EVENT_NAME"),
    event_schedule: env.GITHUB_EVENT_SCHEDULE ?? "",
  };
}

export async function requestOidcToken({ env, audience = OIDC_AUDIENCE, fetchImpl = fetch }) {
  const requestUrl = new URL(required(env, "ACTIONS_ID_TOKEN_REQUEST_URL"));
  requestUrl.searchParams.set("audience", audience);
  const response = await fetchImpl(requestUrl, {
    headers: { Authorization: `Bearer ${required(env, "ACTIONS_ID_TOKEN_REQUEST_TOKEN")}` },
  });
  if (!response.ok) throw new Error("PROVENANCE_REJECTED:OIDC_TOKEN_REQUEST_FAILED");
  const payload = await response.json();
  if (typeof payload.value !== "string") throw new Error("PROVENANCE_REJECTED:OIDC_TOKEN_INVALID");
  return payload.value;
}

export async function prepareProvenance({
  env,
  nowMs = Date.now(),
  primaryStartedAtMs = nowMs,
  fetchImpl = fetch,
  redeemImpl = redeemWorkflowProvenance,
  requestOidcTokenImpl = requestOidcToken,
}) {
  const context = githubContext(env);
  const triggerSource = env.HORIZON_TRIGGER_SOURCE ?? "";
  const handoffId = env.HORIZON_HANDOFF_ID ?? "";
  const targetDateInput = env.HORIZON_TARGET_DATE ?? "";

  if (context.event_name === "schedule") {
    if (!Number.isInteger(primaryStartedAtMs)) {
      throw new Error("PROVENANCE_REJECTED:PRIMARY_START_TIME_INVALID");
    }
    const actualCron = context.event_schedule;
    if (!actualCron) {
      throw new Error("PROVENANCE_REJECTED:MISSING_EVENT_SCHEDULE");
    }
    const targetDate = taipeiToday(primaryStartedAtMs);
    const isPrimary = actualCron === PRIMARY_CRON;
    return {
      trigger_source: isPrimary ? "primary" : "scheduled-verification",
      trigger_event: "schedule",
      trigger_schedule_expression: actualCron,
      target_date: targetDate,
      primary_schedule_on_time: isPrimary && isPrimaryScheduleOnTime(primaryStartedAtMs, targetDate),
      github: context,
    };
  }

  if (context.event_name !== "workflow_dispatch") {
    throw new Error("PROVENANCE_REJECTED:EVENT_INVALID");
  }
  if (!handoffId && triggerSource !== "fallback-watchdog") {
    return {
      trigger_source: "manual",
      trigger_event: "workflow_dispatch",
      trigger_schedule_expression: null,
      target_date: taipeiToday(nowMs),
      github: context,
      github_actor: required(env, "GITHUB_ACTOR"),
    };
  }
  if (!handoffId || triggerSource !== "fallback-watchdog" || !targetDateInput) {
    throw new Error("PROVENANCE_REJECTED:WATCHDOG_INPUT_INVALID");
  }

  let publicKeyJwk;
  try {
    publicKeyJwk = JSON.parse(required(env, "HORIZON_WATCHDOG_PUBLIC_KEY_JWK"));
  } catch {
    throw new Error("PROVENANCE_REJECTED:WATCHDOG_PUBLIC_KEY_INVALID");
  }
  const oidcToken = await requestOidcTokenImpl({ env, audience: OIDC_AUDIENCE, fetchImpl });
  const redeemed = await redeemImpl({
    handoffId,
    oidcToken,
    watchdogUrl: required(env, "HORIZON_WATCHDOG_URL"),
    publicKeyJwk,
    githubContext: context,
    nowMs,
    fetchImpl,
  });
  if (redeemed.targetDate !== targetDateInput) {
    throw new Error("PROVENANCE_REJECTED:TARGET_DATE_MISMATCH");
  }
  return {
    trigger_source: "watchdog",
    trigger_event: "workflow_dispatch",
    trigger_schedule_expression: redeemed.receiptPayload.controller_cron,
    target_date: redeemed.targetDate,
    github: context,
    receipt_signature: redeemed.receiptSignature,
    receipt: redeemed.receiptPayload,
  };
}
