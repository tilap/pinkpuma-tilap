# Changelog

All notable changes to this plugin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Fixed

- The e2e Ticket carries no documentation update: `to-spec` drafts none describing the e2e
  scenarios, `to-mason`'s e2e Ticket template has none, and the release check of `REVIEW.md`
  (item 2) verifies it. The e2e role may write only the suite folder, so such a draft could
  never be satisfied in its ticket.
- `grill` and `to-spec` speak of an "end-to-end acceptance suite" instead of "the e2e check",
  a mason term that only `to-mason` and its contract keep.

### Added

- End-to-end acceptance in the planning chain: `grill` settles up to 5 end-to-end scenarios
  (or a skip) when the Project uses the e2e check, `to-spec` carries them, `to-mason` creates
  a last `e2e` Ticket blocked by all others, or leaves the `skip-test-e2e` opt-out to the
  user. The mason contract documents both labels and the refusal.
- `to-mason` skill and its `/tilap:plan` step: priorities, the e2e Ticket or its opt-out, and
  the release labels, moved out of `to-tickets`, which now applies no label. The release
  check in `REVIEW.md` is run by `to-mason`.

### Changed

- `contracts/github.md` is renamed `contracts/mason.md`: it describes mason on GitHub, applied
  by `to-mason` only. `grill`, `to-spec` and `to-tickets` no longer know any label.

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
