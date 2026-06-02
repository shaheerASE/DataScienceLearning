"""
🟤 DevOps practice — Automated tests for the churn project
==========================================================

In industry, code is NOT trusted until tests prove it works. These tests run
automatically in CI (GitHub Actions) on every push. If you ever break the
pipeline, the tests turn RED and warn you before bad code ships.

This is the safety net every professional team relies on.

Run locally:
    pip install pytest
    pytest -v
"""

import json
import subprocess
import sys
from pathlib import Path

import pandas as pd
import joblib
import pytest

ROOT = Path(__file__).resolve().parents[1]
PROJ = ROOT / "projects" / "02_churn_prediction"
DATA = ROOT / "data" / "churn.csv"
MODEL = PROJ / "model" / "churn_model.joblib"
METRICS = PROJ / "model" / "metrics.json"


def _run(script):
    """Run a project script and fail the test if it errors."""
    result = subprocess.run(
        [sys.executable, str(PROJ / script)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, f"{script} failed:\n{result.stderr}"
    return result


@pytest.fixture(scope="session", autouse=True)
def build_artifacts():
    """Before tests run: generate data and train the model once."""
    _run("generate_data.py")
    _run("02_train.py")
    yield


# --- Data tests ---

def test_dataset_exists_and_has_expected_columns():
    df = pd.read_csv(DATA)
    expected = {"tenure_months", "monthly_charges", "has_contract",
                "support_calls", "is_senior", "churned"}
    assert expected.issubset(df.columns)
    assert len(df) == 1000


def test_churn_rate_is_reasonable():
    df = pd.read_csv(DATA)
    rate = df["churned"].mean()
    assert 0.10 < rate < 0.40, f"Unexpected churn rate: {rate}"


def test_no_negative_or_missing_quantities():
    df = pd.read_csv(DATA)
    assert df["tenure_months"].min() >= 0
    assert not df.isnull().any().any(), "Dataset should have no missing values"


# --- Model tests ---

def test_model_file_is_created():
    assert MODEL.exists(), "Training did not produce a model file"


def test_model_quality_meets_threshold():
    metrics = json.loads(METRICS.read_text())
    # A useful model must beat random guessing (0.5) by a clear margin.
    assert metrics["roc_auc"] > 0.70, f"Model too weak: {metrics}"


# --- Prediction / serving tests ---

def test_high_risk_scores_higher_than_low_risk():
    model = joblib.load(MODEL)
    high_risk = pd.DataFrame([{
        "tenure_months": 2, "monthly_charges": 110,
        "has_contract": 0, "support_calls": 5, "is_senior": 1,
    }])
    low_risk = pd.DataFrame([{
        "tenure_months": 60, "monthly_charges": 45,
        "has_contract": 1, "support_calls": 0, "is_senior": 0,
    }])
    p_high = model.predict_proba(high_risk)[0, 1]
    p_low = model.predict_proba(low_risk)[0, 1]
    assert p_high > p_low, "Risky customer should score higher than loyal one"
    assert 0.0 <= p_low <= 1.0 and 0.0 <= p_high <= 1.0
