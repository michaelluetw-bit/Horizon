import { verifyAssertion } from "./provenance.js";
import { verifyReceipt } from "./receipt.js";

function provenanceError(reason) {
  return new Error(`PROVENANCE_REJECTED:${reason}`);
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

function handoffUrl(watchdogUrl, handoffId, action) {
  if (typeof handoffId !== "string" || !/^[A-Za-z0-9_-]{43}$/.test(handoffId)) {
    throw provenanceError("HANDOFF_ID_INVALID");
  }
  let base;
  try {
    base = new URL(watchdogUrl);
  } catch {
    throw provenanceError("WATCHDOG_URL_INVALID");
  }
  if (
    base.protocol !== "https:" ||
    !base.hostname ||
    base.username ||
    base.password ||
    base.search ||
    base.hash
  ) {
    throw provenanceError("WATCHDOG_URL_INVALID");
  }
  base.pathname = `${base.pathname.replace(/\/$/, "")}/v1/handoffs/${handoffId}/${action}`;
  return base.toString();
}

async function responseJson(response, failureReason) {
  if (!response.ok) throw provenanceError(failureReason);
  try {
    return await response.json();
  } catch {
    throw provenanceError(failureReason);
  }
}

export async function redeemWorkflowProvenance({
  handoffId,
  oidcToken,
  watchdogUrl,
  publicKeyJwk,
  githubContext,
  nowMs,
  fetchImpl,
}) {
  if (!oidcToken || !watchdogUrl || !publicKeyJwk) throw provenanceError("CONFIGURATION_INVALID");
  const headers = { Authorization: `Bearer ${oidcToken}` };
  const assertionEnvelope = await responseJson(
    await fetchImpl(handoffUrl(watchdogUrl, handoffId, "assertion"), { method: "POST", headers }),
    "ASSERTION_ENDPOINT_REJECTED",
  );
  const assertion = await verifyAssertion({
    jws: assertionEnvelope.assertion_jws,
    publicKeyJwk,
    nowMs,
  });
  if (!assertion.accepted || !sameJson(assertion.payload, assertionEnvelope.assertion_payload)) {
    throw provenanceError(assertion.reason ?? "ASSERTION_MISMATCH");
  }

  const redemptionPayload = {
    jti: handoffId,
    github_run_id: githubContext.github_run_id,
    github_run_attempt: githubContext.github_run_attempt,
    github_repository: githubContext.repository,
    github_workflow_ref: githubContext.workflow_ref,
    github_sha: githubContext.commit_sha,
    github_event_name: githubContext.event_name,
  };
  const receiptEnvelope = await responseJson(
    await fetchImpl(handoffUrl(watchdogUrl, handoffId, "redeem"), {
      method: "POST",
      headers: { ...headers, "Content-Type": "application/json" },
      body: JSON.stringify(redemptionPayload),
    }),
    "REDEMPTION_ENDPOINT_REJECTED",
  );
  const receipt = await verifyReceipt({
    receiptSignature: receiptEnvelope.receipt_signature,
    publicKeyJwk,
    assertionPayload: assertion.payload,
    githubContext,
  });
  if (!receipt.accepted || !sameJson(receipt.payload, receiptEnvelope.payload)) {
    throw provenanceError(receipt.reason ?? "RECEIPT_MISMATCH");
  }
  return {
    targetDate: assertion.payload.target_date,
    assertionPayload: assertion.payload,
    receiptSignature: receiptEnvelope.receipt_signature,
    receiptPayload: receipt.payload,
  };
}
