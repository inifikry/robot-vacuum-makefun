#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line (max 140 characters) to /output/entry.txt: the funniest
excuse a robot vacuum gives for missing a spot. The line is a fixed,
deterministic string, so every run produces byte-identical output.
"""

import os

# The entry line: a robot vacuum that negotiated with the dust bunny.
LINE = "The dust bunny and I reached an agreement. It stays in the corner, I stay out of the corner."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-140 characters, UTF-8,
    # and not only whitespace. Fail loudly instead of writing bad output.
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"entry is {len(LINE)} characters, must be 1-140")
    if not LINE.strip():
        raise SystemExit("entry is only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
