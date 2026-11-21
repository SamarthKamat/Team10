import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

P = RGBColor(0x5B, 0x2C, 0x83); PL = RGBColor(0xEF, 0xE8, 0xF7); INK = RGBColor(0x22, 0x22, 0x22)
GREY = RGBColor(0x66, 0x66, 0x66); WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DOM = [RGBColor(0x7B, 0x4F, 0xA6), RGBColor(0x3E, 0x7C, 0xB1), RGBColor(0x4E, 0x8B, 0x3A)]
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

def text(sl, x, y, w, h, runs, size=16, color=INK, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = sl.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h)); tf = tb.text_frame; tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, r in enumerate(runs if isinstance(runs, list) else [runs]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph(); p.alignment = align
        t, b = (r if isinstance(r, tuple) else (r, bold))
        run = p.add_run(); run.text = t; run.font.size = Pt(size); run.font.bold = b; run.font.color.rgb = color; run.font.name = "Calibri"
        p.space_after = Pt(6)
    return tb

def box(sl, x, y, w, h, fill, txt="", size=12, color=WHITE, bold=True, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    s = sl.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    s.fill.solid(); s.fill.fore_color.rgb = fill; s.line.fill.background()
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE: s.adjustments[0] = 0.12
    tf = s.text_frame; tf.word_wrap = True; tf.margin_left = tf.margin_right = Inches(0.05)
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER; r = p.add_run(); r.text = txt
    r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color; r.font.name = "Calibri"
    return s

def header(sl, n, title, sub):
    box(sl, 0, 0, 13.333, 0.12, P, shape=MSO_SHAPE.RECTANGLE)
    text(sl, 0.6, 0.35, 10, 0.5, f"PROJECT A · LENS  ·  CHECKPOINT 1  ·  {n}/3", 12, P, True)
    text(sl, 0.6, 0.7, 12, 0.8, title, 30, INK, True)
    text(sl, 0.6, 1.4, 12, 0.5, sub, 15, GREY)
    text(sl, 0.6, 7.0, 12, 0.35, "Team 10 · Lens: SRS (lead), ANA, AB · Synthetic data only · 26 Nov 2026", 10, GREY)

def notes(sl, t): sl.notes_slide.notes_text_frame.text = t

# Slide 1
s = prs.slides.add_slide(blank)
header(s, 1, "Done: the construct map (D1) covers 90 indicators", "3 domains × 18 constructs × 5 stages. Each indicator is one behaviour you can see, with a source.")
stages = ["Foundational\n3–8", "Preparatory\n8–11", "Middle\n11–14", "Secondary\n14–18", "Post-school\n18–35"]
doms = [("Multiple Intelligences", "8 constructs · Gardner", 8), ("Emotional & Relational", "5 constructs · CASEL", 5), ("Practical & Non-verbal Reasoning", "5 constructs · original tasks", 5)]
x0, y0, cw, ch = 3.6, 2.15, 1.05, 0.62
for j, st in enumerate(stages):
    text(s, x0 + j * (cw + 0.08), y0, cw, 0.6, st, 11, GREY, True, PP_ALIGN.CENTER)
for i, (dn, ds, k) in enumerate(doms):
    y = y0 + 0.7 + i * (ch + 0.12)
    text(s, 0.6, y - 0.02, 2.95, ch, [(dn, True), (ds, False)], 12, INK)
    for j in range(5):
        box(s, x0 + j * (cw + 0.08), y, cw, ch, DOM[i], f"{k}", 18)
text(s, 0.6, 4.95, 8.6, 0.4, "Each cell = indicators for that stage. One growth ladder per construct, from Foundational to Post-school.", 11, GREY)
# shades strip
text(s, 9.5, 2.15, 3.3, 0.4, "7 official URF shades: all checked", 13, P, True)
sh = ["P1 Vision", "P2 Hear", "P3 Voice", "P4 Mind", "P5 Learning", "P6 Intelligence", "P7 Physical"]
for i, t in enumerate(sh):
    box(s, 9.5, 2.6 + i * 0.36, 3.3, 0.3, PL, t, 11, P)
text(s, 9.5, 5.2, 3.4, 0.9, "21 of 21 RPwD Act conditions mapped to a shade. 6 wait for URF (4a, 4b, ASD).", 11, GREY)
text(s, 0.6, 5.45, 8.6, 1.4, [("Also done: ", True), ("0–3 rubric with an N/A rule (an access barrier never becomes a low score) · 7-shade UDL adjustment table · two new scoring formulas for URF to choose from · construct codes for the profile schema (AB, Trajectory)", False)], 13)
notes(s, "Main result first: our D1 construct map is ready for review. It has 90 indicators: 18 constructs, each with one indicator for each of the five stages. The 8 multiple intelligences keep the 8 axes of the Pehchan spider chart. We add two new charts: emotional and relational (CASEL 5) and practical reasoning, where every task is our own. On the right: we checked all seven official URF shades. Every one of the 21 RPwD Act conditions has a shade; six need URF confirmation. We used the fallback because the Pehchan 64 questions have not arrived yet.")

# Slide 2
s = prs.slides.add_slide(blank)
header(s, 2, "Next: items and scoring (D2) by Fri 4 Dec, before exams on 7 Dec", "We map Pehchan's 64 questions when they arrive; the bands stay fixed after D2.")
steps = [
 ("Fri 27 Nov", "D1 FINAL", "ANA review done; file in 1 Lens/Final"),
 ("Mon 30 Nov", "Pehchan map", "Each of the 64 questions → one MI indicator"),
 ("Tue 1 Dec", "Items", "2+ formats per indicator (ANA); URF accessibility review"),
 ("Wed 2 Dec", "Scoring", "Option A in Sheet; AB scoring script; bands confirmed"),
 ("Fri 4 Dec", "D2 sent", "Item log + scoring rules to URF and Trajectory"),
]
for i, (dt, t, dsc) in enumerate(steps):
    x = 0.6 + i * 2.5
    box(s, x, 2.3, 2.3, 0.5, P, dt, 14)
    if i < 4: box(s, x + 2.3, 2.47, 0.2, 0.16, PL, shape=MSO_SHAPE.RIGHT_ARROW)
    text(s, x, 2.95, 2.3, 0.4, t, 16, INK, True, PP_ALIGN.CENTER)
    text(s, x, 3.4, 2.3, 1.0, dsc, 12, GREY, False, PP_ALIGN.CENTER)
box(s, 0.6, 4.65, 5.9, 1.5, PL, "", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 0.8, 4.75, 5.6, 2.0, [("Option A · recommended now", True), ("Score = 100 × Σ wᵢxᵢ ÷ (3 Σ wᵢ), N/A items left out, at least 2 items per construct. Works in the app today; same 8-axis spider chart.", False)], 13, INK)
box(s, 6.83, 4.65, 5.9, 1.5, PL, "", shape=MSO_SHAPE.ROUNDED_RECTANGLE)
text(s, 7.0, 4.75, 5.6, 2.0, [("Option B · after a pilot", True), ("Combine observer, task and the child's own report, weighted by reliability, with a confidence ring on the chart. Needs pilot data and URF approval.", False)], 13, INK)
notes(s, "Next two weeks: Friday 27 the D1 final goes into the Final folder after Anchal's review. Then D2, items and scoring, by Friday 4 December, before the exams. For the new Pehchan formula we give URF two choices. Option A is the one we recommend now: a percent-of-maximum score that leaves out items the child could not access, so a barrier never becomes a low score. It keeps the same spider chart. Option B uses more evidence, including the child's own report, and shows how sure we are, but it needs pilot data first.")

# Slide 3
s = prs.slides.add_slide(blank)
header(s, 3, "Risks and the help we need from URF", "Please give the first four items by Tue 24 Nov, or tell us a date.")
asks = [
 ("1", "Pehchan 64-question bank + current scoring code", "Without it, D2 stays on the fallback base and we re-map later."),
 ("2", "GitHub repository access (Glenn)", "Needed to test the new formula in the NestJS scoring code."),
 ("3", "Scope: vision and physical in Lens?", "D1 covers intelligence only. Must the output stay as 8 spider-chart scores?"),
 ("4", "Shade mapping: RPwD 4(a), 4(b) and ASD", "Default: 4(a)/4(b) → P7, ASD → P4. Please confirm or correct."),
 ("5", "Synthetic personas", "Needed for D3 profiles (18 Dec). Team-made personas only with URF approval."),
]
for i, (n, a, why) in enumerate(asks):
    y = 2.1 + i * 0.86
    box(s, 0.6, y, 0.55, 0.55, P, n, 18, shape=MSO_SHAPE.OVAL)
    text(s, 1.35, y - 0.05, 6.6, 0.45, a, 16, INK, True)
    text(s, 1.35, y + 0.33, 6.6, 0.45, why, 12, GREY)
box(s, 8.4, 2.1, 4.35, 4.4, PL, "")
text(s, 8.6, 2.2, 4.0, 4.3, [("Risks", True),
     ("Late Pehchan bank → D2 re-work. Action: fallback now; map when received.", False),
     ("Shade answers after 4 Dec → D2 formats change. Action: team defaults logged.", False),
     ("Exams 7–13 Dec → no slack. Action: D2 sent Fri 4 Dec.", False),
     ("Label risk: 'Purple Intelligence Disability' next to an intelligence score. Action: show shade codes only in staff views.", False)], 13, INK)
notes(s, "Our asks are the same as in Souvik's Draft 2 email. First, the Pehchan question bank and scoring code. Second, GitHub access. Third, scope: are vision and physical in Lens, and must we keep 8 spider-chart scores? Fourth, the shade mapping for the chronic neurological and blood conditions and for autism; our defaults are on the slide. Fifth, the personas for D3. Biggest risk: a late Pehchan bank. We do not wait: we use the fallback and re-map when it arrives.")

prs.save(sys.argv[1]); print("ok")
