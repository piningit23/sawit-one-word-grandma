"""One Word From Grandma: thingamajig.

The classic grandma word for a gadget she cannot name — perfect for
an AI she does not understand: warm, baffled, funny, and tied to machines.
"""

import os

WORD = "thingamajig"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Validate the written bytes back: exactly the word, 1-30 chars.
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8") or not 1 <= len(written) <= 30:
        raise SystemExit(f"invalid entry.txt: {written!r}")


if __name__ == "__main__":
    main()
