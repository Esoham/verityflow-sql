# Business case study: improving reporting trust

**Scenario:** An operations team needs a reliable view of applications, agent ownership and workflow status. This is a fictional exercise.

## Questions
1. Which application records are missing valid agent mappings?
2. Which loan amounts violate basic validation rules?
3. Do current stages have supporting workflow events?
4. What do current application volumes look like by stage and region?

## Approach
Use left joins to preserve missing reference records, conditional checks to surface exceptions, and grouped SQL reports for a reproducible management snapshot. Generate `dashboard.html` for a lightweight executive-facing visual.

## Findings from the seven-row seeded example
- One record has a nonpositive amount (K005).
- One record has an unmapped agent (K007).
- The event-history check highlights stages without matching events. This may reflect incomplete synthetic event capture; it is a **review flag**, not proof of wrongdoing.
- K002 and K003 share a borrower key and date and warrant duplicate review, not automatic deletion.

## Recommended controls
1. Validate positive requested amounts at ingestion.
2. Maintain an agent reference table and report unmatched identifiers.
3. Define stage-event mapping rules and exception ownership.
4. Review potential duplicates before merging records.
5. Publish KPI definitions with dashboards to avoid interpreting requested amount as funded volume.

**Scope:** No claims of real-world savings, production deployment or actual lending data.
