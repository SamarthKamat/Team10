const pptxgen = require('pptxgenjs');
const React = require('react');
const RDS = require('react-dom/server');
const sharp = require('sharp');
const fa = require('react-icons/fa');
const { applyTheme } = require('/root/.claude/skills/synced/cff2045a-f96c-4f39-86fc-35834c3b1a34_ef085de5-0aae-4361-a659-3a850e7822ec/pptx/scripts/apply_theme.js');

const THEME = { name: 'NESCAFE Classic Study', headFontFace: 'Cambria', bodyFontFace: 'Calibri',
  colors: { dk1: '1F1410', lt1: 'FFFFFF', dk2: '4E342E', lt2: 'F4EBDD', accent1: 'B0161E', accent2: 'B8894A', accent3: '4E342E', accent4: '7E0F15', accent5: '8C7B70', accent6: 'D9C7B0', hlink: 'B0161E', folHlink: '7E0F15' } };
const H = { red: 'B0161E', esp: '1F1410', brown: '4E342E', cream: 'F4EBDD', gold: 'B8894A', grey: '6F625B', white: 'FFFFFF', light: 'EFE4D3', pale: 'FAF6F0' };
const IMG = 'img/', FIG = 'fig/';

async function icon(Comp, color = '#FFFFFF', size = 256) {
  const svg = RDS.renderToStaticMarkup(React.createElement(Comp, { color, size }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return 'image/png;base64,' + buf.toString('base64');
}

(async () => {
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE'; // 13.33 x 7.5
  pres.title = 'NESCAFÉ Classic in India — Marketing Analysis';
  pres.author = 'PGDM BDA Student, GIM';
  pres.theme = { headFontFace: 'Cambria', bodyFontFace: 'Calibri' };
  const C = pres.SchemeColor;

  pres.defineSlideMaster({ title: 'CONTENT', background: { color: 'FFFFFF' },
    objects: [
      { placeholder: { options: { name: 'title', type: 'title', x: 0.6, y: 0.35, w: 12.1, h: 0.8, fontFace: 'Cambria', fontSize: 28, bold: true, color: H.esp, valign: 'middle', align: 'left', margin: 0 }, text: '' } },
      { text: { text: 'NESCAFÉ Classic · Foundation of Marketing · GIM', options: { x: 0.6, y: 7.08, w: 6, h: 0.3, fontSize: 9, color: H.grey, margin: 0 } } },
    ],
    slideNumber: { x: 12.3, y: 7.08, w: 0.5, h: 0.3, fontSize: 9, color: H.grey, align: 'right' } });
  pres.defineSlideMaster({ title: 'DARK', background: { color: H.esp }, objects: [], slideNumber: { x: 12.3, y: 7.08, w: 0.5, h: 0.3, fontSize: 9, color: 'BFAFA3', align: 'right' } });

  const addS = (sec) => pres.addSlide({ masterName: 'CONTENT', sectionTitle: sec });
  const title = (s, t) => s.addText(t, { placeholder: 'title' });
  const kicker = (s, t) => s.addText(t, { x: 0.6, y: 1.12, w: 12.1, h: 0.4, fontSize: 15, italic: true, color: H.red, margin: 0, isTextBox: true });
  const src = (s, t) => s.addText('Source: ' + t, { x: 0.6, y: 6.72, w: 12.1, h: 0.32, fontSize: 9, color: H.grey, margin: 0, isTextBox: true, valign: 'top' });
  const card = (s, x, y, w, h, fill = H.pale) => s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.08, fill: { color: fill }, line: { color: fill } });
  const circleIcon = async (s, Comp, x, y, d = 0.6, bg = H.red) => {
    s.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: bg }, line: { color: bg } });
    s.addImage({ data: await icon(Comp), x: x + d * 0.22, y: y + d * 0.22, w: d * 0.56, h: d * 0.56 });
  };
  const chartTxt = { catAxisLabelColor: H.grey, valAxisLabelColor: H.grey, catAxisLabelFontFace: '+mn-lt', valAxisLabelFontFace: '+mn-lt', dataLabelFontFace: '+mn-lt', catAxisLabelFontSize: 11, valAxisLabelFontSize: 10, dataLabelFontSize: 12, dataLabelColor: H.esp, titleFontFace: '+mn-lt' };

  // ---------- 1 COVER ----------
  pres.addSection({ title: 'Introduction' });
  let s = pres.addSlide({ masterName: 'DARK', sectionTitle: 'Introduction' });
  s.addImage({ path: IMG + 'beans.jpg', x: 0, y: 0, w: 13.333, h: 7.5, sizing: { type: 'cover', w: 13.333, h: 7.5 } });
  s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 13.333, h: 7.5, fill: { color: H.esp, transparency: 25 }, line: { color: H.esp, transparency: 100 } });
  s.addText('FOUNDATION OF MARKETING · ASSIGNMENT & VIVA', { x: 0.8, y: 1.1, w: 9, h: 0.4, fontSize: 14, color: 'E8D6BE', bold: true, charSpacing: 3, margin: 0, isTextBox: true });
  s.addText('NESCAFÉ Classic in India', { x: 0.8, y: 1.65, w: 11, h: 1.2, fontFace: 'Cambria', fontSize: 54, bold: true, color: H.white, margin: 0, isTextBox: true });
  s.addText('Consumer Behaviour, STP, Competitive Positioning & Marketing Strategy', { x: 0.8, y: 2.85, w: 11, h: 0.6, fontSize: 22, italic: true, color: 'E8D6BE', margin: 0, isTextBox: true });
  s.addText([
    { text: 'Presented by: [Student Name]', options: { breakLine: true } },
    { text: 'Term II · PGDM Big Data Analytics 2026–28 · Goa Institute of Management', options: { breakLine: true } },
    { text: 'Faculty: Prof. Shantanu Prasad' }], { x: 0.8, y: 4.6, w: 8, h: 1.3, fontSize: 16, color: H.white, margin: 0, paraSpaceAfter: 4, isTextBox: true });
  s.addText('Photo: A S M Jobaer, Wikimedia Commons, CC BY-SA 4.0. Independent student work; not affiliated with Nestlé.', { x: 0.8, y: 6.9, w: 10, h: 0.3, fontSize: 9, color: 'BFAFA3', margin: 0, isTextBox: true });
  s.addNotes('Introduce yourself and the product. Key message: NESCAFÉ Classic is the entry point into coffee for millions of young Indians — this deck tests whether its STP and 4Ps fit together.');

  // ---------- 2 COMPANY & PRODUCT ----------
  s = addS('Introduction'); title(s, 'From Nestlé to NESCAFÉ Classic: three levels of the brand');
  kicker(s, 'Classic is the flagship, 100% pure “everyday real coffee” of India’s coffee-category leader');
  s.addImage({ path: IMG + 'nescafe_classic.jpg', x: 0.6, y: 1.7, w: 3.4, h: 4.85, sizing: { type: 'cover', w: 3.4, h: 4.85 } });
  const lv = [
    [fa.FaGlobe, 'Company — Nestlé India', 'In India since 1912; incorporated 1959; first factory at Moga (1961). Portfolio spans dairy & nutrition, MAGGI, confectionery and beverages.'],
    [fa.FaMugHot, 'Brand — NESCAFÉ', 'Launched 1938 in Switzerland. In India: soluble coffees, ready-to-drink cold coffee and out-of-home vending via Nestlé Professional.'],
    [fa.FaStar, 'Product — NESCAFÉ Classic', '100% pure instant coffee with a strong aroma; jars of 24/45/90 g plus pouches and single-serve sachets.'],
  ];
  for (let i = 0; i < 3; i++) {
    const y = 1.7 + i * 1.32; card(s, 4.35, y, 8.35, 1.15);
    await circleIcon(s, lv[i][0], 4.55, y + 0.27, 0.6, [H.esp, H.brown, H.red][i]);
    s.addText(lv[i][1], { x: 5.35, y: y + 0.1, w: 7.2, h: 0.38, fontSize: 17, bold: true, color: H.esp, margin: 0, isTextBox: true });
    s.addText(lv[i][2], { x: 5.35, y: y + 0.48, w: 7.2, h: 0.62, fontSize: 13.5, color: H.brown, margin: 0, isTextBox: true, valign: 'top' });
  }
  s.addText([{ text: 'Value proposition: ', options: { bold: true, color: H.red } }, { text: 'real-coffee kick in seconds, from a sachet to a family jar, from India’s most available coffee brand.', options: { color: H.esp } }],
    { x: 4.35, y: 5.75, w: 8.35, h: 0.75, fontSize: 15, italic: true, margin: 0, isTextBox: true, valign: 'middle' });
  src(s, 'Nestlé India (n.d.), At a glance; Wikipedia (2026), Nescafé; NESCAFÉ India (n.d.), Classic product page. Photo: Marwan Bello, Wikimedia Commons, CC BY-SA 4.0.');
  s.addNotes('Separate company, brand and product. Classic is the recruitment SKU — the first jar most households buy.');

  // ---------- 3 RECENT DEVELOPMENTS ----------
  pres.addSection({ title: 'Market' });
  s = addS('Market'); title(s, 'Recent developments: volume-led growth, youth, quick commerce');
  kicker(s, 'Nestlé is investing behind NESCAFÉ while coffee input costs stay high');
  s.addChart(pres.charts.BAR, [{ name: 'Total sales growth y-o-y (%)', labels: ['Q4 FY25', 'Q4 FY26', 'Q1 FY27', 'Q2 FY27'], values: [3.7, 23.4, 25.4, 20.5] }], {
    x: 0.6, y: 1.65, w: 5.4, h: 4.6, barDir: 'col', chartColors: ['D9C7B0', H.gold, H.red, H.red], invertedColors: [], showValue: true, dataLabelPosition: 'outEnd', dataLabelFormatCode: '0.0"%"',
    showTitle: true, title: 'Nestlé India — total sales growth, y-o-y (%)', titleFontSize: 13, titleColor: H.esp, showLegend: false, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, valAxisMaxVal: 30, barGapWidthPct: 60, ...chartTxt });
  const ev = [
    ['2025', 'RTD cold coffee range: Iced Latte & Frappé ₹50/170 ml; launched with gaming streamers', 'Brand extension into Gen Z occasions'],
    ['2025–26', '“Make Your World” (McCann): rap jingle for Gen Z; first-day-of-college story', 'Targets the habit-forming moment'],
    ['FY26', 'Classic drives household recruitment with renewed communication', 'Classic = entry SKU of the franchise'],
    ['Q1–Q2 FY27', 'Volume-led growth in Classic & Sunrise; ad spend +46%; quick commerce a key driver', 'Share of voice + digital shelf'],
    ['Dec 2025', 'HUL relaunches BRU Gold with Sara Ali Khan & Aditya Roy Kapur', 'Premium-instant competition rises'],
  ];
  ev.forEach((e, i) => {
    const y = 1.65 + i * 0.95;
    s.addShape(pres.shapes.OVAL, { x: 6.45, y: y + 0.22, w: 0.22, h: 0.22, fill: { color: H.red }, line: { color: H.red } });
    if (i < 4) s.addShape(pres.shapes.LINE, { x: 6.56, y: y + 0.44, w: 0, h: 0.73, line: { color: 'D9C7B0', width: 1.5 } });
    s.addText(e[0], { x: 6.85, y: y + 0.08, w: 1.25, h: 0.5, fontSize: 13, bold: true, color: H.red, margin: 0, isTextBox: true, valign: 'top' });
    s.addText([{ text: e[1], options: { color: H.esp, breakLine: true } }, { text: '→ ' + e[2], options: { color: H.gold, italic: true, bold: true } }], { x: 8.1, y: y + 0.03, w: 4.6, h: 0.9, fontSize: 12, margin: 0, isTextBox: true, valign: 'top' });
  });
  src(s, 'Business Standard (2025); Ventura Securities (2026); Nestlé India (2026a, 2026b); BusinessWorld (2026); BestMediaInfo (2026); Indian Retailer (2025); afaqs! (2025b); Manifest Media (2026); Financial Express (2025).');
  s.addNotes('Growth is volume-led, not just price — more households and more cups. Ad spend up 46% in Q2 FY27 shows Nestlé is pressing its advantage.');

  // ---------- 4 INDUSTRY ----------
  s = addS('Market'); title(s, 'Industry: a small, home-centric market that youth are opening up');
  kicker(s, 'Low consumption + rising youth adoption + new channels = headroom for an accessible pure coffee');
  const stats = [['91,000 t', 'domestic coffee consumption in 2023, up from 84,000 t in 2012'], ['~50%', 'of Indians drink coffee — mostly at home'], ['0.2%', 'cold coffee’s share of a ₹1 trillion cold-beverage market — tiny base, ~23% CAGR in RTD']];
  stats.forEach((t, i) => { const x = 0.6 + i * 2.65; card(s, x, 1.7, 2.45, 2.2, i === 2 ? H.esp : H.pale);
    s.addText(t[0], { x: x + 0.15, y: 1.8, w: 2.15, h: 0.9, fontFace: 'Cambria', fontSize: 36, bold: true, color: i === 2 ? H.white : H.red, margin: 0, isTextBox: true });
    s.addText(t[1], { x: x + 0.15, y: 2.7, w: 2.15, h: 1.1, fontSize: 12.5, color: i === 2 ? 'E8D6BE' : H.brown, margin: 0, isTextBox: true, valign: 'top' }); });
  s.addChart(pres.charts.BAR, [{ name: 'E-com share of FMCG sales', labels: ['Urban India', 'All metros', 'Top-8 metros'], values: [6, 14, 18] }], {
    x: 8.7, y: 1.6, w: 4.1, h: 2.5, barDir: 'bar', chartColors: ['D9C7B0', H.gold, H.red], showValue: true, dataLabelPosition: 'outEnd', dataLabelFormatCode: '0"%"', showTitle: true, title: 'E-com incl. quick commerce, Oct–Dec 2025', titleFontSize: 11, titleColor: H.esp,
    showLegend: false, valAxisHidden: true, valGridLine: { style: 'none' }, catGridLine: { style: 'none' }, valAxisMaxVal: 24, catAxisOrientation: 'maxMin', barGapWidthPct: 50, ...chartTxt });
  const oc = [['Opportunities', ['Low per-capita consumption = headroom', 'Gen Z cafés & cold coffee year-round', 'Quick commerce enables trial bundles', 'North & West India now the growth engines'], H.brown], ['Challenges', ['Tea’s cultural dominance and low cost', 'Coffee input-cost inflation → price action', 'Premium/D2C instants erode “real coffee” edge', 'Price-led switching to chicory blends'], H.red]];
  oc.forEach((o, i) => { const x = 0.6 + i * 6.15; card(s, x, 4.2, 5.95, 2.35, 'FFFFFF');
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 4.2, w: 5.95, h: 2.35, rectRadius: 0.08, fill: { color: 'FFFFFF' }, line: { color: 'D9C7B0', width: 1 } });
    s.addText(o[0], { x: x + 0.25, y: 4.3, w: 5.5, h: 0.45, fontSize: 17, bold: true, color: o[2], margin: 0, isTextBox: true });
    s.addText(o[1].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < 3 } })), { x: x + 0.25, y: 4.8, w: 5.5, h: 1.65, fontSize: 14, color: H.esp, margin: 0, paraSpaceAfter: 4, isTextBox: true, valign: 'top' }); });
  src(s, 'Mintel (2025) citing Coffee Board data; afaqs! (2025a) citing NielsenIQ; Daily Pioneer (2026) citing NielsenIQ; afaqs! (2025c); Reuters via Yahoo Finance (2025).');
  s.addNotes('Coffee is still small next to tea. The opportunity is creating new drinkers. Quick commerce already accounts for most online FMCG sales in metros.');

  // ---------- 5 COMPETITORS ----------
  s = addS('Market'); title(s, 'Competitors: squeezed between value blends and premium instants');
  kicker(s, 'Differentiation = 100% pure coffee + youthful brand + everywhere availability');
  const hdr = (t) => ({ text: t, options: { bold: true, color: 'FFFFFF', fill: { color: H.brown }, fontSize: 12.5 } });
  const rc = (t, b) => ({ text: t, options: { fontSize: 11.5, color: H.esp, bold: !!b, fill: { color: b ? H.light : 'FFFFFF' } } });
  const rows = [
    [hdr(''), hdr('NESCAFÉ Classic'), hdr('BRU Instant / Gold (HUL)'), hdr('Tata Coffee Grand / Premium'), hdr('Continental Xtra / Speciale (CCL)')],
    ['Product', '100% pure instant; strong aroma', 'Instant: coffee–chicory blend; Gold: pure', 'Powder + decoction crystals; Premium: 100% coffee', 'Xtra 70:30 coffee–chicory; Speciale 100% pure'],
    ['Price tier*', 'Mid / accessible premium', 'Value (Instant); premium (Gold)', 'Value–mid; mid (Premium)', 'Value–mid'],
    ['Target', 'Young adults, students, urban homes', 'Mass homes; strong in South', 'Authenticity seekers', 'Price-conscious homes'],
    ['Image & comms', 'Youthful ambition; “Make Your World”', 'Heritage; Gold relaunch with film stars', 'Plantation heritage; ASMR crystals', 'Value; low ad presence'],
    ['Strength', 'Leadership, reach, youth relevance', 'Distribution depth, blend taste', 'Distinct format, Tata trust', 'Manufacturing scale'],
    ['Weakness', 'Pricier than blends', 'Ageing image', 'Smaller scale', 'Low salience'],
  ].map((r, i) => i === 0 ? r : r.map((c, j) => rc(c, j === 0)));
  s.addTable(rows, { x: 0.6, y: 1.65, w: 12.1, colW: [1.6, 2.6, 2.6, 2.65, 2.65], rowH: 0.62, border: { type: 'solid', pt: 0.75, color: 'D9C7B0' }, valign: 'middle', margin: 0.06 });
  s.addText('*Relative tier inferred from product type and communication — not verified shelf prices.', { x: 0.6, y: 6.35, w: 12.1, h: 0.3, fontSize: 10, italic: true, color: H.grey, margin: 0, isTextBox: true });
  src(s, 'NESCAFÉ India (n.d.); Tata Consumer Products (n.d.); Adgully (2023); CCL Products (2021); Financial Express (2025).');
  s.addNotes('Threat from below: chicory blends are cheaper and match South-Indian taste. Threat from above: BRU Gold, Tata Grand Premium, D2C specialty instants.');

  // ---------- 6 SEGMENTATION ----------
  pres.addSection({ title: 'STP' });
  s = addS('STP'); title(s, 'Segmentation: four bases, five candidate segments');
  kicker(s, 'Behaviour (first-time trier vs loyal; occasion) is the most actionable base for Classic');
  const bases = [[fa.FaUserFriends, 'Demographic', 'Age 18–35; students & young professionals; life stage'], [fa.FaMapMarkerAlt, 'Geographic', 'North/West growth vs South chicory preference; metro vs Tier-2/3'], [fa.FaBrain, 'Psychographic', 'Self-made achievers; café aspirers; convenience seekers'], [fa.FaSyncAlt, 'Behavioural', 'Occasion (study, work, cold-coffee treat); trier vs loyal; benefit sought']];
  for (let i = 0; i < 4; i++) { const x = 0.6 + (i % 2) * 3.05, y = 1.7 + Math.floor(i / 2) * 2.45; card(s, x, y, 2.85, 2.25);
    await circleIcon(s, bases[i][0], x + 0.2, y + 0.2, 0.62, [H.red, H.brown, H.esp, H.gold][i]);
    s.addText(bases[i][1], { x: x + 0.2, y: y + 0.95, w: 2.5, h: 0.4, fontSize: 16, bold: true, color: H.esp, margin: 0, isTextBox: true });
    s.addText(bases[i][2], { x: x + 0.2, y: y + 1.35, w: 2.5, h: 0.85, fontSize: 12.5, color: H.brown, margin: 0, isTextBox: true, valign: 'top' }); }
  const segs = [['Aspiring Starters', '18–24 students & hostellers; price-aware; digital natives', H.red], ['Hustling Professionals', '22–35; WFH/office; energy & focus; quick-commerce buyers', H.red], ['Family Buyers', 'Value, trust, hot & cold coffee for the home', H.brown], ['Café-Culture Upgraders', 'Urban 20–35; may trade up to specialty', H.gold], ['South-Indian Tradition Seekers', 'Prefer chicory/filter taste → Sunrise', H.grey]];
  s.addText('Candidate segments (to validate in interviews)', { x: 6.95, y: 1.65, w: 5.75, h: 0.4, fontSize: 15, bold: true, color: H.esp, margin: 0, isTextBox: true });
  segs.forEach((g, i) => { const y = 2.12 + i * 0.88; s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 6.95, y, w: 0.12, h: 0.7, rectRadius: 0.03, fill: { color: g[2] }, line: { color: g[2] } });
    s.addText([{ text: g[0], options: { bold: true, color: H.esp, breakLine: true, fontSize: 14.5 } }, { text: g[1], options: { color: H.brown, fontSize: 12.5 } }], { x: 7.2, y, w: 5.5, h: 0.75, margin: 0, isTextBox: true, valign: 'middle' }); });
  src(s, 'Analyst synthesis using afaqs! (2025a, 2025b, 2025c) and Manifest Media (2026). Segments are analytical assumptions.');
  s.addNotes('Explain each base with one example. The five segments are my hypotheses — the interviews will test them.');

  // ---------- 7 TARGETING ----------
  s = addS('STP'); title(s, 'Targeting: young starters first, family buyers second');
  kicker(s, 'Portfolio-level differentiated targeting — Sunrise (value), Classic (mainstream youth), Gold (premium), RTD (on-the-go)');
  s.addImage({ path: IMG + 'friends.jpg', x: 0.6, y: 1.7, w: 4.0, h: 2.35, sizing: { type: 'cover', w: 4.0, h: 2.35 } });
  s.addImage({ path: IMG + 'pro_woman.jpg', x: 0.6, y: 4.2, w: 4.0, h: 2.35, sizing: { type: 'cover', w: 4.0, h: 2.35 } });
  const tg = [['PRIMARY · Aspiring Starters & young Hustlers (18–30)', [['Needs', 'Energy for study/work; affordable real coffee'], ['Lifestyle', 'Hostels, PGs, shared flats; social-media heavy'], ['Buying', 'Small jars, sachets, quick-commerce top-ups'], ['Motivation', 'Ambition, independence, “my ritual”']], H.red],
    ['SECONDARY · Urban family buyers & first-time triers', [['Needs', 'Reliable taste, value, hot & cold versatility'], ['Lifestyle', 'Mixed tea/coffee households'], ['Buying', 'Larger jars/pouches; kirana & supermarket'], ['Motivation', 'Family enjoyment, hospitality, value']], H.brown]];
  tg.forEach((t, i) => { const y = 1.7 + i * 2.5; card(s, 4.85, y, 7.85, 2.35);
    s.addText(t[0], { x: 5.05, y: y + 0.12, w: 7.5, h: 0.4, fontSize: 15, bold: true, color: t[2], margin: 0, isTextBox: true });
    t[1].forEach((r, k) => { const xx = 5.05 + (k % 2) * 3.8, yy = y + 0.65 + Math.floor(k / 2) * 0.82;
      s.addText([{ text: r[0], options: { bold: true, color: H.esp, breakLine: true } }, { text: r[1], options: { color: H.brown } }], { x: xx, y: yy, w: 3.6, h: 0.78, fontSize: 12.5, margin: 0, isTextBox: true, valign: 'top' }); }); });
  src(s, 'Analysis based on afaqs! (2025b), Manifest Media (2026), Nestlé India (2026a). Photos: Nathan Dumlao (CC0); Shixart1985 (CC BY 2.0), Wikimedia Commons.');
  s.addNotes('Why youth first: coffee habits form at life-stage transitions such as starting college or a first job. The current campaign is built for exactly that moment.');

  // ---------- 8 POSITIONING ----------
  s = addS('STP'); title(s, 'Positioning: the accessible “real coffee” for every new beginning');
  kicker(s, 'Upper-middle of the map — a defendable space, but crowded by BRU Gold and Tata Grand Premium');
  s.addImage({ path: FIG + 'fig_perceptual_map.png', x: 0.6, y: 1.6, w: 5.75, h: 4.55 });
  s.addText('Illustrative map: positions are analyst judgement from product type & communication — not survey data.', { x: 0.6, y: 6.2, w: 5.75, h: 0.45, fontSize: 10, italic: true, color: H.grey, margin: 0, isTextBox: true });
  card(s, 6.75, 1.65, 5.95, 2.05, H.esp);
  s.addText([{ text: 'Positioning statement (proposed)', options: { bold: true, color: H.gold, breakLine: true, fontSize: 13 } },
    { text: 'For young Indians starting something new, NESCAFÉ Classic is the 100% pure instant coffee that turns every ambition into a ready-in-seconds ritual — with the trust and reach of India’s leading coffee brand.', options: { color: H.white, fontSize: 14.5, italic: true } }], { x: 6.95, y: 1.75, w: 5.6, h: 1.85, margin: 0, isTextBox: true, valign: 'middle' });
  const pb = [['Functional', 'Quick prep · energy · aroma · hot, beaten or cold'], ['Emotional', 'Confidence, independence, a personal ritual'], ['Perceived value', 'Above blends, below premium; sachets = low-risk trial'], ['Associations', 'Red mug & cap · four-note jingle · college · mornings']];
  pb.forEach((p, i) => { const y = 3.9 + i * 0.68; s.addText([{ text: p[0] + '  ', options: { bold: true, color: H.red } }, { text: p[1], options: { color: H.esp } }], { x: 6.75, y, w: 5.95, h: 0.6, fontSize: 13.5, margin: 0, isTextBox: true, valign: 'middle' }); });
  src(s, 'Analyst synthesis; exchange4media (2014); Manifest Media (2026); NESCAFÉ India (n.d.).');
  s.addNotes('Read the map: x = price tier, y = perceived coffee quality. Classic is not the cheapest or the most premium — it owns accessible quality.');

  // ---------- 9 PRODUCT ----------
  pres.addSection({ title: 'Marketing Mix' });
  s = addS('Marketing Mix'); title(s, 'Product strategy: a good–better–best ladder, Classic at the centre');
  kicker(s, 'Keep scopes separate: mix width (company) → line length (NESCAFÉ) → depth (Classic)');
  const rings = [[2.75, H.cream], [2.0, 'D9C7B0'], [1.15, H.red]];
  rings.forEach(([d, c]) => { const cx = 3.45, cy = 4.0; s.addShape(pres.shapes.OVAL, { x: cx - d, y: cy - d * 0.82, w: d * 2, h: d * 1.64, fill: { color: c }, line: { color: 'FFFFFF', width: 2 } }); });
  s.addText([{ text: 'CORE', options: { bold: true, breakLine: true } }, { text: 'Energy & coffee pleasure', options: { fontSize: 11 } }], { x: 2.4, y: 3.45, w: 2.1, h: 1.1, fontSize: 15, color: H.white, align: 'center', valign: 'middle', margin: 0, isTextBox: true });
  s.addText([{ text: 'ACTUAL  ', options: { bold: true } }, { text: '100% pure · aroma · red-cap jar, pouch, sachet', options: {} }], { x: 1.55, y: 2.55, w: 3.8, h: 0.5, fontSize: 11, color: H.esp, align: 'center', margin: 0, isTextBox: true });
  s.addText([{ text: 'AUGMENTED  ', options: { bold: true } }, { text: 'recipes · reach · Nestlé QA · vending', options: {} }], { x: 0.95, y: 5.85, w: 5.0, h: 0.4, fontSize: 11, color: H.brown, align: 'center', margin: 0, isTextBox: true });
  const pm = [['Mix width — Nestlé India', 'Dairy & nutrition · MAGGI prepared foods · confectionery · NESCAFÉ beverages'], ['Line length — NESCAFÉ', 'Classic · Sunrise (coffee–chicory) · Gold (premium) · RTD cold coffee · Professional vending'], ['Depth — Classic', 'Jars 24/45/90 g · pouches & refills · 1.5 g sachets/strips · e-com multipacks'], ['Extensions & changes', 'Classic → RTD “Classic Latte” can (2025); renewed campaign (2025–26); no reformulation found']];
  pm.forEach((p, i) => { const y = 1.7 + i * 1.18; card(s, 6.75, y, 5.95, 1.05);
    s.addText([{ text: p[0], options: { bold: true, color: H.red, breakLine: true, fontSize: 14.5 } }, { text: p[1], options: { color: H.esp, fontSize: 12.5 } }], { x: 6.95, y: y + 0.05, w: 5.6, h: 0.95, margin: 0, isTextBox: true, valign: 'middle' }); });
  src(s, 'Nestlé India (n.d.); NESCAFÉ India (n.d.); Indian Retailer (2025); Kotler et al. (2022) for product-level concepts.');
  s.addNotes('Width = how many lines Nestlé India has; length = items in the NESCAFÉ line; depth = variants of Classic. Sunrise and Gold catch switchers below and above.');

  // ---------- 10 BRANDING ----------
  s = addS('Marketing Mix'); title(s, 'Branding & communication: one youth platform, consistently told');
  kicker(s, 'Message, media, personality and segment all point at 18–30 “starters” — strong synergy');
  const camp = [['2014', '“It All Starts with a NESCAFÉ” · #ItAllStarts'], ['2023', '“Jo Banaye, Special Ban Jaaye” — easy Classic cold coffee'], ['2025', 'Gaming streamers launch RTD cold coffee'], ['2025–26', '“Make Your World” — Gen Z rap jingle; first day of college']];
  s.addShape(pres.shapes.LINE, { x: 0.9, y: 2.35, w: 11.5, h: 0, line: { color: 'D9C7B0', width: 2 } });
  camp.forEach((c, i) => { const x = 0.6 + i * 3.05; s.addShape(pres.shapes.OVAL, { x: x + 0.2, y: 2.2, w: 0.3, h: 0.3, fill: { color: H.red }, line: { color: 'FFFFFF', width: 2 } });
    s.addText(c[0], { x, y: 1.65, w: 2.8, h: 0.45, fontSize: 17, bold: true, color: H.red, margin: 0, isTextBox: true });
    s.addText(c[1], { x, y: 2.65, w: 2.85, h: 0.85, fontSize: 13, color: H.esp, margin: 0, isTextBox: true, valign: 'top' }); });
  const syn = [[fa.FaBullhorn, 'Message', 'Ambition, new beginnings'], [fa.FaMobileAlt, 'Media', 'YouTube, Instagram, gaming streams, QC retail media'], [fa.FaSmile, 'Personality', 'Young, energetic, dependable'], [fa.FaUsers, 'Segment', 'Students & young professionals']];
  for (let i = 0; i < 4; i++) { const x = 0.6 + i * 3.05; card(s, x, 3.75, 2.85, 1.65);
    await circleIcon(s, syn[i][0], x + 0.18, 3.92, 0.55, H.brown);
    s.addText(syn[i][1] + '  ✔', { x: x + 0.85, y: 3.92, w: 1.9, h: 0.55, fontSize: 15, bold: true, color: H.esp, margin: 0, isTextBox: true, valign: 'middle' });
    s.addText(syn[i][2], { x: x + 0.18, y: 4.6, w: 2.55, h: 0.75, fontSize: 12.5, color: H.brown, margin: 0, isTextBox: true, valign: 'top' }); }
  card(s, 0.6, 5.6, 12.1, 0.95, 'FCEDEE');
  s.addText([{ text: 'Gaps: ', options: { bold: true, color: H.red } }, { text: 'family buyers get little tailored messaging · the functional “100% pure” proof is under-told while rivals now claim it too · creator/UGC activity is visible for RTD but thin for Classic.', options: { color: H.esp } }], { x: 0.8, y: 5.65, w: 11.7, h: 0.85, fontSize: 13.5, margin: 0, isTextBox: true, valign: 'middle' });
  src(s, 'exchange4media (2014); afaqs! (2023, 2025b); Nestlé India (n.d.-b); Manifest Media (2026).');
  s.addNotes('Synergy test: does the message suit the segment, and does the media reach them? Yes on all four. Then name the three gaps — they lead to recommendations.');

  // ---------- 11 DISTRIBUTION ----------
  s = addS('Marketing Mix'); title(s, 'Distribution: kirana depth for reach, quick commerce for youth');
  kicker(s, 'Indirect, multi-channel — the channel split mirrors the primary/secondary target split');
  const ch = [['General trade', 'Kiranas, wholesale, rural stockists; ~2,05,000 villages covered (2024)', 'Family buyers, Tier-2/3, triers', H.brown], ['Modern trade', 'Supermarkets & hypermarkets; range visibility, promotions', 'Urban families', H.gold], ['E-commerce', 'Marketplaces; multipacks, reviews, digital shelf', 'Young professionals', H.grey], ['Quick commerce', 'Blinkit, Zepto, Instamart; channel-specific assortments — a key growth driver', 'Students & hustlers in metros', H.red]];
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 3.15, w: 1.6, h: 1.2, rectRadius: 0.08, fill: { color: H.esp }, line: { color: H.esp } });
  s.addText('Nestlé India → distributors', { x: 0.65, y: 3.2, w: 1.5, h: 1.1, fontSize: 13, bold: true, color: H.white, align: 'center', valign: 'middle', margin: 0, isTextBox: true });
  ch.forEach((c, i) => { const y = 1.7 + i * 1.22;
    s.addShape(pres.shapes.LINE, { x: 2.2, y: 3.75, w: 0.45, h: y + 0.5 - 3.75, line: { color: H.gold, width: 1.5, endArrowType: 'triangle' } });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 2.7, y, w: 5.5, h: 1.05, rectRadius: 0.08, fill: { color: H.pale }, line: { color: c[3], width: 1.5 } });
    s.addText([{ text: c[0], options: { bold: true, color: c[3], breakLine: true, fontSize: 14.5 } }, { text: c[1], options: { color: H.esp, fontSize: 12 } }], { x: 2.85, y: y + 0.03, w: 3.7, h: 1.0, margin: 0, isTextBox: true, valign: 'middle' });
    s.addText(c[2], { x: 6.55, y: y + 0.03, w: 1.55, h: 1.0, fontSize: 11, italic: true, color: H.brown, margin: 0, isTextBox: true, valign: 'middle' }); });
  s.addImage({ path: IMG + 'kirana.jpg', x: 8.55, y: 1.7, w: 4.15, h: 2.3, sizing: { type: 'cover', w: 4.15, h: 2.3 } });
  s.addImage({ path: IMG + 'hypermarket.jpg', x: 8.55, y: 4.15, w: 4.15, h: 2.3, sizing: { type: 'cover', w: 4.15, h: 2.3 } });
  src(s, 'Nestlé India (2024, 2026b); Daily Pioneer (2026). Photos: Renzilde (CC BY-SA 3.0); Manivanswiki (CC BY-SA 3.0), Wikimedia Commons.');
  s.addNotes('General trade still carries most FMCG volume; quick commerce is where young urban buyers top up. Risk: price conflict between channels, managed with channel-specific packs.');

  // ---------- 12 QUAL METHOD ----------
  pres.addSection({ title: 'Consumer Research' });
  s = addS('Consumer Research'); title(s, 'Qualitative design: multi-stakeholder in-depth interviews');
  kicker(s, 'Purposive sample n ≥ 5 · semi-structured · recorded with consent · three-level coding');
  const steps = ['Design guide & consent', 'Purposive sample (n ≥ 5)', 'Interview & record', 'Transcribe verbatim', 'In-vivo coding', 'Categories → themes', 'Insights & implications'];
  steps.forEach((t, i) => { const x = 0.6 + i * 1.75; s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.7, w: 1.55, h: 1.1, rectRadius: 0.08, fill: { color: [H.red, H.brown, H.esp][i % 3] }, line: { color: 'FFFFFF' } });
    s.addText([{ text: String(i + 1), options: { bold: true, fontSize: 16, breakLine: true } }, { text: t, options: { fontSize: 11.5 } }], { x: x + 0.05, y: 1.72, w: 1.45, h: 1.06, color: H.white, align: 'center', valign: 'middle', margin: 0, isTextBox: true });
    if (i < 6) s.addShape(pres.shapes.LINE, { x: x + 1.56, y: 2.25, w: 0.18, h: 0, line: { color: H.gold, width: 2, endArrowType: 'triangle' } }); });
  card(s, 0.6, 3.05, 5.9, 3.5);
  s.addText('Sample plan (stakeholders)', { x: 0.8, y: 3.15, w: 5.5, h: 0.4, fontSize: 15, bold: true, color: H.esp, margin: 0, isTextBox: true });
  s.addText(['2 students / hostellers (primary target)', '1 young working professional', '1 household / family buyer', '1 kirana or supermarket retailer', '1 lapsed or competitor-brand user (optional)'].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < 4 } })), { x: 0.8, y: 3.6, w: 5.5, h: 2.0, fontSize: 13.5, color: H.brown, margin: 0, paraSpaceAfter: 5, isTextBox: true, valign: 'top' });
  s.addText('Ethics: informed consent · right to withdraw · anonymised codes R1–R6 · academic use only', { x: 0.8, y: 5.7, w: 5.5, h: 0.75, fontSize: 12, italic: true, color: H.red, margin: 0, isTextBox: true, valign: 'top' });
  card(s, 6.75, 3.05, 5.95, 3.5, H.esp);
  s.addText('12-question guide covers', { x: 6.95, y: 3.15, w: 5.6, h: 0.4, fontSize: 15, bold: true, color: H.gold, margin: 0, isTextBox: true });
  const qs = ['Consumption habits', 'Brand awareness', 'Purchase motivation', 'Preparation & experience', 'Taste & aroma', 'Price perception', 'Brand personality', 'Competitors', 'Ad recall', 'Satisfaction', 'Loyalty', 'Improvements'];
  qs.forEach((q, i) => s.addText((i + 1) + '. ' + q, { x: 6.95 + (i % 2) * 2.85, y: 3.65 + Math.floor(i / 2) * 0.46, w: 2.75, h: 0.42, fontSize: 12.5, color: H.white, margin: 0, isTextBox: true, valign: 'middle' }));
  src(s, 'Research design by the author; coding approach after Gioia et al. (2013) and Braun & Clarke (2006).');
  s.addNotes('Stakeholders, not just consumers: a retailer explains pack-size and channel behaviour that consumers cannot. Minimum five interviews as the brief requires.');

  // ---------- 13 THEMES FRAMEWORK ----------
  s = addS('Consumer Research'); title(s, 'From verbatims to insights: the analysis framework');
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 1.15, w: 12.1, h: 0.45, rectRadius: 0.06, fill: { color: 'FCEDEE' }, line: { color: H.red, width: 1 } });
  s.addText('PLACEHOLDER — interviews pending. Themes below are a-priori candidates, NOT findings. Replace with real coded evidence.', { x: 0.75, y: 1.15, w: 11.8, h: 0.45, fontSize: 13, bold: true, color: H.red, margin: 0, isTextBox: true, valign: 'middle' });
  const lvls = [['Verbatim', '“[exact quote from R_]”', H.grey], ['1st-level in-vivo code', '[respondent’s own words]', H.gold], ['2nd-level category', '[e.g., Convenience]', H.brown], ['Aggregate dimension', '[e.g., Attitudinal beliefs]', H.red]];
  lvls.forEach((l, i) => { const x = 0.6 + i * 3.08; s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.85, w: 2.85, h: 1.3, rectRadius: 0.08, fill: { color: l[2] }, line: { color: l[2] } });
    s.addText([{ text: l[0], options: { bold: true, fontSize: 14.5, breakLine: true } }, { text: l[1], options: { fontSize: 12, italic: true } }], { x: x + 0.1, y: 1.9, w: 2.65, h: 1.2, color: H.white, align: 'center', valign: 'middle', margin: 0, isTextBox: true });
    if (i < 3) s.addShape(pres.shapes.LINE, { x: x + 2.87, y: 2.5, w: 0.2, h: 0, line: { color: H.esp, width: 2, endArrowType: 'triangle' } }); });
  const th = [[fa.FaBolt, 'Convenience'], [fa.FaRupeeSign, 'Price sensitivity'], [fa.FaCoffee, 'Taste & aroma'], [fa.FaShieldAlt, 'Brand trust'], [fa.FaRedo, 'Habit & ritual'], [fa.FaStore, 'Availability'], [fa.FaHeart, 'Emotional connection'], [fa.FaExchangeAlt, 'Alternatives']];
  for (let i = 0; i < 8; i++) { const x = 0.6 + (i % 4) * 3.08, y = 3.45 + Math.floor(i / 4) * 0.95; card(s, x, y, 2.85, 0.8);
    await circleIcon(s, th[i][0], x + 0.15, y + 0.12, 0.56, H.brown);
    s.addText(th[i][1], { x: x + 0.85, y: y + 0.1, w: 1.95, h: 0.6, fontSize: 14, bold: true, color: H.esp, margin: 0, isTextBox: true, valign: 'middle' }); }
  card(s, 0.6, 5.4, 12.1, 1.2, H.pale);
  s.addText([{ text: 'Output per theme: ', options: { bold: true, color: H.red } }, { text: 'supporting respondents (R_, R_) → interpretation → marketing implication → proposition, e.g. “P1: [theme] influences young consumers’ adoption of NESCAFÉ Classic.”', options: { color: H.esp } }], { x: 0.8, y: 5.45, w: 11.7, h: 1.1, fontSize: 13.5, margin: 0, isTextBox: true, valign: 'middle' });
  src(s, 'Framework adapted from the course example and Gioia et al. (2013).');
  s.addNotes('Be honest: interviews are pending, so this slide shows the framework, not findings. Walk through one hypothetical path from a quote to an aggregate dimension.');

  // ---------- 14 SWOT ----------
  pres.addSection({ title: 'Strategy' });
  s = addS('Strategy'); title(s, 'SWOT: strong engine, squeezed middle');
  kicker(s, 'Leverage leadership and reach to own the “first coffee” — defend value without diluting quality');
  const sw = [['Strengths', ['Category leadership & brand trust', '100% pure coffee claim', 'Widest availability incl. quick commerce', 'Consistent youth platform'], H.brown], ['Weaknesses', ['Pricier than chicory blends', 'Less premium than Gold/D2C', 'Thin family-buyer messaging', 'South taste preference favours blends'], H.grey], ['Opportunities', ['Low per-capita consumption', 'Cold coffee becoming year-round', 'Campus & first-job habit formation', 'North/West & Tier-2 growth'], H.gold], ['Threats', ['Coffee input-cost inflation', 'BRU Gold relaunch; Tata Premium; Percol', 'D2C specialty instants', 'Tea’s cultural dominance'], H.red]];
  sw.forEach((q, i) => { const x = 0.6 + (i % 2) * 6.15, y = 1.7 + Math.floor(i / 2) * 2.48; card(s, x, y, 5.95, 2.3, i === 3 ? 'FCEDEE' : H.pale);
    s.addText(q[0], { x: x + 0.25, y: y + 0.12, w: 5.5, h: 0.45, fontSize: 18, bold: true, color: q[2], margin: 0, isTextBox: true });
    s.addText(q[1].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < 3 } })), { x: x + 0.25, y: y + 0.62, w: 5.5, h: 1.6, fontSize: 14, color: H.esp, margin: 0, paraSpaceAfter: 3, isTextBox: true, valign: 'top' }); });
  src(s, 'Analyst synthesis of Sections 3–10 of the report; Financial Express (2025); Gulfood (2026); Reuters via Yahoo Finance (2025).');
  s.addNotes('SWOT summarises the analysis — every point maps to a slide already shown. The key tension: middle-position squeeze under cost inflation.');

  // ---------- 15 RECOMMENDATIONS & PLAN ----------
  s = addS('Strategy'); title(s, 'Recommendations and a 3-month plan: “My First Mug”');
  kicker(s, 'Original student-proposed campaign — not an existing NESCAFÉ activity; budget shares are illustrative');
  const rr = [['QC “First-Cup Kit”', '24 g jar + mug + recipe card', 'New-to-brand buyers; 60-day repeat'], ['Year-round cold coffee', 'Creator recipe series', 'Off-season sales index'], ['Defend value in kiranas', 'Sachet strips, POS', 'Numeric distribution'], ['Campus “Make Your Mug”', 'Sampling at college start', 'QR scans; campus repeat'], ['Make “100% pure” tangible', 'Origin & aroma QR story', '“Real coffee” attribute score']];
  rr.forEach((r, i) => { const y = 1.7 + i * 0.95; card(s, 0.6, y, 5.9, 0.82);
    s.addText(String(i + 1), { x: 0.7, y: y + 0.11, w: 0.6, h: 0.6, fontFace: 'Cambria', fontSize: 26, bold: true, color: H.red, align: 'center', valign: 'middle', margin: 0, isTextBox: true });
    s.addText([{ text: r[0], options: { bold: true, color: H.esp, breakLine: true, fontSize: 14 } }, { text: r[1] + '  ·  KPI: ' + r[2], options: { color: H.brown, fontSize: 11.5 } }], { x: 1.4, y: y + 0.04, w: 5.0, h: 0.76, margin: 0, isTextBox: true, valign: 'middle' }); });
  const mo = [['MONTH 1', 'Launch & trial', 'QC-exclusive kit · teaser reels · creator recipes · Tier-2 kirana POS', 'KPI: kit units, add-to-cart, distribution', H.red], ['MONTH 2', 'Engage & habit', 'Campus activations in 10 cities · exam-season sampling · gaming streams', 'KPI: samples, QR scans, engagement', H.brown], ['MONTH 3', 'Amplify & retain', '“Mug Stories” UGC contest · refill retargeting · brand-lift study', 'KPI: repeat rate, UGC, brand lift', H.esp]];
  mo.forEach((m, i) => { const y = 1.7 + i * 1.6; s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 6.8, y, w: 5.9, h: 1.45, rectRadius: 0.08, fill: { color: m[4] }, line: { color: m[4] } });
    s.addText([{ text: m[0] + ' · ' + m[1], options: { bold: true, color: H.gold, breakLine: true, fontSize: 14 } }, { text: m[2], options: { color: H.white, breakLine: true, fontSize: 12.5 } }, { text: m[3], options: { color: 'E8D6BE', italic: true, fontSize: 11.5 } }], { x: 7.0, y: y + 0.05, w: 5.55, h: 1.35, margin: 0, isTextBox: true, valign: 'middle' }); });
  s.addText('Illustrative budget split: digital & creators 35% · QC media & kit 25% · campus 20% · trade 15% · measurement 5%', { x: 0.6, y: 6.5, w: 12.1, h: 0.25, fontSize: 10.5, italic: true, color: H.grey, margin: 0, isTextBox: true });
  s.addNotes('Each recommendation fixes a gap named earlier. The plan sequences them: trial, then habit, then advocacy, with a KPI for each stage.');

  // ---------- 16 CONCLUSION & REFERENCES ----------
  pres.addSection({ title: 'Close' });
  s = pres.addSlide({ masterName: 'DARK', sectionTitle: 'Close' });
  s.addImage({ path: IMG + 'steam_mug.jpg', x: 8.6, y: 0, w: 4.733, h: 7.5, sizing: { type: 'cover', w: 4.733, h: 7.5 } });
  s.addText('Conclusion', { x: 0.6, y: 0.4, w: 7.6, h: 0.75, fontFace: 'Cambria', fontSize: 34, bold: true, color: H.white, margin: 0, isTextBox: true });
  s.addText(['STP, product ladder, youth communication and twin-engine distribution are coherent — and growth is volume-led.', 'The risk is a squeeze in the middle: value blends below, premium instants above, under coffee-cost inflation.', 'Winning move: own the “first coffee” moment — trial via quick commerce, habit via campus and cold coffee, value via kiranas.'].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < 2 } })),
    { x: 0.6, y: 1.25, w: 7.6, h: 2.3, fontSize: 15, color: 'F4EBDD', margin: 0, paraSpaceAfter: 6, isTextBox: true, valign: 'top' });
  s.addText('Key references', { x: 0.6, y: 3.7, w: 7.6, h: 0.4, fontSize: 14, bold: true, color: H.gold, margin: 0, isTextBox: true });
  s.addText(['afaqs! (2025a, 2025b, 2025c). Nescafé cold coffee; McCann Gen Z ad; coffee epicentre moves North. afaqs.com', 'BestMediaInfo (2026); BusinessWorld (2026). Nestlé India Q2 FY27 results.', 'Daily Pioneer (2026). NielsenIQ FMCG channel data, Oct–Dec 2025.', 'Financial Express (2025). Storm in a coffee cup.', 'Gioia, Corley & Hamilton (2013). Organizational Research Methods, 16(1).', 'Kotler, Keller & Chernev (2022). Marketing Management, 16th ed.', 'Manifest Media (2026). Nescafé sibling conversation about ambition.', 'Mintel (2025). India coffee market report.', 'NESCAFÉ India (n.d.); Nestlé India (n.d.; 2024; 2026a; 2026b).', 'Full APA reference list in the written report, Section 15.'].map((t, k) => ({ text: t, options: { breakLine: k < 9 } })),
    { x: 0.6, y: 4.1, w: 7.6, h: 2.8, fontSize: 10.5, color: 'D9C7B0', margin: 0, paraSpaceAfter: 2, isTextBox: true, valign: 'top' });
  s.addText('Photo: PedanticNarrativeController, Wikimedia Commons, CC0', { x: 0.6, y: 7.1, w: 7.6, h: 0.3, fontSize: 9, color: 'BFAFA3', margin: 0, isTextBox: true });
  s.addNotes('Close with the one-line takeaway: NESCAFÉ Classic should own the first coffee of every new beginning. Thank the professor and invite questions.');

  const out = process.argv[2] || 'deck.pptx';
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log('wrote', out);
})();
