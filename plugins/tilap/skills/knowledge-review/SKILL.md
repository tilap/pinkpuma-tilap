---
name: knowledge-review
description: >-
  Re-read the oldest entries of the owner's knowledge base, check their facts
  (versions, renamed or removed APIs, deprecated tools, changed defaults, broken
  commands) against official sources, and propose updates for the owner to approve.
  Use only when the user invokes /tilap:knowledge-review.
disable-model-invocation: true
metadata:
  plugin: tilap
---

# Knowledge review

Entries age silently: a version moves, a tool is renamed, a default changes. This skill
re-checks the **facts** of a few entries against current official sources and proposes
corrections. The entries are the owner's opinions: it never changes an opinion, and it
never writes before the owner approves that entry.

## Tools

Use the `notes` MCP server: `list_knowledge`, `get_knowledge`, `update_knowledge`, plus the
host's web search and page fetch tools. Ignore the blog, video and expression tools. Do not
call `create_knowledge` or `delete_knowledge`.

If `update_knowledge` is absent, say the notes server is not connected or the token is
read-only, and stop. If `list_knowledge` has no `notVerifiedSinceDays` filter, or its
entries carry no `verifiedAt`, the site is not updated: say so in one line and stop.

## Arguments

The user may give, in any order:

- a **slug**: review only that entry, whatever its verification date or status;
- a **stack** name (`next`): only entries whose `stack` contains it, with or without
  version;
- `--older-than <days>`: the threshold, 90 by default;
- a count, only when the user asks for more than 5 entries.

## Select

1. Call `list_knowledge` with `status: active`, `notVerifiedSinceDays: <threshold>`, and
   `stack` when given. The index comes back oldest verification first.
2. Move the entries with a versioned stack item (`next@16`) before the others, keeping the
   order inside each group.
3. Keep the first 5, or the count the user asked for. Say how many were eligible and how
   many you take.
4. Call `get_knowledge` on each kept entry.

Nothing eligible: say so in one line and stop.

## Verify

For each entry, extract the checkable claims: versions, commands and flags, API and
option names, tool names, defaults, whether a tool is still maintained. Check each one
against an official source: the documentation, the changelog or the release page of the
tool itself. Prefer the page for the entry's reference version, then the latest one. Never
rely on memory or on blog posts for a claim.

Check **facts only**. Style, structure, and whether the practice is a good one are not
yours to judge here.

A claim you cannot confirm or refute from an official source is `unverified`. It never
becomes a proposed change.

## Classify

| Class | Meaning |
| --- | --- |
| `current` | Every checkable claim holds. |
| `needs-update` | At least one sourced fact is wrong or outdated, and the fix is a fact (a version, a name, a command). |
| `deprecate` | The thing the entry is about is removed, abandoned, or replaced by its maintainers, so the rule can no longer be followed. |

## Report

One block per entry, in this order, written in the language of the entry (French):

1. `slug`, title, class.
2. For `needs-update`: the diff, field by field, only the fields that change, old text then
   new text. Keep the owner's wording and opinion; change only the fact.
3. For `deprecate`: the sourced reason.
4. Every claim, in every class, with its source link. A claim has one link or it is not
   listed as checked.
5. `Unverified`: the claims no official source settled. No change is proposed for them.
6. `Opinion question`: when the review suggests a different practice (another tool, another
   approach) rather than a corrected fact, state the question for the owner and propose no
   rewrite.

After the blocks, add a `Gaps` list: topics the base should cover but does not, one line
each. Do not create entries.

Never write a secret, key or credential in the report or in a proposed field. Use
`<redacted>`.

## Approve and write

Nothing is written during the review. Ask the owner, entry by entry, to approve:

- `needs-update` and `deprecate`: the diff or the retirement.
- `current`: the new verification date alone.

On approval, call `update_knowledge` once for that entry:

- `slug`;
- the approved fields only (`status: deprecated` for a retirement);
- `verifiedAt`: now, as an ISO 8601 date-time;
- `status`: always pass it, `active` unless retiring. An older site resets an omitted
  status to `draft`.

An entry the owner declines or leaves unanswered stays untouched, `verifiedAt` included.
Do not change the `slug`.

## After the run

Reply with one line per entry: slug, class, and what was written (`updated`, `verified`,
`deprecated`, `untouched`). Do not paste the entries back.
