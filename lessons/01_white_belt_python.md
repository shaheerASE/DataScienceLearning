# ⚪ White Belt — Lesson 01: Python Fundamentals

> *"Not everything is as seems, Daniel-san."* — and not everything in code is as
> it seems either. We start slow.

Before you touch data, you must speak its language. That language is **Python**.
Today we learn the four movements that everything else is built on.

---

## Movement 1 — Variables (Naming what you hold)

A variable is a labeled box. You put something in, you read its label later.

```python
name = "student"      # text  (a string)
age = 25              # whole number (an integer)
height = 1.75         # decimal number (a float)
is_learning = True    # yes/no (a boolean)
```

**Why it matters:** Data is just values in boxes. Master the boxes first.

---

## Movement 2 — Lists (Holding many things)

Data is rarely one value. It is *many*. A list holds many in order.

```python
scores = [88, 92, 79, 100, 65]

print(scores[0])      # first item -> 88   (we count from 0!)
print(scores[-1])     # last item  -> 65
print(len(scores))    # how many?  -> 5
```

**Why it matters:** A column of data is just a list. You will use these forever.

---

## Movement 3 — Loops (Repetition builds strength)

To do a thing to *every* value, you loop. Wax on, wax off — again and again.

```python
scores = [88, 92, 79, 100, 65]

for score in scores:
    if score >= 90:
        print(score, "-> excellent")
    else:
        print(score, "-> keep training")
```

**Why it matters:** Processing every row of a dataset is a loop. This is the heartbeat of code.

---

## Movement 4 — Functions (One movement, reused)

A function is a movement you practice once, then call by name forever.

```python
def average(numbers):
    """Return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

scores = [88, 92, 79, 100, 65]
print("The average is:", average(scores))
```

**Why it matters:** Good data scientists do not repeat themselves. They build
movements (functions) and reuse them.

---

## 🥋 Your Training (Do this — do not just read)

Open `exercises/01_first_steps.py`. The tasks are waiting for you there.
Type every line yourself. Run it. Break it. Fix it.

When it runs clean, you have earned the first stripe on your white belt.

```bash
python exercises/01_first_steps.py
```

---

## 🧘 Reflect Before You Move On

Ask yourself the three "whys":
1. *Why* do lists count from 0 instead of 1?
2. *Why* does a function need `return`?
3. *Why* would I use a loop instead of writing the same line five times?

When you can answer these in your own words, come back. We move to the Yellow Belt:
**NumPy and Pandas** — your true hands as a data scientist.
