---
title: "Lens D1 · Construct Map, Rubric, Scoring Proposal and 7-Shade Check"
subtitle: "Project A Lens · Team 10 · Version 1 · 23 Nov 2026 · Owner SRS · Reviewer ANA"
---

# 1. Main result

Lens D1 is complete for review. It covers **3 domains, 18 constructs and 5 stages: 90 indicators**. Each indicator is one positive behaviour that an observer can see, and each has a source. The 8 Multiple Intelligence constructs keep the 8 axes of the Pehchan spider chart. Emotional & Relational Intelligence and Practical & Non-verbal Reasoning add two new charts with 5 axes each.

The table is in `1 Lens/Working/Lens_ConstructMap_v1` (Sheet and CSV). Columns: Domain, Construct, Indicator, NEP stage, EBA tag, Source.

**Status:** ready for ANA review (T2.4). After the review, copy to `1 Lens/Final/Lens_ConstructMap_v1_FINAL` by Fri 27 Nov, 6 pm.

**Fallback used:** URF has not yet shared the Pehchan 64-question bank or the scoring code. D1 uses the Playbook fallback base (Gardner 8 MI, CASEL 5, original reasoning tasks, NEP 2020 stages, URF shades P1–P7). When the bank arrives, we map each Pehchan question to one MI indicator.

# 2. Indicator template (agreed SRS + ANA)

`[action verb that you can see] + [what] + [context or example]`

- One behaviour in each indicator. Positive words. Correct for the stage. No time limit.
- **Any-mode rule:** "tells", "names", "explains" and "asks" mean any mode: speech, Indian Sign Language, writing, typing, symbols, pointing or AAC.
- Actions can be done with or without aids. Usual access aids are never counted as "support".
- Example: *Social awareness, Preparatory: "Sees that a classmate is sad, and helps or tells an adult."*

# 3. Construct list

| Domain | Constructs (code) | Source |
|---|---|---|
| 1 · Multiple Intelligences | Linguistic (MI_LIN), Logical-mathematical (MI_LOG), Spatial (MI_SPA), Bodily-kinaesthetic (MI_BOD), Musical (MI_MUS), Interpersonal (MI_INTER), Intrapersonal (MI_INTRA), Naturalist (MI_NAT) | Gardner (1983); Gardner (1999) for naturalist |
| 2 · Emotional & Relational | Self-awareness (ER_SA), Self-management (ER_SM), Social awareness (ER_SOC), Relationship skills (ER_REL), Responsible decision-making (ER_RDM) | CASEL (2020) |
| 3 · Practical & Non-verbal Reasoning | Pattern reasoning (PR_PAT), Classification (PR_CLS), Sequencing & planning (PR_SEQ), Cause-and-effect reasoning (PR_CAU), Everyday problem solving (PR_PRB) | NCF-FS 2022, NCF-SE 2023; Sternberg (1985). All tasks original. |

Stages: Foundational (3–8), Preparatory (8–11), Middle (11–14), Secondary (14–18) from NEP 2020 §4.1–4.2, plus Post-school (18–35), which is Team 10 scope and not an NEP stage. Each construct has one indicator for each stage, so the indicators make a growth ladder.

EBA tags (draft for ANA): Naturalist (all 5 stages), Responsible decision-making (Secondary), Cause-and-effect (Preparatory, Middle, Secondary). All other rows: None.

# 4. 0–3 scoring rubric

| Score | Meaning | Behaviour anchor |
|---|---|---|
| 0 | Not observed | The observer did not see the behaviour in this session, in any format offered. |
| 1 | With much support | Shows the behaviour with a full model, hand-over-hand help or step-by-step prompts. |
| 2 | Sometimes / some support | Shows the behaviour sometimes, or after one hint, a reminder or a partial model. |
| 3 | Consistently, no support | Shows the behaviour each time with no support beyond usual access aids. |
| N/A | Not offered accessibly | The item was not given in a format the learner can access. N/A is left out of every average. |

Rules: record the self-report and the observer score next to each other; the profile uses the observer score; if they differ by 2 points or more, write a note and do not change either number. Report the skill area, not the child: "Naturalist strength area: strong".

# 5. Scoring: roll-up and two proposals for URF

