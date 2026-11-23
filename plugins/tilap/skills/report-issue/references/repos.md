# Repositories

Where the `report-issue` skill files an issue when the current directory does not decide it.
One row per repository. A project may have several names: put the ones the owner says in
"Also called", separated by commas.

| Project           | Repository                 | Also called |
| ----------------- | -------------------------- | ----------- |
| pinkpuma-toolbelt | tilap/pinkpuma-toolbelt    |             |
| pinkpuma-tilap    | tilap/pinkpuma-tilap       |             |
| agent-deck        | tilap/agent-deck           |             |

## Inbox

Repository for reports that match no project: `tilap/agent-workspace` (private). The
owner's reports wait there under `needs-triage`; agents use their own labels. Once a report
is qualified, `gh issue transfer` moves it to the project's repository. The skill never
creates this repository.
