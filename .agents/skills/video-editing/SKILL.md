---
name: video-editing
description: 'AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw capture through FFmpeg, Remotion, ElevenLabs, fal.ai, and final polish in Descript or CapCut. Use when the user wants to edit video, cut footage, create vlogs, or build video content.'
---

# Video Editing

AI-assisted editing for real footage. Not generation from prompts. Editing existing video fast.

## FlowKit: dùng cùng `/fk-capcut-edit` và MCP `capcut` (CLAUDE.md Rule 66)

Trong repo FlowKit, phần này đứng trên mọi mục bên dưới. Skill này lo phần máy làm (ffmpeg, dò im lặng / đổi cảnh, EDL); dựng và tinh chỉnh đi qua CapCut.

**Khi nào gọi gì:**

| Việc | Dùng |
|---|---|
| Kế hoạch dựng theo giây: trailer phút đầu, đổi hình 3–5s, re-hook 3:00 / 6:00, card chữ, nhạc, Shorts | `/fk-capcut-edit` (đọc `skills/fk-capcut-edit/SKILL.md`, ghi `output/<slug>/capcut_edit_sheet.md`) |
| Intro trailer 30s / 45s | `/fk-capcut-edit` → `skills/fk-capcut-edit/scripts/trailer_cuts.py` (`scan` → user duyệt cutlist → `build`) |
| Đặt clip, cắt in/out, card chữ, âm lượng nhạc vào draft CapCut | MCP `capcut` theo `/fk-capcut-edit` mục 2b: `create_project` (tên `<slug> edit_vN`) → `add_clip` → `trim_clip` → `add_text` → `set_clip_volume` → `get_timeline` |
| Dò khoảng chết, cảnh trùng, điểm cắt thoại | Layer 3 / "Scene Detection" bên dưới + mốc từng từ Whisper (`tools/review_dialogue.py`, Rule 67) |
| Bản nháp nhanh không cần CapCut, cắt / ghép hàng loạt, proxy, reframe 9:16 dự phòng | ffmpeg (Layer 3, "Social Media Reframing") |
| Chuyển cảnh, màu, phụ đề, xuất file | User làm tay trong CapCut (MCP không có các tool này) |

**MCP `capcut`:** cài ở phạm vi user (`cmd.exe /c C:\Users\Administrator\capcut-mcp\start-mcp.bat`), ghi thẳng file draft JSON của CapCut Desktop, thời gian tính bằng mili giây, mỗi lần ghi có `.bak`. Trước khi ghi: nhắc user **đóng draft đó trong CapCut**. Không ghi đè draft đã giao, luôn tạo `edit_vN` mới. Tool MCP chưa có trong phiên (`claude mcp get capcut` không Connected) → làm Bảng dựng để user tự dựng.

**Giới hạn FlowKit cho các Layer bên dưới:**
- Layer 1 Capture: bỏ. Đầu vào là clip đã duyệt `output/<slug>/1080/*_1080p_clean.mp4`; bản nháp có thể dùng 720p trong `scenes/`, bản xuất cuối thì không.
- Layer 5 (ElevenLabs, fal.ai, VideoDB) và VideoDB reframe: không dùng. Giọng nói dùng thoại gốc Omni hoặc `/fk-gen-narrator`; nhạc dùng `/fk-gen-music`; mọi bước tốn credit hỏi trước (Rule 29).
- Âm thanh: master −14 LUFS / −1 dBTP theo `/fk-sound-design`, không dùng `loudnorm I=-16`.
- Không burn phụ đề vào hình.
- Script ffmpeg / Remotion tạm đặt trong scratchpad; EDL và bản dựng lưu `output/<slug>/edit/` với số phiên bản (`edit_vN_edl.md`).

## When to Activate

- User wants to edit, cut, or structure video footage
- Turning long recordings into short-form content
- Building vlogs, tutorials, or demo videos from raw capture
- Adding overlays, subtitles, music, or voiceover to existing video
- Reframing video for different platforms (YouTube, TikTok, Instagram)
- User says "edit video", "cut this footage", "make a vlog", or "video workflow"

## Core Thesis

AI video editing is useful when you stop asking it to create the whole video and start using it to compress, structure, and augment real footage. The value is not generation. The value is compression.

## The Pipeline

For measured reference-driven work, chain `taste-distillation` into
`taste-application`, then return here for the editor and final-output review.
The standalone taste skills can use existing footage; generation is optional.

Before live editor or DAW changes, save a versioned project checkpoint and
verify the file exists. Save and verify another checkpoint after the changes.
An API readback proves the current in-memory state, not that it was saved.
Keep rendered media, editable projects, and creative approval as separate
states in the handoff.

For MIDI-driven audio, check pitches against the receiving rack's note mapping
and audition the result; successful clip creation can still produce silence.
For reconstructed projects, validate through native load and save, sort events
in timeline order, verify sample links and mute states, then check and audition
the exact exported audio for unintended silence. XML parsing alone does not
prove that the DAW accepted every clip or produced audible output.
Check a bridge's capability handshake before invoking newer commands. Do not
enable upload or training-data telemetry as a side effect of a creative task;
use a supported local control path when consent or capability is absent.