**Agreed roll-up (Playbook):** construct score = mean observer item score ÷ 3 × 100. Round to an integer, then band: 0–33 emerging, 34–66 developing, 67–100 strong. These bands are fixed after D2 because Trajectory and TwinWorks use them.

**Pehchan today:** sum of 8 Likert answers per intelligence. Problems: self-report only, no accessible formats, a missing answer lowers the sum, no stage reference.

**Option A (recommended for D2): stage-anchored percent-of-maximum with an N/A rule**

$$S_c = 100 \times \frac{\sum_i w_i x_i}{3 \sum_i w_i}$$

over the items of construct *c* that were scored (not N/A). Report only if 2 or more items were scored; else show "not enough evidence". Default weight w~i~ = 1. Each learner uses the indicators of their own stage.

- Pros: transparent; an access barrier never becomes a low score; works in Sheets and NestJS now; 8 MI scores go to the existing spider chart with no change.
- Cons: weights are a judgement until pilot data exists; scores are not compared across stages (by design).

**Option B (propose for v2 after a pilot): multi-source, evidence-weighted score with a confidence band**

$$S_c = \frac{\sum_s r_s S_{c,s}}{\sum_s r_s}, \quad s \in \{\text{observer, task, self-report}\}, \qquad \text{band} = S_c \pm 1.96\,\mathrm{SEM}, \ \mathrm{SEM} = SD_c\sqrt{1-\alpha_c}$$

