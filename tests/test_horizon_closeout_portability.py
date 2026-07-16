from __future__ import annotations

import json
import subprocess
from pathlib import Path
from pathlib import PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
CHANGE_DIR = ROOT / "changes" / "horizon-watchdog-least-privilege-token"
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


def test_horizon_closeout_hash_inputs_are_lf_bytes() -> None:
    for relative_path in HASHED_ARTIFACTS:
        contents = (ROOT / relative_path).read_bytes()
        assert b"\r\n" not in contents, relative_path


def test_horizon_closeout_state_plain_scalars_have_no_mapping_indicators() -> None:
    state_lines = (CHANGE_DIR / ".spec-superflow.yaml").read_text(encoding="utf-8").splitlines()
    offending_fields = []

    for line in state_lines:
        if not line or line.startswith("#") or line[0].isspace():
            continue
        field, separator, value = line.partition(": ")
        if separator and ": " in value and not value.startswith(('"', "'", "|", ">")):
            offending_fields.append(field)

    assert offending_fields == []


def test_horizon_closeout_review_receipt_uses_portable_report_path() -> None:
    receipt_path = (
        CHANGE_DIR
        / ".superpowers"
        / "sdd"
        / "reviews"
        / "Y3JlZGVudGlhbC1yb3RhdGlvbg.json"
    )
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    report = receipt["report"]

    assert "\\" not in report
    report_path = CHANGE_DIR.joinpath(*PurePosixPath(report).parts)
    assert report_path.is_file()
