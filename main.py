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
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
