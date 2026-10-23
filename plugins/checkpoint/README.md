# checkpoint

```
/plugin install checkpoint --marketplace tilap/pinkpuma-tilap
```

Pause in-progress work and pick it up in another session. Install it in the project
where the work lives.

## Skills

| Skill                              | Use when                               |
| ---------------------------------- | -------------------------------------- |
| [handoff](skills/handoff/SKILL.md) | The user invokes `/checkpoint:handoff` |
| [resume](skills/resume/SKILL.md)   | The user invokes `/checkpoint:resume`  |

`handoff` writes the in-progress, uncommitted work of the session to
`.agent/handoffs/` in the project, so another session can pick it up cold. `resume`
loads the latest one, or rebuilds the state from git when none exists. Neither runs
on its own.
