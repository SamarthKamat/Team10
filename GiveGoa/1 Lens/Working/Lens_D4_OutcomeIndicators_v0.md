---
title: "Lens D4 · Outcome Indicators for Funder-Ready (draft v0)"
subtitle: "Project A Lens · Team 10 · Owner SRS · To H · Funder-Ready · Draft sent early per Data Exchange Plan · Final due Fri 15 Jan 2027"
---

# 1. Main result

This is the first draft of the Lens outcome indicators for the LVP funder pack. It has **10 indicators** in 3 groups: reach and participation, strengths found, and growth. Each has a definition, a formula, a data source in the Lens profile, and a reporting rule.

**There are no values in this file.** Lens runs on synthetic personas only. No number from Lens may go into the funder pack as a real result until URF pilots Lens with consent and safeguarding sign-off. Values from synthetic personas may be shown only as "illustrative, synthetic".

**Who receives it:** H · Funder-Ready. The URF project page and programme overview say **Team 22**. Our Lens proposal says "Team 17" in two places (subgoal 4 and the D4 acceptance test). This must be corrected in the charter. See the message to Souvik.

# 2. Indicator list

| ID | Indicator | Definition | Formula | Source field(s) in the Lens profile | Reporting rule |
|---|---|---|---|---|---|
| L-OI-01 | Learners with a Lens profile | Learners assessed with Lens v1 who have a profile in the shared record | count of `learner_code` with `lens_version` = v1 | `learner_code`, `lens_version` | By NEP stage. Aggregate only. |
| L-OI-02 | Complete profiles | Share of profiles with a score for at least 15 of 18 constructs | profiles with ≥ 15 reported scores ÷ L-OI-01 | `<CODE>_score` | Percent, 0 decimals |
| L-OI-03 | Accessible participation | Share of items offered in a format the learner could use | 1 − (`items_na` ÷ `items_total`), mean over learners | `items_na`, `items_total` | Percent. Low values mean the **instrument** needs a format, not the learner. |
| L-OI-04 | Child voice recorded | Share of scored items with the child's own (self) response beside the observer's | self rows ÷ observer rows | response file | Percent |
| L-OI-05 | Instrument shade coverage | Number of the 7 URF shades (P1–P7) for which every indicator has at least one usable format | count from ANA's Item Format Table | `Lens_ItemFormatTable` | 0–7. An instrument measure; never per learner. |
| L-OI-06 | Learners with a named strength | Share of learners with at least one construct in band "strong" | learners with ≥ 1 strong ÷ L-OI-01 | `<CODE>_band` | Percent |
| L-OI-07 | Learners with an EBA pathway strength | Share of learners with band developing or strong in an EBA-tagged construct at their stage | learners meeting rule ÷ L-OI-01 | `<CODE>_band`, D1 EBA tags | Percent. Links to green livelihoods. |
| L-OI-08 | Profiles used for a support plan | Share of profiles loaded by Trajectory and given a ranked support | Trajectory pictures from Lens profiles ÷ L-OI-01 | Trajectory output | Percent. Needs Trajectory D4. |
| L-OI-09 | Growth in a strength area | Mean change in construct score between two Lens assessments at the same stage, 6–12 months apart | mean(score₂ − score₁) | two profiles | Points, 0–100 scale. Only after a pilot. |
| L-OI-10 | Band progress | Share of learners who move up at least one band in at least one construct between two assessments | learners meeting rule ÷ learners with 2 assessments | two profiles | Percent. Only after a pilot. |

# 3. Rules for every indicator

1. **Aggregate only.** Report a group only if it has 10 or more learners (team rule, to protect privacy; URF to confirm the threshold).
2. **No shade breakdown next to strength scores.** Shade codes may be used only for L-OI-03 and L-OI-05 (access and coverage), never to compare strengths between shades.
3. **Never rank or compare children or schools.** The indicators describe the programme and the instrument.
4. **Every value has a source.** Each value names the profile file, date and Lens version. Synthetic values are labelled "illustrative, synthetic".
5. **No baselines yet.** Baselines are set in the first pilot cycle (D5 pilot plan).

# 4. What Funder-Ready needs to confirm (acceptance test)

D4 is accepted when Funder-Ready confirms it can use these indicators in the funder pack. Questions for them:

1. Which of the 10 indicators fit the LVP pack? Can we drop any?
2. Do you need a file (CSV with `indicator_id, period, group, value, n, source`) or only the definitions?
3. Do you need an SDG link per indicator? Draft: L-OI-01 to L-OI-05 → SDG 4.5 (equal access for persons with disabilities); L-OI-07 → SDG 4.7 / SDG 8 [VERIFY AT SOURCE: SDG target wording at unstats.un.org/sdgs/indicators].

# 5. Self-check

- Synthetic only, no values: pass.
- Strengths framing: pass. Low access values point to the instrument, not the learner.
- No fabricated numbers: pass. The 10-learner threshold is a team rule, marked for URF to confirm. SDG targets marked [VERIFY AT SOURCE].
- Plain English: pass.
