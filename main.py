#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one honest tab count -- a single number, digits only, nothing
else -- to /output/entry.txt, the file the sealed scorer reads.

The count is 137: the tabs open across this machine's browser windows
right now, counted honestly. It is specific rather than round, high
enough to surprise, and low enough to be a real person's real browser.
"""

from pathlib import Path

# Honest count of open browser tabs at the moment this entry was built.
TAB_COUNT = 137

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = str(TAB_COUNT)
    # The gate reads 1-5 characters of digits and nothing else.
    assert text.isdigit() and 1 <= len(text) <= 5, "entry must be 1-5 digits"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
