---
description: Review the oldest entries of the knowledge base against official sources and propose updates for approval.
argument-hint: "[slug | stack | --older-than <days>]"
disable-model-invocation: true
---

# Review the knowledge base

Run the knowledge review on these arguments: $ARGUMENTS

With no argument, review the oldest active entries not verified for 90 days.

The skill is written to run when a person asks for it, so run it by reading
[skills/knowledge-review/SKILL.md](${CLAUDE_PLUGIN_ROOT}/skills/knowledge-review/SKILL.md) and
following it exactly as written, not by calling it by name. Its approvals still apply: this
command approves nothing for the owner.
