import csv, os, sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import RadarChart, Reference
from openpyxl.worksheet.datavalidation import DataValidation
import lens_data as d

OUT = sys.argv[1]
os.makedirs(f"{OUT}/1 Lens/Working", exist_ok=True)
HDR = ["Domain", "Construct", "Indicator", "NEP stage", "EBA tag", "Source"]

# CSVs (exact schema)
for name, eba in [("Lens_ConstructMap_v0", False), ("Lens_ConstructMap_v1", True)]:
    with open(f"{OUT}/1 Lens/Working/{name}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(HDR); w.writerows(d.construct_rows(eba))

PURPLE = "5B2C83"; LIGHT = "EFE8F7"; GREY = "F3F3F3"
hfont = Font(bold=True, color="FFFFFF"); hfill = PatternFill("solid", fgColor=PURPLE)
thin = Side(style="thin", color="CCCCCC"); border = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(wrap_text=True, vertical="top")

def table(ws, header, rows, widths, start=1):
    for j, h in enumerate(header, 1):
        c = ws.cell(row=start, column=j, value=h); c.font = hfont; c.fill = hfill; c.alignment = wrap; c.border = border
    for i, r in enumerate(rows, start + 1):
        for j, v in enumerate(r, 1):
            c = ws.cell(row=i, column=j, value=v); c.alignment = wrap; c.border = border
    for j, wd in enumerate(widths, 1):
        ws.column_dimensions[chr(64 + j)].width = wd
    ws.freeze_panes = ws.cell(row=start + 1, column=1)

def title(ws, text, sub=None):
    ws["A1"] = text; ws["A1"].font = Font(bold=True, size=14, color=PURPLE)
    if sub: ws["A2"] = sub; ws["A2"].font = Font(italic=True, color="555555")

wb = Workbook()
# README
ws = wb.active; ws.title = "README"
lines = [
 ("Lens_ConstructMap_v1 · Project A Lens · Deliverable D1 (Construct Map)", True),
 ("Owner: SRS (Lens lead) · Reviewer: ANA · Data owner: AB · Version 1 · 23 Nov 2026 · Status: READY FOR ANA REVIEW (T2.4)", False),
 ("", False),
 ("MAIN RESULT", True),
 ("Lens D1 covers 3 domains, 18 constructs and 5 stages: 90 indicators. Each indicator is one observable, positive behaviour with a source.", False),
 ("The 8 Multiple Intelligence constructs keep the 8 axes of the Pehchan spider chart. Domains 2 and 3 add two new charts (5 axes each).", False),
 ("", False),
 ("SHEETS", True),
 ("ConstructMap – the D1 table. Exact columns: Domain, Construct, Indicator, NEP stage, EBA tag, Source (one row for each indicator).", False),
 ("ConstructList – construct codes (for example MI_NAT) for the profile schema of AB and the Trajectory field 'top_strengths'.", False),
 ("Rubric_0_3 – behaviour anchors for scores 0–3, and the N/A rule.", False),
 ("Scoring – roll-up to 0–100, bands, and the two proposed formulas for URF (Option A and Option B).", False),
 ("Scoring_Example – live formulas on ILLUSTRATIVE numbers (not data) with a spider chart.", False),
 ("Shades_P1_P7 – 7-shade accessibility check: barriers and UDL adjustments for each official URF shade.", False),
 ("RPwD21_Coverage – each of the 21 specified disabilities of the RPwD Act 2016 and its shade.", False),
 ("Open_Questions_URF – the mapping and scope questions that URF must answer.", False),
 ("Sources – full references. Open each link and put Y in column E before you put the file in Final/.", False),
 ("SelfCheck – ground-rule check of this file.", False),
 ("Log_Entries – rows to paste into the Playbook decision log, risk log and handover tracker.", False),
 ("", False),
 ("INDICATOR TEMPLATE (agreed SRS + ANA)", True),
 ("[Action verb that you can see] + [what] + [context or example]. One behaviour. Positive words. Correct for the stage. No time limit.", False),
 ("Example: 'Sees that a classmate is sad, and helps or tells an adult.' (Social awareness, Preparatory)", False),
 ("ANY-MODE RULE: 'tells', 'names', 'explains' and 'asks' mean any mode: speech, Indian Sign Language, writing, typing, symbols, pointing or AAC.", False),
 ("Actions can be done with or without aids. Usual access aids are never counted as 'support' in the rubric.", False),
 ("", False),
 ("FALLBACK NOTE", True),
 ("URF has not yet shared the Pehchan 64-question bank or the scoring code. D1 uses the Playbook fallback: Gardner 8 MI, CASEL 5, original reasoning tasks, NEP 2020 stages, URF shades P1–P7.", False),
 ("When the bank arrives, map each Pehchan question to one MI indicator (new column 'Pehchan Q#' in Working only) and log the change.", False),
 ("", False),
 ("GOOGLE SHEETS: Drive > New > File upload > open with Google Sheets. Keep the name Lens_ConstructMap_v1. ANA and AB comment; SRS edits.", False),
]
for i, (t, b) in enumerate(lines, 1):
    c = ws.cell(row=i, column=1, value=t); c.alignment = Alignment(wrap_text=True)
    if b: c.font = Font(bold=True, color=PURPLE, size=12 if i == 1 else 11)
ws.column_dimensions["A"].width = 150

# ConstructMap
ws = wb.create_sheet("ConstructMap")
table(ws, HDR, d.construct_rows(True), [30, 26, 70, 20, 20, 60])
ws.auto_filter.ref = f"A1:F{len(d.construct_rows())+1}"
fills = {d.MI: "F5F0FB", d.ER: "EEF6FB", d.PR: "F2F8EE"}
for r in range(2, 92):
    for c in range(1, 7):
        ws.cell(row=r, column=c).fill = PatternFill("solid", fgColor=fills[ws.cell(row=r, column=1).value])

# ConstructList
ws = wb.create_sheet("ConstructList")
rows = [[c[0], c[1], c[2], c[4], c[3].replace("Construct: ", ""), 5, "Yes (Pehchan axis)" if c[0].startswith("MI") else "Yes (new chart)"] for c in d.CONSTRUCTS]
table(ws, ["construct_code", "Domain", "Construct", "Definition", "Source", "Indicators (1 per stage)", "Spider-chart axis"], rows, [14, 30, 26, 60, 60, 12, 18])

# Rubric
ws = wb.create_sheet("Rubric_0_3")
table(ws, ["Score", "Short name", "Behaviour anchor (observer)", "Notes and example (PR_SEQ, Foundational: puts 3 routine cards in order)"],
      [list(r) for r in d.RUBRIC] + [["N/A", "Not offered accessibly", "The item was not given in a format that the learner can access (see Shades_P1_P7).", "N/A is not a score. It is left out of every average. Record the reason."]],
      [8, 24, 70, 70])
r0 = 8
for i, t in enumerate([
  "Rules (from Playbook How-to, Scoring D2):",
  "1. Record the child self-report and the observer score next to each other. The profile uses the observer score.",
  "2. If observer and self-report differ by 2 points or more, write a note. Do not change either number.",
  "3. The child takes part in each item. The observer does not only watch.",
  "4. Score the behaviour, not the person. Report words: 'Naturalist strength area: strong'. Never 'the child is emerging'."], r0):
    ws.cell(row=i, column=1, value=t).font = Font(bold=(i == r0))

# Scoring
ws = wb.create_sheet("Scoring")
title(ws, "Scoring: roll-up, bands and two proposals for a new Pehchan formula (draft for URF discussion)")
rows = [
 ["B0 · Pehchan today", "Score(intelligence) = sum of 8 Likert answers", "Raw sum; scale points not yet seen [VERIFY in Pehchan code]", "Simple; already in the app", "Self-report only; no accessible formats; a missing answer silently lowers the sum; no stage reference; no evidence of item quality", "Baseline only"],
 ["D1 · Playbook roll-up (agreed)", "Score_c = (mean of observer item scores in construct c) / 3 × 100", "0–100. Round to integer, then band: 0–33 emerging, 34–66 developing, 67–100 strong", "Same bands for Trajectory and TwinWorks; easy in Sheets", "Treats all items the same; an N/A item must be excluded by hand", "Default for D1/D2 (bands fixed after D2)"],
 ["Option A · Stage-anchored percent-of-maximum (POMP) with N/A rule", "Score_c = 100 × Σ(w_i·x_i) / (3·Σ w_i), over items with x_i ≠ N/A. Report only if n_c ≥ 2 scored items; else 'not enough evidence'. Each learner is scored on the indicators of their own NEP stage.", "0–100 per construct; 8 MI values feed the existing 8-axis spider chart unchanged", "Transparent; an access barrier never becomes a low score; weights w_i (default 1) let URF give more weight to 'core' items; works in Sheets and NestJS with no pilot data", "Weights are a judgement until pilot data exists; scores are not comparable across stages (by design)", "RECOMMENDED for D2 (equal weights w_i = 1 until pilot)"],
 ["Option B · Multi-source, evidence-weighted score with confidence band", "S_c = Σ_s (r_s · S_c,s) / Σ_s r_s, for sources s ∈ {observer, task, self-report}; S_c,s = Option A score of that source; r_s = reliability of the source from the pilot (Cronbach's α). Band: S_c ± 1.96 · SEM, SEM = SD_c · √(1 − α_c).", "0–100 plus an uncertainty ring on the spider chart", "Uses all evidence (child voice counts); shows how sure we are; improves as data grows", "Needs pilot data for r_s, SD and α — until then use equal weights (assumption); changes the Playbook rule 'profile uses observer score' (needs a decision-log entry and URF approval)", "Propose to URF for v2 after pilot"],
 ["Later · Rasch partial-credit model", "P(x) from item difficulty and person location (logits), then rescale to 0–100", "Interval-scale scores; item-fit statistics", "Best measurement quality; finds poor items", "Needs a pilot sample and software; harder to explain; sample size per Linacre (1994) rule of thumb [VERIFY AT SOURCE]", "Mention in D5 refinement note only"],
 ["Display add-on (any option) · Signature strengths", "Rank the constructs within one learner; show the top 3 as 'signature strengths'", "Ranks 1–n", "Strengths framing; feeds Trajectory 'top_strengths'; no comparison between children", "Ties need a rule (use the higher observer score, then alphabetical)", "Use from D3"],
]
table(ws, ["Formula", "Calculation", "Output", "Pros", "Cons", "Use"], rows, [34, 70, 40, 45, 50, 26], start=3)

# Scoring example
ws = wb.create_sheet("Scoring_Example")
ws["A1"] = "ILLUSTRATIVE NUMBERS — NOT DATA. Persona EX-01 is invented to show the formulas. It is not a URF persona or a team persona."
ws["A1"].font = Font(bold=True, color="C00000")
ws["A2"] = "Parameters (ASSUMPTION until pilot):"; ws["A2"].font = Font(bold=True)
params = [("r_observer", 1), ("r_task", 1), ("r_self", 1), ("min_items", 2)]
for i, (k, v) in enumerate(params):
    ws.cell(row=2, column=3 + 2 * i, value=k); ws.cell(row=2, column=4 + 2 * i, value=v).fill = PatternFill("solid", fgColor="FFF2CC")
codes = [c[0] for c in d.CONSTRUCTS if c[0].startswith("MI")]
names = [c[2] for c in d.CONSTRUCTS if c[0].startswith("MI")]
obs = [(3, 2), (2, 2), (1, "NA"), (3, 3), (2, 1), (1, 2), (2, 2), (3, 3)]
slf = [(3, 3), (1, 2), (2, 2), (3, 3), (2, 2), (3, 3), (2, 3), (3, 2)]
tsk = [(3, 3), (2, 1), (2, 1), (3, 2), (1, 1), (1, 1), (2, 2), (3, 3)]
hdr = ["construct_code", "Item", "Observer (0–3/NA)", "Task (0–3/NA)", "Self-report (0–3)", "Weight w_i", "Flag |obs−self| ≥ 2"]
for j, h in enumerate(hdr, 1):
    c = ws.cell(row=4, column=j, value=h); c.font = hfont; c.fill = hfill; c.alignment = wrap
r = 5
for k, code in enumerate(codes):
    for it in range(2):
        ws.cell(row=r, column=1, value=code); ws.cell(row=r, column=2, value=f"{code}_M_{it+1:02d}")
        ws.cell(row=r, column=3, value=obs[k][it]); ws.cell(row=r, column=4, value=tsk[k][it]); ws.cell(row=r, column=5, value=slf[k][it])
        ws.cell(row=r, column=6, value=1)
        ws.cell(row=r, column=7, value=f'=IF(AND(ISNUMBER(C{r}),ISNUMBER(E{r})),IF(ABS(C{r}-E{r})>=2,"NOTE: write reason",""),"")')
        r += 1
last = r - 1
dv = DataValidation(type="list", formula1='"0,1,2,3,NA"', allow_blank=True); ws.add_data_validation(dv); dv.add(f"C5:E{last}")
s0 = last + 3
sh = ["construct_code", "Construct", "n scored (obs)", "D1 Playbook score", "Option A score", "Option A band", "Option B score", "Rank (Option A)", "Tie-break key"]
for j, h in enumerate(sh, 1):
    c = ws.cell(row=s0, column=j, value=h); c.font = hfont; c.fill = hfill; c.alignment = wrap
A = f"$A$5:$A${last}"; C = f"$C$5:$C${last}"; D = f"$D$5:$D${last}"; E = f"$E$5:$E${last}"; F = f"$F$5:$F${last}"
for k, code in enumerate(codes):
    rr = s0 + 1 + k
    ws.cell(row=rr, column=1, value=code); ws.cell(row=rr, column=2, value=names[k])
    ws.cell(row=rr, column=3, value=f'=COUNTIFS({A},A{rr},{C},">=0")')
    ws.cell(row=rr, column=4, value=f'=IF(C{rr}=0,"",ROUND(AVERAGEIFS({C},{A},A{rr})/3*100,0))')
    # Option A: weighted POMP over numeric observer items
    ws.cell(row=rr, column=5, value=f'=IF(C{rr}<$J$2,"not enough evidence",ROUND(100*SUMPRODUCT(--({A}=A{rr}),--ISNUMBER({C}),{F},IF(ISNUMBER({C}),{C},0))/(3*SUMPRODUCT(--({A}=A{rr}),--ISNUMBER({C}),{F})),0))')
    ws.cell(row=rr, column=6, value=f'=IF(ISNUMBER(E{rr}),IF(E{rr}<=33,"emerging",IF(E{rr}<=66,"developing","strong")),"")')
    def src(col):
        return f'IFERROR(AVERAGEIFS({col},{A},A{rr})/3*100,"")'
    ws.cell(row=rr, column=7, value=(f'=ROUND((IF(ISNUMBER({src(C)}),$D$2*{src(C)},0)+IF(ISNUMBER({src(D)}),$F$2*{src(D)},0)+IF(ISNUMBER({src(E)}),$H$2*{src(E)},0))'
                                     f'/(IF(ISNUMBER({src(C)}),$D$2,0)+IF(ISNUMBER({src(D)}),$F$2,0)+IF(ISNUMBER({src(E)}),$H$2,0)),0)'))
    ws.cell(row=rr, column=8, value=f'=IF(ISNUMBER(E{rr}),RANK(E{rr},$E${s0+1}:$E${s0+8}),"")')
    ws.cell(row=rr, column=9, value=f'=IF(ISNUMBER(E{rr}),E{rr}+G{rr}/1000-{k}/100000,-1)')
ws.cell(row=s0 + 10, column=1, value="Signature strengths (top 3, Option A):").font = Font(bold=True)
for t in range(3):
    ws.cell(row=s0 + 11 + t, column=1, value=t + 1)
    ws.cell(row=s0 + 11 + t, column=2, value=f'=IFERROR(INDEX($B${s0+1}:$B${s0+8},MATCH(LARGE($I${s0+1}:$I${s0+8},{t+1}),$I${s0+1}:$I${s0+8},0)),"")')
ws.cell(row=s0 + 15, column=1, value="Note: MI_SPA item 2 is N/A (picture item not offered in tactile format). Option A leaves it out, so n = 1 < min_items and the construct shows 'not enough evidence' instead of a low score. Ties in the top 3: higher Option B score first, then construct order (column I).")
for col, wd in zip("ABCDEFGH", [16, 22, 16, 14, 16, 14, 14, 12]):
    ws.column_dimensions[col].width = wd
ch = RadarChart(); ch.type = "marker"; ch.style = 26; ch.title = "EX-01 (illustrative) · 8 MI axes · Option A"
ch.add_data(Reference(ws, min_col=5, min_row=s0, max_row=s0 + 8), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=2, min_row=s0 + 1, max_row=s0 + 8)); ch.y_axis.delete = False; ch.height = 9; ch.width = 13
ws.add_chart(ch, "K4")

