# 🛠️ Setup Guide — Windows (Day 1)

> Three tools. No more. **Python**, **Git**, **VS Code**.
> Follow in order. Do not skip. Each step builds on the last.

---

## Step 1 — Install Python 🐍

1. Go to **https://www.python.org/downloads/** and download the latest Python 3.x.
2. Run the installer. **⚠️ CRITICAL:** on the first screen, tick the box
   **"Add python.exe to PATH"** *before* clicking Install. (If you forget this,
   nothing will work later. This is the #1 beginner mistake.)
3. Verify — open **PowerShell** (press `Win`, type "PowerShell", Enter) and run:
   ```powershell
   python --version
   ```
   You should see something like `Python 3.12.x`.

---

## Step 2 — Install Git 📦

1. Go to **https://git-scm.com/download/win** — the download starts automatically.
2. Run the installer. Just click **Next** through all screens (defaults are fine).
3. Verify in PowerShell:
   ```powershell
   git --version
   ```

---

## Step 3 — Install VS Code 💻

1. Go to **https://code.visualstudio.com/** and download for Windows.
2. Install (defaults are fine — tick "Add to PATH" if asked).
3. Open VS Code. On the left sidebar, click the **Extensions** icon (four squares)
   and install just one for now:
   - **Python** (by Microsoft)
   That single extension brings everything you need to run and debug Python.

---

## Step 4 — Tell Git who you are (one time only)

In PowerShell, run these two lines with your own name and email:
```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## Step 5 — Clone YOUR dojo 🥋

1. Choose where to keep your code. A simple, clean home:
   ```powershell
   cd $HOME
   mkdir code
   cd code
   ```
2. Clone the repository:
   ```powershell
   git clone https://github.com/shaheerASE/DataScienceLearning.git
   cd DataScienceLearning
   ```
3. Switch to your training branch (this is where all our work lives):
   ```powershell
   git checkout claude/amazing-gauss-yyvEf
   ```

---

## Step 6 — Open it in VS Code

```powershell
code .
```
(The `.` means "this folder". VS Code opens your whole dojo.)

---

## Step 7 — Create a virtual environment (a clean room for this project)

> A *virtual environment* keeps this project's tools separate from the rest of
> your computer. Real teams do this for every project. It is a core DevOps habit.

In VS Code's terminal (menu: **Terminal → New Terminal**):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
You should now see `(.venv)` at the start of your terminal line. That means the
clean room is active.

> ⚠️ If Activate gives a "running scripts is disabled" error, run this once:
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```
> then try the activate line again.

---

## Step 8 — Install the project's tools

```powershell
pip install -r requirements.txt
```

---

## Step 9 — Run your first pipeline 🚀

```powershell
python projects\01_sales_pipeline\pipeline.py
```
(It will run with TODOs unfinished — your job is to fill them in. See
`projects/01_sales_pipeline/README.md`.)

---

## ✅ You are ready when...

- `python --version` and `git --version` both work
- VS Code opens the `DataScienceLearning` folder
- `(.venv)` shows in your terminal
- `pip install -r requirements.txt` finishes without errors

When all four are true — you have set up your dojo like a professional.
Return to the pipeline and begin the real training.

---

## 💾 Saving your work back (after you do the exercises)

```powershell
git add -A
git commit -m "My message describing what I did"
git push origin claude/amazing-gauss-yyvEf
```
