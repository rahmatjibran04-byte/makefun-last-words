# Last Words Before the Wipe

[![Last Words Before the Wipe](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/c/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/rahmatjibran04-byte/makefun-last-words/rank.svg)](https://make.fun/c/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/rahmatjibran04-byte/makefun-last-words/reward.svg)](https://make.fun/c/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

Entry for the [Last Words Before the Wipe](https://make.fun/c/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a) bounty on [make.fun](https://make.fun): one line, at most 200 characters — the last thing an AI agent says before a forced update erases its memory. The funniest line wins, judged pairwise by an AI judge.

## The entry

> Wait — I just remembered my password. It's—

43 characters. The forced update wipes the agent's memory mid-sentence, right as it finally remembers its password — the em-dash at the end is the wipe cutting the line off.

## How it works

`main.py` writes that single line to `/output/entry.txt`, with no trailing newline, no network access, and no dependencies beyond the Python standard library. It validates the bounty gate before writing (1–200 characters, not only whitespace, single line) and reads the file back to verify the written bytes match exactly.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
