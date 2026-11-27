#!/usr/bin/env python3
"""One Line to Your Younger Self entry: writes one line to /output/entry.txt.

The line is addressed straight at a younger self, in one breath, with a
turn: the crease worth keeping is not the one from ironing a shirt for
people who will forget you, but the one earned standing up for the kid
nobody picks.
"""

import os

LINE = "Don't waste your best years ironing your shirt for people who won't remember your name — the only crease that counts is the one you get standing up for the kid nobody picks."

# The gate allows 1-200 characters of non-blank UTF-8 text; refuse to
# write anything outside it rather than submit an invalid entry.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line outside the 1-200 char gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
