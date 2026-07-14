import { env } from "cloudflare:workers";
import { describe, expect, it } from "vitest";

function claimRequest(targetDate) {
  return new Request("https://gate.internal/claim", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ target_date: targetDate }),
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
});
