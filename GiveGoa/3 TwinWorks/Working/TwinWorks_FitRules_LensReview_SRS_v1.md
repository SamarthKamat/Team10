---
title: "TwinWorks · Review of Fit Rules against Lens Constructs"
subtitle: "Project C TwinWorks · Reviewer SRS (with ANA) · For RMA (lead) and AB (role model) · v1 · 21 Nov 2026"
---

# 1. Main result

I checked the TwinWorks fit logic in Proposal C (section 3) against the Lens v1 constructs, scores and bands. The fit logic can use Lens output with **6 changes**. The most important are: treat "not enough evidence" as unknown, not 0 (C1); do not use a shade as a hard check (C2); and present the fit score as a rehearsal aid that never compares learners (C6). There is also a draft map from the 5 role families to the Lens constructs (section 3), for AB to reconcile with NSQF/NCO 2015 and Talent Bridge's map.

# 2. Review comments

| # | Where in Proposal C | Comment | Suggested change | Priority |
|---|---|---|---|---|
| C1 | Fit logic step 2 (gap per domain) | Lens leaves a construct score empty when fewer than 2 items were scored (rule R4). If the fit run reads empty as 0, an access barrier becomes a "gap". | Empty = unknown. Name it in the output ("not enough evidence for X; check with educator"). Leave it out of the fit score denominator. | High |
| C2 | Fit logic step 1 (hard checks) | "No working condition that the picture marks as unsupported" is correct **only if it reads support needs, not shade codes**. A shade is a support category, not a limit on work. | Hard checks read a `working_condition_supports` field (what support makes the condition workable), never `shade`. If no field exists, the condition goes to support recommendations, not to exclusion. | High |
| C3 | Role model: "required level for each strength domain" | Lens reports 18 constructs and 3 domain scores. A domain average hides the constructs a role needs most. | Set required levels at **construct** level (section 3), with weights for centrality. | Medium |
| C4 | Required levels vs Lens scale | Lens scores are 0–100 and read against the learner's own stage. Roles are entry-level, so learners are Secondary or Post-school. | Use required levels as **bands** (developing / strong), not exact numbers, until a pilot exists. Use only Secondary and Post-school profiles. | Medium |
| C5 | Gap at 12 and 24 months (from Trajectory) | Fine. Trajectory gives a 10th–90th percentile band. | Show the gap as a range; call a gap "closed" only if the 10th percentile meets the required band. | Low |
| C6 | Fit score and ranking | Already presented as a rehearsal aid (risk table). Good. | Rank **roles for one learner**, never learners for one role. Words: "Role X fits your strengths in A and B; support C helps with D." No "unsuitable". | High |

# 3. Draft map: role families → Lens constructs (for AB to reconcile)

Central = weight 2, supporting = weight 1. Required band: D = developing, S = strong. These are **team judgements**, to be replaced by NSQF Qualification Pack and NCO 2015 requirements [VERIFY AT SOURCE: AB's TwinWorks_NSQF_Links_v1] and Talent Bridge's role-to-strength map.

| Role family | Central constructs (weight 2) | Supporting constructs (weight 1) | Draft required band | EBA link |
|---|---|---|---|---|
| 1 · Production and assembly | MI_BOD, PR_SEQ, MI_SPA | ER_SM, ER_REL | D | None |
| 2 · Quality inspection and testing | PR_PAT, PR_CLS, MI_LOG | MI_SPA, ER_RDM | D (PR_PAT: S) | None |
| 3 · Packaging, stores and logistics | PR_CLS, PR_SEQ, MI_SPA | MI_LOG, ER_REL | D | None |
| 4 · Laboratory and documentation support | PR_SEQ, MI_LOG, MI_LIN | ER_SM, PR_CLS | D | None |
| 5 · EHS and site greening | MI_NAT, PR_CAU, ER_RDM | MI_INTER, ER_SOC | D (MI_NAT: S) | Environment, Biodiversity, Agriculture |

**Fit score using Lens bands (proposal):** $\text{fit} = \dfrac{\sum_c w_c \cdot \text{met}_c}{\sum_{c \,\text{known}} w_c}$, where met = 1 if the learner's band meets the required band (projected by Trajectory), else 0. Unknown constructs are left out and listed (C1).

# 4. Fields TwinWorks needs from the Lens profile (all in `Lens_ScoringEngine_v1` output)

`learner_code`, `stage`, `<CODE>_score`, `<CODE>_band`, `<CODE>_n`, `top_strengths`. TwinWorks does **not** need any shade field from Lens.

# 5. Self-check

- Synthetic only: pass. No persona data.
- Strengths framing: pass. Changes C1, C2 and C6 protect learners from deficit readings.
- No fabricated numbers: pass. Weights and bands are labelled team judgements. Role requirements are marked [VERIFY AT SOURCE].
- Plain English: pass.

**Time used:** about 1.5 h of my 10 TwinWorks review hours. Next review: D2 fit logic spec (Jan).
