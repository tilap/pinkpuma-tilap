# Changelog

All notable changes to this plugin are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Removed

- `implement-github-issue` skill: it is `/frame:implement`, in the `frame` plugin.
- `report-issue` skill and `/tilap:report-issue`.

## [0.7.0] - 2026-11-26

### Added

- `implement-github-issue` skill (`/tilap:implement-github-issue`): implements a GitHub issue and its sub-issues with
  one commit per sub-issue on a feature branch, delivered as one pull request. It keeps assignees, acceptance-criteria
  checkboxes and project status up to date, and never merges the pull request or closes an issue by hand.
- MIT license, plugin icon, and [privacy policy](PRIVACY.md).

### Changed

- The bundled MCP client is renamed from `notes` to `tilap-data`. Skills that call it use the new name. A permission rule that names a `mcp__plugin_tilap_notes__*` tool no longer matches: the tools are `mcp__plugin_tilap_tilap-data__*`. The `notes_url` and `notes_token` settings keep their names.

### Removed

- `video-article` skill and `/tilap:video-article`.

## [0.6.0] - 2026-11-23

### Added

- `report-issue` skill (`/tilap:report-issue`): turns a rough problem report into a GitHub issue on the right
  repository with `gh`. The repository wins over the skill's defaults: its issue template, title prefix, labels,
  issue type and language are used when it has them, English otherwise. It labels the issue `needs-triage`,
  appends the user's words as an "Original report" section, and asks a question only when the report or the
  repository cannot be determined. It does not auto-invoke and does not use the notes MCP.

## [0.5.0] - 2026-11-18

### Added

- `knowledge-review` skill and `/tilap:knowledge-review` command: re-check the facts of the oldest
  active knowledge entries (versions, renamed or removed APIs, deprecated tools, changed defaults)
  against official sources, report each as `current`, `needs-update` or `deprecate` with a source link
  per claim, and write nothing until the owner approves that entry. Needs a notes site that returns
  `verifiedAt` and filters `list_knowledge` with `notVerifiedSinceDays`.

## [0.4.0] - 2026-11-08

### Added

- `video-article` skill: writes a blog article from one collected video through the notes MCP
  (`list_imports`, `get_import`, `get_writing_guides`, `create_post` with `importId`) and saves it as a
  draft linked to the video (`/tilap:video-article`). It does not auto-invoke.
- `lang` skill: stores one foreign-language phrase and its French translation in
  the private glossary through the notes MCP (`/tilap:lang`). It checks
  `list_expressions` first and does not auto-invoke.

### Removed

- `session-note` skill and `/tilap:session-note`: the site no longer has session notes (their MCP tools
  `create_session_note` and `update_session_note` are gone).
- `explore`, `grill`, `to-spec`, `to-tickets`, `to-mason`, and `/tilap:plan` now live in
  the `frame` plugin. The unreleased planning notes that were here moved with them; see
  `plugins/frame/CHANGELOG.md`.
- `handoff` and `resume` now live in the `checkpoint` plugin
  (`/checkpoint:handoff`, `/checkpoint:resume`).

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
