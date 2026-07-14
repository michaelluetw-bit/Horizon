import { DurableObject } from "cloudflare:workers";

function jsonResponse(payload, status = 200) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
}

function isPositiveInteger(value) {
  return Number.isInteger(value) && value > 0;
}

function oneRow(cursor) {
  return cursor.toArray()[0] ?? null;
}

function parsePayload(request) {
  return request.json().catch(() => null);
}

export class HandoffRegistry extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    this.ctx.storage.sql.exec(`
      CREATE TABLE IF NOT EXISTS handoff (
        singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
        jti TEXT NOT NULL,
        state TEXT NOT NULL,
        assertion_jws TEXT NOT NULL,
        assertion_payload TEXT NOT NULL,
        expected_github_run_id INTEGER,
        expected_github_run_attempt INTEGER,
        github_metadata TEXT,
        receipt_jws TEXT,
        receipt_payload TEXT
      )
    `);
  }

  row() {
    return oneRow(this.ctx.storage.sql.exec("SELECT * FROM handoff WHERE singleton = 1"));
  }

  async fetch(request) {
    const { pathname } = new URL(request.url);
    if (request.method !== "POST") {
      return jsonResponse({ reason: "METHOD_NOT_ALLOWED" }, 405);
    }
    const payload = await parsePayload(request);
    if (!payload) {
      return jsonResponse({ reason: "INVALID_REQUEST" }, 400);
    }
    if (pathname === "/initialize") {
      return this.initialize(payload);
    }
    if (pathname === "/arm") {
      return this.arm(payload);
    }
    if (pathname === "/assertion") {
      return this.assertion(payload);
    }
    if (pathname === "/redeem") {
      return this.redeem(payload);
    }
    return jsonResponse({ reason: "NOT_FOUND" }, 404);
  }

  initialize(payload) {
    if (
      typeof payload.jti !== "string" ||
      typeof payload.assertion_jws !== "string" ||
      !payload.assertion_payload ||
      payload.assertion_payload.jti !== payload.jti
    ) {
      return jsonResponse({ reason: "INVALID_REQUEST" }, 400);
    }

    const result = this.ctx.storage.transactionSync(() => {
      if (this.row()) {
        return { created: false };
      }
      const write = this.ctx.storage.sql.exec(
        `INSERT INTO handoff (singleton, jti, state, assertion_jws, assertion_payload)
         VALUES (1, ?, 'PENDING_DISPATCH', ?, ?)`,
        payload.jti,
        payload.assertion_jws,
        JSON.stringify(payload.assertion_payload),
      );
      if (write.rowsWritten !== 1) {
        throw new Error("HANDOFF_INITIALIZATION_FAILED");
      }
      return { created: true };
    });
    if (!result.created) {
      return jsonResponse({ reason: "JTI_ALREADY_EXISTS" }, 409);
    }
    return jsonResponse({ state: "PENDING_DISPATCH" }, 201);
  }

  arm(payload) {
    if (!isPositiveInteger(payload.github_run_id) || payload.github_run_attempt !== 1) {
      return jsonResponse({ reason: "INVALID_RUN_BINDING" }, 400);
    }
    const result = this.ctx.storage.transactionSync(() => {
      const write = this.ctx.storage.sql.exec(
        `UPDATE handoff
         SET state = 'ARMED', expected_github_run_id = ?, expected_github_run_attempt = ?
         WHERE singleton = 1
           AND state = 'PENDING_DISPATCH'
           AND expected_github_run_id IS NULL
           AND expected_github_run_attempt IS NULL`,
        payload.github_run_id,
        payload.github_run_attempt,
      );
      return write.rowsWritten === 1;
    });
    if (!result) {
      return jsonResponse({ reason: "HANDOFF_NOT_ARMED" }, 409);
    }
    return jsonResponse({
      state: "ARMED",
      expected_github_run_id: payload.github_run_id,
      expected_github_run_attempt: payload.github_run_attempt,
    });
  }

  assertion(payload) {
    const row = this.row();
    if (!row || row.state !== "ARMED") {
      return jsonResponse({ reason: "HANDOFF_NOT_ARMED" }, 409);
    }
    if (
      payload.github_run_id !== row.expected_github_run_id ||
      payload.github_run_attempt !== row.expected_github_run_attempt
    ) {
      return jsonResponse({ reason: "GITHUB_RUN_BINDING_MISMATCH" }, 409);
    }
    return jsonResponse({
      assertion_jws: row.assertion_jws,
      assertion_payload: JSON.parse(row.assertion_payload),
    });
  }

  redeem(payload) {
    if (
      !isPositiveInteger(payload.github_run_id) ||
      payload.github_run_attempt !== 1 ||
      !payload.github_metadata ||
      typeof payload.receipt_jws !== "string" ||
      !payload.receipt_payload
    ) {
      return jsonResponse({ reason: "INVALID_REDEMPTION_REQUEST" }, 400);
    }
    const result = this.ctx.storage.transactionSync(() => {
      const row = this.row();
      if (!row || row.state === "PENDING_DISPATCH") {
        return { ok: false, reason: "HANDOFF_NOT_ARMED" };
      }
      if (row.state === "REDEEMED") {
        return { ok: false, reason: "JTI_ALREADY_REDEEMED" };
      }
      if (
        row.expected_github_run_id !== payload.github_run_id ||
        row.expected_github_run_attempt !== payload.github_run_attempt
      ) {
        return { ok: false, reason: "GITHUB_RUN_BINDING_MISMATCH" };
      }
      const write = this.ctx.storage.sql.exec(
        `UPDATE handoff
         SET state = 'REDEEMED', github_metadata = ?, receipt_jws = ?, receipt_payload = ?
         WHERE singleton = 1
           AND state = 'ARMED'
           AND expected_github_run_id = ?
           AND expected_github_run_attempt = ?`,
        JSON.stringify(payload.github_metadata),
        payload.receipt_jws,
        JSON.stringify(payload.receipt_payload),
        payload.github_run_id,
        payload.github_run_attempt,
      );
      if (write.rowsWritten !== 1) {
        return { ok: false, reason: "ATOMIC_REDEMPTION_FAILED" };
      }
      return { ok: true };
    });
    if (!result.ok) {
      return jsonResponse({ reason: result.reason }, 409);
    }
    return jsonResponse({
      state: "REDEEMED",
      receipt_jws: payload.receipt_jws,
      receipt_payload: payload.receipt_payload,
    });
  }
}
