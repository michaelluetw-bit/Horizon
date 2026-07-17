from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from src.automation.horizon_daily_gate import (
    ABSENT,
    ALREADY_IN_PROGRESS,
    ALREADY_PUBLISHED,
    CANONICAL_SET_INCOMPLETE,
    COMPLETE,
    READY,
    decide_preflight,
    inspect_git_ref,
    inspect_publish_branch_scope,
    inspect_canonical_set,
)


TARGET_DATE = "2026-07-14"


def write_complete_set(root: Path, target_date: str = TARGET_DATE) -> None:
    files = {
        f"data/summaries/horizon-{target_date}-zh.md": f"# Horizon 每日快遞 - {target_date}\n\n{target_date} 正式繁中摘要。\n",
        f"data/summaries/horizon-{target_date}-en.md": f"# Horizon Daily - {target_date}\n\n{target_date} canonical English summary.\n",
        f"docs/_posts/{target_date}-summary-zh.md": (
            "---\n"
            "layout: default\n"
            f"date: {target_date}\n"
            "lang: zh\n"
            f'title: "Horizon Summary: {target_date} (ZH)"\n'
            "---\n\n"
            f"{target_date} 正式繁中發布內容。\n"
        ),
        f"docs/_posts/{target_date}-summary-en.md": (
            "---\n"
            "layout: default\n"
            f"date: {target_date}\n"
            "lang: en\n"
            f'title: "Horizon Summary: {target_date} (EN)"\n'
            "---\n\n"
            f"{target_date} canonical English publication body.\n"
        ),
    }
    for relative_path, content in files.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def test_complete_set_requires_all_four_exact_files_with_valid_content(tmp_path: Path) -> None:
    write_complete_set(tmp_path)

    result = inspect_canonical_set(tmp_path, TARGET_DATE)

    assert result.status == COMPLETE
    assert result.paths == (
        f"data/summaries/horizon-{TARGET_DATE}-zh.md",
        f"data/summaries/horizon-{TARGET_DATE}-en.md",
        f"docs/_posts/{TARGET_DATE}-summary-zh.md",
        f"docs/_posts/{TARGET_DATE}-summary-en.md",
    )


def test_partial_set_fails_closed_instead_of_counting_as_published(tmp_path: Path) -> None:
    path = tmp_path / f"data/summaries/horizon-{TARGET_DATE}-zh.md"
    path.parent.mkdir(parents=True)
    path.write_text(f"# Horizon 每日快遞 - {TARGET_DATE}\n\n內容。\n", encoding="utf-8")

    result = inspect_canonical_set(tmp_path, TARGET_DATE)

    assert result.status == CANONICAL_SET_INCOMPLETE


def test_three_files_or_an_invalid_file_are_each_incomplete(tmp_path: Path) -> None:
    write_complete_set(tmp_path)
    (tmp_path / f"docs/_posts/{TARGET_DATE}-summary-en.md").unlink()

    missing_result = inspect_canonical_set(tmp_path, TARGET_DATE)

    assert missing_result.status == CANONICAL_SET_INCOMPLETE
    assert f"MISSING:docs/_posts/{TARGET_DATE}-summary-en.md" in missing_result.issues

    write_complete_set(tmp_path)
    summary = tmp_path / f"data/summaries/horizon-{TARGET_DATE}-en.md"
    summary.write_text(
        f"# Horizon Daily - {TARGET_DATE}\n\nTODO replace this placeholder.\n",
        encoding="utf-8",
    )

    invalid_result = inspect_canonical_set(tmp_path, TARGET_DATE)

    assert invalid_result.status == CANONICAL_SET_INCOMPLETE
    assert f"PLACEHOLDER_PRESENT:data/summaries/horizon-{TARGET_DATE}-en.md" in invalid_result.issues


def test_placeholder_words_mid_sentence_do_not_block_publishing(tmp_path: Path) -> None:
    write_complete_set(tmp_path)
    summary = tmp_path / f"data/summaries/horizon-{TARGET_DATE}-en.md"
    summary.write_text(
        f"# Horizon Daily - {TARGET_DATE}\n\n"
        "A review of the best TODO apps, with pricing still tbd for some tools.\n",
        encoding="utf-8",
    )

    result = inspect_canonical_set(tmp_path, TARGET_DATE)

    assert result.status == COMPLETE


def test_bracketed_placeholder_markers_still_block_publishing(tmp_path: Path) -> None:
    write_complete_set(tmp_path)
    summary = tmp_path / f"data/summaries/horizon-{TARGET_DATE}-en.md"
    summary.write_text(
        f"# Horizon Daily - {TARGET_DATE}\n\nReal intro text with a [TODO] marker left behind.\n",
        encoding="utf-8",
    )

    result = inspect_canonical_set(tmp_path, TARGET_DATE)

    assert result.status == CANONICAL_SET_INCOMPLETE
    assert f"PLACEHOLDER_PRESENT:data/summaries/horizon-{TARGET_DATE}-en.md" in result.issues


