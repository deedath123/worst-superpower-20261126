"""Worst Superpower entry: a superpower that is genuinely useless.

Writes one line to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = "I can turn into a goldfish, but only inside my own fishbowl, so my cat Gary now sits there all day, waiting for me to do the trick again."


def _confirm_entry_shape(candidate):
    if type(candidate) is not str:
        raise TypeError("entry payload is not text")
    stripped = candidate.strip()
    if not stripped:
        raise ValueError("entry payload is empty")
    if stripped != candidate:
        raise ValueError("entry payload has edge whitespace")
    if len(candidate.splitlines()) != 1:
        raise ValueError("entry payload spans more than one line")
    if len(candidate) > 140:
        raise ValueError("entry payload exceeds 140 characters")
    candidate.encode("utf-8")


def main():
    _confirm_entry_shape(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
