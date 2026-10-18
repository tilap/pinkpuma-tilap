# session-notes

```
/plugin install session-notes --marketplace tilap/pinkpuma-tilap
```

Record the current coding session as one dev note. The plugin ships the skill and the
MCP client. Install it in the project where the work happened, not in the site that
stores the notes.

## Skill

| Skill                                        | Use when                                                                  |
| -------------------------------------------- | ------------------------------------------------------------------------- |
| [session-note](skills/session-note/SKILL.md) | The user asks to keep this session, or runs `/session-notes:session-note` |

The skill writes one note (`log`, `recipe`, `pitfall`, or `decision`) through `capture_note`
and stops. The same `sessionKey` updates that note. It does not create a file.

## MCP client

The client is the `notes` server: Streamable HTTP, `Authorization: Bearer <token>`.
The URL is the notes endpoint (`https://<host>/api/notes/mcp`). The token is an `omk_`
token with full access, created in the site back-office. Neither value is stored in this
plugin.

| Host        | Where the person sets the URL and the token                    | Config file |
| ----------- | -------------------------------------------------------------- | ----------- |
| Claude Code | The plugin's configuration dialog (`notes_url`, `notes_token`) | `.mcp.json` |
| Cursor      | Plugins → Configure (`NOTES_URL`, `NOTES_TOKEN`)               | `mcp.json`  |

A `read_only` token can search and read. Capturing a note needs `full_access`.
