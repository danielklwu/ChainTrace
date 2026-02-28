# ChainTrace

## Product Requirements Document (PRD)

---

# 1. Overview

**ChainTrace** is a standalone CLI-based hardware component lookup tool designed to identify electrical components from board markings and extract structured metadata including manufacturer, part type, datasheet link, and potential supply-chain risk indicators.

The system accepts manually entered component markings, retrieves relevant online sources (top 3 links), and uses Gemini to classify and structure the results into deterministic JSON output. Results are cached locally for reproducibility and future analysis.

Version 1 focuses strictly on component identification and metadata extraction. Supply-chain risk analysis and image/OCR support are explicitly out of scope.

---

# 2. Problem Statement

Hardware security research often requires identifying unknown components from PCB markings. Manual lookup is:

- Time-consuming
- Inconsistent
- Not reproducible
- Difficult to log for research validation

ChainTrace automates component identification and metadata structuring to support:

- Hardware inspection workflows
- Firmware trust analysis preparation
- Supply chain research preparation

---

# 3. Goals

## Primary Goals (v1)

- Accept a single manually entered component marking.
- Search and retrieve top 3 relevant web sources.
- Extract textual data from those sources.
- Use Gemini to:
  - Identify component type
  - Identify manufacturer
  - Provide datasheet URL
  - Provide brief description
  - Flag risk indicators (if mentioned)
- Output deterministic structured JSON.
- Cache results locally.

---

# 4. Non-Goals (Out of Scope)

- OCR / image processing
- Knowledge graph construction
- Automated risk scoring
- Fabrication plant geolocation inference
- Batch processing
- Cloud deployment
- Deep supply-chain tracing

---

# 5. User Persona

## Primary User

- Hardware security researcher
- Comfortable with CLI
- Running locally on Linux/macOS
- Needs reproducible research artifacts

---

# 6. User Flow

1. User runs CLI:

```
chaintrace
```

2. User inputs board marking (supports literal `\n`):

```
DAC
32031
TI 69K
CJ22
```

3. System:
   - Normalizes input
   - Performs search query
   - Retrieves top 3 links
   - Scrapes textual content
   - Feeds aggregated content to Gemini
   - Receives structured JSON
   - Saves result locally
   - Displays summary in terminal

---

# 7. Functional Requirements

## 7.1 Input

- Accept single query per execution.
- Accept multi-line text.
- Preserve formatting.
- No fuzzy correction in v1.

---

## 7.2 Web Retrieval

- Query search engine or API (e.g., SerpAPI, Google API).
- Retrieve top 3 ranked links.
- Extract visible text content.
- Prefer:
  - Manufacturer websites
  - Datasheet repositories
  - Distributor listings (DigiKey, Mouser, Octopart)

---

## 7.3 AI Classification (Gemini)

Gemini must output strict JSON in this schema:

```json
{
  "input_query": "string",
  "normalized_part_number": "string",
  "component_type": "string",
  "manufacturer": "string",
  "manufacturer_country": "string | null",
  "datasheet_url": "string | null",
  "description": "string",
  "risk_indicators": [
    "string"
  ],
  "confidence_score": 0.0
}
```

### Risk Indicators (if found in scraped content)

Examples:

- Export control warnings
- Sanctioned entity mention
- End-of-life (EOL)
- Obsolete part
- Counterfeit warning
- Manufacturing region flagged in policy databases

If none found:

```json
"risk_indicators": []
```

---

## 7.4 Local Storage

- Store JSON output in:

```
./cache/<normalized_part_number>.json
```

- Store:
  - Scraped URLs
  - Raw scraped text
  - Gemini prompt
  - Gemini response

This ensures research reproducibility.

---

## 7.5 CLI Output

Terminal should display:

- Identified part
- Manufacturer
- Component type
- Datasheet link
- Risk indicators (if any)

Example:

```
Part: DAC32031
Manufacturer: Texas Instruments
Type: Digital-to-Analog Converter
Datasheet: https://...
Risk Indicators: None detected
Confidence: 0.92
```

---

# 8. Non-Functional Requirements

| Requirement | Target |
|------------|--------|
| Runtime | Under 60 seconds |
| Environment | Local execution |
| User Scope | Single-user |
| Determinism | Structured JSON output |
| Logging | Full traceability |
| Failure Handling | Graceful error output |

---

# 9. Architecture Overview

## Components

1. CLI Interface
2. Search API Layer
3. Web Scraper Module
4. Aggregation Layer
5. Gemini Prompting Engine
6. JSON Validator
7. Local Cache Manager

## High-Level Flow

```
User Input
    ↓
Search API
    ↓
Top 3 URLs
    ↓
Scraper
    ↓
Aggregated Text
    ↓
Gemini
    ↓
Structured JSON
    ↓
Cache + CLI Output
```

---

# 10. Error Handling

Must handle:

- No search results
- Scraping blocked
- Gemini timeout
- Invalid JSON from Gemini
- Missing datasheet link
- Ambiguous manufacturer

System must never crash silently.

---

# 11. Risks & Technical Challenges

- Scraping restrictions / bot detection
- Ambiguous chip markings
- Gemini hallucination
- Incorrect datasheet matching
- Manufacturer country inference errors

Mitigation:

- Strict JSON validation
- URL citation requirement in prompt
- Logging raw data for auditability

---

# 12. Future Roadmap (Not v1)

- OCR from PCB images
- Batch processing mode
- Risk scoring model
- Knowledge graph of suppliers
- Integration with firmware trust analysis
- SBOM output compatibility
- Fabrication plant geolocation inference

---

# 13. Open Design Decisions

Pending decisions:

- Programming language (Python vs Go)
- Search API provider
- Scraping library (BeautifulSoup vs Playwright)
- Gemini prompt structure strictness
- Confidence scoring methodology

