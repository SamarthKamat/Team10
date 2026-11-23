"""Builds the Interview Toolkit, Viva Preparation, the three Viva-folder files and the combined Interview Pack."""
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(__file__))
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import docxlib as D
import viva_data as V

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HDR = "Nike Running Footwear  |  Marketing Management  |  GIM 2026-27"


def title_block(doc, kicker, title, sub):
    t = doc.add_table(rows=1, cols=1); D.table_borders(t, inside=False, outer=False)
    c = t.rows[0].cells[0]; c.width = Cm(16.4); D.shade(c, D.HEX_INK); D.cell_margins(c, 260, 260, 300, 300)
    p = c.paragraphs[0]; r = p.add_run(kicker.upper()); r.bold = True; r.font.size = Pt(8.5); r.font.color.rgb = D.ACCENT
    p = c.add_paragraph(); r = p.add_run(title); r.bold = True; r.font.size = Pt(22); r.font.color.rgb = RGBColor(255, 255, 255)
    p = c.add_paragraph(); r = p.add_run(sub); r.font.size = Pt(10); r.font.color.rgb = RGBColor(0xDD, 0xDD, 0xDD)
    D.para(doc, "", after=6)


def h1(doc, t):
    p = doc.add_paragraph(style="Heading 1"); p.add_run(t); return p


def h2(doc, t):
    p = doc.add_paragraph(style="Heading 2"); p.add_run(t); return p


def save(doc, name, pdf=False):
    path = os.path.join(ROOT, name)
    doc.save(path)
    if pdf:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", ROOT, path],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("saved", name)


# ---------------- shared pieces ----------------

def hypotheses_table(doc):
    D.table(doc, ["Code", "Working hypothesis (to support, modify or reject)"], [list(h) for h in V.HYPOTHESES], widths=[0.8, 6.2])


def consent(doc):
    D.box(doc, "Consent line (read at the start of every recording)", [V.OPENING,
          "If they say yes, start recording and say the respondent code, date and place aloud, e.g. 'R3, 2 December, Panaji'."],
          fill=D.HEX_PALE, title_color=D.BLUE)


def interview_set(doc, s, with_timing=True, with_answers_space=False, compact=False):
    sid, gender, role, who, qs, optional = s
    p = doc.add_paragraph(style="Heading 2"); p.add_run(f"{sid}: {role}")
    D.para(doc, f"**Gender:** {gender}    **Who to find:** {who}", size=9.5, after=4)
    rows = [["0:00-0:15", "Opening and consent", "-", "-", "-"]]
    t0 = 15
    for i, (q, probe, cap, hyp) in enumerate(qs, 1):
        a, b = t0, t0 + 22
        rows.append([f"{a//60}:{a%60:02d}-{b//60}:{b%60:02d}", f"Q{i}. {q}", probe, cap, hyp])
        t0 = b
    rows.append(["only if < 2:30", f"Optional. {optional}", "-", "-", "-"])
    rows.append(["last 15 s", V.CLOSING, "-", "-", "-"])
    if with_timing:
        D.table(doc, ["Time", "Question (say it naturally)", "Probe if answer is short", "Captures", "Tests"], rows,
                widths=[0.9, 3.0, 1.7, 1.2, 0.6], size=8.5)
    else:
        D.table(doc, ["#", "Question", "Probe"], [[str(i), q, pr] for i, (q, pr, _, _) in enumerate(qs, 1)], widths=[0.4, 4, 2.2], size=8.8)
    D.para(doc, "", after=2)


def rating_card(doc):
    D.para(doc, "**Brand rating card** (show on phone after the questions; 1 = very low, 10 = very high). The workbook's Perceptual_Map sheet averages these to replot the map.", size=9.5)
    D.table(doc, ["Attribute"] + V.RATING_BRANDS, [[a] + [""] * len(V.RATING_BRANDS) for a in V.RATING_ATTRS],
            widths=[2.4] + [1] * len(V.RATING_BRANDS), size=8.5)


