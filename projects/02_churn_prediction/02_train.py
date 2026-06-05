"""
🟣 Project 02 — Step 2: Train & evaluate a model
=================================================

Now the "flying", Daniel-san. We teach a model to predict churn from the
features. We then HONESTLY measure how good it is on data it has never seen.

Key idea — the golden rule of ML:
    NEVER test your model on data it learned from. That is cheating.
    We split data into TRAIN (to learn) and TEST (to judge fairly).

Run:
    python3 projects/02_churn_prediction/02_train.py
"""

import json
import joblib
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "churn.csv"
MODEL_DIR = PROJECT_ROOT / "projects" / "02_churn_prediction" / "model"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

FEATURES = ["tenure_months", "monthly_charges", "has_contract", "support_calls", "is_senior"]
TARGET = "churned"

df = pd.read_csv(DATA_PATH)
X = df[FEATURES]
y = df[TARGET]

# Split: 80% to learn from, 20% held back to judge honestly.
# stratify=y keeps the churn ratio the same in both halves.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Training on {len(X_train)} customers, testing on {len(X_test)} unseen ones.")

# A Pipeline bundles preprocessing + model into ONE object.
# StandardScaler puts all features on the same scale (good practice).
model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000)),
    # ("clf", RandomForestClassifier(n_estimators=200, random_state=42)),
    
])

model.fit(X_train, y_train)  # <- this is the actual "learning"

# --- Judge it on the unseen test set ---
preds = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]

metrics = {
    "accuracy": round(accuracy_score(y_test, preds), 3),
    "precision": round(precision_score(y_test, preds), 3),
    "recall": round(recall_score(y_test, preds), 3),
    "roc_auc": round(roc_auc_score(y_test, proba), 3),
}

print("\n===== 📊 MODEL SCORECARD (on unseen data) =====")
for name, value in metrics.items():
    print(f"  {name:10s}: {value}")
print("\n  What they mean:")
print("  - accuracy : overall % predicted correctly")
print("  - precision: when it says 'will churn', how often it's right")
print("  - recall   : of all who actually churned, how many we caught")
print("  - roc_auc  : overall ranking quality (0.5=coin flip, 1.0=perfect)")

# --- Which features matter most? (interpretability) ---
clf = model.named_steps["clf"]
if hasattr(clf,"coef_"):
    influence = pd.Series(model.named_steps["clf"].coef_[0], index=FEATURES).sort_values()
    print("\nFeature influence — coefficients (negative reduces churn):")
else:
    influence = pd.Series(clf.feature_importances_, index=FEATURES).sort_values(ascending=False)
    print("\nFeature importance — how much each feature drove decisions:")
print(influence.round(3))

# --- Save the model + metrics (this is what DevOps will deploy) ---
joblib.dump(model, MODEL_DIR / "churn_model.joblib")
(MODEL_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2))
print(f"\n💾 Saved model -> {MODEL_DIR / 'churn_model.joblib'}")
print(f"💾 Saved metrics -> {MODEL_DIR / 'metrics.json'}")
print("\n🥋 You have trained, judged, and saved a model. This is real ML.")
