---
name: sw-chinese-opera-qupai
description: Chinese opera playwriting for the Qupai (曲牌体) system — Yuan Zaju, Ming/Qing Chuanqi, Kunqu, and Sichuan Opera Gaoqiang, where sung text is filled into fixed tune patterns (Tianci, 填词) rather than constructed from rhymed couplets varied by metric tempo. Covers stage vs. study dramaturgy (Li Yu vs. Wu Mei & Wang Jilie), the Qingqu (lyrical concert) vs. Juqu (theatrical script) toggle, the Zaju branch (four acts and one wedge, one Gongdiao mode and one rhyme per act, single-singer vocal monopoly, Titling & Naming / Timu Zhengming), the Chuanqi branch (Chu scenes, Fumo prologue, Southern-Northern joint suites / Nanbei Hetao, Jitang exit quatrains), tune-filling mechanics (metrics, Qianqiang, Huantou, Yaopian, Chenzi padding syllables, Wutou focal lines, Weisheng codas, the Forty Prohibitions / Sishi Jin), the seventeen Gongdiao modes and their emotional affects, Taoshu suite arrangement, Paichang scene-alternation laws, spoken-to-sung interfacing, Bangqiang offstage choruses, classical adaptation, and contemporary modern practices. Synthesized from Li Yu's Xianqing Ouji, Wu Mei's Guqu Zhutan and Quxue Tonglun, Wang Jilie's Yinlu Qutan, Kong Shangren's Fanli principles, Guan Hanqing, Tang Xianzu, and Wei Minglun. Use when drafting or revising a Qupai script, selecting a Gongdiao mode for specific emotional colors, arranging a Taoshu suite, filling lyrics into a fixed tune matrix, writing a Zaju act or Chuanqi scene, adapting classical epics into stageworthy versions, writing modern Qupai operas, or diagnosing whether a classical masterwork's prosody may be emulated. Not for Peking, Yu, or Yue opera (which belong to the Banqiang system; see sw-chinese-opera-banqiang).
---

# Chinese Opera Playwriting: The Qupai System (曲牌体)

> **Output Language = Prompt Language**; Technical terms are strictly anchored to their original romanized forms without invented translations (see [sw-workflow/terms.md](../sw-workflow/terms.md)). Traditional theatrical terms (*Qupai*, *Gongdiao*, *Taoshu*, *Wutou*, *Chenzi*, *Qianqiang*, *Huantou*, *Yaopian*, *Zengban*, *Bangqiang*, *Binbai*, *Kejie*, *Zhe*, *Chu*, *Xiezi*) have no direct Western equivalents; in any language, retain the original romanized term plus a single explanatory sentence.

This skill governs the **Qupai system (fixed tune matrix)** of traditional Chinese theatre; its dual counterpart is [sw-chinese-opera-banqiang](../sw-chinese-opera-banqiang/SKILL.md). **The dividing line is governed by musical system (*Shengqiang*), not regional dialect**: in Qupai opera, lyrical text is **filled (*Tian*)** into rigid metric molds of fixed syllable counts, caesuras, and tonal registers, structured in acts (*Zhe*) or scenes (*Chu*), with each act governed by a single *Gongdiao* mode; in Banqiang opera, lyrics consist of 7- or 10-character **paired couplets** that vary tempo and emotional weight via metric transformations (*Banshi*), structured in scenes (*Chang*). See sw-chinese-opera-banqiang §0.1 for the foundational taxonomy.

**Division of Core Theoretical Sources**:  
- **Li Yu's *Casual Expressions of Idle Feelings (Xianqing Ouji)*** provides **stage production laws** (drawing from his self-funded touring troupe, analyzing how a text behaves when staged);  
- **Wu Mei's *Notes on Listening to Operas (Guqu Zhutan)* and *General Treatise on Prosody (Quxue Tonglun)*** provide **prosodic and metric regulations** (balancing internal tensions between his works), while his *Introduction to Chinese Opera* establishes critical evaluation benchmarks;  
- **Wang Jilie's *Discussions on Opera from the Wormhole Studio (Yinlu Qutan)*** provides **theatrical sequence architecture (*Paichang*)**;  
- **Kong Shangren's *Principles (Fanli)* and *Theatrical Outlines (Gangling)*** serve alongside Li Yu as primary playwright documents;  
- **Guan Hanqing's three surviving Zaju masterworks** (*The Injustice to Dou E, Rescuing a Courtesan, The Gold Thread Pond*) provide empirical data across 12 acts;  
- **Tang Xianzu, Wei Minglun, Weng Ouhong, and Luo Huaizhen** provide exceptions and practical blueprints for classical adaptation and modern staging.

Reference tables, scene-by-scene empirical data, comprehensive Qupai indexes, and full citations are located in [reference.md](reference.md). **Excluded from this skill**: All Banqiang mechanics → see `sw-chinese-opera-banqiang`; Prohibitions 17–34 of the Forty Prohibitions (cliché, archaic pedantry, vulgar slang, syntactic friction) → see `sw-dialogue`; the Four Questions of Adaptation → see `sw-format-adaptation`; Properties and Stage Entrances/Exits → see `sw-scene-craft`.

## Targeted Reading Index (Do Not Read Cover-to-Cover)

| Objective | Target Sections | Skip |
|---|---|---|
| Filling lyrics into a single Qupai tune matrix | §4, §5.1–§5.2 | §2, §3, §6, §8, §9, §10 |
| Selecting a Gongdiao mode & assembling a Taoshu suite | §5, §6; run §1.4 switch first | §4.4 onwards, §8, §9, §10 |
| Writing a Yuan Zaju act | §2, §5, §4 (**consult Northern column for Chenzi**) | §3, §8 |
| Writing a Ming/Qing Chuanqi scene | §3, §5, §6, §7 | §2 |
| Adapting classical texts into stageworthy versions | §9, §11, §3.1 | §2, §8, §10 |
| Writing contemporary modern Qupai operas | **Read §10 first**, then §4.1, §5.2, §11 | Rigid suite formulas in §5.3–§5.4 (relaxed in §10) |
| Determining whether a classical masterpiece may be emulated | §11, §1.3 | All other sections |
| Diagnosing an existing draft | **§13**, then cross-reference failed items | All other sections |

---

## 1. Foundational Posture: Two Schools, Two Scoring Scales, Two Pre-Conditions

**Mandatory Reading**: Qupai rules were formulated by two distinct groups occupying opposing vantage points. Without establishing this critical context, subsequent rules will appear directly contradictory.

