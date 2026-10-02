"""Prompt Linter for FlowKit — Enforces Optical Viewpoint, Anti-Ghost Device, Body Lock & Physics Rules."""

import re
import sys
import argparse
import sqlite3
import json

sys.stdout.reconfigure(encoding='utf-8')

FORBIDDEN_GHOST_DEVICE_PATTERNS = [
    (r"\b(phone|smartphone)\b", "FORBIDDEN: Mentioning 'phone' or 'smartphone' causes AI to render a 3D phone device in hand and switches camera to 3rd-person spectator."),
    (r"\b(selfie[- ]?stick)\b", "FORBIDDEN: Mentioning 'selfie stick' renders a physical stick in the shot."),
    (r"\b(device)\b", "FORBIDDEN: Mentioning 'device' causes AI to render gadgets or screens."),
    (r"(?<!off-)\bscreen\b", "FORBIDDEN: Mentioning 'screen' (except 'off-screen') may cause AI to render a phone or monitor screen. Use 'in the frame' instead."),
    (r"\bnegative:\b", "FORBIDDEN: 'Negative:' lines are banned by repo rules. Use plain constraint sentences in prompt body."),
]

def lint_prompt(prompt: str) -> list[dict]:
    """Check prompt against FlowKit rules. Returns list of issues/warnings."""
    issues = []
    p_lower = prompt.lower()

    # 1. Check Ghost Device patterns
    for pat, msg in FORBIDDEN_GHOST_DEVICE_PATTERNS:
        matches = list(re.finditer(pat, p_lower))
        if matches:
            for m in matches:
                issues.append({
                    "severity": "CRITICAL",
                    "type": "GHOST_DEVICE",
                    "token": m.group(0),
                    "position": m.start(),
                    "message": msg
                })

    # 2. Check Optical Viewpoint: If selfie/front lens, check if off-screen constraint exists
    if "selfie" in p_lower or "front-lens" in p_lower or "vlog" in p_lower:
        if not ("off-screen" in p_lower or "outside the visible frame" in p_lower or "outside the frame" in p_lower):
            issues.append({
                "severity": "HIGH",
                "type": "OPTICAL_VIEWPOINT",
                "message": "Selfie shot is missing explicit camera blind-spot constraint: 'the camera lens itself and her right gripping hand are completely outside the visible frame and never seen'."
            })
        if not ("empty" in p_lower and "hand" in p_lower):
            issues.append({
                "severity": "MEDIUM",
                "type": "FREE_HAND_CONSTRAINT",
                "message": "Selfie shot should specify that the free hand is completely empty ('her free left hand is completely empty and flails naturally')."
            })

    # 3. Check Body Lock Early Conditioning
    if "body lock" in p_lower:
        pos_body_lock = p_lower.find("body lock")
        # Check if 0-2s or 0-3s appears before BODY LOCK
        m_timed = re.search(r"\b0-[1-3]s:", p_lower)
        if m_timed and m_timed.start() < pos_body_lock:
            issues.append({
                "severity": "HIGH",
                "type": "BODY_LOCK_POSITION",
                "message": "BODY LOCK is placed AFTER timed action segments (0-2s/0-3s). Rule 39 requires BODY LOCK placed EARLY right after Shot: before timed segments to prevent attention decay."
            })

    return issues


def clean_prompt_of_ghost_devices(prompt: str) -> str:
    """Automatically cleans ghost device keywords from a prompt."""
    cleaned = prompt
    # Replace common patterns
    cleaned = re.sub(r"\bnever drops the phone\b", "never drops the camera", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bnever drops, releases, or lets go of the phone\b", "never drops, releases, or lets go of the camera", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bsmartphone footage\b", "handheld footage", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\braw unstabilized smartphone footage\b", "raw unstabilized footage", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bnatural smartphone perspective\b", "natural wide-angle handheld perspective", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bphone\b", "camera", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bsmartphone\b", "camera", cleaned, flags=re.IGNORECASE)
    return cleaned


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint video prompts for FlowKit rules")
    parser.add_argument("prompt", nargs="?", help="Prompt string to lint")
    parser.add_argument("--scene", help="Scene ID from DB to lint")
    parser.add_argument("--auto-fix", action="store_true", help="Auto-fix ghost device tokens in DB scene")
    args = parser.parse_args()

    prompt_to_check = args.prompt
    if args.scene:
        conn = sqlite3.connect("flow_agent.db")
        row = conn.execute("SELECT video_prompt FROM scene WHERE id = ?", (args.scene,)).fetchone()
        if not row or not row[0]:
            print(f"Scene {args.scene} not found or has no video_prompt.")
            sys.exit(1)
        prompt_to_check = row[0]

    if not prompt_to_check:
        print("Usage: python tools/lint_prompt.py \"<prompt>\" OR --scene <scene_id>")
        sys.exit(0)

    issues = lint_prompt(prompt_to_check)
    if not issues:
        print("✅ PROMPT LINT PASSED! No ghost devices or viewpoint issues found.")
    else:
        print(f"⚠️ FOUND {len(issues)} ISSUES:")
        for idx, iss in enumerate(issues, 1):
            print(f"  [{idx}] [{iss['severity']}] {iss['type']}: {iss['message']}")

        if args.auto_fix and args.scene:
            fixed = clean_prompt_of_ghost_devices(prompt_to_check)
            conn = sqlite3.connect("flow_agent.db")
            conn.execute("UPDATE scene SET video_prompt = ? WHERE id = ?", (fixed, args.scene))
            conn.commit()
            print("\n✨ Auto-fixed prompt saved to DB!")
