"""Data models for ChainTrace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComponentResult:
    """Structured output returned by Gemini after classification."""

    input_query: str
    normalized_part_number: str
    component_type: str
    manufacturer: str
    manufacturer_country: Optional[str]
    datasheet_url: Optional[str]
    description: str
    risk_indicators: list[str] = field(default_factory=list)
    confidence_score: float = 0.0

    def to_dict(self) -> dict:
        return {
            "input_query": self.input_query,
            "normalized_part_number": self.normalized_part_number,
            "component_type": self.component_type,
            "manufacturer": self.manufacturer,
            "manufacturer_country": self.manufacturer_country,
            "datasheet_url": self.datasheet_url,
            "description": self.description,
            "risk_indicators": self.risk_indicators,
            "confidence_score": self.confidence_score,
        }


@dataclass
class SearchResult:
    """A single search result returned by the search layer."""

    url: str
    title: str
    snippet: str


@dataclass
class ScrapedPage:
    """Raw text content scraped from a URL."""

    url: str
    text: str
    success: bool
    error: Optional[str] = None


@dataclass
class CacheEntry:
    """Full cache record stored per lookup."""

    query: str
    normalized_part_number: str
    search_results: list[SearchResult]
    scraped_pages: list[ScrapedPage]
    gemini_prompt: str
    gemini_response: str
    component_result: ComponentResult
