# VerityFlow — SQL Data Quality & Operations Intelligence

A reproducible **independent portfolio project** demonstrating SQL reporting, data governance, exception detection, and executive-friendly presentation using **fictional loan operations data**. No real customers, lenders or private records.

## Business problem
Operations leaders need trustworthy application volumes, reference-data mappings and workflow status. Inconsistent records can distort management reporting.

## Quick start (Python 3, no third-party dependencies)
```bash
python run.py
python dashboard.py
python generate_demo.py
```
Open `dashboard.html` locally. The dashboard uses the seven-record seeded database. The separate generator creates 2,000 fictional CSV records for future analysis; it does **not** automatically feed the SQL dashboard.

## Project contents
- `schema.sql` / `seed.sql` — seven-row seeded SQLite scenario
- `quality_checks.sql` — possible duplicates, invalid amounts, unmapped agents and stage/event exceptions
- `reporting.sql` — stage and region management summaries
- `analytics.sql` — CTEs, window functions, regional stage counts, and a scoped quality KPI
- `run.py` — reproducible SQL demo runner
- `dashboard.py` — self-contained HTML dashboard generator
- `generate_demo.py` — deterministic 2,000-record synthetic CSV generator
- `docs/DATA_DICTIONARY.md` — definitions, joins and metric caveats
- `docs/CASE_STUDY.md` — findings and recommended controls

## Example findings (seven-row seed)
One nonpositive loan amount, one unmapped agent, and a potential repeated applicant/date pair. Missing stage events are review flags, not proven business errors.

## Scope and limitations
Synthetic demonstration only. Requested loan amounts are **not** funded amounts or revenue. Snapshot stage counts are **not** conversion rates. The generated 2,000-record CSV is a separate fixture, not a claim of analyzed production volume. The project does not perform real underwriting or handle PII.

## Resume-ready description
**VerityFlow | SQL, SQLite, Python:** Developed a reproducible SQL reporting and data-quality prototype using joins, CTEs and window functions to identify record exceptions and generate an operations dashboard from synthetic application data.
