"""Publish one canonical Horizon summary to the Dashboard vault."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from opencc import OpenCC


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "data" / "summaries"
DEFAULT_VAULT_ROOT = Path(r"C:\Users\micha\Documents\myvault")
TAIPEI = ZoneInfo("Asia/Taipei")
EXIT_CODES = {
    "SUCCESS": 0,
    "ALREADY_PUBLISHED": 0,
    "SOURCE_NOT_FOUND": 20,
    "AMBIGUOUS_SOURCE": 21,
    "SOURCE_INVALID": 22,
    "PUBLISH_FAILED": 30,
}
REQUIRED_HEADINGS = (
    "Bottom Line",
    "Signals",
    "Why It Matters",
    "Home Impact",
    "Save / Ignore Decision",
    "Next Action",
    "Sources",
)
TAIWAN_TERMS = (
    ("軟件", "軟體"),
    ("數據", "資料"),
    ("網絡", "網路"),
    ("人工智能", "人工智慧"),
    ("信息", "資訊"),
    ("用戶", "使用者"),
    ("視頻", "影片"),
)


class PublishError(RuntimeError):
    def __init__(self, status: str, detail: str):
        self.status = status
        super().__init__(f"{status}: {detail}")


def validate_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise PublishError("SOURCE_INVALID", f"Invalid date: {value}") from exc
    return value


def taipei_today() -> str:
    return datetime.now(TAIPEI).strftime("%Y-%m-%d")


def resolve_source(source_dir: Path, artifact_date: str) -> Path:
    validate_date(artifact_date)
    expected = source_dir / f"horizon-{artifact_date}-zh.md"
    if expected.is_file():
        return expected

    matches = sorted(source_dir.glob(f"horizon-{artifact_date}-*.md")) if source_dir.exists() else []
    if not matches:
        raise PublishError("SOURCE_NOT_FOUND", f"No source for {artifact_date}")

    raise PublishError("SOURCE_INVALID", f"Expected {expected.name}, found {', '.join(item.name for item in matches)}")


def convert_to_taiwan(markdown: str) -> str:
    converted = OpenCC("s2twp").convert(markdown)
    for source, target in TAIWAN_TERMS:
        converted = converted.replace(source, target)
    return converted


def validate_source_markdown(markdown: str, artifact_date: str) -> None:
    if markdown.startswith("---\n") or markdown.startswith("---\r\n"):
        raise PublishError("SOURCE_INVALID", "Source must not contain YAML frontmatter")
    clean_body = markdown.strip()
    if not clean_body:
        raise PublishError("SOURCE_INVALID", "Source Markdown is empty")
    expected_heading = f"# Horizon 每日快遞 - {artifact_date}"
    if clean_body.splitlines()[0] != expected_heading:
        raise PublishError("SOURCE_INVALID", f"Expected heading: {expected_heading}")


def normalize_raw_bytes(source_bytes: bytes, artifact_date: str) -> tuple[str, bytes]:
    try:
        source_text = source_bytes.decode("utf-8", errors="strict")
    except UnicodeError as exc:
        raise PublishError("SOURCE_INVALID", "Source is not valid UTF-8") from exc
    validate_source_markdown(source_text, artifact_date)
    return source_text, source_text.replace("\r\n", "\n").encode("utf-8")


def raw_relative_path(artifact_date: str) -> Path:
    year, month, day = artifact_date.split("-")
    return Path("raw") / year / month / day / f"horizon-{artifact_date}-zh.md"


def horizon_wiki_relative_path(artifact_date: str) -> Path:
    return Path("wiki") / "Horizon" / f"{artifact_date} Horizon.md"


def wiki_link(relative: Path) -> str:
    return relative.with_suffix("").as_posix()


def horizon_wiki_output(
    artifact_date: str,
    source_ref: str,
    raw_relative: Path,
    source_sha256: str,
    raw_sha256: str,
    raw_text: str,
) -> str:
    heading = f"# Horizon 每日快遞 - {artifact_date}"
    content = raw_text.replace("\r\n", "\n")
    if content.startswith(heading):
        content = content[len(heading) :].lstrip("\n")
    raw_link = wiki_link(raw_relative)
    return f'''---
title: "{artifact_date} Horizon"
type: wiki
status: active
created: {artifact_date}
sources:
  - "[[{raw_link}]]"
---

{heading}

> [!info] 原始來源
> - Horizon `origin/main`：`{source_ref}`
> - Vault 原文：[[{raw_link}|Horizon {artifact_date} 原始摘要]]
> - 原始來源 SHA-256：`{source_sha256}`
> - Vault 落地 SHA-256：`{raw_sha256}`
> - 正規化：僅將 CRLF 轉為 LF；可見文字未變。

## Bottom Line

Horizon {artifact_date} 原始摘要已攝取；內容與來源可由下方 Wiki 與 Raw 交叉查閱。

## Horizon 原始摘要

{content.rstrip()}
'''


def require_text(path: Path, label: str) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="strict")
    except OSError as exc:
        raise PublishError("PUBLISH_FAILED", f"Missing {label}: {path}") from exc


def update_horizon_index(index: str, artifact_date: str) -> str:
    link = f"- **Horizon 每日快遞**：[[wiki/Horizon/{artifact_date} Horizon|{artifact_date} Horizon]]"
    newline = "\r\n" if "\r\n" in index else "\n"
    pattern = re.compile(r"(?m)^- \*\*Horizon 每日快遞\*\*：.*$")
    if pattern.search(index):
        return pattern.sub(link, index)
    marker = "## 🚀 快速入口"
    if marker not in index:
        raise PublishError("PUBLISH_FAILED", "Wiki index is missing the quick-entry section")
    return index.replace(marker, f"{marker}{newline}{newline}{link}", 1)


def append_log_entry(log: str, entry: str) -> str:
    if entry in log:
        return log
    newline = "\r\n" if "\r\n" in log else "\n"
    return f"{log.rstrip()}" + newline + entry + newline


def existing_matches(path: Path, expected: bytes) -> bool:
    if not path.exists():
        return False
    try:
        return path.read_bytes() == expected
    except OSError as exc:
        raise PublishError("PUBLISH_FAILED", f"Unable to read existing file: {path}") from exc


def write_new_or_match(path: Path, expected: bytes, label: str) -> bool:
    if path.exists():
        if existing_matches(path, expected):
            return False
        raise PublishError("PUBLISH_FAILED", f"Existing {label} differs: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=path.parent, prefix=f".{path.stem}-", suffix=".tmp", delete=False) as handle:
            handle.write(expected)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        os.replace(temporary, path)
    except OSError as exc:
        raise PublishError("PUBLISH_FAILED", str(exc)) from exc
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    return True


def write_if_changed(path: Path, content: str) -> bool:
    expected = content.encode("utf-8")
    if path.exists() and path.read_bytes() == expected:
        return False
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile("wb", dir=path.parent, prefix=f".{path.stem}-", suffix=".tmp", delete=False) as handle:
            handle.write(expected)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        os.replace(temporary, path)
    except OSError as exc:
        raise PublishError("PUBLISH_FAILED", str(exc)) from exc
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    return True


def source_ref_for(source: Path, project_root: Path) -> str:
    try:
        return source.resolve().relative_to(project_root.resolve()).as_posix()
    except ValueError as exc:
        raise PublishError("SOURCE_INVALID", "Source must be inside the Horizon repository") from exc


def publish_markdown(source_bytes: bytes, vault_root: Path, artifact_date: str, source_ref: str) -> str:
    validate_date(artifact_date)
    expected_source_ref = f"data/summaries/horizon-{artifact_date}-zh.md"
    if source_ref != expected_source_ref:
        raise PublishError("SOURCE_INVALID", f"Expected source {expected_source_ref}, found {source_ref}")

    source_text, raw_bytes = normalize_raw_bytes(source_bytes, artifact_date)
    raw_relative = raw_relative_path(artifact_date)
    wiki_relative = horizon_wiki_relative_path(artifact_date)
    raw_path = vault_root / raw_relative
    wiki_path = vault_root / wiki_relative
    index_path = vault_root / "wiki" / "index.md"
    log_path = vault_root / "wiki" / "log.md"
    index = require_text(index_path, "wiki/index.md")
    log = require_text(log_path, "wiki/log.md")
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    raw_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    wiki = horizon_wiki_output(artifact_date, source_ref, raw_relative, source_sha256, raw_sha256, source_text)
    log_entry = (
        f"- {artifact_date}：攝取 Horizon `origin/main` 的 `{source_ref}`，原文保存為 "
        f"[[{wiki_link(raw_relative)}|Horizon {artifact_date} 原始摘要]]，建立 "
        f"[[{wiki_link(wiki_relative)}]]；原始來源 SHA-256：`{source_sha256}`；"
        f"Vault 落地 SHA-256：`{raw_sha256}`；僅 CRLF→LF 正規化，可見文字未變。"
    )
    updated_index = update_horizon_index(index, artifact_date)
    updated_log = append_log_entry(log, log_entry)

    if wiki_path.exists() and not existing_matches(wiki_path, wiki.encode("utf-8")):
        raise PublishError("PUBLISH_FAILED", f"Existing Horizon Wiki differs: {wiki_path}")

    changed = write_new_or_match(raw_path, raw_bytes, "Raw")
    changed = write_new_or_match(wiki_path, wiki.encode("utf-8"), "Horizon Wiki") or changed
    changed = write_if_changed(index_path, updated_index) or changed
    changed = write_if_changed(log_path, updated_log) or changed
    return "SUCCESS" if changed else "ALREADY_PUBLISHED"


def publish_blob(source_bytes: bytes, vault_root: Path, artifact_date: str, source_ref: str) -> str:
    return publish_markdown(source_bytes, vault_root, artifact_date, source_ref)


def publish(source_dir: Path, vault_root: Path, artifact_date: str, *, project_root: Path = PROJECT_ROOT) -> str:
    source = resolve_source(source_dir, artifact_date)
    try:
        source_bytes = source.read_bytes()
    except OSError as exc:
        raise PublishError("SOURCE_INVALID", f"Unable to read source: {source}") from exc
    return publish_blob(source_bytes, vault_root, artifact_date, source_ref_for(source, project_root))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish the canonical daily Horizon artifact.")
    parser.add_argument("--date", default=taipei_today(), help="Asia/Taipei date in YYYY-MM-DD")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--vault-root", "--target-dir", dest="vault_root", type=Path, default=DEFAULT_VAULT_ROOT)
    parser.add_argument("--source-file", type=Path, help="Read an authoritative UTF-8 source blob from this file")
    parser.add_argument("--source-ref", help="Repository-relative path for --source-file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.source_file or args.source_ref:
            if not args.source_file or not args.source_ref:
                raise PublishError("SOURCE_INVALID", "--source-file and --source-ref must be supplied together")
            try:
                source_bytes = args.source_file.read_bytes()
            except OSError as exc:
                raise PublishError("SOURCE_INVALID", f"Unable to read source file: {args.source_file}") from exc
            status = publish_blob(source_bytes, args.vault_root, args.date, args.source_ref)
        else:
            status = publish(args.source_dir, args.vault_root, args.date)
        print(f"STATUS={status}")
        return EXIT_CODES[status]
    except PublishError as exc:
        print(f"STATUS={exc.status}", file=sys.stderr)
        print(f"DETAIL={exc}", file=sys.stderr)
        return EXIT_CODES.get(exc.status, EXIT_CODES["PUBLISH_FAILED"])


if __name__ == "__main__":
    raise SystemExit(main())