def field_note(doc):
    D.table(doc, ["Field note (fill within 10 minutes of the interview)", ""], [
        ["Respondent code / date / place", ""], ["Approx. age / occupation", ""], ["Duration and language used", ""],
        ["Body language, hesitation, enthusiasm", ""], ["Most striking quote", ""], ["Anything that surprised you", ""],
    ], widths=[2.6, 4.4], size=9)


def analysis_frame(doc):
    D.para(doc, "Use the same layout as the faculty's Qualitative Analysis slide: exact quote, first-level code (in the respondent's words), category, broader theme and the hypothesis it relates to.", size=10)
    D.table(doc, ["Respondent", "Exact quote", "First-level code", "Category", "Broader theme", "Hypothesis"],
            [["R1", "", "", "", "", ""] for _ in range(1)] + [[f"R{i}", "", "", "", "", ""] for i in range(2, 9)],
            widths=[0.8, 2.6, 1.4, 1.2, 1.3, 0.9], size=8.5)
    D.para(doc, "Worked layout example (format only, not data):", size=9, italic=True, color=D.GREY, before=6)
    D.table(doc, ["Exact quote", "First-level code", "Category", "Broader theme", "Hypothesis"],
            [["\"[respondent's exact words]\"", "e.g. 'too costly for a beginner'", "Price barrier", "Affordability", "H2"]],
            widths=[2.4, 1.6, 1.2, 1.3, 0.8], size=8.5)


THEMES = [("Brand awareness and associations", "How respondents know Nike and what they link it with"),
          ("Purchase motivation / benefits sought", "Why they choose a running shoe: comfort, performance, style, price"),
          ("Price sensitivity", "Price ranges, sales, value judgements"),
          ("Competition and switching", "Why they choose ASICS, adidas, Decathlon etc."),
          ("Influence", "Clubs, coaches, peers, store staff, YouTube, parents"),
          ("Channel and trust", "Store vs online, fear of fakes"),
          ("Unmet needs", "Fit, beginner guidance, Indian conditions, community")]


# ---------------- documents ----------------

