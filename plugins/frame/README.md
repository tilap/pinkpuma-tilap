# frame

```
/plugin install frame --marketplace tilap/pinkpuma-tilap
```

Frame one feature: open the options, settle the decisions, then publish the spec and the
tickets. Install it in the project where the feature will be built.

## Skills

| Skill                                    | Use when                             |
| ---------------------------------------- | ------------------------------------ |
| [explore](skills/explore/SKILL.md)       | The user invokes `/frame:explore`    |
| [grill](skills/grill/SKILL.md)           | The user invokes `/frame:grill`      |
| [to-spec](skills/to-spec/SKILL.md)       | The user invokes `/frame:to-spec`    |
| [to-tickets](skills/to-tickets/SKILL.md) | The user invokes `/frame:to-tickets` |
| [to-mason](skills/to-mason/SKILL.md)     | The user invokes `/frame:to-mason`   |

| Command                  | Use when                                                                                              |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| [plan](commands/plan.md) | The user types `/frame:plan <idea>`: grill, to-spec, to-tickets, then to-mason if the project uses it |

`explore` reads the repo, labels current choices as choices, and proposes at least one
option that leaves a prior choice. It does not edit files. It does not run on its own.
It is not part of `/frame:plan`.

`grill`, `to-spec` and `to-tickets` turn an idea into a feature spec and self-contained
tickets, one confirmed step at a time, and know nothing of any development system.
`to-mason` then applies mason's labels, adds the e2e Ticket and releases the work.
`/frame:plan` chains them. They run only when typed.
Their shared rules, review gates and tracker contracts are in
[feature-planning/](feature-planning/): [CONVENTIONS.md](feature-planning/CONVENTIONS.md),
[REVIEW.md](feature-planning/REVIEW.md), [contracts/](feature-planning/contracts/).
