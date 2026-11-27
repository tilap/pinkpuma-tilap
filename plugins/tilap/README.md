# tilap

```
/plugin install tilap --marketplace tilap/pinkpuma-tilap
```

A knowledge base of proven dev practices, a private glossary of foreign-language
expressions, and GitHub issues to report. Install it in the project where the
work happens, not in the site that stores the knowledge base.

## Skills

| Skill                                                | Use when                                   |
| ---------------------------------------------------- | ------------------------------------------ |
| [knowledge](skills/knowledge/SKILL.md)               | The user invokes `/tilap:knowledge`        |
| [knowledge-search](skills/knowledge-search/SKILL.md) | Before designing or implementing a topic   |
| [knowledge-review](skills/knowledge-review/SKILL.md) | The user invokes `/tilap:knowledge-review` |
| [lang](skills/lang/SKILL.md)                         | The user invokes `/tilap:lang`             |
| [report-issue](skills/report-issue/SKILL.md)         | The user invokes `/tilap:report-issue`     |

`knowledge` runs only when invoked. It checks the index with `list_knowledge`, then writes one
entry (`create_knowledge`, or `update_knowledge` when one already covers the decision). New
entries stay `draft` until the user approves activating them.

`knowledge-search` is the only skill that runs on its own. Before a design or implementation
topic it calls `list_knowledge` then `get_knowledge`, applies the matching entries as the
default, and flags a deviation instead of forcing the rule. It is read-only.

`knowledge-review` runs only when invoked. It takes the oldest `active` entries not verified for 90 days
(`list_knowledge` with `notVerifiedSinceDays`, at most 5 per run), checks their facts against official sources,
and reports each as `current`, `needs-update` or `deprecate` with a source link per claim. A claim without a
source is listed as unverified, never proposed. Nothing is written before the owner approves that entry; then
`update_knowledge` sets the changes, `verifiedAt` and `status: active`. `/tilap:knowledge-review [slug | stack |
--older-than <days>]` is the entry point. It does not create entries: gaps are only listed.

`lang` runs only when invoked. It checks `list_expressions`, then stores one phrase
and its French translation with `create_expression` (or `update_expression` when that
phrase is already there). It does not create a file.

`report-issue` runs only when invoked. It turns a rough problem report (a bug, a wrong export, a hunch) into a
GitHub issue and returns the link. It resolves the repository (the one named, the current directory's, or a
project in [repos.md](skills/report-issue/references/repos.md)), follows that repository's issue template, title
prefix, labels and language when it has them, and writes in English otherwise. Under every template it adds an
"Original report" section with the user's words, and it labels the issue `needs-triage`. It asks a question only
when it cannot tell what the report is about or where it goes, does not preview or confirm, and needs `gh`
authenticated. It does not use the tilap-data MCP.

## MCP client

The client is the `tilap-data` server: Streamable HTTP, `Authorization: Bearer <token>`.
The URL is the site MCP endpoint (`https://<host>/api/mcp`). The token is an `omk_`
token with full access, created in the site back-office. Neither value is stored in this
plugin.

| Host        | Where the person sets the URL and the token                    | Config file |
| ----------- | -------------------------------------------------------------- | ----------- |
| Claude Code | The plugin's configuration dialog (`notes_url`, `notes_token`) | `.mcp.json` |
| Cursor      | Plugins → Configure (`NOTES_URL`, `NOTES_TOKEN`)               | `mcp.json`  |

A `read_only` token can search and read. Storing an entry or an expression needs `full_access`.

## Privacy

See the [privacy policy](PRIVACY.md): what the plugin sends, and where.
