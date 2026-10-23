# Changelog

All notable changes to this plugin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Fixed

- The e2e Ticket carries no documentation update: `to-spec` drafts none about the e2e scenarios,
  `to-tickets` never attaches one to it, and gate A item 4 of `REVIEW.md` checks it. The e2e
  role may write only the suite folder, so such a draft could never be satisfied in its ticket.

### Added

- End-to-end acceptance in the planning chain: `grill` settles up to 5 end-to-end scenarios
  (or a skip) when the Project uses the e2e check, `to-spec` carries them, `to-tickets`
  creates a last `e2e` Ticket blocked by all others, or leaves the `skip-test-e2e` opt-out
  to the user. `contracts/github.md` documents both labels and the refusal; gate A of
  `REVIEW.md` gains item 14.

## [0.3.0] - 2026-10-19

### Added

- `handoff` and `resume` skills, moved in from the `handoff` plugin of pinkpuma-toolbelt.
  `resume` now carries `disable-model-invocation`, like every skill here except
  `knowledge-search`.
- `grill`, `to-spec` and `to-tickets` skills and the `/tilap:plan` command, moved in from the
  `feature-planning` plugin of pinkpuma-toolbelt. Their shared rules, review gates and
  tracker contracts live in `feature-planning/`. None of them auto-invokes.

### Changed

- Commands are renamed: `/handoff:handoff` is `/tilap:handoff`, `/feature-planning:grill` is
  `/tilap:grill`, and so on for `resume`, `to-spec`, `to-tickets` and `plan`.

## [0.2.0] - 2026-10-19

### Added

- `knowledge-search` skill: reads the knowledge base before a design or implementation
  topic and applies the matching entries. Read-only, auto-invocable.
- `knowledge` skill: adds or updates one knowledge-base entry through the notes MCP,
  checks the index for duplicates first, and creates entries as drafts. It does not
  auto-invoke.

## [0.1.0] - 2026-10-19

### Added

- `explore` skill: on-demand options for one precise problem, including one option
  that leaves a current repo choice. It does not edit files and does not auto-invoke.
- `session-note` skill and the notes MCP client, moved in from the former
  `session-notes` plugin. The kind is stored as the first tag. It does not
  auto-invoke.
