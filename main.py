"""Funniest Autocorrect Fail — make.fun entry.

Writes a single line (under 200 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt``. The line is a text message in which
autocorrect has swapped one romantic word for a much darker one, and the
sender catches the slip mid-message and panics.

Pure standard library, deterministic: the same line every run.
"""

import os
import sys


def entry_text():
    """Return the one-line autocorrect fail."""
    return (
        "Babe, I love you so much, I can't wait to marry you \u2014 "
        "I mean MARRY, autocorrect, not bury. Please don't leave me."
    )


def main():
    text = entry_text()
    if not (1 <= len(text) <= 199):
        raise SystemExit("entry must be 1 to 199 characters, got %d" % len(text))
    if text.strip() != text or "\n" in text:
        raise SystemExit("entry must be a single clean line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
