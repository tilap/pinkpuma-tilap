# tilap

```
/plugin install tilap --marketplace tilap/pinkpuma-tilap
```

Session notes, a knowledge base of proven dev practices, and a private glossary of
foreign-language expressions. Install it in the project where the work happened, not in
the site that stores them.

## Skills

| Skill                                                | Use when                                 |
| ---------------------------------------------------- | ---------------------------------------- |
| [session-note](skills/session-note/SKILL.md)         | The user invokes `/tilap:session-note`   |
| [knowledge](skills/knowledge/SKILL.md)               | The user invokes `/tilap:knowledge`      |
| [knowledge-search](skills/knowledge-search/SKILL.md) | Before designing or implementing a topic |
| [lang](skills/lang/SKILL.md)                         | The user invokes `/tilap:lang`           |

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

`lang` runs only when invoked. It checks `list_expressions`, then stores one phrase
and its French translation with `create_expression` (or `update_expression` when that
phrase is already there). It does not create a file.

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
