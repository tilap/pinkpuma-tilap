#!/usr/bin/env python3
"""Token counts of one run, for the run report (see ../feature-planning/METRICS.md).

QUICK SOLUTION. It reads the session journals Claude Code keeps on this machine. Their
format is internal to Claude Code and may change in any release; requests the journals
give no usage for are not counted. At worst it answers "unavailable" and the report says
n/a: it only reads, and always exits 0. A supported source (OpenTelemetry) is the way to
better numbers, if they turn out to be worth it.

Usage:
  python3 tokens.py --step preflight=<time> [--step build=<time> ...] --end <time>
                    [--session <id>]

Times are ISO 8601 with a zone (`date -u +%Y-%m-%dT%H:%M:%SZ`). A sub-agent is recognised
by a line `[frame:<agent> <ticket> <attempt>]` in what it was sent; one without it counts
in the orchestrator row of the step it ran in.

Standard library only, Python 3.9 or later.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

STEPS = ["preflight", "planning", "build", "verification", "delivery"]
AGENT_STEP = {
    "plan-reviewer": "planning",
    "developer": "build",
    "final-reviewer": "verification",
}
LABEL = re.compile(
    r"^\s*\[frame:(plan-reviewer|developer|final-reviewer) (#\d+|-) (\d+)\]", re.M
)
FIELDS = {
    "input": "input_tokens",
    "cache_write": "cache_creation_input_tokens",
    "cache_read": "cache_read_input_tokens",
    "output": "output_tokens",
}


def to_time(text):
    try:
        time = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        time = None
    if time is None or time.tzinfo is None:
        raise ValueError(f'invalid time "{text}"')
    return time.timestamp()


def parse_args(argv):
    steps, end = [], None
    session = os.environ.get("CLAUDE_CODE_SESSION_ID")
    for index in range(0, len(argv), 2):
        flag = argv[index]
        value = argv[index + 1] if index + 1 < len(argv) else ""
        if flag == "--step":
            name, _, time = value.partition("=")
            if name not in STEPS:
                raise ValueError(f'unknown step "{name}"')
            steps.append((to_time(time), name))
        elif flag == "--end":
            end = to_time(value)
        elif flag == "--session":
            session = value
        else:
            raise ValueError(f'unknown argument "{flag}"')
    if not steps or end is None:
        raise ValueError("--step and --end are required")
    if not session:
        raise ValueError("no session id: not a Claude Code session")
    if not re.fullmatch(r"[\w-]+", session):
        raise ValueError("invalid session id")
    return sorted(steps), end, session


def find_session(session):
    root = os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude"
    for project in (Path(root) / "projects").iterdir():
        journal = project / f"{session}.jsonl"
        if journal.exists():
            return journal, sorted((project / session / "subagents").glob("*.jsonl"))
    raise ValueError("session journal not found")


def read_lines(path):
    with open(path, encoding="utf-8", errors="replace") as journal:
        for line in journal:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue  # empty, or being written


def text_of(content):
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "\n".join(b.get("text", "") for b in content if b.get("type") == "text")


def requests_of(path):
    """One entry per model request: a request spans several lines repeating its usage."""
    requests, label = {}, None
    for line in read_lines(path):
        message = line.get("message")
        if not isinstance(message, dict):
            continue
        if line.get("type") == "user":
            found = LABEL.search(text_of(message.get("content")))
            if found:
                label = (found[1], found[2], int(found[3]))
        if line.get("type") != "assistant":
            continue
        key, usage = message.get("id"), message.get("usage")
        if not key or not usage:
            continue
        time = requests[key][0] if key in requests else to_time(line["timestamp"])
        requests[key] = (time, usage, message.get("model"), label)
    return requests.values()


def collect(steps, end, session):
    journal, subagents = find_session(session)
    rows = {}
    for path in [journal, *subagents]:
        for time, usage, model, label in requests_of(path):
            if not steps[0][0] <= time <= end:
                continue
            if label and path != journal:
                agent, ticket, attempt = label
                step = AGENT_STEP[agent]
            else:
                agent, ticket, attempt = "orchestrator", "-", 1
                step = [name for start, name in steps if start <= time][-1]
            key = (step, agent, ticket, attempt)
            if key not in rows:
                rows[key] = {"models": [], **{column: 0 for column in FIELDS}}
            row = rows[key]
            if model and model not in row["models"]:
                row["models"].append(model)
            for column, field in FIELDS.items():
                count = usage.get(field)
                if row[column] == "n/a" or not isinstance(count, int):
                    row[column] = "n/a"
                else:
                    row[column] += count
    if not rows:
        raise ValueError("no usage found for this run")

    def order(key):
        step, agent, ticket, attempt = key
        return (
            STEPS.index(step),
            agent != "orchestrator",
            int(ticket[1:] or 0),
            attempt,
        )

    return [
        {
            "step": key[0],
            "agent": key[1],
            "ticket": key[2],
            "attempt": key[3],
            "model": "+".join(rows[key]["models"]) or "n/a",
            **{column: rows[key][column] for column in FIELDS},
        }
        for key in sorted(rows, key=order)
    ]


def main():
    try:
        rows = collect(*parse_args(sys.argv[1:]))
        report = {"available": True, "tool": "claude-code", "rows": rows}
    except Exception as error:  # measuring never fails a run
        report = {"available": False, "reason": str(error)}
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
