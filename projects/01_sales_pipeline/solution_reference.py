"""
🔒 SEALED SCROLL — Reference Solution for Project 01
=====================================================

Student: DO NOT open this until you have truly tried pipeline.py yourself.
Struggle first. The struggle is where the learning lives. THEN compare.

Run it to see the expected output:
    python3 projects/01_sales_pipeline/solution_reference.py
"""

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_PATH = PROJECT_ROOT / "data" / "raw_sales.csv"
CLEAN_PATH = PROJECT_ROOT / "data" / "clean_sales.csv"


def load_data(path):
    df = pd.read_csv(path)
    print(f"📥 Loaded {len(df)} rows from {path.name}")
    return df


def clean_data(df):
    df["category"] = df["category"].str.title()              # 2a
    df["region"] = df["region"].str.title()                  # 2b
    df["date"] = pd.to_datetime(df["date"], errors="coerce") # 2c
    df = df.dropna(subset=["quantity"])                      # 2d
    df = df[df["quantity"] > 0]                              # 2e
    df = df.dropna(subset=["date"])                          # 2f
    print(f"🧹 After cleaning: {len(df)} rows remain")
    return df


def add_revenue(df):
    df = df.copy()
    df["revenue"] = df["quantity"] * df["unit_price"]        # 3
    return df


def summarize(df):
    print("\n===== 📊 BUSINESS SUMMARY =====")
    print(f"Total revenue: {df['revenue'].sum():.2f}")        # 4a

    print("\nRevenue by category:")                           # 4b
    print(df.groupby("category")["revenue"].sum().sort_values(ascending=False))

    print("\nRevenue by region:")                             # 4c
    print(df.groupby("region")["revenue"].sum())


def save_data(df, path):
    df.to_csv(path, index=False)
    print(f"\n💾 Clean data written to {path.name}")


def main():
    df = load_data(RAW_PATH)
    df = clean_data(df)
    df = add_revenue(df)
    summarize(df)
    save_data(df, CLEAN_PATH)
    print("\n🥋 Pipeline complete.")


if __name__ == "__main__":
    main()
