from __future__ import annotations

import hashlib
import os
from pathlib import Path

import pytest

from scripts.publish_horizon import (
    PublishError,
    append_log_entry,
    convert_to_taiwan,
    horizon_wiki_output,
    horizon_wiki_relative_path,
    publish,
    publish_blob,
    raw_relative_path,
    resolve_source,
    update_horizon_index,
)

DATE = "2026-07-11"


def write_source(source_dir: Path, name: str = f"horizon-{DATE}-zh.md") -> Path:
    source_dir.mkdir(parents=True, exist_ok=True)
    source = source_dir / name
    source.write_text(
        f"# Horizon 每日快遞 - {DATE}\n\n軟件、數據、網絡、人工智能、信息、用戶、視頻。\n",
        encoding="utf-8",
    )
    return source


def write_vault_baseline(vault_root: Path) -> None:
    wiki_dir = vault_root / "wiki"
    wiki_dir.mkdir(parents=True)
    (wiki_dir / "index.md").write_text(
        "---\ntitle: Wiki 索引\ntype: wiki\nstatus: active\ncreated: 2026-07-01\n---\n\n# Wiki 索引\n\n## 🚀 快速入口\n",
        encoding="utf-8",
    )
    (wiki_dir / "log.md").write_text(
        "---\ntitle: Wiki 攝取紀錄\ntype: wiki\nstatus: active\ncreated: 2026-07-01\n---\n\n# Wiki 攝取紀錄\n",
        encoding="utf-8",
    )


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


def test_publish_writes_raw_wiki_index_and_append_only_log(tmp_path: Path) -> None:
    source_dir = tmp_path / "data" / "summaries"
    write_source(source_dir)
    vault_root = tmp_path / "vault"
    write_vault_baseline(vault_root)

    result = publish(source_dir, vault_root, DATE, project_root=tmp_path)
    raw = vault_root / "raw" / "2026" / "07" / "11" / f"horizon-{DATE}-zh.md"
    wiki = vault_root / "wiki" / "Horizon" / f"{DATE} Horizon.md"
    wiki_output = wiki.read_text(encoding="utf-8")

    assert result == "SUCCESS"
    assert raw.read_text(encoding="utf-8") == write_source(source_dir).read_text(encoding="utf-8")
    assert not raw.read_text(encoding="utf-8").startswith("---")
    assert f'title: "{DATE} Horizon"' in wiki_output
    assert "type: wiki" in wiki_output
    assert "status: active" in wiki_output
    assert f"created: {DATE}" in wiki_output
    assert f"[[raw/2026/07/11/horizon-{DATE}-zh]]" in wiki_output
    assert f"[[wiki/Horizon/{DATE} Horizon|{DATE} Horizon]]" in (vault_root / "wiki" / "index.md").read_text(encoding="utf-8")
    assert (vault_root / "wiki" / "log.md").read_text(encoding="utf-8").count(f"horizon-{DATE}-zh.md") == 1


def test_publish_is_idempotent_and_does_not_change_mtime(tmp_path: Path) -> None:
    source_dir = tmp_path / "data" / "summaries"
    write_source(source_dir)
    vault_root = tmp_path / "vault"
    write_vault_baseline(vault_root)

    assert publish(source_dir, vault_root, DATE, project_root=tmp_path) == "SUCCESS"
    raw = vault_root / "raw" / "2026" / "07" / "11" / f"horizon-{DATE}-zh.md"
    wiki = vault_root / "wiki" / "Horizon" / f"{DATE} Horizon.md"
    first_raw_mtime = raw.stat().st_mtime_ns
    first_wiki_mtime = wiki.stat().st_mtime_ns
    os.utime(raw, ns=(first_raw_mtime, first_raw_mtime))
    os.utime(wiki, ns=(first_wiki_mtime, first_wiki_mtime))

    assert publish(source_dir, vault_root, DATE, project_root=tmp_path) == "ALREADY_PUBLISHED"
    assert raw.stat().st_mtime_ns == first_raw_mtime
    assert wiki.stat().st_mtime_ns == first_wiki_mtime


def test_publish_blob_normalizes_only_crlf_for_raw(tmp_path: Path) -> None:
    source_ref = f"data/summaries/horizon-{DATE}-zh.md"
    source_body = f"# Horizon 每日快遞 - {DATE}\r\n\r\n罕見字：臺灣、😀、軟件。\r\n"
    source_bytes = source_body.encode("utf-8")
    vault_root = tmp_path / "vault"
    write_vault_baseline(vault_root)

    assert publish_blob(source_bytes, vault_root, DATE, source_ref) == "SUCCESS"

    raw = vault_root / "raw" / "2026" / "07" / "11" / f"horizon-{DATE}-zh.md"
    assert raw.read_bytes() == source_body.replace("\r\n", "\n").encode("utf-8")


def test_publish_blob_rejects_frontmatter_without_writing_vault(tmp_path: Path) -> None:
    source_ref = f"data/summaries/horizon-{DATE}-zh.md"
    source_body = f"---\ntitle: source\n---\n# Horizon 每日快遞 - {DATE}\n"
    vault_root = tmp_path / "vault"
    write_vault_baseline(vault_root)
    index = (vault_root / "wiki" / "index.md").read_text(encoding="utf-8")
    log = (vault_root / "wiki" / "log.md").read_text(encoding="utf-8")

    with pytest.raises(PublishError, match="SOURCE_INVALID") as error:
        publish_blob(source_body.encode("utf-8"), vault_root, DATE, source_ref)

    assert error.value.status == "SOURCE_INVALID"
    assert not (vault_root / "raw").exists()
    assert not (vault_root / "wiki" / "Horizon").exists()
    assert (vault_root / "wiki" / "index.md").read_text(encoding="utf-8") == index
    assert (vault_root / "wiki" / "log.md").read_text(encoding="utf-8") == log


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


