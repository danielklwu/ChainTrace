"""JSON validator.

Parses and validates raw JSON returned by Gemini against the expected
ComponentResult schema, guaranteeing that downstream code always receives
well-formed data.
"""

from __future__ import annotations

import json
import logging
from typing import Any

from chaintrace.models import ComponentResult

logger = logging.getLogger(__name__)

# Required top-level keys in the Gemini response.
REQUIRED_KEYS = {
    "input_query",
    "normalized_part_number",
    "component_type",
    "manufacturer",
    "manufacturer_country",
    "datasheet_url",
    "description",
    "risk_indicators",
    "confidence_score",
}


def parse(raw_response: str) -> ComponentResult:
    """Parse and validate the raw Gemini response into a :class:`ComponentResult`.

    Args:
        raw_response: Raw text returned by :func:`~chaintrace.gemini.classify`.

    Returns:
        A validated :class:`~chaintrace.models.ComponentResult` instance.

    Raises:
        ValueError: If the response is not valid JSON or is missing required
            fields.
    """
    # TODO:
    # 1. Strip any accidental markdown code fences (```json ... ```).
    # 2. json.loads() — raise ValueError with context on failure.
    # 3. Validate all REQUIRED_KEYS are present.
    # 4. Coerce types (confidence_score → float, risk_indicators → list).
    # 5. Construct and return a ComponentResult.
    raise NotImplementedError


def validate_schema(data: dict[str, Any]) -> None:
    """Assert that *data* contains all required keys.

    Args:
        data: Parsed dictionary from Gemini JSON response.

    Raises:
        ValueError: Listing every missing key.
    """
    # TODO: compute missing = REQUIRED_KEYS - data.keys() and raise if non-empty.
    raise NotImplementedError
