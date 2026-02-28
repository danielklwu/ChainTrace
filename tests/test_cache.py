"""Tests for chaintrace.cache."""

import pytest
from pathlib import Path

from chaintrace import cache
from chaintrace.models import ComponentResult


SAMPLE_COMPONENT = ComponentResult(
    input_query="DAC 32031 TI 69K CJ22",
    normalized_part_number="DAC32031",
    component_type="Digital-to-Analog Converter",
    manufacturer="Texas Instruments",
    manufacturer_country="US",
    datasheet_url="https://www.ti.com/lit/ds/symlink/dac32031.pdf",
    description="High-speed 16-bit DAC.",
    risk_indicators=[],
    confidence_score=0.92,
)


class TestGetCachePath:
    def test_returns_json_extension(self):
        # TODO: assert path ends with .json.
        pytest.skip("Not yet implemented")

    def test_sanitises_slashes(self):
        # TODO: part numbers with '/' should not create subdirectories.
        pytest.skip("Not yet implemented")


class TestSaveAndLoad:
    def test_save_creates_file(self, tmp_path):
        # TODO: call cache.save() with tmp_path and assert the file exists.
        pytest.skip("Not yet implemented")

    def test_load_returns_component_result(self, tmp_path):
        # TODO: save then load and assert the result matches SAMPLE_COMPONENT.
        pytest.skip("Not yet implemented")

    def test_load_returns_none_on_miss(self, tmp_path):
        # TODO: assert cache.load("NONEXISTENT", tmp_path) is None.
        pytest.skip("Not yet implemented")


class TestExists:
    def test_true_after_save(self, tmp_path):
        pytest.skip("Not yet implemented")

    def test_false_before_save(self, tmp_path):
        pytest.skip("Not yet implemented")
