#!/usr/bin/env python3
"""Render and verify non-canonical Horizon execution evidence."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.automation.horizon_daily_evidence import (  # noqa: E402
    EvidenceError,
    build_evidence,
    verify_pr_body,
)


def parser() -> argparse.ArgumentParser:
    command_parser = argparse.ArgumentParser(description=__doc__)
    commands = command_parser.add_subparsers(dest="command", required=True)

    render = commands.add_parser("render", help="render manifest, PR body, and Step Summary")
    render.add_argument("--root", type=Path, required=True)
    render.add_argument("--target-date", required=True)
    render.add_argument("--provenance", type=Path, required=True)
    render.add_argument("--manifest", type=Path, required=True)
    render.add_argument("--pr-body", type=Path, required=True)
    render.add_argument("--step-summary", type=Path, required=True)
    render.add_argument("--run-id", type=int, required=True)
    render.add_argument("--run-attempt", type=int, required=True)
    render.add_argument("--workflow-sha", required=True)
    render.add_argument("--head-sha", required=True)
    render.add_argument("--branch", required=True)
    render.add_argument("--workflow-started-at", required=True)
    render.add_argument("--workflow-completed-at", required=True)
    render.add_argument("--artifact-name", required=True)

    verify = commands.add_parser("verify-pr-body", help="fail closed if a PR body differs from its manifest")
    verify.add_argument("--manifest", type=Path, required=True)
    verify.add_argument("--pr-body", type=Path, required=True)
    return command_parser


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise EvidenceError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def render(arguments: argparse.Namespace) -> int:
    workflow = {
        "run_id": arguments.run_id,
        "run_attempt": arguments.run_attempt,
        "workflow_sha": arguments.workflow_sha,
        "head_sha": arguments.head_sha,
        "branch": arguments.branch,
        "workflow_file": ".github/workflows/horizon_daily.yml",
        "workflow_started_at": arguments.workflow_started_at,
        "workflow_completed_at": arguments.workflow_completed_at,
        "artifact_name": arguments.artifact_name,
    }
    evidence = build_evidence(
        root=arguments.root,
        target_date=arguments.target_date,
        provenance=_load_json(arguments.provenance),
        workflow=workflow,
    )
    _write(arguments.manifest, f"{json.dumps(evidence.manifest, ensure_ascii=False, indent=2, sort_keys=True)}\n")
    _write(arguments.pr_body, evidence.pr_body)
    _write(arguments.step_summary, evidence.step_summary)
    print(json.dumps({"status": "EVIDENCE_RENDERED", "manifest": str(arguments.manifest)}))
    return 0


def verify(arguments: argparse.Namespace) -> int:
    manifest = _load_json(arguments.manifest)
    provenance = manifest.get("provenance")
    if not isinstance(provenance, dict):
        raise EvidenceError("PROVENANCE_MISMATCH:MANIFEST")
    verify_pr_body(arguments.pr_body.read_text(encoding="utf-8"), provenance)
    print(json.dumps({"status": "PR_BODY_VERIFIED"}))
    return 0


def main() -> int:
    arguments = parser().parse_args()
    try:
        if arguments.command == "render":
            return render(arguments)
        return verify(arguments)
    except (EvidenceError, OSError, ValueError, json.JSONDecodeError) as error:
        print(f"EVIDENCE_FAILED:{error}", file=sys.stderr)
        return 23


if __name__ == "__main__":
    raise SystemExit(main())
