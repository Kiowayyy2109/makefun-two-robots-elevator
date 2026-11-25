#!/usr/bin/env python3
"""Two Robots in an Elevator — one awkward line of robot small talk."""
import os

LINE = "I updated my firmware this morning and it still didn't include a module for what to do with my arms in here."
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
