from __future__ import annotations

import base64
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

from src.automation.horizon_daily_evidence import EvidenceError, build_evidence, verify_pr_body


TARGET_DATE = "2026-07-14"


def write_complete_set(root: Path) -> None:
    files = {
        f"data/summaries/horizon-{TARGET_DATE}-zh.md": f"# Horizon 每日快遞 - {TARGET_DATE}\n\n內容。\n",
        f"data/summaries/horizon-{TARGET_DATE}-en.md": f"# Horizon Daily - {TARGET_DATE}\n\nContent.\n",
        f"docs/_posts/{TARGET_DATE}-summary-zh.md": (
            "---\nlayout: default\n"
            f"date: {TARGET_DATE}\nlang: zh\n"
            f'title: "Horizon Summary: {TARGET_DATE} (ZH)"\n---\n\n內容。\n'
        ),
        f"docs/_posts/{TARGET_DATE}-summary-en.md": (
            "---\nlayout: default\n"
            f"date: {TARGET_DATE}\nlang: en\n"
            f'title: "Horizon Summary: {TARGET_DATE} (EN)"\n---\n\nContent.\n'
        ),
    }
    for relative_path, content in files.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")


def watchdog_provenance() -> dict[str, object]:
    return {
        "trigger_source": "watchdog",
        "trigger_event": "workflow_dispatch",
        "trigger_schedule_expression": "0 23 * * *",
        "target_date": TARGET_DATE,
        "github": {
            "github_run_id": 123456,
            "github_run_attempt": 1,
            "repository": "michaelluetw-bit/Horizon",
            "workflow_ref": "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
            "commit_sha": "a" * 40,
            "event_name": "workflow_dispatch",
        },
        "receipt_signature": "signed-receipt",
        "receipt": {
            "jti": "j" * 43,
            "controller_cron": "0 23 * * *",
            "controller_scheduled_time": 1783983600000,
            "target_date": TARGET_DATE,
            "github_run_id": 123456,
            "github_run_attempt": 1,
            "repository": "michaelluetw-bit/Horizon",
            "workflow_ref": "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
            "commit_sha": "a" * 40,
            "redeemed_at": 1783970460,
            "receipt_id": "r" * 43,
            "provenance_verification_status": "verified",
        },
    }


def scheduled_verification_provenance() -> dict[str, object]:
    return {
        "trigger_source": "scheduled-verification",
        "trigger_event": "schedule",
        "trigger_schedule_expression": "5 0 * * *",
        "target_date": TARGET_DATE,
        "primary_schedule_on_time": False,
        "github": {
            "github_run_id": 123456,
            "github_run_attempt": 1,
            "repository": "michaelluetw-bit/Horizon",
            "workflow_ref": "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main",
            "commit_sha": "a" * 40,
            "event_name": "schedule",
        },
    }


def workflow_context() -> dict[str, object]:
    return {
        "run_id": 123456,
        "run_attempt": 1,
        "workflow_sha": "a" * 40,
        "head_sha": "a" * 40,
        "branch": "main",
        "workflow_file": ".github/workflows/horizon_daily.yml",
        "workflow_started_at": "2026-07-13T23:00:00Z",
        "workflow_completed_at": "2026-07-13T23:01:00Z",
        "artifact_name": "horizon-execution-manifest-123456",
    }


def test_watchdog_evidence_hashes_all_four_outputs_and_reuses_one_receipt_model(tmp_path: Path) -> None:
    write_complete_set(tmp_path)

    evidence = build_evidence(
        root=tmp_path,
        target_date=TARGET_DATE,
        provenance=watchdog_provenance(),
        workflow=workflow_context(),
    )

    manifest = evidence.manifest
    assert manifest["trigger_source"] == "watchdog"
    assert manifest["provenance"]["receipt_id"] == "r" * 43
    assert manifest["provenance"]["target_date"] == TARGET_DATE
    assert len(manifest["outputs"]) == 4
    expected_sha256 = hashlib.sha256(
        (tmp_path / f"data/summaries/horizon-{TARGET_DATE}-zh.md").read_bytes()
    ).hexdigest()
    assert manifest["outputs"][0]["sha256"] == expected_sha256
    assert "receipt_id" in evidence.step_summary
    assert "receipt_id" in evidence.pr_body
    verify_pr_body(evidence.pr_body, evidence.provenance_model)


