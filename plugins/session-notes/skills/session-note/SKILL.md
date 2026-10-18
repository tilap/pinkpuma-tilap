---
name: session-note
description: >-
  Save the current coding session as one dev note (journal, recipe, pitfall, or
  decision) through this plugin's notes MCP. Use when the user asks to keep a
  session note, capitalize the work, record a recipe or a pitfall, or runs
  /session-notes:session-note.
disable-model-invocation: true
metadata:
  plugin: session-notes
---

# Session note

Write one note and stop. The note is stored by the `notes` MCP server this plugin
ships (`capture_note`). Do not create a file, a draft, or a second note for the same chat.

## Before the call

The server offers `whoami`, `search_notes`, `get_note`, `capture_note`, and
`supersede_note`. If those tools are not available, say the notes server is not
connected and stop. Do not fall back to a local file.

Pick `kind`:

- The user named it (`journal` / `log`, `recipe`, `pitfall`, `decision`): use that.
- Otherwise the default is `log`.
- Ask one question only when the session produced a method worth replaying and the user
  did not name a kind: log or recipe. Then call the tool. Do not ask them to review the text.

For `recipe`, `pitfall`, or `decision`, call `search_notes` first with a short query and
the stack. If a live note covers the same goal, ask once: replace it (pass its id as
`supersedesId`) or keep both. A `log` skips the search.

## The note

Write it in the language of the session. Distill. Do not paste the transcript, the tool
log, or a secret (a database URL with a password, an `sk-` key, an `omk_` token, a private
key). If one appears, drop that fragment and continue.

`sessionKey`: the conversation id when you know it. Otherwise
`<client>-<YYYYMMDD>-<four-word-slug>`, and reuse that exact key if you call the tool
again in this chat. `client` is `cursor` when the host is Cursor and `claude` when the
host is Claude Code.

`project` is the repository name. `stack` is short tags of what was actually used
(`next`, `postgres`), not a wish list.

Body headings:

- `log`: What was asked / What shipped / What failed
- `recipe`: Result / Stack and versions / Steps / How to verify / Do not generalize / What failed
- `pitfall`: Symptom / Wrong approach / Fix
- `decision`: Options / Choice / Why

`summary` is one line.

## After the call

Call `capture_note` once. Reply with the `url` from the tool and the kind. Do not paste
the note back. If the tool rejects a secret, remove it and call once more with the same
`sessionKey`.
