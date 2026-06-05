"""
🟣 LEARN BY BUILDING — Lesson 03a: What "training a model" REALLY is
====================================================================

You said: "I ran scripts but never learned to TRAIN a model."
Fair. So here you BUILD one — on data small enough to see in your head.

THE PROBLEM:
    Predict whether a student passes an exam, from ONE thing: hours studied.

        hours: 1  2  3  6  7  8
        pass : 0  0  0  1  1  1     (0 = failed, 1 = passed)

You can SEE the pattern with your eyes: study more -> pass. Our job is to make a
model DISCOVER that pattern by itself, and put a NUMBER on it.

HOW TO USE THIS FILE:
  - Read each numbered block.
  - Where you see  >>> WRITE:  you type the code yourself. Do NOT look anything up
    first — try from the explanation. Then run and see.
  - Run it:   python projects/02_churn_prediction/learn_03a_train_from_scratch.py
  - It will tell you if each step is right.

There are NO hidden answers in this file. The struggle is the point.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression


# ---------------------------------------------------------------------------
# STEP 1 — The data.
# A model needs two things:
#   X = the FEATURES (the inputs / clues).  Here: hours studied.
#   y = the TARGET   (the answer we want).  Here: passed or not.
#
# scikit-learn expects X as a 2D table (rows = students, columns = features),
# even when there's only ONE feature. That's why we use double brackets / reshape.
# ---------------------------------------------------------------------------

hours = np.array([1, 2, 3, 6, 7, 8]).reshape(-1, 1)   # shape (6, 1): 6 rows, 1 feature
passed = np.array([0, 0, 0, 1, 1, 1])                 # shape (6,):   6 answers

print("X (features):\n", hours.ravel())
print("y (target):  ", passed)


# ---------------------------------------------------------------------------
# STEP 2 — Create the (untrained) model.
# Right now it knows NOTHING. Its knobs (w, b) are not set yet.
#
# >>> WRITE: make a LogisticRegression and store it in a variable called `model`.
#     (hint: it's just  LogisticRegression()  — the class you imported above)
# ---------------------------------------------------------------------------

model = None   # <-- replace None with the model you create


# ---------------------------------------------------------------------------
# STEP 3 — TRAIN it. This is the whole point.
# .fit(X, y) runs the gradient-descent loop: it nudges w and b over and over
# until the formula  sigmoid(w*hours + b)  matches the real answers as well as
# it can. After this ONE line, the model has LEARNED.
#
# >>> WRITE: call model.fit(...) with the hours and passed data.
# ---------------------------------------------------------------------------

# >>> WRITE your .fit(...) line here


# ---------------------------------------------------------------------------
# STEP 4 — Look at what it LEARNED.
# The trained knob `w` lives in  model.coef_  and the bias `b` in model.intercept_.
# If training worked, w should be a POSITIVE number (more hours -> more likely to pass).
#
# >>> WRITE: print model.coef_ and model.intercept_
# ---------------------------------------------------------------------------

# >>> WRITE your two print lines here


# ---------------------------------------------------------------------------
# STEP 5 — USE the trained model to predict a NEW student.
# A student studied 5 hours. Will they pass? What's the probability?
#   model.predict(...)       -> 0 or 1  (the decision)
#   model.predict_proba(...) -> [prob_fail, prob_pass]  (the confidence)
# Remember: the input must be 2D, like [[5]].
#
# >>> WRITE: predict the class AND the probability for a student who studied 5 hours.
# ---------------------------------------------------------------------------

# >>> WRITE your prediction lines here


# ---------------------------------------------------------------------------
# 🥋 SELF-CHECK — do not edit. Runs only if you filled the steps above.
# ---------------------------------------------------------------------------
def _check():
    if model is None:
        print("\n❌ Step 2 not done: `model` is still None.")
        return
    try:
        w = model.coef_[0][0]
    except Exception:
        print("\n❌ Step 3 not done: the model isn't trained yet (no .coef_). Did you call .fit()?")
        return
    print("\n----- MENTOR CHECK -----")
    if w > 0:
        print(f"✅ Trained! Learned weight w = {w:.3f} (positive = more hours, more passing). ")
        p5 = model.predict_proba([[5]])[0][1]
        print(f"✅ A 5-hour student has ~{p5*100:.0f}% predicted chance of passing.")
        print("\n🥋 THIS is training: the model found w from the data by itself.")
        print("   The churn model is the same — just 5 features instead of 1.")
    else:
        print(f"⚠️ w = {w:.3f}. That's unexpected — did you pair hours with the right answers?")


if __name__ == "__main__":
    _check()
