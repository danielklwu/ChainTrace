"""CLI entry point for ChainTrace.

Usage:
    chaintrace                  # interactive prompt
    chaintrace "DAC\\n32031\\nTI 69K\\nCJ22"   # inline query (literal \\n supported)

Supports multi-line input. Literal '\\n' sequences in the query string are
expanded to real newlines before processing.
"""

from __future__ import annotations

import logging
import sys

import click

from chaintrace import __version__
from chaintrace import aggregator, cache, gemini, scraper, search, validator
from chaintrace.models import CacheEntry

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# CLI definition
# ---------------------------------------------------------------------------


@click.command()
@click.version_option(__version__, prog_name="chaintrace")
@click.argument("query", required=False, default=None)
@click.option(
    "--no-cache",
    is_flag=True,
    default=False,
    help="Skip the local cache and always perform a fresh lookup.",
)
@click.option(
    "--cache-dir",
    default="cache",
    show_default=True,
    help="Directory used to store cached results.",
    type=click.Path(),
)
@click.option(
    "--top-n",
    default=3,
    show_default=True,
    help="Number of search results to retrieve.",
    type=int,
)
@click.option(
    "--verbose", "-v",
    is_flag=True,
    default=False,
    help="Enable verbose/debug logging.",
)
def main(
    query: str | None,
    no_cache: bool,
    cache_dir: str,
    top_n: int,
    verbose: bool,
) -> None:
    """ChainTrace — hardware component lookup and supply-chain risk analysis.

    Provide a board QUERY string (supports literal \\\\n for multi-line markings),
    or omit it to be prompted interactively.
    """
    if verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # ------------------------------------------------------------------
    # 1. Collect input
    # ------------------------------------------------------------------
    query = _resolve_query(query)
    if not query:
        click.echo("Error: empty query.", err=True)
        sys.exit(1)

    click.echo(f"[ChainTrace v{__version__}]")
    click.echo(f"Query: {repr(query)}\n")

    # ------------------------------------------------------------------
    # 2. Cache check
    # ------------------------------------------------------------------
    from pathlib import Path
    cache_path = Path(cache_dir)

    # TODO: once cache.load() is implemented, check for a cache hit here
    # and return early when --no-cache is not set.

    # ------------------------------------------------------------------
    # 3. Search
    # ------------------------------------------------------------------
    click.echo("Searching...")
    search_query = search.build_query(query)
    results = search.search(search_query, top_n=top_n)
    click.echo(f"Found {len(results)} result(s).")

    # ------------------------------------------------------------------
    # 4. Scrape
    # ------------------------------------------------------------------
    click.echo("Scraping sources...")
    pages = scraper.scrape(results)
    successful = [p for p in pages if p.success]
    click.echo(f"Scraped {len(successful)}/{len(pages)} page(s) successfully.")

    # ------------------------------------------------------------------
    # 5. Aggregate
    # ------------------------------------------------------------------
    aggregated_text = aggregator.aggregate(pages)

    # ------------------------------------------------------------------
    # 6. Gemini classification
    # ------------------------------------------------------------------
    click.echo("Classifying with Gemini...")
    prompt = gemini.build_prompt(query, aggregated_text)
    raw_response = gemini.classify(prompt)

    # ------------------------------------------------------------------
    # 7. Validate and parse
    # ------------------------------------------------------------------
    component = validator.parse(raw_response)

    # ------------------------------------------------------------------
    # 8. Cache save
    # ------------------------------------------------------------------
    entry = CacheEntry(
        query=query,
        normalized_part_number=component.normalized_part_number,
        search_results=results,
        scraped_pages=pages,
        gemini_prompt=prompt,
        gemini_response=raw_response,
        component_result=component,
    )
    saved_path = cache.save(entry, cache_dir=cache_path)
    logger.debug("Cached result to %s", saved_path)

    # ------------------------------------------------------------------
    # 9. Display summary
    # ------------------------------------------------------------------
    _display_result(component)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _resolve_query(query: str | None) -> str:
    """Return the final query string, prompting interactively if needed.

    Expands literal ``\\n`` sequences to real newlines.

    Args:
        query: Value passed on the command line, or ``None``.

    Returns:
        The resolved, stripped query string.
    """
    if query is None:
        click.echo("Enter component marking (blank line to finish):")
        lines: list[str] = []
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line == "":
                break
            lines.append(line)
        query = "\n".join(lines)
    else:
        # Expand literal \n sequences from shell-quoted strings.
        query = query.replace("\\n", "\n")

    return query.strip()


def _display_result(component) -> None:
    """Print a human-readable summary of *component* to stdout."""
    risk = ", ".join(component.risk_indicators) if component.risk_indicators else "None detected"
    datasheet = component.datasheet_url or "N/A"

    click.echo("\n" + "─" * 50)
    click.echo(f"Part:           {component.normalized_part_number}")
    click.echo(f"Manufacturer:   {component.manufacturer}")
    click.echo(f"Country:        {component.manufacturer_country or 'Unknown'}")
    click.echo(f"Type:           {component.component_type}")
    click.echo(f"Description:    {component.description}")
    click.echo(f"Datasheet:      {datasheet}")
    click.echo(f"Risk Indicators:{' ' + risk}")
    click.echo(f"Confidence:     {component.confidence_score:.2f}")
    click.echo("─" * 50)


if __name__ == "__main__":
    main()
