---
name: to-mason
description: >-
  Prepare published tickets for mason, the automated development system, then release them:
  apply priorities, add the end-to-end (e2e) Ticket or the explicit opt-out, and — on separate
  explicit approval — add the readiness labels that let development start. Use after
  to-tickets, when the project is built by mason on GitHub.
disable-model-invocation: true
metadata:
  plugin: frame
---

# To mason

Conventions: [../../CONVENTIONS.md](../../feature-planning/CONVENTIONS.md) — read it first (the three
places, nothing written to disk, publishing and writing rules). **Then read the contract**
[../../contracts/mason.md](../../feature-planning/contracts/mason.md): mason drops what it cannot read, so its
rules are requirements here.

One job: take a feature and its tickets, already published by `to-tickets`, and make them
what mason reads — then, only on a separate approval, release them. Like `to-tickets`, this
skill decides nothing: a missing decision (an unsettled e2e scenario, an unknown project)
sends the user back to `grill`.

## Step 1 — Gather

The feature, its tickets (numbers, blockers, the priorities of the breakdown) and the spec's
end-to-end scenarios `E*` or skip decision. In order of preference: this conversation; the
feature and its sub-issues read back from the board. Settle the label names: a name the user
gives wins, else the contract's defaults. List the repository's labels (`gh label list`) and
compare; a missing label is reported, never created silently (see Conventions).

## Step 2 — Check the feature and the tickets

Run the contract's checklist over the feature and every ticket, and report it as a short
table. Check what mason would drop silently or refuse: no title or body, more than one
`project:` or `priority:` label, a value off the scale, a ticket that is not a native
sub-issue of the feature, a cycle. Fix what fails, or tell the user what only they can fix.

## Step 3 — Decide the e2e Ticket

Only when the Project uses the e2e check (the spec says so; if it is silent, ask in one short
question, do not guess):

- **Scenarios in the spec** → draft the e2e Ticket: the last one, blocked by **every** other
  ticket, label `e2e`, body from the template below.
- **Skip in the spec** → no e2e Ticket; the feature needs the opt-out label
  (`skip-test-e2e`) instead.
- **Neither** → stop and send the user back to `grill`: mason refuses a feature with
  neither, as `invalid`.

A Project that does not use the check gets neither.

## Step 4 — Review with the user

Show, in one list: each ticket with the labels to add (`priority:` only where the breakdown
set one), the full e2e Ticket draft or the opt-out, and the labels missing from the
repository. Run the **release check** of [REVIEW.md](../../feature-planning/REVIEW.md), answering every item
`pass` / `fail` / `n/a` with its evidence. Nothing is published before the user approves the
exact content.

## Step 5 — Publish

With that approval, in this order:

1. Add the `priority:` labels (only those the breakdown set).
2. Create the e2e Ticket last, as a sub-issue of the feature, blocked by every other ticket
   (`gh issue create --parent <feature> --blocked-by <n>,<n> --title … --body-file -`), with
   its label. **Do not add the ticket-ready label** yet.
3. Opt-out: apply nothing to the feature and tell the user to put the opt-out label on it
   themselves; confirm the label exists.
4. With approval of its exact text, add **one comment on the feature** saying which ticket
   carries the e2e scenarios (`E*` → ticket number), or that the check is opted out.

Report the numbers and what each now carries. Then stop and ask for validation of the list
as it now stands on the tracker.

## Step 6 — Release (separate approval)

Only after the user has looked at the published tickets and says go. Explain first: **from
the moment the labels are in place, development may start unattended.** On approval, in this
order:

1. Add the "tickets final" label (GitHub default: `task-ready`) to **every** ticket, e2e
   Ticket included, together.
2. Add the "feature final" label (GitHub default: `feature-ready`) to the feature, **last**.

Never set or remove labels mason manages (`mason:*`). A ticket added after the release is
ignored; if the list must change, tell the user rather than adding.

## e2e Ticket template

```markdown
## Context

The end-to-end acceptance suite of this feature. It proves, once, on the assembled feature,
the user journeys below.

## What to build

An end-to-end test suite for the scenarios below, and nothing else.

## Scenarios

<The spec's scenarios, copied verbatim, with their ids E1, E2, … (at most 5).>

<When a scenario signs in: a test account exists for it.>

## Done when

- [ ] Each scenario above has at least one test whose name contains its id.
- [ ] `e2e/scenarios.json` lists exactly the scenario ids above.
- [ ] Only the e2e suite folder and `e2e/scenarios.json` were written.

## Constraints

- Write only the e2e suite folder and `e2e/scenarios.json`.
- Do not touch application code.
- Do not run or fix the application: a red suite is repaired later, at feature level, by
  another pass.

## If unsure

Stop and say what is unclear or what the repository lacks (a test account, say). Do not
choose an interpretation.

## Out of scope

- Everything outside the suite folder and the manifest.
```
