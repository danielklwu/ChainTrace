"""Tests for chaintrace.search."""

import pytest

from chaintrace import search
from chaintrace.models import SearchResult


class TestBuildQuery:
    def test_single_line(self):
        # TODO: assert that a simple marking produces a clean query string.
        pytest.skip("Not yet implemented")

    def test_multiline_collapses_whitespace(self):
        # TODO: assert that multi-line markings are collapsed correctly.
        pytest.skip("Not yet implemented")

    def test_appends_context_keywords(self):
        # TODO: assert that helpful keywords (e.g. 'datasheet') are added.
        pytest.skip("Not yet implemented")


class TestSearch:
    def test_returns_top_n_results(self, mocker):
        # TODO: mock the search API response and assert exactly N results.
        pytest.skip("Not yet implemented")

    def test_raises_on_api_error(self, mocker):
        # TODO: simulate an API error and assert RuntimeError is raised.
        pytest.skip("Not yet implemented")
