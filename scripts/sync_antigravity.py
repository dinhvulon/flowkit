#!/usr/bin/env python3
"""Flow Kit — Sync Skills for Google Antigravity (AGY) IDE

Converts skills/fk-*.md into .agents/skills/fk-*/SKILL.md with YAML frontmatter
so that Antigravity IDE recognizes them as native slash commands and on-demand skills.

Usage:
    python scripts/sync_antigravity.py          # Generate/sync .agents/skills/
    python scripts/sync_antigravity.py --clean  # Remove generated .agents/skills/
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
AGENTS_SKILLS_DIR = REPO_ROOT / ".agents" / "skills"
GLOBAL_SKILLS_DIR = Path.home() / ".gemini" / "config" / "skills"


def discover_skills():
    """Scan skills/fk-*.md and extract name + description + content."""
    if not SKILLS_DIR.exists():
        print(f"ERROR: skills/ directory not found at {SKILLS_DIR}", file=sys.stderr)
        return []

    skills = []
    for f in sorted(SKILLS_DIR.glob("fk-*.md")):
        skill_id = f.stem  # e.g. "fk-time-travel-vlog"
        raw_text = f.read_text(encoding="utf-8")
        lines = raw_text.splitlines()

        # Extract description from the first non-empty heading or line
        description = skill_id
        for line in lines:
            line_str = line.strip()
            if line_str.startswith("#"):
                clean_title = line_str.lstrip("#").strip()
                description = clean_title
                break
            elif line_str and not line_str.startswith("<!--"):
                description = line_str
                break

        # Sanitize description for YAML
        description_yaml = description.replace('"', '\\"')

        skills.append({
            "id": skill_id,
            "filename": f.name,
            "description": description_yaml,
            "content": raw_text,
            "path": f,
        })
    return skills


def sync_antigravity(skills):
    """Generate .agents/skills/<skill_id>/SKILL.md for each FlowKit skill."""
    AGENTS_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    synced_count = 0
    for s in skills:
        skill_dir = AGENTS_SKILLS_DIR / s["id"]
        skill_dir.mkdir(parents=True, exist_ok=True)

        target_file = skill_dir / "SKILL.md"

        # Check if references directory exists in skills/
        ref_source = SKILLS_DIR / "references"
        ref_target = skill_dir / "references"
        if ref_source.exists() and not ref_target.exists():
            shutil.copytree(ref_source, ref_target)

        frontmatter = (
            f"---\n"
            f"name: {s['id']}\n"
            f"description: \"{s['description']}\"\n"
            f"---\n\n"
            f"<!-- AUTO-GENERATED from {s['filename']} — do not edit directly. -->\n\n"
        )
        target_file.write_text(frontmatter + s["content"], encoding="utf-8")

        # Also sync to global Antigravity skills directory if available
        if GLOBAL_SKILLS_DIR.exists():
            global_skill_dir = GLOBAL_SKILLS_DIR / s["id"]
            global_skill_dir.mkdir(parents=True, exist_ok=True)
            global_target_file = global_skill_dir / "SKILL.md"
            global_target_file.write_text(frontmatter + s["content"], encoding="utf-8")
            if ref_source.exists() and not (global_skill_dir / "references").exists():
                shutil.copytree(ref_source, global_skill_dir / "references")

        synced_count += 1

    print(f"Synced {synced_count} skills to .agents/skills/ and global Antigravity config")


def clean_antigravity():
    """Remove .agents/skills/ directory."""
    if AGENTS_SKILLS_DIR.exists():
        shutil.rmtree(AGENTS_SKILLS_DIR)
        print("Cleaned .agents/skills/")
    else:
        print("Nothing to clean in .agents/skills/")


def main():
    parser = argparse.ArgumentParser(description="Sync FlowKit skills for Antigravity IDE")
    parser.add_argument("--clean", action="store_true", help="Remove generated .agents/skills/")
    args = parser.parse_args()

    if args.clean:
        clean_antigravity()
        return

    skills = discover_skills()
    if not skills:
        print("No skills found in skills/fk-*.md.", file=sys.stderr)
        return

    sync_antigravity(skills)


if __name__ == "__main__":
    main()
