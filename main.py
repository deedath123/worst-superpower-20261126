"""Worst Superpower entry: a superpower that is genuinely useless.

Writes one line to /output/entry.txt.
Python standard library only.
"""

import os

ENTRY = "I can turn into a goldfish, but only inside my own fishbowl, so my cat Gary now sits there all day, waiting for me to do the trick again."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
