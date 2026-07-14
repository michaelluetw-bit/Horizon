export const WATCHDOG_CRON = "0 22 * * *";
export const MAX_INVOCATION_LAG_MS = 300_000;

export function targetDateForTaipei(epochMilliseconds) {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Taipei",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(new Date(epochMilliseconds));
  const values = Object.fromEntries(
    parts.filter(({ type }) => type !== "literal").map(({ type, value }) => [type, value]),
  );
  return `${values.year}-${values.month}-${values.day}`;
}

function watchdogScheduledTime(targetDate) {
  return Date.parse(`${targetDate}T06:00:00+08:00`);
}

function isInsideWatchdogObservationWindow(targetDate, epochMilliseconds) {
  const startsAt = Date.parse(`${targetDate}T05:55:00+08:00`);
  const endsAt = Date.parse(`${targetDate}T06:05:00+08:00`);
  return epochMilliseconds >= startsAt && epochMilliseconds <= endsAt;
}

function rejected({ decision, reason, targetDate, invocationDeltaMs }) {
  return {
    accepted: false,
    decision,
    reason,
    mayQueryGithub: false,
    targetDate,
    invocationDeltaMs,
  };
}

export function validateScheduledInvocation({ controllerCron, scheduledTime, invocationStartedAt }) {
  if (!Number.isInteger(scheduledTime)) {
    return rejected({
      decision: "CHECK_FAILED",
      reason: "SCHEDULED_TIME_INVALID",
      targetDate: null,
      invocationDeltaMs: null,
    });
  }
  const targetDate = targetDateForTaipei(scheduledTime);

  if (controllerCron !== WATCHDOG_CRON) {
    return rejected({
      decision: "CHECK_FAILED",
      reason: "WATCHDOG_CRON_MISMATCH",
      targetDate,
      invocationDeltaMs: Number.isInteger(invocationStartedAt) ? invocationStartedAt - scheduledTime : null,
    });
  }

  if (!Number.isInteger(invocationStartedAt)) {
    return rejected({
      decision: "STALE_SCHEDULED_INVOCATION",
      reason: "INVOCATION_TIME_INVALID",
      targetDate,
      invocationDeltaMs: null,
    });
  }
  const invocationDeltaMs = invocationStartedAt - scheduledTime;

  if (Math.abs(scheduledTime - watchdogScheduledTime(targetDate)) > MAX_INVOCATION_LAG_MS) {
    return rejected({
      decision: "CHECK_FAILED",
      reason: "WATCHDOG_SCHEDULE_TIME_INVALID",
      targetDate,
      invocationDeltaMs,
    });
  }

  if (invocationDeltaMs < 0 || invocationDeltaMs > MAX_INVOCATION_LAG_MS) {
    return rejected({
      decision: "STALE_SCHEDULED_INVOCATION",
      reason: "INVOCATION_LAG_OUT_OF_RANGE",
      targetDate,
      invocationDeltaMs,
    });
  }

  if (!isInsideWatchdogObservationWindow(targetDate, invocationStartedAt)) {
    return rejected({
      decision: "STALE_SCHEDULED_INVOCATION",
      reason: "INVOCATION_TIME_INVALID",
      targetDate,
      invocationDeltaMs,
    });
  }

  return {
    accepted: true,
    decision: "READY",
    mayQueryGithub: true,
    targetDate,
    invocationDeltaMs,
  };
}
