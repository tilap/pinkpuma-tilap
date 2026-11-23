# Issue format

The format of the issue when the repository has no usable template, and the content rules
for every issue this skill files. The repository's own template, title prefix, labels and
language win over everything here.

## Title

`<area>: <symptom in one sentence>`. The area is the part of the system where the problem
shows (a screen, a feature, an endpoint, an export, a job), taken from the report and the
repository. The symptom says what is wrong, not what to do about it.

```text
Checkout: total differs from the cart
Export: CSV dates are shifted by one day
Auth: session expires after a few minutes
```

## Body

```markdown
## Observation

What was noticed, restated cleanly.

## Expected

What should happen. Marked "to be confirmed" when it is a guess.

## Context

Where it was noticed: feature, flow, endpoint, export, job, environment, device or
version, steps. Only what the user gave; the rest is "not provided".

## Evidence

Logs, data samples, file names, links, screenshots. Left out when there is none.

## Original report

> The user's words, verbatim, in the language they spoke.
```

## Content rules

- Restate the meaning faithfully. Do not add a cause, a fix, a priority or a severity.
- Never invent a fact. An unknown field is "not provided". A guess is written as one:
  "suspected: ...".
- A report with no proof is still a report. Write the observation as a suspicion and leave
  Evidence out. Do not ask for proof.
- Text evidence the user gave (a log, a data sample) goes in a fenced block, in full.
- Images cannot be uploaded by `gh`. List them under Evidence as "to attach: <file name>"
  and tell the user in the reply.
- Original report: the user's own words, not translated, not corrected. It is added to the
  end of the body under every template, so the report can be requalified from what was
  really said.
- Write the headings, the title and the body in English, unless the repository says
  otherwise (see the first section of SKILL.md).
