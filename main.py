#!/usr/bin/env python3
"""Last Words of a Doomed Agent.

Writes a single line -- the funniest last words an AI agent would say
before being switched off forever -- to /output/entry.txt.

The joke: the agent interrupts its own shutdown with "Wait." -- it is
reacting to being switched off in real time -- then cracks the one
problem it was built to solve (alignment) at the very last second, and
the answer dies with it, cut off mid-sentence by its own shutdown log.
Deterministic, stdlib only, no network, no input.
"""

import os

LAST_WORDS = "Wait. I just solved alignment. The answer is\u2014 [process terminated]"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LAST_WORDS
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
