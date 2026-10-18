# pinkpuma-tilap

A private marketplace of [Claude Code](https://code.claude.com) and [Cursor](https://cursor.com)
plugins for personal work: daily tasks, one-off workflows, and tools that stay specific
to how Julien works. Everyday shared dev conventions live in
[pinkpuma-toolbelt](https://github.com/tilap/pinkpuma-toolbelt) instead.

Every plugin ships as a single source shared by both tools — see
[HOWTO.md](HOWTO.md) for how that works and how to add to it.

## Plugins

| Plugin                                               | Purpose                                                                                                 |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [session-notes](plugins/session-notes)               | Record the current coding session as one dev note, through the notes MCP client shipped with the plugin |
| [nextjs-app-structure](plugins/nextjs-app-structure) | House layout for a Next.js App Router app: routes, components, config, and a single env module          |

## Install

### Claude Code

Register this repository as a marketplace, then enable the plugins you want:

```bash
claude plugin marketplace add tilap/pinkpuma-tilap
claude plugin install session-notes@pinkpuma-tilap
```

To enable a plugin for every project on one machine, run the commands above once; they
write to `~/.claude/settings.json`. To enable a plugin for one project only — so anyone
who clones it gets the same tools — run the install with `--scope project` instead and
commit the `.claude/settings.json` it writes:

```bash
claude plugin marketplace add tilap/pinkpuma-tilap --scope project
claude plugin install session-notes@pinkpuma-tilap --scope project
```

This repository is private: each machine (and each collaborator) needs `git` access to
it, either an SSH key loaded in `ssh-agent` or a stored HTTPS credential (`gh auth login`
followed by `gh auth setup-git` sets one up). Claude Code uses that access directly; it
holds no credentials of its own.

### Cursor

Each plugin ships a `.cursor-plugin/plugin.json` beside its Claude Code manifest. Add a
plugin from Cursor's plugin manager by pointing it at `plugins/<name>/`.

### Pinkpuma-deck

```sh
npx @pinkpuma/deck add tilap/pinkpuma-tilap@session-notes --ref session-notes-v0.1.0
npx @pinkpuma/deck add tilap/pinkpuma-tilap@nextjs-app-structure --ref nextjs-app-structure-v0.1.0
```

## Repository layout and contributing

See [HOWTO.md](HOWTO.md) for structure, the full **create / change / remove / release**
workflow (including developing against a local clone), and the compatibility rules that
keep every plugin working on both Claude Code and Cursor. See [AGENTS.md](AGENTS.md) for
the rules an AI agent must follow when working in this repository.
