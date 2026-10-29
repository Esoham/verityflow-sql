CREATE TABLE applications (application_id TEXT PRIMARY KEY, applicant_key TEXT NOT NULL, created_at TEXT NOT NULL, stage TEXT NOT NULL, loan_amount INTEGER NOT NULL, agent_id TEXT NOT NULL);
CREATE TABLE agents (agent_id TEXT PRIMARY KEY, region TEXT NOT NULL);
CREATE TABLE events (event_id INTEGER PRIMARY KEY, application_id TEXT NOT NULL, stage TEXT NOT NULL, event_date TEXT NOT NULL);