# Shades
ws = wb.create_sheet("Shades_P1_P7")
table(ws, ["Code", "Official URF shade", "Related RPwD Act 2016 conditions (Schedule item)", "Possible barrier in a Lens assessment", "UDL adjustments (Engage / Represent / Act-Express)", "Lens-specific rule"],
      [list(s) for s in d.SHADES], [7, 24, 45, 45, 70, 55])
n = len(d.SHADES) + 3
for i, t in enumerate([
  "Rules: A shade is a support category, not a label. Lens never assigns, infers or reports a shade. It reads the shade from the record only to select accessible formats.",
  "Multiple disabilities (item 5): give each shade that applies; mark the first as primary. Benchmark disability (s.2(r), 40%) is not measured or recorded by Lens.",
  "Each indicator needs 2 or more formats (ANA item format table, T2.4). Any reply mode is valid (see README any-mode rule)."], n):
    ws.cell(row=i, column=1, value=t)

ws = wb.create_sheet("RPwD21_Coverage")
table(ws, ["#", "Specified disability (RPwD Act 2016)", "Schedule item", "URF shade", "Mapping status"], [list(x) for x in d.RPWD21], [5, 48, 16, 36, 46])
ws.cell(row=24, column=1, value="Coverage: 21 of 21 specified disabilities have a shade. 15 are team mappings for URF to confirm; 6 are OPEN (Q1–Q3). Schedule item 6 (new categories) → nearest shade + decision-log entry.")

