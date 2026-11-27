#!/usr/bin/env python3
"""One Line to Your Younger Self entry: writes one line to /output/entry.txt."""

import os

LINE = "Don't waste your best years ironing your shirt for people who won't remember your name — the only crease that counts is the one you get standing up for the kid nobody picks."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
