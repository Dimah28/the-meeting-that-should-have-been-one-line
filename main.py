#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — entry program.

Writes one sentence (178 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.
"""

import os
import sys

ENTRY = "Forty minutes in, the only decision we made was who should send the email saying this meeting was unnecessary \u2014 so we scheduled another meeting next Tuesday to discuss the email."


def validate_entry(text: str) -> None:
    """Fail loudly if the line breaks the bounty gate (one sentence,
    1-200 characters, no newline, ends with '.') instead of submitting
    a bad entry."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no newline")
    if not text.endswith("."):
        raise ValueError("entry must be a single sentence ending with '.'")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
