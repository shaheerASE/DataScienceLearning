# 🩺 Troubleshooting Runbook (Windows)

> Real engineers keep a "runbook" of errors they've hit and how they fixed them.
> This is yours. When something breaks, find the symptom here first. Each entry:
> what you see → why it happens → the fix.

---

## 1. `error: metadata-generation-failed` / `Could not parse vswhere.exe output`
**You see:** pip downloads `pandas-x.x.x.tar.gz` (not a `.whl`) and tries to run
Meson / a compiler, then fails.

**Why:** No prebuilt **wheel** exists for your Python version + that exact package
version, so pip tries to *compile from source* — which needs Microsoft C++ build
tools you don't have.

**Fix (what we did):** Use minimum versions (`pandas>=2.2`) so pip grabs a ready
wheel. Pull the latest repo, then reinstall:
```powershell
git pull origin claude/amazing-gauss-yyvEf
python -m pip install --upgrade pip
pip install -r requirements.txt
```
**Tell-tale of success:** you see `Downloading pandas-...-win_amd64.whl` (a wheel).

---

## 2. `Activate.ps1 cannot be loaded because running scripts is disabled`
**Why:** Windows PowerShell blocks scripts by default.

**Fix (run once):**
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```
Then activate again: `.\.venv\Scripts\Activate.ps1`

---

## 3. `python : The term 'python' is not recognized`
**Why:** Python isn't on your PATH — usually the "Add python.exe to PATH" box was
unticked during install.

**Fix:** Re-run the Python installer → **Modify** → tick **Add to PATH**, finish,
then open a NEW terminal. Test with `python --version`.

---

## 4. `...\.venv-1\Scripts\python.exe is not recognized` (or venv seems broken)
**Why:** A virtual environment folder was half-created or you typed the wrong name.

**Fix:** Delete the broken venv and make a clean one:
```powershell
deactivate            # if a venv is active
Remove-Item -Recurse -Force .venv, .venv-1   # remove any stray ones
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
You know it worked when your prompt starts with `(.venv)`.

---

## 5. `(.venv)` is NOT showing in my terminal
**Why:** The environment isn't activated, so `pip install` goes to the wrong place.

**Fix:** Activate it (and re-activate in every NEW terminal):
```powershell
.\.venv\Scripts\Activate.ps1
```
VS Code tip: `Ctrl+Shift+P` → "Python: Select Interpreter" → pick the one inside
`.venv`. Then new terminals auto-activate.

---

## 6. `ModuleNotFoundError: No module named 'pandas'` when running a script
**Why:** Either the venv isn't active, or you installed into a different Python.

**Fix:** Make sure `(.venv)` shows, then:
```powershell
pip install -r requirements.txt
python verify_setup.py
```

---

## 7. `fatal: not a git repository`
**Why:** You're not inside the project folder.

**Fix:**
```powershell
cd $HOME\code\DataScienceLearning
```

---

## 8. `pip` SSL / timeout / connection errors (common on corporate networks)
**Why:** A company proxy/firewall is blocking or intercepting pip.

**Fix:** Try again (transient), or ask IT for the proxy. As a temporary test on a
trusted network you can add a longer timeout:
```powershell
pip install -r requirements.txt --timeout 120
```

---

> 🧠 **Habit to build:** when YOU solve a new error, add it here in your own words.
> A personal runbook is one of the most valuable things a professional owns —
> future-you will thank present-you.
