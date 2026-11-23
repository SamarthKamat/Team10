"""Shared python-docx helpers: styles, hyperlinks, bookmarks, tables, boxes, page numbers."""
import re
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Cm, RGBColor, Inches

INK = RGBColor(0x1A, 0x1A, 0x1A)
ACCENT = RGBColor(0xE4, 0x57, 0x2E)
BLUE = RGBColor(0x2F, 0x5D, 0x7C)
GREY = RGBColor(0x6B, 0x6B, 0x6B)
LINK = RGBColor(0x1F, 0x4E, 0x79)
HEX_INK, HEX_ACCENT, HEX_BLUE = "1A1A1A", "E4572E", "2F5D7C"
HEX_PALE, HEX_PALE_ACC, HEX_ROW = "F2F2F2", "FBE3DA", "F7F7F7"
FONT = "Calibri"

_bm_id = [100]


def new_document(header_text=None):
    doc = Document()
    sec = doc.sections[0]
    sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
    sec.left_margin = sec.right_margin = Cm(2.3)
    sec.top_margin, sec.bottom_margin = Cm(2.2), Cm(2.0)
    st = doc.styles
    n = st["Normal"]
    n.font.name = FONT
    n.font.size = Pt(10.5)
    n.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    n.paragraph_format.space_after = Pt(6)
    n.paragraph_format.line_spacing = 1.15
    for name, size, color, before, after in [("Heading 1", 20, INK, 18, 8), ("Heading 2", 13.5, BLUE, 14, 5),
                                             ("Heading 3", 11.5, INK, 10, 3), ("Title", 30, INK, 0, 6)]:
        s = st[name]
        s.font.name = FONT
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.italic = False
        s.font.color.rgb = color
        rpr = s.element.get_or_add_rPr()
        rf = rpr.find(qn("w:rFonts"))
        if rf is None:
            rf = OxmlElement("w:rFonts"); rpr.append(rf)
        for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            rf.set(qn(a), FONT)
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if rf.get(qn(a)) is not None:
                del rf.attrib[qn(a)]
        s.paragraph_format.space_before = Pt(before)
        s.paragraph_format.space_after = Pt(after)
        s.paragraph_format.keep_with_next = True
    for lst in ("List Bullet", "List Number"):
        st[lst].font.name = FONT
        st[lst].font.size = Pt(10.5)
        st[lst].paragraph_format.space_after = Pt(3)
    if header_text:
        set_header_footer(sec, header_text)
    return doc


# ---------- low-level XML helpers ----------

def shade(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    for old in tcPr.findall(qn("w:shd")):
        tcPr.remove(old)
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hex_color)
    tcPr.append(shd)


def cell_margins(cell, top=60, bottom=60, left=90, right=90):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for k, v in (("top", top), ("bottom", bottom), ("left", left), ("right", right)):
        e = OxmlElement(f"w:{k}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); mar.append(e)
    tcPr.append(mar)


def table_borders(table, color="BFBFBF", size=4, inside=True, outer=True):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    edges = []
    if outer:
        edges += ["top", "left", "bottom", "right"]
    if inside:
        edges += ["insideH", "insideV"]
    for e in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{e}")
        if e in edges:
            el.set(qn("w:val"), "single"); el.set(qn("w:sz"), str(size)); el.set(qn("w:color"), color)
        else:
            el.set(qn("w:val"), "nil")
        b.append(el)
    tblPr.append(b)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    e = OxmlElement("w:tblHeader"); e.set(qn("w:val"), "true"); trPr.append(e)


def cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    e = OxmlElement("w:cantSplit"); e.set(qn("w:val"), "true"); trPr.append(e)


def add_field(paragraph, instr, size=None, color=None, bold=False):
    r = paragraph.add_run()
    for kind, text in (("begin", None), ("instr", instr), ("separate", None), ("text", "1"), ("end", None)):
        if kind == "instr":
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = text
            r._r.append(it)
        elif kind == "text":
            r2 = paragraph.add_run("1")
            if size: r2.font.size = Pt(size)
            if color: r2.font.color.rgb = color
            r2.bold = bold
            r = paragraph.add_run()
        else:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), kind); r._r.append(fc)
    return paragraph


def add_bookmark(paragraph, name):
    _bm_id[0] += 1
    s = OxmlElement("w:bookmarkStart"); s.set(qn("w:id"), str(_bm_id[0])); s.set(qn("w:name"), name)
    e = OxmlElement("w:bookmarkEnd"); e.set(qn("w:id"), str(_bm_id[0]))
    paragraph._p.insert(0, s) if paragraph._p.pPr is None else paragraph._p.pPr.addnext(s)
    paragraph._p.append(e)


