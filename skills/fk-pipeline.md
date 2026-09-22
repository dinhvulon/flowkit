# fk-pipeline — Smart Full-Pipeline Orchestrator

Auto-detect project state and run the correct stages (continuation or full run). Handles batching, parallelism, retries, downloads, TTS, and Telegram notifications.

Usage: `/fk-pipeline [project_id] [orientation] [options]`

Options:
- `--r2v` — direct Reference-to-Video mode (`abra_r2v_8s`). Skips Stage 1 (Scene Images) and generates videos directly from reference entity images (uploaded via `/fk-upload-ref` or Stage 0) using RPC `MZZa6b`.
- `--upscale` — include 4K upscale stage. **Unavailable since Flow moved** — no upsampler rpc has been captured on `flow.google.com`, so every upscale fails `UNSUPPORTED_ON_BATCH_API` (terminal, not retried). Warn the user and run without it; the 1080p render is the deliverable. See `docs/CAPTURE.md`.
- `--tts` — include TTS narration stage (parallel with upscale)
- `--download` — auto-download 4K files as upscales complete
- `--concat` — run concat after all stages done (default: enabled when videos/TTS are done)
- `--no-seo` — skip automatic YouTube SEO metadata generation after concat (SEO runs by default)
- `--no-thumbnail` — skip automatic 4-variant thumbnail generation after concat (Thumbnails run by default)
- `--upload` — automatically upload to YouTube after SEO & thumbnail prep (requires configured YouTube OAuth)
- `--notify` — send Telegram notifications at milestones
- `--interval N` — poll interval in seconds (default: 15)
- `--orientation H|V` — HORIZONTAL or VERTICAL (auto-detected from video.orientation if omitted)

Examples:
- `/fk-pipeline` — detect state and continue most recent project
- `/fk-pipeline --r2v --tts --concat` — direct R2V run: skips start frame images, renders video, TTS, concats, and auto-generates SEO + thumbnails
- `/fk-pipeline --upscale --tts --download --notify` — full run with all options
- `/fk-pipeline <project_id> HORIZONTAL --upscale --download` — explicit project + orientation

---

## When to Use

- Starting a new project from scratch (after scenes are created)
- Resuming a partially-complete project
- Batch-running all remaining stages hands-free
- Want TTS + upscale to run simultaneously
- Want 4K downloads to roll in as each upscale completes

---

## Pre-pipeline: How Projects & Scenes Are Created

`/fk-pipeline` orchestrates rendering, TTS, concat, and publication. To create the project and scenes first, choose one of:

