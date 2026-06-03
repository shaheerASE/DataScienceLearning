"""
🟡 Yellow Belt — Pandas Drills (runnable companion to lesson 02)
================================================================

Every movement from lessons/02_yellow_belt_pandas.md, runnable. Read the output
next to the lesson. Then type your own variations — change values, add columns,
break it, fix it.

    python exercises/02_pandas_drills.py
"""

import numpy as np
import pandas as pd

print("\n--- Movement 1: the DataFrame ---")
df = pd.DataFrame({
    "name":    ["Ayesha", "Lukas", "Sara", "Jonas"],
    "country": ["Pakistan", "Germany", "Austria", "Germany"],
    "sales":   [1200, 80, 1400, 25],
})
print(df)
print("shape:", df.shape)

print("\n--- Movement 2: looking ---")
print(df.describe())

print("\n--- Movement 3: filtering ---")
print("big sales (>100):")
print(df[df["sales"] > 100])

print("\n--- Movement 4: cleaning text ---")
messy = pd.Series(["Germany", "germany", " GERMANY "])
print("before:", list(messy))
print("after :", list(messy.str.strip().str.title()))

print("\n--- Movement 5: missing data ---")
d = pd.DataFrame({"q": [5, np.nan, 3, -1]})
clean = d.dropna(subset=["q"])
clean = clean[clean["q"] > 0]
print("cleaned quantities:", list(clean["q"]))

print("\n--- Movement 6: new column (feature engineering) ---")
df["sales_eur"] = (df["sales"] * 0.92).round(2)
print(df[["name", "sales", "sales_eur"]])

print("\n--- Movement 7: group & summarize ---")
print(df.groupby("country")["sales"].sum())

print("\n🥋 Drills complete. Compare each block to lesson 02, then do Project 01.")


print("\n -----My Drills-----")

# Challenge 1
# Print only Country Pakistan

print(f"--Pakistan Only: \n", df[df["country"] == "Pakistan"])
print()



# Challenge 2
# Add a new Column
print("\n ---Pakistan Sales---")
df["sales_pkr"] = df["sales"]*280
print(df[["name", "sales", "sales_pkr"]])
print()

# Challenge 3
# Print Average sales per country

print(f"Average Sales per Country")
print(df.groupby("country")["sales"].mean())
print()

# Challenge 4
# Print the Highest gross Sales

print(f"---Highest gross sales---")
print(df["sales"].max())