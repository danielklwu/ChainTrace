"""Tests for chaintrace.gemini."""

import pytest

from chaintrace import gemini


SAMPLE_AGGREGATED = "--- Source: https://example.com ---\nDAC32031 is a digital-to-analog converter by TI."


class TestBuildPrompt:
    def test_contains_query(self):
        # TODO: assert the query string appears in the built prompt.
        pytest.skip("Not yet implemented")

    def test_contains_output_schema(self):
        # TODO: assert the JSON schema is embedded in the prompt.
        pytest.skip("Not yet implemented")

    def test_contains_aggregated_text(self):
        # TODO: assert scraped content is included in the prompt.
        pytest.skip("Not yet implemented")


class TestClassify:
    def test_returns_raw_json_string(self, mocker):
        # TODO: mock the Gemini client and assert the raw response is returned.
        pytest.skip("Not yet implemented")

    def test_raises_on_timeout(self, mocker):
        # TODO: simulate a network timeout and assert RuntimeError.
        pytest.skip("Not yet implemented")

    def test_raises_on_missing_api_key(self, mocker):
        # TODO: unset GOOGLE_API_KEY and assert authentication error.
        pytest.skip("Not yet implemented")
