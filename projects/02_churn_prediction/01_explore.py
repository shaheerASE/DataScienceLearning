"""
🟢 Project 02 — Step 1: Explore the data (EDA)
===============================================

EDA = Exploratory Data Analysis. Before ANY model, you look at the data with
your eyes and ask: what drives churn? A model you don't understand is a model
you cannot trust.

This script prints summaries AND saves charts to reports/.

Run:
    python3 projects/02_churn_prediction/01_explore.py
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # "Agg" = save charts to files, no GUI needed (works on servers)
import matplotlib.pyplot as plt
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "churn.csv"
REPORTS_DIR = PROJECT_ROOT / "projects" / "02_churn_prediction" / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

# --- 1. Look at the shape and basics ---
print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst look (.describe gives you mean, min, max, etc.):")
print(df.describe().round(2))

# --- 2. The headline number: how many churned? ---
churn_rate = df["churned"].mean()
print(f"\n📉 Overall churn rate: {churn_rate:.1%}")

# --- 3. Which features differ between churners and stayers? ---
print("\nAverage feature values, split by churn (this hints at WHAT drives churn):")
print(df.groupby("churned").mean().round(2))

# --- 4. Chart A: churn rate by contract status ---
by_contract = df.groupby("has_contract")["churned"].mean()
plt.figure(figsize=(6, 4))
by_contract.plot(kind="bar", color=["#e74c3c", "#2ecc71"])
plt.xticks([0, 1], ["No Contract", "On Contract"], rotation=0)
plt.ylabel("Churn rate")
plt.title("Customers without a contract churn far more")
plt.tight_layout()
chart_a = REPORTS_DIR / "churn_by_contract.png"
plt.savefig(chart_a, dpi=100)
plt.close()
print(f"\n🖼️  Saved {chart_a.name}")

# --- 5. Chart B: tenure distribution, churners vs stayers ---
plt.figure(figsize=(7, 4))
plt.hist(df[df.churned == 0]["tenure_months"], bins=20, alpha=0.6, label="Stayed")
plt.hist(df[df.churned == 1]["tenure_months"], bins=20, alpha=0.6, label="Churned")
plt.xlabel("Tenure (months)")
plt.ylabel("Number of customers")
plt.title("New customers churn most; loyalty grows with time")
plt.legend()
plt.tight_layout()
chart_b = REPORTS_DIR / "churn_by_tenure.png"
plt.savefig(chart_b, dpi=100)
plt.close()
print(f"🖼️  Saved {chart_b.name}")

print("\n🧠 Insight for the business: push customers onto contracts, and protect")
print("   new customers in their first months — that is where churn is highest.")
