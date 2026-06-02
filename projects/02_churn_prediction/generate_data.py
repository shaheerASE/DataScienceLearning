"""
🟣 Project 02 — Step 0: Generate a realistic dataset
=====================================================

In the real world, sometimes you must simulate data to build and test a
pipeline before the production data is ready. Here we create a synthetic but
*realistic* telecom "customer churn" dataset.

Churn = a customer leaving / cancelling. Predicting it is one of the most
common, well-paid ML tasks in industry (telecom, banks, SaaS, gyms...).

Run:
    python3 projects/02_churn_prediction/generate_data.py
"""

import numpy as np
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUT_PATH = PROJECT_ROOT / "data" / "churn.csv"

rng = np.random.default_rng(42)  # fixed seed -> reproducible (a science habit)
N = 1000

# --- Simulate customer features ---
tenure_months = rng.integers(1, 72, N)              # how long they've been a customer
monthly_charges = rng.normal(70, 25, N).clip(20, 150)
has_contract = rng.choice([0, 1], N, p=[0.55, 0.45])  # 1 = on a yearly contract
support_calls = rng.poisson(1.5, N)                  # number of complaints/calls
is_senior = rng.choice([0, 1], N, p=[0.8, 0.2])

# --- Build a "true" churn probability from the features (the hidden pattern) ---
# Customers churn MORE when: low tenure, high charges, no contract, many support calls.
logit = (
    -1.0
    - 0.04 * tenure_months
    + 0.015 * monthly_charges
    - 1.2 * has_contract
    + 0.35 * support_calls
    + 0.3 * is_senior
)
prob_churn = 1 / (1 + np.exp(-logit))
churned = rng.binomial(1, prob_churn)

df = pd.DataFrame({
    "tenure_months": tenure_months,
    "monthly_charges": monthly_charges.round(2),
    "has_contract": has_contract,
    "support_calls": support_calls,
    "is_senior": is_senior,
    "churned": churned,
})

OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUT_PATH, index=False)
print(f"✅ Wrote {len(df)} rows to {OUT_PATH}")
print(f"   Churn rate: {df['churned'].mean():.1%}")
print(df.head())
