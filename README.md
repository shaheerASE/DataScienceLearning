# 🥋 The MLOps Dojo — Data Science × DevOps

> *"First learn stand, then learn fly."*
> You walk two paths at once: the **Data Scientist** (find truth in data) and the
> **DevOps Engineer** (ship it, automate it, keep it running). Together the market
> calls this **MLOps / ML Engineer** — and it is one of the most valuable, future-proof
> careers in both 🇩🇪 Germany and 🇵🇰 Pakistan.

This repository is your **dojo**. We do not just read. We **build**, **break**, and
**ship** — the way real teams in industry work.

---

## 🎯 Your Goal (carved in stone)

> Become a **Data Scientist + DevOps Engineer**, with market-relevant, practical
> skills to survive and thrive — whether doing a Master's in Germany or working in Pakistan.

**Training style:** Straight into practical, industrial tasks. Explanations come *as we go*.

---

## 🧭 The Two Paths, One Journey

```
        DATA SCIENCE                          DEVOPS
   ┌────────────────────┐            ┌────────────────────┐
   │ Python · Pandas    │            │ Git · Linux/CLI    │
   │ Stats · Viz · EDA  │   ───►     │ Docker · CI/CD     │
   │ Machine Learning   │  fuse into │ Cloud · APIs       │
   └────────────────────┘   MLOps    └────────────────────┘
                    \                /
                     \              /
              ┌──────────────────────────┐
              │   ML ENGINEER / MLOps     │
              │  build model → ship it →  │
              │  automate → monitor it    │
              └──────────────────────────┘
```

---

## 🗺️ The Belts (Your Roadmap)

Each belt = real skills + a real artifact you build with your own hands.

| Belt | Focus | You will build |
|------|-------|----------------|
| ⚪ **White** | Python refresher + Git + CLI habits | A clean data script, committed properly |
| 🟡 **Yellow** | NumPy & Pandas — real data wrangling | A data-cleaning pipeline on messy CSVs |
| 🟢 **Green** | EDA & visualization | An analysis report with charts + insights |
| 🔵 **Blue** | Statistics that industry actually uses | A/B test + hypothesis testing notebook |
| 🟣 **Purple** | Machine Learning fundamentals | A trained, evaluated prediction model |
| 🟤 **Brown** | DevOps: Docker, FastAPI, CI/CD | Your model served as a containerized API |
| ⚫ **Black** | Full MLOps project, end to end | Data → model → API → Docker → CI pipeline |

---

## 📂 Dojo Structure

```
DataScienceLearning/
├── README.md
├── requirements.txt           <- dependencies (DevOps habit: pin what you use)
├── lessons/                   <- read this first, each belt
├── exercises/                 <- where you sweat
├── projects/                  <- industrial-style projects (the real deal)
│   ├── 01_sales_pipeline/     <- 🟡 YOU build this (Pandas, TODOs + hints)
│   ├── 02_churn_prediction/   <- 🟢🟣🟤 full MLOps demo (data→model→API→Docker)
│   ├── 03_ab_testing/         <- 🔵 statistics: A/B test + p-values
│   └── 04_sql_practice/       <- 🟡 SQL drills on a real mini-database
├── tests/                     <- automated tests (run by CI)
├── .github/workflows/ci.yml   <- CI/CD: tests run in the cloud on every push
├── PROGRESS.md                <- YOUR progress tracker — update it as you go
└── data/                      <- datasets to train on
```

---

## 🧘 Rules of the Dojo

1. **Type every line yourself.** The hand must remember.
2. **Commit small, commit often.** Each commit is a step. (This is also a DevOps skill.)
3. **Make it run, then make it right, then make it fast.**
4. **Break it on purpose.** Then fix it. That is how you truly learn.
5. **Patience.** Black belts are made of many small white-belt days.

---

## ▶️ Start Here

1. Follow **`SETUP_WINDOWS.md`** (company machine? it has a safe `git --local` path).
2. Confirm your environment with one command — your first win:
   ```bash
   python verify_setup.py
   ```
   All green = the dojo is ready. Tick your first boxes in **`PROGRESS.md`**.
3. Then open **`projects/01_sales_pipeline/`** (you build) and
   **`projects/02_churn_prediction/`** (full demo you run).

We learn by doing — beginning now.
