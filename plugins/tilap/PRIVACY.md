# Privacy policy: tilap plugin

The plugin is a set of skills, one command and an MCP client configuration. It has no
telemetry and no analytics. Its skills send data only to the destinations below.

## What is sent, and where

| Destination                                              | What is sent                                                                                                                                       | When                                                                                                                           |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| The `tilap-data` server at the URL you set               | Your API token, search terms, knowledge entries, expressions and their translations, and any other call your assistant makes to the server's tools | `knowledge-search` runs on its own before a design or implementation task; the rest runs when you invoke a skill or ask for it |
| GitHub, through your authenticated `gh` client           | The issue written from your report, with your words verbatim                                                                                       | `/tilap:report-issue`, without a preview. An issue in a public repository is public                                            |
| GitHub, through your authenticated `gh` client and `git` | Branches, commits, a pull request, and issue updates: assignee, checkboxes, project status, blocker comments                                       | `/tilap:implement-github-issue`, without a confirmation. What goes to a public repository is public                            |
| Official documentation sites                             | Web searches and page requests on the topics of the entries under review                                                                           | `/tilap:knowledge-review`                                                                                                      |

## Storage

The server URL and the token are stored by the host (Claude Code or Cursor) in the plugin
configuration, not in the plugin. What the server keeps, and for how long, is decided by
whoever operates the URL you set. The host and its model provider process the conversation
under their own privacy policies.

## Contact

Open an issue on [tilap/pinkpuma-tilap](https://github.com/tilap/pinkpuma-tilap/issues).