**1.1 Stage Playwrights vs. Study Prosodists (Co-existing perspectives; no arbitrary adjudication).**  
Li Yu represents the stage playwright: *"What Jin Shengtan critiqued was the Western Wing appreciated by scholars in their studies, not the Western Wing performed by actors upon the stage."* Wu Mei and Wang Jilie represent the study prosodists, placing phonological and tonal precision before dramatic construction—the polar opposite of Li Yu's hierarchy of "Structure First, Musical Meter Third." **Wu Mei's split judgment on Li Yu must be read simultaneously**:  
- *Praise*: Li Yu's stage business (*Paichang*) and comedic dialogue (*Kebai*) "stand peerless across a thousand ages";  
- *Censure*: "Though his dramatic layouts are ingenious, his poetic diction is clumsy... unworthy of critical acclaim among literati poets."  
→ **When quoting Li Yu, explicitly note that he provides theatrical production rules, not prosodic literary standards.** Wang Jilie occupies a third position: his dramatic stance is oriented toward the stage, but his operational methodology relies entirely on strict prosodic rules. For the distinction between the Three Craft Disciplines (*Zhiqu* = writing lyrics, the playwright's domain; *Puqu* = musical composition; *Duqu* = vocal performance) and "Vocal Prosody Books (*Qupu*) vs. Notated Instrumental Scores (*Gongpu*)," see [reference-tizhi.md](reference-tizhi.md) §16. **When asked "which Kunqu score to consult," first determine whether the user seeks poetic metrics or vocal notation; confusing the two provides the wrong source.**

**1.2 The Tang-Shen Debate (Three-way debate; no arbitrary adjudication).**  
Shen Jing asserted: *"Better that the prosodic meter be harmonious even if the diction is unpolished."*  
Tang Xianzu countered: *"I care not if my poetry wrenches and snaps the throats of singers across the world."*  
Wu Mei refused to take sides ("Both must unite in harmony"), offering a pragmatic standard of artistic acquisition: *"Shen Jing's strict rules can be mastered through diligent study; Tang Xianzu's poetic genius cannot be achieved through mere effort."* Weng Ouhong provided the middle ground: "So long as the lyrics are clear and the dramatic intent flows smoothly" (see `sw-chinese-opera-banqiang`). **This skill focuses strictly on the learnable, operational side of the craft.**

**1.3 Drama (*Xi*) and Prosody (*Qu*) Are Two Independent Scoring Scales.**  
*The Peach Blossom Fan (Taohua Shan)* and *The Palace of Eternal Youth (Changsheng Dian)* achieve **inverted rankings** when evaluated via literary-metric scales versus theatrical-staging scales. The historical trajectory is marked by the adage: *"Under the Qianlong reign, drama and prosody co-existed; during the Jiaqing and Daoguang eras, prosody survived while drama vanished; after the Xianfeng and Tongzhi periods, both drama and prosody were lost."*  
**Self-Check: Read a script twice in two separate passes**—Pass 1 evaluates dramatic architecture, scene contrast (*Paichang*), and role distribution; Pass 2 audits poetic diction, *Gongdiao* modes, rhyme categories, and four-tone pitch contours. Both passes must carry independent quality scores.

**1.4 Pre-Condition Switch 1: Concert Suites (*Qingqu*) vs. Theatrical Scripts (*Juqu*).**  
Rules governing repeated rhymes (*Chongyun*), padding syllables (*Chenzi*), and borrowed modes (*Jiegong*) become errors if evaluated out of context. **First determine: "Is this intended for the live stage or the scholar's study?"**

| Dimension | **Theatrical Script (Juqu)**<br>*(Live staging with dialogue & action)*<br>**Use for performable stage plays** | **Concert Suite (Qingqu)**<br>*(Aria suites without dialogue or action)*<br>**Use for concert singing & vocal showcases** |
|---|---|---|
| **Borrowed Modes (*Jiegong*)** | Permitted (Nanlü borrowing from Shangdiao, Zhonglü borrowing from Banshe) | Prohibited |
| **Repeated Rhymes (*Chongyun*)** | Permitted; celebrated masters do not avoid them | Strictly prohibited |
| **Padding Syllables (*Chenzi*)** | Abundant padding allowed (Tang Xianzu's Four Dreams: "the more daring, the more wondrous") | Used sparingly |
| **Subject & Metrics** | Centered on romantic leads (Sheng/Dan); metrics more forgiving | "Need not be confined to romance"; metrics far more rigid |

*Failure condition*: Modern contemporary operas relax both columns; see §10.

**1.5 Pre-Condition Switch 2: Debunking a False Premise.**  
The claim that "Ming and Qing Chuanqi strictly adhered to Gongdiao modes" is **historically incorrect**—Wu Mei explicitly identified *The Tale of the Lute (Pipa Ji)* and *The Moon-Worship Pavilion (Baiyue Ting)* as the **historical origin** of the trend "abandoning modal discipline and disregarding pitch suites." Two operational corollaries:  
1. **Surviving digital editions of *The Peony Pavilion* and *The Peach Blossom Fan* systematically omit Gongdiao markings** (verified through act-by-act collation). → **Any catalog entry marked `[Inferred]` serves only as an illustrative example, never as binding authority.** When citing Gongdiao modes and rhyme usage, **draw primary examples exclusively from Yuan Zaju**; in Chuanqi, rely only on the three definitive Northern suites (*Underworld Judgment*, *Severe Interrogation*, *Imperial Audience*) and authenticated annotations.  
2. **"An ancient predecessor marked it this way" is not definitive proof**: distinguish whether a historical instance is a foundational rule (*Ge*) or an anomalous exception (*Li*); if it is an exception, verify secondary and tertiary occurrences (*The Moon-Worship Pavilion* erroneously labeled the Yuediao tune [Kanhua Hui] as Xianlü [Dian Jiangchun], an error repeated cyclically in *Handan Ji* and *Changsheng Dian*).

---

## 2. The Zaju Branch (Yuan Zaju)

Empirical evidence is drawn from Guan Hanqing's three surviving Zaju masterworks (*The Injustice to Dou E*, *Rescuing a Courtesan*, *The Gold Thread Pond*, based on the *Yuanqu Xuan* texts in Wikisource); for the 12-act metrics, see [reference-tizhi.md](reference-tizhi.md) §9.

- **Four Acts and One Wedge (*Si Zhe Yi Xiezi*); the wedge is optional.** (*Rescuing a Courtesan* contains no wedge; a six-month temporal leap is handled entirely through an entrance monologue). *Failure condition*: If the temporal leap contains dramatic events that must be physically enacted on stage, a wedge is mandatory. **A wedge is restricted to Xianlü [Shanghua Shi] or [Duanzheng Hao], containing at most two tunes**; if the narrative cannot fit, expand it into a full act.
- **One act adheres strictly to one Gongdiao mode; four acts must use four distinct modes. Act 1 is permanently Xianlü; Act 4 is permanently Shuangdiao.** (This holds 100% across all three plays, providing a far more operational rule than "four acts, four modes"). Acts 2 and 3 select their modes based on dramatic emotion from Nanlü, Zhenggong, Shangdiao, or Zhonglü. *Self-check*: Does Act 1 open with the four-tune sequence [Dian Jiangchun] → [Hun Jianglong] → [You Hulu] → [Tianxia Le]? Does Act 4 open with [Xinshui Ling]? If not, audit which prosodic lineage is being cited.
- **One act sustains one rhyme from beginning to end; four acts use four distinct rhymes without repetition.** **Gongdiao modes and rhyme categories are locked and transposed together.** (*Self-check*: List the terminal rhyming characters of every tune in an act; any word belonging to a different rhyme group is an error). **The wedge carries its own independent rhyme**, excluded from the four-act non-repetition count. **Repeated rhymes within a suite are permitted**—valid only for theatrical scripts (*Juqu*, §1.4).
- **Single-Singer Vocal Monopoly (*Yiren Zhuchang*)**: Across all 12 acts of the three Guan Hanqing plays, all 123 arias belong exclusively to the female lead (*Zhengdan*); **the wedge singer is flexible** (an elderly male *Chongmo* sings in *Dou E*; the *Zhengdan* sings in *Gold Thread Pond*). *Self-check*: Columnize role labels across the four acts; if a second character sings, the structural purity of Yuan Zaju is broken. **To stage ensemble scenes**: convert the opposing character's speech into dialogue interruptions, and ensure the primary singer **catches the key words of that spoken line** to resume singing; failing to do this turns supporting characters into mute statues.
- **Singing Monopoly Equals Protagonist Status**: In *Rescuing a Courtesan*, all 44 arias are assigned to Zhao Pan'er (the rescuer); the victimized Song Yinzhang sings zero arias, and the play's title reflects this hierarchy—**dramatic architecture, vocal monopoly, and titular identity constitute a single unified decision** (unmatched in Banqiang opera; see §12).
- **Aria Suite Formulas (*Taoshi*)**: Opening and closing tunes are fixed, while middle tunes may be added, omitted, or rearranged (all 12 acts adhere strictly to this formula; [Gewei] bridging tunes and cross-mode borrowings of [Huangzhong Wei] are standard Zaju conventions). **A complete suite must contain 12 to 13 tunes or fewer**: fewer than that is deemed "hasty and thin" (*Shanzhuan*); more than that is deemed "rambling and redundant" (*Xudao*). **The final act's coda (*Weisheng*) may be omitted**, provided the dramatic resolution is handed over to the judicial verdict and spoken verse (*Ciyun*); omitting the coda within Acts 1–3 is a fatal defect.
- **Titling and Naming (*Timu Zhengming*)**: Placed at the very end of the script, spoken rather than sung, comprising two or four lines (one line per narrative strand). **The definitive naming line (*Zhengming*) must embed the full title of the play, and the dramatic action contained within that line must be physically enacted on stage.** If you cannot craft that final line, the title is poorly conceived.
- **`[Huan'ke]` (Stage Substitution Cue)**: The dedicated theatrical notation for "public sleight-of-hand / staged substitution" (swapping divorce papers, switching the person being supported): delivered without verbal explanation; the victim remains ignorant while the audience watches the deception. *Self-check*: The substitution must be immediately followed by an erroneous question from the deceived character to exploit the dramatic irony (cross-reference `sw-scene-craft` on props).
- **Plot-Trap Plays (*Sheju Xi*)**: (Five of Guan Hanqing's eight surviving plays center on women orchestrating elaborate ruses to outwit despots or playboys): **The strategic deception must be explained to the audience in an extensive spoken monologue prior to execution**, and **the trap must be partially unmasked mid-way before pivoting to success.** **This directly contradicts Western suspense conventions**—Chinese opera holds no structural secrets from the audience; concealing the plan Western-style empties Act 3 of theatrical pleasure.

---

## 3. The Chuanqi Branch (Ming/Qing Chuanqi & Kunqu)

- **Scale**: **Ming Chuanqi defaults to an architecture of approximately 40 scenes (*Chu*)**—Wu Mei regarded this length as inherently flawed, noting that 60-scene epics inevitably "diminish the primary conflict while secondary trivialities usurp the stage"; **subplot digressions must be compressed into spoken exposition** (*Self-check*: Beyond the main plot, how many peripheral events does a scene touch? If more than one, collapse them into spoken dialogue). Qing playwrights responded with collections of concise one-act vignettes (*Zhezixi*).
- **Volume Structuring**: *The Peach Blossom Fan* splits into Upper and Lower Volumes, each performed over a full night, linked by an unnumbered interlude (Scene 21) where the narrator (*Fumo*) returns to bridge the volumes (*Self-check*: If the Upper Volume is entirely self-sufficient, the Lower Volume becomes an unwanted sequel). **The structural spine of each scene "cannot be rearranged, nor can it be deleted"** (*Fanli* 4); **major scenes contain eight arias; short scenes contain six or four** (*Fanli* 5, engineered to prevent actors from cutting text) — **the aesthetic trade-off**: Wu Mei noted this strict quota prevented poetic expansiveness and warned that "romantic leads must not be rushed through carelessly."
- **Fumo Prologue (*Fumo Kaichang*)**: Scene 1 features the veteran narrator (*Fumo*) introducing the theme and narrative summary without enacting plot events; Li Yu separated this into two tiers—**first an entrance lyric to subtly suggest the theme, followed by the household exposition (*Jiamen*) to explicitly state the plot summary**. Drafting the *Jiamen* is notoriously difficult; Li Yu advised: *"Leave the opening chapter blank and compose it upon completing the finale."* **Kong Shangren expanded the Fumo into an active through-line**: all four unnumbered scenes in *The Peach Blossom Fan* feature the Master of Ceremonies (Lao Zanli), **who acts simultaneously as an active character within the dramatic world**. *Self-check*: If the narrator speaks only from the framing prologue, they carry zero emotional weight; assign them at least one concrete dramatic action within the main plot spine.
- **Sheng-Dan Alternation & Shared Refrains (*Hetou*)**: **The primary male lead (*Sheng*) and female lead (*Dan*) form the structural engine of the opera, and must be introduced by Scenes 2 and 3**; *historical exceptions*: *Handan Meng* and *Juntian Yue* center on the elderly male (*Laosheng*). **The lyrical meaning of a choral refrain (*Hetou*) must be logically claimable by every character onstage**—when staging scenes where characters harbor conflicting internal secrets, **explicitly divide the singing lines (*Fenchang*)**, or rehearsal directors will collapse them into unison singing.
- **Southern-Northern Joint Suites (*Nanbei Hetao*)**: Invented by the Yuan-dynasty dramatist Shen He, designed for "scenes of grand dramatic scale" (see [reference-taoshu.md](reference-taoshu.md) §4). ***The Peony Pavilion (Imperial Audience)* stands as the supreme masterclass**: **all ten Northern tunes belong exclusively to Du Liniang, while the Southern tunes are distributed among the surrounding ensemble, each concluding with a shared choral refrain (*Hetou*)**—**a joint suite is not empty virtuosity, but the musical dramatization of "the individual defying the collective."** *Failure condition*: If the finale portrays characters sharing equal moral accountability, a joint suite hollows out the protagonist; substitute with sequential solo rotations under the same tune.
- **Functional Allocation of Northern vs. Southern Tunes (Two co-existing principles)**:  
  1. *Northern tunes for external intruders*: (In *The Peach Blossom Fan*, Liu Jingting invades the military garrison in Scene 11; in *The Peony Pavilion*, barbarian kings, bandits, underworld judges, tribunals, and imperial courts sing Northern suites as solo monologues) — **Deploy when an outsider disrupts an established status quo.**  
  2. *Northern tunes for commanders in crisis*: (In *The Peach Blossom Fan*, Scene 18 inverts this; Wang Jilie's canon: "When Sheng, Jing, or Laosheng encounter tragic catastrophes, Northern tunes are appropriate") — **Deploy when a resident protagonist must overpower the stage with masculine fury and tragic weight.**  
  *Shared Criterion*: Do you require structural density and rapid rhythmic punch, or lingering lyricism; do you require the ensemble to join in song? *Proportions*: Chuanqi should consist of 80–90% Southern tunes. *Failure condition*: Zaju is the exact inverse, using 100% Northern tunes.
- **Cross-Scene Modal Resonance (Unique to Qupai; impossible in Banqiang)**: Du Liniang dies under the Southern Shangdiao "Oriole" (*Ying*) suite; Liu Mengmei's Scene 24 (*Contemplating the Portrait*) mirrors her grief using the identical Gongdiao mode and tune family. *Self-check*: Before drafting a new suite, audit whether this Gongdiao mode has appeared previously, and to which character it was attached. ⚠️ Support this only via the three authenticated Northern suites and explicit historical scores (the "Oriole" suite carries the `[Inferred]` tag, §1.5).
- **Collected Tang Exit Quatrains (*Jitang Xiachangshi*)**: In *The Peony Pavilion*, all 55 scenes conclude with four lines assembled from Tang poets, noting the original poet beneath each line; **they may be recited by a single character, split among the cast, or delivered in unison**, **resolving the current scene while hinting at the next** (*Self-check*: Read the four lines in isolation; can you predict the ensuing action?); the finale may break convention with eight lines. **Kong Shangren objected**: *"Collecting Tang verse has become a worn cliché. I compose fresh poetry for every scene, providing an authentic genesis and clear resolution"* (*Fanli* 15)—**both models stand valid; adhere to your chosen stylistic contract.**
- **Four Colors and Four Humors (*Sise Siqi*)**: The character matrix in *The Peach Blossom Fan* **categorizes figures not by moral virtue, but by dramatic function**: The Four Colors (*Zheng* primary / *Jian* foil / *He* mediator / *Run* embellisher) govern the romantic separation/reunion axis; The Four Humors (*Zhong* balanced / *Li* rebellious / *Yu* residual / *Sha* ruinous) govern the dynastic rise/fall axis; two framing commentators occupy a separate overarching category ([reference-tizhi.md](reference-tizhi.md) §11), **complementing rather than replacing the 3D character archetypes in `sw-character-conflict`**. **Role casting serves as critical judgment, but avoids simplistic moral labels**: "When primary colors are exhausted, borrow from Chou and Jing" (*Fanli* 14); *Self-check*: Align "Role Type — Character — Moral Stance" in a matrix; if all three columns match perfectly, the dramaturgical design is lazy.

---

## 4. The Craft of Filling Lyrics (Tianci Fa)

**4.1 What "Filling" Means.**  
**The vocal score is an unalterable stencil (*Fenben*)**: *"The clumsy may not subtract a syllable, nor may the clever add one"; "The older the tune pattern, the better; slight attempts at novelty produce catastrophic errors from the smallest deviation"* (Li Yu). **Address Li Yu's internal paradox**: while declaring ancient tune patterns sacred, his chapters on originality state that "stagnation breeds rot." The operational boundary: **prosodic metrics (tune molds, rhymes, metric frameworks) are inviolable, whereas dramatic plots, comedic business (*Kehun*), and dialogue nuance must be radically original** (analytical synthesis, not Li Yu's explicit text). **Selecting a Qupai tune simultaneously locks tempo, duration, and staging conventions** (Luo Huaizhen) → Sequence of composition: **First define architectural layout → establish controlling premise → arrange tune sequence → finally polish individual lines** (Wu Mei: "Avoid patching together filler lines; avoid settling for compromises"). *Self-check*: Before drafting the first sung line, can you list the scene's tune sequence and the exact dramatic function of each aria? If not, you are not ready to write lyrics.

**4.2 Three Levels of Repetition: Qianqiang, Huantou, and Yaopian.**  
- **Qianqiang (Following Melody)** = Stacking multiple iterations of the same tune, **maintaining identical line metrics without changing a single syllable's structural position**;  
- **Huantou (Altered Head)** = Retaining the body while modifying the opening lines, adding or subtracting one or two syllables;  
- **Yaopian (or Yao)** = The Northern tune equivalent of structural repetition.  
**Failing to differentiate these causes writers to mistake "Huantou" for a direct duplicate** (contemporary scripts often write "Continues Singing" without marking Qianqiang, leaving meter to be deduced from rhyme and line counts). See [reference.md](reference.md) §3 for variations across homonymous tunes and cross-mode variants.

**4.3 Padding Syllables (*Chenzi*).**  
**Three Iron Rules for Southern Tunes**:  
1. **Add padding only where the rhythmic beat is dense, and only at the beginning or middle of a poetic line; never add padding within the final three syllables or where the musical beat is sparse**;  
2. **Maximum three padding syllables per location**;  
3. **Prioritize empty grammatical particles (*Xuzi*) over substantive nouns/verbs (*Shizi*)**.  
**Northern tunes place zero restrictions on padding syllables** (beats are flexible, and padding syllables may carry explicit percussion beats) — **when drafting Northern suites, these three rules are fully suspended**.  
**Arias utilizing syncopated rests (*Chouban*) and the first line of a coda (*Weisheng*) permit zero padding syllables**; extra syllables beyond an 8- or 10-character line default to padding and must not carry heavy metric beats (Tang Xianzu's unrestrained padding left singers unable to parse phrasing, prompting revisions that "reduced the poetry's brilliance tenfold"). **Audit musical meter before writing Southern lyrics**: if a wide beat interval separates the resolving beat of the upper line from the opening beat of the lower line, the opening of the lower line permits zero padding.

**4.4 Wutou: The Focal Crux of the Aria (Four co-existing definitions of "Locating the Core Line").**

| Authority | Nature of Wutou | Operational Search Method |
|---|---|---|
| **Li Yu**<br>*(Theatrical/Staging)* | "Like the eye in a game of Go: possess it and the board lives; lack it and the board dies." | Identify the specific line and key words of the climax; **if you cannot point to it, the aria is dramatically dead.** |
| **Wu Mei**<br>*(Prosodic/Acoustic)* | "The exact juncture where Level (*Ping*), Rising (*Shang*), and Departing (*Qu*) tones cascade together"; syllables 3, 4, 5 of a 7-character line must not share identical tones. | Annotate the final line with four-tone yin/yang marks; locate the three-tone or two-tone cascading sequence. |
| **Wang Jilie**<br>*(Phonological Application)* | Follows Wu Mei, adding: "Most frequently located at the terminal line or the structural crux of the tune." | Check *Beici Guangzheng Pu* for notes stating "Rising/Departing tones cannot be transposed," or Southern scores noting "Departing-Rising sequence is exquisite." |
| **Lu Jun**<br>*(Banqiang counterpart)* | The anchor line expressing theme, internal motivation, or relationship reversal. | Draft the core dramatic line first, then use it to lock the rhyme category for the scene. |

Cross-reference `sw-chinese-opera-banqiang` §2. Two operational corollaries: **At the Wutou, prioritize literary coherence over strict tonal perfection if forced to choose** (the sole instance where prosody yields to meaning; **do not generalize beyond this focal point**); **the exact position of the Wutou must be designated by the playwright prior to composition.** ⚠️ Citing Wang Jilie's correction: Kong Shangren's claim that "the word *Si* is the Wutou" conflates two unrelated phenomena—*Si* belongs to the Zhi-Shi rhyme where sound issues from between the teeth, bearing no connection to Wutou acoustics.

**4.5 The Forty Prohibitions (*Sishi Jin*) and the Four Tones.**  
Derived from Wang Jide's *Qulü* with annotations by Wu Mei ([reference-jinji.md](reference-jinji.md) §12); apply prosodic rules **1–16 and 35–40** (rules 17–34 govern dialogue diction → see `sw-dialogue`). **Wu Mei's overarching caveat must be cited**: *"If one cannot observe every rule, purge the most egregious offenses"; "The rules are exceedingly severe"* → **The Forty Prohibitions serve as a diagnostic health checklist, not an entry threshold.** If time is limited, audit these six fatal errors: repeated rhymes, cross-rhyme pollution, unsingable phrasing, excessive padding, pedantic scholarly jargon, and erratic modal switching.  
**Four Tonal Rules** ([reference-taoshu.md](reference-taoshu.md) §6):  
1. **Never string four identical tones consecutively** (four Level, four Rising, four Departing, or four Entering tones);  
2. **Departing-Rising (*Qu-Shang*) sequences are superior to Rising-Departing (*Shang-Qu*)** → assign low musical pitches to Rising tones and high pitches to Departing tones;  
3. **The Entering Tone (*Rusheng*) is the "Licorice of Prosody"**—Southern Entering tones possess distinct glottal stops that can substitute for Level, Rising, or Departing tones; **Northern tunes lack Entering tones (which merged into the other three tones) and permit zero substitutions**; furthermore, **if a Southern aria adopts an Entering-tone rhyme, the entire suite must maintain Entering-tone rhymes** (sole exceptions: *Jia-Ma* and *Che-She*);  
4. *Self-Check*: Sing the line aloud to ensure tonal pitch does not morph the word into an unintended homophone (e.g., "Guang" sounding like "Kuang"); if it does, swap the word without altering the melody. Rhymes within the six acoustic termination classes may blend; cross-class rhyming is strictly forbidden (e.g., mixing *Zhen-Wen*, *Geng-Qing*, and *Qin-Xun* produced the flawed aria in *The Jade Hairpin [Flirting with the Zither]*, of which it was said: *"Not a single singer could deliver it masterfully"*).

**4.6 Metrics, Caesuras, and Codas (*Weisheng*).**  
**Caesura structures dictate musical beats, not grammatical semantics**: a 7-character line must be established as either **4-over-3** or **3-over-4**; *Self-Check*: Read the line broken at the metric beat—**the severed second half must form an independent, intelligible syntactic phrase** (*The Peach Blossom Fan [Passing Song]* severed "Matching his young lord's noble form" into "Lord's noble form," which Wu Mei condemned as "possessing fine words but ruined melody"). **Assigning proper characters and caesuras is the playwright's responsibility, not the composer's.**  
The **Coda (*Weisheng*)** universally occupies **12 metric beats (*Ban*)**; select from the 11 formal coda titles according to the active Gongdiao mode, maintaining strict structural sequence ([reference-taoshu.md](reference-taoshu.md) §7). For the three conditions permitting coda omissions and trailing cadences (*Suisha*), see [reference-taoshu.md](reference-taoshu.md) §7. **Place the most striking poetic line of the entire suite at the final cadence.** **Rules are rigid, but lyric writing is living craft**: slight tonal variations between a *Qianqiang* / *Yaopian* and its parent tune are permissible, **provided the playwright can cite an ancient masterwork as precedent**. ⚠️ The "Southern Coda Tonal Matrix" in *Guqu Zhutan* contains discrepancies across digital OCR sources and is marked `[To Verify against print editions]`; the 11 formal coda titles remain fully reliable.

**4.7 Verification Circuit: Singing to the Beat (*Anjie Er Ge*).**  
**Upon finishing an aria, sing it aloud against the musical score: *"If the slightest awkwardness arises in pronunciation, rewrite the line immediately"*** (Kong Shangren, *The Making of The Peach Blossom Fan*, working with master performers). Li Yu framed the same law from the negative: Rising-tone words (*Shangsheng*) **drop to the lowest pitch in singing, yet rise to the highest pitch in spoken speech**; when playwrights merely recite lines, *"what sounds elevated in speech drops to an unflattering low register when sung"*—the fatal defect of "scripts written for the desk rather than the stage." → **Every completed aria must be sung aloud by a human voice, never merely recited.** This occupies the identical verification function as the *Shenqiang* (score review) phase in Banqiang opera.

---

## 5. Gongdiao Modes & Taoshu Suites

**5.1 Boundaries of Playwriting Knowledge.**  
Wu Mei defined the limits: *"The Gongdiao mode exists solely to regulate the pitch register of the musical instruments."* He separated musicology from dramatic writing: *"Prosody and tuning theory are two entirely separate disciplines"*; he excluded the mathematical calculations of pipes and intervals, admitting that the historical correspondence between ancient modes and pitch heights was "lost to antiquity." → **Boundary Law: A playwright's modal knowledge ends at instrument register (*Guanse*) and suite assembly (*Liantao*).** When questioned on ancient acoustics or interval derivation, state: "That belongs to musicology, not playwriting craft; Wu Mei declared it irrelevant to libretto construction," redirecting focus to flute registers and suite sequencing.

**5.2 Emotional Affects of the Seventeen Gongdiao Modes.**  
Workflow: **First determine dramatic emotion (separation, joy, grief) → select matching Gongdiao mode → draw arias exclusively from within that mode to assemble the suite.** Never collect pleasing tunes first and force them into an unnatural suite.

| Mode | Emotional Affect | | Mode | Emotional Affect |
|---|---|---|---|---|
| **Xianlü Gong** | Pure, fresh, distant, lingering | | **Banshe Diao** | Plunging into pitfalls, stumbling through perils |
| **Nanlü Gong** | Sighing lamentation, profound sorrow | | **Xiezhi Diao** | Urgent, abrupt, resting in vacancy (Lost in North) |
| **Zhonglü Gong** | Sudden leaps, fluctuating twists | | **Shangjiao Diao** | Sorrowful, meandering, mournful (Lost in South) |
| **Huangzhong Gong**| Opulent, luxurious, tender yearning | | **Shuangdiao** | Vigorous, agile, soaring, resounding |
| **Zhenggong** | Melancholy, desolate, heroic, majestic | | **Shangdiao** | Grievous, resentful, longing, pining |
| **Daogong** | Ethereal, transcendent, serene, tranquil| | **Jiaodiao** | Sobbing, lamenting, resonant (Lost in North) |
| **Dashi Diao** | Suave, elegant, romantic, restrained | | **Yuediao** | Sarcastic mockery, cynical laughter |
| **Xiaoshi Diao** | Delicate, seductive, alluring | | **Gongdiao** | Dignified, solemn, weighty (Lost in North) |
| **Gaoping Diao** | Tortuous, irregular, tangled (Yu in South) | | | |

*(Wu Mei, Quxue Tonglun, Chapter 2. Use these seventeen original descriptions verbatim; do not modernize them into generic emotional adjectives—terms like "stumbling through perils" represent technical acoustic definitions. Yuan dynasty conventions: **Tragedy uses Nanlü and Shangdiao; Comedy uses Huangzhong and Xianlü; Martial heroes sing Zhenggong; Satirical mockery sings Yuediao**).*

**Name Existence ≠ Viable Repertoire**: Northern opera lost three modes; Southern opera lost Shangjiao; Wang Jilie compressed the system into **Nine Common Modes: Xianlü, Nanlü, Huangzhong, Zhonglü, Zhenggong, Dashi, Shangdiao, Yuediao, Shuangdiao**. *Self-check*: If deploying a mode outside these nine, verify whether it possesses sufficient surviving tunes to construct a viable suite. *Failure condition*: Brief scenes, transitional bridges, and pastiche suites (*Jiqu*) may borrow from minor modes. See [reference.md](reference.md) §1 for the complete table of tunes across six Gong and eleven Diao modes and the 21 Rhyme Groups.

**5.3 One Suite, One Mode, and Three Permitted Methods of Modulation.**  
Mixing tunes from different modes within a single suite without rule constitutes **modal corruption (*Chugong / Fandiao*)**, forbidden by prosody ("Though the text be sublime, it cannot be set to instruments").  
- **Borrowed Modes (*Jiegong* in Northern opera)**: Adhere strictly to ancient Yuan precedents; never invent arbitrary modal modulations (*Self-check*: Can you cite the specific Yuan zaju from which this borrowed sequence is drawn? If not, it is flawed).  
- **Pastiche Suites (*Jiqu* in Southern opera) Five Iron Rules**: (1) Borrow only from within the parent mode or another mode **sharing the identical flute pitch register**; (2) **Modes with wildly divergent pitch registers must never be combined**; (3) The opening lines must use the opening lines of the parent tune; (4) The closing lines must use the closing lines of the parent tune, with middle lines drawing from middle segments; (5) **Inverting structural positions is forbidden**; **the pastiche suite belongs to the mode of its opening tune** (*Self-check*: Can you identify every borrowed tune and confirm they share a single flute register? If not, abandon the pastiche).  
- *General Law of Modulation*: **Modulate only between modes sharing the identical flute register** ([reference.md](reference.md) §2). Wu Mei maintained reservations regarding *Jiqu*; Wang Jide's assertion that "Xianlü may blend freely with Shuangdiao" was explicitly rejected by Wu Mei. **Modulating modes and rhymes within a single scene is permitted only when prompted by a major staging shift or dramatic reversal** (e.g., *Changsheng Dian [Pledging Love]*: Dashi mode accompanies the imperial banquet, pivoting to Yuediao for intimate midnight whispers). *Self-check: What physical or emotional event occurred onstage at the exact moment of modal transition? If you cannot answer, do not modulate.*

**5.4 Suite Architecture (*Paitao*).**  
**The Golden Rule of Southern Suites: Slow tunes with added beats (*Zengban*) precede; fast tunes without added beats follow; intermediate tunes sit in between** ([reference-taoshu.md](reference-taoshu.md) §5). Introductory tunes (*Yinzi*) accompany character entrances; Codas (*Weisheng*) provide dramatic resolution; a single scene contains at most three entrance tunes; **clowns (*Chou*) and villains (*Jing*) never use introductory entrance tunes** ([reference-taoshu.md](reference-taoshu.md) §5).  
**The Six Emotional Portals for Suite Selection**: Joy / Sightseeing / Sorrow / Resentment / Action / Romantic Confession, supplemented by Martial, Transitional, and Contemplative categories ([reference-taoshu.md](reference-taoshu.md) §4); **massive romantic confession suites are reserved exclusively for the major dramatic turning points of the play, sung by the romantic leads (Sheng/Dan)**—*Self-check*: **Does the longest confession suite align with the scene of greatest value reversal?** (Mirroring `sw-scene-craft`).  
**Transitional Pastiches (*Zhuan*)**: Deployed as structural joints during scenic transformations; **limit to at most one scene per opera, containing no more than two tunes.**  
**Unnotated Obscure Tunes (*Leng Paizi*)**: Tunes lacking documented metric notation in standard scores cannot be performed. *Self-check*: Check *Nanci Dinglü* or *Jiugong Dacheng* for metric notation before choosing a tune (*Failure condition*: Master composers crafting original melodies are exempt).

---

## 6. Staging Balance (*Paichang*) & Dramatic Action

- **Differentiating Drama from Staging**: *"The emotional trajectory of sorrow, joy, separation, and reunion constitutes the Dramatic Plot (*Juqing*); the physical blocking, pacing, and entrances/exits of the actors constitute Staging Balance (*Paichang*)."* — **Staging balance is an operational budget calculated during lyric writing, not deferred to the director** (occupying the structural tier of Fan Junhong's "Technical Structure," see `sw-chinese-opera-banqiang`).
- **The Law of Staging Alternation (Universal across both systems)**: *"If Act 1 features the male lead (*Sheng*) and Act 2 features the female lead (*Dan*), Act 3 must feature martial spectacles or bustling ensemble scenes; after two or three acts of extended slow suites, interpolate brief transitional vignettes or comedic clown sketches."* *Self-check*: List scenes in order by "Lead Singer / Emotional Atmosphere"; ensure no three consecutive scenes share the same character or mood. *Failure condition*: One-act plays under ten scenes need only avoid back-to-back identical singers. Benchmark: the 50-scene structural breakdown of *The Palace of Eternal Youth* ([reference-tizhi.md](reference-tizhi.md) §8).
- **Transitional Vignettes Are Indispensable**: *"Without them, plot causality fractures and thematic threads sever"*; **they must strictly employ short, rapid tunes**. *Self-check*: Are major dramatic set-pieces separated by transitional scenes? Did you mistakenly place an extended slow aria inside a transition?
- **Balancing Cold and Warm Scenes**: Li Yu rejected dogmatic pacing formulas: *"Theatrical scripts know no absolute warm or cold scenes; they suffer only from departing from human truth"*; **a quiet scene fails not because it is quiet, but because it lacks psychological polish.**
- **Clowns (*Jing/Chou*) as Structural Pillars (Two perspectives; no forced merger)**:  
  - *Wu Mei*: "The sharper the contrast provided by clown roles, the more exquisite the poetic atmosphere"; transitional clown songs must be tightly woven into the dramatic fabric.  
  - *Li Yu*: "Comic business (*Kehun*) is ginseng tonic for the audience," functioning as energy management; two rules: **comedy is not the exclusive property of the clown**, and **every comedic beat must be triggered by an authentic object within the scene** (*Self-check*: Delete any joke that lacks an immediate physical trigger).

---

## 7. Interfacing Spoken Dialogue to Sung Aria (*Binbai → Qu*)

- **The opening line of an aria must be anchored in the preceding line of spoken dialogue** (the most immediately applicable craft rule in classical opera). Two textbook examples from *The Peony Pavilion (Dreaming in the Garden)*:  
  Spoken: *"What splendid weather!"* → instantly igniting [Bubu Jiao];  
  Spoken: *"Without stepping into the garden, how could one know the glory of spring?"* → instantly launching [Zaoluo Pao]: *"See how the purples and reds bloom in splendor."*  
  *Self-check*: Circle the transitional conjunctions in the opening sung line ("Originally," "Yet," "Truly"); trace backward into the preceding spoken dialogue to locate their trigger. If unanchored, the aria erupts out of nowhere. **This rule is universal across both systems**—appearing independently in *Chaoyang Ditch* and Luo Huaizhen's Yue operas, where Banqiang opera frames it as: "Does a direct vocative term precede each aria block?" (see `sw-chinese-opera-banqiang`).
- **Three Absolute Demands on Spoken Dialogue (*Binbai*)**:  
  1. In multi-character scenes, **dialogue handoffs between singers must be sharp and evocative**;  
  2. Kunqu elongates notes across few syllables; **spoken dialogue must relieve vocal exhaustion**;  
  3. Southern suites represent "a single suite in name, but distinct psychological beats in reality"; **all major dramatic pivots occur within the spoken dialogue**.  
  *Acoustic Reality*: When music swells, *"even the finest lyrics register at only seventy percent clarity; yet spoken dialogue is comprehended by every ear word for word."* Li Yu's self-audit technique: *"While the hand grips the brush, the mouth must step upon the stage."* *Self-check*: If a line reads elegantly in the study but sounds muddy when spoken aloud, you failed to write from the perspective of the speaking actor and listening audience.

---

## 8. Bangqiang: The Gaoqiang Textual Apparatus

**Bangqiang**: In Gaoqiang opera (Sichuan Gaoqiang, Yiyang vocal traditions), short choral phrases delivered by the percussion orchestra or offstage ensemble. **The Banqiang system lacks this apparatus**, which is why it receives dedicated focus here. Empirical evidence is drawn from Wei Minglun and Nan Guo's *The Scholar of Bashan (Bashan Xiucai)* (9th draft, 1983; Sichuan Opera Gaoqiang), spanning 9 choral passages.

- **Treated as an Onstage Dramatic Character**: The script places "Bangqiang" at the head of the dialogue line, occupying the identical structural position as a dramatis persona.
- **Four Dramatic Functions (Assign only one function per instance)**:  
  1. *Narrator* (revealing facts the character cannot or will not state—when the scholar doubts his own survival, Bangqiang announces: "A survivor snatched from the jaws of catastrophe");  
  2. *Commentator* (unmasking hypocrisy, demanding an accounting—as Nishang sings "Softly singing...", Bangqiang cuts in: "Faking a smile!");  
  3. *Surrogate Agent* (speaking on the character's behalf or making their decision);  
  4. *Emotional Amplifier* ("No inns upon the Yellow Springs road..." answered by: "Where shall they rest, three thousand wronged souls of Bashan?", completing the poetic couplet while transposing the subject from 'I' to 'three thousand souls').  
  Also provides structural lead-ins and line completions. *Self-check*: Assign a single functional tag to each choral passage; if it lacks a tag, delete it. If it shifts functions mid-passage, the audience loses the acoustic identity of the voice.
- **Three Formal Rules**:  
  1. **Extreme brevity** (six of nine instances contain only 3–7 characters)—**Bangqiang never delivers extended lyrical monologues**;  
  2. **Positioned strictly at points where the character is emotionally or physically incapable of continuing song**;  
  3. **Bangqiang can execute tune modulations** (launching [Guagu Ling], initiating [Xiaoshun Ge], pulling the character into the new melody). *Self-check*: If a Bangqiang line exceeds seven syllables, justify why that line was not given to a dramatic character.
- **The Solitary Exception: When a Character Hears and Obeys Bangqiang.**  
  Bangqiang sings: *"Take your wife and escape to Chengdu!"* Meng Dengke responds in spoken dialogue: *"Ha! That offstage chorus offers fine advice!"* and flees → Bangqiang pivots from "the voice of the community" into "the voice of Fate." **Permitted at most once in an entire opera**, positioned strictly when the character is at a total dead end; using it twice degrades the chorus into a mundane supporting character.

---

## 9. Adaptation & Script Overhauls

- **Li Yu's Boundary of Essence vs. Posture**: *"Preserve the fundamental essence; transform the external posture."*  
  - *Essence = Poetic lyrics and primary dramatic turns: do not alter.*  
  - *Posture = Comedic business and nuanced spoken dialogue: must be radically overhauled.*  
  **Resolve narrative gaps using existing characters before inventing new ones** (Xiao'er in *Pipa Ji*, Caipin in *Mingzhu Ji*). *Failure condition*: Li Yu revised *Pipa Ji* to satisfy Ming/Qing chastity ethics; **borrow his technical craft, never his historical ideological motives.**
- **Condensing Epics (The Elastic Script Method)**: *"Better a concise drama with a definitive ending than an sprawling epic abandoned mid-way."* Mark dispensable scenes with coded tags; **the art lies in "Adding While Subtracting"**—interpolate brief lines in the subsequent scene to acknowledge the pruned event, or plant premonitions in the preceding scene.
- **Converting Classical Epics into Stageworthy Scripts: Wang Jilie's Adaptation of *The Purple Hairpin (Zichai Ji)***.  
  Begin with diagnosis: *"Tang Xianzu's Four Dreams suffer from flawed staging balance... The staging of Zichai Ji is profoundly disjointed, rendering it genuinely unperformable."* Select 14 scenes for performance, logging every deleted tune and its dramaturgical rationale (excessive slow tunes, vocal exhaustion, redundant plot). **This stands as the sole primary historical record of converting an unperformable classical epic into a stageworthy text**, cross-referencing `sw-format-adaptation`.
- **One Action, Three Results (Wu Mei's audit of four historical adaptations)**:  
  - Feng Menglong's definitive promptbooks refined metric notation → **Masterpiece**;  
  - Saoyin Sheng adapting *Bu Fulao* from Northern to Southern modes → **Masterpiece**;  
  - *Southern Western Wing* adapting Northern Zaju into Southern modes → **Failure** (when modal suites failed to align, the adaptor grabbed arbitrary tunes from foreign modes sharing similar line lengths);  
  - Zang Jinshu rewriting the Four Dreams to force metric conformity → **A Different Failure** ("Focuser purely on prosody while ignoring poetic genius... turning gold into lead").  
  **Three Enduring Lessons**:  
  1. Adapting Northern plays into Southern modes cannot be achieved by hunting for tunes with similar syllable counts; you must recompose the entire architecture under the target modal system;  
  2. Textual adaptations must explicitly specify metric percussion beats (*Banshi*);  
  3. Metric conformity and dramatic vitality are two independent verification scales; one must never consume the other.  
  **When lyrics clash with musical meters, alter the Qupai tune, not the words** (Niu Shaoya, *Corrected Tunes for The Peony Pavilion*: "Converts into pastiche suites... leaving the original poetic text untouched by a single character"). *Self-check*: If you alter more words than tunes, your methodology is flawed. *Failure condition*: If the original phrasing is syntactically broken, you must revise the phrasing.
- **Tang Xianzu's Four Operations in Adapting Classical Tales** (Collation against the source tale *Du Liniang's Passionate Return*):  
  1. **Prune family relatives** to isolate the protagonist in psychological desolation;  
  2. **Convert legal actions into capital crimes** (exhuming the corpse was changed from an official action sanctioned by the Prefect into grave-robbing executed privately by Liu Mengmei, violating the Ming Code: "Exhuming graves to expose corpses warrants decapitation")—igniting the conflict driving the entire second half of the opera;  
  3. **Transform love at first sight into "Erotic dreams followed by mourning the dream"**;  
  4. **Retain the finest lines from the original tale verbatim inside spoken dialogue, updating only the sung lyrics** (altering only one character in the portrait inscription: "If not beside the plum, then beside the willow").  
  *Self-check*: Audit each revision: "Did this change generate a more formidable adversary or introduce fresh legal jeopardy?" Superficial verbal polishing without structural escalation does not constitute dramatic adaptation.

---

## 10. Contemporary Modern Qupai Opera

**This section co-exists alongside classical prosody as an equal discipline.** Contemporary practice directly challenges Wu Mei and Wang Jilie's doctrine of "strict metric adherence"; both classical and modern lineages are preserved side by side.

- **Weng Ouhong (Peking Opera Master Writing Kunqu)**: In *Havoc in Heaven* and *Gaoliang Rushing for Water*, he composed full-length Kunqu operas **without using unified suites, opting instead for "Scattered Jewels (*Lingjin Suiyu*)" across shifting tunes**, bridging transitions via melodic modulation because "traditional suites impose excessive constraints upon theatrical momentum."
- **Wei Minglun & Nan Guo's *The Scholar of Bashan* (Sichuan Gaoqiang, 1983) Four Breakthroughs**:  
  1. **Abolishing Modal Suites**: Across eight scenes, **Gongdiao modes appear 0 times**; identical tunes repeat across different scenes and characters ([Hongna'ao] is shared by a blacksmith, a corrupt official, and a courtesan); the only relic of suite structure is the "Continues Singing" notation.  
  2. **Scattered Jewel Selection Based on Emotion and Scale**: Selecting tunes via an emotional/duration matrix ([reference-jinji.md](reference-jinji.md) §13)—the operational logic answers "how long does this emotion last and at what pitch register," discarding "which mode governed the preceding tune."  
  3. **Half-Metric Discipline**: **Sustaining a single rhyme across an aria block remains absolute** ([Xiangluo Dai] maintains 24 lines in *You-Qiu* rhyme); **syllable counts and tonal pitch rules are completely liberated**.  
  4. **Expanding the Tune Title into a Performance Stage Direction**: Tune slots indicate vocal genres ("Kunqu"), foreign Banqiang meters (Peking Opera "Xipi Erliu"), or vocal delivery ("Rhymed Dialogue / Yunbai").
- **Luo Huaizhen's *Ban Zhao* Pursues the Exact Opposite Path**: Composed in contemporary vernacular Chinese, **"yet not a single syllable breaks metric rules"**; odd-syllable tones, line-end rhymes, and Entering-tone distributions are strictly observed, at the cost of **"taking two full days to fill a single Qupai tune."**
- **Synthesis and Divergence**: All three masters discard Gongdiao modes as rigid acoustic keys, treating them instead as indexes of emotion and structural scale. **The debate remains open**: Weng and Wei liberate suites and syllable counts; Luo preserves syllable metrics while modernizing vernacular diction. **Two dramatists across two distinct regional genres and eras (Weng and Wei) independently reached the identical conclusion: modern opera abandons rigid suites**; yet *Ban Zhao* proves classical metric fidelity remains viable.  
  *How to Choose*: Does the production integrate into the historical vocal repertory of Kunqu? If yes, follow Luo (fill by metric score; budget extensive writing time); if not, and the genre possesses a living library of tunes (Sichuan Gaoqiang), follow Weng and Wei (scattered jewels; strict rhyme with flexible syllable counts).
- **The Critical Negative Diagnostic: "Pseudo-Youth Kunqu"**: *"At its core, teenage performers merely parrot the decaying, exhausted breath of late-Ming literati"* (Luo Huaizhen). *Self-check*: Are the sentiments uttered by young characters their authentic psychological truths, or are they hollow echoes of literati who died three centuries ago?

---

## 11. Masterpieces Also Break Prosodic Rules

**The universal maxim: *"Study their literary brilliance, do not imitate their prosodic errors."*** (Wu Mei on Tang Xianzu's Four Dreams). Celebrated texts and their authenticated flaws:  
- ***The Peony Pavilion* & The Four Dreams**: Excessive padding rendering lines impossible to phrase; Scene 28 (*Underworld Vow*) corrupting modal keys; flawed staging pacing throughout; blending Level/Departing rhymes with Entering tones;  
- ***The Peach Blossom Fan***: Frequent pitch/tonal lapses; awkward padding; metric errors in Scene 5 (*Passing Song*); replacing a Northern tune with Southern [Chaotianzi] in Scene 38, "destroying the artistic intent of a joint suite"; "possessing sublime poetry but ruined melody";  
- ***Southern Western Wing***: Suite structures entirely unviable (see §9; Li Yu branded it "the chief offender among theatrical corruptions");  
- ***The Tale of the Lute (Pipa Ji)***: Failing to distinguish *Zhi-Shi* from *Yu-Mo* rhymes; merging *Ge-Luo* with *Jia-Ma*; inverting words to force rhymes; **the final eight scenes are unauthentic additions by later hands**;  
- ***The Moon-Worship Pavilion (Baiyue Ting)***: Abundant obscure tunes lacking metric beats; sharing blame with *Pipa Ji* for abandoning modal discipline;  
- ***The Jade Hairpin (Flirting with the Zither)***: Illicitly mixing *Geng-Ting*, *Zhen-Wen*, and *Qin-Xun* rhymes;  
- ***The Gold Thread Pond***: Act 4 lacking a coda (*Weisheng*)—the third permissible condition for omitting a coda. For exact citations and page numbers, see [reference-jinji.md](reference-jinji.md) §14.

**Two Operational Rules**:  
1. Before citing a classical aria as a structural benchmark, check whether it appears on this list of prosodic errors; if so, avoid emulating the flawed element;  
2. **"An ancient predecessor marked it this way" does not constitute binding authority** (§1.5).

**Two Inviolable Historical Disagreements**: Wang Jilie attacked Jin Shengtan's revisions of *The Western Wing* ("Jin Shengtan's vernacular sketches captured the authentic genius of the Yuan masters... his alterations brought catastrophe upon the play"); Wu Mei and Wang Jilie condemned *The Peach Blossom Fan*, yet Kong Shangren's principles defined their own coherent dramaturgical system (8-aria quotas, rejection of Tang collations, comprehensive dialogue)—**a playwright's operational manifesto and a prosodist's critique represent two distinct coordinate systems; record both.**

---

## 12. Medium Boundaries: The Qupai System vs. Banqiang System

| Dimension | **Qupai System (曲牌体)** | **Banqiang System (板腔体)** |
|---|---|---|
| **Vocal Monopoly** | In Zaju, a single actor monopolizes singing across an entire act; **Singing Right = Protagonist Status** | Singing is distributed across role types (*Hangdang*); anyone can sing |
| **Modal Echoes** | Achieves cross-scene thematic resonance via identical Gongdiao modes and tune families | Impossible; metric tempos (*Banshi*) do not categorize emotion by modal keys |
| **Tune Titles** | Titles generally offer **zero indication of emotional content**, often retaining obscure dialect origins | Metric names (*Banshi*) directly announce tempo, rhythm, and emotional intensity |
| **Rhyme Discipline** | An entire act/scene sustains one rhyme to the end; four acts use four distinct rhymes; repeated rhymes allowed in scripts | An aria block sustains one rhyme; scenes modulate rhymes freely throughout the opera |
| **Offstage Chorus** | Gaoqiang's indigenous Bangqiang acts as an onstage character: narrating, judging, or executing modulations | Lacks Bangqiang; functional equivalents are ensemble refrains (*Hetou*) and offstage singing |

General screenwriting craft principles apply (Kishōtenketsu holds valid, BS2 beat page counts are invalid, conventions are not exposition, enter-late-leave-early fails in opera); see `sw-chinese-opera-banqiang` §0.2. Furthermore: **"One Protagonist, One Central Event" belongs to the Li Yu / Qupai tradition**; Banqiang opera expresses the identical principle as "Longitudinal Concentration"; each discipline retains its indigenous terminology.

---

## 13. Diagnostic Checklist, Workflow, & Training

### 13.1 Diagnostic Checklist

1. **Stage or Study?** If unanswered, the matrix in §1.4 cannot function.  
2. **Did you audit the draft in two separate passes**—one examining staging balance and dramatic turns, and the other examining lyrics, modes, and rhymes (§1)?  
3. **Zaju**: Are the four acts set to four distinct Gongdiao modes? Is Act 1 Xianlü and Act 4 Shuangdiao (§2)?  
4. **Zaju**: Columnize character speech tags; does a second singing character appear within the four acts? Does the subject of the final naming line match the primary singer (§2)?  
5. **Chuanqi**: In which scene do the romantic leads emerge? If the male lead dominates the preceding scene, does he dominate the subsequent scene (§3)?  
6. **Columnize the rhyming characters of each scene**; do rogue words from foreign rhyme groups infiltrate the list (§2, §4)?  
7. **Can you identify the Wutou line and its key syllables in every aria?** If not, the aria is dramatically dead (§4). In Southern tunes, do padding syllables fall strictly on dense beats at the beginning/middle of lines, never exceeding three syllables (§4)?  
8. **Do all tunes in a suite belong to the same Gongdiao mode?** If modulating, do they share a flute pitch register? What concrete event occurred onstage at the exact moment of modal transition (§5)?  
9. **Chart scenes by "Lead Singer / Emotional Atmosphere"**; do three consecutive scenes share the same character or mood? Do transitional vignettes separate major dramatic set-pieces (§6)?  
10. **Does the longest romantic confession suite land on the scene of greatest value reversal** (§5, §6)?  
11. **Can the opening conjunction of every aria find its immediate syntactic anchor in the preceding line of spoken dialogue** (§7)?  
12. **Does every Bangqiang passage carry a single, distinct functional tag?** Does it stay within seven syllables (§8)?  
13. **Adaptation**: Did you alter more words than tunes? If yes, your methodology is flawed (§9).  
14. **Contemporary Modern Opera**: Are you pursuing "strict metric filling" or "scattered jewel selection"? Have you budgeted the distinct operational costs of your chosen path (§10)?  
15. **Does the classical aria you cited as a benchmark appear on the flawed list in §11?** Is the final line of the coda the most striking poetic line of the suite? Has a singer performed every aria aloud to verify phrasing?

### 13.2 Playwriting Workflow

1. **Resolve the Two Core Switches**: Stage vs. Study (§1.4); Zaju vs. Chuanqi (§2 vs. §3). Modern contemporary operas follow §10.  
2. **Define the Core Dramatic Engine**: Compress the narrative into "One protagonist + a single four-character dramatic deed," then audit secondary subplots (§6).  
3. **Lay Out Scene Sequences (*Paichang*)**: Establish total scale (Chuanqi ≤ 40 scenes; Zaju = 4 acts + 1 wedge); construct a master scene table detailing emotional category, lead singer, and warm/cold atmosphere; audit via the Law of Staging Alternation (§3, §6).  
4. **Scene-by-Scene Emotional Architecture**: Determine dramatic emotion → select matching Gongdiao mode → assemble tunes within that mode into a suite (§5.2, §5.3); arrange Southern tunes by Slow / Medium / Fast tempos (§5.4), and Northern suites by ancient opening/closing formulas (§2).  
5. **Draft Spoken Dialogue & Stage Directions (*Kejie*)**: First draft the dialogue interface anchoring the opening sung line (§7); then **fill lyrics**—consult vocal scores for syllable counts, caesuras, and tones; consult rhyme manuals for rhyme groups; designate the Wutou before writing the climactic lines (§4.4); manage padding syllables according to Northern vs. Southern rules (§4.3).  
6. **Singing Verification Circuit (*Anjie Er Ge*)** (§4.7) → **Run the Six Essential Checks of the Forty Prohibitions** (§4.5) → Run the Diagnostic Checklist (§13.1). If preparing both extended and abridged performance scripts, apply the "Adding While Subtracting" method (§9).

### 13.3 Craft Exercises

- **Filling Lyrics to a Rigid Classical Mold**: Take [Xiashan Hu] (*The Moon-Worship Pavilion*), annotate every syllable with its four-tone pitch contour, and fill entirely new dramatic content syllable by syllable; compare old and new texts—if a single tone deviates, rewrite the line. *"The more severe the constraint, the more exquisite the mastery."*  
- **Dual-Track Comparative Exercise**: Take an identical dramatic scene and draft it twice: once via strict metric filling (Luo Huaizhen's method), and once via scattered jewel selection (Wei Minglun's method); compare writing hours against stage performance vitality (§10).
