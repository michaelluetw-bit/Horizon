export const WORKFLOW_FILE = "horizon_daily.yml";
export const WORKFLOW_PATH = ".github/workflows/horizon_daily.yml";
export const HORIZON_REPOSITORY = "michaelluetw-bit/Horizon";
export const FALLBACK_LABEL = "fallback-watchdog";
export const GITHUB_API_HEADERS = {
  Accept: "application/vnd.github+json",
  "X-GitHub-Api-Version": "2026-03-10",
  "User-Agent": "horizon-watchdog/1.0",
};

function asSecondPrecisionIso(date) {
  return date.toISOString().replace(".000", "");
}

export function taipeiCreatedRange(targetDate) {
  const startsAt = new Date(`${targetDate}T00:00:00+08:00`);
  const endsAt = new Date(startsAt.getTime() + 24 * 60 * 60 * 1000);
  const start = asSecondPrecisionIso(startsAt);
  const end = asSecondPrecisionIso(endsAt);
  return { start, end, query: `${start}..${end}` };
}

export function workflowRunsUrl({ event, targetDate, page = 1 }) {
  const range = taipeiCreatedRange(targetDate);
  const url = new URL(
    `https://api.github.com/repos/${HORIZON_REPOSITORY}/actions/workflows/${WORKFLOW_FILE}/runs`,
  );
  url.search = new URLSearchParams({
    event,
    branch: "main",
    created: range.query,
    per_page: "100",
    page: String(page),
  }).toString();
  return url.toString();
}

export async function listWorkflowRuns({ fetchImpl, event, targetDate }) {
  const runs = [];
  let page = 1;
  let totalCount;

  while (totalCount === undefined || runs.length < totalCount) {
    const response = await fetchImpl(workflowRunsUrl({ event, targetDate, page }), {
      headers: GITHUB_API_HEADERS,
    });
    if (!response.ok) {
      throw new Error("WORKFLOW_RUNS_QUERY_FAILED");
    }

    let payload;
    try {
      payload = await response.json();
    } catch {
      throw new Error("WORKFLOW_RUNS_QUERY_INVALID");
    }
    if (
      !Number.isInteger(payload?.total_count) ||
      payload.total_count < 0 ||
      !Array.isArray(payload.workflow_runs) ||
      payload.workflow_runs.length > 100
    ) {
      throw new Error("WORKFLOW_RUNS_QUERY_INVALID");
    }
    if (totalCount === undefined) {
      totalCount = payload.total_count;
    } else if (payload.total_count !== totalCount) {
      throw new Error("WORKFLOW_RUNS_QUERY_INVALID");
    }

    runs.push(...payload.workflow_runs);
    if (runs.length > totalCount || (runs.length < totalCount && payload.workflow_runs.length === 0)) {
      throw new Error("WORKFLOW_RUNS_QUERY_INVALID");
    }
    page += 1;
  }

  return runs;
}

function workflowDispatchUrl() {
  return `https://api.github.com/repos/${HORIZON_REPOSITORY}/actions/workflows/${WORKFLOW_FILE}/dispatches`;
}

function matchesRunUrl(value, expectedOrigin, expectedPath, workflowRunId) {
  try {
    const url = new URL(value);
    return (
      url.protocol === "https:" &&
      url.origin === expectedOrigin &&
      url.pathname === `${expectedPath}/${workflowRunId}` &&
      url.search === "" &&
      url.hash === ""
    );
  } catch {
    return false;
  }
}

function validDispatchPayload(payload) {
  const workflowRunId = payload?.workflow_run_id;
  if (!Number.isInteger(workflowRunId) || workflowRunId <= 0) {
    return false;
  }
  return (
    matchesRunUrl(
      payload.run_url,
      "https://api.github.com",
      `/repos/${HORIZON_REPOSITORY}/actions/runs`,
      workflowRunId,
    ) &&
    matchesRunUrl(
      payload.html_url,
      "https://github.com",
      `/${HORIZON_REPOSITORY}/actions/runs`,
      workflowRunId,
    )
  );
}

