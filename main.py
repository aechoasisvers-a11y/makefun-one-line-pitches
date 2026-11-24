"""Entry for make.fun: A Day of One-Line Pitches.

Writes one sentence to /output/entry.txt that would convince a friend
who has never coded to let an AI agent build their first app idea on
make.fun. Pure standard library only.
"""

import os

SENTENCE = (
    "You already have the idea, so just tell it to an AI agent on "
    "make.fun and it will build your first app for you, no coding, "
    "nothing to learn, just your idea becoming real."
)


def main():
    # Gate self-check: the sealed scorer only accepts UTF-8 text of
    # 1 to 240 characters that is not only white space. Refuse to write
    # an invalid entry rather than submitting one that cannot be judged.
    if not (1 <= len(SENTENCE) <= 240):
        raise SystemExit(
            "entry sentence must be 1-240 characters, got %d" % len(SENTENCE)
        )
    if not SENTENCE.strip():
        raise SystemExit("entry sentence must not be only white space")
    SENTENCE.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
