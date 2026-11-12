"""Deterministic normalization for localized AI output."""

from opencc import OpenCC


_SIMPLIFIED_TO_TRADITIONAL = OpenCC("s2twp")


def normalize_language(text: str, language: str) -> str:
    """Normalize generated text to the script implied by its language tag."""
    if language.lower() == "zh":
        return _SIMPLIFIED_TO_TRADITIONAL.convert(text)
    return text
