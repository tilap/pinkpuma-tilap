# Changelog

All notable changes to this plugin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
