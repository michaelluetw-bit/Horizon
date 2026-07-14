#!/usr/bin/env python3
"""Fail-closed canonical-set gate for Horizon daily publishing."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.automation.horizon_daily_gate import (  # noqa: E402
    CANONICAL_SET_INCOMPLETE,
    COMPLETE,
    GitReferenceError,
    PreflightDecision,
    decide_preflight,
    inspect_canonical_set,
    inspect_git_ref,
    inspect_publish_branch_scope,
)


def parser() -> argparse.ArgumentParser:
    command_parser = argparse.ArgumentParser(description=__doc__)
    commands = command_parser.add_subparsers(dest="command", required=True)

    preflight = commands.add_parser("preflight", help="inspect main and the fixed publish branch")
    preflight.add_argument("--repository", type=Path, required=True)
    preflight.add_argument("--target-date", required=True)
    preflight.add_argument("--main-ref", required=True)
    preflight.add_argument("--publish-ref", required=True)
    preflight.add_argument("--github-output", type=Path)

    validate = commands.add_parser("validate", help="inspect the generated local canonical set")
    validate.add_argument("--root", type=Path, required=True)
    validate.add_argument("--target-date", required=True)
    validate.add_argument("--github-output", type=Path)
    return command_parser


def append_github_output(path: Path | None, name: str, value: str) -> None:
    if path is None:
        return
    with path.open("a", encoding="utf-8", newline="\n") as output:
        output.write(f"{name}={value}\n")


def emit(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))


def run_preflight(arguments: argparse.Namespace) -> int:
    main = inspect_git_ref(arguments.repository, arguments.main_ref, arguments.target_date)
    publish_branch = inspect_git_ref(
        arguments.repository,
        arguments.publish_ref,
        arguments.target_date,
        missing_ref_is_absent=True,
    )
    scope = inspect_publish_branch_scope(
        arguments.repository,
        main_ref=arguments.main_ref,
        publish_ref=arguments.publish_ref,
        target_date=arguments.target_date,
    )
    decision = (
        decide_preflight(main, publish_branch)
        if scope.valid
        else PreflightDecision(
            CANONICAL_SET_INCOMPLETE,
            tuple(f"PUBLISH_BRANCH_SCOPE_INVALID:{path}" for path in scope.unexpected_paths),
        )
    )
    emit(
        {
            "decision": decision.status,
            "issues": list(decision.issues),
            "main_status": main.status,
            "publish_branch_status": publish_branch.status,
            "publish_branch_unexpected_paths": list(scope.unexpected_paths),
            "target_date": arguments.target_date,
        }
    )
    append_github_output(arguments.github_output, "decision", decision.status)
    return 20 if decision.status == CANONICAL_SET_INCOMPLETE else 0


def run_validate(arguments: argparse.Namespace) -> int:
    result = inspect_canonical_set(arguments.root, arguments.target_date)
    emit(
        {
            "issues": list(result.issues),
            "status": result.status,
            "target_date": arguments.target_date,
        }
    )
    append_github_output(arguments.github_output, "canonical_status", result.status)
    return 0 if result.status == COMPLETE else 21


def main() -> int:
    arguments = parser().parse_args()
    try:
        if arguments.command == "preflight":
            return run_preflight(arguments)
        return run_validate(arguments)
    except (GitReferenceError, ValueError, OSError) as error:
        print(f"CANONICAL_GATE_FAILED:{error}", file=sys.stderr)
        return 22


if __name__ == "__main__":
    raise SystemExit(main())
