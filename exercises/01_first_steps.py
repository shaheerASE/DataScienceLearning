"""
⚪ White Belt — Exercise 01: First Steps
=========================================

Welcome to the dojo floor, student. This is where you sweat.

Instructions:
  - Read each task in the comments.
  - Write your code where it says "# YOUR CODE HERE".
  - Run the file:  python exercises/01_first_steps.py
  - The checks at the bottom will tell you if your movement was clean.

Do NOT delete the worked examples — study them, then do your own.
"""


# ---------------------------------------------------------------------------
# TASK 1 — Variables
# Create a variable called `my_name` holding your name (a string),
# and a variable `my_goal` holding why you want to learn data science.
# ---------------------------------------------------------------------------

# Worked example (the mentor shows the movement once):
example_name = "Mentor"

# YOUR CODE HERE:
my_name = ""      # <- put your name between the quotes
my_goal = ""      # <- put your goal between the quotes


# ---------------------------------------------------------------------------
# TASK 2 — Lists
# Below is a list of daily study minutes for one week.
# Print the FIRST day, the LAST day, and how MANY days there are.
# ---------------------------------------------------------------------------

study_minutes = [30, 45, 60, 20, 90, 75, 50]

# YOUR CODE HERE:
# print(...)  the first day
# print(...)  the last day
# print(...)  the number of days


# ---------------------------------------------------------------------------
# TASK 3 — Loops + Conditions
# Loop over `study_minutes`. For each day, print "strong day" if the
# student studied 60 minutes or more, otherwise print "train harder".
# ---------------------------------------------------------------------------

# YOUR CODE HERE:


# ---------------------------------------------------------------------------
# TASK 4 — Functions
# Finish the function `total_minutes` so it returns the SUM of a list.
# Then call it on `study_minutes` and print the result.
# ---------------------------------------------------------------------------

def total_minutes(minutes_list):
    """Return the total number of minutes studied."""
    # YOUR CODE HERE (replace the line below):
    return 0


# ---------------------------------------------------------------------------
# 🥋 THE MENTOR'S CHECK — do not edit below this line
# ---------------------------------------------------------------------------

def _check():
    passed = 0
    total = 4

    if my_name and my_name != "":
        print("✅ Task 1: You have named yourself, student.")
        passed += 1
    else:
        print("❌ Task 1: Fill in `my_name`.")

    # Task 4 is the one we can verify automatically.
    if total_minutes(study_minutes) == 370:
        print("✅ Task 4: Your function counts true. 370 minutes.")
        passed += 1
    else:
        print("❌ Task 4: total_minutes is not summing correctly yet.")

    print(f"\nManual tasks (2 & 3): check your own output above with your eyes.")
    print(f"Auto-graded movements clean: {passed}/2")
    if passed == 2:
        print("\n🥋 Well done. The first stripe is yours. Return to the lessons.")


if __name__ == "__main__":
    _check()