```
Screen Studio / raw footage
  → Claude / Codex
  → FFmpeg
  → Remotion
  → ElevenLabs / fal.ai
  → Descript or CapCut
```

Each layer has a specific job. Do not skip layers. Do not try to make one tool do everything.

## Layer 1: Capture (Screen Studio / Raw Footage)

Collect the source material:
- **Screen Studio**: polished screen recordings for app demos, coding sessions, browser workflows
- **Raw camera footage**: vlog footage, interviews, event recordings
- **Desktop capture via VideoDB**: session recording with real-time context (see `videodb` skill)

Output: raw files ready for organization.

## Layer 2: Organization (Claude / Codex)

Use Claude Code or Codex to:
- **Transcribe and label**: generate transcript, identify topics and themes
- **Plan structure**: decide what stays, what gets cut, what order works
- **Identify dead sections**: find pauses, tangents, repeated takes
- **Generate edit decision list**: timestamps for cuts, segments to keep
- **Scaffold FFmpeg and Remotion code**: generate the commands and compositions

```
Example prompt:
"Here's the transcript of a 4-hour recording. Identify the 8 strongest segments
for a 24-minute vlog. Give me FFmpeg cut commands for each segment."
```

This layer is about structure, not final creative taste.

## Layer 3: Deterministic Cuts (FFmpeg)

FFmpeg handles the boring but critical work: splitting, trimming, concatenating, and preprocessing.

### Extract segment by timestamp

```bash
ffmpeg -i raw.mp4 -ss 00:12:30 -to 00:15:45 -c copy segment_01.mp4
```

### Batch cut from edit decision list

```bash
#!/bin/bash
# cuts.txt: start,end,label
while IFS=, read -r start end label; do
  ffmpeg -i raw.mp4 -ss "$start" -to "$end" -c copy "segments/${label}.mp4"
done < cuts.txt
```

### Concatenate segments

```bash
# Create file list
for f in segments/*.mp4; do echo "file '$f'"; done > concat.txt
ffmpeg -f concat -safe 0 -i concat.txt -c copy assembled.mp4
```

### Create proxy for faster editing

```bash
ffmpeg -i raw.mp4 -vf "scale=960:-2" -c:v libx264 -preset ultrafast -crf 28 proxy.mp4
```

### Extract audio for transcription

```bash
ffmpeg -i raw.mp4 -vn -acodec pcm_s16le -ar 16000 audio.wav
```

### Normalize audio levels

```bash
ffmpeg -i segment.mp4 -af loudnorm=I=-16:TP=-1.5:LRA=11 -c:v copy normalized.mp4
```

## Layer 4: Programmable Composition (Remotion)

Remotion turns editing problems into composable code. Use it for things that traditional editors make painful:

### When to use Remotion

- Overlays: text, images, branding, lower thirds
- Data visualizations: charts, stats, animated numbers
- Motion graphics: transitions, explainer animations
- Composable scenes: reusable templates across videos
- Product demos: annotated screenshots, UI highlights

### Basic Remotion composition

```tsx
import { AbsoluteFill, Sequence, Video, useCurrentFrame } from "remotion";

export const VlogComposition: React.FC = () => {
  const frame = useCurrentFrame();

  return (
    <AbsoluteFill>
      {/* Main footage */}
      <Sequence from={0} durationInFrames={300}>
        <Video src="/segments/intro.mp4" />
      </Sequence>

      {/* Title overlay */}
      <Sequence from={30} durationInFrames={90}>
        <AbsoluteFill style={{
          justifyContent: "center",
          alignItems: "center",
        }}>
          <h1 style={{
            fontSize: 72,
            color: "white",
            textShadow: "2px 2px 8px rgba(0,0,0,0.8)",
          }}>
            The AI Editing Stack
          </h1>
        </AbsoluteFill>
      </Sequence>

      {/* Next segment */}
      <Sequence from={300} durationInFrames={450}>
        <Video src="/segments/demo.mp4" />
      </Sequence>
    </AbsoluteFill>
  );
};
```

### Render output

```bash
npx remotion render src/index.ts VlogComposition output.mp4
```

