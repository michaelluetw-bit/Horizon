import { env } from "cloudflare:workers";
import { describe, expect, it } from "vitest";

const JTI = "C".repeat(43);

function request(path, method, payload) {
  return new Request(`https://handoff.internal${path}`, {
    method,
    headers: { "Content-Type": "application/json" },
    body: payload === undefined ? undefined : JSON.stringify(payload),
  });
}

describe("HandoffRegistry", () => {
  it("atomically binds one jti to the dispatched run and consumes it only once", async () => {
    const id = env.HANDOFF_REGISTRY.idFromName(JTI);
    const stub = env.HANDOFF_REGISTRY.get(id);

    const initialized = await stub.fetch(
      request("/initialize", "POST", {
        jti: JTI,
        assertion_jws: "assertion-jws",
        assertion_payload: { jti: JTI, target_date: "2026-07-14" },
      }),
    );
    expect(initialized.status).toBe(201);

    const armed = await stub.fetch(
      request("/arm", "POST", { github_run_id: 12345, github_run_attempt: 1 }),
    );
    expect(armed.status).toBe(200);
    expect(await armed.json()).toMatchObject({
      state: "ARMED",
      expected_github_run_id: 12345,
      expected_github_run_attempt: 1,
    });

    const assertion = await stub.fetch(
      request("/assertion", "POST", { github_run_id: 12345, github_run_attempt: 1 }),
    );
    expect(assertion.status).toBe(200);
    expect(await assertion.json()).toMatchObject({ assertion_jws: "assertion-jws" });

    const redeemed = await stub.fetch(
      request("/redeem", "POST", {
        github_run_id: 12345,
        github_run_attempt: 1,
        github_metadata: {
          repository: "michaelluetw-bit/Horizon",
          workflow_ref:
            "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
          commit_sha: "a".repeat(40),
          event_name: "workflow_dispatch",
        },
        receipt_jws: "receipt-jws",
        receipt_payload: { receipt_id: "receipt-1", jti: JTI, github_run_id: 12345 },
      }),
    );
    expect(redeemed.status).toBe(200);
    expect(await redeemed.json()).toMatchObject({ state: "REDEEMED", receipt_jws: "receipt-jws" });

    const replay = await stub.fetch(
      request("/redeem", "POST", {
        github_run_id: 12345,
        github_run_attempt: 1,
        github_metadata: {},
        receipt_jws: "different-receipt",
        receipt_payload: {},
      }),
    );
    expect(replay.status).toBe(409);
    expect(await replay.json()).toMatchObject({ reason: "JTI_ALREADY_REDEEMED" });
  });
});
