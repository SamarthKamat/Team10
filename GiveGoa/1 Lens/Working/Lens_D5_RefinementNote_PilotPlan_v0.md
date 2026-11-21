---
title: "Lens D5 · Refinement Note, Pilot Test Plan and Handover (draft v0)"
subtitle: "Project A Lens · Team 10 · Owner SRS · Due Fri 29 Jan 2027 · Accepted when the next cohort could continue from it alone"
---

> **How to use this draft.** Sections 2 and 3 are complete now: the pilot plan does not depend on later results. Sections 1, 4 and 5 have a fixed structure and the facts known on 21 Nov 2026. Fill the `[TO FILL]` parts after D3 (18 Dec) and after Trajectory's feedback (Jan).

# 1. Main result `[TO FILL in Jan]`

Lens v1 is `[status]`. It has `[n]` items for 18 constructs across 3 domains and 5 stages, in `[n]` formats. It covers `[n]` of 7 URF shades fully. It produced profiles for `[n]` synthetic personas, and Trajectory loaded them `[with / without]` rework.

# 2. Pilot test plan (for the next cohort; needs URF consent and safeguarding sign-off first)

Statistical reliability cannot be measured on synthetic data (Lens proposal, Quality checks). This plan says what the first real pilot must measure.

**Preconditions (all required):** URF consent and safeguarding sign-off; parent or guardian consent and the child's own assent in an accessible format; learner codes only; contact only through URF; a trained educator present.

| Question | Method | Data needed | Read the result as |
|---|---|---|---|
| Do two observers score the same behaviour the same way? (inter-rater) | 2 observers score the same session alone. Weighted kappa per item (Cohen, 1968) on the 0–3 scale; ICC for construct scores. | ~20% of sessions double-scored | ICC: < 0.50 poor, 0.50–0.75 moderate, 0.75–0.90 good, > 0.90 excellent (Koo & Li, 2016). Revise anchors for items with low agreement. |
| Are a learner's scores stable over a short time? (test-retest) | Same learner, same stage, 2–4 weeks apart, no new support. ICC (two-way, absolute agreement). | sub-sample | same ICC guide |
| Do items in one construct agree with each other? (internal consistency) | Cronbach's alpha per construct (Cronbach, 1951), only where a construct has 4+ items. | full sample | Use with care for short scales. Low alpha → check item fit. |
| Do items work for every shade? (fairness) | Compare N/A rates and item-score patterns by shade **for items only**, never to compare learners. Rasch partial-credit model and differential item functioning (Masters, 1982) if the sample allows. | full sample | Items with high N/A or a different pattern for one shade get a new format. |
| Does the child agree with the observer? | Self vs observer gap rate (rule R7). | full sample | Many gaps on one item → reword or add an example. |
| Do bands match educators' views? | Educator rates each construct emerging / developing / strong without seeing the score. Agreement with the band. | sub-sample | Informs cut points 33 / 66 (fixed until then). |

**Sample size.** `[VERIFY AT SOURCE]`: choose with URF and the GIM supervisor. Sample-size guidance exists for ICC studies (Koo & Li, 2016 refer to it) and for Rasch calibration (Linacre, 1994). Do not state a number until it is checked at source.

**Output of the pilot:** item revisions; weights $w_i$ and source reliabilities $r_s$ for scoring Option B; baselines for D4 indicators L-OI-09 and L-OI-10.

# 3. Known limits and assumptions (as of 21 Nov 2026)

1. D1 is built on the Playbook fallback base. URF has not yet shared the Pehchan 64 questions or the scoring code. `[Update: date received, mapping done Y/N]`
2. Post-school (18–35) is a Team 10 band, not an NEP stage.
3. Shade mappings for RPwD Schedule 4(a), 4(b), autism and multiple disabilities use team defaults until URF answers Q1–Q7.
4. Weights are all 1 and bands are fixed cut points until pilot data exists.
5. Persona responses are written from each persona's description, with the reason recorded for every response (Lens proposal, Persona profiles). They show how Lens works. They are not evidence about real children.
6. The proposal says "six shades". URF confirmed 7 shades on 20 Nov 2026. Lens uses P1–P7.

# 4. Refinement log `[TO FILL from Trajectory and URF feedback]`

| # | What we found | Source (who, when) | What we changed | Version |
|---|---|---|---|---|
| 1 | | Trajectory D4 load test | | |
| 2 | | URF mentor D2 review | | |
| 3 | | CP2 feedback (15 Jan) | | |

**Ideas for the next cohort (start list):** scoring Option B with confidence rings on the spider chart; Rasch scaling; a learner-facing "my strengths" view in plain words and pictures; Ability Atlas fields (Team 17) folded into the profile; Pehchan side-by-side scores for one cycle.

# 5. Handover note

| # | Item | Content |
|---|---|---|
| 1 | Deliverables | D1 construct map (FINAL 27 Nov), D2 items and scoring (4 Dec), D3 profiles (18 Dec), D4 outcome indicators (15 Jan), D5 this note (29 Jan) |
| 2 | Where | `GiveGoa/1 Lens/Final/` (accepted versions), `Working/` (drafts). Build scripts: `build/` |
| 3 | How to re-run | `python3 Lens_ScoringEngine_v1.py --selftest`, then `python3 Lens_ScoringEngine_v1.py responses.csv out_prefix` |
| 4 | Inputs used | URF shades P1–P7 (20 Nov 2026); NEP 2020; CASEL 2020; Gardner 1983/1999; RPwD Act 2016; CAST UDL 2.2; Pehchan `[received / not received]` |
| 5 | Decisions | Decision log in the Playbook (fallback base, indicator template, N/A rule, shade defaults, Option A) |
| 6 | Open questions | URF Q1–Q7 (D1 note §7) `[mark answered ones]` |
| 7 | Contacts | Through URF only. Lens team: SRS (lead), ANA (items), AB (data and exchange) |
| 8 | First 3 tasks for the next cohort | 1. Read D1 note and this note. 2. Run the self-test. 3. Plan the pilot with URF (section 2). |

# References

- Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin*, 70(4), 213–220.
- Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297–334.
- Koo, T. K., & Li, M. Y. (2016). A guideline of selecting and reporting intraclass correlation coefficients for reliability research. *Journal of Chiropractic Medicine*, 15(2), 155–163.
- Linacre, J. M. (1994). Sample size and item calibration stability. *Rasch Measurement Transactions*, 7(4), 328.
- Masters, G. N. (1982). A Rasch model for partial credit scoring. *Psychometrika*, 47(2), 149–174.
