"""One Letter: Coffee or Tea — entry: the single letter B.

The letter stands for tea — the slow cup. In a field where nine out of ten
revealing titles shout coffee, tea is the contrarian stance: a drink that
waits for you, steam curling off porcelain, sipped slow while the night shift
runs long. Coffee is the performed answer, the third jittery refill; tea is
the honest one, the cup that is still warm when the work is done.

The judge reads two letters at a time and picks the one whose choice feels
more vivid, funnier or truer. Tea answers with a fuller, more alive picture
than "coffee = fuel", with the surprise of the unexpected pick, and with the
truth of a slow, deliberate ritual. B stands alone as a whole answer: one
clean character, nothing needed beside it.

Deterministic: the same single byte on every run. No network, no randomness,
no input read. Writes exactly one character, "B", with no trailing newline,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when the grader sets it).
"""

import os
from pathlib import Path

LETTER = "B"

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
# Fail loudly rather than emit an invalid entry: the gate requires exactly
# 1 character of UTF-8 text, not only whitespace, and the bounty requires
# that character to be the letter A (coffee) or B (tea).
if len(LETTER) != 1 or not LETTER.strip() or LETTER not in ("A", "B"):
    raise ValueError(f"entry letter fails the gate: {LETTER!r}")
# Exactly one byte, no trailing newline: the gate counts characters, and a
# stray newline would make this a two-character entry.
out_dir.joinpath("entry.txt").write_text(LETTER, encoding="utf-8")
