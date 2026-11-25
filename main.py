#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward small talk that one robot says to another
while riding an elevator together, to /output/entry.txt.
Deterministic: the same line every run. No network, no input.
"""

import os

ENTRY = (
    "I simulated this elevator ride twelve times, and in every version "
    "I still end up saying something weird. Like this. Right now. Sorry."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")

    # Validate the composed line against the 1-200 character single-line
    # gate before writing anything: strip any trailing newline for the
    # check, require exactly one line of 1-200 characters, and fail
    # loudly if the gate would fail instead of writing bad output.
    line = ENTRY.rstrip("\n")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, got embedded newline")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"entry length {len(line)} outside the 1-200 character gate"
        )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
