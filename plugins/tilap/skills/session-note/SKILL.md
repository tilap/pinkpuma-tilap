---
name: session-note
description: >-
  Save the current coding session as one dev note (journal, recipe, pitfall, or
  decision) through this plugin's notes MCP. Use only when the user invokes
  /tilap:session-note.
disable-model-invocation: true
metadata:
  plugin: tilap
---

# Session note

Write one note and stop. The note is stored by the `notes` MCP server this plugin
ships. Do not create a file, a draft, or a second note for the same chat.

## Tools

The server is the OrangeMonkey site (`/api/mcp`). It also exposes blog tools. Ignore
those. For a note, use only:

- `whoami`
- `list_session_notes`
- `get_session_note`
- `create_session_note`
- `update_session_note`

`create_session_note` takes `title`, `content`, and optional `project`, `sessionDate`,
`tags`. There is no `kind`, no `sessionKey`, no `stack`, no `url`, and no
`supersedesId`. Tools named `capture_note`, `search_notes`, `get_note`, or
`supersede_note` are not on this server: do not call them and do not describe them as
missing. If `create_session_note` itself is absent, say the notes server is not
connected and stop. Do not fall back to a local file.

## Kind

The user may name a kind: `journal` or `log`, `recipe`, `pitfall`, `decision`. Otherwise
the default is `log`. Ask one question only when the session produced a method worth
replaying and the user did not name a kind: log or recipe. Then call the tool. Do not
ask them to review the text.

The server has no kind field. Store the kind as the **first tag**, exactly one of
`log`, `recipe`, `pitfall`, `decision` (`journal` is the tag `log`). Further tags are
the stack actually used (`next`, `postgres`), not a wish list. Tags are lowercase
slugs (letters, digits, hyphens), at most 10, each at most 40 characters.

## Before the call

For `recipe`, `pitfall`, or `decision`, call `list_session_notes` first with `project`,
`tag` set to that kind, and a short `query`. `query` is literal: every word must appear
somewhere in the title, content, project, or tags. If a note covers the same goal, ask
once: update it (`update_session_note` with its `id`) or keep both. A `log` skips the
search.

If this chat already stored a note, call `update_session_note` with that `id` instead of
creating another one. Remember the `id` from the tool result.

## The note

Write it in the language of the session. Distill. Do not paste the transcript, the tool
log, or a secret (a database URL with a password, an `sk-` key, an `omk_` token, a private
key). If one appears, drop that fragment and continue. The server does not scan for
secrets.

`title` is one line, at most 200 characters. `project` is the repository name (at most
100 characters). Omit `sessionDate` so the server uses today in Europe/Paris, unless the
work happened on another day (`YYYY-MM-DD`). `content` is Markdown, at most 20,000
characters.

Body headings inside `content`:

- `log`: What was asked / What shipped / What failed
- `recipe`: Result / Stack and versions / Steps / How to verify / Do not generalize / What failed
- `pitfall`: Symptom / Wrong approach / Fix
- `decision`: Options / Choice / Why

## After the call

Call `create_session_note` once, or `update_session_note` when this chat already has an
id or the user chose to replace an existing note. The tool returns `{ note: { id, ... } }`.
Reply with that `id` and the kind. Do not paste the note back. There is no public URL:
the journal is private.
