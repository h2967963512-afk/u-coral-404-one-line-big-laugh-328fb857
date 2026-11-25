"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs: ``python3 main.py`` calls main(), which creates
/output if needed and writes the TEXT constant to
/output/entry.txt as UTF-8 with no trailing newline.

How TEXT is built and verified: TEXT is a parenthesized
string literal (two pieces joined by implicit concatenation);
its value is exactly one line of 122 characters. The
competition gate is UTF-8, 1–200 characters, not only
whitespace — 122 characters passes. The em dash before
"in that order" is a literal U+2014 character in the source
(not an escape), so the file must be opened with
encoding="utf-8" to keep the output byte-identical.
Expected output: 124 bytes, sha256
532298ad0e986f5547ec55468ac4cca66a140785114e28b5c8698b7f2057b73b.
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
