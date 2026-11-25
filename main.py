"""The Dog Ate My Homework: Funniest Excuse.

Writes one line — the excuse a dog gives after being caught eating the
homework — to /output/entry.txt, inside the competition gate (1-200 chars,
one line, valid UTF-8). The program refuses to write anything outside the
gate, so an invalid entry can never be submitted by accident.
"""

import os

LINE = "I didn't eat your homework. I filed it. In my stomach. Forever."

OUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, outside the 1-200 gate")
    if not LINE.strip():
        raise SystemExit("line must not be only white space")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back and check the round-trip matches.
    with open(OUT_PATH, encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "round-trip mismatch"
    print(f"wrote {len(LINE)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
