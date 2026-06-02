"""
🟡 Project 01 — Sales Data Pipeline
====================================

This is your first industrial-style task. A pipeline is just a script that
takes data IN, transforms it, and sends clean data OUT.

    RAW CSV  ->  [ read ]  ->  [ clean ]  ->  [ summarize ]  ->  CLEAN CSV + report

Fill in each TODO. Run it. Break it. Fix it.
    python3 projects/01_sales_pipeline/pipeline.py

Mentor's note: 'pd' is the nickname everyone gives pandas. You will type it
thousands of times in your career. Get used to it now.
"""

import pandas as pd
from pathlib import Path

# Paths — we compute them relative to this file so the script works from anywhere.
# (DevOps habit: never hard-code paths like "C:/Users/me/..." — that breaks on
#  every other machine, including the server that runs your code in production.)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_PATH = PROJECT_ROOT / "data" / "raw_sales.csv"
CLEAN_PATH = PROJECT_ROOT / "data" / "clean_sales.csv"


def load_data(path):
    """Step 1 — READ the raw data into a DataFrame (a table in memory)."""
    df = pd.read_csv(path)
    print(f"📥 Loaded {len(df)} rows from {path.name}")
    return df


def clean_data(df):
    """Step 2 — CLEAN the dirty data. This is 80% of the real job."""

    # TODO 2a: Standardize the 'category' column to Title Case so that
    #          'electronics' and 'Electronics' become the SAME value.
    #          HINT:  df["category"] = df["category"].str.title()
    df["category"] = df["category"].str.title()

    # TODO 2b: Do the same for the 'region' column (Title Case).
    # YOUR CODE HERE
    df["region"] = df["region"].str.title()
    # TODO 2c: Convert 'date' to a real datetime. Bad dates become "NaT" (missing).
    #          HINT:  df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # YOUR CODE HERE
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # TODO 2d: Remove rows where 'quantity' is missing (empty cells).
    #          HINT:  df = df.dropna(subset=["quantity"])
    # YOUR CODE HERE
    df=df.dropna(subset=["quantity"])

    # TODO 2e: Remove rows where 'quantity' is negative (you cannot sell -1 item).
    #          HINT:  df = df[df["quantity"] > 0]
    # YOUR CODE HERE
    df = df[df["quantity"]>0]

    # TODO 2f: Remove rows with a missing date (NaT) — time analysis needs valid dates.
    #          HINT:  df = df.dropna(subset=["date"])
    # YOUR CODE HERE
    df=df.dropna(subset=["date"])
    print(f"🧹 After cleaning: {len(df)} rows remain")
    return df


def add_revenue(df):
    """Step 3a — Engineer a new column. Revenue = quantity * unit_price.
    Creating useful new columns from existing ones is called FEATURE ENGINEERING."""

    # TODO 3: Create a 'revenue' column = quantity * unit_price.
    # YOUR CODE HERE
    df["revenue"] = df["quantity"] * df["unit_price"]
    return df


def summarize(df):
    """Step 3b — Answer the manager's question: revenue by category and region."""

    print("\n===== 📊 BUSINESS SUMMARY =====")

    # TODO 4a: Print total revenue across all orders.
    #          HINT:  df["revenue"].sum()
    # YOUR CODE HERE
    total_Revenue = df['revenue'].sum()
    print(f"Total Revenue: {total_Revenue:.2f}")
    # TODO 4b: Print revenue grouped by category, sorted highest first.
    #          HINT:  df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    # YOUR CODE HERE
    category_grouped = df.groupby("category", as_index=False)["revenue"].sum()
    sorted_grouped = category_grouped.sort_values("revenue",ascending=False)
    print(sorted_grouped)
    # TODO 4c: Print revenue grouped by region.
    #          HINT:  df.groupby("region")["revenue"].sum()
    # YOUR CODE HERE
    region_grouped = df.groupby("region", as_index=False)["revenue"].sum()
    print(region_grouped)



def save_data(df, path):
    """Step 4 — SAVE the clean data so others (and future-you) can use it."""
    df.to_csv(path, index=False)
    print(f"\n💾 Clean data written to {path.name}")


def main():
    """The pipeline, orchestrated. Read the order of operations — this IS the pipeline."""
    df = load_data(RAW_PATH)
    df = clean_data(df)
    df = add_revenue(df)
    summarize(df)
    save_data(df, CLEAN_PATH)
    print("\n🥋 Pipeline complete. Inspect data/clean_sales.csv with your own eyes.")


if __name__ == "__main__":
    main()
