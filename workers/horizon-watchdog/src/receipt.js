const KEY_ID = "horizon-watchdog-ed25519-v1";
const RECEIPT_HEADER = {
  alg: "EdDSA",
  kid: KEY_ID,
  typ: "application/horizon-provenance-receipt+jws",
};
const encoder = new TextEncoder();
const decoder = new TextDecoder("utf-8", { fatal: true });

function base64urlEncode(bytes) {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

function base64urlDecode(value) {
  if (typeof value !== "string" || !/^[A-Za-z0-9_-]+$/.test(value)) throw new Error("INVALID_BASE64URL");
  const padded = `${value}${"=".repeat((4 - (value.length % 4)) % 4)}`.replaceAll("-", "+").replaceAll("_", "/");
  return Uint8Array.from(atob(padded), (character) => character.charCodeAt(0));
}

function canonicalJson(value) {
  if (value === null || typeof value === "string" || typeof value === "boolean") return JSON.stringify(value);
  if (typeof value === "number") {
    if (!Number.isFinite(value)) throw new Error("NON_FINITE_JSON_NUMBER");
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) return `[${value.map((entry) => canonicalJson(entry)).join(",")}]`;
  if (typeof value === "object") {
    return `{${Object.keys(value)
      .sort()
      .map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`)
      .join(",")}}`;
  }
  throw new Error("UNSUPPORTED_JSON_VALUE");
}

function exactHeaderMatches(header) {
  return (
    header &&
    header.alg === RECEIPT_HEADER.alg &&
    header.kid === RECEIPT_HEADER.kid &&
    header.typ === RECEIPT_HEADER.typ &&
    Object.keys(header).length === Object.keys(RECEIPT_HEADER).length
  );
}

async function signReceipt(payload, privateKeyJwk) {
  const encodedHeader = base64urlEncode(encoder.encode(canonicalJson(RECEIPT_HEADER)));
  const encodedPayload = base64urlEncode(encoder.encode(canonicalJson(payload)));
  const signingInput = `${encodedHeader}.${encodedPayload}`;
  const privateKey = await crypto.subtle.importKey("jwk", privateKeyJwk, { name: "Ed25519" }, false, ["sign"]);
  const signature = await crypto.subtle.sign({ name: "Ed25519" }, privateKey, encoder.encode(signingInput));
  return `${signingInput}.${base64urlEncode(new Uint8Array(signature))}`;
}

function receiptMatchesContext(payload, assertionPayload, githubContext) {
  return (
    payload.jti === assertionPayload.jti &&
    payload.controller_cron === assertionPayload.controller_cron &&
    payload.controller_scheduled_time === assertionPayload.controller_scheduled_time &&
    payload.target_date === assertionPayload.target_date &&
    payload.github_run_id === githubContext.github_run_id &&
    payload.github_run_attempt === githubContext.github_run_attempt &&
    payload.repository === githubContext.repository &&
    payload.workflow_ref === githubContext.workflow_ref &&
    payload.commit_sha === githubContext.commit_sha &&
    typeof payload.receipt_id === "string" &&
    payload.receipt_id.length > 0 &&
    Number.isInteger(payload.redeemed_at) &&
    payload.provenance_verification_status === "verified"
  );
}

export async function createReceipt({
  privateKeyJwk,
  assertionPayload,
  githubContext,
  redeemedAtMs,
  receiptId,
}) {
  const payload = {
    jti: assertionPayload.jti,
    controller_cron: assertionPayload.controller_cron,
    controller_scheduled_time: assertionPayload.controller_scheduled_time,
    target_date: assertionPayload.target_date,
    github_run_id: githubContext.github_run_id,
    github_run_attempt: githubContext.github_run_attempt,
    repository: githubContext.repository,
    workflow_ref: githubContext.workflow_ref,
    commit_sha: githubContext.commit_sha,
    redeemed_at: Math.floor(redeemedAtMs / 1000),
    receipt_id: receiptId,
    provenance_verification_status: "verified",
  };
  return { receipt_signature: await signReceipt(payload, privateKeyJwk), payload };
}

export async function verifyReceipt({ receiptSignature, publicKeyJwk, assertionPayload, githubContext }) {
  let encodedHeader;
  let encodedPayload;
  let encodedSignature;
  let header;
  let payload;
  try {
    [encodedHeader, encodedPayload, encodedSignature] = receiptSignature.split(".");
    if (!encodedHeader || !encodedPayload || !encodedSignature || receiptSignature.split(".").length !== 3) {
      throw new Error("INVALID_RECEIPT");
    }
    header = JSON.parse(decoder.decode(base64urlDecode(encodedHeader)));
    payload = JSON.parse(decoder.decode(base64urlDecode(encodedPayload)));
  } catch {
    return { accepted: false, reason: "RECEIPT_JWS_INVALID" };
  }
  if (!exactHeaderMatches(header)) return { accepted: false, reason: "RECEIPT_HEADER_INVALID" };

  let signatureValid;
  try {
    const publicKey = await crypto.subtle.importKey("jwk", publicKeyJwk, { name: "Ed25519" }, false, ["verify"]);
    signatureValid = await crypto.subtle.verify(
      { name: "Ed25519" },
      publicKey,
      base64urlDecode(encodedSignature),
      encoder.encode(`${encodedHeader}.${encodedPayload}`),
    );
  } catch {
    return { accepted: false, reason: "RECEIPT_SIGNATURE_INVALID" };
  }
  if (!signatureValid) return { accepted: false, reason: "RECEIPT_SIGNATURE_INVALID" };
  if (!receiptMatchesContext(payload, assertionPayload, githubContext)) {
    return { accepted: false, reason: "RECEIPT_CONTEXT_MISMATCH" };
  }
  return { accepted: true, payload };
}
