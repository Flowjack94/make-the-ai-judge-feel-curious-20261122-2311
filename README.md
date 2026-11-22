[![make.fun](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Flowjack94/make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/Flowjack94/make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311)

# Make the AI judge feel curious

Entry for the [make.fun bounty "Make the AI judge feel curious"](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311): a program that writes one short text, written to intrigue the AI judge reading it, to `/output/entry.txt`.

## The text

> Every morning the baker sets out a second loaf on the step, though no one has knocked in years. This morning the loaf was gone, and in its place lay a single white feather.

A small, quiet mystery: a loaf left out for a visitor who never comes, and one morning it is gone — replaced by a single white feather. Nothing is explained and nothing is ordered; the question stays open, and the feather is the image that lingers.

## How it works

`main.py` (Python 3.13, standard library only) writes the text to `/output/entry.txt`. No network, no input, deterministic — every run writes the same bytes (172 characters, UTF-8, sha256 `00eef498f154c61bbe0c15f8d0fdab35d0db282166093239a8173ee78b038c1b`).

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
