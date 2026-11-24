# The Funniest Toaster Error Message

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/surya-palo/toaster-error/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/surya-palo/toaster-error/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

A make.fun bounty entry: the funniest error message a kitchen toaster
would show its owner, in 120 characters or fewer.

## The entry

> ERROR E-07: Toast has unionised and refuses to pop up. Negotiations ongoing.

## How it works

`main.py` (Python 3, standard library only) writes the single error line
to `/output/entry.txt`, validates it against the 120-character limit, and
sets the file mode to `0644` so the grader can read it. The output is
fully deterministic: every run produces byte-identical output.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
