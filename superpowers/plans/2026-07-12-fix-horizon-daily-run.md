# Horizon Daily Run Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make one GitHub Actions workflow generate the daily Horizon summary, then safely synchronize and publish that exact artifact to the local AI Executive Dashboard.

**Architecture:** `horizon_daily.yml` is the only scheduled producer and copies the committed cloud configuration before running Horizon. `daily-summary.yml` is manual deployment only. The Windows task pulls a clean `main`, validates the canonical dated source, publishes atomically, and verifies the Dashboard API response.

**Tech Stack:** GitHub Actions YAML, Python 3.12, pytest, PowerShell 5.1, uv, OpenCC.

## Global Constraints

- Work only on `codex/fix-horizon-daily-run`, created from synchronized `main`.
- Preserve all pre-existing user changes and include only the daily publish feature in the PR.
- Use Asia/Taipei for artifact dates.
- Never commit API keys or webhook URLs; workflows reference GitHub Secrets by environment-variable name.
- Complete commit, push, PR review, CI, merge, and final `main` synchronization.

---

### Task 1: Lock the scheduled-workflow contract

**Files:**
- Modify: `.github/workflows/daily-summary.yml`
- Modify: `.github/workflows/horizon_daily.yml`
- Modify: `data/config.github.json`
- Test: `tests/test_daily_publish_contract.py`

**Interfaces:**
- Consumes: GitHub Actions secrets named by `data/config.github.json`.
- Produces: one scheduled producer that writes `data/summaries/horizon-YYYY-MM-DD-zh.md` and `docs/_posts/YYYY-MM-DD-summary-zh.md`.

- [x] **Step 1: Verify the regression exists on the synchronized main baseline**

Run a read-only assertion against `git show HEAD` that requires `daily-summary.yml` to have no schedule and requires `horizon_daily.yml` to copy `data/config.github.json` to `data/config.json`.

Expected: FAIL because baseline `daily-summary.yml` is scheduled and baseline `horizon_daily.yml` does not prepare `data/config.json`.

- [x] **Step 2: Keep the failing contract tests**

```python
def test_only_horizon_daily_can_run_horizon_on_a_schedule() -> None:
    canonical = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")
    deployment = (ROOT / ".github/workflows/daily-summary.yml").read_text(encoding="utf-8")

    assert "cron: '0 0 * * *'" in canonical
    assert "cp data/config.github.json data/config.json" in canonical
    assert "schedule:" not in deployment
    assert "uv run horizon" not in deployment
```

- [x] **Step 3: Apply the minimum workflow ownership fix**

```yaml
# horizon_daily.yml
- name: Prepare canonical cloud config
  run: cp data/config.github.json data/config.json

- name: Run Horizon pipeline
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
    DASHSCOPE_API_KEY: ${{ secrets.DASHSCOPE_API_KEY }}
    DEEPSEEK_API_KEY: ${{ secrets.DEEPSEEK_API_KEY }}
  run: uv run horizon --hours 24
```

Keep `daily-summary.yml` as `workflow_dispatch` plus Pages deployment only.

- [x] **Step 4: Run the workflow contract tests**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py -v`

Expected: all tests pass.

### Task 2: Publish one canonical local Dashboard artifact

**Files:**
- Modify: `scripts/publish_horizon.py`
- Modify: `pyproject.toml`
- Modify: `uv.lock`
- Test: `tests/test_publish_horizon.py`

**Interfaces:**
- Consumes: `data/summaries/horizon-YYYY-MM-DD-zh.md`.
- Produces: `01_Horizon/YYYY-MM-DD-horizon.md` with deterministic frontmatter and required sections.

- [x] **Step 1: Run the publisher tests against the baseline behavior**

Expected: FAIL because the baseline publisher does not expose `PublishError`, `resolve_source`, `convert_to_taiwan`, or `publish`.

- [x] **Step 2: Keep the source-selection and idempotency tests**

```python
def test_resolve_source_requires_exactly_one_chinese_artifact(tmp_path: Path) -> None:
    source_dir = tmp_path / "summaries"
    expected = write_source(source_dir)
    assert resolve_source(source_dir, DATE) == expected

def test_publish_is_idempotent_and_does_not_change_mtime(tmp_path: Path) -> None:
    source_dir = tmp_path / "data" / "summaries"
    write_source(source_dir)
    target_dir = tmp_path / "vault" / "01_Horizon"
    assert publish(source_dir, target_dir, DATE, project_root=tmp_path) == "SUCCESS"
    assert publish(source_dir, target_dir, DATE, project_root=tmp_path) == "ALREADY_PUBLISHED"
```

- [x] **Step 3: Keep the minimum deterministic publisher API**

```python
def resolve_source(source_dir: Path, artifact_date: str) -> Path: ...
def convert_to_taiwan(markdown: str) -> str: ...
def publish(
    source_dir: Path,
    target_dir: Path,
    artifact_date: str,
    *,
    project_root: Path = PROJECT_ROOT,
) -> str: ...
```

The implementation must return `SUCCESS` or `ALREADY_PUBLISHED`, reject missing, ambiguous, invalid, or non-UTF-8 sources, validate output before replacement, and use `os.replace` for atomic publication.

- [x] **Step 4: Run publisher tests**

Run: `.venv\Scripts\python.exe -m pytest tests/test_publish_horizon.py -v`

Expected: all tests pass.

### Task 3: Make Windows synchronization observable and fail closed

**Files:**
- Modify: `scripts/sync_latest.ps1`
- Create: `scripts/register_horizon_daily_task.ps1`
- Test: `tests/test_daily_publish_contract.py`

**Interfaces:**
- Consumes: clean local `main`, remote `origin/main`, canonical dated summary, Dashboard API at `http://127.0.0.1:5173/api/artifacts`.
- Produces: `%TEMP%\horizon-daily-publish.log`, stable exit codes, and a verified Dashboard artifact.

