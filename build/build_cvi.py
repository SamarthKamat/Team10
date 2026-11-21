"""Builds Lens_ContentValidity_RatingSheet_v1.xlsx (SRS). Run: python3 build_cvi.py <GiveGoa dir>"""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
OUT = sys.argv[1] + "/1 Lens/Working/Lens_ContentValidity_RatingSheet_v1.xlsx"
P = PatternFill("solid", fgColor="5B2C83"); W = Font(bold=True, color="FFFFFF"); B = Font(bold=True)
wrap = Alignment(wrap_text=True, vertical="top")
wb = Workbook(); ws = wb.active; ws.title = "README"
for i, t in enumerate([
    "Lens D2 · Content validity rating sheet · v1 · Owner SRS · Items from ANA's item log",
    "Each rater scores each item for relevance to its indicator: 1 = not relevant, 2 = somewhat, 3 = quite, 4 = highly relevant.",
    "I-CVI = raters giving 3 or 4 / raters who rated. Pass: 3–5 raters → I-CVI = 1.00; 6+ raters → I-CVI ≥ 0.78 (Lynn, 1986; Polit, Beck & Owen, 2007).",
    "S-CVI/Ave = mean of I-CVI over all items. Pass ≥ 0.90 (Polit & Beck, 2006).",
    "Raters: SRS, ANA, AB, URF mentor, and a special educator if URF arranges one. Rate alone; do not discuss scores first.",
    "Rows 5–6 in Ratings are EXAMPLE rows (illustrative). Delete them before rating. Paste item IDs and text from the item log.",
    "Tab Scoring_Formula_Test checks the D2 construct-score formula on the illustrative EX-01 example (same results as Lens_ScoringEngine_v1.py).",
], 1):
    ws.cell(row=i, column=1, value=t).font = B if i == 1 else Font()
ws.column_dimensions["A"].width = 140

ws = wb.create_sheet("Ratings")
hdr = ["Item ID", "Construct code", "NEP stage", "Indicator", "Item text (from ANA)", "Formats",
       "Rater 1 SRS", "Rater 2 ANA", "Rater 3 AB", "Rater 4 URF mentor", "Rater 5 (optional)", "Rater 6 (optional)",
       "Raters", "Agree (3–4)", "I-CVI", "Pass rule", "Decision", "Comment / revision"]
ws.append(["Lens D2 · Content validity ratings (1–4 relevance)"]); ws["A1"].font = B
ws.append([]); ws.append([])
ws.append(hdr)
for c in ws[4]:
    c.fill = P; c.font = W; c.alignment = wrap
ex = [["NAT-P-1", "MI_NAT", "Preparatory", "(from D1)", "EXAMPLE ROW: delete before rating", "Picture choice; hands-on", 4, 4, 3, 4, None, None],
      ["NAT-P-2", "MI_NAT", "Preparatory", "(from D1)", "EXAMPLE ROW: delete before rating", "Audio; observer checklist", 4, 2, 3, 4, None, None]]
LAST = 300
for r in range(5, LAST + 1):
    row = ex[r - 5] if r - 5 < len(ex) else [None] * 12
    for j, v in enumerate(row, 1):
        ws.cell(row=r, column=j, value=v)
    ws.cell(row=r, column=13, value=f'=IF(A{r}="","",COUNT(G{r}:L{r}))')
    ws.cell(row=r, column=14, value=f'=IF(A{r}="","",COUNTIF(G{r}:L{r},">=3"))')
    ws.cell(row=r, column=15, value=f'=IF(OR(A{r}="",M{r}=0),"",ROUND(N{r}/M{r},2))')
    ws.cell(row=r, column=16, value=f'=IF(O{r}="","",IF(M{r}<=5,1,0.78))')
    ws.cell(row=r, column=17, value=f'=IF(O{r}="","",IF(M{r}<3,"need 3+ raters",IF(O{r}>=P{r},"keep","revise")))')
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="4", allow_blank=True)
dv.error = "Enter 1, 2, 3 or 4"; ws.add_data_validation(dv); dv.add(f"G5:L{LAST}")
ws.conditional_formatting.add(f"Q5:Q{LAST}", CellIsRule(operator="equal", formula=['"revise"'], fill=PatternFill("solid", fgColor="F8D7DA")))
ws.conditional_formatting.add(f"Q5:Q{LAST}", CellIsRule(operator="equal", formula=['"keep"'], fill=PatternFill("solid", fgColor="D4EDDA")))
ws["A2"] = "S-CVI/Ave (mean I-CVI):"; ws["A2"].font = B
ws["D2"] = f'=IFERROR(ROUND(AVERAGE(O5:O{LAST}),2),"")'
ws["E2"] = f'=IF(D2="","",IF(D2>=0.9,"scale passes (≥ 0.90)","scale below 0.90: revise items marked revise"))'
ws["F2"] = "Items to revise:"; ws["G2"] = f'=COUNTIF(Q5:Q{LAST},"revise")'
for col, w in zip("ABCDEFGHIJKLMNOPQR", [10, 11, 12, 40, 45, 26, 9, 9, 9, 11, 10, 10, 8, 9, 8, 9, 14, 40]):
    ws.column_dimensions[col].width = w
ws.freeze_panes = "G5"

ws = wb.create_sheet("Scoring_Formula_Test")
ws.append(["D2 construct-score formula test · EX-01 is invented (illustrative), not data"]); ws["A1"].font = B
ws.append(["Construct", "Item", "Score (0–3 or NA)", "Weight", "Construct score", "Band", "Engine result"])
for c in ws[2]:
    c.fill = P; c.font = W
blocks = [("MI_NAT", [("NAT-P-1", 3), ("NAT-P-2", 3), ("NAT-P-3", 2)], "89 strong"),
          ("MI_LIN", [("LIN-P-1", 1), ("LIN-P-2", 1), ("LIN-P-3", "NA")], "33 emerging"),
          ("MI_SPA", [("SPA-P-1", 2), ("SPA-P-2", 1)], "50 developing"),
          ("MI_MUS", [("MUS-P-1", 3), ("MUS-P-2", "NA")], "not enough evidence")]
r = 3
for code, items, eng in blocks:
    a = r
    for iid, s in items:
        ws.append([code, iid, s, 1]); r += 1
    b = r - 1
    ws.cell(row=a, column=5, value=f'=IF(COUNT(C{a}:C{b})<2,"not enough evidence",ROUND(100*SUMPRODUCT(ISNUMBER(C{a}:C{b})*IFERROR(C{a}:C{b}*1,0)*D{a}:D{b})/(3*SUMPRODUCT(ISNUMBER(C{a}:C{b})*D{a}:D{b})),0))')
    ws.cell(row=a, column=6, value=f'=IF(ISNUMBER(E{a}),IF(E{a}<=33,"emerging",IF(E{a}<=66,"developing","strong")),"not enough evidence")')
    ws.cell(row=a, column=7, value=eng)
for col, w in zip("ABCDEFG", [12, 10, 16, 8, 20, 20, 22]):
    ws.column_dimensions[col].width = w
wb.save(OUT); print("saved", OUT)
