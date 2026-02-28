"""Tests for chaintrace.scraper."""

import pytest

from chaintrace.models import ScrapedPage, SearchResult
from chaintrace import scraper


FAKE_RESULT = SearchResult(
    url="https://example.com/datasheet",
    title="Example Datasheet",
    snippet="DAC32031 digital-to-analog converter.",
)


class TestScrape:
    def test_successful_scrape_returns_text(self, mocker):
        # TODO: mock requests/Playwright response and assert text is extracted.
        pytest.skip("Not yet implemented")

    def test_failed_scrape_returns_error_page(self, mocker):
        # TODO: simulate HTTP 403 and assert success=False, error is set.
        pytest.skip("Not yet implemented")

    def test_all_pages_returned_even_on_partial_failure(self, mocker):
        # TODO: mock two successes and one failure; assert len == 3.
        pytest.skip("Not yet implemented")


class TestExtractText:
    def test_strips_script_tags(self):
        # TODO: pass HTML with <script> blocks and assert they're absent.
        pytest.skip("Not yet implemented")

    def test_strips_style_tags(self):
        pytest.skip("Not yet implemented")

    def test_collapses_whitespace(self):
        pytest.skip("Not yet implemented")