@pytest.mark.parametrize(
    ("source_body", "expected_raw_body", "expected_note"),
    [
        (
            f"# Horizon 每日快遞 - {DATE}\n\n摘要。\n",
            f"# Horizon 每日快遞 - {DATE}\n\n摘要。\n",
            "來源已為 LF，未發生換行轉換；來源與 Vault 落地 SHA-256 相同",
        ),
        (
            f"# Horizon 每日快遞 - {DATE}",
            f"# Horizon 每日快遞 - {DATE}",
            "來源未含換行字元；未發生換行轉換；來源與 Vault 落地 SHA-256 相同",
        ),
        (
            f"# Horizon 每日快遞 - {DATE}\r\n\r\n摘要。\r\n",
            f"# Horizon 每日快遞 - {DATE}\n\n摘要。\n",
            "已將 3 個 CRLF 轉為 LF；來源與 Vault 落地 SHA-256 不同",
        ),
        (
            f"# Horizon 每日快遞 - {DATE}\r\r摘要。\r",
            f"# Horizon 每日快遞 - {DATE}\r\r摘要。\r",
            "來源包含 3 個單獨 CR；本流程僅正規化 CRLF，Vault Raw 保留該位元組",
        ),
        (
            f"# Horizon 每日快遞 - {DATE}\r\n\n摘要。\r",
            f"# Horizon 每日快遞 - {DATE}\n\n摘要。\r",
            "已將 1 個 CRLF 轉為 LF；來源另含 1 個單獨 CR，Vault Raw 保留該位元組",
        ),
    ],
)
def test_publish_blob_reports_actual_line_endings(
    tmp_path: Path,
    source_body: str,
    expected_raw_body: str,
    expected_note: str,
) -> None:
    source_ref = f"data/summaries/horizon-{DATE}-zh.md"
    vault_root = tmp_path / "vault"
    write_vault_baseline(vault_root)

    assert publish_blob(source_body.encode("utf-8"), vault_root, DATE, source_ref) == "SUCCESS"

    raw = vault_root / raw_relative_path(DATE)
    wiki = vault_root / horizon_wiki_relative_path(DATE)
    assert raw.read_bytes() == expected_raw_body.encode("utf-8")
    assert f"> - 正規化：{expected_note}。" in wiki.read_text(encoding="utf-8")


def test_publish_blob_accepts_previous_provenance_format_as_already_published(tmp_path: Path) -> None:
    source_ref = f"data/summaries/horizon-{DATE}-zh.md"
    source_body = f"# Horizon 每日快遞 - {DATE}\r\n\r\n摘要。\r\n"
    source_bytes = source_body.encode("utf-8")
    raw_bytes = source_body.replace("\r\n", "\n").encode("utf-8")
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    raw_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    vault_root = tmp_path / "vault"
    write_vault_baseline(vault_root)

    raw_relative = raw_relative_path(DATE)
    wiki_relative = horizon_wiki_relative_path(DATE)
    raw_path = vault_root / raw_relative
    wiki_path = vault_root / wiki_relative
    raw_path.parent.mkdir(parents=True)
    raw_path.write_bytes(raw_bytes)
    legacy_note = "僅將 CRLF 轉為 LF；可見文字未變"
    legacy_wiki = horizon_wiki_output(
        DATE,
        source_ref,
        raw_relative,
        source_sha256,
        raw_sha256,
        source_body,
        legacy_note,
    )
    wiki_path.parent.mkdir(parents=True)
    wiki_path.write_bytes(legacy_wiki.encode("utf-8"))

    index_path = vault_root / "wiki" / "index.md"
    log_path = vault_root / "wiki" / "log.md"
    index_path.write_text(update_horizon_index(index_path.read_text(encoding="utf-8"), DATE), encoding="utf-8")
    raw_link = raw_relative.with_suffix("").as_posix()
    wiki_link = wiki_relative.with_suffix("").as_posix()
    legacy_log_entry = (
        f"- {DATE}：攝取 Horizon `origin/main` 的 `{source_ref}`，原文保存為 "
        f"[[{raw_link}|Horizon {DATE} 原始摘要]]，建立 [[{wiki_link}]]；"
        f"原始來源 SHA-256：`{source_sha256}`；Vault 落地 SHA-256：`{raw_sha256}`；{legacy_note}。"
    )
    log_path.write_text(append_log_entry(log_path.read_text(encoding="utf-8"), legacy_log_entry), encoding="utf-8")
    original_raw = raw_path.read_bytes()
    original_wiki = wiki_path.read_bytes()
    original_index = index_path.read_bytes()
    original_log = log_path.read_bytes()

    assert publish_blob(source_bytes, vault_root, DATE, source_ref) == "ALREADY_PUBLISHED"
    assert raw_path.read_bytes() == original_raw
    assert wiki_path.read_bytes() == original_wiki
    assert index_path.read_bytes() == original_index
    assert log_path.read_bytes() == original_log
