import sqlite3

conn = sqlite3.connect('flow_agent.db')
cur = conn.cursor()
tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
found = False
for t in tables:
    cols = [c[1] for c in cur.execute(f"PRAGMA table_info({t})").fetchall()]
    for c in cols:
        try:
            m = cur.execute(f"SELECT * FROM {t} WHERE {c} LIKE '%26d8b4c7%'").fetchall()
            if m:
                print(f"Found in {t}.{c}: {m}")
                found = True
        except Exception:
            pass

if not found:
    print("26d8b4c7 was not found in flow_agent.db!")
