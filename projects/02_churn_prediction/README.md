# 🤖 Project 02 — Customer Churn Prediction (Full MLOps Arc)

> **This is your North Star project.** It walks the ENTIRE journey a real ML
> Engineer does: raw data → analysis → model → served API → Docker container.
> Every script here is complete, tested, and runnable. Study it. Reproduce it.
> Then, later, you will build one like it from scratch by yourself.

Churn = a customer leaving. Predicting it is a top-paid, very common ML task in
telecom, banking, SaaS, and subscriptions — in Germany 🇩🇪 and Pakistan 🇵🇰 alike.

---

## 🗺️ The arc (and which belt each step trains)

| Step | File | Belt | What it does |
|------|------|------|--------------|
| 0 | `generate_data.py` | ⚪ | Simulate a realistic 1000-customer dataset |
| 1 | `01_explore.py` | 🟢 | EDA + charts: *what drives churn?* |
| 2 | `02_train.py` | 🟣 | Train, honestly evaluate, and save a model |
| 3 | `serve/app.py` | 🟤 | Serve the model as a live web API (FastAPI) |
| 3 | `serve/Dockerfile` | 🟤 | Package it to run anywhere (Docker) |

---

## ▶️ Run the whole thing (in order)

```bash
# from the repo root, with your virtual environment active:
pip install -r requirements.txt

python3 projects/02_churn_prediction/generate_data.py   # make the data
python3 projects/02_churn_prediction/01_explore.py       # explore + charts
python3 projects/02_churn_prediction/02_train.py         # train + evaluate
```

Then serve the model as an API:
```bash
pip install fastapi uvicorn
uvicorn projects.02_churn_prediction.serve.app:app --reload
# open http://127.0.0.1:8000/docs  and click "Try it out"
```

Or run it the DevOps way, in a container (needs Docker Desktop installed):
```bash
docker build -t churn-api -f projects/02_churn_prediction/serve/Dockerfile projects/02_churn_prediction
docker run -p 8000:8000 churn-api
```

---

## 📊 What "good" looks like (your targets)

- Churn rate of the dataset: ~24%
- Model ROC-AUC on unseen data: ~0.77 (well above 0.5 = random guessing)
- The API returns a `churn_probability` and `risk` for any customer you send

Example API call result for a new, expensive, no-contract customer:
```json
{ "churn_probability": 0.959, "will_churn": true, "risk": "high" }
```

---

## 🧠 The big lessons hiding in this project

1. **80% of ML is NOT the model** — it's data, evaluation, and shipping.
2. **Never test on training data** — the train/test split keeps you honest.
3. **A model on your laptop earns nothing** — serving + Docker is what makes it real.
4. **Reproducibility** — fixed random seeds + pinned requirements = same result every time.

---

## 🥋 Your turn (when you're ready)

After you finish Project 01 (the sales pipeline), come back here and:
1. Run all of Project 02 yourself and confirm the numbers match.
2. Open each file and read every comment — ask "why" three times.
3. **Challenge:** change one thing (e.g. swap `LogisticRegression` for
   `RandomForestClassifier`) and see if the ROC-AUC improves. Tell me what you find.
