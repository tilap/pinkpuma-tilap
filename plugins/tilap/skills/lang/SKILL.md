---
name: lang
description: >-
  Store one foreign-language expression and its French translation in the owner's
  private glossary through this plugin's notes MCP. Use only when the user invokes
  /tilap:lang.
disable-model-invocation: true
metadata:
  plugin: tilap
---

# Lang

Store one expression and stop. The glossary is private. The entry is stored by the
`notes` MCP server this plugin ships. Do not create a file, and do not store a phrase
the user did not ask to keep.

## Tools

The server is the OrangeMonkey site (`/api/mcp`). It also exposes blog, session-note
and knowledge tools. Ignore those. For an expression, use only:

- `list_expressions`
- `get_expression`
- `create_expression`
- `update_expression`
- `delete_expression`

`create_expression` takes `lang`, `expression`, `translation`, and an optional `note`.
`update_expression` takes `id` and any of those fields; omitted fields stay; `note: null`
clears the note. If `create_expression` is absent, say the notes server is not
connected, or that the token is read-only, and stop. Do not fall back to a local file.

## The entry

| Field         | Content                                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `lang`        | Language of the expression: `en`, `fr`, `it`, `es`, `de`, or `vi`.                                                                               |
| `expression`  | The phrase in that language. 1–1,000 characters, not blank.                                                                                      |
| `translation` | Always French. 1–1,000 characters, not blank. When `lang` is `fr`, a rephrasing or a short explanation of the meaning, not a copy of the phrase. |
| `note`        | Optional context the user gave (where they heard it, the register). At most 5,000 characters. Omit it when they gave none.                       |

Take the phrase from what the user states. If they gave the French too, use theirs. If
they gave only the foreign phrase, write the French translation. If the language is
obvious, do not ask. Ask one question only when the phrase or its language is missing
and you cannot tell which of the six codes it is.

The same phrase may exist twice. Do not add a second copy unless the user insists.

## Before the call

Call `list_expressions` with `lang` when you know it and `query` set to the phrase.
`query` is literal: every word must appear, in the expression or the translation, not in
the note. If a row is the same phrase in the same language, stop and say its `id` and
its current translation. Update it with `update_expression` only when the user is
correcting that row. If this chat already stored the phrase, update that `id` instead of
creating another one.

## Several phrases

When the user gives several phrases in the same message, repeat the check and the write
for each one. Otherwise store one and stop.

## Delete

Call `delete_expression` only when the user explicitly asks to remove one, and only after
`get_expression` confirms the `id`.

## After the call

`create_expression` and `update_expression` return `{ expression: { id, ... } }`. Reply
with the `id`, the language, the phrase and the French translation, one line per phrase.
Do not paste the tool payload. There is no public URL.
