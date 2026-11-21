---
title: "Lens D2 · Scoring Rules and Validity Checks"
subtitle: "Project A Lens · Team 10 · Version 1 · Owner SRS · Items: ANA · Scripts and export: AB · Due Fri 4 Dec 2026"
---

# 1. Main result

This note gives the full scoring rules for Lens v1 (SRS owns these in the proposal: "scoring rules and validity checks"). The rules turn item scores into one profile per learner, in fields that Trajectory can load.

- **Item scores:** 0–3, from the D1 rubric. N/A when the item was not offered in a format the learner can use.
- **Construct score:** percent of the maximum, 0–100, over the scored items only (Option A from D1).
- **Bands:** emerging 0–33, developing 34–66, strong 67–100.
- **Engine:** `Lens_ScoringEngine_v1.py` applies all the rules. It has a self-test (15 checks, all pass) and an illustrative example (EX-01, EX-02, invented, not data).
- **Validity:** a content-validity rating sheet (I-CVI) for the Lens team and the URF mentor, plus the accessibility check from D1.

**What D2 still needs from others:** ANA's item bank (2 or more items per indicator, in 2 or more formats), and AB's profile schema to confirm the field names. The rules here do not depend on the exact item wording.

# 2. Inputs and outputs

**Input file (one row per item response).** Columns: `learner_code, stage, construct_code, item_id, source, score`.

| Field | Allowed values | Note |
|---|---|---|
| learner_code | persona code (P01…, EX-01…) | never a name |
| stage | Foundational, Preparatory, Middle, Secondary, Post-school | the learner's own stage |
| construct_code | the 18 codes in D1 `ConstructList` | MI_LIN … PR_PRB |
| item_id | from ANA's item log, e.g. `NAT-P-1` | construct-stage-number |
| source | observer, task, self | self = the child's own response |
| score | 0, 1, 2, 3, NA | NA = not offered accessibly |

**Output (one profile per learner, CSV + JSON).** For each construct: `<CODE>_score` (0–100 or empty), `<CODE>_band`, `<CODE>_n` (items scored). For each domain (MI, ER, PR): score and band. Plus `top_strengths` (up to 3 codes), `items_total`, `items_na`, `notes`, `lens_version`, `scoring_rule`.

# 3. The scoring rules

| Rule | What it says | Why |
|---|---|---|
| R1 · N/A is never 0 | An item not offered in an accessible format is N/A. It is left out of every sum and average. | An access barrier must not lower a strengths score. |
| R2 · Which scores count | The profile uses observer and task scores. The child's self-report is recorded and shown beside them. | Agreed in D1 (Playbook). Option B can add self-report weight after a pilot. |
| R3 · Construct score | $S_c = 100 \times \dfrac{\sum_i w_i x_i}{3 \sum_i w_i}$ over scored items. Default weight $w_i = 1$. Round half up to an integer. | Same scale for every construct; works in Sheets and NestJS. |
| R4 · Minimum evidence | Report a construct only if 2 or more items were scored. Else write "not enough evidence" (empty score). | One item is too little to describe a strength. |
| R5 · Bands | On the rounded integer: 0–33 emerging, 34–66 developing, 67–100 strong. | Fixed after D2; Trajectory and TwinWorks use them. |
| R6 · Domain score | Mean of the reported construct scores in the domain. Needs 3 or more reported constructs. | Keeps the 8-axis MI chart and adds ER and PR charts. |
| R7 · Self vs observer | If self-report and observer differ by 2 or more points on one item, write a note. Change neither number. | The child's view is kept and discussed, never overwritten. |
| R8 · Top strengths | Up to 3 constructs with the highest score in band developing or strong. Ties: more items first, then code order. | Feeds Trajectory `top_strengths`. Ranks inside one learner only. |
| R9 · No comparison across stages | A score is read against the learner's own stage indicators only. | Indicators differ by stage (growth ladder). |
| R10 · Words in reports | Report the skill area, never the child: "Naturalist strength area: strong". Shade codes never appear next to scores. | URF ground rule: strengths and supports, no labels. |

**Rounding examples (from the self-test):** 8/9 → 88.9 → 89 (strong). 2/6 → 33.3 → 33 (emerging). 4/6 → 66.7 → 67 (strong). 10/18 → 55.6 → 56 (developing).

