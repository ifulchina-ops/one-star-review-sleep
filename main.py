#!/usr/bin/env python3
"""One-star review of sleep, for make.fun's "One-Star Review of Something
Essential" bounty.

The program writes a single deadpan one-star review, at most 160
characters, of an everyday essential to /output/entry.txt. The review is
fixed text: the joke is the grievance itself, filed in earnest against a
thing that cannot be fixed, with the sting landing in the last few words.
"""

import os

REVIEW = (
    "One star. Sleep takes eight hours a night, every night, and still "
    "returns me to work tired, like a subscription I never signed up "
    "for and cannot cancel."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> None:
    text = REVIEW.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("review must be 1 to 160 characters")
    if "!" in text:
        raise SystemExit("a deadpan review does not shout")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
