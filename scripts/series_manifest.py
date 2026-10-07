#!/usr/bin/env python3
"""
FlowKit — Batch Episode Series Manifest Manager
Manages per-project series manifests (`output/<slug>/series_manifest.json`).

Features:
1. Per-Project Manifest Architecture: Each project stores its own `series_manifest.json`
   directly inside `output/<slug>/series_manifest.json`.
2. Automatic Synchronization: Automatically generated and kept in sync with FlowKit backend.
3. `sync` / `export`: Generates or pulls the latest manifest from FlowKit API into `output/<slug>/series_manifest.json`.
4. `show`: Renders an overview table of characters, locations, and episode progress.
5. `bootstrap`: Creates a new chapter in FlowKit API reusing pre-existing shared entity UUIDs.

Usage:
    python scripts/series_manifest.py sync --project-id <PID>
    python scripts/series_manifest.py show --project-dir output/hong_nhat_thang_long
    python scripts/series_manifest.py bootstrap --project-dir output/hong_nhat_thang_long --episode 6 --title "Chương VI: Huyết Nguyệt"
"""

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path


def api_request(url, method="GET", payload=None, timeout=15):
    """Perform JSON HTTP request against FlowKit API."""
    data = None
    headers = {"User-Agent": "FlowKit-SeriesManifest"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read().decode("utf-8")
            return json.loads(content) if content else {}
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8") if e.fp else str(e)
        print(f"API Error ({e.code}) on {url}: {err_msg}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Connection Error on {url}: {e}", file=sys.stderr)
        return None


def resolve_manifest_path(project_dir=None, project_id=None, manifest=None, base_url="http://127.0.0.1:8100"):
    """Resolve the path to the per-project series_manifest.json."""
    if manifest:
        return Path(manifest)

    if project_dir:
        p_dir = Path(project_dir)
        return p_dir / "series_manifest.json"

    if project_id:
        # Fetch output-dir from API
        res = api_request(f"{base_url}/api/projects/{project_id}/output-dir")
        if res and "path" in res:
            return Path(res["path"]) / "series_manifest.json"

    # Default fallback: check common project directory
    candidates = list(Path("output").glob("*/series_manifest.json"))
    if candidates:
        return candidates[0]

    return Path("output/default/series_manifest.json")


def sync_from_project_api(project_id, base_url="http://127.0.0.1:8100"):
    """Trigger API to auto-generate and return per-project series_manifest.json."""
    print(f"🔄 Syncing series manifest from API for project {project_id}...")
    manifest_data = api_request(f"{base_url}/api/projects/{project_id}/manifest")
    if not manifest_data:
        print(f"❌ Failed to sync manifest for project {project_id}", file=sys.stderr)
        return False

    slug = manifest_data.get("slug", "project")
    target_path = Path(f"output/{slug}/series_manifest.json")
    print(f"✅ Series manifest automatically synced and saved to: {target_path}")
    print(f"  Title:      {manifest_data.get('series_title')}")
    print(f"  Characters: {len(manifest_data.get('shared_entities', {}).get('characters', []))}")
    print(f"  Locations:  {len(manifest_data.get('shared_entities', {}).get('locations', []))}")
    print(f"  Episodes:   {len(manifest_data.get('episodes', []))}")
    return True


def show_manifest(manifest_path):
    """Print an overview of the series manifest."""
    m_path = Path(manifest_path)
    if not m_path.exists():
        print(f"❌ Manifest not found at: {manifest_path}", file=sys.stderr)
        return False

    data = json.loads(m_path.read_text(encoding="utf-8"))
    print("\n=======================================================")
    print(f"📚 PER-PROJECT SERIES MANIFEST: {data.get('series_title')}")
    print(f"Location:    {m_path}")
    print(f"Slug:        {data.get('slug')}")
    print(f"Material:    {data.get('material')}")
    print(f"Orientation: {data.get('orientation')}")
    print(f"Default TTS: {data.get('default_voice')}")
    print("=======================================================\n")

    chars = data.get("shared_entities", {}).get("characters", [])
    print(f"🎭 Shared Characters ({len(chars)}):")
    for c in chars:
        m_id = c.get("media_id", "NO MEDIA ID")
        print(f"  • {c.get('name'):<22} | UUID: {m_id}")

    locs = data.get("shared_entities", {}).get("locations", [])
    print(f"\n🏛️ Shared Locations ({len(locs)}):")
    for l in locs:
        m_id = l.get("media_id", "NO MEDIA ID")
        print(f"  • {l.get('name'):<25} | UUID: {m_id}")

    episodes = data.get("episodes", [])
    print(f"\n🎬 Episode Roadmap ({len(episodes)} episodes):")
    for ep in episodes:
        num = ep.get("episode", "?")
        title = ep.get("title", "")
        status = ep.get("status", "PLANNING")
        vid_id = ep.get("video_id", "N/A")[:8]
        print(f"  [{status:<10}] Ep {num:<2}: {title:<35} (VID: {vid_id})")

    print("=======================================================\n")
    return True


def bootstrap_episode(manifest_path, episode_num, episode_title, base_url="http://127.0.0.1:8100",
                      only=None, flow_project_id=None):
    """Create a new chapter project in FlowKit with shared entities pre-linked.

    `POST /api/projects` takes reference stubs under `characters` and has no
    `media_id` field, so the entities are created first and each reused UUID
    is attached afterwards with `PATCH /api/characters/{cid}`.

    `only` limits the reuse to the named entities (e.g. a vlogger's face sheet
    when every episode gets a new outfit and new locations).
    """
    m_path = Path(manifest_path)
    if not m_path.exists():
        print(f"❌ Manifest not found: {manifest_path}", file=sys.stderr)
        return False

    data = json.loads(m_path.read_text(encoding="utf-8"))
    series_title = data.get("series_title", "Series")
    material = data.get("material", "realistic")

    project_name = f"{series_title} — Ep {episode_num}: {episode_title}"
    story_summary = f"Episode {episode_num} of {series_title}. {data.get('story_bible', '')}"

    wanted = set(only) if only else None
    all_entities = []
    shared = data.get("shared_entities", {})
    for cat in ["characters", "locations", "key_props"]:
        for item in shared.get(cat, []):
            if wanted is not None and item.get("name") not in wanted:
                continue
            all_entities.append(item)
    if wanted is not None:
        missing = wanted - {e.get("name") for e in all_entities}
        if missing:
            print(f"❌ Not in manifest: {', '.join(sorted(missing))}", file=sys.stderr)
            return False

    payload = {
        "name": project_name,
        "story": story_summary,
        "material": material,
        "characters": [
            {k: e.get(k) for k in ("name", "entity_type", "description", "voice_description")
             if e.get(k) is not None}
            for e in all_entities
        ],
    }
    if flow_project_id:
        payload["flow_project_id"] = flow_project_id

    print(f"\n🚀 Bootstrapping new episode project via API:")
    print(f"  Name: {project_name}")
    print(f"  Reusing {len(all_entities)} shared entity references...")

    # Creating a fresh Flow project waits out the server's 45-60s request gap.
    res = api_request(f"{base_url}/api/projects", method="POST", payload=payload, timeout=300)
    if not res or "id" not in res:
        print("Failed to create project in FlowKit API", file=sys.stderr)
        return False

    new_pid = res["id"]
    print(f"✅ Episode project created successfully!")
    print(f"  Project ID: {new_pid}")

    created = api_request(f"{base_url}/api/projects/{new_pid}/characters") or []
    ids_by_name = {c.get("name"): c.get("id") for c in created}
    linked = 0
    for e in all_entities:
        cid = ids_by_name.get(e.get("name"))
        patch = {k: e.get(k) for k in ("media_id", "reference_image_url") if e.get(k)}
        if not cid or not patch.get("media_id"):
            print(f"  ⚠️ {e.get('name')}: no media_id reused — generate or upload its ref", file=sys.stderr)
            continue
        if api_request(f"{base_url}/api/characters/{cid}", method="PATCH", payload=patch) is not None:
            linked += 1
    print(f"  Pre-linked entities: {linked}/{len(all_entities)}")

    # Auto-initialize output directory and project manifest
    api_request(f"{base_url}/api/projects/{new_pid}/output-dir")

    print(f"\nNext Steps:")
    print(f"  1. Create video:  POST /api/videos (project_id={new_pid})")
    print(f"  2. Create scenes: POST /api/scenes (using character_names)")
    print(f"  3. Generate refs only for entities that were not pre-linked.")
    return linked == len(all_entities)


def main():
    parser = argparse.ArgumentParser(description="FlowKit Per-Project Series Manifest Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # sync
    p_sync = subparsers.add_parser("sync", help="Auto-sync series_manifest.json from FlowKit API")
    p_sync.add_argument("--project-id", required=True, help="FlowKit project ID to sync")
    p_sync.add_argument("--api-url", default="http://127.0.0.1:8100", help="FlowKit base URL")

    # show
    p_show = subparsers.add_parser("show", help="Display manifest summary")
    p_show.add_argument("--project-dir", help="Project directory (e.g. output/hong_nhat_thang_long)")
    p_show.add_argument("--project-id", help="Project ID")
    p_show.add_argument("--manifest", help="Direct path to series_manifest.json")
    p_show.add_argument("--api-url", default="http://127.0.0.1:8100", help="FlowKit base URL")

    # bootstrap
    p_boot = subparsers.add_parser("bootstrap", help="Create new episode project reusing shared entities")
    p_boot.add_argument("--project-dir", help="Source project directory (e.g. output/hong_nhat_thang_long)")
    p_boot.add_argument("--manifest", help="Direct path to series_manifest.json")
    p_boot.add_argument("--episode", type=int, required=True, help="Episode number (e.g. 6)")
    p_boot.add_argument("--title", required=True, help="Episode title")
    p_boot.add_argument("--api-url", default="http://127.0.0.1:8100", help="FlowKit base URL")
    p_boot.add_argument("--only", nargs="+", metavar="NAME",
                        help="Reuse only these shared entities (e.g. the vlogger's face sheet)")
    p_boot.add_argument("--flow-project-id",
                        help="Reuse this Flow project instead of creating a fresh one")

    args = parser.parse_args()

    if args.command == "sync":
        ok = sync_from_project_api(args.project_id, base_url=args.api_url)
        sys.exit(0 if ok else 1)
    elif args.command == "show":
        m_path = resolve_manifest_path(project_dir=args.project_dir, project_id=args.project_id, manifest=args.manifest, base_url=args.api_url)
        ok = show_manifest(m_path)
        sys.exit(0 if ok else 1)
    elif args.command == "bootstrap":
        m_path = resolve_manifest_path(project_dir=args.project_dir, manifest=args.manifest, base_url=args.api_url)
        ok = bootstrap_episode(m_path, args.episode, args.title, base_url=args.api_url,
                               only=args.only, flow_project_id=args.flow_project_id)
        sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
