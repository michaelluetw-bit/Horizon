# Force Track Daily Artifacts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ensure the successful daily Horizon workflow commits its ignored Markdown artifacts to `main` so the local sync can publish the exact dated report.

**Architecture:** Keep `.gitignore` unchanged for local generated files. Change only the GitHub Actions commit step to force-add `data/summaries` and `docs/_posts`, guarded by the existing path-scoped `git status` condition.

**Tech Stack:** GitHub Actions YAML, pytest, GitHub Actions CI.

## Global Constraints

- Work only on `codex/force-track-daily-artifacts`, created from synchronized `main`.
- Do not add API keys, webhook values, or generated output files to the source diff.
- Preserve local ignore behavior; only the cloud workflow may force-track generated Markdown.
- Complete TDD, commit, push, PR review, CI, merge, and final `main` synchronization.

---

### Task 1: Lock the generated-artifact commit contract

**Files:**
- Modify: `.github/workflows/horizon_daily.yml`
- Modify: `tests/test_daily_publish_contract.py`
- Create: `docs/superpowers/plans/2026-07-12-force-track-daily-artifacts.md`

**Interfaces:**
- Consumes: ignored generated files under `data/summaries` and `docs/_posts` after `uv run horizon --hours 24`.
- Produces: a daily bot commit containing the matching summary and Pages post.

- [x] **Step 1: Write the failing workflow contract test**

```python
def test_daily_workflow_force_tracks_ignored_generated_artifacts() -> None:
    workflow = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")

    assert "git add -f data/summaries docs/_posts" in workflow
```

- [x] **Step 2: Run the test and verify RED**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py::test_daily_workflow_force_tracks_ignored_generated_artifacts -v`

Expected: FAIL because the current workflow uses `git add data/summaries docs/_posts`.

- [x] **Step 3: Apply the minimal workflow change**

```yaml
- name: Commit and push changes
  run: |
    if [ -n "$(git status --porcelain data/summaries docs/_posts)" ]; then
      git config --global user.name "github-actions[bot]"
      git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
      git add -f data/summaries docs/_posts
      git commit -m "docs: 雲端自動生成每日快報 [skip ci]"
      git push origin main
    fi
```

- [x] **Step 4: Verify GREEN locally**

Run: `.venv\Scripts\python.exe -m pytest tests/test_daily_publish_contract.py -v`

Run: `uv run pytest -q`

Expected: both commands exit with zero failures.

### Task 2: Deliver and replay the missed artifact

**Files:**
- Include: only the three files in Task 1.

**Interfaces:**
- Consumes: a clean feature branch and green PR CI.
- Produces: merged workflow fix, committed 2026-07-12 artifacts, and a verified local Dashboard publication.

- [ ] **Step 1: Commit, push, review, and merge**

Commit message: `fix: commit generated Horizon artifacts`

PR acceptance criteria: exact three-file scope, no secret patterns, Windows CI successful, and PR state `CLEAN`.

- [ ] **Step 2: Replay the 2026-07-12 workflow**

Dispatch `Horizon Daily Aggregation` from merged `main`, then verify:

```text
data/summaries/horizon-2026-07-12-zh.md
docs/_posts/2026-07-12-summary-zh.md
```

- [ ] **Step 3: Run and verify local sync**

Run `scripts/sync_latest.ps1` on clean `main` after the generated commit is pulled. Success requires exit code `0`, a published `01_Horizon/2026-07-12-horizon.md`, and a matching Dashboard API artifact.
