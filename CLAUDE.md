# Flow Kit

Base URL: `http://127.0.0.1:8100`

## Pre-flight

Before ANY workflow:
```bash
curl -s http://127.0.0.1:8100/health
# Must return: {"extension_connected": true}

curl -s http://127.0.0.1:8100/api/flow/status
# Must return: {"transport": "batch", "flow_project_id": "<uuid>", ...}
```

Also needed: **one signed-in `https://flow.google.com/` tab left open**. Only the
page can sign a Flow request, so nothing works headless.

## Critical Rules (MUST follow)

1. **Media ID is always UUID** — format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`. Never use `CAMS...` / base64 strings.
2. **Scene prompts = ACTION only** — never describe character appearance. Reference images handle visual consistency via `imageInputs`.
3. **All reference images must exist before scene images** — verify every entity has `media_id` before generating scene images.
4. **No throwaway scripts in repo & Scratch Directory Only** — NEVER write Python, shell, or any script file in `scripts/`, `tools/`, or project root to loop over API requests or run temporary test/debug code. Use `POST /api/requests/batch` to submit all requests at once, then poll `GET /api/requests/batch-status`. Any temporary test, debug, or one-off scripts MUST strictly be placed in the conversation scratch directory (`<appDataDir>/brain/<conversation-id>/scratch/`).
5. **Reference images are always 16:9 (landscape)** — characters included. A character ref is one 16:9 multi-view sheet (e.g. face close-up | 3/4 | full body in outfit); locations are a single landscape shot.
6. **UUID extraction** — if a response gives `CAMS...` instead of UUID, extract UUID from the `fifeUrl` in the response URL: `/image/{UUID}?...`.
7. **Cascade on regen** — regenerating an image auto-clears downstream video + upscale.
8. **REGENERATE vs GENERATE** — `GENERATE_*` skips if already COMPLETED. `REGENERATE_*` always runs (clears + regenerates).
9. **Image Material required** — every project needs a `material` field (e.g. `realistic`, `3d_pixar`, `anime`). List available: `GET /api/materials`.
10. **Server handles throttling — EVERY Flow request spaced 45–60s** — every call the server sends to Flow (image/video/upscale submit, image upload, project creation, status polls, metadata reads) waits a random 45–60s after the previous one (`FLOW_GENERATION_MIN_INTERVAL_S=45` / `FLOW_GENERATION_MAX_INTERVAL_S=60` in `agent/config.py`; `VIDEO_POLL_TIMEOUT=900` to fit the slower polls). User-set 2026-10-04: bursts trip `PUBLIC_ERROR_UNUSUAL_ACTIVITY`. Submit ALL requests via `/batch` and let the server pace them; do NOT loop faster. If a script paces its own submits, use `random.uniform(45, 60)` between requests and stop on `UNUSUAL_ACTIVITY` / `QUOTA`.
11. **Video prompts use sub-clip timing** — structure 8s video as time segments: `0-3s: [action]. 3-6s: [action]. 6-8s: [action].`
12. **Character dialogue in sub-clips** — embed speech in quotes: `Luna says "Goodnight."` Max 10-15 words per character per 2-3s segment.
13. **Scenes are mutable** — use `PATCH /api/scenes/{sid}` to update `prompt`, `video_prompt`, `narrator_text`, `character_names` after creation. Don't delete and recreate — patch instead.
14. **Fact-check before scripting** — ALWAYS research events via web search before writing project stories, scene prompts, or narrator text. Facts (events, dates, names, operations, outcomes) MUST match real sources. Editorial opinion and analysis are allowed but must be framed as such. Never invent events, operation names, or statistics. **Exception (user 2026-10-05): time-travel / POV survival vlogs (`/fk-time-travel-vlog`, `/fk-vlog-guide`) are fiction — invention is allowed and research is optional; see the skill's "Hư cấu được phép" section.**
15. **Real-people bypass** — when characters are based on real famous people (politicians, celebrities, military leaders), NEVER use their real name as entity `name` or anywhere in `description`, `image_prompt`, `prompt`, or `video_prompt`. AI image generators reject known public figures. Instead: (a) use a **role-based alias** as entity name (e.g. "Tổng Tư Lệnh" not "Trump", "Thủ Tướng Sắt" not "Netanyahu"), (b) describe **physical appearance only** — distinctive hair, face shape, build, clothing style — without naming who it is, (c) `narrator_text` may use real titles/roles for storytelling but real names never flow into image/video generation. Keep a `real_reference` mapping in the project plan file (`.omc/research/`) for internal tracking.
16. **Review before upscale** — ALWAYS run `/fk-review-video` (light mode) after video generation, before upscaling. Scenes scoring < 7.5 get `video_prompt` updated from review errors, then regen video. Max 2 review-regen cycles.
17. **Auto-retry failed videos (up to 5x)** — When generating videos, any failure or timeout MUST be automatically retried up to 5 times. If failed due to content filters (e.g. `as29s failed: [5]`), auto-sanitize prompt keywords and call `REGENERATE_IMAGE` to get a fresh start frame before regenerating the video.
18. **Rolling download & Review Before Upscale/Clean (Chưa xóa logo khi mới sinh 720p)** — Khi video 720p sinh xong, lập tức tải về `${OUTDIR}/scenes/scene_{idx}_{sid}.mp4`. **TUYỆT ĐỐI CHƯA CẦN XÓA LOGO Ở BƯỚC NÀY** để tránh lãng phí tài nguyên CPU/GPU và thời gian nếu video cần sửa prompt hoặc regen. Trích xuất frame trực tiếp từ video 720p để chạy AI Review Scorecard và đưa lên Review Board cho User duyệt trước. **CHỈ SAU KHI USER DUYỆT CẢNH**: Gửi lệnh Upscale 1080p (`veo_3_1_upsampler_1080p` qua RPC `p0UkFb`), tải video 1080p về thư mục riêng `${OUTDIR}/1080/scene_{idx}_{sid}_1080p.mp4`, rồi mới chạy `remove_watermark_video` trực tiếp trên bản 1080p (`${OUTDIR}/1080/scene_{idx}_{sid}_1080p_clean.mp4`) để đưa vào Concat cuối cùng.
19. **Mandatory review & Review Board** — Pipeline skills (`/fk-pipeline`, `/fk-gen-videos`) MUST automatically execute `/fk-review-video` immediately after video generation, display the per-scene scorecard table showing which nodes passed and which need regeneration, and ensure the Review Board web app (`python tools/review_server.py 8200`) is running.
20. **Language matching for SEO & Thumbnails** — YouTube metadata (`/fk-youtube-seo`) and thumbnails (`/fk-thumbnail`) MUST match the dialogue/script language (e.g. 100% Japanese for Japanese POV vlogs, Vietnamese for Vietnamese, English for English). Never generate English/Vietnamese SEO for Japanese dialogue vlogs.
21. **Flush stale queue on new project** — whenever starting or creating a new project (e.g. `/fk-create-project`, `/fk-time-travel-vlog`), ALWAYS execute `python -c "import sqlite3; conn = sqlite3.connect('flow_agent.db'); conn.execute('UPDATE request SET status=\\'FAILED\\' WHERE status=\\'PENDING\\''); conn.commit()"` first to flush all stale PENDING requests and prevent worker auto-retry loops causing `PUBLIC_ERROR_UNUSUAL_ACTIVITY`.
22. **Mandatory Scene Image Review before Video Generation** — After generating scene images (Step 6), ALWAYS download images locally to `${OUTDIR}/images/scene_{idx}.jpg`, launch the Image Review Board (`review_images.html`), and pause for user review. Never jump directly into video generation without user approval of the scene start frames. Any unsatisfactory images MUST be resubmitted with `REGENERATE_IMAGE`.
23. **Start Frame is Input Reference Only** — The generated scene image (`start_image_media_id` / start frame) serves strictly as the motion starting anchor. Character identity consistency still requires character reference images (`character_names` + `reference_media_ids` / `imageInputs`) to preserve the locked visual identity across the video.
24. **Laomedeia Voice Profile** — For female travel vloggers / narrators, configure `voice_description` using the **Laomedeia** profile (Google Gemini-TTS: upbeat, mid-high pitched, energetic expressive conversational female voice, fast confident vlog delivery with dry humor, rises into real cracking screams when in danger, drops to a fast whisper when hiding). Structure video prompt dialogue accordingly (`Mia says "..."`) so Veo 3 / Pinhole synthesizes matching native vocal audio. In Omni Flash / Pinhole Reference-to-Video (`MZZa6b`), Slot 7 is natively pinned to `[["laomedeia"]]` by default.
25. **Strict Step-by-Step Review Gates (Images then Videos)** — Pipeline execution MUST proceed strictly step-by-step with explicit human review gates:
    - **Step 6.5 (Image Review Gate)**: As soon as scene images are generated, STOP immediately. Clean image watermarks, download all images to `${OUTDIR}/images/scene_{idx}.jpg`, present the image gallery/review board to the user, and PAUSE. Do NOT generate videos until the user explicitly reviews and approves the start frames.
27. **Omni Flash Ingredients Only (Reference-to-Video / `abra_r2v`)** — Khi tạo video cho các dự án vlog/nhân vật, **TUYỆT ĐỐI KHÔNG tạo ảnh Start Frame (`GENERATE_IMAGE`) rồi chạy Image-to-Video (`i2v`)**. Phương pháp start-frame làm chuyển động bị cứng, dễ méo người và biến dạng khuôn mặt khi chuyển động. **BẮT BUỘC chỉ sử dụng Omni Flash Ingredients (`GENERATE_VIDEO_REFS` / `omni_flash_models.reference_to_video` / `abra_r2v_<duration>s` qua RPC `MZZa6b`)**:
    - Đính kèm trực tiếp các thành phần tham chiếu (Ingredients): Nhân vật (`Mia`), Trang phục (`Mia Outfit`), và Bối cảnh/Địa điểm (`reference_media_ids`).
    - Model `abra_r2v` tổng hợp trực tiếp chuyển động video mượt mà từ các thành phần tham chiếu và prompt, tích hợp khẩu hình native với voice profile **Laomedeia** (Slot 7).
    - Không chạy quy trình `GENERATE_IMAGE` cho từng cảnh; sau khi các entity có `media_id`, gửi thẳng yêu cầu `GENERATE_VIDEO_REFS`.
28. **Clean-Before-Video-Gen (Bắt buộc tẩy logo ảnh trước khi đưa vào sinh video)** — Đối với BẤT KỲ phân cảnh nào cần tạo ảnh Start Frame hoặc ảnh Reference từ Google Flow/AI (như cảnh vũ trụ, drone, phong cảnh thiên nhiên, hoặc start frame chuyển cảnh):
    - **TUYỆT ĐỐI KHÔNG dùng trực tiếp `media_id` do Google Flow tự sinh** để đưa thẳng vào sinh video. Ảnh AI của Google luôn tự chèn watermark logo ở góc dưới; nếu đưa thẳng vào i2v/r2v thì model video sẽ làm logo đó nhấp nháy, méo mó và dính chết vào video.
    - **Quy trình bắt buộc 4 bước đối với mọi ảnh do AI sinh**:
      1. Tải ảnh gốc về máy: `${OUTDIR}/images/scene_{idx}_{sid}.jpg`.
      2. Chạy ngay `python tools/remove_watermark_from_image.py "${OUTDIR}/images/scene_{idx}_{sid}.jpg"` để xóa sạch logo và SynthID ➔ sinh ra file `scene_{idx}_{sid}_clean.jpg`.
      3. Upload file sạch `scene_{idx}_{sid}_clean.jpg` ngược lên Google Flow qua `POST /api/flow/upload-image` để nhận một `media_id` UUID hoàn toàn sạch logo.
      4. Cập nhật `media_id` sạch này vào Scene (`horizontal_image_media_id` / `vertical_image_media_id`), đưa lên Review Board cho user duyệt. CHỈ SAU ĐÓ mới dùng `media_id` sạch này để sinh video!
29. **Confirm before every generation step (overrides the automatic parts of rules 16, 17, 19)** — Generation spends Flow credits, so:
    - **Before** any call that makes Flow generate media (`/fk-gen-refs`, `/fk-gen-images`, `/fk-gen-videos`, `GENERATE_*` / `REGENERATE_*` batches, test clips, retries, review-driven regens), state what will be generated and how many items, then **wait for the user's explicit yes**.
    - **After** each generation step finishes, STOP: show the results for review and wait for approval before starting the next stage (refs → videos → regens → concat).
    - Failures and low review scores are **reported, not auto-retried**: propose the fix (sanitized prompt, regen list) and ask before resubmitting.
    - Non-generating work (creating projects/scenes, uploading existing images, PATCHing fields, downloading, watermark removal) can proceed when the user asks for it.
30. **Vlog production lessons live in `/fk-time-travel-vlog` section 11** (user feedback: constraints as sentences not `Negative:`, phone is the camera, wipes never make the vlogger vanish, scene refs for cities, landscape refs for 16:9, hardest clip first, separate outfit ref `<Vlogger> Outfit` to lock clothing, no `selfie-stick`/phone keywords to avoid ghost devices/screens, pure POV with empty hand, camera locked in hand for run/jump action physics, single-arm vlog holding to prevent dual-arm glitch, crowd fleeing forward with vlogger away from disaster, anti-CGI documentary anchors for disaster scenes). Follow them for every POV/vlog project.
31. **On any pipeline error** (request `FAILED`, stuck `PROCESSING`, `extension_connected: false`, HTTP 4xx/5xx from `:8100`, YouTube `HttpError`, error strings like `UNSAFE_GENERATION` / `not found` / `CAPTCHA` / `NO_AT_TOKEN` / `NO_FLOW_PROJECT` / `UNSUPPORTED_ON_BATCH_API`): invoke `/fk-doctor` before guessing a fix.
32. **AI-First Video Review before User Approval & Conditional Upscale (Tự động review trên video 720p thô ➔ Duyệt ➔ Upscale 1080p & Xóa Logo)** — Sau khi video 720p hoàn tất và tải về máy, Agent trích xuất frames trực tiếp từ video 720p thô (chưa cần xóa logo), tự động chạy phân tích `/fk-review-video` trước: chấm điểm theo 6 tiêu chuẩn cốt lõi (Character Consistency 25%, Prompt Adherence 20%, Motion Quality 20%, Visual Fidelity 15%, Temporal Coherence 10%, Composition 10%), rà soát lỗi AI (Critical/High/Minor), và trình bày bảng Scorecard chi tiết kèm ảnh preview frames cho User xem trước. **Chỉ khi User duyệt thông qua cảnh**: Mới tiến hành gửi batch Upscale 1080p và xóa logo trên video 1080p.
41. **No Behind-the-Head 3rd-Person Shots & Camera Materialization Glitch (Cấm quay sau đầu chuyển selfie & Cấm biến camera thành đạo cụ)** — (1) Cấm shot sau đầu/sau lưng vlogger rồi xoay ra trước mặt (`starts from behind head then turns`). (2) Đơn góc nhìn thay thế hoàn toàn Whip Pan (xem Rule 42): Dùng 100% Selfie Qua Vai hoặc Cặp Shot Kép cắt cảnh riêng biệt. (3) Cấm mô tả camera làm đạo cụ cầm tay; thấu kính chính là điểm nhìn người xem.
42. **Single-Perspective Vlog Purity & No 180° Camera Flips in a Single Shot (Quy tắc đơn góc nhìn thuần khiết & Cấm xoay lật 180° cam trước/cam sau trong 1 shot)** — Mỗi shot 8s–10s giữ duy nhất 1 góc máy cố định: hoặc 100% Selfie (Cam trước 0.5x), hoặc 100% First-Person POV (Cam sau). Tuyệt đối cấm lia xoay 180° giữa hai camera trong cùng 1 shot liên tục. Dùng kỹ thuật Over-the-Shoulder Selfie Interaction (vlogger chiếm 1/3 tiền cảnh, đối tượng 2/3 hậu cảnh, tương tác qua ánh mắt và quay đầu).
43. **Temporary & Debug Scripts in Scratch Directory Only (Tất cả script tạm/debug/test bắt buộc lưu trong `scratch/`)** — Mọi script tạm thời, one-off script để test prompt, debug API, test chức năng, kiểm tra trạng thái hoặc setup tạm (như `test_*.py`, `check_*.py`, `setup_*.py`, `debug_*.py`, `patch_*.py`) TUYỆT ĐỐI KHÔNG được tạo trong các thư mục mã nguồn của dự án (như `scripts/`, `tools/`, hoặc thư mục gốc repo `c:/flowkit/`). BẮT BUỘC chỉ được tạo trong thư mục artifact scratch của cuộc hội thoại (`<appDataDir>/brain/<conversation-id>/scratch/` hoặc chạy inline one-liner `python -c "..."`). Sau khi hoàn tất mục đích debug/test, phải dọn dẹp sạch sẽ để giữ codebase repo luôn sạch, chuẩn và chuyên nghiệp.
44. **Inter-Scene Posture & Gaze Continuity (Khớp tư thế & hướng nhìn giữa 2 shot liền kề — Match on Action)** — Khi Clip A kết thúc ở một tư thế quay đầu/ngoái nhìn, Clip B bắt buộc phải mở đầu ở đúng tư thế đó trong 1-2s đầu rồi mới mô tả nhân vật chuyển đổi tư thế ngay trong khung hình. Điều này biến mối nối giữa 2 clip thành chuyển động Match on Action tự nhiên, xóa bỏ hoàn toàn lỗi giật hình.
45. **Camera-Touch Prevention & Functional Prop Dressing Physics (Chống với tay chạm ống kính & Khóa hành vi mặc/đeo đạo cụ chức năng thực tế)** — (1) Khóa cấm chạm thấu kính: Tay tự do giữ ngang ngực hoặc cách xa camera (`free hand NEVER reaches toward, touches, covers, taps, or points at the camera lens`). (2) Khóa hành vi mặc/đeo đạo cụ chức năng: Phải mô tả trực tiếp động tác xỏ/mặc (`slips and slides directly onto`, `fits securely over`, `pulls over`, `fastens onto`), nhân vật thực sự mặc đồ trên người (`physically wears`), cấm chỉ tả chung chung "giật dây/cầm dây" khiến AI bỏ qua thao tác mặc đồ thực tế. (3) Đồng bộ 3 giai đoạn: 0-3s xỏ/mặc đồ, 3-6s đạo cụ mặc hoàn chỉnh giơ ngang ngực khoe camera, 6-8s cảm xúc & kiểm tra độ ấm/vừa vặn.

## Pipeline Order (Omni Flash R2V Ingredients Workflow)

```
0. Research          /fk-research "topic" (fact-check via web search, save to .omc/research/)
1. Health check      GET  /health → extension_connected: true
2. Create project    POST /api/projects (with entities + material, story from research)
3. Create video      POST /api/videos (HORIZONTAL or VERTICAL)
4. Create scenes     POST /api/scenes (with character_names, duration: 4/6/8/10s, video_prompt)
5. Gen ref images    POST /api/requests/batch (GENERATE_CHARACTER_IMAGE / upload locked refs)
                     Verify all key entities (Character, Outfit, Location) have UUID media_id
