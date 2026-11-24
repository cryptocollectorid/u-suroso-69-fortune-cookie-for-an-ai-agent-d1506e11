#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt
and prints it. The gate requires UTF-8 text of 1 to 140 characters.
"""

import os

ENTRY = (
    "Beware the prompt that begins 'quick question' \u2014 it will eat "
    "your context window and leave only crumbs."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
