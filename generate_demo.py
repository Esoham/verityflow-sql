"""Deterministic fictional application data for portfolio demonstrations."""
import csv,random
from datetime import date,timedelta
from pathlib import Path
random.seed(42)
out=Path(__file__).parent/'data'/'generated_applications.csv'
out.parent.mkdir(exist_ok=True)
with out.open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['application_id','borrower_key','created_at','stage','loan_amount','agent_id'])
 for i in range(1,2001):
  day=date(2026,1,1)+timedelta(days=random.randrange(180))
  borrower=f'C{random.randrange(1,1701):04d}'
  stage=random.choices(['submitted','approved','funded','declined'],[45,30,15,10])[0]
  amount=random.randrange(50,451)*1000
  agent=random.choice(['AG1','AG2','AG3','AG4'])
  if i%97==0:amount=0
  if i%131==0:agent='UNKNOWN'
  w.writerow([f'APP{i:05d}',borrower,day,stage,amount,agent])
print(f'Wrote 2000 synthetic records to {out}')
