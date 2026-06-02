# 🟡 Yellow Belt — Lesson 02: Pandas, Your True Hands

> *"Wax on, right hand. Wax off, left hand."* Pandas is the two hands of every
> data scientist. Today we train each movement on tiny examples — so that when
> you face the real Project 01 pipeline, your hands already know the way.

Everything below is **runnable**. Open a Python file or a terminal, type each
snippet yourself (do NOT copy-paste), and watch what it does. There is a
companion file `exercises/02_pandas_drills.py` that runs all of these for you.

```python
import pandas as pd   # everyone writes "pd". Always.
```

---

## Movement 1 — The DataFrame (a table in memory)

A **DataFrame** is just a spreadsheet living in your program: rows and columns.

```python
df = pd.DataFrame({
    "name":   ["Ayesha", "Lukas", "Sara", "Jonas"],
    "country":["Pakistan", "Germany", "Pakistan", "Germany"],
    "sales":  [1200, 80, 1400, 25],
})
print(df)
print(df.shape)     # (4, 3) -> 4 rows, 3 columns
print(df.columns)   # the column names
```

**Why:** every dataset you ever load becomes a DataFrame. This is home base.

---

## Movement 2 — Looking before you leap

Before doing anything, a professional *looks*.

```python
print(df.head(2))      # first 2 rows
print(df.describe())   # count, mean, min, max for number columns
print(df.info())       # column types + missing-value counts
```

**Why:** `df.info()` and `df.describe()` are the first thing you run on ANY new
dataset. They reveal missing values and surprises before they bite you.

---

## Movement 3 — Selecting columns and rows (filtering)

```python
print(df["sales"])                      # one column
print(df[["name", "sales"]])            # two columns (note the double brackets)

# Filtering: rows where a condition is true
big = df[df["sales"] > 100]             # only big sales
print(big)

pk = df[df["country"] == "Pakistan"]    # only Pakistan
print(pk)
```

**Why:** "give me only the rows that matter" is half of all data work. The
condition inside `df[ ... ]` is a yes/no test applied to every row.

---

## Movement 4 — Cleaning text (the Project 01 skill)

Real data has messy text: `"Germany"`, `"germany"`, `" Germany "`. To a
computer these are three *different* values. We standardize them.

```python
messy = pd.Series(["Germany", "germany", " GERMANY "])
clean = messy.str.strip().str.title()   # remove spaces, then Title Case
print(clean)        # all become "Germany"
```

**Why:** this exact `.str.title()` move is what you'll use in Project 01 to fix
the `category` and `region` columns. You just learned it on a toy first.

---

## Movement 5 — Handling missing data

```python
import numpy as np
d = pd.DataFrame({"q": [5, np.nan, 3, -1]})

print(d.isnull())              # True where a value is missing
d2 = d.dropna(subset=["q"])    # drop rows missing 'q'
d3 = d2[d2["q"] > 0]           # drop the impossible -1
print(d3)
```

**Why:** missing and impossible values lie to your analysis. Removing them
(or filling them) is the heart of "data cleaning" — the 80% of the job.

---

## Movement 6 — New columns (feature engineering)

```python
df["sales_eur"] = df["sales"] * 0.92    # a new column from an old one
print(df)
```

**Why:** combining columns into new, more useful ones is called *feature
engineering*. In Project 01 you create `revenue = quantity * unit_price` exactly
like this.

---

## Movement 7 — Group & summarize (the manager's answer)

```python
by_country = df.groupby("country")["sales"].sum()
print(by_country)
```

This says: *"split the rows by country, then sum the sales in each group."*
The output answers a business question in one line.

**Why:** `groupby` is the single most-used Pandas verb in industry. "Revenue per
region", "users per country", "average order per customer" — all `groupby`.

---

## 🥋 Your training

Run the drills and read each printed result against the explanation above:
```bash
python exercises/02_pandas_drills.py
```

Then — and only then — you are ready to fill the TODOs in
`projects/01_sales_pipeline/pipeline.py`. You will recognize every movement:
`.str.title()`, `.dropna()`, the `> 0` filter, the new column, the `groupby`.
You already practiced them all here.

---

## 🧘 The three whys

1. *Why* double brackets `df[["a","b"]]` for multiple columns but single for one?
2. *Why* must we standardize text BEFORE we `groupby` it?
3. *Why* is dropping a row with `quantity = -1` a judgment call, not an obvious rule?

Answer these in your own words, then walk to Project 01. Your hands are ready.
