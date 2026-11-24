"""One-Line Office Joke: 24-Hour Sprint.

Writes a single-line joke about office life to /output/entry.txt.

The joke: meetings have multiplied so far that the standup itself needs
a warm-up meeting and a debrief meeting. The punchline is the agenda item
itself -- scheduling yet another meeting -- which anyone who has sat
through a calendar full of syncs will recognise instantly.
"""

import os

ENTRY = (
    "Our standup now has a pre-standup to prepare the standup, "
    "and the standup's only agenda item is scheduling the post-standup."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """The sealed gate wants UTF-8 text of 1..200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main() -> None:
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