- [x] **Step 1: Keep the safety-contract regression tests**

The tests require `pull --ff-only`, a global mutex, structured log markers, explicit source errors, no `git reset`, and no `Start-Sleep`.

- [x] **Step 2: Keep explicit exit semantics**

```text
10 INVALID_REPOSITORY
11 WRONG_BRANCH
12 DIRTY_WORKTREE
13 PULL_FAILED
20 SOURCE_NOT_FOUND
21 AMBIGUOUS_SOURCE
22 SOURCE_INVALID
30 PUBLISH_FAILED
40 PUBLISH_SUCCESS_DASHBOARD_UNAVAILABLE
41 DASHBOARD_VALIDATION_FAILED
```

- [x] **Step 3: Verify the invalid-repository path**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py::test_sync_invalid_repository_returns_code_10_without_creating_target -v`

Expected: one test passes and the target directory is not created.

### Task 4: Add an independent CI gate

**Files:**
- Create: `.github/workflows/ci.yml`
- Modify: `tests/test_daily_publish_contract.py`
- Modify: `docs/superpowers/plans/2026-07-12-fix-horizon-daily-run.md`

**Interfaces:**
- Consumes: a pull request or a push to `main`.
- Produces: a read-only `CI / test` check that installs locked development dependencies and runs the complete pytest suite without production secrets.

- [x] **Step 1: Write the failing CI contract test**

```python
def test_ci_runs_locked_full_tests_without_production_secrets() -> None:
    workflow_path = ROOT / ".github/workflows/ci.yml"
    assert workflow_path.exists(), "Missing independent CI workflow"
    workflow = workflow_path.read_text(encoding="utf-8")

    assert "pull_request:" in workflow
    assert "branches: [main]" in workflow
    assert "contents: read" in workflow
    assert "uv sync --locked --extra dev" in workflow
    assert "uv run pytest -q" in workflow
    for forbidden in ("OPENAI_API_KEY", "DEEPSEEK_API_KEY", "DASHSCOPE_API_KEY", "HORIZON_WEBHOOK_URL"):
        assert forbidden not in workflow
```

- [x] **Step 2: Run the test and verify RED**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py::test_ci_runs_locked_full_tests_without_production_secrets -v`

Expected: FAIL with `Missing independent CI workflow`.

- [x] **Step 3: Add the minimal read-only workflow**

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    name: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - uses: astral-sh/setup-uv@v6
      - run: uv sync --locked --extra dev
      - run: uv run pytest -q
```

- [x] **Step 4: Run the CI contract and full suite**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py tests/test_publish_horizon.py -v`

Run: `.venv\Scripts\python.exe -m pytest -q`

Expected: both commands exit with zero failures.

### Task 4B: Run CI on Windows

**Files:**
- Modify: `.github/workflows/ci.yml`
- Modify: `tests/test_daily_publish_contract.py`
- Modify: `docs/superpowers/plans/2026-07-12-fix-horizon-daily-run.md`

**Interfaces:**
- Consumes: the Windows-specific `powershell.exe` behavioral test for `scripts/sync_latest.ps1`.
- Produces: a `CI / test` GitHub Actions check that can execute the complete suite, including the Windows synchronization test.

- [x] **Step 1: Add the runner requirement to the CI contract**

```python
assert "runs-on: windows-latest" in workflow
```

- [x] **Step 2: Run the CI contract and verify RED**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py::test_ci_runs_locked_full_tests_without_production_secrets -v`

Expected: FAIL because the workflow currently contains `runs-on: ubuntu-latest`.

- [x] **Step 3: Make the runner match the Windows contract**

```yaml
jobs:
  test:
    name: test
    runs-on: windows-latest
```

Keep the existing read-only permission, locked dependency installation, full pytest command, and absence of production secrets.

- [x] **Step 4: Verify GREEN locally and in GitHub Actions**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py::test_ci_runs_locked_full_tests_without_production_secrets -v`

Then push the commit and require the `CI / test` check to be successful before merge.

### Task 5: Verify and deliver

**Files:**
- Include: all files listed in Tasks 1-3
- Include: `docs/superpowers/plans/2026-07-12-fix-horizon-daily-run.md`

**Interfaces:**
- Consumes: complete feature-branch diff and GitHub Actions execution results.
- Produces: merged PR, synchronized clean `main`, and a verified 2026-07-12 output.

- [x] **Step 1: Run the focused tests**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py tests/test_publish_horizon.py -v`

Expected: all focused tests pass.

- [x] **Step 2: Run the complete test suite**

Run: `.venv\Scripts\python.exe -m pytest -q`

Expected: zero failures.

- [ ] **Step 3: Inspect the exact PR diff**

Run: `git diff --check` and `git diff --stat origin/main...HEAD` after commit.

Expected: no whitespace errors and no files outside the listed scope.

- [ ] **Step 4: Commit, push, open PR, review, and merge**

Commit message: `fix: restore reliable Horizon daily publishing`

PR acceptance criteria: required tests green, Actions YAML valid, no secret values in the diff, and CI green.

- [ ] **Step 5: Synchronize main and replay the missed date**

After merge, switch to `main`, run `git pull --ff-only origin main`, manually dispatch `Horizon Daily Aggregation`, and verify both:

```text
data/summaries/horizon-2026-07-12-zh.md
01_Horizon/2026-07-12-horizon.md
```

Success requires the GitHub run conclusion `success`, the Windows sync exit code `0`, and the Dashboard API to return the canonical artifact.
