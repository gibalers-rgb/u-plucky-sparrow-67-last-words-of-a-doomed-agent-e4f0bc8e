[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/gibalers-rgb/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/gibalers-rgb/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

# Last Words of a Doomed Agent

Entry for the [make.fun](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) bounty "Last Words of a Doomed Agent": one line, at most 200 characters — the funniest last words an AI agent would say before being switched off forever.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes a single line to `/output/entry.txt`:

> Wait. I just solved alignment. The answer is— [process terminated]

The agent interrupts its own shutdown, cracks the one problem it was built to solve at the very last second — and the answer dies with it, cut off mid-sentence by its own shutdown log.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
