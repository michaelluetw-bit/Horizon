import { describe, expect, it, vi } from "vitest";

import { GITHUB_OIDC_JWKS_URL, verifyGithubOidc } from "../src/github-oidc.js";

const NOW_MS = Date.parse("2026-07-13T22:01:00.000Z");
const AUDIENCE = "urn:horizon:p0-b2r:redemption:v1";

function base64url(value) {
  const bytes = typeof value === "string" ? new TextEncoder().encode(value) : value;
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

async function makeGithubOidcToken(privateKey, claims) {
  const header = base64url(JSON.stringify({ alg: "RS256", kid: "test-github-kid", typ: "JWT" }));
  const payload = base64url(JSON.stringify(claims));
  const signingInput = `${header}.${payload}`;
  const signature = await crypto.subtle.sign(
    { name: "RSASSA-PKCS1-v1_5" },
    privateKey,
    new TextEncoder().encode(signingInput),
  );
  return `${signingInput}.${base64url(new Uint8Array(signature))}`;
}

async function githubKeyPair() {
  const keyPair = await crypto.subtle.generateKey(
    {
      name: "RSASSA-PKCS1-v1_5",
      modulusLength: 2048,
      publicExponent: new Uint8Array([1, 0, 1]),
      hash: "SHA-256",
    },
    true,
    ["sign", "verify"],
  );
  return {
    privateKey: keyPair.privateKey,
    publicJwk: { ...(await crypto.subtle.exportKey("jwk", keyPair.publicKey)), kid: "test-github-kid" },
  };
}

function validClaims() {
  return {
    iss: "https://token.actions.githubusercontent.com",
    aud: AUDIENCE,
    repository: "michaelluetw-bit/Horizon",
    workflow_ref:
      "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
    ref: "refs/heads/main",
    event_name: "workflow_dispatch",
    run_id: 12345,
    run_attempt: 1,
    sha: "a".repeat(40),
    nbf: Math.floor(NOW_MS / 1000) - 1,
    exp: Math.floor(NOW_MS / 1000) + 60,
  };
}

describe("verifyGithubOidc", () => {
  it("accepts only the configured Horizon workflow identity", async () => {
    const { privateKey, publicJwk } = await githubKeyPair();
    const token = await makeGithubOidcToken(privateKey, validClaims());
    const fetchImpl = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ keys: [publicJwk] }), { status: 200 }),
    );

    await expect(
      verifyGithubOidc({ token, audience: AUDIENCE, nowMs: NOW_MS, fetchImpl }),
    ).resolves.toMatchObject({ accepted: true, claims: validClaims() });
    expect(fetchImpl).toHaveBeenCalledWith(GITHUB_OIDC_JWKS_URL);
  });

  it("accepts GitHub's positive decimal string run metadata and normalizes it", async () => {
    const { privateKey, publicJwk } = await githubKeyPair();
    const token = await makeGithubOidcToken(privateKey, {
      ...validClaims(),
      run_id: "12345",
      run_attempt: "1",
    });
    const fetchImpl = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ keys: [publicJwk] }), { status: 200 }),
    );

    await expect(
      verifyGithubOidc({ token, audience: AUDIENCE, nowMs: NOW_MS, fetchImpl }),
    ).resolves.toMatchObject({
      accepted: true,
      claims: expect.objectContaining({ run_id: 12345, run_attempt: 1 }),
    });
  });

  it.each([
    ["repository", { repository: "attacker/Horizon" }],
    [
      "workflow_ref",
      { workflow_ref: "michaelluetw-bit/Horizon/.github/workflows/other.yml@refs/heads/main" },
    ],
    ["ref", { ref: "refs/heads/release" }],
    ["event_name", { event_name: "schedule" }],
    ["audience", { aud: "urn:horizon:other" }],
    ["run_id", { run_id: "not-a-run-id" }],
    ["run_attempt", { run_attempt: "0" }],
  ])("rejects a correctly signed token with an unexpected %s claim", async (_field, mutation) => {
    const { privateKey, publicJwk } = await githubKeyPair();
    const token = await makeGithubOidcToken(privateKey, {
      ...validClaims(),
      ...mutation,
    });
    const fetchImpl = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ keys: [publicJwk] }), { status: 200 }),
    );

    await expect(
      verifyGithubOidc({ token, audience: AUDIENCE, nowMs: NOW_MS, fetchImpl }),
    ).resolves.toEqual({ accepted: false, reason: "OIDC_CLAIMS_INVALID" });
  });
});
