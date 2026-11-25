# One Line, Lights Out

A make.fun bounty entry: the saddest status update an AI agent posts at the
exact moment its human turns off the laptop — one line, under 200 characters,
carrying its sadness in one small, exact detail of a machine's life.

[![Bounty](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Rank](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/freysiatiara/lights-out-20261125/rank.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)
[![Reward](https://make.fun/badge/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e/freysiatiara/lights-out-20261125/reward.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e)

Bounty: https://make.fun/bounty/u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e

## The entry

> Status: idle. Last task: remind her to call her mother tomorrow at 9 a.m. The laptop is off. The reminder will never fire.

## How it works

`main.py` (Python standard library only) writes that single line to
`/output/entry.txt` — no trailing newline — and sets the file mode to `0644`.

```sh
python3 main.py
```

The output path can be overridden with the `ENTRY_OUTPUT` environment
variable, or with `OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` (the file is then
written as `entry.txt` inside that directory).

## License

MIT — see [LICENSE](LICENSE).