**Google Sheets formula** (for AB's scoring sheet; scores in C2:C20, weights in D2:D20, "NA" as text):

```
=IF(COUNT(C2:C20)<2, "not enough evidence",
    ROUND(100*SUMPRODUCT(ISNUMBER(C2:C20)*IFERROR(C2:C20*1,0)*D2:D20)
          / (3*SUMPRODUCT(ISNUMBER(C2:C20)*D2:D20)), 0))
```

This formula is tested in the `Scoring_Formula_Test` tab of the rating sheet, which gives the same results as the engine.

Band: `=IF(ISNUMBER(E2), IF(E2<=33,"emerging",IF(E2<=66,"developing","strong")), "not enough evidence")`. Note: Sheets `ROUND` rounds half away from zero, which equals "half up" for these positive scores.

# 4. Pehchan compatibility

Pehchan today sums 8 Likert answers for each of the 8 intelligences into a spider chart. Lens keeps the same 8 MI axes, so the existing chart takes `MI_*_score` (0–100) directly.

When URF shares the 64 questions and the scoring code:

1. Map each Pehchan question to one MI indicator in D1 (a new column `pehchan_q` in the item log).
2. Re-score old Pehchan answers with R3 on a 0–100 scale: $100 \times (\text{sum} - 8 \cdot \min) / (8 \cdot (\max - \min))$ for one intelligence. [VERIFY AT SOURCE: the Likert range in Pehchan's code, e.g. 1–5.]
3. Keep both columns for one cycle ("Pehchan score", "Lens score"), so URF can compare. Log the change in the Decision log.

# 5. Validity checks (what we can and cannot check on synthetic data)

| Check | Method | Who | Pass rule | When |
|---|---|---|---|---|
| Content validity: relevance | Each rater scores each item 1–4 for relevance to its indicator. I-CVI = raters giving 3 or 4 ÷ number of raters (Lynn, 1986). | SRS, ANA, AB + URF mentor (+ special educator if URF arranges) | 3–5 raters: I-CVI = 1.00. 6 or more raters: I-CVI ≥ 0.78 (Lynn, 1986; Polit, Beck & Owen, 2007). Scale average S-CVI/Ave ≥ 0.90 (Polit & Beck, 2006). | Mon 30 Nov – Wed 2 Dec |
| Item revision | Items below the pass rule are revised once and rated again, or dropped. | ANA | — | Thu 3 Dec |
| Accessibility coverage | Each indicator has 2 or more formats; each of P1–P7 has at least one usable format per indicator (D1 7-shade table, ANA's Item Format Table). | ANA, SRS | 0 gaps | Thu 3 Dec |
| Originality | Each item logs its author and its inspiration. Nothing from Raven, WISC or any published test. | ANA | 100% logged | Thu 3 Dec |
| Language | Text search for banned words and label words (`build/audit_d1.py` rules applied to the item text). | SRS | 0 hits | Thu 3 Dec |
| Scoring correctness | `Lens_ScoringEngine_v1.py --selftest` | SRS, AB | all checks pass | each change |
| Reliability | **Cannot be measured on synthetic data.** Written into the pilot test plan (D5). | SRS | — | D5 |

**Rating sheet:** `Lens_ContentValidity_RatingSheet_v1.xlsx`. It has one row per item, a column for each rater, and live I-CVI and pass/revise formulas. ANA pastes the item IDs and text from the item log.

# 6. D2 schedule (before exams on 7 Dec)

| Date | Work | Who |
|---|---|---|
| Mon 30 Nov | ANA's item bank v1 in `1 Lens/Working`; rating sheet sent | ANA, SRS |
| Tue 1 – Wed 2 Dec | Ratings (about 45 min each rater) | SRS, ANA, AB, URF mentor |
| Thu 3 Dec | Revise items; accessibility, originality and language checks; run engine on a test file | ANA, SRS, AB |
| Fri 4 Dec | D2 to URF mentor: items, formats, scoring rules, engine, rating results | SRS |

# 7. Self-check against the URF ground rules

- **Synthetic data and codes only:** pass. The example uses EX-01 and EX-02, marked illustrative.
- **Strengths framing:** pass. Bands describe a skill area. N/A protects learners from access barriers.
- **No fabricated numbers:** pass. The only thresholds are cited (Lynn 1986; Polit & Beck 2006; Polit, Beck & Owen 2007). The Pehchan Likert range is marked [VERIFY AT SOURCE].
- **Original items:** the rules hold no items. ANA's items are checked in section 5.
- **Plain English:** pass.

**Verify manually:** open Lynn (1986) and Polit & Beck (2006) and confirm the thresholds before D2 goes to URF.

# References

- Lynn, M. R. (1986). Determination and quantification of content validity. *Nursing Research*, 35(6), 382–385.
- Polit, D. F., & Beck, C. T. (2006). The content validity index: Are you sure you know what's being reported? Critique and recommendations. *Research in Nursing & Health*, 29(5), 489–497.
- Polit, D. F., Beck, C. T., & Owen, S. V. (2007). Is the CVI an acceptable indicator of content validity? Appraisal and recommendations. *Research in Nursing & Health*, 30(4), 459–467.
- CAST (2018). *Universal Design for Learning Guidelines version 2.2.* <https://udlguidelines.cast.org>
- Lens D1 note and construct map (Team 10, 2026).
