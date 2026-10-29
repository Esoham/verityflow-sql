from pathlib import Path
import sqlite3
HERE=Path(__file__).resolve().parent
con=sqlite3.connect(':memory:')
for name in ('schema.sql','seed.sql'): con.executescript((HERE/name).read_text())
for name in ('quality_checks.sql','reporting.sql'):
    print('\n'+name)
    sql=(HERE/name).read_text()
    for query in sql.split(';'):
        if query.strip():
            query='\n'.join(line for line in query.splitlines() if not line.lstrip().startswith('--')).strip()
            if not query: continue
            cur=con.execute(query)
            print([column[0] for column in cur.description])
            for row in cur.fetchall(): print(row)
