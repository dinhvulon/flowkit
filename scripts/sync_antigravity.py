#!/usr/bin/env python3
"""
Flow Kit — Sync Skills for Google Antigravity (AGY) IDE
Converts skills/fk-*.md into .agents/skills/fk-*/SKILL.md with YAML frontmatter
so that Antigravity IDE recognizes them as native slash commands and on-demand skills.

Usage:
    python scripts/sync_antigravity.py          # Generate/sync .agents/skills/
    python scripts/sync_antigravity.py --clean  # Remove generated .agents/skills/
"""

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
AGENTS_SKILLS_DIR = ROOT / ".agents" / "skills"


def discover_skills():
    """Scan skills/fk-*.md and extract name + description + content."""
    if not SKILLS_DIR.exists():
        print(f"ERROR: skills/ directory not found at {SKILLS_DIR}")
        return []

    skills = []
    for path in sorted(SKILLS_DIR.glob("fk-*.md")):
        skill_id = path.stem  # e.g. "fk-vlog-japan"
        raw_text = path.read_text(encoding="utf-8")
        lines = raw_text.splitlines()

        # Extract description from first markdown heading or line
        description = skill_id
        for line in lines:
            line_str = line.strip().lstrip("#").strip()
            if line_str:
                description = line_str
                break

        # Sanitize description for YAML (avoid quotes issues)
        description_yaml = description.replace('"', '\\"')

        skills.append({
            "id": skill_id,
            "description": description_yaml,
            "path": path,
            "content": raw_text,
        })
    return skills


def sync_antigravity(skills):
    """Generate .agents/skills/<skill_id>/SKILL.md for each FlowKit skill."""
    AGENTS_SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0

    GLOBAL_SKILLS_DIR = Path.home() / ".gemini" / "config" / "skills"
    has_global = GLOBAL_SKILLS_DIR.exists()

    for skill in skills:
        # 1. Sync to workspace .agents/skills
        skill_dir = AGENTS_SKILLS_DIR / skill["id"]
        skill_dir.mkdir(parents=True, exist_ok=True)
        skill_file = skill_dir / "SKILL.md"

        frontmatter = (
            f"---\n"
            f"name: {skill['id']}\n"
            f"description: \"{skill['description']}\"\n"
            f"---\n\n"
            f"<!-- AUTO-GENERATED from {skill['path'].name} — do not edit directly. -->\n\n"
        )
        full_content = frontmatter + skill["content"]
        skill_file.write_text(full_content, encoding="utf-8")

        # 2. Sync to global Antigravity config skills if present
        if has_global:
            global_skill_dir = GLOBAL_SKILLS_DIR / skill["id"]
            global_skill_dir.mkdir(parents=True, exist_ok=True)
            (global_skill_dir / "SKILL.md").write_text(full_content, encoding="utf-8")

        count += 1

    msg = f"Successfully synced {count} skills to .agents/skills/"
    if has_global:
        msg += f" and {GLOBAL_SKILLS_DIR}"
    print(msg + " for Antigravity IDE.")
    return count


def clean_antigravity():
    """Remove .agents/skills/ directory."""
    if AGENTS_SKILLS_DIR.exists():
        shutil.rmtree(AGENTS_SKILLS_DIR)
        print(f"Removed {AGENTS_SKILLS_DIR}")
        # Clean .agents if empty
        agents_dir = ROOT / ".agents"
        try:
            agents_dir.rmdir()
        except OSError:
            pass
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
        print("No skills found in skills/fk-*.md.")
        sys.exit(1)

    sync_antigravity(skills)


if __name__ == "__main__":
    main()