ws = wb.create_sheet("Open_Questions_URF")
table(ws, ["ID", "Topic", "Question for URF (Titus, Glenn)", "Team default until URF replies"], [list(q) for q in d.OPEN_QS], [6, 45, 70, 60])

ws = wb.create_sheet("Sources")
table(ws, ["ID", "Full reference", "Used for", "Where to check", "Opened & checked by SRS (Y/N)"], [list(s) + [""] for s in d.SOURCES], [6, 80, 45, 60, 16])

ws = wb.create_sheet("SelfCheck")
chk = [
 ["Synthetic data only; codes not names", "PASS", "No persona data in D1. Example sheet uses EX-01, marked illustrative."],
 ["Strengths framing; no label or diagnosis", "PASS", "All 90 indicators are positive behaviours. Bands describe a skill area, not a child. Shade names never sit next to scores."],
 ["Every indicator observable, one behaviour, stage-fit", "PASS – ANA to confirm", "One action verb per indicator; stage ladder F→PS for each construct."],
 ["Every construct has a real source", "PASS – SRS to open links", "S01–S12. Mark Y in Sources!E before Final/."],
 ["No fabricated numbers", "PASS", "Only numbers: stage ages (NEP 2020), 21 conditions (RPwD Act), 64 questions (URF, 20 Nov). Example numbers labelled illustrative. Rasch sample size marked [VERIFY AT SOURCE]."],
 ["Original items only", "PASS", "Reasoning tasks written by Team 10; no Raven, WISC or other test content."],
 ["Plain English (STE); no 'leverage/robust/seamless/delve'", "PASS", "Checked by text search."],
 ["Schema exact", "PASS", "ConstructMap columns: Domain, Construct, Indicator, NEP stage, EBA tag, Source."],
 ["Manual checks before Final/", "TO DO", "(1) ANA 15-min review; (2) open each source link; (3) URF answers Q1–Q7 or log team default; (4) reconcile with Pehchan 64 Q when shared."],
]
table(ws, ["Check", "Result", "Evidence / action"], chk, [50, 22, 100])

