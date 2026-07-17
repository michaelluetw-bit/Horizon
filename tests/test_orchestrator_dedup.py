"""Tests for orchestrator deduplication (cross-source URL merge and topic dedup)."""

import asyncio
import json
from datetime import datetime, timezone
from types import SimpleNamespace

from rich.console import Console

from src.models import ContentItem, SourceType
from src.orchestrator import HorizonOrchestrator


def make_item(item_id: str, url: str, source: SourceType = SourceType.RSS) -> ContentItem:
    return ContentItem(
        id=item_id,
        source_type=source,
        title=item_id,
        url=url,
        published_at=datetime.now(timezone.utc),
        ai_score=9.0,
    )


def make_orchestrator() -> HorizonOrchestrator:
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(ai=SimpleNamespace())
    orchestrator.console = Console(record=True)
    return orchestrator


class _StubAIClient:
    def __init__(self, response: str):
        self.response = response

    async def complete(self, system, user, temperature=None, max_tokens=None):
        return self.response


def test_merge_keeps_urls_that_differ_only_in_query_string() -> None:
    items = [
        make_item("a", "https://www.youtube.com/watch?v=aaa", SourceType.REDDIT),
        make_item("b", "https://youtube.com/watch?v=bbb", SourceType.HACKERNEWS),
    ]

    merged = make_orchestrator().merge_cross_source_duplicates(items)

    assert len(merged) == 2


def test_merge_still_collapses_same_url_across_sources() -> None:
    items = [
        make_item("a", "https://www.example.com/story/", SourceType.REDDIT),
        make_item("b", "https://example.com/story", SourceType.HACKERNEWS),
    ]

    merged = make_orchestrator().merge_cross_source_duplicates(items)

    assert len(merged) == 1
    assert set(merged[0].metadata["merged_sources"]) == {"reddit", "hackernews"}


def test_merge_ignores_tracking_parameters_but_keeps_identifying_ones() -> None:
    # utm_* / ref only carry attribution — the same story must merge.
    items = [
        make_item("a", "https://example.com/story?utm_source=reddit&ref=share", SourceType.REDDIT),
        make_item("b", "https://example.com/story", SourceType.HACKERNEWS),
    ]
    merged = make_orchestrator().merge_cross_source_duplicates(items)
    assert len(merged) == 1

    # `v` identifies the video — different values must stay separate,
    # regardless of extra tracking params or param ordering.
    items = [
        make_item("c", "https://youtube.com/watch?v=aaa&utm_source=x", SourceType.REDDIT),
        make_item("d", "https://www.youtube.com/watch?utm_source=y&v=aaa", SourceType.HACKERNEWS),
        make_item("e", "https://youtube.com/watch?v=bbb", SourceType.RSS),
    ]
    merged = make_orchestrator().merge_cross_source_duplicates(items)
    assert len(merged) == 2


def test_topic_dedup_ignores_groups_with_non_integer_primary_index(monkeypatch) -> None:
    """A malformed AI response must degrade gracefully, not crash the run."""
    items = [make_item("a", "https://example.com/a"), make_item("b", "https://example.com/b")]
    response = json.dumps({"duplicates": [["0", 1]]})
    monkeypatch.setattr(
        "src.orchestrator.create_ai_client", lambda config: _StubAIClient(response)
    )

    result = asyncio.run(make_orchestrator().merge_topic_duplicates(items))

    assert result == items


def test_topic_dedup_drops_non_primary_duplicates(monkeypatch) -> None:
    items = [make_item("a", "https://example.com/a"), make_item("b", "https://example.com/b")]
    response = json.dumps({"duplicates": [[0, 1]]})
    monkeypatch.setattr(
        "src.orchestrator.create_ai_client", lambda config: _StubAIClient(response)
    )

    result = asyncio.run(make_orchestrator().merge_topic_duplicates(items))

    assert [item.id for item in result] == ["a"]
