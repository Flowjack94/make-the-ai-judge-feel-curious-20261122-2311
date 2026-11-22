"""Make the AI judge feel curious — entry program.

Writes one short text to /output/entry.txt: a text written to intrigue
the AI judge reading it. Standard library only, no network, no input,
fully deterministic — every run writes the same bytes.

The text: a small, quiet mystery. A baker keeps setting out a second
loaf for a visitor who never comes; one morning the loaf is gone and
something else is there instead. Nothing is explained, nothing is
ordered — the question is left open, and the image (one white feather)
is the thing that lingers. Written against the judge's brief: intrigue
first (the open question keeps the reader asking), calm shown by the
scene itself rather than instructed, plain concrete words, and a fresh
image instead of a stock phrase.
"""

import hashlib
import os
import sys

TEXT = (
    "Every morning the baker sets out a second loaf on the step, "
    "though no one has knocked in years. This morning the loaf was "
    "gone, and in its place lay a single white feather."
)

# The sealed scorer runs the program with no environment, so the
# default is the path the rules name. MAKEFUN_OUTPUT only lets a
# developer run the same check locally against another path.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> int:
    chars = len(TEXT)
    if not 1 <= chars <= 280:
        print(f"entry is {chars} characters, must be 1-280", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    data = TEXT.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Verify the written bytes by reading them back.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("read-back mismatch", file=sys.stderr)
        return 1
    decoded = written.decode("utf-8")
    if len(decoded) != chars or not decoded.strip():
        print("read-back failed the gate", file=sys.stderr)
        return 1

    digest = hashlib.sha256(written).hexdigest()
    print(f"wrote {OUTPUT_PATH}: {chars} characters, sha256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
