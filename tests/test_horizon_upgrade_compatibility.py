from pathlib import Path

from src.ai.localization import normalize_language
from src.models import Config


def test_chinese_output_is_traditional():
    assert normalize_language("简体中文标题与内容", "zh") == "簡體中文標題與內容"
    assert normalize_language("English title", "en") == "English title"


def test_cloud_config_keeps_existing_languages_threshold_and_sources():
    path = Path(__file__).resolve().parents[1] / "data" / "config.github.json"
    config = Config.model_validate_json(path.read_text(encoding="utf-8"))

    assert config.ai.languages == ["zh", "en"]
    assert config.processing.profile_settings["tech-news"].threshold == 8.0
    assert {source.name for source in config.sources.rss} == {
        "Simon Willison",
        "GitHub Trending - Daily",
        "LWN.net",
    }
    assert {source.subreddit for source in config.sources.reddit.subreddits} == {
        "MachineLearning",
        "LocalLLaMA",
    }
    assert config.ai.provider.value == "openai"
    assert config.ai.model == "gpt-6.1-terra"
    assert config.ai.api_key_env == "OPENAI_API_KEY"
    assert config.ai.base_url is None
