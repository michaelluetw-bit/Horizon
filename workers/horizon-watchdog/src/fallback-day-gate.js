import { DurableObject } from "cloudflare:workers";

const TARGET_DATE_PATTERN = /^\d{4}-\d{2}-\d{2}$/;

function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
}

export class FallbackDayGate extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    this.ctx.storage.sql.exec(`
      CREATE TABLE IF NOT EXISTS fallback_day_claim (
        singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
        target_date TEXT NOT NULL,
        state TEXT NOT NULL
      )
    `);
  }

  async fetch(request) {
    if (request.method !== "POST" || new URL(request.url).pathname !== "/claim") {
      return jsonResponse({ reason: "NOT_FOUND" }, 404);
    }
    const payload = await request.json().catch(() => null);
    if (!TARGET_DATE_PATTERN.test(payload?.target_date ?? "")) {
      return jsonResponse({ reason: "INVALID_REQUEST" }, 400);
    }
    const claimed = this.ctx.storage.transactionSync(() => {
      const existing = this.ctx.storage.sql.exec(
        "SELECT target_date FROM fallback_day_claim WHERE singleton = 1",
      ).toArray()[0];
      if (existing) return false;
      const write = this.ctx.storage.sql.exec(
        "INSERT INTO fallback_day_claim (singleton, target_date, state) VALUES (1, ?, 'CLAIMED')",
        payload.target_date,
      );
      if (write.rowsWritten !== 1) throw new Error("FALLBACK_DAY_CLAIM_FAILED");
      return true;
    });
    if (!claimed) return jsonResponse({ reason: "FALLBACK_DAY_ALREADY_CLAIMED" }, 409);
    return jsonResponse({ state: "CLAIMED", target_date: payload.target_date }, 201);
  }
}
