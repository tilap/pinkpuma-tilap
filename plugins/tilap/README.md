# tilap

```
/plugin install tilap --marketplace tilap/pinkpuma-tilap
```

Personal daily skills. Install it in the project where the work happened, not in the
site that stores the notes.

## Skills

| Skill                                        | Use when                               |
| -------------------------------------------- | -------------------------------------- |
| [explore](skills/explore/SKILL.md)           | The user invokes `/tilap:explore`      |
| [session-note](skills/session-note/SKILL.md) | The user invokes `/tilap:session-note` |
| [knowledge](skills/knowledge/SKILL.md)       | The user invokes `/tilap:knowledge`    |
| [knowledge-search](skills/knowledge-search/SKILL.md) | Before designing or implementing a topic |
| [handoff](skills/handoff/SKILL.md)           | The user invokes `/tilap:handoff`      |
| [resume](skills/resume/SKILL.md)             | The user invokes `/tilap:resume`       |
| [grill](skills/grill/SKILL.md)               | The user invokes `/tilap:grill`        |
| [to-spec](skills/to-spec/SKILL.md)           | The user invokes `/tilap:to-spec`      |
| [to-tickets](skills/to-tickets/SKILL.md)     | The user invokes `/tilap:to-tickets`   |
| [to-mason](skills/to-mason/SKILL.md)         | The user invokes `/tilap:to-mason`     |

| Command                    | Use when                                                  |
| -------------------------- | --------------------------------------------------------- |
| [plan](commands/plan.md)   | The user types `/tilap:plan <idea>`: grill, to-spec, to-tickets, then to-mason if the project uses it |

`explore` reads the repo, labels current choices as choices, and proposes at least one
option that leaves a prior choice. It does not edit files. It does not run on its own.

`session-note` runs only when invoked. It writes one note (`log`, `recipe`, `pitfall`, or `decision`) through
`create_session_note` and stops. The kind is the first tag, because the server has no
kind field. The same chat updates that note with `update_session_note`. It does not
create a file.

`knowledge` runs only when invoked. It checks the index with `list_knowledge`, then writes one
entry (`create_knowledge`, or `update_knowledge` when one already covers the decision). New
entries stay `draft` until the user approves activating them.

`knowledge-search` is the only skill that runs on its own. Before a design or implementation
topic it calls `list_knowledge` then `get_knowledge`, applies the matching entries as the
default, and flags a deviation instead of forcing the rule. It is read-only.

`handoff` writes the in-progress, uncommitted work of the session to
`.agent/handoffs/` in the project, so another session can pick it up cold; `resume` loads the
latest one, or rebuilds the state from git when none exists. Neither runs on its own.

`grill`, `to-spec` and `to-tickets` turn an idea into a feature spec and self-contained
tickets, one confirmed step at a time, and know nothing of any development system.
`to-mason` then applies mason's labels, adds the e2e Ticket and releases the work.
`/tilap:plan` chains them. They run only when typed.
Their shared rules, review gates and tracker contracts are in
[feature-planning/](feature-planning/): [CONVENTIONS.md](feature-planning/CONVENTIONS.md),
[REVIEW.md](feature-planning/REVIEW.md), [contracts/](feature-planning/contracts/).

## MCP client

The client is the `notes` server: Streamable HTTP, `Authorization: Bearer <token>`.
The URL is the site MCP endpoint (`https://<host>/api/mcp`). The token is an `omk_`
token with full access, created in the site back-office. Neither value is stored in this
plugin.

| Host        | Where the person sets the URL and the token                    | Config file |
| ----------- | -------------------------------------------------------------- | ----------- |
| Claude Code | The plugin's configuration dialog (`notes_url`, `notes_token`) | `.mcp.json` |
| Cursor      | Plugins → Configure (`NOTES_URL`, `NOTES_TOKEN`)               | `mcp.json`  |

A `read_only` token can search and read. Capturing a note needs `full_access`.