1. **Japanese Historical POV Vlogs (Kyoto Heian, Kamakura, Edo)**:
   - Use **[`/fk-vlog-japan`](file:///c:/flowkit/skills/fk-vlog-japan.md)** (or run `python scripts/create_kyoto_heian_1000.py`).
   - Automatically builds 10-12 scenes with Pan-Focus f/8–f/11 optics, walking-talking selfie prompts, strict period/ethnicity locks, and conversational Japanese dialogue (`dialog-japan`).
2. **General / Custom Story Projects**:
   - Use **[`/fk-create-project`](file:///c:/flowkit/skills/fk-create-project.md)** to generate scenes from any story concept.
3. **Real Face Reference (Optional)**:
   - Use **[`/fk-upload-ref "<image_path>" --entity "Vlogger"`](file:///c:/flowkit/skills/fk-upload-ref.md)** to lock your real face before running `/fk-pipeline`.

After project & scenes exist ➔ run `/fk-pipeline --r2v --tts --concat` to automate everything end-to-end!

---

## Step 1: Resolve Project and State

### 1a. Fetch project

```bash
# Most recent project
curl -s http://127.0.0.1:8100/api/projects
# Use last item → {id, name}

# Get video + scenes
VID=$(curl -s "http://127.0.0.1:8100/api/videos?project_id=<PID>" | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['id'])")
curl -s "http://127.0.0.1:8100/api/scenes?video_id=$VID" > /tmp/fk_scenes.json
curl -s "http://127.0.0.1:8100/api/projects/<PID>/characters" > /tmp/fk_chars.json
curl -s "http://127.0.0.1:8100/api/projects/<PID>/output-dir" > /tmp/fk_outdir.json
```

### 1b. Derive slug and output dir

```python
import json

outdir_meta = json.load(open('/tmp/fk_outdir.json'))
SLUG = outdir_meta['slug']
OUTDIR = outdir_meta['path']
```

### 1c. State detection

```python
import json, glob as globmod, os

scenes = json.load(open('/tmp/fk_scenes.json'))
chars  = json.load(open('/tmp/fk_chars.json'))
PREFIX = video_orientation.lower()  # from GET /api/videos/{vid} → orientation field; 'horizontal' or 'vertical'
N      = len(scenes)

def pct(done, total):
    return f"{done}/{total}" if total else "0/0"

state = {
    # Stage 0: ref images
    'refs_total':   len(chars),
    'refs_done':    sum(1 for c in chars if c.get('media_id')),
    'refs_missing': [c['id'] for c in chars if not c.get('media_id')],

    # Stage 1: scene images
    'images_total':   N,
    'images_done':    sum(1 for s in scenes if s.get(f'{PREFIX}_image_status') == 'COMPLETED'),
    'images_pending': [s['id'] for s in scenes if s.get(f'{PREFIX}_image_status') != 'COMPLETED'],

    # Stage 2: videos
    'videos_total':   N,
    'videos_done':    sum(1 for s in scenes if s.get(f'{PREFIX}_video_status') == 'COMPLETED'),
    'videos_pending': [s['id'] for s in scenes if s.get(f'{PREFIX}_video_status') != 'COMPLETED'],

    # Stage 2.5: review
    'review_done':    False,  # set True after review passes or max cycles

    # Stage 3: upscale
    'upscale_total':   N,
    'upscale_done':    sum(1 for s in scenes if s.get(f'{PREFIX}_upscale_status') == 'COMPLETED'),
    'upscale_pending': [s['id'] for s in scenes
                        if s.get(f'{PREFIX}_upscale_status') not in ('COMPLETED', 'FAILED')],
    'upscale_failed':  [s['id'] for s in scenes if s.get(f'{PREFIX}_upscale_status') == 'FAILED'],

    # Stage 4: TTS
    'tts_total':  N,
    'tts_done':   len(globmod.glob(f'{OUTDIR}/tts/scene_*.wav')),
    'has_narrator': any(s.get('narrator_text') for s in scenes),

    # Stage 5: downloads
    'dl_total':  N,
    'dl_done':   len(globmod.glob(f'{OUTDIR}/4k/scene_*.mp4')),
}
```

### 1d. Print detected state and plan

```
Detected state for <project_name> [HORIZONTAL]:
  Refs:      5/5  ✓
  Images:    50/50 ✓
  Videos:    50/50 ✓
  Review:    passed (48/50 good, 2 fixed after regen)
  Upscale:   39/50  ← in progress
  TTS:       50/50 ✓
  Downloads: 39/50  ← behind upscale

Plan:
  [ACTIVE]  Continue upscale (11 remaining)
  [ACTIVE]  Download as upscales complete
  [SKIP]    TTS (already done)
  [QUEUED]  Concat after upscale+download complete
```

---

## Step 2: Stage Routing

Use this decision tree to determine which stages to run and in what order.

```python
stages_to_run = []

# Sequential gates — each stage blocks the next
if state['refs_done'] < state['refs_total']:
    stages_to_run.append('REFS')
elif state['images_done'] < state['images_total']:
    stages_to_run.append('IMAGES')
elif state['videos_done'] < state['videos_total']:
    stages_to_run.append('VIDEOS')

# Review (after videos done, before upscale)
if state['videos_done'] == state['videos_total'] and not state['review_done']:
    stages_to_run.append('REVIEW')

# Upscale (after review passes)
if upscale_flag and state['videos_done'] == state['videos_total'] and state['review_done']:
    if state['upscale_done'] < state['upscale_total']:
        stages_to_run.append('UPSCALE')

# TTS — parallel with upscale/videos (independent)
if tts_flag and state['has_narrator'] and state['tts_done'] < state['tts_total']:
    stages_to_run.append('TTS')  # runs concurrently

# Downloads — rolling alongside upscale
if download_flag and state['dl_done'] < state['dl_total']:
    stages_to_run.append('DOWNLOAD')  # runs concurrently with UPSCALE

# Concat — after all downloads + TTS done
if concat_flag:
    stages_to_run.append('CONCAT')  # runs last
```

**Parallelism rules:**
- `REFS` → `IMAGES` → `VIDEOS` → `REVIEW` are **sequential** (each requires previous)
- `UPSCALE` + `TTS` can run **simultaneously** (spawn 2 agents)
- `DOWNLOAD` runs **rolling** alongside UPSCALE (check each poll cycle)
- `CONCAT` runs **after** UPSCALE + DOWNLOAD + TTS all complete

---

## Step 3: Run Each Stage

### Stage 0 — Ref Images

Only run if any entity is missing `media_id`.

> [!TIP]
> **Custom Face Reference:** If you uploaded custom character or asset photos via `/fk-upload-ref`, those entities already have a valid `media_id` UUID. Stage 0 will automatically preserve them (skipping AI generation) and pass them as `imageInputs` references in Stage 1 (Scene Images) and Stage 2 (Scene Videos).

```bash
# For each entity missing media_id, submit GENERATE_CHARACTER_IMAGE
# Batch 5 at a time
for CID in <missing_ids>:
  curl -X POST http://127.0.0.1:8100/api/requests \
    -H "Content-Type: application/json" \
    -d '{"type":"GENERATE_CHARACTER_IMAGE","character_id":"<CID>","project_id":"<PID>"}'
```

**Poll until all entities have `media_id`** before moving to Stage 1.

**Retry rule:** If a ref gen fails, resubmit once. If fails again, warn user and skip.

---

### Stage 1 — Scene Images (Skip if using `--r2v`)

Only run after all refs have `media_id`.

> [!NOTE]
> **R2V Mode:** If `--r2v` is set, **SKIP Stage 1 entirely**. FlowKit will use the reference entity images (`character_names`) directly to generate videos via `abra_r2v_8s` without generating start scene images first.

```bash
# For each scene with image_status != COMPLETED (I2V mode only):
curl -X POST http://127.0.0.1:8100/api/requests \
  -H "Content-Type: application/json" \
  -d '{"type":"GENERATE_IMAGE","scene_id":"<SID>","project_id":"<PID>","video_id":"<VID>","orientation":"<ORIENTATION>"}'
```

Batch 5 at a time. Poll every 15s. Submit next batch when current batch completes.

**Failed images:** Resubmit once with `REGENERATE_IMAGE` (forces re-run).

---

### Stage 2 — Scene Videos

**A. Standard Mode (I2V with `abra_i2v_8s`):**
Only run after all scene images COMPLETED.
```bash
curl -X POST http://127.0.0.1:8100/api/requests \
  -H "Content-Type: application/json" \
  -d '{"type":"GENERATE_VIDEO","scene_id":"<SID>","project_id":"<PID>","video_id":"<VID>","orientation":"<ORIENTATION>"}'
```

**B. R2V Mode (Ingredients with `abra_r2v_8s` via RPC `MZZa6b`):**
Runs directly when Stage 0 (Ref Images) is complete:
```bash
curl -X POST http://127.0.0.1:8100/api/requests \
  -H "Content-Type: application/json" \
  -d '{"type":"GENERATE_VIDEO_REFS","scene_id":"<SID>","project_id":"<PID>","video_id":"<VID>","orientation":"<ORIENTATION>"}'
```

> [!TIP]
> **Dual-Track Voice Handling:**
> 1. **In-Video Lip-Sync (Veo 3):** Structure the `video_prompt` with quoted dialogue in sub-clips (e.g. `0-3s: Luna walks and says "Konnichiwa"`). Veo 3 / Omni Flash automatically animates the character's lips and generates natural speaking audio inside the video.
> 2. **Studio TTS Narration:** Run Stage 3 with `--tts` (OmniVoice / EdgeTTS) to generate crisp narration audio that aligns cleanly with the storyline during concatenation.

Batch 5. Poll 15s. Each video takes 2-5 min.

**Auto-Retry Rule (Max 5 Attempts):**
- Any video generation that fails (timeout after 420s or API error) MUST be automatically retried up to **5 times** (`MAX_RETRIES = 5`).
- If an operation fails repeatedly due to content moderation or safety filters (e.g. `as29s failed: [5]`):
  1. Automatically sanitize `video_prompt` and scene `prompt` to remove sensitive/violent trigger words (weapons, poison, smoke, war cries).
  2. Call `REGENERATE_IMAGE` first to create a fresh, clean start frame (`media_id`).
  3. Call `GENERATE_VIDEO` again with the clean start frame.

**Immediate Rolling Download:**
- As soon as each scene video reaches `COMPLETED`, immediately download it to `${OUTDIR}/scenes/scene_{IDX3}_{SCENE_ID}.mp4`.
- Never wait for the entire pipeline to finish before downloading; completed clips are stored locally on disk right away.

---

### Stage 2.5 — Mandatory Review Videos & Review Board

Runs automatically after the video batch completes (or after all retries settle). Uses `/fk-review-video` to catch AI generation errors and review each node before concatenation:

```bash
# 1. Run light review on all completed videos via API
curl -s -X POST "http://127.0.0.1:8100/api/videos/<VID>/review?project_id=<PID>&mode=light&orientation=<ORIENTATION>"
```

**Auto-Report & Node Status Table:**
Always print the per-node review summary directly to the terminal:
```
===========================================================================
🎬 AI VISION REVIEW REPORT (Overall Score: X.X/10)
===========================================================================
Scene      | Score  | Verdict    | Face Cons.   | Motion     | Main Issue / Action
---------------------------------------------------------------------------
Scene 0    | 7.97   | GOOD       | 8.5          | 7.5        | Keep as-is
Scene 1    | 7.48   | ACCEPTABLE | 7.5          | 8.5        | Keep as-is
Scene 2    | 6.90   | ACCEPTABLE | 7.5          | 7.5        | Optional regen (text overlay)
Scene 6    | FAILED | NEED REGEN | -            | -          | Auto-sanitized, regenerating
===========================================================================
```

**Launch Scene Review Board (Interactive Web UI):**
Automatically ensure the review server is active so the user can inspect videos in browser:
```bash
python tools/review_server.py 8200
```
Print the review link:
👉 **`http://localhost:8200?video_id=<VID>`**

**Interpret results & Fix Loop (max 2 review cycles):**
- Scenes scoring **7.5+** (good/excellent) → pass, proceed to concat
- Scenes scoring **4.0–7.4** (acceptable/poor) → update `video_prompt` based on `fix_guide` + `errors`, then regen video
- Scenes scoring **0–3.9** (unusable) or **FAILED** → sanitize prompt, regen image first (`REGENERATE_IMAGE`), then regen video

```python
for cycle in range(2):
    review = run_review(VID, mode='light')
    bad_scenes = [s for s in review if s['total_score'] < 7.5]
    if not bad_scenes:
        break  # all pass

    for scene in bad_scenes:
        new_prompt = improve_prompt(scene['video_prompt'], scene['errors'], scene['fix_guide'])
        curl_patch(f"/api/scenes/{scene['scene_id']}", {"video_prompt": new_prompt})

        if scene['total_score'] < 4.0:
            submit_request("REGENERATE_IMAGE", scene['scene_id'])
        else:
            submit_request("GENERATE_VIDEO", scene['scene_id'])
```

After review passes (or review cycles complete):
- Download any newly completed scenes
- Proceed to Concat with all approved scenes


---

### Stage 3 — Upscale (4K)

Only run after review passes (or max review cycles exhausted). TIER_TWO only.

```bash
curl -X POST http://127.0.0.1:8100/api/requests \
  -H "Content-Type: application/json" \
  -d '{"type":"UPSCALE_VIDEO","scene_id":"<SID>","project_id":"<PID>","video_id":"<VID>","orientation":"<ORIENTATION>"}'
```

Batch 5. **Resubmit failed upscales** once automatically.

---

### Stage 4 — TTS Narration (parallel)

Runs in parallel with Stage 2 or 3. Requires `narrator_text` on scenes and a voice template.

```bash
# Check templates
curl -s http://127.0.0.1:8100/api/tts/templates
# Pick template name (e.g. vi_male_narrator)

# Trigger narration for video
curl -X POST http://127.0.0.1:8100/api/videos/<VID>/narrate \
  -H "Content-Type: application/json" \
  -d '{"template":"<template_name>"}'
```

Poll `output/<slug>/tts/` for WAV files as they appear.

**If no template exists:** Pause and instruct user to run `/fk-gen-tts-template` or `/fk-import-voice` first.

---

### Stage 5 — Rolling Downloads (parallel with upscale)

Each poll cycle, check for newly completed upscales not yet downloaded:

```python
newly_completed = [
    s for s in scenes
    if s.get(f'{PREFIX}_upscale_status') == 'COMPLETED'
    and s.get(f'{PREFIX}_upscale_url')
    and not os.path.exists(f"{OUTDIR}/4k/scene_{s['display_order']:03d}_{s['id']}.mp4")
]
```

For each, write URL to temp file and download via curl:

```bash
URL=$(cat /tmp/url_scene_<order>.txt)
curl -s "$URL" -o "output/<slug>/4k/scene_<order:03d>_<scene_id>.mp4"
```

**Important:** Write URL to temp file before passing to curl — avoids shell encoding mangling GCS signatures.

Verify each download:
```bash
ffprobe -v quiet -show_entries format=duration -of csv=p=0 "<file>"
# Must be > 0 seconds
```

---

### Stage 6 — Concat

Run after UPSCALE + DOWNLOAD + TTS all complete. Delegates to `/fk-concat`.

Invoke: `/fk-concat --4k --with-tts` (or appropriate flags based on what was run).

---

### Stage 7 — Auto SEO & Thumbnails (Publishing Prep)

Runs automatically after Concat completes (unless `--no-seo` or `--no-thumbnail` is specified). Prepares the entire publishing kit ready for upload:

1. **Auto YouTube SEO (`/fk-youtube-seo`)**:
   - Auto-detects format: **9:16 Shorts** (Shorts hook, #Shorts, condensed description) or **16:9 Long-form** (full 4-part description, 3-tier tags, timestamps chapters).
   - Auto-detects language: matches project language (VI, EN, JA).
   - Generates and writes files:
     - `output/<slug>/youtube_metadata.json` (machine-readable for upload API)
     - `output/<slug>/youtube_metadata.md` (clean human-readable copy/paste document)

2. **Auto Thumbnails (`/fk-thumbnail`)**:
   - Generates 4 hook-worthy thumbnail variants matching video orientation (9:16 or 16:9).
   - Follows `/fk-thumbnail-guide` (2-line bold hook text, character reference consistency, high contrast).
   - Saves into `output/<slug>/thumbnails/variant_1..4.png`.

3. **Publishing Gate**:
   - Prints the full package summary to the console: Title, Description preview, and Thumbnail file paths.
   - If `--upload` was passed, automatically invokes `/fk-youtube-upload`. Otherwise, halts safely so you can review before uploading manually.

---

## Step 4: Poll Loop

```python
import time

INTERVAL = 15
cycle = 0

while stages_to_run:
    cycle += 1
    print(f"[cycle {cycle}] Polling...")

    # Refresh scene data
    scenes = fetch_scenes(VID)
    state = compute_state(scenes, chars, OUTDIR, PREFIX)

    # Submit next batch for active sequential stage
    active_stage = stages_to_run[0]  # HEAD of sequential chain
    if active_stage in ('REFS','IMAGES','VIDEOS','UPSCALE'):
        submit_next_batch(active_stage, state, PID, VID, ORIENTATION)

    # Check if active stage completed
    if stage_complete(active_stage, state):
        stages_to_run.pop(0)
        print(f"✅ {active_stage} complete")
        if notify_flag:
            send_telegram(f"✅ {active_stage} complete for {project_name}")

    # Parallel: Rolling downloads (every cycle when upscaling)
    if 'DOWNLOAD' in stages_to_run:
        download_newly_completed(scenes, state, OUTDIR, PREFIX, PID=PID, VID=VID)
        if state['dl_done'] >= state['upscale_done']:
            pass  # downloads caught up — keep watching

    # Check if all done
    remaining_sequential = [s for s in stages_to_run if s not in ('TTS','DOWNLOAD','CONCAT')]
    if not remaining_sequential and state['dl_done'] == state['upscale_done']:
        if 'CONCAT' in stages_to_run:
            run_concat()
        break

    time.sleep(INTERVAL)
```

---

## Step 5: Failure Handling

| Failure type | Detection | Action |
|---|---|---|
| Ref image FAILED | `media_id` missing after request COMPLETED | Resubmit `GENERATE_CHARACTER_IMAGE` once |
| Scene image FAILED | `horizontal_image_status == FAILED` | Resubmit `REGENERATE_IMAGE` once |
| Video FAILED | `horizontal_video_status == FAILED` | Resubmit `GENERATE_VIDEO` once |
| Review FAILED (score < 7.5) | `total_score < 7.5` in review results | Update `video_prompt` from `fix_guide` + `errors`, regen video (max 2 cycles) |
| Review UNUSABLE (score < 4.0) | `total_score < 4.0` in review results | Update `video_prompt`, regen image first (`REGENERATE_IMAGE`), then video |
| Upscale FAILED | `horizontal_upscale_status == FAILED` | Resubmit `UPSCALE_VIDEO` once |
| Download 4KB (XML error) | `ffprobe` returns 0s or non-numeric | Re-download (URL still valid for ~8h) |
| Worker stalled | pending > 0, processing = 0 for 2+ min | Print warning; suggest server restart |
| TTS no template | `GET /api/tts/templates` returns empty | Pause; prompt user to create template |

**Max retries:** 2 per scene per stage. After 2 failures, log and skip — report at end.

---

## Step 6: Final Summary

```
Pipeline complete for <project_name>
  Refs:      5/5
  Images:    50/50
  Videos:    50/50
  Review:    passed (48 good, 2 fixed after regen)
  Upscale:   50/50  (1 retry)
  Downloads: 50/50
  TTS:       50/50
  Failed:    0

Ready for: /fk-concat --4k --with-tts
```

Send via Telegram if `--notify`.

---

## Concurrent TTS + Upscale Pattern

When both `--tts` and `--upscale` are requested and videos are done, spawn two parallel tracks:

```
Track A (main agent):   UPSCALE → batch 5 → poll → batch 5 → ...
                        └─ DOWNLOAD: rolling on each poll cycle

Track B (sub-agent):    TTS → POST /api/videos/<VID>/narrate → poll tts/ dir
```

Use the Agent tool with `oh-my-claudecode:executor` for Track B:

```
Agent(
  subagent_type="oh-my-claudecode:executor",
  prompt="Run TTS narration for video <VID> using template <template>.
          Poll output/<slug>/tts/ every 30s until all <N> WAV files appear.
          Report done when complete."
)
```

Main agent handles upscale + downloads. Both finish independently.

---

## Console Output Format

```
[fk-pipeline] Operation Absolute Resolve - Cinematic Edition [HORIZONTAL]
Stage:     UPSCALE (39/50) + DOWNLOAD (39/50) rolling
Queue:     5 pending / 5 processing
TTS:       50/50 ✓ (parallel, done)
Cycle 12 / next poll in 15s...
```

---

## Common Issues

| Issue | Fix |
|-------|-----|
| `extension_connected: false` | Chrome extension disconnected — reload extension |
| Stage stuck at 0/N | Check `/api/requests?status=FAILED` for errors |
| Upscale TIER_ONE error | Account is TIER_ONE — skip `--upscale` |
| Downloads 4KB XML error | Write URL to temp file, re-curl |
| TTS `torch not found` | Set `TTS_PYTHON_BIN=/opt/homebrew/bin/python3.10` in server env |
| Worker stalled | POST http://127.0.0.1:8100/api/worker/restart or restart server |

---

## Next Steps

| After pipeline | Skill |
|---|---|
| Mix TTS into videos | `/fk-concat --with-tts` |
| Add branding watermark | `/fk-brand-logo` |
| Generate YouTube SEO | `/fk-youtube-seo` |
| Upload to YouTube | `/fk-youtube-upload` |