def test_preflight_stops_on_partial_main_before_considering_the_publish_branch(tmp_path: Path) -> None:
    main_root = tmp_path / "main"
    publish_root = tmp_path / "publish"
    (main_root / f"data/summaries/horizon-{TARGET_DATE}-zh.md").parent.mkdir(parents=True)
    (main_root / f"data/summaries/horizon-{TARGET_DATE}-zh.md").write_text(
        f"# Horizon 每日快遞 - {TARGET_DATE}\n\n內容。\n", encoding="utf-8"
    )
    write_complete_set(publish_root)

    decision = decide_preflight(
        inspect_canonical_set(main_root, TARGET_DATE),
        inspect_canonical_set(publish_root, TARGET_DATE),
    )

    assert decision.status == CANONICAL_SET_INCOMPLETE


def test_preflight_distinguishes_main_publish_branch_and_empty_sets(tmp_path: Path) -> None:
    main_root = tmp_path / "main"
    publish_root = tmp_path / "publish"

    write_complete_set(main_root)
    already_published = decide_preflight(
        inspect_canonical_set(main_root, TARGET_DATE),
        inspect_canonical_set(publish_root, TARGET_DATE),
    )
    assert already_published.status == ALREADY_PUBLISHED

    for path in main_root.rglob("*"):
        if path.is_file():
            path.unlink()
    write_complete_set(publish_root)
    already_in_progress = decide_preflight(
        inspect_canonical_set(main_root, TARGET_DATE),
        inspect_canonical_set(publish_root, TARGET_DATE),
    )
    assert already_in_progress.status == ALREADY_IN_PROGRESS

    for path in publish_root.rglob("*"):
        if path.is_file():
            path.unlink()
    ready = decide_preflight(
        inspect_canonical_set(main_root, TARGET_DATE),
        inspect_canonical_set(publish_root, TARGET_DATE),
    )
    assert ready.status == READY


def test_git_ref_gate_materializes_exact_paths_and_allows_a_missing_publish_branch(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-b", "main"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "tests@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Horizon Tests"], cwd=repo, check=True)
    write_complete_set(repo)
    subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "complete canonical set"], cwd=repo, check=True, capture_output=True)

    main = inspect_git_ref(repo, "HEAD", TARGET_DATE)
    missing_publish_branch = inspect_git_ref(
        repo,
        "refs/heads/automation/horizon-daily-publish",
        TARGET_DATE,
        missing_ref_is_absent=True,
    )

    assert main.status == COMPLETE
    assert missing_publish_branch.status == ABSENT


def test_gate_cli_emits_a_github_output_decision_for_exact_git_refs(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-b", "main"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "tests@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Horizon Tests"], cwd=repo, check=True)
    write_complete_set(repo)
    subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "complete canonical set"], cwd=repo, check=True, capture_output=True)
    github_output = tmp_path / "github-output"

    result = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).resolve().parents[1] / "scripts" / "horizon_daily_gate.py"),
            "preflight",
            "--repository",
            str(repo),
            "--target-date",
            TARGET_DATE,
            "--main-ref",
            "HEAD",
            "--publish-ref",
            "refs/heads/automation/horizon-daily-publish",
            "--github-output",
            str(github_output),
        ],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(result.stdout)["decision"] == ALREADY_PUBLISHED
    assert github_output.read_text(encoding="utf-8") == "decision=ALREADY_PUBLISHED\n"


def test_publish_branch_scope_rejects_a_pull_request_with_any_noncanonical_path(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-b", "main"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "tests@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Horizon Tests"], cwd=repo, check=True)
    write_complete_set(repo)
    subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "main canonical set"], cwd=repo, check=True, capture_output=True)
    subprocess.run(
        ["git", "checkout", "-b", "automation/horizon-daily-publish"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    (repo / "unexpected.md").write_text("unexpected\n", encoding="utf-8")
    subprocess.run(["git", "add", "unexpected.md"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "unexpected branch file"], cwd=repo, check=True, capture_output=True)

    scope = inspect_publish_branch_scope(
        repo,
        main_ref="main",
        publish_ref="HEAD",
        target_date=TARGET_DATE,
    )

    assert scope.valid is False
    assert scope.unexpected_paths == ("unexpected.md",)


def test_preflight_cli_fails_closed_when_the_publish_branch_has_an_unexpected_path(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "init", "-b", "main"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "tests@example.invalid"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Horizon Tests"], cwd=repo, check=True)
    write_complete_set(repo)
    subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "main canonical set"], cwd=repo, check=True, capture_output=True)
    subprocess.run(
        ["git", "checkout", "-b", "automation/horizon-daily-publish"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    (repo / "unexpected.md").write_text("unexpected\n", encoding="utf-8")
    subprocess.run(["git", "add", "unexpected.md"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "unexpected branch file"], cwd=repo, check=True, capture_output=True)

    result = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).resolve().parents[1] / "scripts" / "horizon_daily_gate.py"),
            "preflight",
            "--repository",
            str(repo),
            "--target-date",
            TARGET_DATE,
            "--main-ref",
            "main",
            "--publish-ref",
            "automation/horizon-daily-publish",
        ],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    payload = json.loads(result.stdout)
    assert result.returncode == 20, result.stdout + result.stderr
    assert payload["decision"] == CANONICAL_SET_INCOMPLETE
    assert payload["issues"] == ["PUBLISH_BRANCH_SCOPE_INVALID:unexpected.md"]
    assert payload["publish_branch_unexpected_paths"] == ["unexpected.md"]
