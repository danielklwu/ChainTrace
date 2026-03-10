"""Gemini prompting engine.

Constructs a structured prompt from aggregated web content, calls the
Gemini API, and returns the raw JSON response string.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

# Gemini model identifier. Override via CHAINTRACE_GEMINI_MODEL env var.
DEFAULT_MODEL = "gemini-3-flash-preview"

# JSON schema description embedded in the system prompt so Gemini returns
# deterministic structured output.
OUTPUT_SCHEMA = """\
{
  "input_query": "string",
  "normalized_part_number": "string",
  "component_type": "string",
  "manufacturer": "string",
  "manufacturer_country": "string | null",
  "datasheet_url": "string | null",
  "description": "string",
  "risk_indicators": ["string"],
  "confidence_score": 0.0
}"""


def build_prompt(query: str, aggregated_text: str) -> str:
    """Construct the full prompt sent to Gemini.

    The prompt instructs Gemini to:
      - Act as a hardware component identification expert.
      - Use only information present in the provided source text.
      - Cite the datasheet URL directly from the sources.
      - Return *only* valid JSON matching OUTPUT_SCHEMA.

    Args:
        query:           The original (normalised) user query.
        aggregated_text: Combined text from all scraped pages.

    Returns:
        A complete prompt string ready to be sent to the Gemini API.
    """
    # TODO: craft the system + user prompt. Key requirements:
    # - Strict JSON output instruction (no markdown fences, no extra prose).
    # - URL citation requirement.
    # - Risk indicator enumeration guidance.
    # - Confidence scoring guidance.
    raise NotImplementedError


def classify(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """Send *prompt* to Gemini and return the raw response text.

    Args:
        prompt: Complete prompt built by :func:`build_prompt`.
        model:  Gemini model identifier.

    Returns:
        Raw text response from the API (expected to be JSON).

    Raises:
        RuntimeError: On API authentication failure, network error, or
            response timeout.
    """
    # TODO:
    # 1. Load GOOGLE_API_KEY from environment.
    # 2. Initialise google-generativeai client.
    # 3. Call model.generate_content(prompt) with appropriate generation config
    #    (temperature=0 for determinism, max_output_tokens budget).
    # 4. Return response.text.
    raise NotImplementedError
