"""
🟡 Project 04 — SQL Drills (fill in the queries yourself)
=========================================================

First run setup_db.py to create the database. Then fill in each SQL query
string below. Run this file to check your answers automatically.

    python3 projects/04_sql_practice/setup_db.py
    python3 projects/04_sql_practice/queries.py

SQL is read like a sentence:
    SELECT  <columns>   FROM <table>   WHERE <condition>
    GROUP BY <column>   ORDER BY <column>   LIMIT <n>
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "shop.db"


# ===========================================================================
# Fill in each SQL string. The expected answer is shown in the comment.
# ===========================================================================

# DRILL 1: Select the names of all customers from Pakistan.
#          Expected rows: Ayesha, Sara, Bilal
QUERY_1 = """
-- YOUR SQL HERE, e.g. SELECT name FROM customers WHERE country = '...';
"""

# DRILL 2: Count how many orders there are in total.
#          Expected: 10
QUERY_2 = """
-- YOUR SQL HERE  (hint: SELECT COUNT(*) ...)
"""

# DRILL 3: Total revenue (SUM of amount) per country.
#          Hint: JOIN orders to customers, then GROUP BY country.
#          Expected: Germany 1495.0, Pakistan 3255.0
QUERY_3 = """
-- YOUR SQL HERE
-- SELECT c.country, SUM(o.amount)
-- FROM orders o JOIN customers c ON o.customer_id = c.customer_id
-- GROUP BY c.country;
"""

# DRILL 4: The single highest-value order (product + amount), top 1.
#          Expected: Laptop, 1300.0
QUERY_4 = """
-- YOUR SQL HERE (hint: ORDER BY amount DESC LIMIT 1)
"""


# ===========================================================================
# THE MENTOR'S CHECK — do not edit below this line
# ===========================================================================

EXPECTED = {
    "QUERY_1": [("Ayesha",), ("Sara",), ("Bilal",)],
    "QUERY_2": [(10,)],
    "QUERY_3": [("Germany", 1495.0), ("Pakistan", 3255.0)],
    "QUERY_4": [("Laptop", 1300.0)],
}


def _normalize(rows):
    # Sort so order doesn't matter, and round floats.
    out = []
    for row in rows:
        out.append(tuple(round(x, 2) if isinstance(x, float) else x for x in row))
    return sorted(out, key=lambda r: tuple(str(x) for x in r))


def main():
    if not DB_PATH.exists():
        print("❌ Database not found. Run setup_db.py first.")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    queries = {"QUERY_1": QUERY_1, "QUERY_2": QUERY_2, "QUERY_3": QUERY_3, "QUERY_4": QUERY_4}

    passed = 0
    for name, sql in queries.items():
        clean = "\n".join(l for l in sql.splitlines() if not l.strip().startswith("--")).strip()
        if not clean:
            print(f"⬜ {name}: not attempted yet.")
            continue
        try:
            rows = cur.execute(clean).fetchall()
            if _normalize(rows) == _normalize(EXPECTED[name]):
                print(f"✅ {name}: correct!")
                passed += 1
            else:
                print(f"❌ {name}: got {rows}, expected {EXPECTED[name]}")
        except Exception as e:
            print(f"❌ {name}: SQL error -> {e}")

    conn.close()
    print(f"\n🥋 {passed}/4 drills solved.")
    if passed == 4:
        print("Excellent. You can query data. This skill alone gets interviews.")


if __name__ == "__main__":
    main()
