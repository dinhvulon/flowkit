# EMBERS v7: production by act

Written for: the user and the production agent. Script, prompts and runtime are unchanged (v7, 10:02, 119 clips); this file only splits production into five stages.

Hook (0:00–0:24.5, 7 re-cuts) is cut in the edit from clips of later acts; nothing is generated for it. It is assembled after Act 2B (needs RR-06, EM-02, CH-02, RR-02, BN-02, LS-02, RR-07, plus audio from EM-01, EL-06, FL-13).

| Act | Clips | Time (usable) | Videos | Start frames to generate | Last-frame chain (no image) | Two native voices | Hardest shots (test first) | Locations |
|---|---|---|---|---|---|---|---|---|
| **Act 1 — Setup & the line** | RA-02 → EM-03 | 0:24.5–3:10.0 (166s) | 34 | 34 | — | RA-02 | FL-08, FL-09, FL-11, MP-05 | Fire Line, Hale Ranch, Keller Barn, Ridge Road, Staging Area |
|  | *morning sale → fire line → wind turns → Eli at the barn → Eli missing* | | | | | | | |
| **Act 2A — The choice & Ridge Road** | CH-00 → RR-12 | 3:10.0–4:54.5 (104s) | 21 | 21 | — | — | RR-13 | Cedar Flat, Keller Barn, Ridge Road, Staging Area |
|  | *dispatch says no → Ray blocks her → into the fire → Cedar Flat (1) → Keller's gate* | | | | | | | |
| **Act 2B — The barn & the escape** | BN-01 → LH-09 | 4:54.5–6:44.0 (110s) | 23 | 22 | BN-13b | BN-04 | BN-13b, ES-05, LH-05 | Cedar Flat, Keller Barn, Ridge Road |
|  | *barn fight → roof collapses → escape, way down cut off → Cedar Flat (2), Ray stays* | | | | | | | |
| **Act 3A — All is lost & trust** | LS-01 → TR-08 | 6:44.0–8:11.5 (88s) | 19 | 18 | LS-05b | TR-01 | LS-01 | Ridge Road, The Black |
|  | *trapped, no radio, shelter fits one → the mare bolts → Nora follows Eli uphill* | | | | | | | |
| **Act 3B — Burnover & dawn** | BK-01 → DW-09 | 8:11.5–10:02.0 (110s) | 22 | 22 | — | — | BK-14 | Cedar Flat, The Black |
|  | *the black → burnover under the foil → mother reveal → dawn, the cost, final image* | | | | | | | |

Totals: 119 videos, 117 start-frame images, 2 last-frame chains.

## Files per act
- `prompts_v7_<act>.json`: the act's clips from `prompts_v7.json` (same objects, same order).
- `vn_v7_<act>.json`: the act's Vietnamese review sheet.

## Order inside each act (every step that spends credits waits for the user's yes, Rule 29)
1. Create the act's scenes on the server (`POST /api/scenes`, `duration` set on every scene); no credits.
2. Test the hardest shot of the act first (Act 1: FL-08), start frame + video, review.
3. Start frames for the rest of the act in batches of 3 → download → de-watermark → upload clean → Review Board → **user approves**.
4. Videos (Omni Flash r2v, start frame + refs) in batches of 3 → 720p download → `/fk-review-video` scorecard → **user approves** (keep ≥ 9/10).
5. Last-frame chains (BN-13b, LS-05b) only after the clip before them is approved.
6. Upscale 1080p + de-watermark only for approved clips; edit at the end (Rule 66).

## Before Act 1
- Wire multi-voice in the pipeline before RA-02 (Act 1), BN-04 (Act 2B), TR-01 (Act 3A).
- Optional ref fixes still open: Fire Line (white side strips), Nora Body Fire (radio in the chest pouch, bandana on the right wrist).
