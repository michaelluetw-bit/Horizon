from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_only_horizon_daily_can_run_horizon_on_a_schedule() -> None:
    canonical = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")
    deployment = (ROOT / ".github/workflows/daily-summary.yml").read_text(encoding="utf-8")

    assert "cron: '0 0 * * *'" in canonical
    assert "TZ: Asia/Taipei" in canonical
    assert "group: horizon-daily" in canonical
    assert "uv run horizon --hours 24" in canonical
    assert "cp data/config.github.json data/config.json" in canonical
    assert "schedule:" not in deployment
    assert "uv run horizon" not in deployment
    assert "git commit" not in deployment
    assert "peaceiris/actions-gh-pages" in deployment


def test_daily_workflow_force_tracks_ignored_generated_artifacts() -> None:
    workflow = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")

    assert "git add -f data/summaries docs/_posts" in workflow
    assert "if git diff --cached --quiet; then" in workflow
    assert "git status --porcelain data/summaries docs/_posts" not in workflow


def test_force_add_stages_ignored_generated_artifacts(tmp_path: Path) -> None:
    (tmp_path / ".gitignore").write_text("data/summaries/*.md\ndocs/_posts/*.md\n", encoding="utf-8")
    source = tmp_path / "data" / "summaries" / "horizon-2026-07-12-zh.md"
    post = tmp_path / "docs" / "_posts" / "2026-07-12-summary-zh.md"
    source.parent.mkdir(parents=True)
    post.parent.mkdir(parents=True)
    source.write_text("summary", encoding="utf-8")
    post.write_text("post", encoding="utf-8")

    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True, text=True)
    subprocess.run(
        ["git", "add", "-f", "data/summaries", "docs/_posts"],
        cwd=tmp_path,
        check=True,
        capture_output=True,
        text=True,
    )
    staged = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=tmp_path,
        check=False,
        capture_output=True,
        text=True,
    )

    assert staged.returncode == 1


def test_ci_runs_locked_full_tests_without_production_secrets() -> None:
    workflow_path = ROOT / ".github/workflows/ci.yml"

    assert workflow_path.exists(), "Missing independent CI workflow"
    workflow = workflow_path.read_text(encoding="utf-8")

    assert "pull_request:" in workflow
    assert "branches: [main]" in workflow
    assert "contents: read" in workflow
    assert "runs-on: windows-latest" in workflow
    assert "uv sync --locked --extra dev" in workflow
    assert "uv run pytest -q" in workflow
    for forbidden in ("OPENAI_API_KEY", "DEEPSEEK_API_KEY", "DASHSCOPE_API_KEY", "HORIZON_WEBHOOK_URL"):
        assert forbidden not in workflow


def test_cloud_config_is_valid_and_excludes_paused_categories() -> None:
    config = json.loads((ROOT / "data/config.github.json").read_text(encoding="utf-8"))
    serialized = json.dumps(config, ensure_ascii=False).lower()
    workflow = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")

    for paused in ("politics", "finance", "investment", "world", "semianalysis"):
        assert paused not in serialized
    assert "ai-tools" in serialized
    assert "github-trending" in serialized
    assert config["ai"]["api_key_env"] in workflow


def test_sync_script_exposes_required_safety_contract() -> None:
    script = (ROOT / "scripts/sync_latest.ps1").read_text(encoding="utf-8")

    for marker in (
        "pull --ff-only origin main",
        "Global\\HorizonDailyCloudToLocalPublish",
        "horizon-daily-publish.log",
        "INVALID_REPOSITORY",
        "WRONG_BRANCH",
        "DIRTY_WORKTREE",
        "PULL_FAILED",
        "SOURCE_NOT_FOUND",
        "SOURCE_INVALID",
        "PUBLISH_FAILED",
        "PUBLISH_SUCCESS_DASHBOARD_UNAVAILABLE",
        "DASHBOARD_VALIDATION_FAILED",
    ):
        assert marker in script
    assert "Start-Sleep" not in script
    assert "git reset" not in script


def test_sync_script_selects_chinese_source_when_bilingual_summaries_exist() -> None:
    script = (ROOT / "scripts/sync_latest.ps1").read_text(encoding="utf-8")

    assert '$expectedName = "horizon-$ArtifactDate-zh.md"' in script
    assert "$expectedSource = Join-Path $sourceDir $expectedName" in script
    assert "Test-Path -LiteralPath $expectedSource -PathType Leaf" in script
    assert "$matches.Count -gt 1" not in script


def test_sync_invalid_repository_returns_code_10_without_creating_target(tmp_path: Path) -> None:
    script = ROOT / "scripts/sync_latest.ps1"
    target = tmp_path / "vault" / "01_Horizon"
    result = subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(script),
            "-ProjectRoot",
            str(tmp_path / "missing"),
            "-TargetDir",
            str(target),
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    assert result.returncode == 10
    assert "STATUS=INVALID_REPOSITORY" in result.stdout
    assert not target.exists()


def test_task_registration_uses_daily_retry_and_no_parallel_policy() -> None:
    script = (ROOT / "scripts/register_horizon_daily_task.ps1").read_text(encoding="utf-8")

    assert "Horizon Daily Sync Publish" in script
    assert "09:00" in script
    assert "PT10M" in script
    assert "<Count>3</Count>" in script
    assert "IgnoreNew" in script
    assert "StartWhenAvailable" in script
    assert "InteractiveToken" in script
    assert "<RunLevel>LeastPrivilege</RunLevel>" in script
    assert "schtasks.exe" in script
