// Shared helpers for building the Word deliverables with docx-js
const fs = require('fs');
const d = require('docx');
const {
  Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, ShadingType,
  AlignmentType, ImageRun, BorderStyle, PageBreak, LevelFormat, Footer, Header, PageNumber,
  TableOfContents, VerticalAlign, TabStopType,
} = d;

const C = { red: 'B0161E', brown: '4E342E', esp: '1F1410', cream: 'F4EBDD', gold: 'B8894A', grey: '6F625B', light: 'EFE4D3', white: 'FFFFFF' };
const BODY = 'Calibri', HEAD = 'Cambria';
const CONTENT_W = 9638; // A4 with 1-inch-ish margins (11906 - 2*1134)

// inline markup: **bold**, *italic*
function runs(text, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let last = 0, m;
  while ((m = re.exec(text))) {
    if (m.index > last) out.push(new TextRun({ text: text.slice(last, m.index), ...base }));
    const t = m[0];
    if (t.startsWith('**')) out.push(new TextRun({ text: t.slice(2, -2), bold: true, ...base }));
    else out.push(new TextRun({ text: t.slice(1, -1), italics: true, ...base }));
    last = m.index + t.length;
  }
  if (last < text.length) out.push(new TextRun({ text: text.slice(last), ...base }));
  return out;
}

const H1 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun(t)], pageBreakBefore: false });
const H2 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun(t)] });
const H3 = (t) => new Paragraph({ heading: HeadingLevel.HEADING_3, children: [new TextRun(t)] });
const P = (t, o = {}) => new Paragraph({ children: runs(t, o.run || {}), alignment: o.align || AlignmentType.JUSTIFIED, spacing: { after: 140, line: 288 }, ...(o.para || {}) });
const B = (items, level = 0) => items.map((t) => new Paragraph({ children: runs(t), numbering: { reference: 'bul', level }, spacing: { after: 70, line: 276 } }));
let numInst = 0;
const N = (items) => { numInst++; return items.map((t) => new Paragraph({ children: runs(t), numbering: { reference: 'num', level: 0, instance: numInst }, spacing: { after: 70, line: 276 } })); };
const PB = () => new Paragraph({ children: [new PageBreak()] });
const SP = (n = 120) => new Paragraph({ spacing: { after: n }, children: [] });

function cell(text, w, o = {}) {
  const paras = String(text).split('\n').map((line) => new Paragraph({
    children: runs(line, { size: o.size || 18, color: o.color, bold: o.bold }),
    spacing: { after: 30, line: 252 }, alignment: o.align || AlignmentType.LEFT,
  }));
  return new TableCell({
    width: { size: w, type: WidthType.DXA }, children: paras,
    shading: o.fill ? { type: ShadingType.CLEAR, color: 'auto', fill: o.fill } : undefined,
    margins: { top: 70, bottom: 70, left: 100, right: 100 }, verticalAlign: o.valign || VerticalAlign.TOP,
  });
}
// T(header[], rows[][], widthsFractions[], opts)
function T(header, rows, fr, o = {}) {
  const total = o.width || CONTENT_W;
  const sum = fr.reduce((a, b) => a + b, 0);
  const w = fr.map((f) => Math.floor((f / sum) * total));
  w[w.length - 1] += total - w.reduce((a, b) => a + b, 0);
  const border = { style: BorderStyle.SINGLE, size: 4, color: 'D8CCBE' };
  const borders = { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border };
  const trs = [];
  if (header) trs.push(new TableRow({ tableHeader: true, cantSplit: true, children: header.map((h, i) => cell(h, w[i], { fill: o.headFill || C.brown, color: C.white, bold: true, size: o.size || 18 })) }));
  rows.forEach((r, ri) => trs.push(new TableRow({ cantSplit: true, children: r.map((c, i) => cell(c, w[i], { fill: (o.firstColFill && i === 0) ? C.light : (ri % 2 ? 'FBF7F1' : undefined), bold: o.firstColBold && i === 0, size: o.size || 18 })) })));
  return new Table({ width: { size: total, type: WidthType.DXA }, columnWidths: w, rows: trs, borders });
}
let figN = 0, tabN = 0;
function caption(kind, text) {
  const n = kind === 'Figure' ? ++figN : ++tabN;
  return new Paragraph({ alignment: AlignmentType.LEFT, spacing: { before: 60, after: 200 }, keepLines: true,
    children: [new TextRun({ text: `${kind} ${n}. `, bold: true, size: 18, color: C.red }), ...runs(text, { size: 18, color: C.grey, italics: false })] });
}
function tableTitle(text) { // caption ABOVE a table
  const n = ++tabN;
  return new Paragraph({ keepNext: true, spacing: { before: 160, after: 80 }, children: [new TextRun({ text: `Table ${n}. `, bold: true, size: 19, color: C.red }), new TextRun({ text, bold: true, size: 19, color: C.esp })] });
}
function F(path, wIn, capText) {
  const buf = fs.readFileSync(path);
  const { w: pw, h: ph } = imgSize(buf);
  const wpx = wIn * 96, hpx = wpx * ph / pw;
  const type = path.endsWith('.png') ? 'png' : 'jpg';
  return [new Paragraph({ alignment: AlignmentType.CENTER, keepNext: true, spacing: { before: 120, after: 40 }, children: [new ImageRun({ type, data: buf, transformation: { width: wpx, height: hpx }, altText: { title: capText.slice(0, 60), description: capText, name: path.split('/').pop() } })] }), caption('Figure', capText)];
}
function imgSize(buf) {
  if (buf[0] === 0x89) return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) };
  let i = 2; while (i < buf.length) { const m = buf[i + 1]; const len = buf.readUInt16BE(i + 2); if (m >= 0xC0 && m <= 0xCF && m !== 0xC4 && m !== 0xC8 && m !== 0xCC) return { h: buf.readUInt16BE(i + 5), w: buf.readUInt16BE(i + 7) }; i += 2 + len; }
  throw new Error('size');
}
// shaded callout box (single-cell table)
function NOTE(title, lines, fill = C.cream, accent = C.red) {
  const kids = [];
  if (title) kids.push(new Paragraph({ spacing: { after: 60 }, children: [new TextRun({ text: title, bold: true, color: accent, size: 20 })] }));
  lines.forEach((l) => kids.push(new Paragraph({ spacing: { after: 50, line: 264 }, children: runs(l, { size: 19 }) })));
  const nb = { style: BorderStyle.NONE, size: 0, color: 'FFFFFF' };
  return new Table({ width: { size: CONTENT_W, type: WidthType.DXA }, columnWidths: [CONTENT_W], borders: { top: nb, bottom: nb, left: nb, right: nb, insideHorizontal: nb, insideVertical: nb },
    rows: [new TableRow({ cantSplit: true, children: [new TableCell({ width: { size: CONTENT_W, type: WidthType.DXA }, shading: { type: ShadingType.CLEAR, color: 'auto', fill }, margins: { top: 140, bottom: 140, left: 200, right: 200 }, children: kids })] })] });
}

