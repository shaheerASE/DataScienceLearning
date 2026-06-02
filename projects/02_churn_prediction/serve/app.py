"""
🟤 Project 02 — Step 3: Serve the model as an API (the "Ops" in MLOps)
======================================================================

A model is useless until other software can ask it questions. We wrap it in a
web API using FastAPI. Now ANY app (a website, a mobile app, another service)
can send customer data and get a churn prediction back.

Run locally (after training the model):
    pip install fastapi uvicorn
    uvicorn projects.02_churn_prediction.serve.app:app --reload
Then open http://127.0.0.1:8000/docs  -> interactive API you can click & test.
"""

from pathlib import Path
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "churn_model.joblib"

app = FastAPI(title="Churn Prediction API", version="1.0")

# Load the model ONCE at startup, not on every request (performance habit).
model = joblib.load(MODEL_PATH)


class Customer(BaseModel):
    """Defines + validates the input. FastAPI rejects bad data automatically."""
    tenure_months: int = Field(..., ge=0, example=5)
    monthly_charges: float = Field(..., ge=0, example=95.0)
    has_contract: int = Field(..., ge=0, le=1, example=0)
    support_calls: int = Field(..., ge=0, example=4)
    is_senior: int = Field(..., ge=0, le=1, example=0)


@app.get("/health")
def health():
    """A health check — DevOps uses this to know the service is alive."""
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: Customer):
    """Take one customer, return churn probability + a yes/no flag."""
    row = pd.DataFrame([customer.model_dump()])
    probability = float(model.predict_proba(row)[0, 1])
    return {
        "churn_probability": round(probability, 3),
        "will_churn": bool(probability >= 0.5),
        "risk": "high" if probability >= 0.5 else "low",
    }
