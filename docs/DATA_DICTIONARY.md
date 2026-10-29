# Data dictionary and metric definitions

All entities and identifiers are fictional.

| Table | Field | Meaning | Quality control |
|---|---|---|---|
| applications | application_id | Unique application key | Primary key, required |
| applications | applicant_key | Pseudonymous borrower key | Review repeated key/date pairs; not automatically duplicates |
| applications | created_at | ISO date of application | Should parse as date |
| applications | stage | Current operational state | Approved vocabulary |
| applications | loan_amount | Requested amount in USD | Must be positive |
| applications | agent_id | Originating agent identifier | Must resolve to agents table |
| agents | agent_id | Agent reference key | Primary key |
| agents | region | Reporting territory | Nonblank |
| events | application_id | Related application | Should match applications |
| events | stage | Recorded workflow event | Compare to current application stage |
| events | event_date | Date of stage event | ISO date |

## KPI definitions

- **Application volume**: count of application records, not unique borrowers.
- **Requested amount**: sum of amounts as stored; not funded volume or revenue.
- **Unmapped agent count**: applications whose agent ID has no matching agent record.
- **Clean record percentage**: percentage without nonpositive amount or unmapped agent; not a complete data quality score.
- **Stage distribution**: snapshot counts, not conversion rates. Conversion requires a complete event history and cohort definitions.

## Source-to-target mapping

`applications.agent_id` → `agents.agent_id` (LEFT JOIN; retain unmapped applications).
`applications.application_id` → `events.application_id` (match stages for event presence).
No personal names, real addresses, SSNs, or actual financial records are used.