r~s~ is the reliability of each source from the pilot (Cronbach's α). Until the pilot, r~s~ = 1 for all sources (assumption).

- Pros: the child's own voice counts; shows how sure we are (a ring on the spider chart); improves as data grows.
- Cons: needs pilot data; changes the Playbook rule "the profile uses the observer score", so it needs URF approval and a decision-log entry.

**Later (D5 note only):** Rasch partial-credit model for interval-scale scores and item-fit checks. Needs a pilot sample [VERIFY AT SOURCE: sample-size guidance, Linacre 1994].

**Display add-on:** rank constructs inside one learner and show the top 3 as "signature strengths". This feeds Trajectory `top_strengths` and never compares children.

The sheet `Scoring_Example` shows all formulas on illustrative numbers for an invented learner EX-01 (not data).

# 6. 7-shade accessibility check (P1–P7)

| Code · Shade | RPwD Act 2016 (Schedule) | Possible barrier | Main adjustments (UDL) |
|---|---|---|---|
| P1 · Purple Vision | 1B blindness, low vision | Pictures, print, visual patterns | Audio, tactile objects and diagrams, large print, high contrast, screen reader |
| P2 · Purple Hear | 1C deaf, hard of hearing | Spoken instructions, audio, pitch | ISL video, captions, pictures, text; rhythm by vibration |
| P3 · Purple Voice | 1D speech and language | Spoken replies | Pointing, symbol cards, typing, AAC; never score speech clarity |
| P4 · Purple Mind | 2(b) ASD*, 3 mental illness | New places, noise, social demand, time pressure | Quiet place, routine, visual schedule, breaks, no time limit |
| P5 · Purple Learning Disability | 2(a) SLD | Dense text, written replies | Short words, read-aloud, pictures, spoken replies, more time |
| P6 · Purple Intelligence Disability | 2 intellectual disability | Abstract, multi-step items | Concrete objects, hands-on tasks, step-by-step prompts |
| P7 · Purple Physical | 1A locomotor (leprosy cured, CP, dwarfism, MD, acid attack); 4(a), 4(b)* default | Writing, pointing, movement, stamina | Spoken replies, switches, eye-gaze, observer records, short sessions |

\* = open mapping question for URF. Item 5 (multiple disabilities, deaf-blindness): give each shade that applies and mark the primary. All 21 specified disabilities have a shade (sheet `RPwD21_Coverage`). A shade is a support category. Lens never assigns, infers or reports a shade.

# 7. Questions for URF

1. **Q1** Do Schedule 4(a) chronic neurological conditions (multiple sclerosis, Parkinson's disease) sit under P7? *Default: P7.*
2. **Q2** Under which shade does URF record 4(b) blood disorders (haemophilia, thalassemia, sickle cell disease)? *Default: P7 for adjustments only.*
3. **Q3** Is autism spectrum disorder (Act item 2(b)) under P4 Purple Mind or P6? *Default: P4.*
4. **Q4** Can a learner have more than one shade with one primary? Is deaf-blindness P1 + P2? *Default: yes.*
5. **Q5** Where does the shade come from (URF record, family, certificate)? *Default: Lens reads it only to select formats.*
6. **Q6** Are Pehchan's vision and physical measures in Lens scope, and must the output stay as 8 spider-chart scores? *Default: intelligence only; 8 MI axes kept.*
7. **Q7** Does the app show shade names to learners or families? *Default: codes only, in staff views.*

Also needed: the Pehchan 64-question bank, the current scoring code and GitHub repository access.

# 8. Self-check against the URF ground rules

- **Synthetic data and codes only:** pass. D1 has no persona data. EX-01 is marked illustrative.
- **Strengths framing, no labels:** pass. All 90 indicators are positive behaviours. Bands describe a skill area. Shade names never sit next to scores.
- **No fabricated numbers or citations:** pass with manual checks. Numbers used: NEP stage ages, 21 conditions (RPwD Act), 64 questions (URF, 20 Nov). Open each source link in `Sources` and mark Y before Final/.
- **Original items:** pass. Reasoning tasks are Team 10's own work. Nothing is taken from Raven, WISC or a similar test.
- **Plain English:** pass (text search for banned words: none).

**Verify manually before upload:** (1) ANA's 15-minute review; (2) open each source link; (3) URF answers to Q1–Q7, or log the team default; (4) map the Pehchan 64 questions when received.

# 9. Handover note

1. **Deliverable:** Lens D1 Construct Map, `Lens_ConstructMap_v1`, 23 Nov 2026 (FINAL copy on 27 Nov after review).
2. **Location:** `GiveGoa/1 Lens/Working/` (draft), `GiveGoa/1 Lens/Final/` (final).
3. **Use:** (a) filter `ConstructMap` by NEP stage; (b) ANA writes 2 or more D2 items per indicator in the item log; (c) AB uses `ConstructList` codes in the profile schema.
4. **Inputs:** URF shades P1–P7 (20 Nov); NEP 2020; CASEL 2020; Gardner 1983/1999; RPwD Act 2016. Pehchan bank: not received.
5. **Limits and assumptions:** one indicator per construct per stage; Post-school band is team scope; EBA tags are a draft; shade mappings marked OPEN wait for URF.
6. **Next tasks:** D2 items and scoring (Fri 4 Dec); confirm bands; decide Option A or B with URF.
7. **Author:** SRS. Reviewer: ANA.

# References

- CASEL (2020). *CASEL's SEL Framework: What Are the Core Competence Areas and Where Are They Promoted?* <https://casel.org/casel-sel-framework-11-2020/>
- CAST (2018). *Universal Design for Learning Guidelines version 2.2.* <https://udlguidelines.cast.org>
- Gardner, H. (1983). *Frames of Mind: The Theory of Multiple Intelligences.* Basic Books.
- Gardner, H. (1999). *Intelligence Reframed: Multiple Intelligences for the 21st Century.* Basic Books.
- MHRD, Government of India (2020). *National Education Policy 2020.* <https://www.education.gov.in/sites/upload_files/mhrd/files/NEP_Final_English_0.pdf>
- NCERT (2022). *National Curriculum Framework for Foundational Stage.* <https://ncert.nic.in/pdf/NCF_for_Foundational_Stage_20_October_2022.pdf>
- NCERT (2023). *National Curriculum Framework for School Education.* <https://dsel.education.gov.in/sites/default/files/update/ncf_2023.pdf>
- Rights of Persons with Disabilities Act, 2016 (Act No. 49 of 2016), The Schedule. <https://indiacode.nic.in/bitstream/123456789/15939/1/the_rights_of_persons_with_disabilities_act%2C_2016.pdf>
- Sternberg, R. J. (1985). *Beyond IQ: A Triarchic Theory of Human Intelligence.* Cambridge University Press.
- United Nations (2006). *Convention on the Rights of Persons with Disabilities*, Article 24.
- W3C (2023). *Web Content Accessibility Guidelines (WCAG) 2.2.* <https://www.w3.org/TR/WCAG22/>