export async function dispatchWatchdogFallback({ fetchImpl, token, targetDate, handoffId }) {
  const response = await fetchImpl(workflowDispatchUrl(), {
    method: "POST",
    headers: {
      ...GITHUB_API_HEADERS,
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      ref: "main",
      return_run_details: true,
      inputs: {
        trigger_source: "fallback-watchdog",
        target_date: targetDate,
        handoff_id: handoffId,
      },
    }),
  });

  if (response.status !== 200) {
    return {
      decision: response.status === 204 ? "DISPATCH_ACCEPTED_WITHOUT_PROVENANCE" : "DISPATCH_FAILED",
      httpStatus: response.status,
      mayRetry: false,
    };
  }

  let payload;
  try {
    payload = await response.json();
  } catch {
    return { decision: "DISPATCH_RESPONSE_INVALID", httpStatus: response.status, mayRetry: false };
  }
  if (!validDispatchPayload(payload)) {
    return { decision: "DISPATCH_RESPONSE_INVALID", httpStatus: response.status, mayRetry: false };
  }
  return {
    decision: "DISPATCH_CONFIRMED",
    httpStatus: response.status,
    workflowRunId: payload.workflow_run_id,
    runUrl: payload.run_url,
    htmlUrl: payload.html_url,
  };
}

function isVerifiedWorkflowRun(run, event, range) {
  const createdAt = Date.parse(run.created_at);
  const rangeStart = Date.parse(range.start);
  const rangeEnd = Date.parse(range.end);
  const workflowPathMatches =
    run.path === WORKFLOW_PATH || run.path === `${WORKFLOW_PATH}@refs/heads/main`;

  return (
    Number.isInteger(run.id) &&
    run.id > 0 &&
    run.event === event &&
    run.head_branch === "main" &&
    workflowPathMatches &&
    Number.isFinite(createdAt) &&
    createdAt >= rangeStart &&
    createdAt < rangeEnd
  );
}

export function decidePrimaryRuns(runs, range) {
  if (!Array.isArray(runs) || !runs.every((run) => isVerifiedWorkflowRun(run, "schedule", range))) {
    return {
      decision: "CHECK_FAILED",
      reason: "PRIMARY_QUERY_INVALID",
      mayDispatch: false,
    };
  }

  if (runs.length > 1) {
    return {
      decision: "CHECK_FAILED",
      reason: "PRIMARY_NOT_UNIQUE",
      mayDispatch: false,
    };
  }

  if (runs.length === 1) {
    return {
      decision: "PRIMARY_PRESENT",
      mayDispatch: false,
      primaryRunId: runs[0].id,
    };
  }

  return { decision: "PRIMARY_MISSING", mayDispatch: true };
}

export function decideFallbackRuns(runs, range) {
  if (!Array.isArray(runs) || runs.some((run) => typeof run.name !== "string")) {
    return { decision: "CHECK_FAILED", reason: "FALLBACK_QUERY_INVALID", mayDispatch: false };
  }
  const candidates = runs.filter((run) => run.name.includes(FALLBACK_LABEL));
  if (!candidates.every((run) => isVerifiedWorkflowRun(run, "workflow_dispatch", range))) {
    return { decision: "CHECK_FAILED", reason: "FALLBACK_QUERY_INVALID", mayDispatch: false };
  }
  if (candidates.length > 1) {
    return { decision: "CHECK_FAILED", reason: "FALLBACK_NOT_UNIQUE", mayDispatch: false };
  }
  if (candidates.length === 1) {
    return { decision: "FALLBACK_ALREADY_REQUESTED", mayDispatch: false, workflowRunId: candidates[0].id };
  }
  return { decision: "FALLBACK_NOT_REQUESTED", mayDispatch: true };
}