def _hl_run(text, color=LINK, underline=False, bold=False, size=None, italic=False):
    r = OxmlElement("w:r"); rPr = OxmlElement("w:rPr")
    rf = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rf.set(qn(a), FONT)
    rPr.append(rf)
    if bold:
        rPr.append(OxmlElement("w:b"))
    if italic:
        rPr.append(OxmlElement("w:i"))
    c = OxmlElement("w:color"); c.set(qn("w:val"), str(color)); rPr.append(c)
    if underline:
        u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    if size:
        sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rPr.append(sz)
    r.append(rPr)
    t = OxmlElement("w:t"); t.set(qn("xml:space"), "preserve"); t.text = text; r.append(t)
    return r


def add_internal_link(paragraph, text, anchor, **kw):
    h = OxmlElement("w:hyperlink"); h.set(qn("w:anchor"), anchor)
    h.append(_hl_run(text, **kw)); paragraph._p.append(h)


def add_external_link(paragraph, text, url, **kw):
    rid = paragraph.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), rid)
    kw.setdefault("underline", True)
    h.append(_hl_run(text, **kw)); paragraph._p.append(h)


# ---------- rich text ----------
TOKEN = re.compile(r"(\*\*.+?\*\*|\[\[[^\]]+\]\])")


def rich(paragraph, text, refs=None, size=None, color=None, italic=False, bold=False):
    """Write text with **bold** and [[ref;ref]] citations (linked to bookmarks ref_<key>)."""
    for part in TOKEN.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = paragraph.add_run(part[2:-2]); r.bold = True
            if size: r.font.size = Pt(size)
            if color: r.font.color.rgb = color
            r.italic = italic
        elif part.startswith("[[") and refs is not None:
            keys = [k.strip() for k in part[2:-2].split(";")]
            pre = paragraph.add_run(" (" if not paragraph.text.endswith(" ") and paragraph.text else "(")
            if paragraph.runs and paragraph.runs[-2:-1] and False:
                pass
            for i, k in enumerate(keys):
                if k not in refs:
                    raise KeyError(f"Unknown reference key: {k}")
                if i:
                    sep = paragraph.add_run("; ")
                    if size: sep.font.size = Pt(size)
                add_internal_link(paragraph, refs[k][0], "ref_" + k, size=size)
            post = paragraph.add_run(")")
            for r in (pre, post):
                if size: r.font.size = Pt(size)
        else:
            r = paragraph.add_run(part)
            if size: r.font.size = Pt(size)
            if color: r.font.color.rgb = color
            r.italic = italic; r.bold = bold
    _fix_double_space(paragraph)
    return paragraph


def _fix_double_space(p):
    # "text  (" -> "text (" when a citation follows a trailing space
    runs = p._p.findall(qn("w:r"))
    for i, r in enumerate(runs[:-1]):
        t = r.find(qn("w:t"))
        n = runs[i + 1].find(qn("w:t"))
        if t is not None and n is not None and t.text and n.text and t.text.endswith(" ") and n.text.startswith(" ("):
            n.text = n.text[1:]


# ---------- blocks ----------

def para(doc, text="", refs=None, style=None, align=None, size=None, color=None, italic=False, bold=False,
         after=None, before=None, keep=False):
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    if text:
        rich(p, text, refs, size=size, color=color, italic=italic, bold=bold)
    if align == "j":
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    elif align == "c":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "r":
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if after is not None: p.paragraph_format.space_after = Pt(after)
    if before is not None: p.paragraph_format.space_before = Pt(before)
    if keep: p.paragraph_format.keep_with_next = True
    return p


def bullets(doc, items, refs=None, style="List Bullet", size=None):
    for it in items:
        p = doc.add_paragraph(style=style)
        rich(p, it, refs, size=size)
        p.paragraph_format.space_after = Pt(3)


