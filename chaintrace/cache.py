"""Local cache manager.

Persists full lookup records to disk under ./cache/<normalized_part_number>.json
for research reproducibility.  Each entry stores raw scraped text, the Gemini
prompt, the Gemini response, and the final structured result.
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from chaintrace.models import CacheEntry, ComponentResult

logger = logging.getLogger(__name__)

# Default cache directory, relative to the working directory.
DEFAULT_CACHE_DIR = Path("cache")


def get_cache_path(normalized_part_number: str, cache_dir: Path = DEFAULT_CACHE_DIR) -> Path:
    """Return the file path for a given part number's cache entry.

    Args:
        normalized_part_number: Normalised part identifier used as filename.
        cache_dir:              Directory where cache files are stored.

    Returns:
        A :class:`~pathlib.Path` pointing to ``<cache_dir>/<part>.json``.
    """
    # TODO: sanitise normalized_part_number for use as a filename
    # (replace slashes, spaces, etc.).
    raise NotImplementedError


def save(entry: CacheEntry, cache_dir: Path = DEFAULT_CACHE_DIR) -> Path:
    """Serialise *entry* to JSON and write it to the cache directory.

    Creates the cache directory if it does not exist.

    Args:
        entry:     Full :class:`~chaintrace.models.CacheEntry` to persist.
        cache_dir: Target cache directory.

    Returns:
        The :class:`~pathlib.Path` of the written file.

    Raises:
        OSError: If the file cannot be written.
    """
    # TODO:
    # 1. Build the target path via get_cache_path().
    # 2. os.makedirs(cache_dir, exist_ok=True).
    # 3. Serialise entry to a dict (expand nested dataclasses).
    # 4. json.dump with indent=2.
    # 5. Log the saved path and return it.
    raise NotImplementedError


def load(normalized_part_number: str, cache_dir: Path = DEFAULT_CACHE_DIR) -> ComponentResult | None:
    """Load a cached :class:`~chaintrace.models.ComponentResult` if it exists.

    Args:
        normalized_part_number: Part identifier to look up.
        cache_dir:              Directory to search for cached files.

    Returns:
        A :class:`~chaintrace.models.ComponentResult` if a cache hit is found,
        otherwise ``None``.
    """
    # TODO:
    # 1. Build path via get_cache_path().
    # 2. Return None if the file does not exist.
    # 3. json.load and reconstruct ComponentResult.
    raise NotImplementedError


def exists(normalized_part_number: str, cache_dir: Path = DEFAULT_CACHE_DIR) -> bool:
    """Return ``True`` if a cache entry exists for *normalized_part_number*.

    Args:
        normalized_part_number: Part identifier to check.
        cache_dir:              Directory to search.
    """
    # TODO: delegate to get_cache_path().exists().
    raise NotImplementedError
