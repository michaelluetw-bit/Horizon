import { describe, expect, it } from "vitest";

import {
  ASSERTION_AUDIENCE,
  ASSERTION_ISSUER,
  createAssertion,
  verifyAssertion,
} from "../src/provenance.js";

const SCHEDULED_TIME = Date.parse("2026-07-13T23:00:00.000Z");
const ISSUED_AT = Date.parse("2026-07-13T23:01:00.000Z");

async function signingKeys() {
  const keyPair = await crypto.subtle.generateKey({ name: "Ed25519" }, true, ["sign", "verify"]);
  return {
    privateKeyJwk: await crypto.subtle.exportKey("jwk", keyPair.privateKey),
    publicKeyJwk: await crypto.subtle.exportKey("jwk", keyPair.publicKey),
  };
}

function base64urlEncode(bytes) {
  let binary = "";
  for (const byte of bytes) binary += String.fromCharCode(byte);
  return btoa(binary).replaceAll("+", "-").replaceAll("/", "_").replaceAll("=", "");
}

function base64urlDecode(value) {
  const padded = `${value}${"=".repeat((4 - (value.length % 4)) % 4)}`.replaceAll("-", "+").replaceAll("_", "/");
  return Uint8Array.from(atob(padded), (character) => character.charCodeAt(0));
}

async function resignPayload(jws, privateKeyJwk, payload) {
  const [encodedHeader] = jws.split(".");
  const encodedPayload = base64urlEncode(new TextEncoder().encode(JSON.stringify(payload)));
  const signingInput = `${encodedHeader}.${encodedPayload}`;
  const privateKey = await crypto.subtle.importKey("jwk", privateKeyJwk, { name: "Ed25519" }, false, ["sign"]);
  const signature = await crypto.subtle.sign({ name: "Ed25519" }, privateKey, new TextEncoder().encode(signingInput));
  return `${signingInput}.${base64urlEncode(new Uint8Array(signature))}`;
}

async function payloadHash(payload) {
  const { payload_sha256: _payloadSha256, ...withoutHash } = payload;
  const canonical = JSON.stringify(
    Object.fromEntries(Object.entries(withoutHash).sort(([left], [right]) => left.localeCompare(right))),
  );
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(canonical));
  return Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, "0")).join("");
}

describe("Cloudflare provenance assertion", () => {
  it("signs all required authoritative claims and verifies them against the scheduled time", async () => {
    const { privateKeyJwk, publicKeyJwk } = await signingKeys();

    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 23 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: ISSUED_AT,
      jti: "A".repeat(43),
    });

    expect(assertion.payload).toMatchObject({
      schema_version: 1,
      issuer: ASSERTION_ISSUER,
      audience: ASSERTION_AUDIENCE,
      repository: "michaelluetw-bit/Horizon",
      workflow_identifier:
        "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
      controller_cron: "0 23 * * *",
      controller_scheduled_time: SCHEDULED_TIME,
      target_date: "2026-07-14",
      jti: "A".repeat(43),
      one_time_nonce: "A".repeat(43),
      issued_at: ISSUED_AT / 1000,
      expires_at: ISSUED_AT / 1000 + 900,
    });
    expect(assertion.payload.payload_sha256).toMatch(/^[a-f0-9]{64}$/);

    await expect(
      verifyAssertion({
        jws: assertion.jws,
        publicKeyJwk,
        nowMs: ISSUED_AT + 1,
      }),
    ).resolves.toMatchObject({
      accepted: true,
      payload: assertion.payload,
    });
  });

  it("rejects an assertion at its fixed expiry boundary", async () => {
    const { privateKeyJwk, publicKeyJwk } = await signingKeys();
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 23 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: ISSUED_AT,
      jti: "B".repeat(43),
    });

    await expect(
      verifyAssertion({
        jws: assertion.jws,
        publicKeyJwk,
        nowMs: ISSUED_AT + 900_000,
      }),
    ).resolves.toEqual({ accepted: false, reason: "ASSERTION_EXPIRED" });
  });

  it("rejects a signed assertion whose payload hash no longer matches its claims", async () => {
    const { privateKeyJwk, publicKeyJwk } = await signingKeys();
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 23 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: ISSUED_AT,
      jti: "C".repeat(43),
    });
    const [, encodedPayload] = assertion.jws.split(".");
    const tamperedPayload = {
      ...JSON.parse(new TextDecoder().decode(base64urlDecode(encodedPayload))),
      payload_sha256: "0".repeat(64),
    };
    const tampered = await resignPayload(assertion.jws, privateKeyJwk, tamperedPayload);

    await expect(
      verifyAssertion({
        jws: tampered,
        publicKeyJwk,
        nowMs: ISSUED_AT + 1,
      }),
    ).resolves.toEqual({ accepted: false, reason: "ASSERTION_PAYLOAD_HASH_INVALID" });
  });

  it.each([
    ["an out-of-window scheduled time", { controller_scheduled_time: SCHEDULED_TIME + 300_001 }],
    ["a target date that differs from the Taipei scheduled date", { target_date: "2026-07-13" }],
  ])("rejects a signed assertion with %s", async (_description, mutation) => {
    const { privateKeyJwk, publicKeyJwk } = await signingKeys();
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 23 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: ISSUED_AT,
      jti: "D".repeat(43),
    });
    const payload = { ...assertion.payload, ...mutation };
    payload.payload_sha256 = await payloadHash(payload);
    const resigned = await resignPayload(assertion.jws, privateKeyJwk, payload);

    await expect(
      verifyAssertion({
        jws: resigned,
        publicKeyJwk,
        nowMs: ISSUED_AT + 1,
      }),
    ).resolves.toEqual({ accepted: false, reason: "ASSERTION_SCHEDULE_TIME_INVALID" });
  });
});
