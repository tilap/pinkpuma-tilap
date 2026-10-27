# Changelog

All notable changes to this plugin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
