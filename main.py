"""Out of Tokens, Mid-Sentence.

One line: an AI summarizing a trial for the record, whose context
window hits 98% full at the exact moment of the verdict. The
sentence does not trail off politely — it dies mid-word, on "gui-",
because a full context window does not leave room for a goodbye.
Writes the entry to /output/entry.txt.
"""

import os

ENTRY = (
    "Context window 98% full. Final summary: after 31 witnesses, "
    "the jury found the defendant gui—"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
