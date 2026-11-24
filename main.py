"""One Emoji, One Dream Vacation — entry writer.

Writes exactly one emoji, a tropical hut (an overwater bungalow
on a quiet lagoon), to the absolute output path /output/entry.txt.
Stdlib only: no network, no images, no extra text.
"""

import os

ENTRY = "\U0001f6d6"  # HUT: a tropical hut — one dream-vacation postcard
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
