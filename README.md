# Daily Brief

English | [简体中文](README.zh-CN.md)

Make a short working agenda from the tasks you already have. The helper separates blocked work and fits ready tasks into the minutes you have available.

[Download v0.2.1](https://github.com/KarmenLoop/skill-daily-brief/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-daily-brief/issues)

## What it does

The sample has 90 minutes available. The overdue 40-minute proposal enters the agenda; the invoice stays blocked and the 60-minute review is deferred.

This is a deterministic planning helper. It does not inspect your calendar, estimate tasks with AI, or execute the agenda.

![Daily Brief sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-daily-brief-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-daily-brief 0.2.1`. The sample has 90 minutes available. The overdue 40-minute proposal enters the agenda; the invoice stays blocked and the 60-minute review is deferred.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Choose the working date, available_minutes, and realistic task lengths. Priority 1 is highest; mark tasks ready, blocked, or done.

Compare a 30-minute day with a 120-minute day using the same tasks. Review what moves into deferred rather than silently treating every task as scheduled.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Will it send reminders?** No. Save the output or pass selected items to your own reminder tool after reviewing them.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
