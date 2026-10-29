-- Stage-level summary counts applications, not unique borrowers.
SELECT stage,COUNT(*) AS applications,SUM(loan_amount) AS requested_amount
FROM applications GROUP BY stage ORDER BY applications DESC,stage;
-- Region coverage, including unmapped records.
SELECT COALESCE(g.region,'UNMAPPED') AS region,COUNT(*) AS applications,
ROUND(AVG(CASE WHEN a.loan_amount > 0 THEN a.loan_amount END),2) AS avg_positive_amount
FROM applications a LEFT JOIN agents g ON a.agent_id=g.agent_id
GROUP BY COALESCE(g.region,'UNMAPPED') ORDER BY applications DESC,region;
