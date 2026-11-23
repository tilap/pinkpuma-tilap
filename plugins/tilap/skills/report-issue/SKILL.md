---
name: report-issue
description: >-
  Turn a quick, rough problem report (a bug, a wrong export, a hunch) into a
  well-formed GitHub issue on the right repository, in the repository's own
  template and language, labelled needs-triage. Use only when the user invokes
  /tilap:report-issue.
disable-model-invocation: true
metadata:
  plugin: tilap
---

# Report issue

The owner notices a problem and wants it captured now, before it is forgotten. They
describe it loosely, in any language. This skill restates it as a clean issue, files it
with `gh`, and returns the link. It is a report from someone who noticed something, not a
qualified ticket: no priority, no fix, no investigation.

## The repository wins

Write in English unless the repository says otherwise. Everything the repository already
defines wins over this skill's defaults: its issue template, title prefix, labels, issue
type and language. If the template is written in another language (or, with no template,
the five latest issue titles are), write the issue in that language.

## Tools

`gh`, authenticated. If it is missing or not authenticated, print the drafted issue, say
why it was not filed, and stop. Never create a repository. Use `--repo OWNER/REPO` on every
`gh` call, so the result never depends on the current directory.

## Steps

### 1. Read the report

The report is what the user wrote with the invocation. It may be vague, partly guessed, or
have no proof. That is a valid report. Ask at most one question, and only when:

- you cannot tell what the report is about, or
- the repository cannot be determined (step 2).

Never ask about severity, steps, version, evidence or expected behaviour. A missing
detail is written as "not provided", not asked for.

### 2. Resolve the repository

Take the first rule that gives one repository:

1. The user names one: match it by name or alias in [repos.md](references/repos.md), or
   take it as is when it is written `owner/repo`.
2. The current directory is a git repository: `gh repo view --json nameWithOwner,isFork`.
   For a fork, ask which of the fork and its parent gets the issue.
3. The subject matches a project or alias in [repos.md](references/repos.md).
4. Several repositories are equally plausible (a session with several folders): ask one
   question naming the two or three candidates.
5. Nothing matches: use the `Inbox` repository of [repos.md](references/repos.md). If none
   is set, print the drafted issue and ask where it goes.

### 3. Use the repository's template

List the templates on the default branch:

```bash
gh api repos/OWNER/REPO/contents/.github/ISSUE_TEMPLATE --jq '.[].name'
```

Also check `.github/ISSUE_TEMPLATE.md`. `config.yml` is not a template. A 404 (no such
folder, or an empty repository) means there is no template. Read the chosen
file with `-H "Accept: application/vnd.github.raw+json"` on the same `contents` path.
Pick the template closest to a problem report.

- Markdown template: follow its structure and section order exactly.
- YAML form: one `### <label>` section per field, in order, the value under it, and
  `_No response_` for a field you cannot fill.
- Take its title prefix, labels and issue type. Add nothing it does not declare, except the
  label of step 5.

If no template is about problems, or most required fields cannot be filled from the
report, use the format of [issue-format.md](references/issue-format.md) instead. Do not
ask. Say in the reply which template was not used and why. With no template at all, use
that format without comment.

### 4. Draft

Follow [issue-format.md](references/issue-format.md) for the content rules, the title and
the closing "Original report" section. That section is always added, also under a
repository template.

### 5. Label

The label is `needs-triage`: reported, not qualified, not prioritized. List the labels
first (`gh label list --repo OWNER/REPO --limit 200 --json name --jq '.[].name'`). If the
repository already has a label with the same meaning, use that one. If it has none, create
it:

```bash
gh label create needs-triage --repo OWNER/REPO --color ededed \
  --description "Reported, not yet qualified or prioritized"
```

Add the labels the template declares. Add no other label.

### 6. File

Write the body to a unique temporary file, so newlines and quotes survive, then:

```bash
gh issue create --repo OWNER/REPO --title "<title>" --body-file "$body_file" \
  --label needs-triage
```

One `--label` per label. Pass `--type` only when the template declares an issue type;
if `gh` rejects it, file without it and say so. Remove the temporary file afterwards.

There is no preview and no confirmation, whether the repository is public or private.
Filing what the user said is the purpose of this skill, and what they say is theirs to
watch.

### 7. Reply

The issue link as a Markdown link, and one line saying what it reports. Then only what
the user needs to act on or know:

- images to attach by hand (`gh` cannot upload them), by file name;
- a template that was not used, and why;
- the repository, when it was not the one they named or the current one;
- a label that was created.

No recap of the issue body.
