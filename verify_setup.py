"""
🥋 verify_setup.py — Your first hands-on win
=============================================

Run this RIGHT AFTER you install Python and the requirements. It checks your
environment and gives you instant feedback. When you see all green checks,
you have earned your first PROGRESS.md box — the dojo is ready.

    python verify_setup.py
"""

import sys


def check(label, condition, fix=""):
    mark = "✅" if condition else "❌"
    print(f"  {mark} {label}")
    if not condition and fix:
        print(f"       fix: {fix}")
    return condition


def main():
    print("=" * 55)
    print("🥋  CHECKING YOUR DOJO SETUP")
    print("=" * 55)

    ok = True

    # 1. Python version
    v = sys.version_info
    py_ok = v.major == 3 and v.minor >= 9
    ok &= check(
        f"Python {v.major}.{v.minor}.{v.micro} (need 3.9+)",
        py_ok,
        "Install a newer Python from python.org and tick 'Add to PATH'.",
    )

    # 2. Core libraries
    for lib in ["pandas", "numpy", "matplotlib", "sklearn", "scipy", "joblib"]:
        try:
            __import__(lib)
            present = True
        except ImportError:
            present = False
        ok &= check(
            f"library: {lib}",
            present,
            "Run:  pip install -r requirements.txt",
        )

    # 3. sqlite3 (ships with Python — should always be present)
    try:
        import sqlite3  # noqa: F401
        sqlite_ok = True
    except ImportError:
        sqlite_ok = False
    ok &= check("library: sqlite3 (built-in)", sqlite_ok)

    # 4. A tiny real computation — prove the stack actually WORKS, not just imports
    try:
        import pandas as pd
        df = pd.DataFrame({"x": [1, 2, 3, 4]})
        smoke_ok = int(df["x"].sum()) == 10
    except Exception:
        smoke_ok = False
    ok &= check("smoke test: pandas can do math", smoke_ok)

    print("=" * 55)
    if ok:
        print("🎉  ALL GREEN. Your dojo is ready, student.")
        print("    Go tick the 'Setup' boxes in PROGRESS.md — your first win.")
        print("    Then open projects/02_churn_prediction/README.md and run it.")
    else:
        print("⚠️   Some checks failed. Fix the ❌ items above, then run me again.")
        sys.exit(1)
    print("=" * 55)


if __name__ == "__main__":
    main()
