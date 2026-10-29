-- Potential duplicate applicant on same day; review rather than automatically delete.
SELECT applicant_key,created_at,COUNT(*) AS application_count
FROM applications GROUP BY applicant_key,created_at HAVING COUNT(*) > 1;
-- Nonpositive loan amounts.
SELECT application_id,loan_amount FROM applications WHERE loan_amount <= 0;
-- Unmapped agent IDs.
SELECT a.application_id,a.agent_id FROM applications a LEFT JOIN agents g ON g.agent_id=a.agent_id WHERE g.agent_id IS NULL;
-- Application stage without a corresponding event.
SELECT a.application_id,a.stage FROM applications a LEFT JOIN events e ON e.application_id=a.application_id AND e.stage=a.stage WHERE e.event_id IS NULL;
