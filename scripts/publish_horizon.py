"""Publish Horizon summaries to the AI Executive Dashboard vault.

This script intentionally keeps Horizon as the producer and the dashboard vault
as a published-artifact target. It does not run AI or change Horizon's original
output files.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path

from opencc import OpenCC


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "data" / "summaries"
DEFAULT_DASHBOARD_HORIZON_DIR = Path(
    r"C:\Users\micha\Documents\2026_agent\download\knowledge\19_codex\AI Executive Dashboard\01_Horizon"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert Horizon summary Markdown to Traditional Chinese and publish it to Dashboard."
    )
    parser.add_argument(
        "--source",
        type=Path,
        help="Source Horizon Markdown file. Defaults to the newest *.md in data/summaries.",
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=DEFAULT_SOURCE_DIR,
        help="Directory to scan when --source is not provided.",
    )
    parser.add_argument(
        "--target-dir",
        type=Path,
        default=DEFAULT_DASHBOARD_HORIZON_DIR,
        help="Dashboard 01_Horizon directory.",
    )
    parser.add_argument(
        "--date",
        help="Artifact date in YYYY-MM-DD. Defaults to date parsed from filename, then today.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing dashboard artifact.",
    )
    return parser.parse_args()


def newest_markdown(source_dir: Path) -> Path:
    files = sorted(source_dir.glob("*.md"), key=lambda item: item.stat().st_mtime, reverse=True)
    if not files:
        raise FileNotFoundError(f"No Markdown files found in {source_dir}")
    return files[0]


def infer_date(source: Path, explicit_date: str | None) -> str:
    if explicit_date:
        validate_date(explicit_date)
        return explicit_date

    match = re.search(r"(20\d{2}-\d{2}-\d{2})", source.name)
    if match:
        validate_date(match.group(1))
        return match.group(1)

    return datetime.now().strftime("%Y-%m-%d")


def validate_date(value: str) -> None:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError(f"Invalid date, expected YYYY-MM-DD: {value}") from exc


def strip_frontmatter(markdown: str) -> str:
    return re.sub(r"\A---\s*\n.*?\n---\s*\n?", "", markdown, flags=re.DOTALL)


def first_content_line(markdown: str) -> str:
    for line in markdown.splitlines():
        clean = line.strip().lstrip("#").strip()
        if clean and not clean.startswith(">") and not clean.startswith("---"):
            return clean
    return "Horizon 原始摘要已轉換為繁體中文。"


def build_dashboard_markdown(source: Path, artifact_date: str, traditional_body: str) -> str:
    source_title = first_content_line(traditional_body)
    body_without_frontmatter = strip_frontmatter(traditional_body).strip()

    return f"""---
title: "{artifact_date} Horizon"
date: "{artifact_date}"
module: "horizon"
agent: "Horizon"
status: "completed"
source_type: "horizon-export"
source_path: "{source}"
tags:
  - ai-executive-dashboard
  - horizon
  - published-artifact
---

# {artifact_date} Horizon

## Bottom Line

Horizon 原始摘要已先轉換為繁體中文，再發布為 Dashboard 可讀取的今日 Horizon artifact。此檔案代表 Horizon 原始程式輸出已進入 Published Artifact 階段。

## Signals

- 來源檔案：`{source.name}`
- 原始標題：{source_title}
- 發布路徑：`01_Horizon/{artifact_date}-horizon.md`

## Why It Matters

這建立了 Producer → Published Artifact → Consumer 的邊界。Horizon 保持原始輸出位置不變，Dashboard 只讀既有 Vault 內的發布成果。

## Home Impact

Home 應顯示今日 Horizon artifact，而不是舊 proof 或 Horizon 原始資料夾內容。

## Save / Ignore Decision

待使用者閱讀今日內容後判斷。Publisher 只負責格式、轉換與發布，不代替內容品質決策。

## Next Action

在 Home 確認此 artifact 顯示為今日 Horizon，再填寫 7 天驗證 Day 1 四題。

## Sources

- Horizon 原始輸出：`{source}`

## Horizon 原始摘要（繁體中文）

{body_without_frontmatter}
"""


def main() -> None:
    args = parse_args()
    source = args.source or newest_markdown(args.source_dir)
    source = source.resolve()
    artifact_date = infer_date(source, args.date)
    target_dir = args.target_dir
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{artifact_date}-horizon.md"

    if target.exists() and not args.force:
        raise FileExistsError(f"Target already exists: {target}. Use --force to overwrite.")

    raw_markdown = source.read_text(encoding="utf-8")
    traditional_markdown = OpenCC("s2twp").convert(raw_markdown)
    dashboard_markdown = build_dashboard_markdown(source, artifact_date, traditional_markdown)
    target.write_text(dashboard_markdown, encoding="utf-8", newline="\n")

    print(f"Published: {target}")


if __name__ == "__main__":
    main()