def test_watchdog_evidence_rejects_receipt_context_mismatch_before_pr_creation(tmp_path: Path) -> None:
    write_complete_set(tmp_path)
    provenance = watchdog_provenance()
    provenance["receipt"]["github_run_id"] = 999  # type: ignore[index]

    with pytest.raises(EvidenceError, match="RECEIPT_CONTEXT_MISMATCH"):
        build_evidence(
            root=tmp_path,
            target_date=TARGET_DATE,
            provenance=provenance,
            workflow=workflow_context(),
        )


def test_scheduled_verification_evidence_records_the_actual_nonprimary_cron(tmp_path: Path) -> None:
    write_complete_set(tmp_path)

    evidence = build_evidence(
        root=tmp_path,
        target_date=TARGET_DATE,
        provenance=scheduled_verification_provenance(),
        workflow=workflow_context(),
    )

    assert evidence.manifest["trigger_source"] == "scheduled-verification"
    assert evidence.manifest["trigger_schedule_expression"] == "5 0 * * *"
    assert evidence.provenance_model["primary_schedule_on_time"] is False
    verify_pr_body(evidence.pr_body, evidence.provenance_model)


def test_evidence_cli_writes_only_noncanonical_run_files(tmp_path: Path) -> None:
    write_complete_set(tmp_path)
    provenance_path = tmp_path / "provenance.json"
    provenance_path.write_text(json.dumps(watchdog_provenance()), encoding="utf-8")
    manifest_path = tmp_path / "evidence" / "execution-manifest.json"
    body_path = tmp_path / "evidence" / "pr-body.md"
    summary_path = tmp_path / "evidence" / "step-summary.md"

    result = subprocess.run(
        [
            sys.executable,
            str(Path(__file__).resolve().parents[1] / "scripts" / "horizon_daily_evidence.py"),
            "render",
            "--root",
            str(tmp_path),
            "--target-date",
            TARGET_DATE,
            "--provenance",
            str(provenance_path),
            "--manifest",
            str(manifest_path),
            "--pr-body",
            str(body_path),
            "--step-summary",
            str(summary_path),
            "--run-id",
            "123456",
            "--run-attempt",
            "1",
            "--workflow-sha",
            "a" * 40,
            "--head-sha",
            "a" * 40,
            "--branch",
            "main",
            "--workflow-started-at",
            "2026-07-13T23:00:00Z",
            "--workflow-completed-at",
            "2026-07-13T23:01:00Z",
            "--artifact-name",
            "horizon-execution-manifest-123456",
        ],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(manifest_path.read_text(encoding="utf-8"))["run_id"] == 123456
    assert "receipt_id" in body_path.read_text(encoding="utf-8")
    assert "receipt_id" in summary_path.read_text(encoding="utf-8")


def test_pr_body_readback_rejects_any_provenance_model_mismatch(tmp_path: Path) -> None:
    write_complete_set(tmp_path)
    evidence = build_evidence(
        root=tmp_path,
        target_date=TARGET_DATE,
        provenance=watchdog_provenance(),
        workflow=workflow_context(),
    )
    altered_model = {**evidence.provenance_model, "target_date": "2026-07-15"}
    encoded = base64.urlsafe_b64encode(
        json.dumps(altered_model, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).decode("ascii").rstrip("=")
    altered = re.sub(
        r"(<!-- horizon-provenance-v1:)[A-Za-z0-9_-]+( -->)",
        rf"\g<1>{encoded}\g<2>",
        evidence.pr_body,
        count=1,
    )

    with pytest.raises(EvidenceError, match="PROVENANCE_MISMATCH"):
        verify_pr_body(altered, evidence.provenance_model)
