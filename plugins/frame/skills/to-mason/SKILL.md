---
name: to-mason
description: >-
  Prepare published tickets for mason, the automated development system, then release them:
  apply priorities, add the feature-test Ticket or the explicit opt-out, and — on separate
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
skill decides nothing: a missing decision (an unsettled feature-test decision, an unknown project)
sends the user back to `grill`.

## Step 1 — Gather

The feature, its tickets (numbers, blockers, the priorities of the breakdown) and the spec's
acceptance scenarios `S*` with the feature-test decision (all, all but some, or skip). In order of preference: this conversation; the
feature and its sub-issues read back from the board. Settle the label names: a name the user
gives wins, else the contract's defaults. List the repository's labels (`gh label list`) and
compare; a missing label is reported, never created silently (see Conventions).

## Step 2 — Check the feature and the tickets

Run the contract's checklist over the feature and every ticket, and report it as a short
table. Check what mason would drop silently or refuse: no title or body, more than one
`project:` or `priority:` label, a value off the scale, a ticket that is not a native
sub-issue of the feature, a cycle. Fix what fails, or tell the user what only they can fix.

## Step 3 — Decide the feature-test Ticket

First find out whether the Project declares the feature-test check: read `mason.config.yaml`
in the code place (the check is declared by a `builder.featureTest` entry and a feature Gate
with `skipWhen`). If the file cannot be read, ask in one short question; do not guess. A
Project that does not declare the check gets neither a ticket nor the opt-out label.

When it does, by the spec's feature-test decision:

- **All scenarios, or all but some** → draft the feature-test Ticket: the last one, blocked by
  **every** other ticket, label `feature-test`, body from the template below. The scenarios
  left out are named in its body, with the reason, and not tested.
- **Skip** → no feature-test Ticket; the feature needs the opt-out label
  (`skip-feature-test`) instead.
- **Neither** → stop and send the user back to `grill`: mason refuses a feature with
  neither, as `invalid`.

## Step 4 — Review with the user

Show, in one list: each ticket with the labels to add (`priority:` only where the breakdown
set one), the full feature-test Ticket draft or the opt-out, and the labels missing from the
repository. Run the **release check** of [REVIEW.md](../../feature-planning/REVIEW.md), answering every item
`pass` / `fail` / `n/a` with its evidence. Nothing is published before the user approves the
exact content.

## Step 5 — Publish

With that approval, in this order:

1. Add the `priority:` labels (only those the breakdown set).
2. Create the feature-test Ticket last, as a sub-issue of the feature, blocked by every other ticket
   (`gh issue create --parent <feature> --blocked-by <n>,<n> --title … --body-file -`), with
   its label. **Do not add the ticket-ready label** yet.
3. Opt-out: apply nothing to the feature and tell the user to put the opt-out label on it
   themselves; confirm the label exists.
4. With approval of its exact text, add **one comment on the feature** saying which ticket
   carries the feature-test scenarios (`S*` → ticket number), or that the check is opted out.

Report the numbers and what each now carries. Then stop and ask for validation of the list
as it now stands on the tracker.

## Step 6 — Release (separate approval)

Only after the user has looked at the published tickets and says go. Explain first: **from
the moment the labels are in place, development may start unattended.** On approval, in this
order:

1. Add the "tickets final" label (GitHub default: `task-ready`) to **every** ticket,
   feature-test Ticket included, together.
2. Add the "feature final" label (GitHub default: `feature-ready`) to the feature, **last**.

Never set or remove labels mason manages (`mason:*`). A ticket added after the release is
ignored; if the list must change, tell the user rather than adding.

## feature-test Ticket template

```markdown
## Context

The feature tests of this feature. They prove, once, on the assembled feature, what the
scenarios below say it does. The feature is built when this ticket runs.

## What to build

Tests for the scenarios below, each at the level the scenario names (a service, a route, a
page), and nothing else.

## Scenarios

<The spec's acceptance scenarios, copied verbatim, with their ids S1, S2, …>

<Scenarios left out, with the reason, when the spec names any.>

<When a scenario signs in: a test account exists for it.>

## Done when

- [ ] Each scenario above has at least one test whose name contains its id.
- [ ] `feature-tests/scenarios.json` lists exactly the scenario ids above.
- [ ] Only tests and `feature-tests/scenarios.json` were changed.
- [ ] The tests pass against the built feature.

## Constraints

- Write tests and `feature-tests/scenarios.json` only; update an existing test only where
  a scenario above changes it.
- Do not touch application code.
- Run the tests against the built feature as you go.
- A test that fails because the feature does not do what its scenario says is not fixed by
  weakening the test or changing the application: stop and say what the feature does
  instead.

## If unsure

Stop and say what is unclear or what the repository lacks (a test account, say). Do not
choose an interpretation.

## Out of scope

- Everything that is not a test or the manifest.
```
