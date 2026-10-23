---
name: sw-workflow
description: 'Project orchestrator for the screenwriting skill set (Workflow Scheduling, State Management, and Story Bible) — a meta-skill that routes a screenplay, stage-play, or narrative film project through progressive creative stages (premise → structure → character → scenes → draft → revision → submission) and TV/streaming series projects through a dedicated series stage pipeline (engine → character web & season arc → bible → pilot structure → breaking story & outline → draft → pitch package). Names which sw-* skill to invoke at each milestone, defines deliverables and advisory exit gates, and preserves all project state in story-bible.md across sessions. Use when starting a new script project, resuming an existing one, deciding "what to do next", or coordinating the entire screenwriting suite.'
---

# Screenwriting Project Orchestrator & Story Bible (sw-workflow)

> **Output Language:** English (or matching user query language). All terminology anchors to original craft terms (see [terms.md](terms.md)).

This meta-skill acts as the central conductor for the entire `sw-*` screenwriting suite. It does not introduce competing craft theories; rather, it performs two essential operational functions:
1. **Stage Scheduling:** Directs which specialized skill to invoke at each step, what deliverables must be produced, and what advisory benchmarks define readiness to advance.
2. **State Persistence:** Preserves all creative decisions, loglines, character rosters, and structural outlines in a localized `story-bible.md` file so context is never lost across sessions.

---

## 1. Session Protocol (Start, Progress, and Wrap)

### Session Start
1. Look for `story-bible.md` in the current workspace or designated script directory.
2. **If Found:** Read only the three operational sections: *Current Stage*, *Locked Decisions*, and *Decision Log*. Recap in three concise sentences:
   - What the project is.
   - What stage it has reached.
   - What key decisions were locked during the previous session.
   *Immediately dive into the active stage without re-debating settled decisions unless the user explicitly requests a revision.*
3. **One-Off Deliverables (No Bible Required):** If the user requests an immediate, standalone deliverable (e.g., a one-page pitch, an episode beat sheet, a coverage analysis) that will not require persistent multi-session tracking, bypass creating a bible.
4. **If Not Found (New Project):** Identify the entrance path (see Section 3), initialize `story-bible.md` using the reference template, populate the Project Metadata and Current Stage, and leave future stages blank. Do not bombard the user with more than 3–4 questions at once; infer what is obvious and tag as `(Pending Confirmation)`.

### During the Session
- As each stage deliverable is finalized, immediately record it in the corresponding section of `story-bible.md` and increment the *Current Stage*.
- Any major pivot (revising the premise, changing the ending, cutting a lead character) must be logged with one line in the *Decision Log*: `Date | What was altered | Strategic rationale`.
- Keep `story-bible.md` concise and high-level (~20K–25K tokens maximum). Record final conclusions rather than messy brainstorming notes. Full scripts, step outlines, and treatments belong in their own dedicated files (`script.md`, `outline.md`), with only their file paths referenced in the bible.

### Session Wrap
- Ensure `story-bible.md` reflects all newly locked decisions.
- Conclude with a single clear sentence: `Next Step: [Actionable task for next session]`.

---

## 2. Feature Film & Narrative Stage Pipeline

