"""
🟡 Project 04 — SQL Practice: build the database
=================================================

SQL is on nearly EVERY data science / data engineering job posting. You cannot
escape it. Good news: Python ships with SQLite, so you need NO extra software.

This script creates a small e-commerce database (customers + orders) so you
have something real to query.

Run:
    python3 projects/04_sql_practice/setup_db.py
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "shop.db"

# Start fresh every time.
if DB_PATH.exists():
    DB_PATH.unlink()

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.executescript(
    """
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        name        TEXT,
        country     TEXT,
        signup_date TEXT
    );

    CREATE TABLE orders (
        order_id    INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product     TEXT,
        amount      REAL,
        order_date  TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
    """
)

customers = [
    (1, "Ayesha",  "Pakistan",   "2025-01-10"),
    (2, "Lukas",   "Germany",    "2025-02-15"),
    (3, "Sara",    "Pakistan",   "2025-02-20"),
    (4, "Jonas",   "Germany",    "2025-03-01"),
    (5, "Bilal",   "Pakistan",   "2025-03-12"),
    (6, "Mia",     "Germany",    "2025-04-05"),
]

orders = [
    (101, 1, "Laptop",   1200.00, "2025-03-01"),
    (102, 1, "Mouse",      25.00, "2025-03-02"),
    (103, 2, "Keyboard",   80.00, "2025-03-05"),
    (104, 3, "Monitor",   300.00, "2025-03-10"),
    (105, 3, "Laptop",   1100.00, "2025-03-11"),
    (106, 4, "Mouse",      25.00, "2025-03-15"),
    (107, 5, "Monitor",   320.00, "2025-04-01"),
    (108, 2, "Laptop",   1300.00, "2025-04-02"),
    (109, 6, "Keyboard",   90.00, "2025-04-10"),
    (110, 1, "Monitor",   310.00, "2025-04-12"),
]

cur.executemany("INSERT INTO customers VALUES (?,?,?,?)", customers)
cur.executemany("INSERT INTO orders VALUES (?,?,?,?,?)", orders)
conn.commit()
conn.close()

print(f"✅ Built database: {DB_PATH.name}")
print(f"   {len(customers)} customers, {len(orders)} orders.")
print("   Now open queries.py and solve the SQL drills.")
