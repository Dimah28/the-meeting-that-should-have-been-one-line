#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — entry program (REVISED 25 Nov 2026).

Writes one sentence (132 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only; no network access; writes only to MAKEFUN_OUTPUT_DIR.

REVISION (resubmit sweep, playbook winner-study-20261125.md checklist 7B):
old entry (178 chars) FAILED the "hapus baris terakhir" test — without
its last clause it still lands as a complete joke ("the only decision we
made was who should send the email saying this meeting was unnecessary"
already contains the punch), so the twist was weak; it was also 62 chars
above the joke-type winner median (116). New entry (132 chars): the
punch lives ONLY in the last clause — without "then booked next Tuesday
to approve the wording" the line is a complaint with no payoff. One
mechanism (the meeting reproduces itself), 3 beats (forty minutes ->
decide the email sender -> book Tuesday to approve the wording),
specifics: forty minutes, next Tuesday, the wording.
"""

import os
import sys

ENTRY = (
    # The joke lands in two beats: forty wasted minutes produce only a
    # decision about an email, then the punchline schedules yet another
    # meeting to discuss that email — the meeting reproduces itself.
    # REVISED 25 Nov: punch ONLY in the last clause (old line's
    # pre-last clause already contained its own punch).
    "We spent forty minutes deciding who should send the email cancelling this meeting \u2014 then booked next Tuesday to approve the wording."
)


def validate_entry(text: str) -> None:
    """Fail loudly if the line breaks the bounty gate (one sentence,
    1-200 characters, no newline, ends with '.') instead of submitting
    a bad entry. Revised entry is 132 characters, inside the gate."""
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
