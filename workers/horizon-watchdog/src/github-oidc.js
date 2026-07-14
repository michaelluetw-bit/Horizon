export const GITHUB_OIDC_ISSUER = "https://token.actions.githubusercontent.com";
export const GITHUB_OIDC_JWKS_URL = `${GITHUB_OIDC_ISSUER}/.well-known/jwks`;
export const HORIZON_REPOSITORY = "michaelluetw-bit/Horizon";
export const HORIZON_WORKFLOW_REF =
  "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main";

const encoder = new TextEncoder();
const decoder = new TextDecoder("utf-8", { fatal: true });

function base64urlDecode(value) {
  if (typeof value !== "string" || !/^[A-Za-z0-9_-]+$/.test(value)) {
    throw new Error("INVALID_BASE64URL");
  }
  const padded = `${value}${"=".repeat((4 - (value.length % 4)) % 4)}`.replaceAll("-", "+").replaceAll("_", "/");
  return Uint8Array.from(atob(padded), (character) => character.charCodeAt(0));
}

function parseJwt(token) {
  if (typeof token !== "string") throw new Error("OIDC_TOKEN_INVALID");
  const parts = token.split(".");
  if (parts.length !== 3 || parts.some((part) => part.length === 0)) throw new Error("OIDC_TOKEN_INVALID");
  const [encodedHeader, encodedPayload, encodedSignature] = parts;
  return {
    encodedHeader,
    encodedPayload,
    encodedSignature,
    header: JSON.parse(decoder.decode(base64urlDecode(encodedHeader))),
    claims: JSON.parse(decoder.decode(base64urlDecode(encodedPayload))),
  };
}

function claimsAreExpected(claims, audience, nowSeconds) {
  return (
    claims.iss === GITHUB_OIDC_ISSUER &&
    claims.aud === audience &&
    claims.repository === HORIZON_REPOSITORY &&
    claims.workflow_ref === HORIZON_WORKFLOW_REF &&
    claims.ref === "refs/heads/main" &&
    claims.event_name === "workflow_dispatch" &&
    Number.isInteger(claims.run_id) &&
    claims.run_id > 0 &&
    Number.isInteger(claims.run_attempt) &&
    claims.run_attempt > 0 &&
    typeof claims.sha === "string" &&
    /^[a-f0-9]{40}$/i.test(claims.sha) &&
    Number.isInteger(claims.nbf) &&
    Number.isInteger(claims.exp) &&
    claims.nbf <= nowSeconds &&
    nowSeconds < claims.exp
  );
}

export async function verifyGithubOidc({ token, audience, nowMs, fetchImpl }) {
  let parsed;
  try {
    parsed = parseJwt(token);
  } catch {
    return { accepted: false, reason: "OIDC_TOKEN_INVALID" };
  }
  if (parsed.header.alg !== "RS256" || typeof parsed.header.kid !== "string") {
    return { accepted: false, reason: "OIDC_HEADER_INVALID" };
  }

  let jwks;
  try {
    const response = await fetchImpl(GITHUB_OIDC_JWKS_URL);
    if (!response.ok) return { accepted: false, reason: "OIDC_JWKS_UNAVAILABLE" };
    jwks = await response.json();
  } catch {
    return { accepted: false, reason: "OIDC_JWKS_UNAVAILABLE" };
  }
  const jwk = jwks?.keys?.find((candidate) => candidate.kid === parsed.header.kid && candidate.kty === "RSA");
  if (!jwk) {
    return { accepted: false, reason: "OIDC_KEY_NOT_FOUND" };
  }

  let signatureValid;
  try {
    const publicKey = await crypto.subtle.importKey(
      "jwk",
      jwk,
      { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" },
      false,
      ["verify"],
    );
    signatureValid = await crypto.subtle.verify(
      { name: "RSASSA-PKCS1-v1_5" },
      publicKey,
      base64urlDecode(parsed.encodedSignature),
      encoder.encode(`${parsed.encodedHeader}.${parsed.encodedPayload}`),
    );
  } catch {
    return { accepted: false, reason: "OIDC_SIGNATURE_INVALID" };
  }
  if (!signatureValid) {
    return { accepted: false, reason: "OIDC_SIGNATURE_INVALID" };
  }

  if (!claimsAreExpected(parsed.claims, audience, Math.floor(nowMs / 1000))) {
    return { accepted: false, reason: "OIDC_CLAIMS_INVALID" };
  }
  return { accepted: true, claims: parsed.claims };
}
