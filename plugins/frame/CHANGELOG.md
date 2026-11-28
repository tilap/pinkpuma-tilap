# Changelog

All notable changes to this plugin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.4.0] - 2026-11-28

### Added

- `ship` skill (`/frame:ship <issue>`): takes a GitHub issue that holds the grill's final record to an
  open pull request without confirmation. It drafts the tickets, has a fresh agent review the plan,
  publishes them as sub-issues, builds them, and resumes from GitHub when run again.
- `implement` skill (`/frame:implement`), moved from `tilap:implement-github-issue`. A fresh agent
  reviews the assembled feature (gate C) before the pull request, a failing feature test is fixed in the
  application, and the plugin's own comments are marked and never read as specification.

- Run report: `ship` and `implement` post on the issue the time and tokens of the run by step and
  agent, and its notable difficulties, in a fixed format (`feature-planning/METRICS.md`).
  Token counts come from `scripts/tokens.py`, which reads Claude Code's session journals.

### Changed

- `grill` ends with a final record that stands on its own, under fixed headings, and proposes no next
  step.
- The feature-test ticket template is shared in `feature-planning/feature-test-ticket.md`.

### Removed

- `/frame:chain`: `/frame:ship` replaces it.

## [0.3.0] - 2026-11-26

### Added

- MIT license and plugin icon.
- `/frame:chain <instructions>`: after `grill`, runs `to-spec`, `to-tickets` and `to-mason` without stopping. It makes the choices itself (the run's instructions, then the project's docs and decisions, then built-in defaults), approves the publications for that run, and releases only when told to. `grill` and `plan` are unchanged.

### Changed

- `to-tickets`, the conventions and the README hand GitHub tickets built in an agent session over to
  `/tilap:implement-github-issue`.

### Fixed

- The tracker contract no longer says a ticket's tests may be written before its code.

## [0.2.1] - 2026-11-02

### Changed

- Tickets no longer promise tests "written first by another agent": the system's producer writes code and tests together.

### Added

- Gate A items 14-16: shared state is sequenced by blockers, shared rules (identity, keys) are set once and consistent, prerequisites exist on the base branch.
- Mason release check items 4-5: the base branch is ready, and the mason settings (parallelism, install step) fit the plan.
- Mason contract known limits: feature branch cut once, workspaces installed once, parallel tickets and shared files, shared cache race.

## [0.2.0] - 2026-10-27

### Changed

- The end-to-end acceptance suite per feature is replaced by **feature tests**, following
  bluewombat: the spec's acceptance scenarios `S*` are what the last ticket proves, once, on the
  assembled feature, with plain tests at the level each scenario names. `grill` no longer asks
  whether the project has an e2e suite, caps nothing at 5 scenarios and settles instead which
  scenarios cannot be proved from outside, or a skip. `to-spec` drops its end-to-end section for a
  one-line feature-tests decision. `to-mason` reads `mason.config.yaml` to know whether the
  project declares the check, then creates a `feature-test` Ticket or leaves the
  `skip-feature-test` opt-out. The mason contract and the release check follow.
- `grill` (level 8), `to-spec` and the plan review (item 9) take in every cross-cutting
  standard the project's documentation names (accessibility, design, a security policy, a
  global journey suite): what it requires of the need in observable terms and where it is
  checked. A standard the docs do not hold is not invented.

## [0.1.0] - 2026-10-23

### Added

- `explore`, `grill`, `to-spec`, `to-tickets`, `to-mason`, and the `/frame:plan` command,
  moved from the `tilap` plugin. Shared rules, review gates, and tracker contracts stay in
  `feature-planning/`. Commands are `/frame:explore`, `/frame:grill`, `/frame:to-spec`,
  `/frame:to-tickets`, `/frame:to-mason`, and `/frame:plan`.
- End-to-end acceptance in the planning chain: `grill` settles up to 5 end-to-end scenarios
  (or a skip) when the project uses the e2e check, `to-spec` carries them, `to-mason` creates
  a last `e2e` Ticket blocked by all others, or leaves the `skip-test-e2e` opt-out to the
  user. The mason contract documents both labels and the refusal. The e2e Ticket carries no
  documentation update, and the release check verifies that.
- `to-mason` applies priorities, the e2e Ticket or its opt-out, and the release labels.
  `to-tickets` applies no label. The release check in `REVIEW.md` is run by `to-mason`.
- `contracts/mason.md` describes mason on GitHub and is applied by `to-mason` only.
  `grill`, `to-spec`, and `to-tickets` know no label.
