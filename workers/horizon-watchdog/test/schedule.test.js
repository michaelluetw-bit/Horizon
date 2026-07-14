import { describe, expect, it } from "vitest";

import { validateScheduledInvocation } from "../src/contracts.js";

describe("validateScheduledInvocation", () => {
  it("uses Cloudflare scheduledTime to derive the Taipei target date", () => {
    const scheduledTime = Date.parse("2026-07-13T22:00:00.000Z");

    expect(
      validateScheduledInvocation({
        controllerCron: "0 22 * * *",
        scheduledTime,
        invocationStartedAt: scheduledTime + 300_000,
      }),
    ).toEqual({
      accepted: true,
      decision: "READY",
      mayQueryGithub: true,
      targetDate: "2026-07-14",
      invocationDeltaMs: 300_000,
    });
  });

  it("fails closed before any GitHub read when Cloudflare reports another cron", () => {
    const scheduledTime = Date.parse("2026-07-13T22:00:00.000Z");

    expect(
      validateScheduledInvocation({
        controllerCron: "17 21 * * *",
        scheduledTime,
        invocationStartedAt: scheduledTime,
      }),
    ).toMatchObject({
      accepted: false,
      decision: "CHECK_FAILED",
      reason: "WATCHDOG_CRON_MISMATCH",
      mayQueryGithub: false,
      targetDate: "2026-07-14",
    });
  });

  it("fails closed when the platform timestamp is not an integer epoch milliseconds value", () => {
    expect(
      validateScheduledInvocation({
        controllerCron: "0 22 * * *",
        scheduledTime: Number.NaN,
        invocationStartedAt: Date.parse("2026-07-13T22:00:00.000Z"),
      }),
    ).toMatchObject({
      accepted: false,
      decision: "CHECK_FAILED",
      reason: "SCHEDULED_TIME_INVALID",
      mayQueryGithub: false,
    });
  });

  it.each([
    [
      "scheduledTime is later than the approved five-minute window",
      Date.parse("2026-07-13T22:05:00.001Z"),
      Date.parse("2026-07-13T22:05:00.001Z"),
      "CHECK_FAILED",
      "WATCHDOG_SCHEDULE_TIME_INVALID",
    ],
    [
      "the handler starts before the Cloudflare scheduled time",
      Date.parse("2026-07-13T22:00:00.000Z"),
      Date.parse("2026-07-13T21:59:59.999Z"),
      "STALE_SCHEDULED_INVOCATION",
      "INVOCATION_LAG_OUT_OF_RANGE",
    ],
    [
      "the handler starts one millisecond beyond the maximum lag",
      Date.parse("2026-07-13T22:00:00.000Z"),
      Date.parse("2026-07-13T22:05:00.001Z"),
      "STALE_SCHEDULED_INVOCATION",
      "INVOCATION_LAG_OUT_OF_RANGE",
    ],
  ])("fails closed when %s", (_description, scheduledTime, invocationStartedAt, decision, reason) => {
    expect(
      validateScheduledInvocation({
        controllerCron: "0 22 * * *",
        scheduledTime,
        invocationStartedAt,
      }),
    ).toMatchObject({
      accepted: false,
      decision,
      reason,
      mayQueryGithub: false,
    });
  });

  it("fails closed when the handler itself starts after the observation window", () => {
    const scheduledTime = Date.parse("2026-07-13T22:05:00.000Z");

    expect(
      validateScheduledInvocation({
        controllerCron: "0 22 * * *",
        scheduledTime,
        invocationStartedAt: scheduledTime + 1,
      }),
    ).toMatchObject({
      accepted: false,
      decision: "STALE_SCHEDULED_INVOCATION",
      reason: "INVOCATION_TIME_INVALID",
      mayQueryGithub: false,
    });
  });
});
