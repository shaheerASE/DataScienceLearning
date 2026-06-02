# 🟡 Project 01 — The Sales Data Pipeline

> **The scenario (this is real industry work):**
> You join a company. On day one, a manager drops a file on your desk:
> *"Here's last week's sales export. The numbers look off and I need a clean
> summary by end of day. Go."*
>
> This is the single most common task a junior data scientist does. We start here.

---

## 🎯 What you will build

A small **data pipeline** — a script that:
1. **Reads** raw messy data (`data/raw_sales.csv`)
2. **Cleans** it (the data is dirty on purpose — just like real life)
3. **Computes** a business summary (revenue per category, per region)
4. **Saves** the clean result so others can use it

This single project touches Python, Pandas, *and* good engineering habits.

---

## 🔍 First: look at the data with your own eyes

Before writing any code, a good data scientist **looks**. Open
`data/raw_sales.csv`. You will notice it is *dirty* — on purpose:

| Problem hiding in the data | Why it matters |
|---|---|
| `category` is inconsistent: `Electronics`, `electronics`, `kitchen` | Grouping will split the same category into many |
| `region` mixes case: `North`, `north`, `south` | Same problem — `North` ≠ `north` to a computer |
| Some `quantity` cells are **empty** | Math on missing values breaks or lies |
| One `quantity` is **negative** (`-1`) | You cannot sell minus-one mouse. Bad data. |
| One row has a **missing date** | Time analysis needs valid dates |

> 🧠 **Rule of the trade:** *Real data is always dirty. ~80% of the job is cleaning it.*
> Nobody warns you about this in school. I warn you now.

---

## 🥋 Your training steps

1. **Install the tools** (DevOps habit — set up your environment first):
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Open** `pipeline.py`. It is scaffolded with `# TODO` movements.
   Fill in each TODO. Each one is explained right above it.

3. **Run it** and watch it work:
   ```bash
   python3 projects/01_sales_pipeline/pipeline.py
   ```

4. When it runs clean, it prints a summary and writes
   `data/clean_sales.csv`. Open that file — admire your clean data.

5. **Commit your work** (the DevOps reflex):
   ```bash
   git add -A
   git commit -m "Complete sales pipeline: clean data + revenue summary"
   ```

---

## ✅ You have earned the stripe when...

- The script runs with **no errors**
- Negative and missing quantities are **gone**
- `Electronics` and `electronics` are counted as **one** category
- You can read the printed summary and **explain it to your manager**

When that is true — return to me. We move to **EDA & visualization** (Green Belt),
where we turn this clean data into charts that tell a story.

> *Patience. Make it run first. Then make it right.*
