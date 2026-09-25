Generate videos for all scenes in a video.

Usage: `/fk-gen-videos <project_id> <video_id>`

## Step 0: Detect orientation

```bash
PROJ_OUT=$(curl -s http://127.0.0.1:8100/api/projects/<PID>/output-dir)
OUTDIR=$(echo "$PROJ_OUT" | python3 -c "import sys,json; print(json.load(sys.stdin)['path'])")
ORI=$(cat ${OUTDIR}/meta.json | python3 -c "import sys,json; print(json.load(sys.stdin).get('orientation','HORIZONTAL'))")
ori=$(echo "$ORI" | tr '[:upper:]' '[:lower:]')
```
**NEVER hardcode VERTICAL or HORIZONTAL.** Use `${ORI}` for API params, `${ori}_*` for DB field lookups.

## Step 1: Pre-check — all scene images must be ready

```bash
curl -s "http://127.0.0.1:8100/api/scenes?video_id=<VID>"
```

**ABORT** if any scene is missing `${ori}_image_media_id` (UUID) or `${ori}_image_status` != `"COMPLETED"`. Tell user to run `/fk-gen-images` first.

## Step 2: Filter scenes needing video

Only scenes where `${ori}_video_status` != `"COMPLETED"` or `${ori}_video_media_id` is missing.

## Step 3: Submit ALL requests at once

The server handles throttling automatically (max 5 concurrent, 10s cooldown). Submit everything in one batch call. Video generation takes 2-5 minutes per scene.

```bash
curl -X POST http://127.0.0.1:8100/api/requests/batch \
  -H "Content-Type: application/json" \
  -d '{
    "requests": [
      {"type": "GENERATE_VIDEO", "scene_id": "<SID1>", "project_id": "<PID>", "video_id": "<VID>", "orientation": "${ORI}"},
      {"type": "GENERATE_VIDEO", "scene_id": "<SID2>", "project_id": "<PID>", "video_id": "<VID>", "orientation": "${ORI}"}
    ]
  }'
```

Build the `requests` array from ALL scenes filtered in Step 2. Do NOT manually batch or loop.

Poll aggregate status every 30s until done (videos take longer):

```bash
curl -s "http://127.0.0.1:8100/api/requests/batch-status?video_id=<VID>&type=GENERATE_VIDEO"
# Wait for: "done": true
# If "all_succeeded": false → some failed, check individual failures
```

## Step 4: Auto-Retry Failed Videos (Max 5 Attempts)

Do NOT stop if a scene fails or times out. Automatically retry up to **5 times**:
1. Check failure reason:
   - If timed out or transient API error: resubmit `GENERATE_VIDEO` up to 5 times.
   - If content filter / safety rejection (e.g. `as29s failed: [5]`):
     a. Automatically sanitize `video_prompt` and scene `prompt` to remove sensitive/violent trigger words (poison, weapons, smoke, gore, screaming).
     b. Call `REGENERATE_IMAGE` first to create a fresh, compliant start frame (`media_id`).
     c. Call `GENERATE_VIDEO` with the new start frame.
2. Only mark permanently failed after 5 failed attempts.

## Step 5: Immediate Rolling Download

As each scene reaches `COMPLETED`, immediately download it locally to preserve files and allow instant preview:
```bash
# Save to:
${OUTDIR}/scenes/scene_{IDX3}_{SCENE_ID}.mp4
```

## Step 6: Mandatory AI Vision Review & Review Board

Automatically trigger `/fk-review-video` immediately without waiting for user instruction:
```bash
curl -s -X POST "http://127.0.0.1:8100/api/videos/<VID>/review?project_id=<PID>&mode=light&orientation=${ORI}"
```

**Print per-node status scorecard table:**
| Scene | Score | Verdict | Face Consistency | Action |
|-------|-------|---------|------------------|--------|
| Scene 0 | 8.2 | EXCELLENT | 8.5 | Ready for concat |
| Scene 1 | 7.6 | GOOD | 8.0 | Ready for concat |
| Scene X | 6.2 | ACCEPTABLE | 7.0 | Auto-regen / prompt tweak |

If any scene scores < 7.5, automatically propose/patch prompt and trigger regeneration (max 2 review cycles).

**Launch Scene Review Board (Interactive Web UI):**
```bash
python tools/review_server.py 8200
```
Provide the link: **`http://localhost:8200?video_id=<VID>`**

## Step 7: Output & Mandatory Individual Video Review Gate (CRITICAL)

1. **Verify all videos downloaded locally**:
   - Ensure every scene video is downloaded to `${OUTDIR}/scenes/scene_{idx:02d}_{sid}.mp4`.
2. **Present individual videos for review**:
   - Launch Review Board: `python tools/review_server.py 8200`.
   - Provide link: **`http://localhost:8200?video_id=<VID>`** or **`http://localhost:8200/review_images.html`**.
   - Print comprehensive Markdown table in chat showing every single unconcatenated scene video (Scene index, title/action, duration, local video link/file, vision score, status).
3. **STOP AND PAUSE HERE:**
   - **DO NOT** call `/fk-concat` or concatenate the video automatically!
   - Ra video là User review luôn từng clip một!
   - Ask user for feedback on each clip. If any clip needs adjustments (e.g. action, camera angle, phone selfie vlog perspective, lip sync), update the scene's `video_prompt` and submit `REGENERATE_VIDEO`.
   - Wait for explicit user instruction ("ghép video", "concat đi", or `/fk-concat`) before concatenating.

## Important rules

- **Mandatory Individual Video Review Gate (CRITICAL):** Ra video là User review luôn từng clip riêng lẻ! Never auto-concatenate into a final video until the user has reviewed and approved all individual clips.
- **Auto-retry rule (CRITICAL):** Videos must be automatically retried up to 5 times before giving up.
- **Immediate download (CRITICAL):** Download scene videos to `${OUTDIR}/scenes/` as soon as they complete.
- **Auto-review (CRITICAL):** ALWAYS run vision review (`/fk-review-video`) automatically after generation.
- **GENERATE vs REGENERATE:** `GENERATE_VIDEO` skips scenes already `COMPLETED`. To force-regenerate, reset `${ori}_video_status` to `PENDING` first, then submit.
- **Cascade on regen:** Regenerating a video auto-clears the upscale status for that scene.
- **Chain video prompt rule (CRITICAL):** Chain scenes with children use `transition_prompt` for video generation, NOT `video_prompt`. This is because the video transitions from the current scene's image to the child scene's image. When fixing chain scene videos, always update `transition_prompt`. `video_prompt` is only used for ROOT scenes or leaf scenes (no children).
- **Chain cascade (CRITICAL):** When regenerating a scene that has CONTINUATION children, you MUST also regenerate images + videos for all descendants in the chain. The child's image was EDIT_IMAGE'd from the parent's old image — if the parent's video changes, the child's start frame won't match the parent's end frame.
  - Walk the full chain to the leaf: `parent_scene_id` links form the chain
  - Regen child images **sequentially** (each child depends on parent completing first)
  - **Update `end_scene_media_id`**: After each child image regen completes, PATCH parent's `${ori}_end_scene_media_id` = child's new `${ori}_image_media_id`. This is CRITICAL — without it, video gen uses stale end frame and the video won't transition to the child's image.
  - After all images complete + end_scene_media_ids updated, regen the **parent video too** (so its end frame matches child's new start image)
  - Then batch regen videos for all children (parent + children can be parallel)
  - **Always proactively propose this cascade to the user** — don't wait for them to notice the mismatch

