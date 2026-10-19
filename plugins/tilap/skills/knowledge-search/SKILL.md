---
name: knowledge-search
description: >-
  Before designing or implementing a technical topic (env vars, auth, data
  fetching, testing, deployment, project structure, ...), consult the owner's
  knowledge base of proven dev practices through this plugin's notes MCP and apply
  the matching entries. Use at the start of a design or implementation task, and
  when the user asks how they usually do something.
metadata:
  plugin: tilap
---

# Knowledge search

The owner keeps a knowledge base of opinionated, proven dev practices. Read it before
you decide how to build something, so you apply their default instead of inventing one.
This skill only reads. To add or change an entry, the user invokes `/tilap:knowledge`.

## Tools

Use only `list_knowledge` and `get_knowledge` on the `notes` MCP server. If they are
absent, the server is not connected: say so in one line and continue without the base.
Do not guess what the base would say.

## When

Run it once per topic, before the first design or implementation step, not on every
edit. Skip it for a typo, a rename, or a question that has no practice behind it.

## Steps

1. Call `list_knowledge` with a short `query` (one or two words from the topic, literal:
   every word must appear), and `stack` when the project's stack is known (`next`,
   `postgres`). If nothing matches, retry once with a `tag` or a broader word. The index
   shows slug, title, summary, tags and stack, not the rule.
2. Call `get_knowledge` on each entry whose `summary` fits the task. Read `appliesWhen`
   and `notAppliesWhen` before the rule.
3. Apply the rule as the default. Mention the entry by slug and give the rationale when
   it matters for the choice.
4. If the task falls under `notAppliesWhen`, or needs something the rule forbids, flag
   the deviation to the user and say why. Do not force the rule, and do not drop it
   silently.
5. An entry marked `deprecated` is history, not a default. Say so and do not apply it.

## No match

Say the base has no entry on the topic, in one line, and proceed with your own judgment.
If the user then settles on a practice worth keeping, suggest `/tilap:knowledge`. Do not
write the entry yourself.
