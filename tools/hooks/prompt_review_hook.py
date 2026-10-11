"""Claude Code PostToolUse hook: after a video prompt is written, lint it and ask for /fk-review-prompt.

Triggers on:
  - Write / Edit of a prompt JSON file (path contains "prompt" and ends with .json)
  - Bash commands that POST / PATCH /api/scenes with a video_prompt
    (lints every scene whose video_prompt changed in the last few minutes)

Never blocks: it only injects context so Claude runs the review (Lesson 86).
"""

import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(ROOT / "tools"))

RECENT = timedelta(minutes=5)
PROMPT_FILE = re.compile(r"prompt[^/\\]*\.json$", re.IGNORECASE)


def lint_summary(prompt: str) -> str:
    from lint_prompt import lint_prompt
    issues = lint_prompt(prompt)
    if not issues:
        return "linter: 0 issues"
    counts = {}
    for i in issues:
        counts[i["severity"]] = counts.get(i["severity"], 0) + 1
    head = ", ".join(f"{n} {s}" for s, n in sorted(counts.items()))
    detail = "; ".join(f"[{i['severity']}] {i['type']}" for i in issues[:6])
    return f"linter: {head} — {detail}"


def recent_scene_prompts():
    db = ROOT / "flow_agent.db"
    if not db.exists():
        return []
    cutoff = datetime.now(timezone.utc) - RECENT
    out = []
    with sqlite3.connect(db) as conn:
        for sid, updated, prompt in conn.execute(
                "SELECT id, updated_at, video_prompt FROM scene WHERE video_prompt IS NOT NULL "
                "ORDER BY updated_at DESC LIMIT 20"):
            try:
                ts = datetime.fromisoformat(str(updated).replace("Z", "+00:00").replace(" ", "T"))
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
            except ValueError:
                continue
            if ts >= cutoff:
                out.append((sid, prompt))
    return out


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    tool = data.get("tool_name", "")
    tin = data.get("tool_input", {}) or {}
    targets = []  # (label, prompt text)

    if tool in ("Write", "Edit"):
        path = tin.get("file_path", "")
        if PROMPT_FILE.search(path) and Path(path).is_file():
            targets.append((path, Path(path).read_text(encoding="utf-8", errors="replace")))
    elif tool == "Bash":
        cmd = tin.get("command", "")
        # Only real calls to the FlowKit server (docs edits that merely mention the endpoint don't count)
        if ":8100" in cmd and "/api/scenes" in cmd and "video_prompt" in cmd:
            targets = [(f"scene {sid}", p) for sid, p in recent_scene_prompts()]

    if not targets:
        return

    lines = [f"- {label}: {lint_summary(text)}" for label, text in targets]
    context = (
        "PROMPT REVIEW REQUIRED (Lesson 86): a video_prompt was just written or changed.\n"
        + "\n".join(lines)
        + "\nBefore showing this prompt to the user or asking to generate, run /fk-review-prompt on it: "
          "re-read the WHOLE prompt, tabulate every statement per subject (speed, direction, on-screen position by second, "
          "hands/mouth, camera fixed vs shaking), run checklist B, and attach the self-review report."
    )
    print(json.dumps({
        "systemMessage": "Prompt review hook: " + " | ".join(lines),
        "hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": context},
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
