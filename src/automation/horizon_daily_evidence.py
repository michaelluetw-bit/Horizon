"""Non-canonical execution evidence for the Horizon daily workflow."""

from __future__ import annotations

import base64
import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping

from .horizon_daily_gate import COMPLETE, canonical_paths, inspect_canonical_set


HORIZON_REPOSITORY = "michaelluetw-bit/Horizon"
HORIZON_WORKFLOW_REF = (
    "michaelluetw-bit/Horizon/.github/workflows/horizon_daily.yml@refs/heads/main"
)
PRIMARY_CRON = "17 21 * * *"
WATCHDOG_CRON = "0 22 * * *"
PROVENANCE_MARKER = "horizon-provenance-v1"
_MARKER_PATTERN = re.compile(r"<!-- horizon-provenance-v1:([A-Za-z0-9_-]+) -->")
_JTI_PATTERN = re.compile(r"^[A-Za-z0-9_-]{43}$")


class EvidenceError(RuntimeError):
    """Evidence could not be derived from one verified provenance model."""


@dataclass(frozen=True)
class EvidenceDocuments:
    manifest: dict[str, Any]
    provenance_model: dict[str, Any]
    pr_body: str
    step_summary: str


def build_evidence(
    *,
    root: Path,
    target_date: str,
    provenance: Mapping[str, Any],
    workflow: Mapping[str, Any],
) -> EvidenceDocuments:
    _validate_target_date(target_date)
    canonical = inspect_canonical_set(root, target_date)
    if canonical.status != COMPLETE:
        raise EvidenceError(f"CANONICAL_SET_INCOMPLETE:{','.join(canonical.issues)}")

    normalized_workflow = _normalize_workflow(workflow)
    provenance_model, manual_actor, receipt_signature = _validate_provenance(
        provenance,
        target_date=target_date,
        workflow=normalized_workflow,
    )
    outputs = [
        {
            "path": relative_path,
            "sha256": hashlib.sha256((root / relative_path).read_bytes()).hexdigest(),
        }
        for relative_path in canonical_paths(target_date)
    ]
    manifest: dict[str, Any] = {
        "schema_version": 1,
        "timezone": "Asia/Taipei",
        "target_date": target_date,
        "configured_primary_schedule_expression": PRIMARY_CRON,
        "configured_watchdog_schedule_expression": WATCHDOG_CRON,
        "trigger_source": provenance_model["trigger_source"],
        "trigger_event": provenance_model["trigger_event"],
        "trigger_schedule_expression": provenance_model["trigger_schedule_expression"],
        "workflow_started_at": normalized_workflow["workflow_started_at"],
        "workflow_completed_at": normalized_workflow["workflow_completed_at"],
        "run_id": normalized_workflow["run_id"],
        "run_attempt": normalized_workflow["run_attempt"],
        "workflow_sha": normalized_workflow["workflow_sha"],
        "workflow_file": normalized_workflow["workflow_file"],
        "head_sha": normalized_workflow["head_sha"],
        "branch": normalized_workflow["branch"],
        "artifact_name": normalized_workflow["artifact_name"],
        "provenance": provenance_model,
        "outputs": outputs,
    }
    if manual_actor:
        manifest["github_actor"] = manual_actor
    if receipt_signature:
        manifest["receipt_signature"] = receipt_signature

    marker = _provenance_marker(provenance_model)
    common_markdown = _render_provenance_markdown(provenance_model)
    pr_body = (
        f"{marker}\n"
        "此 PR 由 Horizon Daily Aggregation 自動建立或更新。\n\n"
        "## P0-B2R execution provenance\n\n"
        f"{common_markdown}\n\n"
        "`ruff` 與 `test` 均通過後，GitHub 會依 repository auto-merge 設定自動合併。\n"
    )
    step_summary = (
        f"{marker}\n"
        "## Horizon P0-B2R execution evidence\n\n"
        f"{common_markdown}\n\n"
        f"- 四檔 canonical outputs：`{len(outputs)}`\n"
        f"- manifest artifact：`{normalized_workflow['artifact_name']}`\n"
    )
    return EvidenceDocuments(
        manifest=manifest,
        provenance_model=provenance_model,
        pr_body=pr_body,
        step_summary=step_summary,
    )


