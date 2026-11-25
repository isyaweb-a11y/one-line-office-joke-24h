"""One-Line Office Joke: 24-Hour Sprint -- revised entrypoint.

A single-line joke about office life, written to /output/entry.txt.

The joke is built from two observations that stack: the standup has
grown a pre-standup to prepare it, and the standup's only agenda item
is scheduling the post-standup. The punchline is the agenda itself --
yet another meeting -- which anyone whose calendar is full of syncs
will recognise instantly.
"""

import os

OBSERVATION = "Our standup now has a pre-standup to prepare the standup,"
PUNCHLINE = "and the standup's only agenda item is scheduling the post-standup."

MAX_CHARS = 200
MIN_CHARS = 1


def compose(first: str, second: str) -> str:
    """Stitch the observation and the punchline into a single line."""
    fragments = [first.strip(), second.strip()]
    return " ".join(fragments)


def check_joke(line: str) -> str:
    """Gate the joke the way the sealed judge does: 1..200 chars, one line."""
    assert MIN_CHARS <= len(line) <= MAX_CHARS, f"line is {len(line)} chars"
    assert line == line.strip(), "no stray whitespace around the line"
    assert "\n" not in line, "the joke must stay on one line"
    assert line.endswith("."), "the joke should end on the punchline"
    return line


def joke_structure(line: str) -> dict:
    """Per-bounty structure check: the joke needs setup, escalation, payoff.

    Setup names the standup, the escalation adds the pre-standup, and the
    payoff is the agenda item itself -- scheduling the post-standup. All
    three beats must be present, in order, for the joke to land.
    """
    words = line.split()
    assert 10 <= len(words) <= 40, f"line has {len(words)} words"
    assert line.count("standup") >= 3, "the joke must repeat 'standup' to escalate"
    assert "pre-standup" in line, "the escalation beat is missing"
    assert "post-standup" in line, "the payoff beat is missing"
    assert line.index("pre-standup") < line.index("post-standup")
    return {"words": len(words), "chars": len(line), "beats": 3}


def main() -> None:
    line = check_joke(compose(OBSERVATION, PUNCHLINE))
    structure = joke_structure(line)
    assert structure["beats"] == 3
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
