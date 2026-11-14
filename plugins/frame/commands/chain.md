---
description: After the grill, run to-spec, to-tickets and to-mason without stopping, making every choice itself from the given instructions and the defaults.
argument-hint: "[instructions specific to this run]"
disable-model-invocation: true
---

# Chain the steps after the grill

Take the feature agreed in this conversation through the rest of the plugin, hands-off:
$ARGUMENTS

The instructions above are specific to this run (granularity, seams, priorities, tests, labels,
whether to release). Run this command in the conversation where `/frame:grill` ended: the
**Settled so far** is the source. If the understanding was not agreed, or the need is not in
this conversation, say so and stop: this command does not interview.

Read [CONVENTIONS.md](${CLAUDE_PLUGIN_ROOT}/feature-planning/CONVENTIONS.md) now: it holds the rules of
every step.

The skills are written to run when a person asks for them, so a step is run by reading its
file and following it as written, not by calling it by name:

1. **To spec** — [skills/to-spec/SKILL.md](${CLAUDE_PLUGIN_ROOT}/skills/to-spec/SKILL.md).
   Skipped when the grill concluded that the need fits a single ticket.
2. **To tickets** — [skills/to-tickets/SKILL.md](${CLAUDE_PLUGIN_ROOT}/skills/to-tickets/SKILL.md).
3. **To mason** — [skills/to-mason/SKILL.md](${CLAUDE_PLUGIN_ROOT}/skills/to-mason/SKILL.md).
   Only when the instructions say the project is built by mason, or the code place holds a
   `mason.config.yaml`. Otherwise the chain ends after `to-tickets`, and says so.

## What this command takes over

Wherever a step waits for the person, this command answers instead, then goes on:

- **The three places**: the instructions, else what the conversation already named, else the
  inference the conventions describe (code = current directory, GitHub repository = its git
  remote). Ask only when nothing can be inferred.
- **Test boundaries (`to-spec` Step 3)**: choose the seams by the instructions, then the
  defaults below. Do not wait for confirmation.
- **Slicing (`to-tickets` Steps 3 and 5)**: validate the list once the checks of Step 6 pass.
- **Gate A**: answer every item. Correct each `fail` and run the gate again, three rounds at
  most. A `fail` that remains stops the chain with the item, its evidence and a recommendation.
- **Publishing**: the spec, the tickets, the review sheet, the priorities, the feature-test
  Ticket, and the comment on the feature are approved by this command, for this run only. A
  label that does not exist is created only if the instructions say so; otherwise stop.
- **Release (`to-mason` Step 6)**: **not approved** unless the instructions say to release.
  Without it, stop once the tickets stand on the tracker and say how to release them.
- **Closing questions** ("is the list right?", "validate the published list"): skipped.

## What this command never takes over

- **A decision nobody made.** A step that sends the person back to `grill` (a missing
  decision, an open question that blocks, an unsettled feature-test decision) does so here
  too: stop, name the question, recommend an answer.
- **A contradiction with an accepted decision record** that neither the instructions nor the
  grill reopen: stop.
- **The rules of the steps.** Nothing is written to disk, nothing is invented, nothing is
  published twice, and the report names what was done and what was not.

## Defaults

Used when the instructions say nothing on a point, in this order of authority: the
instructions of the run, then the project's own docs and decisions, then this list.

- Respect the existing architecture and past decisions (decision records, docs, the code) for
  organisation, tests and naming. Leave one only with a stated reason.
- Reuse before creating: one rule in one place (DRY), an existing mechanism rather than a new one.
- Colocate: code, its tests and its documentation live where the project already puts them.
- The simplest thing that works: no option and no defensive case without an observed need.
- Tickets are vertical slices, each green alone, each criterion backed by a test that can fail.
- Between two valid options, take the more reversible one.

A choice made from the defaults is a decision: record it in the spec (or, for a single
ticket, in the ticket) as "Decided by default", with what it turned down. The owner replaces
it if they disagree.

## Report

End with a short report: what was published (numbers, titles, blockers, the frontier), the
choices taken by default, and what stopped the chain, if anything.
