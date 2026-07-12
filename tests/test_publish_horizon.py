from __future__ import annotations

import os
from pathlib import Path

import pytest

from scripts.publish_horizon import PublishError, convert_to_taiwan, publish, resolve_source


DATE = "2026-07-11"


def write_source(source_dir: Path, name: str = f"horizon-{DATE}-zh.md") -> Path:
    source_dir.mkdir(parents=True, exist_ok=True)
    source = source_dir / name
    source.write_text("# 每日摘要\n\n軟件、數據、網絡、人工智能、信息、用戶、視頻。\n", encoding="utf-8")
    return source


def test_resolve_source_uses_chinese_artifact(tmp_path: Path) -> None:
    source_dir = tmp_path / "summaries"
    expected = write_source(source_dir)

    assert resolve_source(source_dir, DATE) == expected


def test_resolve_source_uses_chinese_artifact_when_other_languages_exist(tmp_path: Path) -> None:
    source_dir = tmp_path / "summaries"
    expected = write_source(source_dir)
    write_source(source_dir, f"horizon-{DATE}-en.md")

    assert resolve_source(source_dir, DATE) == expected


@pytest.mark.parametrize(
    ("filenames", "status"),
    [
        ([], "SOURCE_NOT_FOUND"),
        ([f"horizon-{DATE}-en.md"], "SOURCE_INVALID"),
    ],
)
def test_resolve_source_rejects_missing_or_invalid_sources(tmp_path: Path, filenames: list[str], status: str) -> None:
    source_dir = tmp_path / "summaries"
    for filename in filenames:
        write_source(source_dir, filename)

    with pytest.raises(PublishError, match=status) as error:
        resolve_source(source_dir, DATE)

    assert error.value.status == status


def test_convert_to_taiwan_applies_fixed_terms() -> None:
    converted = convert_to_taiwan("軟件 數據 網絡 人工智能 信息 用戶 視頻")

    assert converted == "軟體 資料 網路 人工智慧 資訊 使用者 影片"


def test_publish_writes_required_frontmatter_sections_and_relative_source(tmp_path: Path) -> None:
    source_dir = tmp_path / "data" / "summaries"
    write_source(source_dir)
    target_dir = tmp_path / "vault" / "01_Horizon"

    result = publish(source_dir, target_dir, DATE, project_root=tmp_path)
    target = target_dir / f"{DATE}-horizon.md"
    output = target.read_text(encoding="utf-8")

    assert result == "SUCCESS"
    for field in (
        f'title: "{DATE} Horizon"',
        f'date: "{DATE}"',
        'module: "horizon"',
        'agent: "Horizon"',
        'status: "completed"',
        f'source: "data/summaries/horizon-{DATE}-zh.md"',
    ):
        assert field in output
    for heading in (
        "Bottom Line",
        "Signals",
        "Why It Matters",
        "Home Impact",
        "Save / Ignore Decision",
        "Next Action",
        "Sources",
    ):
        assert f"## {heading}" in output


def test_publish_is_idempotent_and_does_not_change_mtime(tmp_path: Path) -> None:
    source_dir = tmp_path / "data" / "summaries"
    write_source(source_dir)
    target_dir = tmp_path / "vault" / "01_Horizon"

    assert publish(source_dir, target_dir, DATE, project_root=tmp_path) == "SUCCESS"
    target = target_dir / f"{DATE}-horizon.md"
    first_mtime = target.stat().st_mtime_ns
    os.utime(target, ns=(first_mtime, first_mtime))

    assert publish(source_dir, target_dir, DATE, project_root=tmp_path) == "ALREADY_PUBLISHED"
    assert target.stat().st_mtime_ns == first_mtime


def test_invalid_source_does_not_replace_existing_artifact(tmp_path: Path) -> None:
    source_dir = tmp_path / "data" / "summaries"
    source_dir.mkdir(parents=True)
    (source_dir / f"horizon-{DATE}-zh.md").write_bytes(b"\xff\xfe")
    target_dir = tmp_path / "vault" / "01_Horizon"
    target_dir.mkdir(parents=True)
    target = target_dir / f"{DATE}-horizon.md"
    target.write_text("existing", encoding="utf-8")

    with pytest.raises(PublishError, match="SOURCE_INVALID"):
        publish(source_dir, target_dir, DATE, project_root=tmp_path)

    assert target.read_text(encoding="utf-8") == "existing"