See the [Remotion docs](https://www.remotion.dev/docs) for detailed patterns and API reference.

## Layer 5: Generated Assets (ElevenLabs / fal.ai)

Generate only what you need. Do not generate the whole video.

### Voiceover with ElevenLabs

```python
import os
import requests

resp = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
    headers={
        "xi-api-key": os.environ["ELEVENLABS_API_KEY"],
        "Content-Type": "application/json"
    },
    json={
        "text": "Your narration text here",
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
)
with open("voiceover.mp3", "wb") as f:
    f.write(resp.content)
```

### Music and SFX with fal.ai

Use the `fal-ai-media` skill for:
- Background music generation
- Sound effects (ThinkSound model for video-to-audio)
- Transition sounds

### Generated visuals with fal.ai

Use for insert shots, thumbnails, or b-roll that doesn't exist:
```
generate(app_id: "fal-ai/nano-banana-pro", input_data: {
  "prompt": "professional thumbnail for tech vlog, dark background, code on screen",
  "image_size": "landscape_16_9"
})
```

### VideoDB generative audio

If VideoDB is configured:
```python
voiceover = coll.generate_voice(text="Narration here", voice="alloy")
music = coll.generate_music(prompt="lo-fi background for coding vlog", duration=120)
sfx = coll.generate_sound_effect(prompt="subtle whoosh transition")
```

## Layer 6: Final Polish (Descript / CapCut)

The last layer is human. Use a traditional editor for:
- **Pacing**: adjust cuts that feel too fast or slow
- **Captions**: auto-generated, then manually cleaned
- **Color grading**: basic correction and mood
- **Final audio mix**: balance voice, music, and SFX levels
- **Export**: platform-specific formats and quality settings

This is where taste lives. AI clears the repetitive work. You make the final calls.

In FlowKit, the rough cut is placed into a CapCut draft by the `capcut` MCP (see "FlowKit" above and `/fk-capcut-edit` §2b); the user then polishes and exports in CapCut.

## Social Media Reframing

Different platforms need different aspect ratios:

| Platform | Aspect Ratio | Resolution |
|----------|-------------|------------|
| YouTube | 16:9 | 1920x1080 |
| TikTok / Reels | 9:16 | 1080x1920 |
| Instagram Feed | 1:1 | 1080x1080 |
| X / Twitter | 16:9 or 1:1 | 1280x720 or 720x720 |

### Reframe with FFmpeg

```bash
# 16:9 to 9:16 (center crop)
ffmpeg -i input.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" vertical.mp4

# 16:9 to 1:1 (center crop)
ffmpeg -i input.mp4 -vf "crop=ih:ih,scale=1080:1080" square.mp4
```

### Reframe with VideoDB

```python
from videodb import ReframeMode

# Smart reframe (AI-guided subject tracking)
reframed = video.reframe(start=0, end=60, target="vertical", mode=ReframeMode.smart)
```

## Scene Detection and Auto-Cut

### FFmpeg scene detection

```bash
# Detect scene changes (threshold 0.3 = moderate sensitivity)
ffmpeg -i input.mp4 -vf "select='gt(scene,0.3)',showinfo" -vsync vfr -f null - 2>&1 | grep showinfo
```

### Silence detection for auto-cut

```bash
# Find silent segments (useful for cutting dead air)
ffmpeg -i input.mp4 -af silencedetect=noise=-30dB:d=2 -f null - 2>&1 | grep silence
```

### Highlight extraction

Use Claude to analyze transcript + scene timestamps:
```
"Given this transcript with timestamps and these scene change points,
identify the 5 most engaging 30-second clips for social media."
```

## What Each Tool Does Best

| Tool | Strength | Weakness |
|------|----------|----------|
| Claude / Codex | Organization, planning, code generation | Not the creative taste layer |
| FFmpeg | Deterministic cuts, batch processing, format conversion | No visual editing UI |
| Remotion | Programmable overlays, composable scenes, reusable templates | Learning curve for non-devs |
| Screen Studio | Polished screen recordings immediately | Only screen capture |
| ElevenLabs | Voice, narration, music, SFX | Not the center of the workflow |
| Descript / CapCut | Final pacing, captions, polish | Manual, not automatable |

## Key Principles

1. **Edit, don't generate.** This workflow is for cutting real footage, not creating from prompts.
2. **Structure before style.** Get the story right in Layer 2 before touching anything visual.
3. **FFmpeg is the backbone.** Boring but critical. Where long footage becomes manageable.
4. **Remotion for repeatability.** If you'll do it more than once, make it a Remotion component.
5. **Generate selectively.** Only use AI generation for assets that don't exist, not for everything.
6. **Taste is the last layer.** AI clears repetitive work. You make the final creative calls.

## Native Fusion Presets

[ITO Production v1](assets/fusion/ito-production-v1/README.md) provides restrained highlight bloom, opposing RGB spatial offsets and a luminance/edge halo. The exact files passed prior native import, save/reopen and short motion-render checks after two-source visual review. These are starting values requiring shot-specific review; the halo does not detect or track subjects.

[ITO V28](assets/fusion/ito-v28/README.md) contains preserved, native-verified Fusion graph snippets and an idempotent Lua installer. These are technical compatibility examples, **not recommended production defaults**: their documented visual limitations require tuning and taste review before use. See the bundle provenance for the scope of prior import and render checks.

## Related Skills

- `fal-ai-media` — AI image, video, and audio generation
- `videodb` — Server-side video processing, indexing, and streaming
- `content-engine` — Platform-native content distribution

