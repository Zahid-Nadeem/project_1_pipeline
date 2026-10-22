# Multi-Page Bookstore Scraping & Data Engineering Pipeline

A modular, production-ready ETL pipeline designed to crawl an entire e-commerce storefront catalog sequentially, handle relative URL pagination layouts dynamically, and export a sanitized dataset ready for analytics or machine learning consumption patterns.

## Technical Architecture

* **Relative Link Resolution:** Integrates Python's native `urllib.parse.urljoin` utility to reconstruct absolute routing endpoints dynamically from structural pagination fragments (`href`), eliminating rigid hard-coded folder strings.
* **Modular Clean Segmentation:** Implements single-responsibility design principles across isolated functions for network handling (`get_soup`), DOM processing (`parse_books`), and data orchestration workflows (`run`).
* **Production-Grade Log Tracking:** Utilizes standard `logging` levels (`INFO`, `ERROR`, `WARNING`) rather than simple standard terminal printing to systematically capture execution paths and connection thresholds.
* **Typing & Schema Consistency:** Deploys a Pandas data engineering execution pattern to strip non-numeric character metrics (`£`), cast raw fields cleanly into appropriate computational formats (`float`), and structure database-ingestion ready CSV datasets.

## Component Stack

* **Language Platform:** Python 3.14+
* **Data Processing:** `pandas`
* **Parsing Utilities:** `beautifulsoup4`, `urllib.parse`
* **Networking Infrastructure:** `requests`

## Operational Blueprint

```text
[Initial Page Request] ──> [get_soup Request Guard] ──> [BeautifulSoup Node Loop]
                                                                │
[CSV Target Export]  <── [Pandas Clean Pipeline]  <── [urljoin Target Loops]
```

## System Deployment

### 1. Project Prerequisites
Initialize and activate your localized virtual environment tracking layer:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Required Dependencies
Install the standard system interaction libraries inside your active isolated environment workspace:

```powershell
pip install requests beautifulsoup4 pandas lxml
```

### 3. Run the Pipeline Execution Agent
Run the main script directly using the terminal configuration prompt:

```powershell
python project_1_pipeline.py
```

## Dataset Specifications

The pipeline formats records cleanly and writes the final rows directly to `sanitized_product_feed.csv` adhering to the following structural output layout:

| Attribute Header | Data Format Type | Functional Field Description |
| :--- | :--- | :--- |
| `title` | String / Text | The complete un-truncated book heading extracted natively from the anchor attribute node block. |
| `price_gbp` | Floating-point (Float) | Standardized product value layout with transactional currency markers completely scrubbed out. |
