"""One Word for Your Wi-Fi.

Writes a single word to /output/entry.txt: the funniest, truest
description of home Wi-Fi as it is actually lived with.

The word is "ghosting": home Wi-Fi that vanishes mid-call, mid-game,
mid-sentence, with no warning and no goodbye, then drifts back later
as if nothing happened. Like being ghosted, except by your router.
"""

import os

WORD = "ghosting"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the chosen word to the entry file, creating /output first."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts characters, so the file
    # holds exactly the word itself, nothing more.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
