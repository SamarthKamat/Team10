"""Builds Nike_Running_Marketing_Management_Report.docx and .pdf.

Two passes: pass 1 renders the PDF, reads which page each heading/table/figure
lands on, then pass 2 writes those page numbers into the Contents, List of
Tables and List of Figures (all entries are clickable links).
"""
import os, re, subprocess, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
import docxlib as D
from refs import REFS, ordered_keys
import content_a as A
import content_b as B

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHARTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
PHOTOS = os.path.join(ROOT, "photos")
NAME = "Nike_Running_Marketing_Management_Report"
HEADER = "Nike Running Footwear  |  Marketing Management Assignment  |  GIM 2026-27"

SECTIONS = [
    (1, "Introduction to the Company and Product", A.S1, "Brief section 1: company, brand and product introduction",
     "Product classification; brand identity and personality; needs, wants and demand"),
    (2, "Recent Happenings in the Company, Industry and Market", A.S2, "Brief section 2: recent developments (2024-2026) with date, source and significance",
     "Marketing environment; actual strategies and tactics"),
    (3, "Industry Analysis", A.S3, "Brief section 3: industry overview, structure, PESTEL, opportunities and challenges",
     "PESTEL; 5C framework; demand trends"),
    (4, "Competitor Analysis", A.S4, "Brief section 4: major competitors and comparison table",
     "Competitive analysis; points of comparison; price comparison (analytics)"),
    (5, "Segmentation and Targeting Strategy", A.S5, "Brief section 5: four segmentation bases, targeting, consumer vs purchaser",
     "Segmentation bases; strategic vs tactical targeting; attractiveness vs compatibility; personas"),
    (6, "Competitive Positioning", B.S6, "Brief section 6: positioning, POPs/PODs, perceived value, perceptual map",
     "Positioning statement; POPs and PODs; customer perceived value; perceptual mapping"),
    (7, "Product Strategy", B.S7, "Brief section 7: product levels, mix, line, PLC, NPD",
     "Core/actual/augmented product; product mix width and depth; PLC; NPD"),
    (8, "Branding and Communication Strategy", B.S8, "Brief section 8: brand, campaigns and IMC",
     "Brand equity (CBBE); brand personality; IMC; endorsement"),
    (9, "Distribution Strategy", B.S9, "Brief section 9: channels, availability and fit with segments",
     "Distribution channels; general vs modern trade vs e-commerce; channel conflict"),
    (10, "Conclusions and Recommendations", B.S10, "Brief section 10: evaluation, SWOT, unmet needs, recommendations",
     "SWOT; 4Ps; marketing gaps"),
    (11, "Proposed Marketing Plan", B.S11, "Brief section 11: original 6-12 month plan with objectives, budget and KPIs",
     "Marketing planning; SMART objectives; marketing metrics and KPIs"),
]

FIG_W = {"timeline": 16, "perceptual": 13, "channels": 15.5, "plc": 14.5, "sources": 14, "tmm": 13.5}


