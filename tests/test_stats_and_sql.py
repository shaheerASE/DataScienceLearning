"""
🟤 DevOps practice — tests for the stats (A/B) and SQL projects
===============================================================
These run in CI on every push, guarding Projects 03 and 04.
"""

import sqlite3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _run(path):
    result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
    assert result.returncode == 0, f"{path} failed:\n{result.stderr}"
    return result


# --- Project 03: A/B testing ---

def test_ab_test_runs_and_finds_significance():
    out = _run(ROOT / "projects" / "03_ab_testing" / "ab_test.py").stdout
    # With the fixed seed, the green button is a real, significant winner.
    assert "STATISTICALLY SIGNIFICANT" in out


# --- Project 04: SQL ---

def test_sql_database_builds_and_queries_work():
    _run(ROOT / "projects" / "04_sql_practice" / "setup_db.py")
    db = ROOT / "projects" / "04_sql_practice" / "shop.db"
    assert db.exists()

    conn = sqlite3.connect(db)
    cur = conn.cursor()
    # Sanity: the data we expect is really there.
    assert cur.execute("SELECT COUNT(*) FROM orders").fetchone()[0] == 10
    revenue = dict(cur.execute(
        "SELECT c.country, SUM(o.amount) FROM orders o "
        "JOIN customers c ON o.customer_id = c.customer_id GROUP BY c.country"
    ).fetchall())
    conn.close()
    assert revenue["Germany"] == 1495.0
    assert revenue["Pakistan"] == 3255.0
