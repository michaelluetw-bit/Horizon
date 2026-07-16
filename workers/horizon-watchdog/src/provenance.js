import { MAX_INVOCATION_LAG_MS, targetDateForTaipei, WATCHDOG_CRON } from "./contracts.js";

export const ASSERTION_ISSUER = "urn:horizon:cloudflare-watchdog:v1";
export const ASSERTION_AUDIENCE = "urn:horizon:p0-b2r:redemption:v1";
export const HORIZON_REPOSITORY = "michaelluetw-bit/Horizon";
export const HORIZON_WORKFLOW_IDENTIFIER =
  "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main";
export const KEY_ID = "horizon-watchdog-ed25519-v1";

const ASSERTION_HEADER = {
  alg: "EdDSA",
  kid: KEY_ID,
  typ: "application/horizon-provenance-assertion+jws",
};
const encoder = new TextEncoder();
const decoder = new TextDecoder("utf-8", { fatal: true });

function base64urlEncode(bytes) {
  let binary = "";
  for (const byte of bytes) {
    binary += String.fromCharCode(byte);
  }
  return btoa(binary).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

function base64urlDecode(value) {
  if (typeof value !== "string" || !/^[A-Za-z0-9_-]+$/.test(value)) {
    throw new Error("INVALID_BASE64URL");
  }
  const padded = `${value}${"=".repeat((4 - (value.length % 4)) % 4)}`.replaceAll("-", "+").replaceAll("_", "/");
  const binary = atob(padded);
  return Uint8Array.from(binary, (character) => character.charCodeAt(0));
}

function canonicalJson(value) {
  if (value === null || typeof value === "string" || typeof value === "boolean") {
    return JSON.stringify(value);
  }
  if (typeof value === "number") {
    if (!Number.isFinite(value)) {
      throw new Error("NON_FINITE_JSON_NUMBER");
    }
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) {
    return `[${value.map((entry) => canonicalJson(entry)).join(",")}]`;
  }
  if (typeof value === "object") {
    return `{${Object.keys(value)
      .sort()
      .map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`)
      .join(",")}}`;
  }
  throw new Error("UNSUPPORTED_JSON_VALUE");
}

async function sha256Hex(text) {
  const digest = await crypto.subtle.digest("SHA-256", encoder.encode(text));
  return Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, "0")).join("");
}

function watchdogScheduledTime(targetDate) {
  return Date.parse(`${targetDate}T07:00:00+08:00`);
}

function scheduleClaimsAreValid(payload) {
  if (
    payload.controller_cron !== WATCHDOG_CRON ||
    !Number.isInteger(payload.controller_scheduled_time) ||
    typeof payload.target_date !== "string"
  ) {
    return false;
  }
  const expectedTargetDate = targetDateForTaipei(payload.controller_scheduled_time);
  return (
    payload.target_date === expectedTargetDate &&
    Math.abs(payload.controller_scheduled_time - watchdogScheduledTime(expectedTargetDate)) <=
      MAX_INVOCATION_LAG_MS
  );
}

function hasValidJti(payload) {
  try {
    return (
      typeof payload.jti === "string" &&
      payload.jti === payload.one_time_nonce &&
      base64urlDecode(payload.jti).byteLength === 32
    );
  } catch {
    return false;
  }
}

function assertionClaimRejection(payload, nowSeconds) {
  if (
    payload.schema_version !== 1 ||
    payload.issuer !== ASSERTION_ISSUER ||
    payload.audience !== ASSERTION_AUDIENCE ||
    payload.repository !== HORIZON_REPOSITORY ||
    payload.workflow_identifier !== HORIZON_WORKFLOW_IDENTIFIER
  ) {
    return "ASSERTION_CLAIMS_INVALID";
  }
  if (!scheduleClaimsAreValid(payload)) {
    return "ASSERTION_SCHEDULE_TIME_INVALID";
  }
  if (!hasValidJti(payload)) {
    return "ASSERTION_JTI_INVALID";
  }
  if (
    !Number.isInteger(payload.issued_at) ||
    !Number.isInteger(payload.expires_at) ||
    payload.expires_at !== payload.issued_at + 900
  ) {
    return "ASSERTION_CLAIMS_INVALID";
  }
  if (nowSeconds < payload.issued_at) {
    return "ASSERTION_NOT_YET_VALID";
  }
  if (nowSeconds >= payload.expires_at) {
    return "ASSERTION_EXPIRED";
  }
  return null;
}

async function payloadHashMatches(payload) {
  if (typeof payload.payload_sha256 !== "string" || !/^[a-f0-9]{64}$/.test(payload.payload_sha256)) {
    return false;
  }
  const { payload_sha256: _payloadSha256, ...withoutHash } = payload;
  return payload.payload_sha256 === (await sha256Hex(canonicalJson(withoutHash)));
}

function exactHeaderMatches(header) {
  return (
    header &&
    header.alg === ASSERTION_HEADER.alg &&
    header.kid === ASSERTION_HEADER.kid &&
    header.typ === ASSERTION_HEADER.typ &&
    Object.keys(header).length === Object.keys(ASSERTION_HEADER).length
  );
}

async function signCompactJws(header, payload, privateKeyJwk) {
  const encodedHeader = base64urlEncode(encoder.encode(canonicalJson(header)));
  const encodedPayload = base64urlEncode(encoder.encode(canonicalJson(payload)));
  const signingInput = `${encodedHeader}.${encodedPayload}`;
  const privateKey = await crypto.subtle.importKey("jwk", privateKeyJwk, { name: "Ed25519" }, false, ["sign"]);
  const signature = await crypto.subtle.sign({ name: "Ed25519" }, privateKey, encoder.encode(signingInput));
  return `${signingInput}.${base64urlEncode(new Uint8Array(signature))}`;
}

function parseCompactJws(jws) {
  if (typeof jws !== "string") {
    throw new Error("JWS_INVALID");
  }
  const parts = jws.split(".");
  if (parts.length !== 3 || parts.some((part) => part.length === 0)) {
    throw new Error("JWS_INVALID");
  }
  const [encodedHeader, encodedPayload, encodedSignature] = parts;
  return {
    encodedHeader,
    encodedPayload,
    encodedSignature,
    header: JSON.parse(decoder.decode(base64urlDecode(encodedHeader))),
    payload: JSON.parse(decoder.decode(base64urlDecode(encodedPayload))),
  };
}

export async function createAssertion({ privateKeyJwk, controllerCron, scheduledTime, issuedAtMs, jti }) {
  const targetDate = targetDateForTaipei(scheduledTime);
  const issuedAt = Math.floor(issuedAtMs / 1000);
  const payloadWithoutHash = {
    schema_version: 1,
    issuer: ASSERTION_ISSUER,
    audience: ASSERTION_AUDIENCE,
    repository: HORIZON_REPOSITORY,
    workflow_identifier: HORIZON_WORKFLOW_IDENTIFIER,
    controller_cron: controllerCron,
    controller_scheduled_time: scheduledTime,
    target_date: targetDate,
    jti,
    one_time_nonce: jti,
    issued_at: issuedAt,
    expires_at: issuedAt + 900,
  };
  const payload = {
    ...payloadWithoutHash,
    payload_sha256: await sha256Hex(canonicalJson(payloadWithoutHash)),
  };
  return { jws: await signCompactJws(ASSERTION_HEADER, payload, privateKeyJwk), payload };
}

export async function verifyAssertion({ jws, publicKeyJwk, nowMs }) {
  let parsed;
  try {
    parsed = parseCompactJws(jws);
  } catch {
    return { accepted: false, reason: "ASSERTION_JWS_INVALID" };
  }
  if (!exactHeaderMatches(parsed.header)) {
    return { accepted: false, reason: "ASSERTION_HEADER_INVALID" };
  }

  let signatureValid;
  try {
    const publicKey = await crypto.subtle.importKey("jwk", publicKeyJwk, { name: "Ed25519" }, false, ["verify"]);
    signatureValid = await crypto.subtle.verify(
      { name: "Ed25519" },
      publicKey,
      base64urlDecode(parsed.encodedSignature),
      encoder.encode(`${parsed.encodedHeader}.${parsed.encodedPayload}`),
    );
  } catch {
    return { accepted: false, reason: "ASSERTION_SIGNATURE_INVALID" };
  }
  if (!signatureValid) {
    return { accepted: false, reason: "ASSERTION_SIGNATURE_INVALID" };
  }

  const nowSeconds = Math.floor(nowMs / 1000);
  const claimRejection = assertionClaimRejection(parsed.payload, nowSeconds);
  if (claimRejection) {
    return { accepted: false, reason: claimRejection };
  }
  if (!(await payloadHashMatches(parsed.payload))) {
    return { accepted: false, reason: "ASSERTION_PAYLOAD_HASH_INVALID" };
  }
  return { accepted: true, payload: parsed.payload };
}
