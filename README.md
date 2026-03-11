# ChainTrace

CLI tool for hardware component identification and supply-chain risk analysis.  
Accepts a PCB board marking, retrieves top web sources, and uses Gemini to return structured JSON metadata.

---

## Project Structure

```
chaintrace/
├── __init__.py       # package version
├── cli.py            # Click CLI entry point  (`chaintrace` command)
├── models.py         # shared dataclasses (ComponentResult, SearchResult, …)
├── search.py         # search API layer
├── scraper.py        # web scraping & text extraction
├── aggregator.py     # merge scraped pages into one prompt payload
├── gemini.py         # Gemini prompt construction & API call
├── validator.py      # parse & validate Gemini JSON output
└── cache.py          # local cache manager (./cache/<part>.json)

tests/
├── test_search.py
├── test_scraper.py
├── test_gemini.py
├── test_validator.py
└── test_cache.py

cache/                # git-ignored; created at runtime
.env.example          # copy to .env and add your API keys
pyproject.toml
```

---

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 2. Install the package in editable mode (including dev extras)
pip install -e ".[dev]"

# 3. Configure API keys
cp .env.example .env
# edit .env and fill in GOOGLE_API_KEY and SERPAPI_KEY
```

---

## Usage

```bash
# Interactive prompt
chaintrace

# Inline query (use literal \n for multi-line markings)
chaintrace "DAC\n32031\nTI 69K\nCJ22"

# Skip local cache
chaintrace --no-cache "DAC32031"

# Verbose logging
chaintrace -v "DAC32031"
```

### Example output

```
Part:               DAC32031
Manufacturer:       Texas Instruments
Country:            USA
Type:               Integrated Circuit (IC)
Datasheet:          https://www.ti.com/lit/ds/symlink/dac32031.pdf
Risk Indicators:    None detected
Confidence:         0.90

Description:
The DAC32031 is a specialized integrated circuit from Texas
Instruments, functioning as a Digital-to-Analog Converter (DAC).
```

---

## Running Tests

```bash
pytest
```

---

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GOOGLE_API_KEY` | Yes | Gemini API key |
| `SERPAPI_KEY` | Yes | SerpAPI key (or use Google Custom Search) |
| `CHAINTRACE_GEMINI_MODEL` | No | Override Gemini model (default: `gemini-2.0-flash`) |
| `CHAINTRACE_CACHE_DIR` | No | Override cache directory (default: `cache/`) |
