"""Tests for chaintrace.validator."""

import pytest

from chaintrace import validator
from chaintrace.models import ComponentResult

VALID_JSON = """\
{
  "input_query": "DAC 32031 TI 69K CJ22",
  "normalized_part_number": "DAC32031",
  "component_type": "Digital-to-Analog Converter",
  "manufacturer": "Texas Instruments",
  "manufacturer_country": "US",
  "datasheet_url": "https://www.ti.com/lit/ds/symlink/dac32031.pdf",
  "description": "High-speed 16-bit DAC.",
  "risk_indicators": [],
  "confidence_score": 0.92
}"""

MISSING_KEY_JSON = """\
{
  "input_query": "DAC 32031 TI 69K CJ22",
  "normalized_part_number": "DAC32031"
}"""


class TestParse:
    def test_valid_json_returns_component_result(self):
        # TODO: call validator.parse(VALID_JSON) and assert fields.
        pytest.skip("Not yet implemented")

    def test_strips_markdown_fences(self):
        # TODO: wrap VALID_JSON in ```json ... ``` and assert it still parses.
        pytest.skip("Not yet implemented")

    def test_raises_on_invalid_json(self):
        # TODO: pass malformed JSON and assert ValueError.
        pytest.skip("Not yet implemented")

    def test_raises_on_missing_keys(self):
        # TODO: pass MISSING_KEY_JSON and assert ValueError listing missing keys.
        pytest.skip("Not yet implemented")