def toolkit():
    doc = D.new_document(); D.set_header_footer(doc.sections[0], HDR)
    title_block(doc, "Primary research", "Interview Toolkit", "Qualitative interviews with Nike running-footwear stakeholders: method, questionnaires, recording, coding and findings templates")
    h1(doc, "A. Research objectives")
    D.bullets(doc, ["Understand how Indian runners and buyers choose running shoes (decision process, benefits sought, influences).",
                    "Find out how consumers, parents and retailers perceive Nike versus ASICS, adidas, Puma, Skechers and Decathlon.",
                    "Identify barriers to buying Nike running shoes and reactions to the new Vegam Run.",
                    "Understand channel behaviour: stores, brand site, marketplaces, fear of counterfeits.",
                    "Test the working hypotheses H1-H6 used in the report."])
    hypotheses_table(doc)
    h1(doc, "B. Research methodology")
    D.para(doc, "Exploratory, qualitative research using short semi-structured in-depth interviews. Open-ended, non-leading questions with probes. Interviews are recorded with consent, transcribed word for word and analysed with three-level coding (quote, code, category, theme), as taught in class.", align="j")
    h1(doc, "C. Sampling unit")
    D.para(doc, "Any person who buys, uses, sells or influences the purchase of running shoes in India: runners, parents, store owners, store staff and coaches.")
    h1(doc, "D. Sample selection")
    D.para(doc, "Purposive (judgement) sampling for variety of stakeholder types, with snowball referrals through run clubs. Minimum five respondents as required by the faculty; eight are planned (two women, six men).", align="j")
    D.table(doc, ["Code", "Stakeholder", "Gender", "Where to find"], [[s[0], s[2], s[1], s[3]] for s in V.SETS], widths=[0.6, 2.8, 0.8, 3.3], size=8.8)
    h1(doc, "E. Interview questionnaires")
    D.para(doc, "Each questionnaire has 8-10 open-ended questions: the core questions used in the 2-3 minute recordings, the optional question, the word-association exercise and the brand rating card. Probes are used only if an answer is very short.", align="j")
    for s in V.SETS:
        sid, gender, role, who, qs, optional = s
        h2(doc, f"{sid}: {role}")
        rows = [[str(i), q, pr] for i, (q, pr, _, _) in enumerate(qs, 1)]
        n = len(qs)
        rows += [[str(n + 1), optional, "Why?"],
                 [str(n + 2), "When I say Nike running shoes, what three words come to mind?", "If Nike were a person, who would it be?"],
                 [str(n + 3), "Please rate these six brands on the rating card.", "Why did you give Nike that score?"],
                 [str(n + 4), "If you could tell Nike one thing to improve for runners in India, what would it be?", "Anything else?"]]
        D.table(doc, ["#", "Question", "Probe"], rows, widths=[0.4, 4.2, 2.4], size=8.8)
    h1(doc, "F. Interview recording template")
    field_note(doc)
    h1(doc, "G. Qualitative coding framework")
    D.table(doc, ["Level", "What you do", "Example format"], [
        ["1. First-level (open) codes", "Label each meaningful phrase with a short code, close to the respondent's words", "'Pegasus feels too costly'"],
        ["2. Categories", "Group similar codes", "Price barrier"],
        ["3. Themes", "Group categories into broader themes", "Affordability"],
        ["4. Hypothesis link", "Mark which hypothesis each theme supports or contradicts", "H2 supported / not supported"],
    ], widths=[1.6, 3.2, 2.2])
    h1(doc, "H. Thematic analysis framework")
    D.table(doc, ["Theme", "What to look for", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"],
            [[a, b] + [""] * 8 for a, b in THEMES], widths=[1.6, 2.2] + [0.4] * 8, size=8.3)
    h1(doc, "I. Findings presentation template")
    D.table(doc, ["Theme", "Summary of what respondents said", "Supporting quote", "Hypothesis outcome", "Marketing implication"],
            [[t[0], "", "", "", ""] for t in THEMES], widths=[1.5, 2, 1.6, 1, 1.6], size=8.5)
    h1(doc, "J. Limitations")
    D.bullets(doc, ["Small purposive sample: shows reasons and themes, not percentages.",
                    "Short recordings limit depth; probes help.",
                    "Respondents may give socially desirable answers; avoid leading questions and don't share questions beforehand.",
                    "Mostly Goa and nearby cities; tier-1 and tier-2 differences may be under-represented."])
    h1(doc, "K. Store-visit observation sheet")
    D.table(doc, ["Observation", "Store 1", "Store 2"], [[x, "", ""] for x in [
        "Store type (Nike EBO / MBO / large-format)", "Brands on running wall and approx. number of models each",
        "Nike models and MRPs seen (Vegam, Pegasus, Vomero)", "Competitor models and MRPs", "Shelf position of Nike vs others",
        "Offers / discounts displayed", "Staff advice when asked for a beginner shoe", "Photo taken (file name)"]],
        widths=[3, 2, 2])
    save(doc, "Nike_Running_Interview_Toolkit.docx")


def viva_prep():
    doc = D.new_document(); D.set_header_footer(doc.sections[0], HDR)
    n = sum(len(q) for _, q in V.VIVA)
    title_block(doc, "Viva preparation", "Viva Questions & Answers", f"{n} likely questions with natural answers you can say aloud in 30-60 seconds")
    D.box(doc, "How to use this", ["Read each answer aloud twice, then answer from memory in your own words.",
                                   "Key numbers to remember: Rs 1,380 cr (Nike India FY25), $46.4 bn (Nike FY26), Rs 3,795 (Vegam Run), Rs 12,995 (Pegasus 42), 69,000+ (Tata Mumbai Marathon 2026), GST 5% up to Rs 2,500 and 18% above.",
                                   "If you don't know something, say what evidence you used and what you'd check. Don't guess numbers."],
          fill=D.HEX_PALE, title_color=D.BLUE)
    k = 0
    for cat, qs in V.VIVA:
        h1(doc, cat)
        for q, a in qs:
            k += 1
            p = D.para(doc, f"Q{k}. {q}", bold=True, keep=True, after=2, before=6, color=D.INK)
            D.para(doc, a, align="j", after=6)
    save(doc, "Nike_Running_Viva_Preparation.docx")


def viva1(doc=None, standalone=True):
    if standalone:
        doc = D.new_document(); D.set_header_footer(doc.sections[0], HDR)
        title_block(doc, "Viva | Folder 1 - Voice recordings", "Interview Guide for Recordings",
                    "8 short interviews (2 women, 6 men), 2-3 minutes each, with question flow and timings")
    h1(doc, "Sampling plan")
    D.table(doc, ["Code", "Stakeholder", "Gender", "Who to find"], [[s[0], s[2], s[1], s[3]] for s in V.SETS], widths=[0.6, 2.8, 0.8, 3.3], size=8.8)
    D.para(doc, "Eight respondents cover every stakeholder type and exceed the minimum of five.", size=9.5, italic=True, color=D.GREY)
    h1(doc, "Recording rules")
    D.bullets(doc, ["Use your phone's voice recorder in a quiet place; hold it about 30 cm away.",
                    "Don't share the questions beforehand, and don't suggest answers.",
                    "Let people answer in Hindi, Konkani, Marathi or English, and keep their natural words.",
                    "Keep each recording under 3 minutes: about 15 s opening, 5-6 questions of about 20 s each, 15 s close.",
                    "Use the probe only if the answer is a few words. Ask the optional question only if you're under 2:30.",
                    "Don't re-record to get 'better' answers. Real hesitation is fine and is what the faculty expects."])
    h1(doc, "File naming")
    D.table(doc, ["Example file name", "Meaning"], [["R1_F_Runner_2026-12-02.m4a", "Code, gender, role, date"],
                                                   ["R6_M_MBOOwner_2026-12-03.m4a", "Multi-brand store owner"]], widths=[3, 4])
    consent(doc)
    h1(doc, "Interview sets")
    for s in V.SETS:
        interview_set(doc, s)
    D.box(doc, "After every interview", ["Ask the word-association question and show the brand rating card if time allows (outside the 3-minute recording is fine).",
                                         "Fill the field note within 10 minutes."], fill=D.HEX_PALE, title_color=D.BLUE)
    hypotheses_table(doc)
    if standalone:
        save(doc, "Viva_1_Interview_Guide_Recordings.docx")


def viva2(doc=None, standalone=True):
    if standalone:
        doc = D.new_document(); D.set_header_footer(doc.sections[0], HDR)
        title_block(doc, "Viva | Folder 2 - Transcripts", "Transcript Sheets",
                    "One sheet per respondent. Questions are filled in; type the answers exactly as spoken")
    D.box(doc, "Transcription rules", ["Type exactly what was said, including 'umm', repeats and mixed languages. Add an English translation in brackets where needed.",
                                       "Add a timestamp [0:35] at the start of each answer.",
                                       "Mark unclear words as [inaudible 1:12]. Don't fix grammar or improve answers."],
          fill=D.HEX_PALE, title_color=D.BLUE)
    for i, s in enumerate(V.SETS):
        sid, gender, role, who, qs, optional = s
        if i:
            D.page_break(doc)
        h1(doc, f"Transcript {sid}: {role}")
        D.table(doc, ["Respondent code", "Gender", "Age (approx.)", "Occupation", "Date / place", "Duration", "Language"],
                [[sid, gender, "", "", "", "", ""]], size=8.5)
        D.para(doc, "", after=4)
        D.para(doc, f"[0:00] **Interviewer:** {V.OPENING}", size=9.5)
        D.para(doc, "[0:__] **Respondent:** ______________________________________________", size=9.5)
        for j, (q, *_rest) in enumerate(qs, 1):
            D.para(doc, f"[0:__] **Interviewer (Q{j}):** {q}", size=9.5, before=4)
            for _ in range(3):
                D.para(doc, "[0:__] **Respondent:** ____________________________________________________________", size=9.5, after=2)
        D.para(doc, f"[_:__] **Interviewer (optional):** {optional}", size=9.5, before=4)
        D.para(doc, "[_:__] **Respondent:** ____________________________________________________________", size=9.5)
    if standalone:
        save(doc, "Viva_2_Transcript_Sheets.docx")


def viva3(doc=None, standalone=True):
    if standalone:
        doc = D.new_document(); D.set_header_footer(doc.sections[0], HDR)
        title_block(doc, "Viva | Folder 3 - Analysis and findings", "Analysis Framework",
                    "Quote, code, category, theme, hypothesis: the faculty's qualitative analysis format")
    h1(doc, "Step 1: Code every transcript")
    analysis_frame(doc)
    h1(doc, "Step 2: Compare across respondents")
    D.table(doc, ["Theme", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "Pattern"],
            [[t[0]] + [""] * 9 for t in THEMES], widths=[1.8] + [0.45] * 8 + [1.4], size=8.3)
    h1(doc, "Step 3: Test the hypotheses")
    D.table(doc, ["Code", "Hypothesis", "Supported / partly / not supported", "Evidence (respondent + quote)"],
            [[h[0], h[1], "", ""] for h in V.HYPOTHESES], widths=[0.6, 3, 1.4, 2.4], size=8.5)
    h1(doc, "Step 4: Write the findings")
    D.table(doc, ["Finding", "Write here"], [["1. Main reasons people choose a running shoe", ""],
                                             ["2. How Nike is perceived vs competitors", ""],
                                             ["3. Barriers to buying Nike (and reaction to Vegam Run)", ""],
                                             ["4. Who influences the purchase", ""],
                                             ["5. Channel and trust (store vs online, fakes)", ""],
                                             ["6. Implications for Nike's marketing (link to report Section 10-11)", ""]],
            widths=[3, 4])
    if standalone:
        save(doc, "Viva_3_Analysis_Framework.docx")


def pack():
    doc = D.new_document(); D.set_header_footer(doc.sections[0], HDR)
    title_block(doc, "Viva", "Viva Interview Pack", "All three viva folders in one file: recording guide, rating card, field notes, transcript template and analysis frame")
    D.box(doc, "Why no answers are written here", [
        "The viva tests real primary research. Answers written in advance and read out by respondents would be invented data, and a follow-up question from the faculty would expose it.",
        "Real two-to-three-minute answers are quick to collect. Send the recordings or typed transcripts and they can be coded and added to the report, slides and viva answers."],
        fill=D.HEX_PALE, title_color=D.BLUE)
    viva1(doc, standalone=False)
    h1(doc, "Exercises (after the questions)")
    D.para(doc, V.WORD_ASSOC)
    rating_card(doc)
    h1(doc, "Field note")
    field_note(doc)
    D.page_break(doc)
    h1(doc, "Transcript template")
    D.table(doc, ["Time", "Speaker", "What was said (exact words)", "English (if needed)"],
            [["[0:00]", "Interviewer", "", ""], ["[0:__]", "Respondent", "", ""], ["[0:__]", "Interviewer", "", ""], ["[0:__]", "Respondent", "", ""]],
            widths=[0.7, 1.1, 3.4, 2.2])
    viva3(doc, standalone=False)
    save(doc, "Nike_Viva_Interview_Pack.docx")


if __name__ == "__main__":
    toolkit(); viva_prep(); viva1(); viva2(); viva3(); pack()
