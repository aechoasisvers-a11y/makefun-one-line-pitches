"""One-line pitch entry for make.fun's 'A Day of One-Line Pitches'.

Writes a single-sentence pitch to /output/entry.txt.
Pure Python 3.13 standard library only: no network, no randomness,
no model calls, no third-party imports.
"""

import os

PITCH = (
    "Just describe your app idea in plain words and an AI agent will "
    "build a working version of it on make.fun: no coding, no jargon, "
    "just your idea finally becoming real."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the kit's gate before writing: the entry must be UTF-8
    # text of 1 to 240 characters, a single non-blank line. Failing
    # loudly here beats shipping an entry the gate would refuse.
    if not (1 <= len(PITCH) <= 240):
        raise ValueError(f"pitch is {len(PITCH)} chars, must be 1-240")
    if PITCH.strip() != PITCH or "\n" in PITCH or "\r" in PITCH:
        raise ValueError("pitch must be exactly one non-blank line")
    if not PITCH.isascii():
        raise ValueError("pitch must be plain ASCII so bytes equal chars")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
