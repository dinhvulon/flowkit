---
name: sw-format-adaptation
description: Screenplay format, page craft, the writing process, and adaptation — merged from Wendy Henson (spec format rules), Richard Walter (page craft, revision discipline), Neill Hicks (selling vs. shooting scripts, draft progression), Syd Field (master scene technique, card method, adaptation as original work), Robert McKee (step outline → treatment → screenplay), Julian Hoxter (format elements, adaptation four questions), Diamond & Weissman (one-page nine-step), and Eric Bork (60/30/10 rule) — including typography standards, element conventions (V.O./O.S., MORE/CONT'D, dual dialogue), the Fountain machine-writable output contract, and international formatting conventions. Use when formatting a spec script, choosing output file types, writing clean action lines, planning draft pipelines, cutting pages, adapting external IP or true stories, or preparing a submission-ready draft.
---

# Screenplay Format, Process & Adaptation (sw-format-adaptation)

> **Output Language:** English (or matching user query language). All terminology anchors to original craft terms (see [terms.md](../sw-workflow/terms.md)).

This skill governs three indispensable disciplines of professional screenwriting:
1. **The Page Craft:** Industry-standard spec formatting, typography, margins, and cinematic action writing.
2. **The Development Pipeline:** Moving systematically from raw premise → step outline → treatment → first draft pages → targeted revision passes.
3. **The Craft of Adaptation:** Translating novels, stage plays, and true events into dynamic visual cinema without being trapped by source prose.

---

## 1. The Selling Script vs. The Shooting Script

- **Neill Hicks’ Golden Rule:** You are writing a **Selling (Spec) Script**, not a production shooting script.
  - Omit scene numbers, camera angles, lens choices, and technical editing transitions.
  - **The Prime Directive: Make the script an effortless, irresistible read.** Never force the reader to work, decode abbreviations, or flip back to figure out where they are. *You are directing the reader’s imagination, not the camera operator.*
- **John Milius:** *"I never write camera directions. I never write 'we close in' or 'we see.' That is an arrogant intrusion. The format only needs to tell the reader whether it is interior or exterior, location, and day or night. The rest should read like an electric novel—clear, muscular, and visually compelling."*
- **Wendy Henson:** An improperly formatted script is rejected before the reader reaches page five. Readers scan formatting first to gauge basic professionalism: *"Never give an executive an easy excuse to throw your script in the trash."*
- **Richard Walter’s Principle 32:** If you want the industry to treat you as a master screenwriter, hold yourself to professional standards.

---

## 2. Hard Spec Formatting Rules

- **Typography & Length:**
  - **Font:** Courier 12 pt exclusively (fixed-width: 10 characters per inch, 6 lines per inch).
  - **Standard Length:** 90–120 pages (1 page ≈ 1 minute of screen time; 100–110 pages is the industry sweet spot). Under 85 suggests amateur shallowness; over 125 signals a lack of narrative discipline.
- **Title Page:**
  - Contains **only** the Title, "Written by", and Author Name (plus contact info / agent info in the bottom corner).
  - Omit draft dates, revision numbers, copyright notices, WGA registration numbers, or decorative artwork.
- **Scene Headings (Sluglines):**
  - All uppercase. `INT.` or `EXT.` + Specific Location + `-` + `DAY` or `NIGHT`.
  - Order moves from general to specific: `INT. LAMBEAU FIELD - LOCKER ROOM - DAY`.
- **Action Paragraphs:**
  - Strict present tense, active voice (*"Paul carries Joe"*, never *"Joe is being carried by Paul"*).
  - Describe only what can be seen by a lens or heard by a microphone (never write *"She stands there contemplating her childhood trauma"*).
  - Keep paragraphs tight (2–4 lines maximum). A script page must breathe; it cannot resemble a solid wall of prose.
  - Capitalize character names upon their **first introduction only**, followed by age in parentheses: `ELENA (34)`.
  - Capitalize vital props and sound effects only when load-bearing for the narrative.
- **Never Direct the Camera:**
  - Prohibit `CLOSE UP`, `ANGLE ON`, `POV`, `DISSOLVE TO`, or *"WE SEE / WE HEAR"*.
  - Imply camera distance through descriptive scale: a slugline implies a wide establishing view; describing a torn corner of an envelope implies an extreme close-up.
  - Every scene transition is an assumed hard cut; do not write `CUT TO:` between standard scenes.
- **Master Scene Technique:**
  - A dramatic action with temporal and spatial unity constitutes one continuous master scene even if characters move between interconnected rooms.
- **Dialogue Layout:**
  - Character name centered/indented at 3.7" from the left margin, all caps.
  - Dialogue block: Left-aligned at 2.5", width ~3.5" (runs to 6.0").
  - Parentheticals (wrylys): Positioned at 3.1", restricted to short active verbs `(whispering)`, `(tense)`. 95% of parentheticals should be deleted—let the dialogue line carry the emotion.
  - **(V.O.) Voiceover:** Used when the speaker is not physically in the scene space (narration, thoughts, telephone caller).
  - **(O.S.) Off-Screen:** Used when the speaker is physically present in the room/location, but outside the immediate camera frame (e.g., from an adjacent doorway).
  - **(CONT'D):** Appended to a character's name when their speech is interrupted by an action paragraph and resumes.

---

## 3. Typographic Layout Grid (US Letter, Courier 12 pt)

| Element | Left Margin / Indent | Width / Right Limit | Formatting Rules |
|---|---|---|---|
| **Page Margins** | Left 1.5", Right 1.0", Top 1.0", Bottom 1.0" | ~55 lines per page | Left margin is wide for binding |
| **Scene Heading** | 1.5" (Flush Left) | Up to 7.5" (~60 chars) | ALL CAPS; preceded by blank line |
| **Action Paragraph** | 1.5" (Flush Left) | 6.0" wide (~60 chars) | Double-space between paragraphs |
| **Character Name** | 3.7" (~Character 22) | Fixed indent, not centered | ALL CAPS, followed by (V.O.) / (O.S.) |
| **Parenthetical** | 3.1" | ~2.0" width | Lowercase in parens; single line |
| **Dialogue Block** | 2.5" | 3.5" width (to 6.0") | Single-spaced within block |
| **Transition** | Right-aligned to 7.5" | Starts at ~6.0" | `CUT TO:` / `FADE OUT.` (All caps) |
| **Page Number** | Top Right (0.5" from top edge, at 7.2") | Formatted as `2.` | Begins on page 2 |

---

## 4. The Machine-Writable Standard: Fountain (`.fountain`)

The primary plain-text format for automated generation and script versioning is **Fountain**. It compiles cleanly into `.fdx` (Final Draft) or formatted PDFs:
- **Title Page:** Leading key-value pairs (`Title:`, `Credit:`, `Author:`, `Draft date:`).
- **Scene Headings:** Begin with `INT.`, `EXT.`, or a leading period `.` (e.g., `.INT. NORA'S CABIN - NIGHT`).
- **Character Names:** Preceded by a blank line, in ALL CAPS, or forced with `@` (e.g., `@CAPTAIN NORA`).
- **Dual Dialogue:** Append `^` to the second character’s name to place speeches side-by-side.
- **Transitions:** End with `TO:` or forced with a leading `>` (e.g., `> SMASH CUT TO:`).
- **Action:** Standard text blocks. Comments wrapped in `/* ... */`, notes in `[[ ... ]]`.

---

## 5. Muscular Action Paragraph Craft (McKee & Walter)

- **Absolute Present Tense + Kinetic Motion:**
  - Replace passive forms and weak linking verbs (`is`, `are`, `begins to`, `starts to`) with visceral action verbs.
  - *Weak:* `Frank is walking slowly and thoughtfully across the room toward the window.`
  - *Muscular:* `Frank saunters to the window. Stares out into the rain.`
- **Richard Walter’s Diagnostic Symbols:**
  - **Hwk? (How do we know?):** If an actor cannot physically express it or a lens cannot photograph it, delete it.
  - **SIFYN (See It For Yourself, Novelist):** Leave psychological interior monologues and literary floral descriptions for novels.
  - **Drekt/Akt (Direct Action):** Show characters doing, not hesitating to do.
  - **Notnot (Eliminate Negatives):** Do not describe what *doesn't* happen (*"He doesn't answer"*, *"The room isn't crowded"*). Describe what is actively there (*"Silence"*, *"An empty hall"*).
  - **Novry (Kill Adverbs):** Replace *"He runs very quickly"* with *"He sprints"*, *"He bolts"*, *"He charges"*.
  - **Conk (Concrete Specificity):** Use precise brand names, objects, and terms over generic labels.
  - **4 v. 6 (Word Economy):** If four words can convey the scene with equal punch, cut the six words.

---

## 6. The Step-by-Step Writing Pipeline

### Phase 1: Pre-Writing & Concept Validation
- **Eric Bork’s 60/30/10 Rule:** 60% of a script's ultimate commercial and artistic success rests on the core concept/idea; 30% rests on structural execution; only 10% rests on final dialogue polish. Validate the premise before drafting pages.
- **The 3 Cs (Diamond & Weissman):** Lock Character, Concept, and Conflict into a one-page, nine-step treatment.
- **The Step Outline (Robert McKee):**
  - Build an index-card step outline detailing every single scene in 1–2 sentences: *Who enters, what is their objective, what obstacle blocks them, how does the value turn from positive to negative, and what is the scene's structural function?*
  - Pitch the step outline orally in 10 minutes to verify narrative velocity and emotional grip.

### Phase 2: Treatment & First Draft
- **The Present-Tense Treatment:** Draft a 20–40 page prose treatment describing sensory action and psychological subtext without writing dialogue.
- **Drafting Pages with Velocity:**
  - Commit to writing forward without premature rewriting: draft 3–5 pages a day.
  - Do not edit earlier scenes until the full first draft is finished; early editing stifles momentum and creates top-heavy scripts.
  - Syd Field: A sprawling 140-page first draft is far easier to sculpt and compress than an underwritten 75-page draft.

### Phase 3: The Revision Passes
- **Macro-to-Micro Sequence:**
  1. *Structural Pass:* Audit act breaks, midpoint reversal, and eliminate redundant middle-act sequences.
  2. *Character & Motivation Pass:* Ensure every supporting character has a distinct motivation and does not merely serve as the protagonist's cheerleader.
  3. *Scene Tightening (Chop the Tops and Tails):* Cut the first three lines and last three lines of every scene to enter at the moment of highest conflict and exit on a cliffhanger.
  4. *Dialogue Polish:* Read dialogue aloud; run the Cover-the-Names test; eliminate parentheticals and on-the-nose declarations.

---

## 7. The Craft of Adaptation

- **Syd Field’s Principle: Apples and Oranges:**
  - An adaptation is an **original screenplay inspired by source material**, not a slavish transcription.
  - Novels excel at interior psychology; theatre excels at spoken language; cinema excels at **externalized behavior in visual space**.
  - Respect the overarching thematic soul of the source work, but ruthlessly alter chronology, condense secondary characters, and invent visual set pieces to replace prose narration.
- **Robert McKee’s Adaptation Laws:**
  - The more purely literary or internal the original novel, the harder it is to adapt directly into cinema. Focus on stories that possess clear interpersonal and extra-personal conflict.
  - *Be prepared to reinvent from the inside out:* create visual metaphors and behavioral actions that dramatize internal monologues.
- **Julian Hoxter’s Four Adaptation Questions:**
  1. Do you hold legal, ironclad underlying rights or life-story options?
  2. Can the internal conflict be dramatized through visible behavior?
  3. What narrative liberties must be taken to serve a 110-minute visual canvas?
  4. What core thematic symbol can be externalized on screen?
- **Adapting Real-Life Events (Eric Bork):**
  - Real history does not occur in three neat acts. Screenwriters must compress real-world timelines, combine multiple historical figures into composite characters, and heighten dramatic stakes.
  - *The obligation of drama is to convey essential human and emotional truth, not pedantic documentary chronology.*

---

## 8. Screenplay Format Diagnostic Checklist

### Universal Checks (All Scripts)
1. **Action Writing:** Are action lines in strict present tense, active voice, free of camera directions, and under 4 lines per block?
2. **Visual Focus:** Is every sentence describe something a lens can capture or a microphone can hear?
3. **Master Scenes:** Are scenes framed as master setups rather than fragmented micro-angles?
4. **Dialogue Margins:** Is dialogue formatted in a compact, readable column with minimal parentheticals?
5. **Character Introductions:** Are characters capitalized on first appearance with an age descriptor, but written in standard casing thereafter?
6. **Scene Entrances & Exits:** Have conversational hellos, goodbyes, and idle transitions been pruned?
7. **Pacing:** Does the page count correspond realistically to target screen runtime?

### Hollywood Spec Checks (Fountain / Spec)
8. **Font:** Standard Courier 12 pt exclusively?
9. **Page Count:** Between 90 and 120 pages?
10. **Title Page:** Stripped of drafts, dates, and registration numbers?
11. **Technical Shorthand:** Are `(V.O.)` and `(O.S.)` used correctly and sparingly?
12. **Transitions:** Free of unnecessary `CUT TO:` markers between ordinary master scenes?

---

## 9. End-to-End Workflow: From Concept to Submission Draft

1. **Premise & Concept Audit:** Lock the high-concept logline; test against the 60/30/10 rule.
2. **Character & World Profiles:** Establish 3D baselines, core wounds, and visual signatures.
3. **The Step Outline:** Map 40–60 scenes on index cards, tracking value turns (`+` to `-`) and structural act milestones.
4. **The Prose Treatment:** Draft the present-tense narrative spine without formal dialogue to test plot mechanics.
5. **First Draft Execution:** Write forward in Fountain format; track daily page counts without looping back to polish.
6. **Subtractive Compression Pass:** Trim 10–15% of page fat by tightening prose, eliminating throat-clearing scene starts, and cutting repetitive beats.
7. **Targeted Polish Passes:** Run dedicated audits for character voice distinctiveness, visual subtext, and strict format compliance.
8. **Final Packaging:** Compile cleanly into standard industry PDF with minimalist title page.
