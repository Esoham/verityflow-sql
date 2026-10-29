# Executive findings — synthetic data quality audit

## Decision supported
Which data issues should an operations reporting team review before relying on application and agent KPIs?

## Reproducible results
Run `python run.py` against the seven-record fictional seed.

| Control | Finding | Recommended action |
|---|---|---|
| Nonpositive amount | K005 (1) | Verify the source amount |
| Unmapped agent | K007 (1) | Check agent reference mapping |
| Potential duplicate applicant/date | K002 and K003 (1 pair) | Compare source IDs before merging |
| Stage without matching event | K002, K003, K005, K006 (4) | Review event capture completeness |

Flags may overlap and must not be summed as a unique-record defect rate.

## Business recommendations
1. Quarantine nonpositive requested amounts for review.
2. Route unmatched agents to reference-data owners.
3. Define workflow event completeness and exception ownership.
4. Require human review before merging suspected duplicates.
5. Publish KPI definitions and data lineage with dashboards.

## Interpretation limits
Requested amounts are not funded volume or revenue. Snapshot stage counts are not conversion rates. Missing events may reflect incomplete capture. All data is fictional; no real operational savings are claimed.
