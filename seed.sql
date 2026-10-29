INSERT INTO agents VALUES ('AG1','Southeast'),('AG2','West'),('AG3','Northeast');
INSERT INTO applications VALUES
('K001','C101','2026-09-01','approved',170000,'AG1'),
('K002','C102','2026-09-02','submitted',210000,'AG2'),
('K003','C102','2026-09-02','submitted',210000,'AG2'),
('K004','C103','2026-09-03','funded',95000,'AG1'),
('K005','C104','2026-09-04','approved',0,'AG3'),
('K006','C105','2026-09-05','submitted',150000,'AG3'),
('K007','C106','2026-09-06','funded',125000,'AG9');
INSERT INTO events VALUES (1,'K001','submitted','2026-09-01'),(2,'K001','approved','2026-09-04'),(3,'K004','funded','2026-09-05'),(4,'K007','funded','2026-09-07');
