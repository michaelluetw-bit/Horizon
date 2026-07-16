import { describe, expect, it, vi } from "vitest";

import {
  evaluateScheduledInvocation,
  handleHandoffRequest,
  requestContextMatchesClaims,
} from "../src/index.js";
import { createAssertion } from "../src/provenance.js";
import { verifyReceipt } from "../src/receipt.js";

const SCHEDULED_TIME = Date.parse("2026-07-13T22:00:00.000Z");

function scheduleRun({ id = 12345, createdAt = "2026-07-13T21:17:00Z" } = {}) {
  return {
    id,
    event: "schedule",
    head_branch: "main",
    path: ".github/workflows/horizon_daily.yml",
    created_at: createdAt,
  };
}

function availableDayGate() {
  const fetch = vi.fn().mockResolvedValue(
    new Response(JSON.stringify({ state: "CLAIMED", target_date: "2026-07-14" }), { status: 201 }),
  );
  return {
    binding: {
      idFromName: vi.fn(() => "day-object"),
      get: vi.fn(() => ({ fetch })),
    },
    fetch,
  };
}

describe("evaluateScheduledInvocation", () => {
  it("does not dispatch when the exact primary schedule run already exists", async () => {
    const fetchImpl = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ total_count: 1, workflow_runs: [scheduleRun()] }), { status: 200 }),
    );

    await expect(
      evaluateScheduledInvocation({
        controller: { cron: "0 22 * * *", scheduledTime: SCHEDULED_TIME },
        env: {},
        invocationStartedAt: SCHEDULED_TIME,
        fetchImpl,
      }),
    ).resolves.toMatchObject({
      decision: "PRIMARY_PRESENT",
      targetDate: "2026-07-14",
      primaryRunId: 12345,
      configured_watchdog_schedule_expression: "0 22 * * *",
      trigger_schedule_expression: "0 22 * * *",
      scheduled_time: SCHEDULED_TIME,
      invocation_started_at: SCHEDULED_TIME,
      invocation_delta_ms: 0,
      max_invocation_lag_ms: 300_000,
      api_version: "2026-03-10",
    });
    expect(fetchImpl).toHaveBeenCalledTimes(1);
  });

  it("runs a date-scoped acceptance cron in primary-read-only mode", async () => {
    const verificationCronTime = Date.parse("2026-07-16T01:30:00.000Z");
    const scheduledTime = verificationCronTime + 45_000;
    const fetchImpl = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({
          total_count: 1,
          workflow_runs: [
            scheduleRun({ id: 67890, createdAt: "2026-07-15T22:14:34Z" }),
          ],
        }),
        { status: 200 },
      ),
    );

    await expect(
      evaluateScheduledInvocation({
        controller: { cron: "30 1 16 7 *", scheduledTime },
        env: {
          HORIZON_WATCHDOG_VERIFICATION_CRON: "30 1 16 7 *",
          HORIZON_WATCHDOG_VERIFICATION_TARGET_DATE: "2026-07-16",
          CF_VERSION_METADATA: { id: "version-1" },
        },
        invocationStartedAt: scheduledTime + 1_010,
        fetchImpl,
      }),
    ).resolves.toMatchObject({
      decision: "PRIMARY_PRESENT",
      execution_mode: "verification",
      target_date: "2026-07-16",
      primary_run_id: 67890,
      trigger_schedule_expression: "30 1 16 7 *",
      worker_version_id: "version-1",
    });
    expect(fetchImpl).toHaveBeenCalledTimes(1);
  });

  it("never dispatches from an acceptance cron when the primary run is absent", async () => {
    const verificationTime = Date.parse("2026-07-16T01:30:00.000Z");
    const fetchImpl = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ total_count: 0, workflow_runs: [] }), {
        status: 200,
      }),
    );

    await expect(
      evaluateScheduledInvocation({
        controller: { cron: "30 1 16 7 *", scheduledTime: verificationTime },
        env: {
          HORIZON_WATCHDOG_VERIFICATION_CRON: "30 1 16 7 *",
          HORIZON_WATCHDOG_VERIFICATION_TARGET_DATE: "2026-07-16",
        },
        invocationStartedAt: verificationTime + 1_000,
        fetchImpl,
      }),
    ).resolves.toMatchObject({
      decision: "CHECK_FAILED",
      execution_mode: "verification",
      reason: "VERIFICATION_PRIMARY_MISSING",
      target_date: "2026-07-16",
    });
    expect(fetchImpl).toHaveBeenCalledTimes(1);
  });

  it("creates a handoff and arms only the run returned by a confirmed fallback dispatch", async () => {
    const signingKeyPair = await crypto.subtle.generateKey({ name: "Ed25519" }, true, ["sign", "verify"]);
    const privateKeyJwk = await crypto.subtle.exportKey("jwk", signingKeyPair.privateKey);
    const registryFetch = vi
      .fn()
      .mockResolvedValueOnce(new Response(JSON.stringify({ state: "PENDING_DISPATCH" }), { status: 201 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ state: "ARMED" }), { status: 200 }));
    const registry = {
      idFromName: vi.fn(() => "handoff-object"),
      get: vi.fn(() => ({ fetch: registryFetch })),
    };
    const dayGate = availableDayGate();
    const fetchImpl = vi
      .fn()
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ total_count: 0, workflow_runs: [] }), { status: 200 }),
      )
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ total_count: 0, workflow_runs: [] }), { status: 200 }),
      )
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({
            workflow_run_id: 12345,
            run_url: "https://api.github.com/repos/michaelluetw-bit/Horizon/actions/runs/12345",
            html_url: "https://github.com/michaelluetw-bit/Horizon/actions/runs/12345",
          }),
          { status: 200 },
        ),
      );

    await expect(
      evaluateScheduledInvocation({
        controller: { cron: "0 22 * * *", scheduledTime: SCHEDULED_TIME },
        env: {
          HANDOFF_REGISTRY: registry,
          FALLBACK_DAY_GATE: dayGate.binding,
          HORIZON_GITHUB_TOKEN: "test-token",
          HORIZON_ASSERTION_PRIVATE_KEY_JWK: JSON.stringify(privateKeyJwk),
        },
        invocationStartedAt: SCHEDULED_TIME,
        fetchImpl,
      }),
    ).resolves.toMatchObject({
      decision: "DISPATCH_CONFIRMED",
      targetDate: "2026-07-14",
      workflowRunId: 12345,
    });
    expect(fetchImpl).toHaveBeenCalledTimes(3);
    expect(registryFetch).toHaveBeenCalledTimes(2);
    expect(dayGate.fetch).toHaveBeenCalledTimes(1);
    expect(new URL(registryFetch.mock.calls[0][0].url).pathname).toBe("/initialize");
    expect(new URL(registryFetch.mock.calls[1][0].url).pathname).toBe("/arm");
  });

  it("records a network dispatch failure without retrying the same invocation", async () => {
    const signingKeyPair = await crypto.subtle.generateKey({ name: "Ed25519" }, true, ["sign", "verify"]);
    const privateKeyJwk = await crypto.subtle.exportKey("jwk", signingKeyPair.privateKey);
    const registryFetch = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ state: "PENDING_DISPATCH" }), { status: 201 }),
    );
    const registry = {
      idFromName: vi.fn(() => "handoff-object"),
      get: vi.fn(() => ({ fetch: registryFetch })),
    };
    const dayGate = availableDayGate();
    const fetchImpl = vi
      .fn()
      .mockResolvedValueOnce(new Response(JSON.stringify({ total_count: 0, workflow_runs: [] }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ total_count: 0, workflow_runs: [] }), { status: 200 }))
      .mockRejectedValueOnce(new Error("network unavailable"));

    await expect(
      evaluateScheduledInvocation({
        controller: { cron: "0 22 * * *", scheduledTime: SCHEDULED_TIME },
        env: {
          HANDOFF_REGISTRY: registry,
          FALLBACK_DAY_GATE: dayGate.binding,
          HORIZON_GITHUB_TOKEN: "test-token",
          HORIZON_ASSERTION_PRIVATE_KEY_JWK: JSON.stringify(privateKeyJwk),
        },
        invocationStartedAt: SCHEDULED_TIME,
        fetchImpl,
      }),
    ).resolves.toMatchObject({
      decision: "DISPATCH_FAILED",
      reason: "DISPATCH_REQUEST_FAILED",
      targetDate: "2026-07-14",
    });
    expect(fetchImpl).toHaveBeenCalledTimes(3);
    expect(registryFetch).toHaveBeenCalledTimes(1);
  });

  it("fails closed before creating a handoff when another invocation already claimed the target date", async () => {
    const fetchImpl = vi
      .fn()
      .mockResolvedValueOnce(new Response(JSON.stringify({ total_count: 0, workflow_runs: [] }), { status: 200 }))
      .mockResolvedValueOnce(new Response(JSON.stringify({ total_count: 0, workflow_runs: [] }), { status: 200 }));
    const dayGateFetch = vi.fn().mockResolvedValue(
      new Response(JSON.stringify({ reason: "FALLBACK_DAY_ALREADY_CLAIMED" }), { status: 409 }),
    );
    const dayGate = {
      idFromName: vi.fn(() => "day-object"),
      get: vi.fn(() => ({ fetch: dayGateFetch })),
    };

    await expect(
      evaluateScheduledInvocation({
        controller: { cron: "0 22 * * *", scheduledTime: SCHEDULED_TIME },
        env: { FALLBACK_DAY_GATE: dayGate },
        invocationStartedAt: SCHEDULED_TIME,
        fetchImpl,
      }),
    ).resolves.toMatchObject({
      decision: "CHECK_FAILED",
      reason: "FALLBACK_DAY_ALREADY_CLAIMED",
      targetDate: "2026-07-14",
    });
    expect(fetchImpl).toHaveBeenCalledTimes(2);
    expect(dayGateFetch).toHaveBeenCalledTimes(1);
  });
});

