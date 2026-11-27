# Feature-test ticket

The last ticket of a feature, blocked by **every** other ticket. Body:

```markdown
## Context

The feature tests of this feature. They prove, once, on the assembled feature, what the
scenarios below say it does. The feature is built when this ticket runs.

## What to build

Tests for the scenarios below, each at the level the scenario names (a service, a route, a
page), and nothing else.

## Scenarios

<The specification's acceptance scenarios, copied verbatim, with their ids S1, S2, …>

<Scenarios left out, with the reason, when the specification names any.>

<When a scenario signs in: a test account exists for it.>

## Done when

- [ ] Each scenario above has at least one test whose name contains its id.
- [ ] Only tests were changed.
- [ ] The tests pass against the built feature.

## Constraints

- Write tests only; update an existing test only where a scenario above changes it.
- Do not touch application code.
- Run the tests against the built feature as you go.
- A test that fails because the feature does not do what its scenario says is not fixed by
  weakening the test or changing the application: stop and say what the feature does
  instead.

## If unsure

Stop and say what is unclear or what the repository lacks (a test account, say). Do not
choose an interpretation.

## Out of scope

- Everything that is not a test.
```
