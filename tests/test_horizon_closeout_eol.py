from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HASHED_ARTIFACTS = (
    "changes/horizon-watchdog-least-privilege-token/tasks.md",
    "changes/horizon-watchdog-least-privilege-token/execution-contract.md",
)


def test_horizon_closeout_hash_inputs_are_forced_to_lf() -> None:
    completed = subprocess.run(
        ["git", "check-attr", "eol", "--", *HASHED_ARTIFACTS],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    attributes = {
        path: value
        for path, attribute, value in (
            line.split(": ", 2) for line in completed.stdout.splitlines()
        )
        if attribute == "eol"
    }

    assert attributes == {path: "lf" for path in HASHED_ARTIFACTS}