def verify_pr_body(pr_body: str, expected_provenance_model: Mapping[str, Any]) -> None:
    matches = _MARKER_PATTERN.findall(pr_body)
    if len(matches) != 1:
        raise EvidenceError("PROVENANCE_MISMATCH:PR_BODY_MARKER_INVALID")
    try:
        padding = "=" * ((4 - len(matches[0]) % 4) % 4)
        actual = json.loads(base64.urlsafe_b64decode(f"{matches[0]}{padding}"))
    except (ValueError, json.JSONDecodeError):
        raise EvidenceError("PROVENANCE_MISMATCH:PR_BODY_MARKER_INVALID") from None
    if _canonical_json(actual) != _canonical_json(dict(expected_provenance_model)):
        raise EvidenceError("PROVENANCE_MISMATCH:PR_BODY")


def _normalize_workflow(workflow: Mapping[str, Any]) -> dict[str, Any]:
    required_integer_fields = ("run_id", "run_attempt")
    for key in required_integer_fields:
        if not isinstance(workflow.get(key), int) or workflow[key] <= 0:
            raise EvidenceError(f"WORKFLOW_CONTEXT_INVALID:{key}")
    required_string_fields = (
        "workflow_sha",
        "head_sha",
        "branch",
        "workflow_file",
        "workflow_started_at",
        "workflow_completed_at",
        "artifact_name",
    )
    normalized: dict[str, Any] = {}
    for key in required_string_fields:
        value = workflow.get(key)
        if not isinstance(value, str) or not value:
            raise EvidenceError(f"WORKFLOW_CONTEXT_INVALID:{key}")
        normalized[key] = value
    for key in required_integer_fields:
        normalized[key] = workflow[key]
    if normalized["workflow_file"] != ".github/workflows/horizon_daily.yml":
        raise EvidenceError("WORKFLOW_CONTEXT_INVALID:workflow_file")
    if normalized["branch"] != "main":
        raise EvidenceError("WORKFLOW_CONTEXT_INVALID:branch")
    if not all(re.fullmatch(r"[a-fA-F0-9]{40}", normalized[key]) for key in ("workflow_sha", "head_sha")):
        raise EvidenceError("WORKFLOW_CONTEXT_INVALID:sha")
    return normalized


def _validate_provenance(
    provenance: Mapping[str, Any],
    *,
    target_date: str,
    workflow: Mapping[str, Any],
) -> tuple[dict[str, Any], str | None, str | None]:
    source = provenance.get("trigger_source")
    event = provenance.get("trigger_event")
    schedule_expression = provenance.get("trigger_schedule_expression")
    if provenance.get("target_date") != target_date:
        raise EvidenceError("PROVENANCE_MISMATCH:target_date")
    _validate_github_context(provenance.get("github"), workflow, event)

    base_model: dict[str, Any] = {
        "trigger_source": source,
        "trigger_event": event,
        "trigger_schedule_expression": schedule_expression,
        "target_date": target_date,
        "github_run_id": workflow["run_id"],
        "github_run_attempt": workflow["run_attempt"],
        "workflow_sha": workflow["workflow_sha"],
        "manifest_artifact_name": workflow["artifact_name"],
    }
    if source == "primary":
        on_time = provenance.get("primary_schedule_on_time")
        if (
            event != "schedule"
            or schedule_expression != PRIMARY_CRON
            or not isinstance(on_time, bool)
        ):
            raise EvidenceError("PROVENANCE_MISMATCH:primary")
        base_model["provenance_verification_status"] = "not_applicable"
        base_model["primary_schedule_on_time"] = on_time
        return base_model, None, None
    if source == "scheduled-verification":
        on_time = provenance.get("primary_schedule_on_time")
        if (
            event != "schedule"
            or not isinstance(schedule_expression, str)
            or not schedule_expression
            or schedule_expression == PRIMARY_CRON
            or on_time is not False
        ):
            raise EvidenceError("PROVENANCE_MISMATCH:scheduled_verification")
        base_model["provenance_verification_status"] = "not_applicable"
        base_model["primary_schedule_on_time"] = False
        return base_model, None, None
    if source == "manual":
        actor = provenance.get("github_actor")
        if event != "workflow_dispatch" or schedule_expression is not None or not isinstance(actor, str) or not actor:
            raise EvidenceError("PROVENANCE_MISMATCH:manual")
        base_model["provenance_verification_status"] = "not_applicable"
        return base_model, actor, None
    if source != "watchdog" or event != "workflow_dispatch":
        raise EvidenceError("PROVENANCE_MISMATCH:source")

    receipt = provenance.get("receipt")
    receipt_signature = provenance.get("receipt_signature")
    if not isinstance(receipt, Mapping) or not isinstance(receipt_signature, str) or not receipt_signature:
        raise EvidenceError("PROVENANCE_MISMATCH:receipt_missing")
    _validate_receipt(receipt, target_date, workflow)
    if schedule_expression != receipt["controller_cron"]:
        raise EvidenceError("PROVENANCE_MISMATCH:controller_cron")
    base_model.update(
        {
            "receipt_id": receipt["receipt_id"],
            "jti": receipt["jti"],
            "controller_cron": receipt["controller_cron"],
            "controller_scheduled_time": receipt["controller_scheduled_time"],
            "provenance_verification_status": receipt["provenance_verification_status"],
        }
    )
    return base_model, None, receipt_signature


