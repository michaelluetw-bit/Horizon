from __future__ import annotations

import re
import subprocess
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator


ABSENT = "ABSENT"
COMPLETE = "COMPLETE"
CANONICAL_SET_INCOMPLETE = "CANONICAL_SET_INCOMPLETE"
ALREADY_PUBLISHED = "ALREADY_PUBLISHED"
ALREADY_IN_PROGRESS = "ALREADY_IN_PROGRESS"
READY = "READY"

# Flag placeholder markers only when they lead a line (optionally after
# Markdown heading/list/quote punctuation) or appear in bracketed marker
# form ([TODO], {placeholder}, <tbd>). A summary that merely mentions such
# a word mid-sentence (e.g. news about "TODO apps") must not block
# publishing.
PLACEHOLDER_PATTERN = re.compile(
    r"(?m)(?:^[ \t]*(?:[#>*+-][ \t]*)*(?:placeholder|todo|tbd)\b"
    r"|[\[{<](?:placeholder|todo|tbd)[\]}>])",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class CanonicalSetResult:
    status: str
    paths: tuple[str, ...]
    issues: tuple[str, ...] = ()


@dataclass(frozen=True)
class PreflightDecision:
    status: str
    issues: tuple[str, ...] = ()


@dataclass(frozen=True)
class PublishBranchScopeResult:
    valid: bool
    unexpected_paths: tuple[str, ...] = ()


class GitReferenceError(RuntimeError):
    """A required git ref or blob could not be read deterministically."""


def canonical_paths(target_date: str) -> tuple[str, ...]:
    _parse_target_date(target_date)
    return (
        f"data/summaries/horizon-{target_date}-zh.md",
        f"data/summaries/horizon-{target_date}-en.md",
        f"docs/_posts/{target_date}-summary-zh.md",
        f"docs/_posts/{target_date}-summary-en.md",
    )


def inspect_canonical_set(root: Path, target_date: str) -> CanonicalSetResult:
    paths = canonical_paths(target_date)
    existing_paths = [relative_path for relative_path in paths if (root / relative_path).is_file()]
    if not existing_paths:
        return CanonicalSetResult(ABSENT, paths)

    issues: list[str] = []
    for relative_path in paths:
        path = root / relative_path
        if not path.is_file():
            issues.append(f"MISSING:{relative_path}")
            continue
        issues.extend(_validate_markdown(path, relative_path, target_date))

    if issues:
        return CanonicalSetResult(CANONICAL_SET_INCOMPLETE, paths, tuple(issues))
    return CanonicalSetResult(COMPLETE, paths)


def inspect_git_ref(
    repository: Path,
    ref: str,
    target_date: str,
    *,
    missing_ref_is_absent: bool = False,
) -> CanonicalSetResult:
    """Apply the canonical gate to exact blobs from one immutable git ref."""
    paths = canonical_paths(target_date)
    if not _git_ref_exists(repository, ref):
        if missing_ref_is_absent:
            return CanonicalSetResult(ABSENT, paths)
        raise GitReferenceError(f"GIT_REF_NOT_FOUND:{ref}")

    with _temporary_root() as root:
        for relative_path in paths:
            tree_entry = _git(repository, ["ls-tree", "-z", ref, "--", relative_path])
            if not tree_entry.stdout:
                continue
            blob = _git(repository, ["show", f"{ref}:{relative_path}"], text=False)
            output_path = root / relative_path
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_bytes(blob.stdout)
        return inspect_canonical_set(root, target_date)


def inspect_publish_branch_scope(
    repository: Path,
    *,
    main_ref: str,
    publish_ref: str,
    target_date: str,
) -> PublishBranchScopeResult:
    """Require the fixed publish branch's PR diff to contain only the four exact paths."""
    if not _git_ref_exists(repository, main_ref):
        raise GitReferenceError(f"GIT_REF_NOT_FOUND:{main_ref}")
    if not _git_ref_exists(repository, publish_ref):
        return PublishBranchScopeResult(valid=True)
    changed = _git(
        repository,
        ["diff", "--name-only", f"{main_ref}...{publish_ref}"],
        text=True,
    ).stdout.splitlines()
    allowed_paths = set(canonical_paths(target_date))
    unexpected_paths = tuple(sorted(path for path in changed if path not in allowed_paths))
    return PublishBranchScopeResult(valid=not unexpected_paths, unexpected_paths=unexpected_paths)


def decide_preflight(main: CanonicalSetResult, publish_branch: CanonicalSetResult) -> PreflightDecision:
    if main.status == COMPLETE:
        return PreflightDecision(ALREADY_PUBLISHED)
    if main.status != ABSENT:
        return PreflightDecision(CANONICAL_SET_INCOMPLETE, main.issues)
    if publish_branch.status == COMPLETE:
        return PreflightDecision(ALREADY_IN_PROGRESS)
    if publish_branch.status != ABSENT:
        return PreflightDecision(CANONICAL_SET_INCOMPLETE, publish_branch.issues)
    return PreflightDecision(READY)


@contextmanager
def _temporary_root() -> Iterator[Path]:
    with TemporaryDirectory(prefix="horizon-daily-gate-") as directory:
        yield Path(directory)


def _git_ref_exists(repository: Path, ref: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"],
        cwd=repository,
        check=False,
        capture_output=True,
    )
    if result.returncode == 0:
        return True
    if result.returncode == 1:
        return False
    raise GitReferenceError(f"GIT_REF_LOOKUP_FAILED:{ref}")


def _git(repository: Path, arguments: list[str], *, text: bool = False) -> subprocess.CompletedProcess[str] | subprocess.CompletedProcess[bytes]:
    result = subprocess.run(
        ["git", *arguments],
        cwd=repository,
        check=False,
        capture_output=True,
        text=text,
        encoding="utf-8" if text else None,
        errors="strict" if text else None,
    )
    if result.returncode != 0:
        raise GitReferenceError(f"GIT_BLOB_READ_FAILED:{' '.join(arguments)}")
    return result


def _parse_target_date(target_date: str) -> date:
    try:
        return date.fromisoformat(target_date)
    except (TypeError, ValueError) as exc:
        raise ValueError("target_date must use YYYY-MM-DD") from exc


def _validate_markdown(path: Path, relative_path: str, target_date: str) -> list[str]:
    try:
        content = path.read_text(encoding="utf-8", errors="strict")
    except (OSError, UnicodeError):
        return [f"UTF8_INVALID:{relative_path}"]

    issues: list[str] = []
    if not content.strip():
        issues.append(f"BODY_EMPTY:{relative_path}")
    if target_date not in content:
        issues.append(f"TARGET_DATE_MISSING:{relative_path}")
    if PLACEHOLDER_PATTERN.search(content):
        issues.append(f"PLACEHOLDER_PRESENT:{relative_path}")

    if relative_path.startswith("data/summaries/"):
        expected_title = (
            f"# Horizon 每日快遞 - {target_date}"
            if relative_path.endswith("-zh.md")
            else f"# Horizon Daily - {target_date}"
        )
        if not content.startswith(f"{expected_title}\n"):
            issues.append(f"SUMMARY_TITLE_INVALID:{relative_path}")
        return issues

    issues.extend(_validate_post(content, relative_path, target_date))
    return issues


def _validate_post(content: str, relative_path: str, target_date: str) -> list[str]:
    frontmatter, body = _split_frontmatter(content)
    if frontmatter is None:
        return [f"FRONTMATTER_INVALID:{relative_path}"]

    language = "zh" if relative_path.endswith("-zh.md") else "en"
    suffix = "ZH" if language == "zh" else "EN"
    expected = {
        "layout": "default",
        "date": target_date,
        "lang": language,
        "title": f"Horizon Summary: {target_date} ({suffix})",
    }
    issues = [
        f"FRONTMATTER_INVALID:{relative_path}"
        for key, value in expected.items()
        if frontmatter.get(key) != value
    ]
    if not body.strip():
        issues.append(f"POST_BODY_EMPTY:{relative_path}")
    return issues


def _split_frontmatter(content: str) -> tuple[dict[str, str] | None, str]:
    if not content.startswith("---\n"):
        return None, content
    marker = "\n---\n"
    closing_index = content.find(marker, len("---\n"))
    if closing_index == -1:
        return None, content
    raw_frontmatter = content[len("---\n") : closing_index]
    frontmatter: dict[str, str] = {}
    for line in raw_frontmatter.splitlines():
        if ":" not in line:
            return None, content
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter, content[closing_index + len(marker) :]
