import { describe, expect, it, vi } from "vitest";

import { redeemWorkflowProvenance } from "../src/github-redemption.js";
import { createAssertion } from "../src/provenance.js";
import { createReceipt } from "../src/receipt.js";

const SCHEDULED_TIME = Date.parse("2026-07-13T23:00:00.000Z");
const JTI = "G".repeat(43);
const GITHUB_CONTEXT = {
  github_run_id: 12345,
  github_run_attempt: 1,
  repository: "michaelluetw-bit/Horizon",
  workflow_ref: "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
  commit_sha: "a".repeat(40),
  event_name: "workflow_dispatch",
};

async function signingKeys() {
  const keyPair = await crypto.subtle.generateKey({ name: "Ed25519" }, true, ["sign", "verify"]);
  return {
    privateKeyJwk: await crypto.subtle.exportKey("jwk", keyPair.privateKey),
    publicKeyJwk: await crypto.subtle.exportKey("jwk", keyPair.publicKey),
  };
}

describe("redeemWorkflowProvenance", () => {
  it("rejects a non-HTTPS watchdog endpoint before sending GitHub identity material", async () => {
    const fetchImpl = vi.fn();

    await expect(
      redeemWorkflowProvenance({
        handoffId: JTI,
        oidcToken: "github-oidc-token",
        watchdogUrl: "http://watchdog.example",
        publicKeyJwk: { kty: "OKP" },
        githubContext: GITHUB_CONTEXT,
        nowMs: SCHEDULED_TIME + 1,
        fetchImpl,
      }),
    ).rejects.toThrow("PROVENANCE_REJECTED:WATCHDOG_URL_INVALID");
    expect(fetchImpl).not.toHaveBeenCalled();
  });

  it("requires GitHub to verify the assertion and the receipt before returning the target date", async () => {
    const { privateKeyJwk, publicKeyJwk } = await signingKeys();
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 23 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: SCHEDULED_TIME,
      jti: JTI,
    });
    const receipt = await createReceipt({
      privateKeyJwk,
      assertionPayload: assertion.payload,
      githubContext: GITHUB_CONTEXT,
      redeemedAtMs: SCHEDULED_TIME + 1,
      receiptId: "receipt-1",
    });
    const fetchImpl = vi
      .fn()
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({ assertion_jws: assertion.jws, assertion_payload: assertion.payload }),
          { status: 200 },
        ),
      )
      .mockResolvedValueOnce(new Response(JSON.stringify(receipt), { status: 200 }));

    await expect(
      redeemWorkflowProvenance({
        handoffId: JTI,
        oidcToken: "github-oidc-token",
        watchdogUrl: "https://watchdog.example",
        publicKeyJwk,
        githubContext: GITHUB_CONTEXT,
        nowMs: SCHEDULED_TIME + 1,
        fetchImpl,
      }),
    ).resolves.toMatchObject({
      targetDate: "2026-07-14",
      receiptSignature: receipt.receipt_signature,
    });
    expect(fetchImpl).toHaveBeenCalledTimes(2);
    expect(new URL(fetchImpl.mock.calls[0][0]).pathname).toBe(`/v1/handoffs/${JTI}/assertion`);
    expect(new URL(fetchImpl.mock.calls[1][0]).pathname).toBe(`/v1/handoffs/${JTI}/redeem`);
    expect(JSON.parse(fetchImpl.mock.calls[1][1].body)).toMatchObject({ jti: JTI });
  });
});