def _validate_github_context(github: Any, workflow: Mapping[str, Any], event: Any) -> None:
    if not isinstance(github, Mapping):
        raise EvidenceError("PROVENANCE_MISMATCH:github_context")
    expected = {
        "github_run_id": workflow["run_id"],
        "github_run_attempt": workflow["run_attempt"],
        "repository": HORIZON_REPOSITORY,
        "workflow_ref": HORIZON_WORKFLOW_REF,
        "commit_sha": workflow["head_sha"],
        "event_name": event,
    }
    if any(github.get(key) != value for key, value in expected.items()):
        raise EvidenceError("PROVENANCE_MISMATCH:github_context")


def _validate_receipt(receipt: Mapping[str, Any], target_date: str, workflow: Mapping[str, Any]) -> None:
    expected = {
        "controller_cron": WATCHDOG_CRON,
        "target_date": target_date,
        "github_run_id": workflow["run_id"],
        "github_run_attempt": workflow["run_attempt"],
        "repository": HORIZON_REPOSITORY,
        "workflow_ref": HORIZON_WORKFLOW_REF,
        "commit_sha": workflow["head_sha"],
        "provenance_verification_status": "verified",
    }
    if any(receipt.get(key) != value for key, value in expected.items()):
        raise EvidenceError("RECEIPT_CONTEXT_MISMATCH")
    if not _JTI_PATTERN.fullmatch(str(receipt.get("jti", ""))):
        raise EvidenceError("RECEIPT_CONTEXT_MISMATCH")
    if not _JTI_PATTERN.fullmatch(str(receipt.get("receipt_id", ""))):
        raise EvidenceError("RECEIPT_CONTEXT_MISMATCH")
    if not isinstance(receipt.get("controller_scheduled_time"), int) or receipt["controller_scheduled_time"] <= 0:
        raise EvidenceError("RECEIPT_CONTEXT_MISMATCH")
    if not isinstance(receipt.get("redeemed_at"), int) or receipt["redeemed_at"] <= 0:
        raise EvidenceError("RECEIPT_CONTEXT_MISMATCH")


def _validate_target_date(target_date: str) -> None:
    try:
        date.fromisoformat(target_date)
    except (TypeError, ValueError) as error:
        raise EvidenceError("PROVENANCE_MISMATCH:target_date") from error


def _canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _provenance_marker(model: Mapping[str, Any]) -> str:
    encoded = base64.urlsafe_b64encode(_canonical_json(dict(model)).encode("utf-8")).decode("ascii").rstrip("=")
    return f"<!-- {PROVENANCE_MARKER}:{encoded} -->"


def _render_provenance_markdown(model: Mapping[str, Any]) -> str:
    return f"```json\n{json.dumps(dict(model), ensure_ascii=False, indent=2, sort_keys=True)}\n```"
