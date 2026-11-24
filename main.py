#!/usr/bin/env python3
"""Writes the funniest toaster error message to /output/entry.txt.

The entry is a single deadpan error line: the toast has unionised and
refuses to pop up. No trailing newline: the gate counts every character,
and the line must stay within the 120-character limit.
"""

import os

ENTRY = "ERROR E-07: Toast has unionised and refuses to pop up. Negotiations ongoing."
MAX_CHARS = 120

def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} characters, limit is {MAX_CHARS}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