class Builder:
    def __init__(self, pages=None, breaks=None):
        self.pages = pages or {}
        self.breaks = breaks or set()
        self.tables, self.figures, self.toc = [], [], []
        self.tn = self.fn = 0
        self.doc = None

    def pg(self, anchor):
        return self.pages.get(anchor, "00")

    # ---- block renderer ----
    def render(self, blocks):
        doc = self.doc
        for b in blocks:
            kind = b[0]
            if kind == "h2":
                anchor = f"h_{len(self.toc)}"
                p = doc.add_paragraph(style="Heading 2"); p.add_run(b[1]); D.add_bookmark(p, anchor)
                self.toc.append((b[1], anchor, 1))
            elif kind == "h3":
                p = doc.add_paragraph(style="Heading 3"); p.add_run(b[1])
            elif kind == "p":
                D.para(doc, b[1], REFS, align="j")
            elif kind == "quote":
                p = D.para(doc, b[1], REFS, italic=True, color=D.BLUE, size=11)
                p.paragraph_format.left_indent = Cm(1); p.paragraph_format.right_indent = Cm(1)
            elif kind == "ul":
                D.bullets(doc, b[1], REFS)
            elif kind == "table":
                _, cap, headers, rows, src, widths = b
                self.tn += 1
                anchor = f"tab_{self.tn}"
                p = D.para(doc, "", keep=True, after=3, before=6)
                r = p.add_run(f"Table {self.tn}: "); r.bold = True; r.font.color.rgb = D.ACCENT; r.font.size = Pt(9.5)
                r = p.add_run(cap); r.bold = True; r.font.size = Pt(9.5)
                D.add_bookmark(p, anchor)
                self.tables.append((f"Table {self.tn}: {cap}", anchor))
                D.table(doc, headers, rows, REFS, widths=widths)
                D.para(doc, src, REFS, size=8, italic=True, color=D.GREY, after=8, before=2)
            elif kind == "fig":
                _, name, cap, src = b
                self.fn += 1
                anchor = f"fig_{self.fn}"
                D.picture(doc, os.path.join(CHARTS, name + ".png"), FIG_W.get(name, 15))
                p = D.para(doc, "", align="c", keep=True, after=1)
                r = p.add_run(f"Figure {self.fn}: "); r.bold = True; r.font.color.rgb = D.ACCENT; r.font.size = Pt(9.5)
                r = p.add_run(cap); r.bold = True; r.font.size = Pt(9.5)
                D.add_bookmark(p, anchor)
                self.figures.append((f"Figure {self.fn}: {cap}", anchor))
                D.para(doc, src, REFS, size=8, italic=True, color=D.GREY, align="c", after=10)
            elif kind == "photo":
                path = os.path.join(PHOTOS, b[1])
                if os.path.exists(path):
                    self.fn += 1
                    anchor = f"fig_{self.fn}"
                    D.picture(doc, path, 11)
                    p = D.para(doc, "", align="c", keep=True, after=1)
                    r = p.add_run(f"Figure {self.fn}: "); r.bold = True; r.font.color.rgb = D.ACCENT; r.font.size = Pt(9.5)
                    r = p.add_run(b[2]); r.bold = True; r.font.size = Pt(9.5)
                    D.add_bookmark(p, anchor)
                    self.figures.append((f"Figure {self.fn}: {b[2]}", anchor))
                    D.para(doc, "Source: Author's own photograph.", size=8, italic=True, color=D.GREY, align="c", after=10)
            elif kind == "box":
                fill, col = (D.HEX_PALE, D.BLUE) if b[1].startswith("Note") else (D.HEX_PALE_ACC, D.ACCENT)
                D.box(doc, b[1], b[2], REFS, fill=fill, title_color=col)
            elif kind == "swot":
                self.swot(b[1])
            else:
                raise ValueError(kind)

    def swot(self, data):
        doc = self.doc
        self.tn += 1
        anchor = f"tab_{self.tn}"
        p = D.para(doc, "", keep=True, after=3)
        r = p.add_run(f"Table {self.tn}: "); r.bold = True; r.font.color.rgb = D.ACCENT; r.font.size = Pt(9.5)
        r = p.add_run("SWOT analysis of Nike Running in India"); r.bold = True; r.font.size = Pt(9.5)
        D.add_bookmark(p, anchor)
        self.tables.append((f"Table {self.tn}: SWOT analysis of Nike Running in India", anchor))
        t = doc.add_table(rows=2, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        D.table_borders(t, color="FFFFFF", size=12)
        fills = {"Strengths": ("2F5D7C", "E3ECF2"), "Weaknesses": ("6B6B6B", "EFEFEF"),
                 "Opportunities": ("3A8F85", "E1F0EE"), "Threats": ("E4572E", "FBE3DA")}
        for idx, key in enumerate(["Strengths", "Weaknesses", "Opportunities", "Threats"]):
            c = t.rows[idx // 2].cells[idx % 2]
            c.width = Cm(8.2)
            D.shade(c, fills[key][1]); D.cell_margins(c, 120, 120, 150, 150)
            q = c.paragraphs[0]
            rr = q.add_run(key.upper()); rr.bold = True; rr.font.size = Pt(10.5)
            rr.font.color.rgb = RGBColor.from_string(fills[key][0])
            q.paragraph_format.keep_with_next = True
            for it in data[key]:
                q = c.add_paragraph(); D.rich(q, "•  " + it, REFS, size=9)
                q.paragraph_format.space_after = Pt(2); q.paragraph_format.keep_with_next = True
        for row in t.rows:
            D.cant_split(row)
        D.fix_widths(t, [8.2, 8.2])
        D.para(doc, "Source: Author's analysis using evidence from Sections 2-9.", size=8, italic=True, color=D.GREY, after=8)

    # ---- section opener ----
    def opener(self, num, title, brief, concepts):
        doc = self.doc
        if num in self.breaks:
            D.page_break(doc)
        p = D.para(doc, "", before=14, after=0, keep=True)
        r = p.add_run(f"SECTION {num:02d}"); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = D.ACCENT
        anchor = f"sec_{num}"
        h = doc.add_paragraph(style="Heading 1"); h.add_run(f"{num}. {title}")
        h.paragraph_format.space_before = Pt(0)
        D.add_bookmark(h, anchor)
        self.toc.append((f"{num}. {title}", anchor, 0))
        t = doc.add_table(rows=1, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        D.table_borders(t, inside=False, outer=False)
        for i, (lab, txt) in enumerate((("Answers", brief), ("Course concepts applied", concepts))):
            c = t.rows[0].cells[i]
            c.width = Cm(8.2); D.shade(c, D.HEX_PALE); D.cell_margins(c, 80, 80, 140, 140)
            q = c.paragraphs[0]
            rr = q.add_run(lab.upper() + "\n"); rr.bold = True; rr.font.size = Pt(7.5); rr.font.color.rgb = D.GREY
            rr = q.add_run(txt); rr.font.size = Pt(9)
            q.paragraph_format.space_after = Pt(0)
            q.paragraph_format.keep_with_next = True
        D.cant_split(t.rows[0])
        D.fix_widths(t, [8.2, 8.2])
        D.para(doc, "", after=2, keep=True)

    def unnumbered(self, title, anchor, new_page=True):
        if new_page:
            D.page_break(self.doc)
        h = self.doc.add_paragraph(style="Heading 1"); h.add_run(title)
        D.add_bookmark(h, anchor)
        return h

    # ---- whole document ----
    def build(self, path):
        self.doc = doc = D.new_document()
        self.cover()
        # front matter section (roman)
        sec = doc.add_section(WD_SECTION.NEW_PAGE)
        D.set_page_number_format(sec, "lowerRoman", 1)
        D.set_header_footer(sec, HEADER, page_label="")
        self.front_matter()
        # main section (arabic)
        sec = doc.add_section(WD_SECTION.NEW_PAGE)
        D.set_page_number_format(sec, "decimal", 1)
        D.set_header_footer(sec, HEADER)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("Introduction"); D.add_bookmark(h, "intro")
        self.toc.append(("Introduction", "intro", 0))
        self.render(A.INTRO)
        for num, title, blocks, brief, concepts in SECTIONS:
            self.opener(num, title, brief, concepts)
            self.render(blocks)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("Overall Conclusion"); D.add_bookmark(h, "concl")
        h.paragraph_format.space_before = Pt(20)
        self.toc.append(("Overall Conclusion", "concl", 0))
        self.render(B.CONCLUSION)
        h = doc.add_paragraph(style="Heading 2"); h.add_run("Limitations of the study"); D.add_bookmark(h, "limits")
        self.toc.append(("Limitations of the study", "limits", 1))
        D.bullets(doc, B.LIMITATIONS, REFS)
        self.references()
        self.unnumbered("Appendices", "appx")
        self.toc.append(("Appendices", "appx", 0))
        for i, (t, items) in enumerate(B.APPENDICES):
            h = doc.add_paragraph(style="Heading 2"); h.add_run(t); D.add_bookmark(h, f"appx_{i}")
            self.toc.append((t, f"appx_{i}", 1))
            D.bullets(doc, items, REFS)
        doc.core_properties.title = "Nike Running Footwear: Marketing Management Assignment"
        doc.core_properties.author = "PGDM Student, GIM"
        doc.save(path)
        self._fill_lists(path)

    def cover(self):
        doc = self.doc
        D.clear_header_footer(doc.sections[0])
        t = doc.add_table(rows=1, cols=1); D.table_borders(t, inside=False, outer=False)
        c = t.rows[0].cells[0]; c.width = Cm(16.4); D.shade(c, D.HEX_INK); D.cell_margins(c, 500, 500, 400, 400)
        p = c.paragraphs[0]
        r = p.add_run("GOA INSTITUTE OF MANAGEMENT  |  PGDM - BIG DATA ANALYTICS  |  TERM II"); r.font.size = Pt(9); r.bold = True
        r.font.color.rgb = RGBColor(0xBF, 0xBF, 0xBF)
        p = c.add_paragraph(); r = p.add_run("Marketing Management: Individual Assignment & Viva"); r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.paragraph_format.space_before = Pt(30)
        p = c.add_paragraph(); r = p.add_run("NIKE"); r.bold = True; r.font.size = Pt(54); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        p.paragraph_format.space_after = Pt(0)
        p = c.add_paragraph(); r = p.add_run("RUNNING FOOTWEAR"); r.bold = True; r.font.size = Pt(26); r.font.color.rgb = D.ACCENT
        p = c.add_paragraph(); r = p.add_run(A.SUBTITLE); r.font.size = Pt(12.5); r.font.color.rgb = RGBColor(0xE6, 0xE6, 0xE6)
        p.paragraph_format.space_before = Pt(14); p.paragraph_format.space_after = Pt(30)
        photo = os.path.join(PHOTOS, "nike_cover.jpg")
        if os.path.exists(photo):
            D.para(doc, "", after=4)
            D.picture(doc, photo, 7.5)
        else:
            D.para(doc, "", after=20)
        rows = [("Submitted to", "Prof. Shantanu Prasad"), ("Submitted by", "[Student name]"),
                ("Roll number", "[Roll number]"), ("Programme", "PGDM - Big Data Analytics, Term II, 2026-27"),
                ("Brand / Product", "Nike / Nike Running Footwear (focus: Pegasus; Vegam Run)"),
                ("Company", "NIKE, Inc. and its Indian operations"), ("Submission date", "29 November 2026")]
        t = doc.add_table(rows=len(rows), cols=2); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        D.table_borders(t, color="D9D9D9", size=4, outer=False)
        for i, (a, b) in enumerate(rows):
            D.cell_text(t.rows[i].cells[0], a, bold=True, size=10, color=D.GREY)
            D.cell_text(t.rows[i].cells[1], b, size=10)
            t.rows[i].cells[0].width = Cm(4.5); t.rows[i].cells[1].width = Cm(11.9)
            for c in t.rows[i].cells: D.cell_margins(c, 70, 70, 100, 100)
        D.para(doc, "", after=10)
        t = doc.add_table(rows=1, cols=1); D.table_borders(t, inside=False, outer=False)
        c = t.rows[0].cells[0]; D.shade(c, D.HEX_ACCENT); D.cell_margins(c, 120, 120, 300, 300)
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run("Goa Institute of Management, Sanquelim Campus, Goa  |  Academic Year 2026-27"); r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF); r.bold = True

    def front_matter(self):
        doc = self.doc
        h = doc.add_paragraph(style="Heading 1"); h.add_run("Declaration")
        D.para(doc, "I declare that this assignment on Nike Running Footwear is my own work, prepared for the Marketing Management course at Goa Institute of Management. All secondary sources used are acknowledged in the text and listed in the References. All primary research (interviews) was conducted by me with the consent of the respondents.", align="j")
        D.para(doc, "Use of AI tools: [complete as per GIM policy, or delete this line].", italic=True, color=D.GREY)
        D.para(doc, "Signature: ____________________          Name: [Student name]          Date: ____________", before=24)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("Acknowledgement"); h.paragraph_format.space_before = Pt(30)
        D.para(doc, "I thank Prof. Shantanu Prasad for his guidance in the Marketing Management course, the respondents who gave their time for the interviews, and the store staff who allowed observation of their running-shoe displays.", align="j")
        D.page_break(doc)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("Executive Summary"); D.add_bookmark(h, "exec")
        t = doc.add_table(rows=1, cols=4); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        D.table_borders(t, color="FFFFFF", size=12)
        for i, (big, small) in enumerate(A.EXEC_FIGURES):
            c = t.rows[0].cells[i]; c.width = Cm(4.1); D.shade(c, D.HEX_PALE); D.cell_margins(c, 120, 120, 100, 100)
            q = c.paragraphs[0]; q.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = q.add_run(big); r.bold = True; r.font.size = Pt(17); r.font.color.rgb = D.ACCENT
            q = c.add_paragraph(); q.alignment = WD_ALIGN_PARAGRAPH.CENTER
            D.rich(q, small, REFS, size=8)
        D.para(doc, "", after=4)
        for t_ in A.EXEC_SUMMARY:
            D.para(doc, t_, REFS, align="j")
        # contents
        D.page_break(doc)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("Contents")
        self.toc_anchor_par = D.para(doc, "", after=0)
        D.page_break(doc)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("List of Tables")
        self.lot_anchor_par = D.para(doc, "", after=0)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("List of Figures"); h.paragraph_format.space_before = Pt(20)
        self.lof_anchor_par = D.para(doc, "", after=0)
        h = doc.add_paragraph(style="Heading 1"); h.add_run("Abbreviations"); h.paragraph_format.space_before = Pt(20)
        D.table(doc, ["Abbreviation", "Meaning"], A.ABBREVIATIONS, widths=[1.2, 4], size=8.8)

    def references(self):
        doc = self.doc
        self.unnumbered("References", "refs")
        self.toc.append(("References", "refs", 0))
        D.para(doc, "APA 7th edition. Every reference is cited at least once in the report. Click a citation in the text to jump here, and click a link to open the source. Prices and web pages were accessed in November 2026.", size=9, italic=True, color=D.GREY)
        for k in ordered_keys():
            lab, full, url, *_ = REFS[k]
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1); p.paragraph_format.first_line_indent = Cm(-1)
            p.paragraph_format.space_after = Pt(5)
            r = p.add_run(full + " "); r.font.size = Pt(9.5)
            D.add_external_link(p, url, url, size=9)
            D.add_bookmark(p, "ref_" + k)

    def _fill_lists(self, path):
        # Re-open and insert TOC/LoT/LoF lines at placeholder paragraphs.
        from docx import Document
        doc = Document(path)
        self.doc = doc

        def insert_after(anchor_text_idx, lines_builder):
            pass
        # find the three empty placeholder paragraphs following the headings
        paras = doc.paragraphs
        idx = {p.text: i for i, p in enumerate(paras) if p.style.name == "Heading 1"}
        targets = [("Contents", self.toc_lines), ("List of Tables", self.lot_lines), ("List of Figures", self.lof_lines)]
        for head, fn in targets:
            ph = paras[idx[head] + 1]
            tmp = Document_lines(doc, fn)
            for el in tmp:
                ph._p.addprevious(el)
        doc.save(path)

    def toc_lines(self, doc):
        for text, anchor, level in self.toc:
            D.toc_line(doc, text, anchor, self.pg(anchor), level=level, size=10.5 if level == 0 else 9.5, bold=level == 0)

    def lot_lines(self, doc):
        for text, anchor in self.tables:
            D.toc_line(doc, text, anchor, self.pg(anchor), size=9)

    def lof_lines(self, doc):
        for text, anchor in self.figures:
            D.toc_line(doc, text, anchor, self.pg(anchor), size=9)


def Document_lines(doc, fn):
    """Build paragraphs at the end of doc via fn, then detach and return their elements."""
    body = doc.element.body
    before = len(body)
    fn(doc)
    sectPr = body[-1] if body[-1].tag.endswith("sectPr") else None
    new = [e for e in list(body)[before - (1 if sectPr is not None else 0):] if not e.tag.endswith("sectPr")]
    for e in new:
        body.remove(e)
    return new


def to_pdf(docx_path):
    out = os.path.dirname(docx_path)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", out, docx_path],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return docx_path[:-5] + ".pdf"


def page_map(pdf, builder):
    """Return {anchor: printed page label} by locating each entry's text in the PDF."""
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout).group(1))
    texts = []
    for i in range(1, n + 1):
        t = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", pdf, "-"], capture_output=True, text=True).stdout
        texts.append(re.sub(r"\s+", " ", t))
    # first main page = page whose footer says "Page 1" and contains "Introduction" heading
    start_search = next(i for i, t in enumerate(texts) if "Abbreviations" in t and "Meaning" in t) + 1
    first_main = next(i for i in range(start_search, n) if "Purpose and scope" in texts[i])
    # contents pages end before first page containing "Abbreviations" table
    start_search = next(i for i, t in enumerate(texts) if "Abbreviations" in t and "Meaning" in t) + 1
    res = {}

    def norm(s):
        return re.sub(r"\s+", " ", s).strip()

    entries = [(t, a) for t, a, _ in builder.toc] + builder.tables + builder.figures
    for text, anchor in entries:
        key = norm(text)[:60]
        found = None
        for i in range(start_search, n):
            if key in texts[i]:
                found = i; break
        if found is None:
            # try a shorter key
            key2 = key[:35]
            for i in range(start_search, n):
                if key2 in texts[i]:
                    found = i; break
        if found is None:
            print("WARN: not located:", text)
            continue
        res[anchor] = str(found - first_main + 1)
    return res, n


def stranded_openers(pdf):
    """Section numbers whose opener starts in the lower 45% of a page."""
    import pdfplumber
    out = set()
    with pdfplumber.open(pdf) as pdf_:
        for page in pdf_.pages:
            words = page.extract_words()
            for i, w in enumerate(words[:-1]):
                if w["text"] == "SECTION" and re.fullmatch(r"\d\d", words[i + 1]["text"]):
                    if w["top"] > page.height * 0.55:
                        out.add(int(words[i + 1]["text"]))
    return out


def main():
    out = os.path.join(ROOT, NAME + ".docx")
    pages, breaks = {}, set()
    for it in range(5):
        b = Builder(pages, breaks)
        b.build(out)
        pdf = to_pdf(out)
        new_pages, n = page_map(pdf, b)
        new_breaks = breaks | stranded_openers(pdf)
        stable = new_pages == pages and new_breaks == breaks
        pages, breaks = new_pages, new_breaks
        if stable:
            break
    print("Passes:", it + 1, "| Pages:", n, "| tables:", b.tn, "| figures:", b.fn,
          "| toc entries:", len(b.toc), "| page breaks before sections:", sorted(breaks))


if __name__ == "__main__":
    main()
