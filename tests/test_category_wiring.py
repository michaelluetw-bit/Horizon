from __future__ import annotations

import asyncio
from datetime import datetime, timezone
from unittest.mock import AsyncMock, Mock

from src.models import (
    GitHubSourceConfig,
    HackerNewsConfig,
    OSSInsightConfig,
    RedditConfig,
    RedditSubredditConfig,
    RedditUserConfig,
    TelegramChannelConfig,
    TelegramConfig,
)
from src.scrapers.github import GitHubScraper
from src.scrapers.hackernews import HackerNewsScraper
from src.scrapers.ossinsight import OSSInsightScraper
from src.scrapers.reddit import RedditScraper
from src.scrapers.telegram import TelegramScraper


_SINCE = datetime(2020, 1, 1, tzinfo=timezone.utc)
_NOW = datetime(2026, 7, 13, 0, 0, tzinfo=timezone.utc)


def test_supported_source_configs_accept_optional_category() -> None:
    assert GitHubSourceConfig(type="user_events", category="oss").category == "oss"
    assert HackerNewsConfig(category="tech").category == "tech"
    assert (
        RedditSubredditConfig(subreddit="LocalLLaMA", category="ai-community").category
        == "ai-community"
    )
    assert (
        RedditUserConfig(username="alice", category="community").category == "community"
    )
    assert (
        TelegramChannelConfig(channel="zaihuapd", category="ai-news").category
        == "ai-news"
    )
    assert OSSInsightConfig(category="oss-trending").category == "oss-trending"


def test_github_event_keeps_its_source_category() -> None:
    source = GitHubSourceConfig(type="user_events", username="alice", category="oss")
    scraper = GitHubScraper([source], AsyncMock())
    event = {
        "id": "event-1",
        "type": "PushEvent",
        "created_at": _NOW.isoformat().replace("+00:00", "Z"),
        "repo": {"name": "alice/repo"},
        "payload": {"commits": [{"message": "Initial commit"}]},
    }

    item = scraper._parse_event(event, source)

    assert item is not None
    assert item.metadata["category"] == "oss"


def test_github_release_keeps_its_source_category() -> None:
    source = GitHubSourceConfig(
        type="repo_releases",
        owner="example",
        repo="project",
        category="oss",
    )
    response = Mock()
    response.json.return_value = [
        {
            "id": 1,
            "tag_name": "v1.0.0",
            "html_url": "https://github.com/example/project/releases/tag/v1.0.0",
            "body": "Release notes",
            "author": {"login": "maintainer"},
            "published_at": _NOW.isoformat().replace("+00:00", "Z"),
        }
    ]
    client = AsyncMock()
    client.get.return_value = response

    items = asyncio.run(
        GitHubScraper([source], client)._fetch_repo_releases(source, _SINCE)
    )

    assert len(items) == 1
    assert items[0].metadata["category"] == "oss"


def test_hackernews_story_keeps_configured_category() -> None:
    scraper = HackerNewsScraper(HackerNewsConfig(category="tech"), AsyncMock())
    story = {
        "id": 1,
        "title": "A story",
        "url": "https://example.com/story",
        "by": "author",
        "time": int(_NOW.timestamp()),
        "score": 100,
        "type": "story",
        "descendants": 0,
    }

    item = scraper._parse_story(story, [])

    assert item.metadata["category"] == "tech"


def test_reddit_post_keeps_its_source_category() -> None:
    config = RedditConfig(
        subreddits=[
            RedditSubredditConfig(subreddit="LocalLLaMA", category="ai-community")
        ]
    )
    scraper = RedditScraper(config, AsyncMock())
    post = {
        "id": "post-1",
        "title": "A post",
        "is_self": True,
        "subreddit": "LocalLLaMA",
        "permalink": "/r/LocalLLaMA/comments/post-1/",
        "author": "author",
        "created_utc": _NOW.timestamp(),
        "score": 100,
        "upvote_ratio": 0.95,
        "num_comments": 0,
        "selftext": "content",
    }

    item = scraper._parse_post(post, [], "subreddit", category="ai-community")

    assert item is not None
    assert item.metadata["category"] == "ai-community"


def test_telegram_message_keeps_its_channel_category() -> None:
    cfg = TelegramChannelConfig(channel="zaihuapd", category="ai-news")
    html = """
    <div class="tgme_widget_message" data-post="zaihuapd/1">
      <div class="tgme_widget_message_text js-message_text">Hello world</div>
      <time datetime="2026-07-13T00:00:00+00:00">00:00</time>
    </div>
    """

    items = TelegramScraper(TelegramConfig(), AsyncMock())._parse_channel_html(
        html, cfg, _SINCE
    )

    assert len(items) == 1
    assert items[0].metadata["category"] == "ai-news"


def test_ossinsight_item_keeps_configured_category() -> None:
    scraper = OSSInsightScraper(OSSInsightConfig(category="oss-trending"), AsyncMock())
    row = {
        "repo_name": "example/project",
        "repo_id": 1,
        "stars": 100,
        "forks": 10,
        "pushes": 5,
        "pull_requests": 2,
    }

    item = scraper._row_to_item(row, "Python")

    assert item is not None
    assert item.metadata["category"] == "oss-trending"
