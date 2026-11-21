# Team 10 · GiveGoa · Shraddha (SRS, Lens lead) · all SRS deliverables

Folders match the GiveGoa Google Drive. Upload each file to the same path in Drive. Start with `GiveGoa/Shraddha_Full_Project_Roadmap.md`.

| Drive path | File | Task |
|---|---|---|
| 1 Lens/Working | `Lens_ConstructMap_v0.csv` (EBA blank, for Anchal) | T1.3 |
| 1 Lens/Working | `Lens_ConstructMap_v1.xlsx` (open with Google Sheets) + `.csv` | T1.3 → T2.4 review |
| 1 Lens/Final | `Lens_ConstructMap_v1_FINAL.xlsx` + `.csv` (QA_Audit + Review_Signoff tabs) | T4.1 (D1) — upload after Anchal's review |
| 1 Lens/Working | `Lens_D1_Note_v1.docx` / `.md` (rubric, scoring options, 7-shade check, URF questions, handover) | D1 |
| 1 Lens/Working | `Lens_D2_ScoringRules_v1.docx` / `.md`, `Lens_ScoringEngine_v1.py`, `Lens_ContentValidity_RatingSheet_v1.xlsx`, `Lens_ScoringExample_*_ILLUSTRATIVE` | D2 (scoring rules + validity) |
| 1 Lens/Working | `Lens_D4_OutcomeIndicators_v0.docx` / `.md` | D4 draft for Funder-Ready (Team 22) |
| 1 Lens/Working | `Lens_D5_RefinementNote_PilotPlan_v0.docx` / `.md` | D5 draft (pilot plan complete) |
| 3 TwinWorks/Working | `TwinWorks_FitRules_LensReview_SRS_v1.docx` / `.md` | TwinWorks review (SRS) |
| 4 Admin and URF/Checkpoint slides | `Lens_CP1_Slides_v1.pptx` (3 slides + speaker notes) | T3.1 |
| 5 SDG Video | `SDG_Voiceover_RecordingGuide_v1.md` | T3.1 |
| (root) | `Shraddha_Week2_Messages_and_Logs.md` (11 ready messages, log rows, checklist) | T4.1, T4.4 |

`build/` holds the scripts: `python3 build_xlsx.py ../GiveGoa [final]`, `python3 build_cvi.py ../GiveGoa`, `python3 build_pptx.py <out.pptx>`, `python3 audit_d1.py <ConstructMap.csv>`. Engine check: `python3 "GiveGoa/1 Lens/Working/Lens_ScoringEngine_v1.py" --selftest`.