describe("handleHandoffRequest", () => {
  it("requires the redemption body to repeat the exact handoff jti from the route", () => {
    const claims = {
      run_id: 12345,
      run_attempt: 1,
      repository: "michaelluetw-bit/Horizon",
      workflow_ref: "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
      sha: "a".repeat(40),
      event_name: "workflow_dispatch",
    };
    const payload = {
      jti: "wrong".repeat(9),
      github_run_id: claims.run_id,
      github_run_attempt: claims.run_attempt,
      github_repository: claims.repository,
      github_workflow_ref: claims.workflow_ref,
      github_sha: claims.sha,
      github_event_name: claims.event_name,
    };

    expect(requestContextMatchesClaims(payload, claims, "F".repeat(43))).toBe(false);
  });

  it("returns an assertion only after a valid OIDC identity matches the armed run", async () => {
    const signingKeyPair = await crypto.subtle.generateKey({ name: "Ed25519" }, true, ["sign", "verify"]);
    const privateKeyJwk = await crypto.subtle.exportKey("jwk", signingKeyPair.privateKey);
    const publicKeyJwk = await crypto.subtle.exportKey("jwk", signingKeyPair.publicKey);
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 22 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: SCHEDULED_TIME,
      jti: "E".repeat(43),
    });
    const registryFetch = vi.fn().mockResolvedValue(
      new Response(
        JSON.stringify({ assertion_jws: assertion.jws, assertion_payload: assertion.payload }),
        { status: 200 },
      ),
    );
    const oidcClaims = {
      run_id: 12345,
      run_attempt: 1,
      repository: "michaelluetw-bit/Horizon",
      workflow_ref: "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
      sha: "a".repeat(40),
      event_name: "workflow_dispatch",
    };

    const response = await handleHandoffRequest({
      request: new Request(`https://watchdog.example/v1/handoffs/${"E".repeat(43)}/assertion`, {
        method: "POST",
        headers: { Authorization: "Bearer oidc-token" },
      }),
      env: {
        HANDOFF_REGISTRY: {
          idFromName: vi.fn(() => "handoff-object"),
          get: vi.fn(() => ({ fetch: registryFetch })),
        },
        HORIZON_ASSERTION_PUBLIC_KEY_JWK: JSON.stringify(publicKeyJwk),
      },
      nowMs: SCHEDULED_TIME + 1,
      fetchImpl: vi.fn(),
      verifyOidcImpl: vi.fn().mockResolvedValue({ accepted: true, claims: oidcClaims }),
    });

    expect(response.status, await response.clone().text()).toBe(200);
    await expect(response.json()).resolves.toMatchObject({ assertion_jws: assertion.jws });
    expect(registryFetch).toHaveBeenCalledTimes(1);
  });

  it("redeems the armed assertion into a receipt bound to the actual GitHub run", async () => {
    const signingKeyPair = await crypto.subtle.generateKey({ name: "Ed25519" }, true, ["sign", "verify"]);
    const privateKeyJwk = await crypto.subtle.exportKey("jwk", signingKeyPair.privateKey);
    const publicKeyJwk = await crypto.subtle.exportKey("jwk", signingKeyPair.publicKey);
    const jti = "F".repeat(43);
    const assertion = await createAssertion({
      privateKeyJwk,
      controllerCron: "0 22 * * *",
      scheduledTime: SCHEDULED_TIME,
      issuedAtMs: SCHEDULED_TIME,
      jti,
    });
    const registryFetch = vi
      .fn()
      .mockResolvedValueOnce(
        new Response(
          JSON.stringify({ assertion_jws: assertion.jws, assertion_payload: assertion.payload }),
          { status: 200 },
        ),
      )
      .mockResolvedValueOnce(new Response(JSON.stringify({ state: "REDEEMED" }), { status: 200 }));
    const oidcClaims = {
      run_id: 12345,
      run_attempt: 1,
      repository: "michaelluetw-bit/Horizon",
      workflow_ref: "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
      sha: "a".repeat(40),
      event_name: "workflow_dispatch",
    };
    const response = await handleHandoffRequest({
      request: new Request(`https://watchdog.example/v1/handoffs/${jti}/redeem`, {
        method: "POST",
        headers: { Authorization: "Bearer oidc-token", "Content-Type": "application/json" },
        body: JSON.stringify({
          jti,
          github_run_id: oidcClaims.run_id,
          github_run_attempt: oidcClaims.run_attempt,
          github_repository: oidcClaims.repository,
          github_workflow_ref: oidcClaims.workflow_ref,
          github_sha: oidcClaims.sha,
          github_event_name: oidcClaims.event_name,
        }),
      }),
      env: {
        HANDOFF_REGISTRY: {
          idFromName: vi.fn(() => "handoff-object"),
          get: vi.fn(() => ({ fetch: registryFetch })),
        },
        HORIZON_ASSERTION_PRIVATE_KEY_JWK: JSON.stringify(privateKeyJwk),
        HORIZON_ASSERTION_PUBLIC_KEY_JWK: JSON.stringify(publicKeyJwk),
      },
      nowMs: SCHEDULED_TIME + 1,
      fetchImpl: vi.fn(),
      verifyOidcImpl: vi.fn().mockResolvedValue({ accepted: true, claims: oidcClaims }),
    });

    expect(response.status, await response.clone().text()).toBe(200);
    const receipt = await response.json();
    await expect(
      verifyReceipt({
        receiptSignature: receipt.receipt_signature,
        publicKeyJwk,
        assertionPayload: assertion.payload,
        githubContext: {
          github_run_id: oidcClaims.run_id,
          github_run_attempt: oidcClaims.run_attempt,
          repository: oidcClaims.repository,
          workflow_ref: oidcClaims.workflow_ref,
          commit_sha: oidcClaims.sha,
        },
      }),
    ).resolves.toMatchObject({ accepted: true });
    expect(registryFetch).toHaveBeenCalledTimes(2);
    expect(new URL(registryFetch.mock.calls[1][0].url).pathname).toBe("/redeem");
  });
});
