from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import threading
import tomllib
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterator

import pytest


ROOT = Path(__file__).resolve().parents[1]
SYNC_DATE = "2026-07-13"


def run_git(args: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def create_sync_project(tmp_path: Path, source_body: str | None) -> Path:
    remote = tmp_path / "origin.git"
    seed = tmp_path / "seed"
    project = tmp_path / "project"
    remote.mkdir()
    run_git(["init", "--bare"], cwd=remote)
    seed.mkdir()
    run_git(["init"], cwd=seed)
    run_git(["checkout", "-b", "main"], cwd=seed)
    run_git(["config", "user.email", "tests@example.invalid"], cwd=seed)
    run_git(["config", "user.name", "Horizon Tests"], cwd=seed)

    (seed / "scripts").mkdir()
    shutil.copy2(ROOT / "scripts" / "sync_latest.ps1", seed / "scripts" / "sync_latest.ps1")
    shutil.copy2(ROOT / "scripts" / "publish_horizon.py", seed / "scripts" / "publish_horizon.py")
    (seed / "scripts" / "guard.ps1").write_text("$guard = $true\n", encoding="utf-8")
    (seed / "src").mkdir()
    (seed / "src" / "guard.py").write_text("GUARD = True\n", encoding="utf-8")
    (seed / "config").mkdir()
    (seed / "config" / "publish.json").write_text("{}\n", encoding="utf-8")
    if source_body is not None:
        source = seed / "data" / "summaries" / f"horizon-{SYNC_DATE}-zh.md"
        source.parent.mkdir(parents=True)
        source.write_text(source_body, encoding="utf-8")

    initial_paths = ["scripts", "src", "config"]
    if source_body is not None:
        initial_paths.append("data")
    run_git(["add", *initial_paths], cwd=seed)
    run_git(["commit", "-m", "seed sync fixture"], cwd=seed)
    run_git(["remote", "add", "origin", str(remote)], cwd=seed)
    run_git(["push", "-u", "origin", "main"], cwd=seed)
    subprocess.run(
        ["git", "clone", "--branch", "main", str(remote), str(project)],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return project


def update_origin_source(tmp_path: Path, project: Path, source_body: str) -> None:
    remote = run_git(["remote", "get-url", "origin"], cwd=project).stdout.strip()
    updater = tmp_path / "updater"
    subprocess.run(
        ["git", "clone", "--branch", "main", remote, str(updater)],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    run_git(["config", "user.email", "tests@example.invalid"], cwd=updater)
    run_git(["config", "user.name", "Horizon Tests"], cwd=updater)
    (updater / "data" / "summaries" / f"horizon-{SYNC_DATE}-zh.md").write_text(source_body, encoding="utf-8")
    run_git(["add", "data/summaries"], cwd=updater)
    run_git(["commit", "-m", "update origin summary"], cwd=updater)
    run_git(["push", "origin", "main"], cwd=updater)


def remove_origin_source(tmp_path: Path, project: Path) -> None:
    remote = run_git(["remote", "get-url", "origin"], cwd=project).stdout.strip()
    updater = tmp_path / "updater"
    subprocess.run(
        ["git", "clone", "--branch", "main", remote, str(updater)],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    run_git(["config", "user.email", "tests@example.invalid"], cwd=updater)
    run_git(["config", "user.name", "Horizon Tests"], cwd=updater)
    run_git(["rm", f"data/summaries/horizon-{SYNC_DATE}-zh.md"], cwd=updater)
    run_git(["commit", "-m", "remove origin summary"], cwd=updater)
    run_git(["push", "origin", "main"], cwd=updater)


@contextmanager
def dashboard_server(artifact_date: str) -> Iterator[str]:
    payload = json.dumps(
        {
            "artifacts": [
                {
                    "relativePath": f"01_Horizon\\{artifact_date}-horizon.md",
                    "date": artifact_date,
                    "module": "horizon",
                    "agent": "Horizon",
                    "status": "completed",
                    "source": f"data/summaries/horizon-{artifact_date}-zh.md",
                }
            ]
        }
    ).encode("utf-8")

    class ArtifactHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            if self.path != "/api/artifacts":
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, _format: str, *_args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), ArtifactHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def run_sync(project: Path, target: Path, dashboard_base_url: str, tmp_path: Path) -> subprocess.CompletedProcess[str]:
    logs = tmp_path / "logs"
    logs.mkdir(exist_ok=True)
    env = os.environ | {"TEMP": str(logs), "TMP": str(logs)}
    return subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(project / "scripts" / "sync_latest.ps1"),
            "-ProjectRoot",
            str(project),
            "-TargetDir",
            str(target),
            "-DashboardBaseUrl",
            dashboard_base_url,
            "-ArtifactDate",
            SYNC_DATE,
            "-PythonExecutable",
            sys.executable,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        env=env,
    )


def test_sync_publishes_origin_main_blob_when_worktree_is_clean(tmp_path: Path) -> None:
    source_body = f"# Horizon 每日快遞 - {SYNC_DATE}\n\n正式來源：繁體中文。\n"
    project = create_sync_project(tmp_path, source_body)
    target = tmp_path / "vault" / "01_Horizon"

    with dashboard_server(SYNC_DATE) as dashboard_base_url:
        result = run_sync(project, target, dashboard_base_url, tmp_path)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "STATUS=SUCCESS" in result.stdout
    published = (target / f"{SYNC_DATE}-horizon.md").read_text(encoding="utf-8")
    assert source_body.strip() in published
    assert run_git(["status", "--short"], cwd=project).stdout == ""


def test_sync_rejects_invalid_origin_summary(tmp_path: Path) -> None:
    project = create_sync_project(tmp_path, "# 不符合 Horizon 契約\n\n內容。\n")
    target = tmp_path / "vault" / "01_Horizon"

    with dashboard_server(SYNC_DATE) as dashboard_base_url:
        result = run_sync(project, target, dashboard_base_url, tmp_path)

    assert result.returncode == 22, result.stdout + result.stderr
    assert "STATUS=TODAY_OUTPUT_INVALID" in result.stdout
    assert not target.exists()


def test_sync_publishes_origin_blob_when_local_generated_summary_is_dirty(tmp_path: Path) -> None:
    project = create_sync_project(tmp_path, f"# Horizon 每日快遞 - {SYNC_DATE}\n\n舊版來源。\n")
    origin_body = f"# Horizon 每日快遞 - {SYNC_DATE}\n\norigin/main 正式內容：罕見字：臺灣、😀、軟件。\n"
    local_body = f"# Horizon 每日快遞 - {SYNC_DATE}\n\n本機未信任內容。\n"
    update_origin_source(tmp_path, project, origin_body)
    local_source = project / "data" / "summaries" / f"horizon-{SYNC_DATE}-zh.md"
    local_source.write_text(local_body, encoding="utf-8")
    status_before = run_git(["status", "--short"], cwd=project).stdout
    target = tmp_path / "vault" / "01_Horizon"

    with dashboard_server(SYNC_DATE) as dashboard_base_url:
        result = run_sync(project, target, dashboard_base_url, tmp_path)

    assert result.returncode == 0, result.stdout + result.stderr
    origin_blob = subprocess.check_output(
        ["git", "-C", str(project), "show", f"origin/main:data/summaries/horizon-{SYNC_DATE}-zh.md"]
    )
    assert origin_blob == origin_body.encode("utf-8")
    published = (target / f"{SYNC_DATE}-horizon.md").read_text(encoding="utf-8")
    assert "origin/main 正式內容：罕見字：臺灣、😀、軟體。" in published
    assert local_body.strip() not in published
    assert local_source.read_text(encoding="utf-8") == local_body
    assert run_git(["status", "--short"], cwd=project).stdout == status_before


@pytest.mark.parametrize("relative_path", ["scripts/guard.ps1", "src/guard.py", "config/publish.json"])
def test_sync_rejects_dirty_code_or_configuration(tmp_path: Path, relative_path: str) -> None:
    project = create_sync_project(tmp_path, f"# Horizon 每日快遞 - {SYNC_DATE}\n\n正式內容。\n")
    dirty_path = project / relative_path
    dirty_path.write_text("local change\n", encoding="utf-8")
    target = tmp_path / "vault" / "01_Horizon"

    with dashboard_server(SYNC_DATE) as dashboard_base_url:
        result = run_sync(project, target, dashboard_base_url, tmp_path)

    assert result.returncode == 12, result.stdout + result.stderr
    assert "STATUS=DIRTY_CODE_WORKTREE" in result.stdout
    assert not target.exists()
    assert dirty_path.read_text(encoding="utf-8") == "local change\n"


def test_sync_reports_missing_today_origin_output(tmp_path: Path) -> None:
    project = create_sync_project(tmp_path, f"# Horizon 每日快遞 - {SYNC_DATE}\n\n舊本機內容。\n")
    remove_origin_source(tmp_path, project)
    local_source = project / "data" / "summaries" / f"horizon-{SYNC_DATE}-zh.md"
    target = tmp_path / "vault" / "01_Horizon"

    with dashboard_server(SYNC_DATE) as dashboard_base_url:
        result = run_sync(project, target, dashboard_base_url, tmp_path)

    assert result.returncode == 20, result.stdout + result.stderr
    assert "STATUS=TODAY_OUTPUT_MISSING" in result.stdout
    assert not target.exists()
    assert "舊本機內容" in local_source.read_text(encoding="utf-8")


def test_sync_is_idempotent_for_the_same_origin_blob(tmp_path: Path) -> None:
    source_body = f"# Horizon 每日快遞 - {SYNC_DATE}\n\n同日正式內容。\n"
    project = create_sync_project(tmp_path, source_body)
    target = tmp_path / "vault" / "01_Horizon"

    with dashboard_server(SYNC_DATE) as dashboard_base_url:
        first = run_sync(project, target, dashboard_base_url, tmp_path)
        target_file = target / f"{SYNC_DATE}-horizon.md"
        first_mtime = target_file.stat().st_mtime_ns
        second = run_sync(project, target, dashboard_base_url, tmp_path)

    assert first.returncode == 0, first.stdout + first.stderr
    assert second.returncode == 0, second.stdout + second.stderr
    assert "STATUS=ALREADY_PUBLISHED" in second.stdout
    assert target_file.stat().st_mtime_ns == first_mtime
    assert run_git(["status", "--short"], cwd=project).stdout == ""


def test_sync_reports_origin_fetch_failure(tmp_path: Path) -> None:
    project = create_sync_project(tmp_path, f"# Horizon 每日快遞 - {SYNC_DATE}\n\n正式內容。\n")
    run_git(["remote", "set-url", "origin", str(tmp_path / "missing-origin.git")], cwd=project)
    target = tmp_path / "vault" / "01_Horizon"

    with dashboard_server(SYNC_DATE) as dashboard_base_url:
        result = run_sync(project, target, dashboard_base_url, tmp_path)

    assert result.returncode == 13, result.stdout + result.stderr
    assert "STATUS=ORIGIN_FETCH_FAILED" in result.stdout
    assert not target.exists()


def test_only_horizon_daily_can_run_horizon_on_a_schedule() -> None:
    canonical = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")
    deployment = (ROOT / ".github/workflows/daily-summary.yml").read_text(encoding="utf-8")

    assert "cron: '17 21 * * *'" in canonical
    assert "cron: '17 0 * * *'" not in canonical
    assert "cron: '0 0 * * *'" not in canonical
    assert "TZ: Asia/Taipei" in canonical
    assert "group: horizon-daily" in canonical
    assert "uv run horizon --hours 24" in canonical
    assert 'uv run horizon --hours 24 --target-date "$TARGET_DATE"' in canonical
    assert "cp data/config.github.json data/config.json" in canonical
    assert "schedule:" not in deployment
    assert "uv run horizon" not in deployment
    assert "git commit" not in deployment
    assert "peaceiris/actions-gh-pages" in deployment


def test_daily_workflow_creates_or_updates_an_app_owned_pull_request() -> None:
    workflow = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")

    assert "\npermissions:\n  contents: read\n" in workflow
    assert "\npermissions:\n  contents: write\n" not in workflow
    assert "persist-credentials: false" in workflow
    assert "Stage exact canonical artifacts" in workflow
    assert "actions/create-github-app-token@v3" in workflow
    assert "${{ vars.HORIZON_AUTOMATION_APP_CLIENT_ID }}" in workflow
    assert "${{ secrets.HORIZON_AUTOMATION_APP_PRIVATE_KEY }}" in workflow
    assert "permission-contents: write" in workflow
    assert "permission-pull-requests: write" in workflow
    assert "peter-evans/create-pull-request@v8" in workflow
    assert "token: ${{ steps.app-token.outputs.token }}" in workflow
    assert "branch-token: ${{ steps.app-token.outputs.token }}" in workflow
    assert "branch: automation/horizon-daily-publish" in workflow
    assert "base: main" in workflow
    assert "delete-branch: true" in workflow
    assert "pull-request-number" in workflow
    assert 'gh pr merge "$PR_NUMBER" --repo "$GITHUB_REPOSITORY" --auto --merge' in workflow
    assert "git push origin main" not in workflow
    assert "[skip ci]" not in workflow
    assert "GITHUB_TOKEN" not in workflow


def test_daily_workflow_requires_verified_provenance_and_exact_four_file_gate() -> None:
    workflow = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")

    run_name = next(line for line in workflow.splitlines() if line.startswith("run-name:"))
    assert "github" in run_name
    assert "inputs" in run_name
    assert "vars" not in run_name
    assert "workflow_dispatch:" in workflow
    for input_name in ("trigger_source", "target_date", "handoff_id"):
        assert f"      {input_name}:" in workflow
    assert "id-token: write" in workflow
    assert "workers/horizon-watchdog/src/github-provenance.mjs" in workflow
    assert "HORIZON_EVIDENCE_DIR: ${{ runner.temp }}" not in workflow
    assert 'evidence_dir="$RUNNER_TEMP/horizon-evidence"' in workflow
    assert 'echo "HORIZON_EVIDENCE_DIR=$evidence_dir" >> "$GITHUB_ENV"' in workflow
    assert "HORIZON_WORKFLOW_STARTED_AT: ${{ steps.workflow-start.outputs.workflow_started_at }}" in workflow
    assert "HORIZON_WATCHDOG_URL: ${{ vars.HORIZON_WATCHDOG_URL }}" in workflow
    assert "HORIZON_WATCHDOG_PUBLIC_KEY_JWK: ${{ vars.HORIZON_WATCHDOG_PUBLIC_KEY_JWK }}" in workflow
    assert "scripts/horizon_daily_gate.py preflight" in workflow
    assert "--main-ref origin/main" in workflow
    assert "--publish-ref origin/automation/horizon-daily-publish" in workflow
    assert "scripts/horizon_daily_gate.py validate" in workflow
    assert "scripts/horizon_daily_evidence.py render" in workflow
    assert "actions/upload-artifact@v6" in workflow
    assert "body-path:" in workflow
    assert "gh pr view \"$PR_NUMBER\" --repo \"$GITHUB_REPOSITORY\" --json body --jq .body" in workflow
    assert "scripts/horizon_daily_evidence.py verify-pr-body" in workflow
    assert "data/summaries/horizon-${{ steps.provenance.outputs.target_date }}-zh.md" in workflow
    assert "data/summaries/horizon-${{ steps.provenance.outputs.target_date }}-en.md" in workflow
    assert "docs/_posts/${{ steps.provenance.outputs.target_date }}-summary-zh.md" in workflow
    assert "docs/_posts/${{ steps.provenance.outputs.target_date }}-summary-en.md" in workflow
    assert "git add -f data/summaries docs/_posts" not in workflow


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


def test_ci_requires_blocking_ruff_from_the_locked_dev_extra() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    pyproject = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    dev_dependencies = pyproject["project"]["optional-dependencies"]["dev"]
    assert any(dependency.startswith("ruff") for dependency in dev_dependencies)
    assert "  ruff:\n" in workflow
    ruff_job = workflow.split("  ruff:\n", 1)[1].split("\n  test:\n", 1)[0]
    assert "name: ruff" in ruff_job
    assert "continue-on-error: true" not in ruff_job
    assert "uv sync --locked --extra dev" in ruff_job
    assert "uv run ruff check ." in ruff_job


def test_ci_uses_a_single_uv_cache_writer() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    ruff_job = workflow.split("  ruff:", 1)[1].split("  test:", 1)[0]
    test_job = workflow.split("  test:", 1)[1].split("  watchdog:", 1)[0]

    assert "enable-cache: false" in ruff_job
    assert "enable-cache: false" not in test_job


def test_ci_runs_the_watchdog_contract_suite_without_deployment() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "  watchdog:" in workflow
    assert "workers/horizon-watchdog" in workflow
    assert "npm ci" in workflow
    assert "npm test" in workflow
    assert "wrangler deploy" not in workflow


def test_workflows_use_node24_action_runtimes() -> None:
    ci_workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    daily_workflow = (ROOT / ".github/workflows/horizon_daily.yml").read_text(encoding="utf-8")
    combined_workflows = f"{ci_workflow}\n{daily_workflow}"

    for action in (
        "actions/checkout@v6",
        "actions/setup-node@v5",
        "actions/setup-python@v6",
        "astral-sh/setup-uv@v7",
    ):
        assert action in ci_workflow
        assert action in daily_workflow
    assert "actions/upload-artifact@v6" in daily_workflow
    for deprecated_action in (
        "actions/checkout@v4",
        "actions/setup-node@v4",
        "actions/setup-python@v5",
        "astral-sh/setup-uv@v3",
        "astral-sh/setup-uv@v6",
        "actions/upload-artifact@v4",
    ):
        assert deprecated_action not in combined_workflows


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
        "fetch",
        "origin/main:$sourceRef",
        "Export-GitBlob",
        "RedirectStandardOutput = $true",
        "BaseStream.CopyToAsync",
        "--source-file",
        "Global\\HorizonDailyCloudToLocalPublish",
        "horizon-daily-publish.log",
        "INVALID_REPOSITORY",
        "WRONG_BRANCH",
        "DIRTY_CODE_WORKTREE",
        "ORIGIN_FETCH_FAILED",
        "ORIGIN_BLOB_READ_FAILED",
        "TODAY_OUTPUT_MISSING",
        "TODAY_OUTPUT_INVALID",
        "VAULT_PUBLISH_FAILED",
        "PUBLISH_SUCCESS_DASHBOARD_UNAVAILABLE",
        "DASHBOARD_VALIDATION_FAILED",
    ):
        assert marker in script
    assert "Start-Sleep" not in script
    assert "git reset" not in script
    assert "git checkout" not in script
    assert "pull --ff-only origin main" not in script


def test_sync_script_selects_chinese_source_when_bilingual_summaries_exist() -> None:
    script = (ROOT / "scripts/sync_latest.ps1").read_text(encoding="utf-8")

    assert '$expectedName = "horizon-$ArtifactDate-zh.md"' in script
    assert '$sourceRef = "data/summaries/$expectedName"' in script
    assert '$originObject = "origin/main:$sourceRef"' in script
    assert '"cat-file", "-t", $originObject' in script
    assert "Test-Path -LiteralPath $expectedSource -PathType Leaf" not in script
    assert "$sourceDir = Join-Path $ProjectRoot" not in script


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
