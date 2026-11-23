"""Builds Nike_Running_Data_Workbook.xlsx."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import ScatterChart, BarChart, Reference, Series
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from refs import REFS, ordered_keys
import viva_data as V

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HF = PatternFill("solid", fgColor="1A1A1A"); HFont = Font(bold=True, color="FFFFFF", name="Calibri")
INP = PatternFill("solid", fgColor="FFF4CC"); THIN = Side(style="thin", color="D0D0D0")
B = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
wb = Workbook()


def sheet(name, title, note, headers, rows, widths, first=False):
    ws = wb.active if first else wb.create_sheet(name)
    ws.title = name
    ws["A1"] = title; ws["A1"].font = Font(bold=True, size=14, color="E4572E")
    ws["A2"] = note; ws["A2"].font = Font(italic=True, color="6B6B6B")
    for i, h in enumerate(headers, 1):
        c = ws.cell(row=4, column=i, value=h); c.fill = HF; c.font = HFont; c.alignment = Alignment(wrap_text=True, vertical="center"); c.border = B
    for r, row in enumerate(rows, 5):
        for i, v in enumerate(row, 1):
            c = ws.cell(row=r, column=i, value=v); c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = B
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = "A5"
    return ws


# README
ws = sheet("README", "Nike Running Footwear: Data Workbook", "Supports the report, slides and viva. Yellow cells are inputs.",
           ["Sheet", "What it contains", "What you need to do"], [
    ["Source_Log", f"All {len(REFS)} references with URL, type and reliability grade", "Open each link once and tick 'Checked'"],
    ["Price_Comparison", "India MRPs of comparable running shoes (Nov 2026)", "Update prices on a store visit; add Puma/Skechers if found"],
    ["India_Revenue", "Latest reported India revenue of major players", "None (cite sources as given)"],
    ["Perceptual_Map", "Respondent rating input -> averages -> chart", "Enter each respondent's rating card scores"],
    ["Google_Trends", "Template for brand search interest (India, 12 months)", "Download from trends.google.com and paste"],
    ["Interview_Coding", "Quote -> code -> category -> theme -> hypothesis; counts per theme", "Code each transcript line"],
    ["Hypotheses", "H1-H6 with outcome column", "Mark outcomes after coding"],
    ["KPI_Tracker", "Marketing-plan KPIs with targets", "Planning reference for viva"],
], [20, 60, 55], first=True)

# Source log
rows = []
for k in ordered_keys():
    lab, full, url, typ, rel = REFS[k]
    rows.append([lab, full, url, typ, rel, ""])
ws = sheet("Source_Log", "Source log", "Every reference used in the report. Pages were found through search; open each link to confirm before submission.",
           ["Citation", "Full reference (APA 7)", "URL", "Source type", "Reliability", "Checked (Y/N)"], rows, [22, 70, 50, 18, 18, 12])
for r in range(5, 5 + len(rows)):
    ws.cell(row=r, column=3).hyperlink = ws.cell(row=r, column=3).value
    ws.cell(row=r, column=3).font = Font(color="1F4E79", underline="single")
    ws.cell(row=r, column=6).fill = INP

# Price comparison
prices = [
    ["Nike", "Vegam Run", "Entry", 3795, "Open Magazine (2026a)", "Reported launch price"],
    ["Nike", "Pegasus 41", "Core (previous)", 11895, "Nike India (n.d.-c)", "MRP"],
    ["Nike", "Pegasus 42", "Core daily", 12995, "Nike India (n.d.-b)", "MRP"],
    ["Nike", "Vomero 18", "Max cushion", 13295, "Nike India (n.d.-d)", "MRP; some colourways Rs 14,195-14,995"],
    ["Nike", "Pegasus Premium", "Premium", 19295, "Nike India (n.d.-e)", "MRP"],
    ["ASICS", "Novablast 5", "Core daily", 12000, "Fat Marathoner (2026c); Amazon trackers", "Approx. Amazon selling price"],
    ["ASICS", "Gel-Cumulus 28", "Core daily", 12999, "Fat Marathoner (2026b)", "Reported"],
    ["ASICS", "Novablast 6", "Core daily", 15999, "Fat Marathoner (2026c)", "Reported list price"],
    ["adidas", "Adizero EVO SL", "Performance trainer", 15999, "adidas India (n.d.)", "MRP"],
    ["Decathlon", "Jogflow 150 Breathe", "Entry", 1999, "Decathlon India (n.d.-b)", "Selling price (MRP 2,599)"],
    ["Decathlon", "Kiprun Kipcore", "Entry daily", 4999, "Decathlon India (n.d.-a)", "Selling price (MRP 6,499)"],
    ["Decathlon", "Kiprun Kipride", "Core daily", 9999, "Decathlon India (n.d.-c)", "Selling price (MRP 13,999)"],
    ["Decathlon", "Kiprun Kipstorm Elite", "Race", 19999, "Fat Marathoner (2026b)", "Reported"],
]
ws = sheet("Price_Comparison", "Running-shoe price comparison, India", "Indicative, November 2026. GST: 5% up to Rs 2,500, 18% above (PIB, 2025).",
           ["Brand", "Model", "Tier", "Price (Rs)", "Source", "Note", "GST slab", "Price vs Pegasus 42"], [p + ["", ""] for p in prices], [12, 22, 18, 12, 34, 34, 10, 16])
for r in range(5, 5 + len(prices)):
    ws.cell(row=r, column=4).number_format = "#,##0"
    ws.cell(row=r, column=7, value=f'=IF(D{r}<=2500,"5%","18%")')
    ws.cell(row=r, column=8, value=f"=D{r}/$D$7-1").number_format = "0%"
ch = BarChart(); ch.type = "bar"; ch.title = "India price (Rs)"; ch.height = 9; ch.width = 18
ch.add_data(Reference(ws, min_col=4, min_row=4, max_row=4 + len(prices)), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=2, min_row=5, max_row=4 + len(prices))); ch.legend = None
ws.add_chart(ch, "J4")

# India revenue
sheet("India_Revenue", "India revenue of major sportswear players", "All categories, latest reported; years differ slightly.",
      ["Company", "Revenue (Rs crore)", "Period", "Source"], [
    ["Decathlon Sports India", 4478, "FY26 (operating)", "Open Magazine (2026b)"], ["Decathlon Sports India", 4133, "FY25", "Entrackr (2025)"],
    ["adidas India Marketing", 3259, "FY25", "Open Magazine (2026b)"], ["Puma India", 3200, "2026", "Open Magazine (2026b)"],
    ["Skechers South Asia", 1971, "Latest", "Open Magazine (2026b)"], ["Nike India", 1380, "FY25 (+14%)", "Financial Express (2026)"],
    ["ASICS India", 430, "2025 estimate", "Financial Express (2025)"]], [26, 18, 18, 30])

# Perceptual map
ws = wb.create_sheet("Perceptual_Map")
ws["A1"] = "Perceptual map from respondent ratings"; ws["A1"].font = Font(bold=True, size=14, color="E4572E")
ws["A2"] = "Enter each respondent's 1-10 ratings (yellow). Averages and the chart update automatically. Until ratings exist, the 'Provisional' column is used in the report."
ws["A2"].font = Font(italic=True, color="6B6B6B")
brands = V.RATING_BRANDS
attrs = ["Credibility", "Price level"]
hdr = ["Respondent", "Attribute"] + brands
for i, h in enumerate(hdr, 1):
    c = ws.cell(row=4, column=i, value=h); c.fill = HF; c.font = HFont
r = 5
for sid in [s[0] for s in V.SETS]:
    for a in attrs:
        ws.cell(row=r, column=1, value=sid); ws.cell(row=r, column=2, value=a)
        for j in range(len(brands)):
            ws.cell(row=r, column=3 + j).fill = INP
        r += 1
last = r - 1
ws.cell(row=r + 1, column=1, value="Summary").font = Font(bold=True)
sh = ["Brand", "Avg credibility", "Avg price level", "Provisional credibility", "Core MRP (Rs)", "Plot credibility"]
for i, h in enumerate(sh, 1):
    c = ws.cell(row=r + 2, column=i, value=h); c.fill = HF; c.font = HFont
prov = {"Nike": (8.4, 12995), "ASICS": (8.8, 12999), "adidas": (7.8, 15999), "Puma": (6.2, 9000), "Skechers": (4.8, 7000), "Decathlon (Kiprun)": (6.6, 4999)}
s0 = r + 3
for j, b in enumerate(brands):
    rr = s0 + j; col = get_column_letter(3 + j)
    ws.cell(row=rr, column=1, value=b)
    ws.cell(row=rr, column=2, value=f'=IFERROR(AVERAGEIFS({col}5:{col}{last},$B$5:$B${last},"Credibility"),"")')
    ws.cell(row=rr, column=3, value=f'=IFERROR(AVERAGEIFS({col}5:{col}{last},$B$5:$B${last},"Price level"),"")')
    ws.cell(row=rr, column=4, value=prov[b][0]); ws.cell(row=rr, column=5, value=prov[b][1])
    ws.cell(row=rr, column=6, value=f'=IF(B{rr}="",D{rr},B{rr})')
sc = ScatterChart(); sc.title = "Price vs perceived running credibility"; sc.style = 13; sc.height = 10; sc.width = 18
sc.x_axis.title = "Core MRP (Rs)"; sc.y_axis.title = "Credibility (1-10)"
for j, b in enumerate(brands):
    rr = s0 + j
    ser = Series(Reference(ws, min_col=6, min_row=rr), Reference(ws, min_col=5, min_row=rr), title=b)
    ser.marker.symbol = "circle"; ser.marker.size = 10; ser.graphicalProperties.line.noFill = True
    sc.series.append(ser)
ws.add_chart(sc, "J4")
for i, w in enumerate([12, 16, 12, 12, 12, 12, 12, 14], 1):
    ws.column_dimensions[get_column_letter(i)].width = w

# Google trends
ws = sheet("Google_Trends", "Google Trends: brand search interest in India",
           "Go to trends.google.com, region India, past 12 months, compare: Nike running shoes, ASICS, Adidas running shoes, Decathlon running shoes, Skechers. Download CSV and paste below.",
           ["Week", "Nike running shoes", "ASICS", "adidas running shoes", "Decathlon running shoes", "Skechers"], [[""] * 6 for _ in range(52)], [14, 18, 12, 20, 22, 12])
for r in range(5, 57):
    for c in range(1, 7):
        ws.cell(row=r, column=c).fill = INP
ws.cell(row=58, column=1, value="Average").font = Font(bold=True)
for c in range(2, 7):
    L = get_column_letter(c)
    ws.cell(row=58, column=c, value=f'=IFERROR(AVERAGE({L}5:{L}56),"")')

# Interview coding
themes = ["Brand awareness and associations", "Purchase motivation / benefits sought", "Price sensitivity",
          "Competition and switching", "Influence", "Channel and trust", "Unmet needs"]
ws = sheet("Interview_Coding", "Interview coding sheet", "One row per meaningful quote. Use the dropdowns for theme and hypothesis.",
           ["Respondent", "Exact quote", "First-level code", "Category", "Broader theme", "Hypothesis", "Supports / contradicts"],
           [[""] * 7 for _ in range(120)], [12, 60, 26, 20, 32, 12, 18])
dv = DataValidation(type="list", formula1='"' + ",".join(themes) + '"', allow_blank=True); ws.add_data_validation(dv); dv.add("E5:E124")
dv2 = DataValidation(type="list", formula1='"' + ",".join(h[0] for h in V.HYPOTHESES) + ',None"', allow_blank=True); ws.add_data_validation(dv2); dv2.add("F5:F124")
dv3 = DataValidation(type="list", formula1='"Supports,Contradicts,Mixed"', allow_blank=True); ws.add_data_validation(dv3); dv3.add("G5:G124")
ws["I4"] = "Theme"; ws["J4"] = "Quotes"; ws["K4"] = "Respondents mentioning"
for c in ("I4", "J4", "K4"):
    ws[c].fill = HF; ws[c].font = HFont
for i, t in enumerate(themes, 5):
    ws.cell(row=i, column=9, value=t)
    ws.cell(row=i, column=10, value=f'=COUNTIF($E$5:$E$124,I{i})')
    ws.cell(row=i, column=11, value=f'=SUMPRODUCT(($E$5:$E$124=I{i})/COUNTIFS($A$5:$A$124,$A$5:$A$124&"",$E$5:$E$124,$E$5:$E$124&""))')
ws.column_dimensions["I"].width = 34; ws.column_dimensions["K"].width = 22

# Hypotheses
ws = sheet("Hypotheses", "Working hypotheses", "Mark the outcome after coding the interviews.",
           ["Code", "Hypothesis", "Supporting quotes", "Contradicting quotes", "Outcome"],
           [[h[0], h[1], f'=COUNTIFS(Interview_Coding!$F$5:$F$124,A{i},Interview_Coding!$G$5:$G$124,"Supports")',
             f'=COUNTIFS(Interview_Coding!$F$5:$F$124,A{i},Interview_Coding!$G$5:$G$124,"Contradicts")', ""] for i, h in enumerate(V.HYPOTHESES, 5)],
           [8, 70, 18, 20, 22])

# KPI tracker
sheet("KPI_Tracker", "Proposed marketing plan KPIs (author's proposal; targets are assumptions)", "Budget total Rs 45 crore (assumed).",
      ["Initiative", "Objective", "KPI", "Target", "Budget (Rs cr)", "Timeline", "Actual", "Status"], [
    ["First 5K with Vegam", "O1, O2", "5K plan sign-ups / finishers", "150,000 / 50,000", 9.0, "Jan-Apr 2027", "", ""],
    ["NRC City Crews", "O2, O3", "Active crew members", "10 cities live", 6.0, "Feb-Nov 2027", "", ""],
    ["Fit Lab", "O3, O4", "Fit-lab conversion rate", "35%", 5.5, "Mar-Aug 2027", "", ""],
    ["Trade-Up credit", "O4", "Vegam-to-Pegasus/Vomero trade-up", "15%", 4.0, "Jun-Nov 2027", "", ""],
    ["Genuine Swoosh", "O5", "Authenticated marketplace listings", "90%", 3.0, "Jan-Jun 2027", "", ""],
    ["Ambassador + After Dark", "O3", "Women participants; earned media", "6,000 women", 9.5, "Apr-Dec 2027", "", ""],
    ["Marathon-season burst", "O1, O3", "Consideration lift", "+10 points", 8.0, "Nov 2027-Jan 2028", "", ""],
    ["TOTAL", "", "", "", "=SUM(E5:E11)", "", "", ""]], [26, 10, 34, 18, 14, 18, 10, 10])

out = os.path.join(ROOT, "Nike_Running_Data_Workbook.xlsx")
wb.save(out)
print("saved", out)
