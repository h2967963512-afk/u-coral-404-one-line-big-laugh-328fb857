"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line, 122 characters, inside the 200-character
# gate. Setup is mundane (asking a GPS for the fastest route home);
# the turn is the escalating list of places — ex's house, gym,
# childhood trauma — and the punch lands in the last three words,
# "in that order", which reframes a routing bug as deliberate cruelty.
# Revision note: entry kept as written — one line, 122 characters,
# two short sentences; the joke is the escalating list plus the
# implied intent of the final phrase.

import os

TEXT = (
    "I asked my GPS for the fastest route home. It took me past my "
    "ex's house, my gym, and my childhood trauma — in that order."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
