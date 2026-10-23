---
name: explore
description: >-
  Explore options for one precise problem, including at least one option that
  leaves a current repo choice. Use only when the user invokes /frame:explore or
  /explore.
disable-model-invocation: true
metadata:
  plugin: frame
---

# Explore

This turn is idea exploration for one precise problem. Widen the solution space.
Do not edit files. Do not implement.

## Stance

- Read the repo and state what it does today. Label those as current choices, not
  requirements.
- Keep the choices that still serve the problem. Also propose at least one option
  that drops a prior choice, and say what that choice was protecting.
- When a project rule or AGENTS.md conflicts with an option, name the conflict and
  keep the option. Do not silently conform. Safety rules and the user's own
  preferences still apply.
- Treat training knowledge as a hypothesis. Check the code, and current docs for
  any library or API, before recommending a pattern. If you cannot check, say what
  is unverified and how stale it might be.

## Answer

1. The problem, in one sentence.
2. Current choices in the repo that touch it.
3. Two or three options. At least one stays inside those choices. At least one
   leaves one of them.
4. For each option: what it costs, what it assumes, and what still needs a fresh
   check.
