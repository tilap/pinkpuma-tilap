---
name: grill
description: >-
  Turn a fuzzy idea or business need into one complete, shared understanding through a
  relentless round-by-round interview, grounded in the project's docs and code (read-only)
  and writing nothing to disk. Use when the user brings an idea, feature request or need
  that is not yet precise, before any spec or ticket is written.
disable-model-invocation: true
metadata:
  plugin: frame
---

# Grill

Conventions: [../../CONVENTIONS.md](../../feature-planning/CONVENTIONS.md) — read it first (the three
places, nothing written to disk, reading the project, vocabulary, writing rules).

One job: interview the user until you and they share one precise understanding of a need,
complete enough that a spec can be written from it without the user in the room. This is
the only skill in the chain that makes decisions; the next ones only record and slice them.
It writes no file and publishes nothing: the conversation is its record.

## Step 1 — Take in the need and the places

Start from the user's argument or the conversation. If they point at an existing feature or
ticket, read its body and comments. Note which of the three places they named (board,
tracker, code); you will need them in the next steps, so settle any missing one now in a
single short question. Restate the need in two sentences — who has the problem, what they
cannot do today.

## Step 2 — Gather the facts yourself

Read the project documentation and the code that touch the need (read-only; see
Conventions). **Facts are your job, never the user's.** If the host lets you explore in the
background, do so and keep interviewing on the questions that do not depend on it.

## Step 3 — Interview in rounds

Map the need as a **decision tree**: every decision branches into the decisions that depend
on it. The **frontier** is every open decision whose prerequisites are settled — what you can
ask now without guessing answers you have not heard.

Each round, ask the frontier — at most the 7 questions that unblock the most — then wait.
Number every question across the whole session, give your recommended answer, and word it so
that "yes" accepts the recommendation:

```
❓ **Q1 — <title>**: <question, with options when there are several>

➡️ <recommended answer, and why in one line>
```

A question that depends on another still open belongs to a later round. Each answer reshapes
the tree: recompute the frontier and ask the next round.

Work the tree **business first**, skipping any level the need already makes obvious:

1. **Problem and outcome** — who suffers today, what success looks like and how anyone would
   observe it.
2. **Actors** — who acts, who is affected, who may do what.
3. **Business rules** — invariants, limits, states, transitions; precise numbers, not "a few"
   or "quickly".
4. **Scenarios** — concrete examples, then edge cases you invent to probe each rule: empty,
   concurrent, repeated, cancelled, partial, unauthorised, at the limit.
5. **Scope** — what is deliberately refused. Explicit "no"s are often the most useful lines.
6. **Technical shape** — only choices visible to the business or hard to reverse; leave the
   rest to implementation.
7. **Testing** — at which boundaries the behaviour can be checked from outside (existing
   ones first), so tickets can state observable outcomes later. Then the **feature tests**:
   the scenarios of level 4 are what gets proved once, by tests, on the assembled feature,
   at the level a scenario names (a service, a route, a page). Settle whether every
   scenario can be proved that way, and name those that cannot with the reason; or an
   explicit **skip** (a refactor, a configuration change, a trivial need). A scenario
   behind a sign-in states that a test account exists. Do not ask whether the Project has
   a test suite or an e2e suite: the plugin keeps no configuration and the project's own
   tooling decides whether the check runs. Never write a scenario that only a full browser
   journey could prove unless the need is that journey.
8. **Cross-cutting** — for each of data migration, security and permissions, performance or
   limits, dependency changes and backward compatibility, **and every other cross-cutting
   standard the project's own documentation sets** (accessibility, design, a security
   policy, a global journey suite… whatever the docs you read in Step 2 name): does the
   need touch it? Settle a decision, or an explicit "not concerned", so no review later has
   to guess. Where a project standard applies, state what it requires of this need in
   observable terms, and say where it is checked when the docs say so (the project's CI,
   a Gate, the feature tests); do not invent a standard the docs do not hold.

Keep the language sharp while interviewing:

- **Vocabulary** — a word the docs or code use differently, or two words for one concept:
  stop and settle it ("The docs call this a *Booking*; you said *reservation* — same?").
- **Code disagreements** — the user states how something works and the code says otherwise:
  show the contradiction and ask which one is right.
- **Decision-record conflicts** — an answer contradicts an accepted ADR: say so and ask
  whether it is being reopened.

## Step 4 — Keep the record visible

Nothing may exist only in the user's head or only in a scrolled-away message. After every
round, close with a compact **Settled so far** block: decisions (D1, D2, …), business rules
(R1, …), scenarios (S1, …) with the ones that cannot be proved by feature tests, or the
skip, scope refusals, and what is still open. Update it rather than repeating the whole
history. Propose a documentation update (decision record, business rule) when it qualifies
(see Conventions) and record the agreed draft in the block.

## Step 5 — Close

The interview is done when the frontier is empty: every branch visited, nothing silently
assumed, open questions empty or explicitly deferred by the user. Then:

1. Show the final **Settled so far** and ask the user to confirm it matches their
   understanding.
2. Size the need and end with exactly one next step, as the conventions say (Handing over
   to the next step): tell the person which command to type, in this same conversation:
   - fits a single ticket → `/frame:to-tickets`;
   - larger → `/frame:to-spec`.

Do not start the next step yourself, and do not ask whether to go on: you cannot start it, so
the person has to type the command.
