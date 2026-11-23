"""Builds Nike_Running_Presentation.pptx (22 slides, 16:9, with speaker notes)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import viva_data as V

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
PH = os.path.join(ROOT, "photos")
INK = RGBColor(0x1A, 0x1A, 0x1A); ACC = RGBColor(0xE4, 0x57, 0x2E); GREY = RGBColor(0x6B, 0x6B, 0x6B)
PALE = RGBColor(0xF2, 0xF2, 0xF2); WHITE = RGBColor(255, 255, 255); BLUE = RGBColor(0x2F, 0x5D, 0x7C)
FONT = "Calibri"

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
BLANK = prs.slide_layouts[6]
N = [0]


def rect(s, x, y, w, h, fill, line=False):
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    r.fill.solid(); r.fill.fore_color.rgb = fill
    if not line:
        r.line.fill.background()
    r.shadow.inherit = False
    return r


def text(s, x, y, w, h, t, size=16, bold=False, color=INK, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    lines = t if isinstance(t, list) else [t]
    for i, ln in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = ln; r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = FONT
    return tb


def bullets(s, x, y, w, h, items, size=16, color=INK, gap=8):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = True
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(gap)
        head, _, rest = it.partition("|")
        r = p.add_run(); r.text = "■  "; r.font.size = Pt(size - 6); r.font.color.rgb = ACC; r.font.name = FONT
        if rest:
            r = p.add_run(); r.text = head; r.font.bold = True; r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = FONT
            r = p.add_run(); r.text = " " + rest; r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = FONT
        else:
            r = p.add_run(); r.text = head; r.font.size = Pt(size); r.font.color.rgb = color; r.font.name = FONT
    return tb


def slide(title, kicker, notes):
    N[0] += 1
    s = prs.slides.add_slide(BLANK)
    rect(s, 0, 0, Inches(0.18), prs.slide_height, ACC)
    text(s, Inches(0.6), Inches(0.35), Inches(11), Inches(0.35), kicker.upper(), 11, True, ACC)
    text(s, Inches(0.6), Inches(0.65), Inches(12), Inches(0.8), title, 28, True, INK)
    text(s, Inches(0.6), Inches(7.0), Inches(9), Inches(0.3), "Nike Running Footwear | Marketing Management | GIM 2026-27", 9, False, GREY)
    text(s, Inches(12.0), Inches(7.0), Inches(0.8), Inches(0.3), str(N[0]), 9, True, GREY, PP_ALIGN.RIGHT)
    s.notes_slide.notes_text_frame.text = notes
    return s


def table(s, x, y, w, headers, rows, size=11, col_w=None, row_h=0.36):
    t = s.shapes.add_table(len(rows) + 1, len(headers), x, y, w, Inches(row_h * (len(rows) + 1))).table
    if col_w:
        tot = sum(col_w)
        for i, cw in enumerate(col_w):
            t.columns[i].width = Emu(int(w * cw / tot))
    for r in range(len(rows) + 1):
        for c in range(len(headers)):
            cell = t.cell(r, c)
            v = headers[c] if r == 0 else rows[r - 1][c]
            cell.text = str(v)
            cell.margin_left = cell.margin_right = Inches(0.06); cell.margin_top = cell.margin_bottom = Inches(0.03)
            for p in cell.text_frame.paragraphs:
                for rr in p.runs:
                    rr.font.size = Pt(size); rr.font.name = FONT
                    rr.font.bold = r == 0
                    rr.font.color.rgb = WHITE if r == 0 else INK
            cell.fill.solid(); cell.fill.fore_color.rgb = INK if r == 0 else (PALE if r % 2 == 0 else WHITE)
    return t


def img(s, name, x, y, w=None, h=None, folder=CH):
    p = os.path.join(folder, name)
    return s.shapes.add_picture(p, x, y, width=w, height=h)


def stat(s, x, y, big, small, w=Inches(2.9)):
    rect(s, x, y, w, Inches(1.35), PALE)
    text(s, x, y + Inches(0.12), w, Inches(0.6), big, 28, True, ACC, PP_ALIGN.CENTER)
    text(s, x + Inches(0.1), y + Inches(0.78), w - Inches(0.2), Inches(0.5), small, 11, False, GREY, PP_ALIGN.CENTER)


# 1 Title
N[0] += 1
s = prs.slides.add_slide(BLANK)
rect(s, 0, 0, prs.slide_width, prs.slide_height, INK)
rect(s, 0, Inches(6.6), prs.slide_width, Inches(0.9), ACC)
text(s, Inches(0.8), Inches(0.8), Inches(11), Inches(0.4), "GOA INSTITUTE OF MANAGEMENT  |  PGDM - BIG DATA ANALYTICS  |  MARKETING MANAGEMENT", 12, True, RGBColor(0xBF, 0xBF, 0xBF))
text(s, Inches(0.8), Inches(2.0), Inches(11), Inches(1.3), "NIKE", 80, True, WHITE)
text(s, Inches(0.8), Inches(3.3), Inches(11), Inches(0.8), "RUNNING FOOTWEAR IN INDIA", 36, True, ACC)
text(s, Inches(0.8), Inches(4.3), Inches(11), Inches(0.8), "A marketing management analysis: from global running leader to India's first-choice running brand?", 18, False, RGBColor(0xE0, 0xE0, 0xE0))
text(s, Inches(0.8), Inches(6.78), Inches(12), Inches(0.5), "[Student name]  |  [Roll number]  |  Prof. Shantanu Prasad  |  29 November 2026", 14, True, WHITE)
s.notes_slide.notes_text_frame.text = "Good morning. My assignment is on Nike's running footwear in India. I focus on the Pegasus, Nike's everyday running shoe, and the new Vegam Run, Nike's first shoe designed for India."

# 2 Company
s = slide("NIKE, Inc.: a running company at heart", "Company introduction",
          "Nike started in 1964 as Blue Ribbon Sports, a running-shoe business. FY26 revenue was 46.4 billion dollars, flat. Running is its best category, with five straight quarters of double-digit growth. In India it has been through a long reset: licence with Sierra, then a subsidiary, then cutting partners, and now Nykaa and Vegam.")
stat(s, Inches(0.6), Inches(1.7), "$46.4 bn", "FY26 revenue, flat (Nike, 2026b)")
stat(s, Inches(3.7), Inches(1.7), "5 quarters", "of double-digit Running growth (Nike, 2026c)")
stat(s, Inches(6.8), Inches(1.7), "Rs 1,380 cr", "Nike India FY25 sales, +14% (Financial Express, 2026)")
stat(s, Inches(9.9), Inches(1.7), "~150", "retail partners, down from ~350 (Inside Retail)")
img(s, "timeline.png", Inches(0.9), Inches(3.4), w=Inches(11.5))

# 3 Product
s = slide("The product: Nike's running ladder in India", "Product introduction",
          "Running shoes are shopping goods: people compare fit, cushioning and price. Nike has a clear ladder. Pegasus is the core product I analyse in depth. Vegam Run, at a reported 3,795 rupees, is the new entry point.")
table(s, Inches(0.6), Inches(1.7), Inches(7.6), ["Tier", "Model", "India MRP (Rs)"], [
    ["Entry / India-built", "Vegam Run", "3,795 (reported)"], ["Core daily", "Pegasus 42", "12,995"],
    ["Max cushion", "Vomero 18", "13,295-14,995"], ["Premium", "Pegasus Premium", "19,295"],
    ["Race", "Alphafly 4, Vaporfly, Swooshfly", "Not verified"]], size=13, col_w=[2.2, 3, 2], row_h=0.5)
if os.path.exists(os.path.join(PH, "nike_cover.jpg")):
    img(s, "nike_cover.jpg", Inches(8.6), Inches(1.7), h=Inches(4.6), folder=PH)
else:
    rect(s, Inches(8.6), Inches(1.7), Inches(4.2), Inches(4.6), PALE)
    text(s, Inches(8.8), Inches(3.6), Inches(3.8), Inches(1), "[Add your own photo of a Pegasus or Vegam Run]", 14, False, GREY, PP_ALIGN.CENTER)
text(s, Inches(0.6), Inches(5.0), Inches(7.6), Inches(1.4), "Shopping good for most buyers; specialty good for serious runners. Source: Nike India product pages; Open Magazine (2026a).", 12, False, GREY)

# 4 Industry
s = slide("Industry: a two-tier market in a running boom", "Industry overview",
          "Running shoes are about 31.8 percent of athletic footwear (IMARC). The market is two-tier: premium brands above 6,000 rupees and a value tier below 3,000, where most volume is. Nike is smaller than adidas, Puma and Skechers in India. No audited market size exists, so I use revenues as a proxy.")
img(s, "brand_revenue.png", Inches(0.6), Inches(1.6), w=Inches(7.4))
bullets(s, Inches(8.4), Inches(1.7), Inches(4.5), Inches(4.8), [
    "Running shoes|~31.8% of athletic footwear (IMARC, 2026)",
    "Two tiers|premium Rs 6,000-20,000 vs value below Rs 3,000",
    "Growth|running ~19-20% a year (ASICS estimate)",
    "No audited market size|revenue used as proxy, no share estimated"], size=15)

# 5 Recent developments
s = slide("Recent developments, 2024-2026", "Recent happenings",
          "These are the developments that matter most. The biggest are Nykaa taking over nike.com in February 2026 and the Vegam Run launch on 1 November 2026. The GST change makes shoes below 2,500 rupees much cheaper relative to Nike.")
table(s, Inches(0.6), Inches(1.6), Inches(12.1), ["Date", "Development", "Why it matters"], [
    ["May 2025", "After Dark Tour Mumbai 10K: 3,000+ women", "Community-led brand building"],
    ["Sep 2025", "\"Why Do It?\" relaunches \"Just Do It\"", "Message fits new runners"],
    ["22 Sep 2025", "GST 5% up to Rs 2,500; 18% above", "Value brands gain a price edge"],
    ["Feb 2026", "nike.com India run by Nykaa", "Asset-light e-commerce"],
    ["Apr 2026", "Pegasus 42 in India at Rs 12,995", "Core price rises"],
    ["1 Oct 2026", "Q1 FY27: Running up double digits, Vomero leads", "Global running momentum"],
    ["1 Nov 2026", "Vegam Run launches at ~Rs 3,795 on Flipkart", "Biggest pricing and channel shift in a decade"]],
    size=13, col_w=[1.3, 5, 4], row_h=0.58)

# 6 PESTEL
s = slide("PESTEL: the context for Nike Running", "PESTEL analysis",
          "Key points: GST puts nearly all Nike running shoes in the 18 percent slab; the running boom is the social driver; the BIS Quality Control Order deadline is July 2027; and counterfeits are a legal and trust issue.")
items = [("P", "Political", "Fit India, Khelo India; Make in India"), ("E", "Economic", "GST 5% vs 18% at Rs 2,500; price sensitivity"),
         ("S", "Social", "Running boom; more women runners; athleisure"), ("T", "Technological", "Super-shoe foams; running apps; quick commerce"),
         ("E", "Environmental", "Heat, monsoon, poor roads; sustainability"), ("L", "Legal", "BIS footwear QCO (Jul 2027); anti-counterfeit cases")]
for i, (l, h, d) in enumerate(items):
    x = Inches(0.6 + (i % 3) * 4.15); y = Inches(1.7 + (i // 3) * 2.5)
    rect(s, x, y, Inches(3.95), Inches(2.25), PALE)
    text(s, x + Inches(0.2), y + Inches(0.1), Inches(1), Inches(0.8), l, 40, True, ACC)
    text(s, x + Inches(1.0), y + Inches(0.3), Inches(2.8), Inches(0.5), h, 18, True, INK)
    text(s, x + Inches(0.2), y + Inches(1.0), Inches(3.6), Inches(1.2), d, 14, False, INK)

# 7 Competitors
s = slide("Competitors: specialists above, value below", "Competitor analysis",
          "ASICS is the running specialist and the main threat with serious runners. Decathlon's Kiprun is the main threat with beginners, at 2,000 to 6,000 rupees. adidas and Puma are bigger than Nike in India. The price ladder shows Nike's gap between Vegam and Pegasus.")
img(s, "price_ladder.png", Inches(0.5), Inches(1.5), w=Inches(7.3))
table(s, Inches(8.0), Inches(1.6), Inches(4.9), ["Brand", "Strength", "Weakness"], [
    ["ASICS", "Running credibility, fit", "Lower awareness"], ["adidas", "Scale, cricket", "Less running focus"],
    ["Puma", "Scale, value", "Weaker running image"], ["Skechers", "Comfort walking", "Not 'serious running'"],
    ["Decathlon", "Price-performance", "Low aspiration"]], size=11, col_w=[1.2, 1.9, 1.8], row_h=0.55)

# 8 Segmentation
s = slide("Segmentation: four bases", "Segmentation",
          "I used all four bases. Behavioural segmentation is the most useful for running: usage rate and user status separate a 30-kilometre-a-week runner from a beginner. Five psychographic segments come out of this.")
quad = [("Demographic", "18-40; men + fast-growing women; ISEC A1-B; students, professionals; parents buying for teens"),
        ("Geographic", "Mumbai, Bengaluru, Delhi lead; tier-2 is the growth frontier; heat and monsoon"),
        ("Psychographic", "Performance chasers, fitness balancers, social runners, style-led aspirers, cautious beginners"),
        ("Behavioural", "Usage rate; loyalty (Nike-loyal vs switchers); race-season occasions; benefits sought; user status")]
for i, (h, d) in enumerate(quad):
    x = Inches(0.6 + (i % 2) * 6.2); y = Inches(1.7 + (i // 2) * 2.55)
    rect(s, x, y, Inches(5.95), Inches(2.3), PALE)
    rect(s, x, y, Inches(0.12), Inches(2.3), ACC)
    text(s, x + Inches(0.35), y + Inches(0.15), Inches(5.4), Inches(0.5), h, 20, True, INK)
    text(s, x + Inches(0.35), y + Inches(0.75), Inches(5.4), Inches(1.5), d, 15, False, INK)

# 9 Targeting
s = slide("Targeting: attractiveness vs compatibility", "Targeting",
          "Using the Session 9 framework: performance chasers and fitness balancers are primary. Cautious beginners are very attractive and became compatible with Vegam Run. Value-only buyers are not targeted because they'd dilute the brand. Nike uses differentiated multi-segment targeting.")
table(s, Inches(0.6), Inches(1.6), Inches(12.1), ["Segment", "Attractiveness", "Compatibility", "Decision"], [
    ["Performance chasers (A1-A2)", "Medium size, high value", "Very high", "Primary"],
    ["Fitness balancers (A2-B)", "Large, growing", "High", "Primary"],
    ["Cautious beginners (metro + tier-2)", "Very large, fast growing", "Medium, rising with Vegam", "Secondary (growth)"],
    ["Style-led students", "Large; parents pay", "High brand fit", "Secondary"],
    ["Value-only (< Rs 2,500)", "Huge volume, low margin", "Low", "Not targeted"]], size=14, col_w=[3.2, 3, 3, 2], row_h=0.6)
bullets(s, Inches(0.6), Inches(5.4), Inches(12), Inches(1.4), [
    "Strategic targeting|whom Nike creates value for: serious and regular urban runners",
    "Tactical targeting|how to reach them: run clubs, race expos, NRC app, Strava, marketplace search"], size=15)

# 10 Positioning
s = slide("Positioning: POPs and PODs", "Positioning",
          "The positioning statement follows the Session 11 template. Cushioning and durability are points of parity. Innovation, aspiration and community are points of difference. Value for money is the gap.")
rect(s, Inches(0.6), Inches(1.6), Inches(12.1), Inches(1.3), PALE)
text(s, Inches(0.85), Inches(1.7), Inches(11.6), Inches(1.1), "\"For urban Indian runners who take their running seriously, Nike Running is the performance running brand that helps you run further and faster than you thought you could, because its shoes are built on the innovations elite athletes race in.\"", 15, False, BLUE)
table(s, Inches(0.6), Inches(3.2), Inches(12.1), ["Attribute", "Type", "Desirable", "Deliverable", "Differentiating"], [
    ["Comfortable cushioning", "POP", "Yes", "Yes", "No"], ["Elite innovation (ZoomX, super shoes)", "POD", "Yes", "Yes", "Yes"],
    ["Brand aspiration (Swoosh, athletes)", "POD", "Yes", "Yes", "Yes"], ["Running community (NRC, After Dark)", "POD", "Yes", "Partly", "Yes where present"],
    ["Value for money", "Gap", "Yes", "Only via Vegam", "No"]], size=13, col_w=[3.6, 1, 1.4, 1.8, 2.2], row_h=0.55)

# 11 Perceptual map
s = slide("Perceptual map: an open 'affordable + credible' space", "Perceptual map",
          "The price axis uses real MRPs. The credibility axis is provisional and will be replaced by my respondents' ratings; the workbook replots it. The open space is affordable and credible. Decathlon is moving into it from below, and Vegam Run is Nike's move in from above.")
img(s, "perceptual.png", Inches(0.6), Inches(1.5), h=Inches(5.3))
bullets(s, Inches(8.0), Inches(1.9), Inches(4.9), Inches(4.5), [
    "Price axis|actual India MRPs of core running shoes",
    "Credibility axis|provisional, to be replaced by interview rating cards",
    "Insight|whoever owns 'affordable + credible' wins India's new runners"], size=15)

# 12 Product strategy
s = slide("Product strategy: levels, line and life cycle", "Product strategy",
          "Core benefit is comfortable, confident running. The augmented product is the NRC app, fitting and events. Pegasus is mature and refreshed yearly; Vomero is in renewed growth; Vegam is in introduction.")
table(s, Inches(0.6), Inches(1.6), Inches(6.0), ["Level", "Pegasus 42"], [
    ["Core", "Comfortable, injury-free, confident running"], ["Actual", "ReactX + Air Zoom, mesh upper, Swoosh, box"],
    ["Augmented", "NRC app plans, store fitting, exchange policy, run clubs"]], size=13, col_w=[1.3, 4.7], row_h=0.75)
img(s, "plc.png", Inches(6.9), Inches(1.6), w=Inches(6.0))
bullets(s, Inches(0.6), Inches(4.9), Inches(12), Inches(1.6), [
    "Line depth|deep at the premium end, thin below Rs 4,000 until Vegam",
    "NPD|Vegam went from brief to product in 55 days, against about 18 months normally (Nike, 2026a)"], size=15)

# 13 Branding & communication
s = slide("Branding and communication", "Branding & IMC",
          "Brand equity in India is ahead of sales. Cricket and global films build awareness; community events like After Dark build running loyalty but are too small. I'd localise Why Do It for beginners and add an Indian running ambassador.")
table(s, Inches(0.6), Inches(1.6), Inches(12.1), ["Campaign", "Audience", "Assessment"], [
    ["Winning Isn't for Everyone (2024)", "Competitive runners", "Strong for serious runners; can alienate beginners"],
    ["After Dark Tour Mumbai (May 2025)", "Women runners", "Very effective, but limited scale"],
    ["NorBlack NorWhite (Jun 2025)", "Young style-led women", "Local relevance; lifestyle more than running"],
    ["Why Do It? (Sep 2025)", "Gen Z", "Right message for beginners; India adaptation missing"],
    ["Shubman Gill: Nike Mind (2026)", "Cricket fans", "High reach, low running relevance"],
    ["Vegam Run launch (Nov 2026)", "New runners", "Right message; depends on reviews and trial"]], size=13, col_w=[3.8, 2.6, 5.7], row_h=0.58)

# 14 Pricing
s = slide("Pricing: premium ladder with a new entry point", "Pricing",
          "Nike prices for value-based premium positioning. Vegam at 3,795 rupees creates a Good-Better-Best ladder. The risk is the 18 percent GST slab above 2,500 rupees and marketplace discounting.")
stat(s, Inches(0.6), Inches(1.7), "Rs 3,795", "Vegam Run (Good)")
stat(s, Inches(3.7), Inches(1.7), "Rs 12,995", "Pegasus 42 (Better)")
stat(s, Inches(6.8), Inches(1.7), "Rs 13,295+", "Vomero 18 (Best comfort)")
stat(s, Inches(9.9), Inches(1.7), "18% GST", "on footwear above Rs 2,500")
bullets(s, Inches(0.6), Inches(3.5), Inches(12), Inches(3), [
    "Strategy|value-based premium pricing with a new penetration-style entry product",
    "Gap|value rivals at Rs 1,999-5,999 sit in or near the 5% GST slab",
    "Risk|marketplace discounting erodes premium perception",
    "Recommendation|hold core MRPs; replace blanket discounts with trade-up credit"], size=16)

# 15 Distribution
s = slide("Distribution: asset-light, metro-heavy", "Distribution",
          "Nike now runs partner stores, multi-brand outlets, a Nykaa-run nike.com and authorised marketplaces. This fits metro performance runners but not tier-2 beginners. Vegam on Flipkart is the first fix. Counterfeits and discounting are the main risks.")
img(s, "channels.png", Inches(0.6), Inches(1.5), w=Inches(7.2))
bullets(s, Inches(8.1), Inches(1.7), Inches(4.8), Inches(5), [
    "Partner EBOs|93 to 120+ stores, depending on source",
    "nike.com|run by Nykaa since Feb 2026",
    "Marketplaces|Flipkart, Myntra, Ajio, VegNonVeg, Superkicks",
    "Gap|expert fitting outside metros",
    "Risk|'first copy' counterfeits"], size=15)

# 16 Interview methodology
s = slide("Primary research: interview methodology", "Interview methodology",
          "Exploratory qualitative research. Eight short semi-structured interviews, two women and six men, across every stakeholder type. Purposive sampling with snowball referrals. Three-level coding as taught in class.")
table(s, Inches(0.6), Inches(1.6), Inches(7.3), ["Code", "Stakeholder", "Gender"], [[x[0], x[2], x[1]] for x in V.SETS], size=12, col_w=[0.8, 5.2, 1.3], row_h=0.5)
bullets(s, Inches(8.2), Inches(1.7), Inches(4.7), Inches(5), [
    "Design|exploratory, semi-structured, 2-3 min each",
    "Sampling|purposive + snowball; minimum 5, planned 8",
    "Analysis|quote, code, category, theme, hypothesis",
    "Tools|rating card feeds the perceptual map"], size=15)

# 17 Findings
s = slide("Interview findings", "Interview findings",
          "This slide is completed after the interviews. Fill in the main themes with one short real quote each, and mark each hypothesis as supported or not. Do not fill this in before the interviews.")
table(s, Inches(0.6), Inches(1.6), Inches(12.1), ["Hypothesis", "Statement", "Result"], [[h[0], h[1], "[after interviews]"] for h in V.HYPOTHESES], size=12, col_w=[1.2, 8.4, 2.5], row_h=0.5)
text(s, Inches(0.6), Inches(6.3), Inches(12), Inches(0.5), "Findings will be added from real interview transcripts; no responses have been pre-written.", 12, False, GREY)

# 18 SWOT
s = slide("SWOT analysis", "SWOT",
          "Strengths are brand and innovation. Weaknesses are India sales and store reach. Opportunities are the running boom, tier-2 and women runners. Threats are ASICS, Decathlon, GST and counterfeits.")
sw = [("STRENGTHS", BLUE, ["Strongest sports brand", "Running innovation leadership", "Global running momentum", "NRC app, After Dark Tour"]),
      ("WEAKNESSES", GREY, ["India sales behind adidas, Puma", "Reduced store network", "Thin range below Rs 4,000", "Little India running communication"]),
      ("OPPORTUNITIES", RGBColor(0x3A, 0x8F, 0x85), ["Running boom: 69,000+ at TMM 2026", "Tier-2 and women runners", "Vegam Run wider rollout 2027", "Comfort / Vomero demand"]),
      ("THREATS", ACC, ["ASICS aims for #1 premium by 2029", "Decathlon Kiprun value", "GST 18% above Rs 2,500", "Counterfeits, discounting"])]
for i, (h, col, its) in enumerate(sw):
    x = Inches(0.6 + (i % 2) * 6.2); y = Inches(1.6 + (i // 2) * 2.65)
    rect(s, x, y, Inches(5.95), Inches(2.45), PALE)
    rect(s, x, y, Inches(5.95), Inches(0.5), col)
    text(s, x + Inches(0.2), y + Inches(0.06), Inches(5.5), Inches(0.4), h, 16, True, WHITE)
    bullets(s, x + Inches(0.2), y + Inches(0.6), Inches(5.6), Inches(1.8), its, size=14, gap=2)

# 19 Recommendations
s = slide("Recommendations", "Recommendations",
          "Four recommendations, each linked to evidence: make Vegam the first Nike, offer fit help, authenticate products, and expand the running community with an Indian running ambassador.")
recs = [("Product", "Good-Better-Best ladder; wide-fit and monsoon editions"), ("Price", "Hold core MRPs; trade-up credit instead of blanket discounts"),
        ("Promotion", "Localise 'Why Do It?' for beginners; Indian running ambassador; NRC in 10 cities"),
        ("Place", "Vegam via Flipkart and tier-2 MBOs; Fit Lab in 30 stores; authenticated listings")]
for i, (h, d) in enumerate(recs):
    y = Inches(1.65 + i * 1.25)
    rect(s, Inches(0.6), y, Inches(2.4), Inches(1.05), INK)
    text(s, Inches(0.6), y, Inches(2.4), Inches(1.05), h, 20, True, WHITE, PP_ALIGN.CENTER, MSO_ANCHOR.MIDDLE)
    rect(s, Inches(3.0), y, Inches(9.7), Inches(1.05), PALE)
    text(s, Inches(3.25), y, Inches(9.3), Inches(1.05), d, 16, False, INK, anchor=MSO_ANCHOR.MIDDLE)

# 20 Marketing plan
s = slide("Proposed 12-month marketing plan (my proposal)", "Proposed marketing plan",
          "This is my proposal, not Nike's plan. Seven initiatives over 12 months with an assumed 45 crore rupee budget, about 3 percent of Nike India's reported sales. Each has an objective, audience, timeline, budget and KPI.")
table(s, Inches(0.6), Inches(1.55), Inches(7.0), ["Initiative", "Rs cr", "KPI"], [
    ["First 5K with Vegam", "9.0", "5K finishers; Vegam units"], ["NRC City Crews (3 to 10 cities)", "6.0", "Active members"],
    ["Fit Lab (30 stores)", "5.5", "Conversion; returns"], ["Trade-Up credit", "4.0", "15% trade-up"],
    ["Genuine Swoosh (QR)", "3.0", "90% authenticated listings"], ["Ambassador + After Dark", "9.5", "Earned media"],
    ["Marathon-season burst", "8.0", "Consideration +10 pts"]], size=12, col_w=[3.2, 0.8, 3], row_h=0.5)
img(s, "gantt.png", Inches(7.8), Inches(1.6), w=Inches(5.2))
text(s, Inches(7.8), Inches(4.4), Inches(5.2), Inches(2), ["Objective: make Vegam the best-selling Nike running shoe in India,", "add 200,000 NRC users, and convert 15% of Vegam buyers to Pegasus or Vomero."], 13, False, INK)

# 21 Conclusion
s = slide("Conclusion", "Conclusion",
          "Nike has the strongest running brand but not yet the strongest running business in India. The 2026 changes are the right direction. Keep the premium core, and use Vegam, community and fit-led authenticated retail to win India's next generation of runners.")
rect(s, Inches(0.6), Inches(1.7), Inches(12.1), Inches(1.6), INK)
text(s, Inches(0.9), Inches(1.8), Inches(11.5), Inches(1.4), "Nike has India's strongest running brand, but not yet its strongest running business.", 26, True, WHITE, anchor=MSO_ANCHOR.MIDDLE)
bullets(s, Inches(0.6), Inches(3.7), Inches(12), Inches(3), [
    "Keep|premium performance position with Pegasus, Vomero and race shoes",
    "Recruit|India's new runners with Vegam Run and a beginner programme",
    "Convert|through community running, fit help and authenticated retail",
    "Validate|with the stakeholder interviews before final recommendations"], size=18)

# 22 References
s = slide("Key references", "References",
          "The full APA reference list with working links is in the report and the workbook's source log.")
refs = ["Nike, Inc. (2026a). Nike Vegam Run is built for India's next generation of runners.",
        "Nike, Inc. (2026b). Fiscal 2026 fourth quarter and full year results.",
        "Nike, Inc. (2026d). Fiscal 2027 first quarter results.",
        "Nike India. (2026a). Nike India changes coming February 2026.",
        "Financial Express. (2026). Finding the right fit (Nike India FY25 sales).",
        "Open Magazine. (2026a, 2026b). Vegam Run on Flipkart; Decathlon vs Nike, adidas, Puma.",
        "Press Information Bureau. (2025). GST rate rationalisation factsheet.",
        "Bureau of Indian Standards. (2026). Footwear QCO amendment order.",
        "Financial Express. (2025). ASICS sprinting towards top spot.",
        "Procam International. (2026). 69,000+ runners for Tata Mumbai Marathon 2026.",
        "IMARC Group. (2026). India athletic footwear market.",
        "LawBeat. (2024). Nike wins trademark suit against counterfeit shoes."]
bullets(s, Inches(0.6), Inches(1.6), Inches(12.1), Inches(5.2), refs, size=13, gap=3)

out = os.path.join(ROOT, "Nike_Running_Presentation.pptx")
prs.save(out)
print("slides:", len(prs.slides), out)
