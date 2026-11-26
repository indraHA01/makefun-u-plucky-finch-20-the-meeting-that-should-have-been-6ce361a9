"""The Meeting That Should Have Been an Email.

make.fun entry for competition
u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.

The program writes exactly one line — one joke about a meeting that
should have been an email — to /output/entry.txt. The line is at most
200 characters, a single line, plain UTF-8 text.

Run:  python3 main.py
"""

from __future__ import annotations

import os
import sys

# The entry: one line, at most 200 characters, one joke about a meeting
# that should have been an email. Final: the recursion twist — the meeting
# doesn't just waste an hour, it breeds a follow-up to confirm the waste.
ENTRY = "We spent an hour agreeing this meeting should have been an email, then booked a follow-up to confirm it."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not line.strip():
        raise ValueError("entry is blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")


def main() -> int:
    validate(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
