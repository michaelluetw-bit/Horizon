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
    this.ctx.storage.sql.exec(`
      CREATE TABLE IF NOT EXISTS watchdog_audit (
        scheduled_time INTEGER PRIMARY KEY,
        target_date TEXT NOT NULL,
        record_json TEXT NOT NULL
      )
    `);
  }

  async fetch(request) {
    const url = new URL(request.url);
    if (request.method === "POST" && url.pathname === "/claim") {
      return this.claim(request);
    }
    if (request.method === "POST" && url.pathname === "/audit") {
      return this.storeAudit(request);
    }
    if (request.method === "GET" && url.pathname === "/audit") {
      return this.readAudit(url.searchParams.get("target_date"));
    }
    return jsonResponse({ reason: "NOT_FOUND" }, 404);
  }

  async claim(request) {
    const payload = await request.json().catch(() => null);
    if (!TARGET_DATE_PATTERN.test(payload?.target_date ?? "")) {
      return jsonResponse({ reason: "INVALID_REQUEST" }, 400);
    }
    const claimed = this.ctx.storage.transactionSync(() => {
      const existing = this.ctx.storage.sql
        .exec("SELECT target_date FROM fallback_day_claim WHERE singleton = 1")
        .toArray()[0];
      if (existing) return false;
      const write = this.ctx.storage.sql.exec(
        "INSERT INTO fallback_day_claim (singleton, target_date, state) VALUES (1, ?, 'CLAIMED')",
        payload.target_date,
      );
      if (write.rowsWritten !== 1) throw new Error("FALLBACK_DAY_CLAIM_FAILED");
      return true;
    });
    if (!claimed)
      return jsonResponse({ reason: "FALLBACK_DAY_ALREADY_CLAIMED" }, 409);
    return jsonResponse(
      { state: "CLAIMED", target_date: payload.target_date },
      201,
    );
  }

  async storeAudit(request) {
    const payload = await request.json().catch(() => null);
    const targetDate = payload?.target_date ?? "";
    const record = payload?.record;
    if (
      !TARGET_DATE_PATTERN.test(targetDate) ||
      !record ||
      typeof record !== "object" ||
      Array.isArray(record) ||
      record.target_date !== targetDate ||
      !Number.isInteger(record.scheduled_time) ||
      typeof record.decision !== "string" ||
      !record.decision
    ) {
      return jsonResponse({ reason: "INVALID_REQUEST" }, 400);
    }
    const recordJson = JSON.stringify(record);
    if (new TextEncoder().encode(recordJson).byteLength > 32_768) {
      return jsonResponse({ reason: "INVALID_REQUEST" }, 400);
    }

    const stored = this.ctx.storage.transactionSync(() => {
      const existing = this.ctx.storage.sql
        .exec(
          "SELECT record_json FROM watchdog_audit WHERE scheduled_time = ?",
          record.scheduled_time,
        )
        .toArray()[0];
      if (existing)
        return existing.record_json === recordJson ? "EXISTING" : "CONFLICT";
      const write = this.ctx.storage.sql.exec(
        "INSERT INTO watchdog_audit (scheduled_time, target_date, record_json) VALUES (?, ?, ?)",
        record.scheduled_time,
        targetDate,
        recordJson,
      );
      if (write.rowsWritten !== 1)
        throw new Error("WATCHDOG_AUDIT_WRITE_FAILED");
      return "CREATED";
    });
    if (stored === "CONFLICT")
      return jsonResponse({ reason: "WATCHDOG_AUDIT_CONFLICT" }, 409);
    return jsonResponse(
      { state: "STORED", target_date: targetDate },
      stored === "CREATED" ? 201 : 200,
    );
  }

  readAudit(targetDate) {
    if (!TARGET_DATE_PATTERN.test(targetDate ?? "")) {
      return jsonResponse({ reason: "INVALID_REQUEST" }, 400);
    }
    const rows = this.ctx.storage.sql
      .exec(
        "SELECT target_date, record_json FROM watchdog_audit WHERE target_date = ? ORDER BY scheduled_time",
        targetDate,
      )
      .toArray();
    let records;
    try {
      records = rows.map((row) => JSON.parse(row.record_json));
    } catch {
      return jsonResponse({ reason: "WATCHDOG_AUDIT_INVALID" }, 500);
    }
    return jsonResponse({ target_date: targetDate, records });
  }
}
