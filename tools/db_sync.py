"""Sync flow_agent.db through git.

  python tools/db_sync.py save   # before commit: flush WAL into flow_agent.db and stage it
  python tools/db_sync.py load   # on another machine: overwrite local DB with the pushed one
"""
import sqlite3
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "flow_agent.db"
HEALTH_URL = "http://127.0.0.1:8100/health"


def git(*args: str) -> None:
    subprocess.run(["git", *args], cwd=ROOT, check=True)


def server_running() -> bool:
    try:
        urllib.request.urlopen(HEALTH_URL, timeout=2)
        return True
    except OSError:
        return False


def save() -> None:
    conn = sqlite3.connect(DB)
    busy, _, _ = conn.execute("PRAGMA wal_checkpoint(TRUNCATE)").fetchone()
    conn.close()
    if busy:
        sys.exit("Checkpoint blocked by an active reader/writer - wait for the worker to go idle and retry.")
    git("add", DB.name)
    print(f"{DB.name} flushed and staged.")


def load() -> None:
    # Replacing the file under a live connection, or leaving a stale -wal next to
    # the new file, corrupts the DB: SQLite would replay old WAL frames onto it.
    if server_running():
        sys.exit("Stop the agent server first (it holds the DB open).")
    git("fetch")
    for suffix in ("-wal", "-shm"):
        DB.with_name(DB.name + suffix).unlink(missing_ok=True)
    git("checkout", "@{u}", "--", DB.name)
    print(f"{DB.name} replaced with the upstream version.")


if __name__ == "__main__":
    commands = {"save": save, "load": load}
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        sys.exit(__doc__)
    commands[sys.argv[1]]()
