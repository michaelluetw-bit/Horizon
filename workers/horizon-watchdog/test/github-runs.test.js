import { describe, expect, it, vi } from "vitest";

import {
  decidePrimaryRuns,
  dispatchWatchdogFallback,
  GITHUB_API_HEADERS,
  listWorkflowRuns,
  taipeiCreatedRange,
  workflowRunsUrl,
} from "../src/github-runs.js";

const range = {
  start: "2026-07-13T16:00:00Z",
  end: "2026-07-14T16:00:00Z",
};

function scheduledRun(id, createdAt) {
  return {
    id,
    event: "schedule",
    head_branch: "main",
    path: ".github/workflows/horizon_daily.yml",
    created_at: createdAt,
  };
}

describe("taipeiCreatedRange", () => {
  it("creates the frozen half-open UTC interval for a Taipei target date", () => {
    expect(taipeiCreatedRange("2026-07-14")).toEqual({
      start: "2026-07-13T16:00:00Z",
      end: "2026-07-14T16:00:00Z",
      query: "2026-07-13T16:00:00Z..2026-07-14T16:00:00Z",
    });
  });
});

describe("workflowRunsUrl", () => {
  it("uses the exact workflow endpoint and every frozen server-side filter", () => {
    const url = new URL(
      workflowRunsUrl({ event: "schedule", targetDate: "2026-07-14", page: 2 }),
    );

    expect(url.origin).toBe("https://api.github.com");
    expect(url.pathname).toBe(
      "/repos/michaelluetw-bit/Horizon/actions/workflows/horizon_daily.yml/runs",
    );
    expect(Object.fromEntries(url.searchParams)).toEqual({
      event: "schedule",
      branch: "main",
      created: "2026-07-13T16:00:00Z..2026-07-14T16:00:00Z",
      per_page: "100",
      page: "2",
    });
  });
});

describe("listWorkflowRuns", () => {
  it("reads every page before a primary candidate decision", async () => {
    const firstPage = Array.from({ length: 100 }, (_, index) =>
      scheduledRun(index + 1, "2026-07-13T21:17:00Z"),
    );
    const lastRun = scheduledRun(101, "2026-07-13T21:18:00Z");
    const fetchImpl = vi
      .fn()
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ total_count: 101, workflow_runs: firstPage }), { status: 200 }),
      )
      .mockResolvedValueOnce(
        new Response(JSON.stringify({ total_count: 101, workflow_runs: [lastRun] }), { status: 200 }),
      );

    await expect(
      listWorkflowRuns({ fetchImpl, event: "schedule", targetDate: "2026-07-14" }),
    ).resolves.toEqual([...firstPage, lastRun]);
    expect(fetchImpl).toHaveBeenCalledTimes(2);
    expect(new URL(fetchImpl.mock.calls[1][0]).searchParams.get("page")).toBe("2");
    expect(fetchImpl.mock.calls[0][1].headers).toMatchObject({
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2026-03-10",
      "User-Agent": "horizon-watchdog/1.0",
    });
  });
});

describe("dispatchWatchdogFallback", () => {
  it("uses return_run_details and accepts only a verifiable 200 run response", async () => {
    const fetchImpl = vi.fn().mockResolvedValue(
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
      dispatchWatchdogFallback({
        fetchImpl,
        token: "test-token",
        targetDate: "2026-07-14",
        handoffId: "test-jti",
      }),
    ).resolves.toEqual({
      decision: "DISPATCH_CONFIRMED",
      httpStatus: 200,
      workflowRunId: 12345,
      runUrl: "https://api.github.com/repos/michaelluetw-bit/Horizon/actions/runs/12345",
      htmlUrl: "https://github.com/michaelluetw-bit/Horizon/actions/runs/12345",
    });

    const [url, options] = fetchImpl.mock.calls[0];
    expect(url).toBe(
      "https://api.github.com/repos/michaelluetw-bit/Horizon/actions/workflows/horizon_daily.yml/dispatches",
    );
    expect(options.headers).toMatchObject({
      ...GITHUB_API_HEADERS,
      Authorization: "Bearer test-token",
      "Content-Type": "application/json",
    });
    expect(JSON.parse(options.body)).toEqual({
      ref: "main",
      return_run_details: true,
      inputs: {
        trigger_source: "fallback-watchdog",
        target_date: "2026-07-14",
        handoff_id: "test-jti",
      },
    });
  });

  it("does not retry a 204 because the dispatch might already exist", async () => {
    const fetchImpl = vi.fn().mockResolvedValue(new Response(null, { status: 204 }));

    await expect(
      dispatchWatchdogFallback({
        fetchImpl,
        token: "test-token",
        targetDate: "2026-07-14",
        handoffId: "test-jti",
      }),
    ).resolves.toEqual({
      decision: "DISPATCH_ACCEPTED_WITHOUT_PROVENANCE",
      httpStatus: 204,
      mayRetry: false,
    });
    expect(fetchImpl).toHaveBeenCalledTimes(1);
  });

  it.each([
    ["omits the returned run ID", { run_url: "https://api.github.com/repos/michaelluetw-bit/Horizon/actions/runs/12345" }],
    [
      "returns a URL for another run",
      {
        workflow_run_id: 12345,
        run_url: "https://api.github.com/repos/michaelluetw-bit/Horizon/actions/runs/54321",
        html_url: "https://github.com/michaelluetw-bit/Horizon/actions/runs/12345",
      },
    ],
  ])("fails closed for a 200 that %s", async (_description, payload) => {
    const fetchImpl = vi.fn().mockResolvedValue(new Response(JSON.stringify(payload), { status: 200 }));

    await expect(
      dispatchWatchdogFallback({
        fetchImpl,
        token: "test-token",
        targetDate: "2026-07-14",
        handoffId: "test-jti",
      }),
    ).resolves.toEqual({
      decision: "DISPATCH_RESPONSE_INVALID",
      httpStatus: 200,
      mayRetry: false,
    });
    expect(fetchImpl).toHaveBeenCalledTimes(1);
  });
});

describe("decidePrimaryRuns", () => {
  it("fails closed instead of choosing one of multiple verified schedule runs", () => {
    expect(
      decidePrimaryRuns(
        [
          scheduledRun(101, "2026-07-13T21:17:00Z"),
          scheduledRun(102, "2026-07-13T21:18:00Z"),
        ],
        range,
      ),
    ).toEqual({
      decision: "CHECK_FAILED",
      reason: "PRIMARY_NOT_UNIQUE",
      mayDispatch: false,
    });
  });

  it("fails closed when the API returns a sole run that does not match main", () => {
    const run = scheduledRun(101, "2026-07-13T21:17:00Z");
    run.head_branch = "release";

    expect(decidePrimaryRuns([run], range)).toEqual({
      decision: "CHECK_FAILED",
      reason: "PRIMARY_QUERY_INVALID",
      mayDispatch: false,
    });
  });
});