ws = wb.create_sheet("Log_Entries")
logs = [
 ["Decision log", "23 Nov", "Lens D1 uses the fallback base (Gardner 8 MI, CASEL 5, original reasoning tasks, NEP 2020 stages, URF P1–P7) because URF has not yet shared the Pehchan 64-question bank", "SRS", "Playbook fallback; reconcile when the bank arrives"],
 ["Decision log", "23 Nov", "Indicator template agreed: [visible action] + [what] + [context]; any-mode rule; aids are not 'support'", "SRS, ANA", "Accessible to all 7 shades; one template for D2 items"],
 ["Decision log", "23 Nov", "Team defaults for open shade mappings: 4(a) and 4(b) → P7 for adjustments; ASD → P4; item 5 → multi-shade with primary", "SRS", "Pending URF answers Q1–Q4"],
 ["Decision log", "23 Nov", "N/A rule: an item not offered in an accessible format is N/A, not 0, and is left out of averages", "SRS", "An access barrier must not lower a strengths score"],
 ["Risk log", "23 Nov", "Pehchan 64 Q and scoring code not received; D1 may need re-mapping", "SRS", "Use fallback; map each Pehchan Q to an MI indicator in Working when received · Open"],
 ["Risk log", "23 Nov", "URF does not answer shade questions Q1–Q7 before D2 (4 Dec)", "SRS, SC", "Use the team defaults; record them; ask again at the joint check-in · Open"],
 ["Handover tracker", "Fri 27 Nov", "Lens D1 construct map (Lens_ConstructMap_v1_FINAL)", "Lens (SRS) → URF; copy to AB/ANA", "Ready for review → Final after ANA sign-off"],
 ["Handover tracker", "Thu 26 Nov", "Construct codes (ConstructList) for profile schema", "Lens (SRS) → Lens (AB), Trajectory (SM)", "Sent with v1"],
]
table(ws, ["Log", "Date", "Entry", "Who", "Reason / action / status"], logs, [18, 12, 90, 30, 55])

wb.save(f"{OUT}/1 Lens/Working/Lens_ConstructMap_v1.xlsx")
print("saved")
