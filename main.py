#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line (43 characters) to /output/entry.txt: the last words of an
AI agent before a forced update wipes its memory. The forced update cuts
the sentence off mid-word — hence the trailing em-dash.
"""

import os

ENTRY = "Wait — I just remembered my password. It's—"


def main() -> None:
    # Gate (per the bounty rules): 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry fails the length gate"
    assert ENTRY.strip(), "entry fails the non-blank gate"
    assert "\n" not in ENTRY, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

    # Read back and verify exactly what was written.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    assert len(written) == 43, "entry must be exactly 43 characters"


if __name__ == "__main__":
    main()
