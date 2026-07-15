import { SELF } from "cloudflare:test";
import { env } from "cloudflare:workers";
import { describe, expect, it } from "vitest";

function claimRequest(targetDate) {
  return new Request("https://gate.internal/claim", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ target_date: targetDate }),
  });
}

function auditRequest(record) {
  return new Request("https://gate.internal/audit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ target_date: record.target_date, record }),
  });
}

describe("FallbackDayGate", () => {
  it("atomically allows only the first fallback claim for a Taipei target date", async () => {
    const stub = env.FALLBACK_DAY_GATE.get(env.FALLBACK_DAY_GATE.idFromName("2026-07-14"));

    const first = await stub.fetch(claimRequest("2026-07-14"));
    const second = await stub.fetch(claimRequest("2026-07-14"));

    expect(first.status).toBe(201);
    await expect(first.json()).resolves.toEqual({ state: "CLAIMED", target_date: "2026-07-14" });
    expect(second.status).toBe(409);
    await expect(second.json()).resolves.toEqual({ reason: "FALLBACK_DAY_ALREADY_CLAIMED" });
  });

  it("persists a sanitized scheduled decision and exposes it by exact target date", async () => {
    const targetDate = "2026-07-16";
    const record = {
      target_date: targetDate,
      scheduled_time: Date.parse("2026-07-16T01:30:00.000Z"),
      trigger_schedule_expression: "30 1 16 7 *",
      invocation_started_at: Date.parse("2026-07-16T01:30:01.000Z"),
      invocation_delta_ms: 1_000,
      execution_mode: "verification",
      decision: "PRIMARY_PRESENT",
      primary_run_id: 67890,
      worker_version_id: "version-1",
    };
    const stub = env.FALLBACK_DAY_GATE.get(
      env.FALLBACK_DAY_GATE.idFromName(targetDate),
    );

    const stored = await stub.fetch(auditRequest(record));
    expect(stored.status).toBe(201);

    const publicResponse = await SELF.fetch(
      `https://watchdog.example/v1/audits/${targetDate}`,
    );
    expect(publicResponse.status).toBe(200);
    await expect(publicResponse.json()).resolves.toEqual({
      target_date: targetDate,
      records: [record],
    });
  });
});
