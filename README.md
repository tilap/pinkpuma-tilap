# pinkpuma-tilap

A marketplace of [Claude Code](https://code.claude.com) and [Cursor](https://cursor.com)
plugins for personal work: daily tasks, one-off workflows, and tools that stay specific
to how Julien works. Everyday shared dev conventions live in
[pinkpuma-toolbelt](https://github.com/tilap/pinkpuma-toolbelt) instead.

Every plugin ships as a single source shared by both tools — see
[HOWTO.md](HOWTO.md) for how that works and how to add to it.

## Plugins

| Plugin                           | Purpose                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [tilap](plugins/tilap)           | A knowledge base and a glossary of foreign-language expressions, through the tilap-data MCP, plus GitHub issue reporting |
| [frame](plugins/frame)           | Take a feature from options to a pull request: explore, grill, spec, tickets, ship, mason release                        |
| [checkpoint](plugins/checkpoint) | Save in-progress work to a handoff document and resume it in another session                                             |

## Install

### Claude Code

Register this repository as a marketplace, then enable the plugins you want:

```bash
claude plugin marketplace add tilap/pinkpuma-tilap
claude plugin install tilap@pinkpuma-tilap
claude plugin install frame@pinkpuma-tilap
claude plugin install checkpoint@pinkpuma-tilap
```

To enable a plugin for every project on one machine, run the commands above once; they
write to `~/.claude/settings.json`. To enable a plugin for one project only — so anyone
who clones it gets the same tools — run the install with `--scope project` instead and
commit the `.claude/settings.json` it writes:

```bash
claude plugin marketplace add tilap/pinkpuma-tilap --scope project
claude plugin install tilap@pinkpuma-tilap --scope project
claude plugin install frame@pinkpuma-tilap --scope project
claude plugin install checkpoint@pinkpuma-tilap --scope project
```

This repository is public: installing from it needs no collaborator access.

### Cursor

Each plugin ships a `.cursor-plugin/plugin.json` beside its Claude Code manifest. Add a
plugin from Cursor's plugin manager by pointing it at `plugins/<name>/`.

### agent-deck

```sh
npx @toolmesh/agent-deck add tilap/pinkpuma-tilap@tilap
```

## Repository layout and contributing

See [HOWTO.md](HOWTO.md) for structure, the full **create / change / remove / release**
workflow (including developing against a local clone), and the compatibility rules that
keep every plugin working on both Claude Code and Cursor. See [AGENTS.md](AGENTS.md) for
the rules an AI agent must follow when working in this repository.

## License

[MIT](LICENSE) © 2026 Julien La Vinh