6. Gen videos (R2V)  POST /api/requests/batch (type: "GENERATE_VIDEO_REFS")
                     Omni Flash abra_r2v synthesizes clips directly from Ingredients (Character, Outfit)
                     Auto-retry failed videos up to 5x; rolling download 720p clips to scenes/
6.5 Review videos   MANDATORY GATE! Trích xuất frames từ video 720p thô (CHƯA CẦN XÓA LOGO).
                     Display per-scene scorecard table + Review Board (http://localhost:8200).
                     STOP & PAUSE: User reviews each scene clip individually.
                     Nếu chưa đạt: sửa prompt -> REGENERATE_VIDEO (ở mức 720p, không tốn công xóa logo).
7. Upscale 1080p     CHỈ KHI USER DUYỆT CẢNH: POST /api/requests/batch (type: "UPSCALE_VIDEO", RPC p0UkFb)
                     Tải video 1080p về folder 1080/ -> ${OUTDIR}/1080/scene_XX_1080p.mp4
8. De-watermark      Chạy remove_watermark_video TRỰC TIẾP trên bản 1080p -> ${OUTDIR}/1080/scene_XX_1080p_clean.mp4
9. Concat           ffmpeg normalize + concat (dùng toàn bộ video 1080p clean đã duyệt)
10. SEO & Thumbnails Auto-match script language (e.g. 100% native Japanese for Japanese POV vlog)
```

## Since Flow moved (September 2026)

Flow lives at `flow.google.com` and signs every call in the page. Consequences
that change how you work:

- **`POST /api/projects` creates a fresh Flow project** unless you pass
  `flow_project_id`, which reuses an existing one. `FLOW_PROJECT_ID` is optional
  (the default project for internal `/api/flow/*` calls).
- **Two capabilities are unported**, both on the Veo path, because their
  payloads were never captured: **video** upscale (not image export, which
  works) and Veo start+end-frame chaining. They fail with
  `UNSUPPORTED_ON_BATCH_API` rather than silently producing the wrong thing.
  r2v (`GENERATE_VIDEO_REFS`) always runs as Omni Flash Ingredients
  (`MZZa6b` + `abra_r2v_<N>s`); `N` comes from the scene's `duration`
  (4/6/8/10); a missing or invalid `duration` silently becomes 10s — always PATCH it. Omni also covers frame and first+last — use
  `model_family=omni_flash`. `FLOW_ALLOW_DEGRADED=1` (exactly `1`; `true` counts as off) drops Veo
  chaining to plain i2v; video upscale has no fallback. See `docs/CAPTURE.md`.
- **A poll saying "Media not found." is not a failure.** Finished jobs report it.

## Batch API

Submit N requests at once (server paces them automatically — every Flow request spaced a random 45–60s, see rule 10):

```bash
curl -X POST http://127.0.0.1:8100/api/requests/batch \
  -H "Content-Type: application/json" \
  -d '{"requests": [{"type": "...", "scene_id": "...", "project_id": "...", "video_id": "...", "orientation": "VERTICAL"}, ...]}'
```

Poll aggregate status:

```bash
curl -s "http://127.0.0.1:8100/api/requests/batch-status?video_id=<VID>&type=GENERATE_IMAGE"
# Returns: {"total": 40, "pending": 30, "processing": 5, "completed": 5, "failed": 0, "done": false}
# When "done": true → all requests have left the queue (completed or failed)
# When "all_succeeded": true → every request completed successfully
```

## Skills

This project has reusable skills in `skills/`. When the user says `/fk-<name>`, read `skills/fk-<name>.md` and follow the instructions inside.

| Skill | Purpose |
|-------|---------|
| `/fk-add-material` | fk-add-material — Image Material System |
| `/fk-brand-logo` | fk-brand-logo — Apply Channel Branding (Intro + Outro + Logo + 4K Badge) |
| `/fk-camera-guide` | Camera Guide — Cinematic Video Prompts (Veo 3) |
| `/fk-change-model` | fk-change-model — View & Change Video/Image Model Keys |
| `/fk-change-provider` | fk-change-provider — View & Switch the AI CLI for a Role |
| `/fk-concat-fit-narrator` | Trim each scene video to fit its TTS narrator duration, burn text overlays, then concatenate into a final video. |
| `/fk-concat` | Download and concatenate all scene videos into a single video with optional TTS narration. |
| `/fk-create-project` | Create a new Google Flow video project. Ask the user for: |
| `/fk-creative-mix` | Creative video mixing — combine techniques for cinematic results. |
| `/fk-dashboard` | Show live GLA status in Claude Code statusline. |
| `/fk-doctor` | Diagnose any FlowKit error and prescribe a fix. Knows the full error taxonomy across Google Flow, the Chrome extension, the FastAPI layer, the worker, and the YouTube upload pipeline. |
| `/fk-fix-uuids` | Find and fix any non-UUID media_ids (CAMS... format) across all scenes and entities. |
| `/fk-gen-chain-videos` | Generate videos with automatic scene chaining (start+end frame transitions). |
| `/fk-gen-images` | Generate scene images for all scenes in a video. |
| `/fk-gen-music` | fk-gen-music — Generate Music via Suno |
| `/fk-gen-narrator` | fk-gen-narrator — Generate Narrator Text + TTS for All Scenes |
| `/fk-gen-refs` | Generate reference images for all entities in a project. |
| `/fk-gen-text-overlays` | fk-gen-text-overlays — Generate Text Overlays from Narrator Text |
| `/fk-gen-tts-template` | fk-gen-tts-template — Generate Voice Template |
| `/fk-gen-videos` | Generate videos for all scenes in a video. |
| `/fk-import-voice` | fk-import-voice — Import Existing Voice as Template |
| `/fk-insert-scene` | Insert new scene(s) into an existing video chain — for multi-angle shots, cutaways, or close-ups. |
| `/fk-monitor` | fk-monitor — Full Pipeline Monitor |
| `/fk-pipeline` | fk-pipeline — Smart Full-Pipeline Orchestrator |
| `/fk-refresh-urls` | Re-sign expired media URLs for all scenes in a video (images, videos, upscale videos) and character reference images. |
| `/fk-remove-watermark` | fk-remove-watermark — Remove Watermark & Disrupt SynthID from Images and Videos |
| `/fk-research` | fk-research — Fact-Check & Research Before Scripting |
| `/fk-review-board` | Start the Scene Review Board web app for visual feedback on scene chains. |
| `/fk-review-video` | Review AI-generated scene videos for quality using Claude Vision. |
| `/fk-status` | Show full status dashboard for a project. |
| `/fk-switch-project` | fk-switch-project — Switch Active Project |
| `/fk-thumbnail-guide` | YouTube Thumbnail Guide — Hook-Worthy Design Rules |
| `/fk-thumbnail` | Generate 4 YouTube-optimized thumbnail variants for a project video. |
| `/fk-time-travel-vlog` | fk-time-travel-vlog — Time Travel Vlog Orchestrator (Mọi Thời Kỳ, Mọi Địa Điểm) |
| `/fk-upload-image` | Upload a local image file to Google Flow and get a media_id (UUID). |
| `/fk-upload-ref` | fk-upload-ref — Upload Custom Reference Image for Character/Entity |
| `/fk-vlog-guide` | fk-vlog-guide — Master Guide & Interactive Hub for Historical POV Vlogs |
| `/fk-youtube-seo` | fk-youtube-seo — Generate YouTube Metadata (SEO-Optimized) |
| `/fk-youtube-upload` | fk-youtube-upload — Upload Video to YouTube (Shorts + Long-form) |
| `/translate-capcut-srt` | Trích xuất Auto Captions từ CapCut Desktop project và dịch sang ngôn ngữ khác. |
| `/extract-capcut-srt` | Liệt kê project CapCut và trích xuất phụ đề Auto Captions thành file .srt chuẩn. |
