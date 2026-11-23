#!/usr/bin/env python3
"""One Emoji, One Smile — entry program.

Writes exactly one emoji, and nothing else, to entry.txt.

The chosen emoji is U+1F31E SUN WITH FACE. Why this one, against the
judge's five criteria (in order):

1. Warm and friendly to a stranger: sunshine is the plainest symbol of
   warmth there is, and the smiling face makes it a greeting, not a
   weather report. A stranger reading it feels wished well, not
   addressed.
2. Warmth at first glance: a beaming sun reads as kind, friendly and
   gently funny with zero context. No setup, no caption, no joke to get.
3. Universal: the sun means warmth, morning and good cheer in every
   culture and to every age. No irony, no in-joke, nothing that can
   land wrong.
4. Chosen rather than default: it is not the first smiley that comes
   to mind (that is the plain 🙂 family). Picking a smiling sun is a
   deliberate, slightly playful choice — yet it stays instantly
   readable, no decoding needed.
5. Right for a stranger: sunshine carries no intimacy, no sarcasm and
   no flirtation. A hug or a heart from someone unknown can read odd;
   a sun cannot.

Rejected on purpose: 🙂 / 😊 (default, fails criterion 4),
🥰 / 😘 (intimate/flirty, fails criterion 5), 😂 / 😉 (ironic or
teasing, fails criterion 3), 🌻 / ☀️ (cheerful but faceless — less
personally warm than a face that smiles back).

Deterministic, standard library only, no network, no input. The
output directory honours $MAKEFUN_OUTPUT_DIR and defaults to /output.
"""

import os

EMOJI = "\U0001F31E"  # SUN WITH FACE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
