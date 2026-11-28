# frame

```
/plugin install frame --marketplace tilap/pinkpuma-tilap
```

Take one feature from its options to a pull request: settle the decisions, then publish the
tickets and build them. Install it in the project where the feature is built.

## From a ticket to a pull request

1. Type `/frame:grill` and answer until the need is settled.
2. Put its final record in a GitHub issue.
3. Open a new session: the interview left in the context is read again at every request of
   the run.
4. Type `/frame:ship <issue url>`.
5. Review and merge the pull request.

`ship` checks the access, the repository and the issue, drafts the tickets, has a fresh
agent review the plan, publishes them as sub-issues, then builds them: one agent per ticket,
one commit each, a fresh agent reviewing the assembled feature, one pull request. It asks no
confirmation. It stops on a decision the issue does not hold, a review that keeps failing or
a blocker, with the question as a comment on the issue; type the same command again once
answered. It needs `gh` authenticated with the `project` scope and write access to the
repository, and refuses a project built by mason. A permission mode that lets commands run
without asking keeps the run unattended.

## Skills

| Skill                                    | Use when                                                  |
| ---------------------------------------- | --------------------------------------------------------- |
| [explore](skills/explore/SKILL.md)       | The user invokes `/frame:explore`                         |
| [grill](skills/grill/SKILL.md)           | The user invokes `/frame:grill`                           |
| [ship](skills/ship/SKILL.md)             | The user invokes `/frame:ship <issue>` on a grilled issue |
| [implement](skills/implement/SKILL.md)   | The user invokes `/frame:implement <issue>`               |
| [to-spec](skills/to-spec/SKILL.md)       | The user invokes `/frame:to-spec`                         |
| [to-tickets](skills/to-tickets/SKILL.md) | The user invokes `/frame:to-tickets`                      |
| [to-mason](skills/to-mason/SKILL.md)     | The user invokes `/frame:to-mason`                        |

| Command                  | Use when                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| [plan](commands/plan.md) | The user types `/frame:plan <idea>`: grill, to-spec, to-tickets, then to-mason if the project uses it |

`explore` reads the repo, labels current choices as choices, and proposes at least one
option that leaves a prior choice. It does not edit files. It does not run on its own.
It is not part of `/frame:plan`.

`grill`, `to-spec` and `to-tickets` turn an idea into a feature spec and self-contained
tickets, one confirmed step at a time, and know nothing of any development system.
`to-mason` then applies mason's labels, adds the feature-test Ticket and releases the work.
`/frame:plan` chains them. Every skill here runs only when typed.

`implement` builds an issue and its sub-issues: one commit per ticket on a feature branch and
one pull request that a person merges. With several tickets it delegates the code to
sub-agents, on a less costly model for routine ones when the host allows it, reviews each
diff and runs the ticket's tests before merging it. The whole suite runs before the first
ticket, to know what already fails, and again at the end. It never weakens or skips a test to
get it to pass, and stops after two CI fixes that leave a check red. Run again, it resumes
the earlier work. It assigns the issues, ticks the verified acceptance criteria, moves the
project status when there is one, and comments only for a blocker or a deviation. It treats
as specification only what owners, members and collaborators of the repository wrote.

Each run of `ship` or `implement` ends with one report comment on the issue: time and tokens
by step and by agent, then the notable difficulties, in the fixed format of
[METRICS.md](feature-planning/METRICS.md). Token counts come from
[scripts/tokens.py](scripts/tokens.py), a quick solution that reads Claude Code's local session
journals (needs `python3`); elsewhere, or if it fails, they are `n/a`. Only the counts are posted.

Shared rules, review gates and tracker contracts are in
[feature-planning/](feature-planning/): [CONVENTIONS.md](feature-planning/CONVENTIONS.md),
[REVIEW.md](feature-planning/REVIEW.md), [contracts/](feature-planning/contracts/).
