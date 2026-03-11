"""Aggregation layer.

Combines scraped page content from multiple sources into a single text
payload that can be fed to the Gemini prompt engine.
"""

from __future__ import annotations

import logging
from typing import Sequence

from chaintrace.models import ScrapedPage

logger = logging.getLogger(__name__)

# Approximate character budget per page to keep the prompt within token limits.
MAX_CHARS_PER_PAGE = 4_000


def aggregate(pages: Sequence[ScrapedPage]) -> str:
    """Merge successful scrape results into one consolidated text block.

    Only pages with ``success=True`` are included.  Each section is prefixed
    with the source URL so Gemini can cite it when producing the datasheet URL
    or description.

    Args:
        pages: Scraped pages returned by
            :func:`~chaintrace.scraper.scrape`.

    Returns:
        A single string suitable for inclusion in the Gemini prompt.
    """
    sections: list[str] = []
    for page in pages:
        if not page.success:
            continue
        body = truncate(page.text)
        sections.append(f"--- Source: {page.url} ---\n{body}")

    if not sections:
        logger.warning("No successful pages to aggregate.")
        return ""

    return "\n\n".join(sections)


def truncate(text: str, max_chars: int = MAX_CHARS_PER_PAGE) -> str:
    """Trim *text* to at most *max_chars* characters.

    Args:
        text:      Input string.
        max_chars: Maximum allowed length.

    Returns:
        Truncated string, with an ellipsis appended if content was removed.
    """
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "…"
