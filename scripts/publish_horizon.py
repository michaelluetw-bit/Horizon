"""Publish one canonical Horizon summary to the Dashboard vault."""

from __future__ import annotations

import argparse
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
DEFAULT_TARGET_DIR = Path(
    r"C:\Users\micha\Documents\2026_agent\download\knowledge\19_codex\AI Executive Dashboard\01_Horizon"
)
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


def build_output(source: Path, artifact_date: str, body: str, project_root: Path) -> str:
    try:
        source_ref = source.resolve().relative_to(project_root.resolve()).as_posix()
    except ValueError as exc:
        raise PublishError("SOURCE_INVALID", "Source must be inside the Horizon repository") from exc

    clean_body = re.sub(r"\A---\s*\n.*?\n---\s*\n?", "", body, flags=re.DOTALL).strip()
    if not clean_body:
        raise PublishError("SOURCE_INVALID", "Source Markdown is empty")

    return f'''---
title: "{artifact_date} Horizon"
date: "{artifact_date}"
module: "horizon"
agent: "Horizon"
status: "completed"
source: "{source_ref}"
source_type: "horizon-export"
tags:
  - ai-executive-dashboard
  - horizon
  - published-artifact
---

# {artifact_date} Horizon

## Bottom Line

Horizon 已產出 {artifact_date} 原始摘要，並以確定性格式發布至 Dashboard 的單一知識庫。

## Signals

- 來源檔案：`{source_ref}`
- 發布檔案：`01_Horizon/{artifact_date}-horizon.md`

## Why It Matters

此成果維持 Horizon、Published Artifact 與 Dashboard 之間的固定資料邊界。

## Home Impact

Home 應將此檔案識別為 {artifact_date} 的正式 Horizon artifact。

## Save / Ignore Decision

待每日閱讀驗證決定；Publisher 不代替內容品質判斷。

## Next Action

確認 Home 顯示今日 artifact，再進行每日內容品質驗證。

## Sources

- `{source_ref}`

## Horizon 原始摘要（繁體中文）

{clean_body}
'''


def validate_output(markdown: str, artifact_date: str, source_ref: str) -> None:
    required_fields = (
        f'title: "{artifact_date} Horizon"',
        f'date: "{artifact_date}"',
        'module: "horizon"',
        'agent: "Horizon"',
        'status: "completed"',
        f'source: "{source_ref}"',
    )
    missing_fields = [field for field in required_fields if field not in markdown]
    missing_headings = [heading for heading in REQUIRED_HEADINGS if f"## {heading}" not in markdown]
    if missing_fields or missing_headings:
        detail = ", ".join(missing_fields + missing_headings)
        raise PublishError("PUBLISH_FAILED", f"Output validation failed: {detail}")
    markdown.encode("utf-8", errors="strict")


def publish(source_dir: Path, target_dir: Path, artifact_date: str, *, project_root: Path = PROJECT_ROOT) -> str:
    source = resolve_source(source_dir, artifact_date)
    try:
        raw = source.read_text(encoding="utf-8", errors="strict")
    except UnicodeError as exc:
        raise PublishError("SOURCE_INVALID", f"Source is not valid UTF-8: {source}") from exc

    converted = convert_to_taiwan(raw)
    output = build_output(source, artifact_date, converted, project_root)
    source_ref = source.resolve().relative_to(project_root.resolve()).as_posix()
    validate_output(output, artifact_date, source_ref)

    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{artifact_date}-horizon.md"
    if target.exists() and target.read_text(encoding="utf-8", errors="strict") == output:
        return "ALREADY_PUBLISHED"

    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", newline="\n", dir=target_dir, prefix=f".{target.stem}-", suffix=".tmp", delete=False
        ) as handle:
            handle.write(output)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        validate_output(temporary.read_text(encoding="utf-8", errors="strict"), artifact_date, source_ref)
        os.replace(temporary, target)
    except PublishError:
        raise
    except Exception as exc:
        raise PublishError("PUBLISH_FAILED", str(exc)) from exc
    finally:
        if temporary and temporary.exists():
            temporary.unlink()
    return "SUCCESS"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish the canonical daily Horizon artifact.")
    parser.add_argument("--date", default=taipei_today(), help="Asia/Taipei date in YYYY-MM-DD")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--target-dir", type=Path, default=DEFAULT_TARGET_DIR)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        status = publish(args.source_dir, args.target_dir, args.date)
        print(f"STATUS={status}")
        return EXIT_CODES[status]
    except PublishError as exc:
        print(f"STATUS={exc.status}", file=sys.stderr)
        print(f"DETAIL={exc}", file=sys.stderr)
        return EXIT_CODES.get(exc.status, EXIT_CODES["PUBLISH_FAILED"])


if __name__ == "__main__":
    raise SystemExit(main())
