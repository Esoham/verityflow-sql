-- Additional management reporting; compatible with the seeded SQLite demo.
-- KPI: volume by month and stage
WITH monthly AS (
 SELECT substr(created_at,1,7) AS month,stage,COUNT(*) AS application_count
 FROM applications GROUP BY substr(created_at,1,7),stage
)
SELECT month,stage,application_count,
 SUM(application_count) OVER (PARTITION BY month) AS monthly_total
FROM monthly ORDER BY month,stage;

-- Data-quality score by row (not a production risk score)
WITH flags AS (
 SELECT a.application_id,
 CASE WHEN a.loan_amount <= 0 THEN 1 ELSE 0 END AS invalid_amount,
 CASE WHEN g.agent_id IS NULL THEN 1 ELSE 0 END AS unmapped_agent
 FROM applications a LEFT JOIN agents g ON g.agent_id=a.agent_id
)
SELECT COUNT(*) AS records,
 SUM(CASE WHEN invalid_amount+unmapped_agent=0 THEN 1 ELSE 0 END) AS clean_records,
 ROUND(100.0*SUM(CASE WHEN invalid_amount+unmapped_agent=0 THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0),1) AS clean_pct
FROM flags;

-- Agent coverage by stage
SELECT COALESCE(g.region,'UNMAPPED') AS region,a.stage,COUNT(*) AS applications
FROM applications a LEFT JOIN agents g ON a.agent_id=g.agent_id
GROUP BY COALESCE(g.region,'UNMAPPED'),a.stage ORDER BY region,a.stage;
