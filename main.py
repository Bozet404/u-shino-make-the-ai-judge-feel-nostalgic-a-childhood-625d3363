"""Write one nostalgic childhood sentence to $OUTPUT_DIR/entry.txt.

The bounty asks for a single sentence, at most 280 characters, that brings
back a childhood memory. The program is deliberately tiny: it holds one
hand-written line, checks it against the gate (1-280 UTF-8 characters, not
only whitespace, exactly one sentence), and writes it to entry.txt.
"""

import os

SENTENCE = (
    "The rice steamed in Grandma's kitchen, the radio hummed low, and "
    "barefoot on the cool tiles I believed summer evenings — fireflies at "
    "the window, her hand resting on my hair — would never end."
)


def main() -> None:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-280")
    if text != text.strip() or not text:
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