def cell_text(cell, text, refs=None, bold=False, size=9, color=None, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    rich(p, text, refs, size=size, color=color, bold=bold)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    if align == "c":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def table(doc, headers, rows, refs=None, widths=None, size=8.8, header_fill=HEX_INK, total_width_cm=16.4,
          zebra=True, first_col_bold=False):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    table_borders(t, color="D0D0D0", size=4)
    if widths is None:
        widths = [1] * len(headers)
    tot = sum(widths)
    wcm = [total_width_cm * w / tot for w in widths]
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        cell_text(c, h, bold=True, size=size, color=RGBColor(0xFF, 0xFF, 0xFF))
        shade(c, header_fill)
    repeat_header(t.rows[0])
    for r, row in enumerate(rows, start=1):
        cant_split(t.rows[r])
        for i, v in enumerate(row):
            c = t.rows[r].cells[i]
            cell_text(c, str(v), refs, size=size, bold=(first_col_bold and i == 0))
            if zebra and r % 2 == 0:
                shade(c, HEX_ROW)
    for row in t.rows:
        for i, c in enumerate(row.cells):
            c.width = Cm(wcm[i])
            cell_margins(c)
    fix_widths(t, wcm)
    return t


def fix_widths(t, wcm):
    """Fixed layout + grid column widths so Word and LibreOffice honour column sizes."""
    tblPr = t._tbl.tblPr
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    tw = OxmlElement("w:tblW"); tw.set(qn("w:w"), str(int(sum(wcm) * 567))); tw.set(qn("w:type"), "dxa")
    for old in tblPr.findall(qn("w:tblW")):
        tblPr.remove(old)
    tblPr.append(tw)
    for i, col in enumerate(t.columns):
        col.width = Cm(wcm[i])


def box(doc, title, items, refs=None, fill=HEX_PALE_ACC, title_color=ACCENT, numbered=False, size=9.5, width_cm=16.4):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_borders(t, inside=False, outer=False)
    c = t.rows[0].cells[0]
    c.width = Cm(width_cm)
    shade(c, fill)
    cell_margins(c, 120, 120, 180, 180)
    cant_split(t.rows[0])
    # left accent bar
    tcPr = c._tc.get_or_add_tcPr()
    borders = OxmlElement("w:tcBorders")
    l = OxmlElement("w:left"); l.set(qn("w:val"), "single"); l.set(qn("w:sz"), "24"); l.set(qn("w:color"), str(title_color))
    borders.append(l); tcPr.append(borders)
    p = c.paragraphs[0]
    r = p.add_run(title); r.bold = True; r.font.color.rgb = title_color; r.font.size = Pt(size + 0.5)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    for i, it in enumerate(items, 1):
        q = c.add_paragraph()
        rich(q, (f"{i}. " if numbered else "•  ") + it, refs, size=size)
        q.paragraph_format.space_after = Pt(2)
        q.paragraph_format.left_indent = Cm(0.35)
        q.paragraph_format.first_line_indent = Cm(-0.35)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def page_break(doc):
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def set_page_number_format(section, fmt="decimal", start=1):
    sectPr = section._sectPr
    for old in sectPr.findall(qn("w:pgNumType")):
        sectPr.remove(old)
    pg = OxmlElement("w:pgNumType"); pg.set(qn("w:fmt"), fmt); pg.set(qn("w:start"), str(start))
    sectPr.append(pg)


def set_header_footer(section, header_text, page_label="Page "):
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    hp = section.header.paragraphs[0]
    hp.text = ""
    r = hp.add_run(header_text); r.font.size = Pt(8); r.font.color.rgb = GREY
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pPr = hp._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr"); b = OxmlElement("w:bottom")
    b.set(qn("w:val"), "single"); b.set(qn("w:sz"), "4"); b.set(qn("w:color"), "BFBFBF"); b.set(qn("w:space"), "4")
    bdr.append(b); pPr.append(bdr)
    fp = section.footer.paragraphs[0]
    fp.text = ""
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = fp.add_run(page_label); r.font.size = Pt(8.5); r.font.color.rgb = GREY
    add_field(fp, "PAGE", size=8.5, color=GREY)


def clear_header_footer(section):
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    for p in section.header.paragraphs + section.footer.paragraphs:
        p.text = ""


def toc_line(doc, text, anchor, page="00", level=0, size=10, bold=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.left_indent = Cm(0.6 * level)
    pf.space_after = Pt(2 if level else 4)
    pf.tab_stops.add_tab_stop(Cm(16.3), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
    add_internal_link(p, text, anchor, color=INK if bold else RGBColor(0x26, 0x26, 0x26), bold=bold, size=size)
    r = p.add_run("\t")
    add_internal_link(p, str(page), anchor, color=INK, bold=bold, size=size)
    return p


def picture(doc, path, width_cm=15.5):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.space_after = Pt(2)
    p.add_run().add_picture(path, width=Cm(width_cm))
    return p
