import { describe, expect, it } from "vitest";

import { prepareProvenance } from "../src/github-provenance-core.js";

const SHA = "a".repeat(40);
const WORKFLOW_REF = "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main";

function environment(overrides = {}) {
  return {
    GITHUB_RUN_ID: "123456",
    GITHUB_RUN_ATTEMPT: "1",
    GITHUB_SHA: SHA,
    GITHUB_REPOSITORY: "michaelluetw-bit/Horizon",
    HORIZON_GITHUB_WORKFLOW_REF: WORKFLOW_REF,
    GITHUB_EVENT_NAME: "schedule",
    GITHUB_ACTOR: "horizon-maintainer",
    HORIZON_TRIGGER_SOURCE: "",
    HORIZON_HANDOFF_ID: "",
    HORIZON_TARGET_DATE: "",
    ...overrides,
  };
}

describe("GitHub workflow provenance routing", () => {
  it("uses the actual schedule event for primary provenance", async () => {
    const provenance = await prepareProvenance({
      env: environment(),
      nowMs: Date.parse("2026-07-13T21:17:00Z"),
    });

    expect(provenance).toMatchObject({
      trigger_source: "primary",
      trigger_event: "schedule",
      trigger_schedule_expression: "17 21 * * *",
      target_date: "2026-07-14",
      primary_schedule_on_time: true,
    });
  });

  it("records a delayed schedule as delivered but not on-time primary evidence", async () => {
    const provenance = await prepareProvenance({
      env: environment(),
      nowMs: Date.parse("2026-07-14T01:10:00Z"),
    });

    expect(provenance).toMatchObject({
      trigger_source: "primary",
      target_date: "2026-07-14",
      primary_schedule_on_time: false,
    });
  });

  it("uses the captured workflow entry time for primary on-time evidence", async () => {
    const provenance = await prepareProvenance({
      env: environment(),
      nowMs: Date.parse("2026-07-13T21:22:01Z"),
      primaryStartedAtMs: Date.parse("2026-07-13T21:21:59Z"),
    });

    expect(provenance).toMatchObject({
      trigger_source: "primary",
      target_date: "2026-07-14",
      primary_schedule_on_time: true,
    });
  });

  it("rejects a manual dispatch that only claims to be the watchdog", async () => {
    await expect(
      prepareProvenance({
        env: environment({
          GITHUB_EVENT_NAME: "workflow_dispatch",
          HORIZON_TRIGGER_SOURCE: "fallback-watchdog",
        }),
        nowMs: Date.parse("2026-07-13T22:00:00Z"),
      }),
    ).rejects.toThrow("PROVENANCE_REJECTED:WATCHDOG_INPUT_INVALID");
  });

  it("rejects a manual dispatch that supplies a handoff ID without valid watchdog provenance", async () => {
    await expect(
      prepareProvenance({
        env: environment({
          GITHUB_EVENT_NAME: "workflow_dispatch",
          HORIZON_HANDOFF_ID: "h".repeat(43),
        }),
        nowMs: Date.parse("2026-07-13T22:00:00Z"),
      }),
    ).rejects.toThrow("PROVENANCE_REJECTED:WATCHDOG_INPUT_INVALID");
  });

  it("accepts a watchdog run only when redemption returns the signed target date", async () => {
    const handoffId = "h".repeat(43);
    const redeemed = {
      targetDate: "2026-07-14",
      receiptSignature: "signed-receipt",
      receiptPayload: {
        jti: handoffId,
        controller_cron: "0 22 * * *",
        controller_scheduled_time: 1783970400000,
        target_date: "2026-07-14",
        github_run_id: 123456,
        github_run_attempt: 1,
        repository: "michaelluetw-bit/Horizon",
        workflow_ref: WORKFLOW_REF,
        commit_sha: SHA,
        redeemed_at: 1783970460,
        receipt_id: "r".repeat(43),
        provenance_verification_status: "verified",
      },
    };
    const redeemImpl = async (arguments_) => {
      expect(arguments_.handoffId).toBe(handoffId);
      expect(arguments_.githubContext.github_run_id).toBe(123456);
      return redeemed;
    };

    const provenance = await prepareProvenance({
      env: environment({
        GITHUB_EVENT_NAME: "workflow_dispatch",
        HORIZON_TRIGGER_SOURCE: "fallback-watchdog",
        HORIZON_HANDOFF_ID: handoffId,
        HORIZON_TARGET_DATE: "2026-07-14",
        HORIZON_WATCHDOG_URL: "https://watchdog.example.invalid",
        HORIZON_WATCHDOG_PUBLIC_KEY_JWK: JSON.stringify({ kty: "OKP" }),
      }),
      nowMs: Date.parse("2026-07-13T22:00:00Z"),
      requestOidcTokenImpl: async () => "oidc-token",
      redeemImpl,
    });

    expect(provenance).toMatchObject({
      trigger_source: "watchdog",
      trigger_event: "workflow_dispatch",
      target_date: "2026-07-14",
      receipt_signature: "signed-receipt",
    });
  });
});
