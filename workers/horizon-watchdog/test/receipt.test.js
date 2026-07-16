import { describe, expect, it } from "vitest";

import { createAssertion } from "../src/provenance.js";
import { createReceipt, verifyReceipt } from "../src/receipt.js";

const SCHEDULED_TIME = Date.parse("2026-07-13T23:00:00.000Z");
const REDEEMED_AT = Date.parse("2026-07-13T23:02:00.000Z");
const GITHUB_CONTEXT = {
  github_run_id: 12345,
  github_run_attempt: 1,
  repository: "michaelluetw-bit/Horizon",
  workflow_ref: "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
  commit_sha: "a".repeat(40),
};

async function signingKeys() {
  const keyPair = await crypto.subtle.generateKey({ name: "Ed25519" }, true, ["sign", "verify"]);
  return {
    privateKeyJwk: await crypto.subtle.exportKey("jwk", keyPair.privateKey),
    publicKeyJwk: await crypto.subtle.exportKey("jwk", keyPair.publicKey),
  };
}

describe("Cloudflare redemption receipt", () => {
  it("binds the assertion jti and actual GitHub run context in a signed receipt", async () => {
    const { privateKeyJwk, publicKeyJwk } = await signingKeys();
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 23 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: REDEEMED_AT,
      jti: "D".repeat(43),
    });

    const receipt = await createReceipt({
      privateKeyJwk,
      assertionPayload: assertion.payload,
      githubContext: GITHUB_CONTEXT,
      redeemedAtMs: REDEEMED_AT,
      receiptId: "receipt-1",
    });

    expect(receipt.payload).toMatchObject({
      jti: "D".repeat(43),
      controller_cron: "0 23 * * *",
      controller_scheduled_time: SCHEDULED_TIME,
      target_date: "2026-07-14",
      ...GITHUB_CONTEXT,
      redeemed_at: REDEEMED_AT / 1000,
      receipt_id: "receipt-1",
      provenance_verification_status: "verified",
    });

    await expect(
      verifyReceipt({
        receiptSignature: receipt.receipt_signature,
        publicKeyJwk,
        assertionPayload: assertion.payload,
        githubContext: GITHUB_CONTEXT,
      }),
    ).resolves.toMatchObject({ accepted: true, payload: receipt.payload });
  });

  it("rejects a receipt when the current GitHub run no longer matches", async () => {
    const { privateKeyJwk, publicKeyJwk } = await signingKeys();
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 23 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: REDEEMED_AT,
      jti: "E".repeat(43),
    });
    const receipt = await createReceipt({
      privateKeyJwk,
      assertionPayload: assertion.payload,
      githubContext: GITHUB_CONTEXT,
      redeemedAtMs: REDEEMED_AT,
      receiptId: "receipt-2",
    });

    await expect(
      verifyReceipt({
        receiptSignature: receipt.receipt_signature,
        publicKeyJwk,
        assertionPayload: assertion.payload,
        githubContext: { ...GITHUB_CONTEXT, github_run_id: 99999 },
      }),
    ).resolves.toEqual({ accepted: false, reason: "RECEIPT_CONTEXT_MISMATCH" });
  });
});
