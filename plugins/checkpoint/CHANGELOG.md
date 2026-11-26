# Changelog

All notable changes to this plugin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.1] - 2026-11-26

### Added

- MIT license and plugin icon.

## [0.1.0] - 2026-10-23

### Added

- `handoff` and `resume`, moved from the `tilap` plugin. `handoff` writes the session's
  in-progress work to `.agent/handoffs/`. `resume` loads one, or rebuilds state from git
  when none exists. Commands are `/checkpoint:handoff` and `/checkpoint:resume`. Neither
  auto-invokes.
