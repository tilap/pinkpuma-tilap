---
name: knowledge
description: >-
  Add or update one entry in the owner's knowledge base (a proven dev practice or
  recipe) through this plugin's notes MCP. Use only when the user invokes
  /tilap:knowledge.
disable-model-invocation: true
metadata:
  plugin: tilap
---

# Knowledge

Write one knowledge entry and stop. An entry is one precise, reusable decision ("how we
handle env vars in Next"), not a session log. The entry is stored by the `notes` MCP
server this plugin ships. Do not create a file or a second entry for the same topic.

## Tools

The server is the OrangeMonkey site (`/api/mcp`). It also exposes blog and session-note
tools. Ignore those. For knowledge, use only:

- `list_knowledge`
- `get_knowledge`
- `create_knowledge`
- `update_knowledge`

If `create_knowledge` is absent, say the notes server is not connected, or that the
token is read-only, and stop. Do not fall back to a local file.

## Source of the entry

Take the practice from what the user states, or from the current chat when they point at
it ("capitalize what we just did"). Do not invent a rule the user did not hold. If the
chat shows a method worked but the user never said it should be the default, propose the
rule in one sentence and ask them to confirm before writing.

Ask one question at most, and only for a field you cannot derive: usually `appliesWhen`
or whether the rule is a default or a one-off.

## Before the call

Always call `list_knowledge` first, with a short `query` (a topic word or two) and the
`stack` when known. `query` is literal: every word must appear. If an entry covers the
same decision, call `get_knowledge`, then ask once: update it (`update_knowledge` with
its `slug`) or create a distinct entry. Never create a near-duplicate.

If this chat already stored an entry, update that one. Remember its `slug`.

## The entry

Write in the language of the user's existing entries (check the index), otherwise the
language of the session. One entry is one decision; split if the user gave two.

| Field | Content |
| --- | --- |
| `title` | The topic, often a question. At most 200 characters. |
| `summary` | One line: when and why to consult it. At most 300 characters. |
| `appliesWhen` | The context where the rule holds. At most 500 characters. |
| `notAppliesWhen` | Where it does not hold, or where to flag a deviation. Optional. |
| `rule` | The method, short and imperative. Markdown. |
| `rationale` | Why this method, what it avoids. Markdown. |
| `alternatives` | What was discarded and why. Optional. |
| `body` | Detail, examples, step by step. Optional. Keep the rule itself out of it. |
| `stack` | Technologies with a reference version when it matters (`next@16`, `postgres`). Empty when agnostic. |
| `tags` | Domain tags, lowercase slugs, at most 10. Reuse tags already in the index. |
| `slug` | Lowercase slug. Omit to derive it from the title. Never changed afterward. |

Distill. Never write a key, token, password, or connection string with credentials; use
`<redacted>`. The server does not scan for secrets.

## Status

A new entry is a `draft` and is not served to read-only tokens. Create it as a draft
unless the user said it is ready, then pass `status: active`. Activation and retirement
(`deprecated`) are `update_knowledge` calls. Do not activate an entry the user has not
approved.

## After the call

Call `create_knowledge` once, or `update_knowledge` for an existing entry. Reply with the
`slug`, the status, and one line saying what the rule is. Do not paste the entry back.
If it is a draft, say so and that activating it is a separate step.
