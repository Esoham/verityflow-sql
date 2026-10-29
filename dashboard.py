"""Generate a self-contained HTML dashboard from the seeded SQLite demonstration."""
from pathlib import Path
import sqlite3,html
ROOT=Path(__file__).resolve().parent
db=sqlite3.connect(':memory:')
for script in ('schema.sql','seed.sql'):db.executescript((ROOT/script).read_text())
total=db.execute('SELECT COUNT(*) FROM applications').fetchone()[0]
stages=db.execute('SELECT stage,COUNT(*) FROM applications GROUP BY stage ORDER BY stage').fetchall()
invalid=db.execute('SELECT COUNT(*) FROM applications WHERE loan_amount<=0').fetchone()[0]
unmapped=db.execute('SELECT COUNT(*) FROM applications a LEFT JOIN agents g ON a.agent_id=g.agent_id WHERE g.agent_id IS NULL').fetchone()[0]
rows=''.join(f'<tr><td>{html.escape(stage)}</td><td>{count}</td><td><div class="bar" style="width:{100*count/max(1,total):.1f}%"></div></td></tr>' for stage,count in stages)
page=f"""<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>VerityFlow | Operations Intelligence</title><style>
body{{font:16px system-ui;background:#0b1220;color:#e8eef7;margin:0;padding:35px;max-width:1000px;margin:auto}}
h1{{font-size:38px;margin-bottom:6px}}p{{color:#a8b9cc}}.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin:28px 0}}.card{{background:#18263b;padding:20px;border-radius:14px}}.value{{font-size:34px;font-weight:750;color:#78d5bd}}table{{width:100%;border-collapse:collapse;background:#18263b;border-radius:14px;overflow:hidden}}td,th{{text-align:left;padding:14px;border-bottom:1px solid #33465d}}.bar{{height:12px;background:#78d5bd;border-radius:8px}}.note{{margin-top:25px;font-size:13px}}
</style><h1>VerityFlow</h1><p>Operations Intelligence · Synthetic loan application data</p>
<div class="cards"><div class="card">Applications<div class="value">{total}</div></div><div class="card">Invalid amounts<div class="value">{invalid}</div></div><div class="card">Unmapped agents<div class="value">{unmapped}</div></div></div>
<h2>Application stage distribution</h2><table><thead><tr><th>Stage</th><th>Count</th><th>Share</th></tr></thead><tbody>{rows}</tbody></table>
<p class="note">Demonstration only. Data is fictional. Metrics reflect the small seeded dataset, not a lender's operations.</p></html>"""
target=ROOT/'dashboard.html';target.write_text(page,encoding='utf-8');print(f'Wrote {target}')