| # | Stage | Invoked Skill | Stage Deliverable (Written to `story-bible.md`) | Advisory Pass Gate |
|---|---|---|---|---|
| **0** | **Kickoff & Scope** | `sw-workflow` | Project metadata, format, target audience, runtime, entrance path | Clear concept of genre, length, and intended medium |
| **1** | **Premise & Theme** | `sw-premise-theme` | Spark & personal resonance, Core What-If, **Egri Premise** (Trait + Conflict + Climax), **McKee Controlling Idea** (Value + Cause), **Third Rail** (Desire vs. Misbelief), Dramatic Core, Logline | Exactly one central premise; passes the stranger pitch test; dramatic core is essential to plot; theme locked |
| **2** | **Structure** | `sw-story-structure` | Four cornerstones (Beginning, Ending, Plot Point I, Plot Point II), Midpoint nature (False Peak / False Valley), BS2 Beat Sheet with page anchors, Subplot alignment | Ending known before writing; Catalyst by pg 12; Break into Two by pg 25; Midpoint mirrors All Is Lost; shortest act is Act III |
| **3** | **Character & Conflict** | `sw-character-conflict` | 3D character profiles, Orchestration matrix, Unity of Opposites binding, Adversary's leverage ("knife"), Origin Scenes, 10-step conflict escalation | Protagonist is most dimensional; adversary total power exceeds hero; no duplicate character archetypes; no deus ex machina |
| **4** | **Step Outline & Beats** | `sw-scene-craft` + `sw-format-adaptation` | Step Outline (Scene #, Slugline, Dramatic Objective, Value Turn `+` to `-`, Structural Beat), 40-Card Board, Core props and image system | Every scene turns on a value; Act III contains multi-step set pieces; transitions established; zero pure-exposition scenes |
| **5** | **First Draft Pages** | `sw-dialogue` + `sw-format-adaptation` | Master screenplay file (`.fountain` or industry standard format), page count tracking, daily velocity | Page count within target range; format conforms to industry rules; dialogue passes the Cover-the-Names test |
| **6** | **Revision & Diagnostic** | Diagnostic Checklists across skills | Prioritized revision punch-list, track changes, version history | Audited against Structural (13), Character (14), Scene (13), and Dialogue (12) diagnostic checklists |
| **7** | **Industry Package** | `sw-industry-business` | Query letter, 1-page synopsis, pitch deck text, target buyer / festival strategy | Passes the 7-element PROBLEM concept test; logline verified |

---

## 3. Project Entrance Paths

| User Starting Context | Pipeline Path | Strategic Guidance |
|---|---|---|
| **Feature / Narrative Film from Scratch** | Full 0 → 7 sequence | Standard rigorous path. |
| **Existing Draft Needing Polish / Rewrite** | Reverse-Audit 1–3 → 6 | Extract premise, structure, and character traits from the existing script into the bible; missing elements form the immediate revision punch-list. |
| **Adapting a Novel, Play, or True Story** | `sw-format-adaptation` → 1 → 2... | Answer the 4 adaptation questions first: *Where is the original conflict centered? What must be invented or dramatized visually?* Confirm rights and life-story agreements. |
| **Short Film / One-Act Drama** | 1 → 2 (Lu Jun dynamic arc) → 3 → 5 | Compress the board to 10–15 scene cards; maximum 3–5 characters; must possess an undeniable Dramatic Core. |
| **Television / Streaming Series / Pilot** | Series Pipeline (S0–S7) | The series engine takes precedence over the pilot script: *Prove the engine can generate 100 episodes before writing Episode 1.* |
| **Half-Hour Comedy / Sitcom** | S0–S7 (with `sw-sitcom-comedy`) | Tailor page counts, multi-cam vs. single-cam formats, and rapid joke density. |
| **Raw Idea / Logline Validation** | Stage 1 → Stage 7 PROBLEM test | Test the concept's market viability before investing time in structural treatment. |

---

## 4. Television & Streaming Series Pipeline (S0–S7)

A series is not merely an extended feature film. A film represents a closed arc with a single resolution; a series is a **sustainable dynamic engine** driven by unresolved interpersonal tension, act-outs, multi-strand runners (A/B/C stories), and character webs built for longevity.

| # | Stage | Invoked Skill | Deliverable | Advisory Pass Gate |
|---|---|---|---|---|
| **S0** | **Platform & Format** | `sw-workflow` | Network/Streaming specs, 1-hour vs. 30-min, episode count, season arc scope | Clear broadcast commercial breaks vs. streaming continuous structure |
| **S1** | **Series Engine & Franchise** | `sw-series-engine-bible` + `sw-premise-theme` | Thematic thesis vs. antithesis, 4 Franchise Elements (Concept, Conflict, Theme, Story Pattern), Tacit Contract, 5–6 episode story springboards | Engine easily generates future seasons; springboards do not repeat identical conflict dynamics |
| **S2** | **Character Web & Season Arc** | `sw-series-engine-bible` + `sw-character-conflict` | 3–5 lead profiles, irreconcilable character dynamics, Season Arc grid (Episode x Character Want/Wound), Tentpoles | Characters cannot comfortably agree; every lead has something vital to lose; finale resolves *this season's question*, not the overall series engine |
| **S3** | **Series Bible & Pitch Docs** | `sw-series-engine-bible` | Logline & Springboard, Pitch Deck, Master Series Bible, Multi-strand storyline grid | A stranger can read the bible and immediately explain what happens each week |
| **S4** | **Pilot Structural Design** | `sw-series-structure` | Pilot type (Premise vs. Typical Episode vs. Hybrid), Act breakdown, Act-Out cliffhangers, A/B/C plot entry/exit points | Every act-out poses an urgent new dilemma; C-story runner carries character texture; invisible acts clearly defined |
| **S5** | **Breaking Story & Outline** | `sw-writers-room` + `sw-scene-craft` | Beat sheet (6–8 scenes per act) → locked Scene Outline | Every scene has a tangible objective and value turn; changes to the ending are reflected in the outline |
| **S6** | **Pilot Script & Table Read** | `sw-dialogue` + `sw-format-adaptation` | Production-ready pilot script, cold read notes, rewrite passes | Script page count fits industry timing; cold readers ask: *"What happens next?"* |
| **S7** | **Pitch Package & Strategy** | `sw-industry-business` | 20-minute pitch script, 1-page leave-behind, target buyer list | Focused pitch tailored to specific network/streamer mandates |

---

## 5. Minimal Stage Execution Rules

You do not need to re-read every skill file in its entirety before taking action. For each active milestone:
1. Review the designated skill's **Workflow** and **Diagnostic Checklist** sections first.
2. Consult detailed body chapters only when confronting a specific creative roadblock.
3. Reference `reference.md` for masterclass examples and worked case studies.

---

## 6. Subagent & Concurrency Boundaries

- **Never split sequential narrative stages across parallel agents:** Premise, structure, character psychology, and scene beats form an organic continuum. Fracturing them across disjointed agents causes catastrophic continuity breaks and hallucinations.
- **Allowed Parallel Tasks:**
  1. *Multi-Angle Diagnostic Passes (Stage 6):* Parallel read-only agents can audit a completed draft simultaneously (one inspecting structural turns, another vetting dialogue authenticity, another auditing formatting rules).
  2. *Deep Background Research:* Spawning an agent to gather historical context, medical accuracy, or technical procedures without cluttering the primary creative thread.
- *Parallel subagents must be read-only; all updates to `story-bible.md` must be committed directly in the main orchestrator session.*

---

## 7. Language and Terminology Contract

1. **Output Language = User Request Language:** Converse and deliver documents in the language requested by the user (English, Vietnamese, Japanese, etc.).
2. **Standard Craft Terminology:** Screenwriting craft vocabulary anchors to established international English terminology (e.g., *Logline, Inciting Incident, Beat Sheet, Act-Out, Subtext, Turning Point, All Is Lost*). Never invent confusing, ad-hoc translations for established industry terms.
3. **Script Language Integrity:** The language of the screenplay itself is governed by the fictional world and creative agreement. Maintain proper script format conventions regardless of the conversational language used in chat.

---

## 8. Screenwriter & Director Division of Labor (Luo Huaizhen)

1. The screenwriter creates the structural architecture and literary soul; the director renders it in dynamic three-dimensional cinematic space.
2. The screenwriter must guard the core thematic premise and moral dilemma fiercely, while remaining flexible regarding physical blocking, lens choices, and staging adjustments.
3. When notes or revisions are accepted, **the writer must execute the rewrite personally** to preserve narrative coherence and distinct character voice.
4. Collaboration is a **multiplicative partnership**, never subtractive.

---

## 9. Comprehensive Workflow Self-Audit

1. Does the workspace contain an active, up-to-date `story-bible.md`?
2. Has the active session advanced at least one concrete stage deliverable?
3. Is `story-bible.md` concise, readable, and free of sprawling scratchpad debates?
4. Have all foundational pivots (premise, character, ending changes) been recorded in the Decision Log?
5. Does the session conclude with a single, unambiguous Next Step?

