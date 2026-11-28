# Run report

One comment per run on the feature, saying what the run consumed and what made it harder.
Posted by `implement` and `ship`. Its format is fixed so that reports can be compared and
parsed: same headings, columns, order and labels in every report.

## Collect during the run

- Read the clock when the command starts, at the start of each step, and at the start and
  end of each sub-agent.
- Write each time, and each notable difficulty as it happens, to a notes file in a temporary
  directory outside the repository. Do not rely on the conversation to remember them.
- Ask every sub-agent to report the difficulties it met.
- Start every brief and every follow-up sent to a sub-agent with the line
  `[frame:<agent> <ticket> <attempt>]`, with the values of its report row, for instance
  `[frame:developer #43 1]` or `[frame:plan-reviewer - 2]`.
- Take token counts from the script below only. Never estimate one.
- Measuring never stops or fails a run: what cannot be obtained is `n/a`.

## Token counts

When the report is due, run [tokens.py](../scripts/tokens.py) with the start of each step
that took place and the end of the run:

```bash
python3 <path to tokens.py> --step preflight=<time> --step build=<time> --end <time>
```

It prints the token columns and the model of each row, to merge with the durations of the
notes. A row it does not give, or `"available": false`, is `n/a`.

This is a quick solution: it supports Claude Code only, by reading its session journals,
whose format is internal to it and may change in any release. Requests the journals give no
usage for are not counted. It only reads, and a failure changes nothing but the report.

## Format

Everything in the comment is in English. This is the whole comment:

```markdown
<!-- frame:metrics v1 -->

### Metrics

command: ship | feature: #42 | run: 1 | status: completed | tool: claude-code

| step         | agent          | ticket | attempt | model             | duration_s | input | cache_write | cache_read | output |
| ------------ | -------------- | ------ | ------- | ----------------- | ---------- | ----- | ----------- | ---------- | ------ |
| preflight    | orchestrator   | -      | 1       | claude-sonnet-5-5 | 40         | 1200  | 18000       | 90000      | 2100   |
| planning     | orchestrator   | -      | 1       | claude-sonnet-5-5 | 420        | 8400  | 61000       | 940000     | 14200  |
| planning     | plan-reviewer  | -      | 1       | claude-sonnet-5-5 | 120        | 900   | 42000       | 210000     | 6100   |
| build        | orchestrator   | -      | 1       | claude-sonnet-5-5 | 1560       | 5200  | 38000       | 1450000    | 11800  |
| build        | developer      | #43    | 1       | claude-sonnet-5-5 | 660        | 3100  | 74000       | 820000     | 21500  |
| build        | developer      | #44    | 1       | claude-sonnet-5-5 | 480        | 2400  | 51000       | 530000     | 14900  |
| verification | orchestrator   | -      | 1       | claude-sonnet-5-5 | 540        | 1800  | 12000       | 380000     | 3900   |
| verification | final-reviewer | -      | 1       | claude-sonnet-5-5 | 300        | 1100  | 55000       | 340000     | 7200   |
| delivery     | orchestrator   | -      | 1       | claude-sonnet-5-5 | 540        | 1500  | 9000        | 460000     | 3200   |
| total        | -              | -      | -       | -                 | 3100       | 25600 | 360000      | 5220000    | 84900  |

### Notable difficulties

| step     | ticket | category    | status     | description                                                                 |
| -------- | ------ | ----------- | ---------- | --------------------------------------------------------------------------- |
| build    | #43    | code-defect | fixed      | Existing date parser ignored time zones; fixed before the ticket could pass |
| build    | #44    | tooling     | workaround | Test browser missing; installed it in the worktree                          |
| delivery | -      | ci          | fixed      | Preview build failed on the new database schema; 2 CI runs                  |
```

## Header

| Field     | Value                                                   |
| --------- | ------------------------------------------------------- |
| `command` | `ship` or `implement`: the command the person typed     |
| `feature` | The issue number                                        |
| `run`     | 1 plus the number of run reports already on the feature |
| `status`  | `completed` or `stopped`                                |
| `tool`    | The host running the agents, in lower case with hyphens |

## Metrics table

`step` is one of these, in this order. A step lasts until the next one starts.

| `step`         | Starts when                         |
| -------------- | ----------------------------------- |
| `preflight`    | The command starts                  |
| `planning`     | `ship` starts drafting the tickets  |
| `build`        | The feature branch is worked on     |
| `verification` | The checks on the whole feature run |
| `delivery`     | The feature branch is first pushed  |

| `agent`          | Who                                        |
| ---------------- | ------------------------------------------ |
| `orchestrator`   | The session that runs the command          |
| `plan-reviewer`  | A sub-agent running gate A                 |
| `developer`      | A sub-agent writing the code of one ticket |
| `final-reviewer` | A sub-agent running gate C                 |

- Rows are ordered by step; within a step, the orchestrator first, then by ticket and
  attempt. The last row is `total`.
- Each step has its `orchestrator` row, even when it did not take place: its other cells are
  then `-`. A step entered again adds to its row.
- `attempt`: a ticket sent back, or a new review round, adds a row. It is 1 for the
  orchestrator. Work the orchestrator does on a ticket stays in `build` / `orchestrator`.
- `ticket`: the ticket of a `developer` row, `-` elsewhere.
- `model`: as the host names it.
- `duration_s`: whole seconds. For the orchestrator, the whole step, sub-agents included.
  For `total`, the elapsed time of the run, not the sum of the rows.
- Tokens are raw integers by type, with no unit, separator or weighting:
  - `input`: input tokens neither read from nor written to a cache;
  - `cache_write`: input tokens written to a cache;
  - `cache_read`: input tokens read from a cache;
  - `output`: output tokens, reasoning included.
- `total` sums each token column. A column holding an `n/a` has `n/a` as its total.
- `-` means not applicable, `n/a` that the data is not available. A type the host's model
  does not have is `n/a`.

## Notable difficulties

A difficulty enters when it explains a notable amount of extra time or tokens. An incident
solved at once, with no rework and no wait, does not. Every `attempt` above 1 has its line,
saying why.

| `category`     | Covers                                                   |
| -------------- | -------------------------------------------------------- |
| `spec`         | Need ambiguous, contradictory, or wrong against the code |
| `code-defect`  | Existing bug found while building                        |
| `test-failure` | Failing tests that forced rework, unstable tests         |
| `review`       | Failed review to run again, with no better category      |
| `ci`           | CI failure or slowness                                   |
| `timeout`      | Command or agent hung, interrupted or too long           |
| `tooling`      | Tool, permission or access missing or failing            |
| `environment`  | Installation, database, ports, variables, worktree       |
| `other`        | Anything else                                            |

- `status`: `fixed`, `workaround` or `open`.
- One line per difficulty, ordered by step then ticket, with no `|` in the description.
- State what was observed and what was done. A cause that is not proven starts with
  `suspected:`.
- The issue may be public: no secret, token, personal data or log excerpt.
- With none, the table holds the single row `| - | - | none | - | - |`.

## Post it

Post one report at the end of each run, once the CI checks are settled or when the run
stops, and read it back. A run whose preflight fails writes nothing. A report is never
edited by a later run, and posting it is not counted in it.