const styles = {
  default: { document: { run: { font: BODY, size: 22, color: '231A16' } } },
  paragraphStyles: [
    { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HEAD, size: 34, bold: true, color: C.red }, paragraph: { spacing: { before: 360, after: 160 }, keepNext: true, outlineLevel: 0, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: C.gold, space: 4 } } } },
    { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: HEAD, size: 26, bold: true, color: C.brown }, paragraph: { spacing: { before: 240, after: 100 }, keepNext: true, outlineLevel: 1 } },
    { id: 'Heading3', name: 'Heading 3', basedOn: 'Normal', next: 'Normal', quickFormat: true, run: { font: BODY, size: 23, bold: true, color: C.esp }, paragraph: { spacing: { before: 180, after: 80 }, keepNext: true, outlineLevel: 2 } },
    { id: 'Title', name: 'Title', basedOn: 'Normal', run: { font: HEAD, size: 52, bold: true, color: C.red }, paragraph: { spacing: { before: 0, after: 120 } } },
  ],
};
const numbering = { config: [
  { reference: 'bul', levels: [
    { level: 0, format: LevelFormat.BULLET, text: '▪', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 260 } }, run: { color: C.red } } },
    { level: 1, format: LevelFormat.BULLET, text: '–', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 900, hanging: 260 } } } }] },
  { reference: 'num', levels: [{ level: 0, format: LevelFormat.DECIMAL, text: '%1.', alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 300 } } } }] },
] };

function headerFooter(leftText) {
  return {
    headers: { default: new Header({ children: [new Paragraph({ tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }], border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'D8CCBE', space: 4 } }, children: [new TextRun({ text: leftText, size: 16, color: C.grey }), new TextRun({ text: '\tFoundation of Marketing · GIM · PGDM BDA 2026–28', size: 16, color: C.grey })] })] }) },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: 'Page ', size: 16, color: C.grey }), new TextRun({ children: [PageNumber.CURRENT], size: 16, color: C.grey }), new TextRun({ text: ' of ', size: 16, color: C.grey }), new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: C.grey })] })] }) },
  };
}
const page = { size: { width: 11906, height: 16838 }, margin: { top: 1134, bottom: 1134, left: 1134, right: 1134, header: 600, footer: 600 } };

module.exports = { d, C, runs, H1, H2, H3, P, B, N, PB, SP, T, F, NOTE, caption, tableTitle, styles, numbering, headerFooter, page, CONTENT_W, TableOfContents, Paragraph, TextRun, AlignmentType, ImageRun, imgSize };
