const fs = require('fs');
const L = require('./lib');
const { d, C, H1, H2, H3, P, B, N, PB, SP, T, F, NOTE, caption, tableTitle, styles, numbering, headerFooter, page, CONTENT_W, Paragraph, TextRun, AlignmentType, ImageRun } = L;
const FIG = 'fig/', IMG = 'img/';
const out = process.argv[2] || 'report.docx';

// ---------------- COVER ----------------
const banner = fs.readFileSync(FIG + 'cover_banner.jpg');
const cover = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 300 }, children: [new ImageRun({ type: 'jpg', data: banner, transformation: { width: 640, height: 288 }, altText: { title: 'Cover banner', description: 'Roasted coffee beans with the title NESCAFÉ Classic', name: 'cover' } })] }),
  new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 160 }, children: [new TextRun({ text: 'A Comprehensive Marketing Analysis of NESCAFÉ Classic Instant Coffee in India', font: 'Cambria', size: 44, bold: true, color: C.red })] }),
  new Paragraph({ spacing: { after: 420 }, children: [new TextRun({ text: 'Consumer Behaviour, STP, Competitive Positioning and Marketing Strategy', font: 'Cambria', size: 28, italics: true, color: C.brown })] }),
  T(null, [
    ['**Product**', 'NESCAFÉ Classic Instant Coffee (Nestlé India Ltd.)'],
    ['**Course**', 'Foundation of Marketing — Synchronous Assignment & Viva'],
    ['**Term / Programme**', 'Term II, PGDM Big Data Analytics 2026–28'],
    ['**Institution**', 'Goa Institute of Management'],
    ['**Faculty**', 'Prof. Shantanu Prasad'],
    ['**Submitted by**', '[Student Name]   ·   Roll No.: [Roll Number]'],
    ['**Date of submission**', '[DD Month 2026]'],
  ], [1, 2.6], { size: 21, firstColFill: true }),
  SP(500),
  new Paragraph({ children: [new TextRun({ text: 'Cover photograph: “Roasted coffee beans on the surface” by A S M Jobaer, Wikimedia Commons, CC BY-SA 4.0 (cropped and toned). NESCAFÉ is a registered trademark of Société des Produits Nestlé S.A.; this is an independent student assignment, not affiliated with or endorsed by Nestlé.', size: 15, color: C.grey, italics: true })] }),
  PB(),
];

// ---------------- TOC ----------------
const toc = [
  new Paragraph({ spacing: { after: 200 }, children: [new TextRun({ text: 'Contents', font: 'Cambria', size: 34, bold: true, color: C.red })] }),
  new L.TableOfContents('Contents', { hyperlink: true, headingStyleRange: '1-2' }),
  PB(),
];

// ---------------- BODY ----------------
const body = [];
const add = (...xs) => xs.forEach((x) => Array.isArray(x) ? body.push(...x) : body.push(x));

// 1 Executive summary
add(H1('1. Executive Summary'));
add(P('This report analyses the marketing of **NESCAFÉ Classic**, Nestlé India’s flagship 100% pure instant coffee, in the Indian market. It was prepared for the Foundation of Marketing course and follows the assignment brief: company and product introduction, recent developments, industry and competitor analysis, segmentation and targeting, competitive positioning, product strategy, branding and communication, distribution, conclusions with recommendations, and a marketing plan. A qualitative consumer-research design (minimum five stakeholder interviews) supports the viva component.'));
add(P('**Approach.** The analysis uses secondary sources — Nestlé India’s official website, quarterly filings and press releases; business and marketing media such as Business Standard, afaqs!, BestMediaInfo and Financial Express; and industry/government sources such as NielsenIQ (as reported in the press), Mintel and the Press Information Bureau. Facts are cited in APA 7th style; analytical judgements, assumptions and illustrative estimates are labelled as such.'));
add(P('**Key secondary-research findings.** (1) India’s coffee market is small relative to tea but expanding: domestic consumption rose from 84,000 tonnes (2012) to 91,000 tonnes (2023) (Mintel, 2025). (2) Nestlé India’s recent quarters show strong, volume-led growth — total sales grew 20.5% in Q2 FY27 (BusinessWorld, 2026) — with NESCAFÉ Classic and NESCAFÉ Sunrise named as growth drivers. (3) Growth in the category is being pulled by younger consumers, cold-coffee occasions and quick commerce. (4) NESCAFÉ Classic occupies the “accessible 100% pure coffee” position — above chicory-blend value brands such as BRU Instant and below premium freeze-dried or specialty instant coffees — and its communication (“Make Your World”, 2025–26) is tightly aligned with a Gen Z/young-adult target.'));
add(P('**Consumer research.** A ready-to-use interview guide, consent statement, respondent profile template and a three-level (Gioia-style) coding framework are provided. *Interview findings are deliberately left as clearly marked placeholders because the interviews had not been completed when this report was drafted; no respondent data has been invented.*'));
add(P('**Recommendations (summary).** Build a quick-commerce-first “first-cup” trial kit; convert cold-coffee interest into a year-round ritual; defend value perception with sachet and mid-size packs in Tier-2/3 kiranas; extend the “Make Your World” platform through campus and creator programmes; and use first-party digital data to measure household recruitment. A three-month, illustrative-budget marketing plan (“My First Mug”) operationalises these ideas.'));

// 2 Intro
add(H1('2. Introduction to Nestlé, NESCAFÉ and NESCAFÉ Classic'));
add(H2('2.1 Nestlé (company level)'));
add(P('Nestlé S.A., headquartered in Vevey, Switzerland, is one of the world’s largest food and beverage companies. In India, Nestlé’s presence dates back to 1912, when sales agents began operating in Chennai and Kolkata; **Nestlé India Limited** was incorporated in 1959 and set up its first factory at Moga, Punjab, in 1961 (Nestlé India, n.d.-a; Wikipedia, 2026b). Nestlé India today sells across milk products and nutrition, prepared dishes and cooking aids (e.g., MAGGI), confectionery, and powdered and liquid beverages (NESCAFÉ). The company follows an April–March financial year; FY2025–26 was its first full year on that basis.'));
add(H2('2.2 NESCAFÉ (brand level)'));
add(P('NESCAFÉ was launched by Nestlé in Switzerland in 1938 as a soluble (instant) coffee and has become one of the most widely recognised coffee brands globally (Wikipedia, 2026a). In India, NESCAFÉ is an umbrella brand that spans several soluble-coffee products, ready-to-drink (RTD) cold coffee and out-of-home formats through Nestlé Professional (vending machines and kiosks). Nestlé India reports that NESCAFÉ continues to lead the coffee category, gaining market share and increasing household penetration (Business Standard, 2025b).'));
add(H2('2.3 NESCAFÉ Classic (product level)'));
add(P('**NESCAFÉ Classic** is the brand’s flagship 100% pure instant coffee — a soluble coffee powder/granule that dissolves in hot water or milk, and which Indian consumers also whip with sugar to make “beaten” or frothy coffee and blend into cold coffee. The official NESCAFÉ India page describes it as the brand’s signature coffee with an “unmistakeable aroma and full flavour” and lists glass-jar packs of 24 g, 45 g and 90 g (NESCAFÉ India, n.d.). Retailers also list pouches, larger refill packs and single-serve sachets (e.g., 1.5 g sachets supplied through Nestlé Professional), all labelled “100% pure coffee” and manufactured by Nestlé India (BigBasket, n.d.; Nestlé Professional India, n.d.).'));
add(F(IMG + 'nescafe_classic.jpg', 2.4, 'NESCAFÉ Classic single-serve sachet strip as sold at retail. Photo: Marwan Bello, Wikimedia Commons, CC BY-SA 4.0.'));
add(NOTE('Value proposition (analyst’s summary)', [
  '**For** young Indians and busy households **who want** a quick, energising, real-coffee experience at home, hostel or work, **NESCAFÉ Classic offers** 100% pure coffee with a strong aroma, ready in seconds, in pack sizes from a single sachet to a family jar — **backed by** the trust of India’s most widely available coffee brand.',
]));
add(SP());
add(H2('2.4 Why NESCAFÉ Classic is suitable for marketing analysis'));
add(B([
  '**A category still being built.** India is a tea-dominant market, so coffee brands must *create* consumers, not just win share — STP and consumer-behaviour choices are visible and consequential.',
  '**Clear product-range architecture.** Classic sits between Sunrise (coffee–chicory, value/South-oriented) and Gold (premium), making product-line and positioning analysis concrete.',
  '**Active, current marketing.** 2025–26 brought a new Gen Z campaign, RTD extensions, gaming-streamer partnerships and a pronounced quick-commerce push — real tactics to evaluate.',
  '**Multi-channel distribution.** The same SKU family flows through kiranas, modern trade, marketplaces and quick commerce, allowing channel–segment fit to be tested.',
]));

// 3 Recent developments
add(H1('3. Recent Developments and Market Activities'));
add(P('The table below summarises recent, verifiable developments and — more importantly — what each one signals about Nestlé’s marketing strategy. Dates are as reported by the cited source.'));
add(tableTitle('Recent developments and their marketing significance'));
add(T(['Period', 'Development (fact)', 'Marketing significance (analysis)'], [
  ['Feb 2025', 'Nestlé India said it was considering “as low as possible” price increases as coffee, cocoa and edible-oil costs rose; analysts noted coffee remained inflationary (Reuters via Yahoo Finance, 2025; Business Standard, 2025a).', 'Input-cost inflation squeezes a mass brand. It forces careful price-pack architecture (protecting low-unit-price sachets) and makes perceived value central to communication.'],
  ['2025', 'NESCAFÉ RTD cold coffee extended in India: Iced Latte and Iced Frappé at ₹50/170 ml; Classic, Choco and Caramel Lattes at ₹75/200 ml (Indian Retailer, 2025).', 'Brand extension into youth-led cold occasions; recruits new drinkers who may later adopt Classic at home.'],
  ['2025', 'Nestlé India partnered with gaming streamers to launch the RTD cold-coffee range, reporting strong organic views (Nestlé India, n.d.-b).', 'Media follows the target: Gen Z attention is in gaming/streaming, not only TV.'],
  ['2025', 'Nestlé India said RTD cold coffee grew at ~23% CAGR over two years; Gen Z and millennials are the main buyers; cold coffee is only ~0.2% of a ₹1 trillion cold-beverage market (NielsenIQ estimate) (afaqs!, 2025a).', 'A small base with high growth — a long runway, and a reason to keep teaching “make cold coffee at home with Classic”.'],
  ['2025–26', '“Make Your World” campaign by McCann for NESCAFÉ Classic: a full-length rap jingle aimed at Gen Z; a later film shows an elder sister gifting her brother a NESCAFÉ jar on his first college day (afaqs!, 2025b; Manifest Media, 2026).', 'Re-energises the brand’s long-running youth/“self-made ambition” positioning and targets the moment of habit formation — starting college.'],
  ['FY2025–26', 'Coverage of annual results notes NESCAFÉ Classic continued to drive household recruitment, supported by a renewed communication campaign (Nestlé India, 2026a).', 'Confirms Classic’s strategic role: the entry/recruitment SKU of the NESCAFÉ franchise.'],
  ['Apr–Jun 2026 (Q1 FY27)', 'Sales grew 25.4%; powdered & liquid beverages posted high double-digit, volume-led growth in NESCAFÉ Classic and Sunrise; quick commerce described as a key growth driver (Nestlé India, 2026b).', 'Growth is volume-led (more households/cups), not just price — evidence that penetration strategy is working.'],
  ['Jul–Sep 2026 (Q2 FY27)', 'Total sales rose 20.5% to ₹6,782.2 crore; advertising and sales-promotion spend rose 46%; e-commerce grew strongly, led by quick commerce (BestMediaInfo, 2026; BusinessWorld, 2026).', 'Nestlé is investing heavily behind brands and digital shelves — competitors must respond or cede share of voice.'],
  ['Oct 2025 / Dec 2025', 'HUL relaunched BRU Gold with actors Sara Ali Khan and Aditya Roy Kapur; commentators argued BRU needed to refresh its “cool factor” (Financial Express, 2025).', 'Competitive pressure at the premium-instant edge of Classic’s position.'],
  ['2025', 'CCL Products introduced UK brand Percol in India to push beyond mass-market coffee (Gulfood, 2026).', 'More premium instant choices for urban youth; Classic must justify its “real coffee” credentials.'],
], [1.1, 3.6, 3.3], { size: 17 }));
add(SP());
add(...F(FIG + 'fig_nestle_growth.png', 5.6, 'Nestlé India total sales growth (y-o-y) in selected quarters. Sources: Business Standard (2025c); Ventura Securities (2026); Nestlé India (2026b); BusinessWorld (2026). Note: Nestlé India reports company-level, not brand-level, sales.'));

// 4 Industry
add(H1('4. Indian Instant Coffee Industry Analysis'));
add(H2('4.1 Industry overview and size'));
add(P('Coffee in India has historically been a South-Indian, filter-coffee habit and a small fraction of hot-beverage consumption compared with tea. According to Coffee Board data cited by Mintel, domestic coffee consumption grew from **84,000 tonnes in 2012 to 91,000 tonnes in 2023**, and about half of Indians drink coffee, mostly at home (Mintel, 2025). Instant (soluble) coffee is the dominant at-home format outside the South because it needs no equipment. A Financial Express report citing Euromonitor estimated the Indian coffee market at roughly ₹9,000 crore and growing faster than twice the global average (Financial Express, 2025).'));
add(...F(FIG + 'fig_consumption.png', 4.2, 'Domestic coffee consumption in India, 2012 vs 2023 (tonnes). Source: Coffee Board of India data as reported by Mintel (2025) and PIB (2025).'));
add(H2('4.2 Market structure and shares'));
add(P('The branded instant segment has long been led by Nestlé (NESCAFÉ) and Hindustan Unilever (BRU), with Tata Consumer Products (Tata Coffee Grand) and CCL Products (Continental) as smaller national players and a growing set of D2C specialty brands. **Published share estimates vary widely and are not directly comparable**, so this report does not rely on a single figure:'));
add(tableTitle('Reported market-share estimates (use with caution)'));
add(T(['Estimate', 'Source & scope', 'Comment'], [
  ['NESCAFÉ ≈ 40%', 'Financial Express citing Euromonitor (2025); total coffee market', 'Most credible recent estimate found; definition (value, total coffee) matters.'],
  ['BRU ≈ 33%', 'Financial Express (2025); “category” share', 'Conflicts with the above; scope unclear.'],
  ['Continental ≈ 3.1%', 'CCL Products earnings-call transcript (CCL Products, 2022)', 'Older; company-reported.'],
], [1.2, 2.8, 3], { size: 17 }));
add(P('*Implication:* a student analysis should treat NESCAFÉ as the category leader with BRU as a close challenger, without overstating precision. Primary syndicated data (NielsenIQ/Euromonitor) would be required for exact shares.'));
add(H2('4.3 Consumer preferences and behaviour'));
add(B([
  '**At-home, milk-based and sweet.** Indian instant coffee is typically prepared with milk and sugar; “beaten” coffee and homemade cold coffee are popular rituals.',
  '**Price sensitivity and small packs.** Single-serve sachets and small pouches lower the entry price and suit daily-wage and student budgets — critical in a category where many users are first-time triers.',
  '**Convenience and functional energy.** Coffee is linked to staying alert — exams, night shifts, long commutes, work-from-home.',
  '**Taste segmentation by blend.** South-Indian consumers often prefer a coffee–chicory “filter-like” body; pure coffee is associated with stronger aroma and “real coffee” credentials.',
  '**Youth and café culture.** Gen Z treat cafés as social destinations and drive demand for cold and premium formats; North and West India are now described as primary growth engines (afaqs!, 2025c; Mintel, 2025).',
]));
add(H2('4.4 Digital influence and channel shifts'));
add(P('Digital discovery (Instagram reels, YouTube recipes, gaming streams) shapes trial among young consumers, while quick commerce has made impulse and top-up purchases instant. NielsenIQ data reported for the October–December 2025 quarter show e-commerce (including quick commerce) at **6% of urban FMCG sales, 14% across all metros and 18% in the top eight metros**, with quick commerce contributing over three-quarters of e-commerce FMCG sales (Daily Pioneer, 2026). Traditional trade still accounts for the large majority of FMCG volumes (IBEF, 2025).'));
add(...F(FIG + 'fig_ecom_share.png', 5.4, 'E-commerce (incl. quick commerce) share of FMCG sales, Oct–Dec 2025 quarter. Source: NielsenIQ as reported by Daily Pioneer (2026).'));
add(H2('4.5 PESTLE scan (selective)'));
add(P('PESTLE is used here only for factors that materially affect NESCAFÉ Classic’s marketing choices.'));
add(tableTitle('Selective PESTLE factors and their implications'));
add(T(['Factor', 'Evidence / observation', 'Implication for NESCAFÉ Classic'], [
  ['Economic', 'Coffee input-cost inflation; Nestlé flagged pricing action (Reuters via Yahoo Finance, 2025).', 'Protect price points via pack-size management; communicate value, not just taste.'],
  ['Social', 'Gen Z café culture; coffee shifting from occasional treat to daily habit (Mintel, 2025; afaqs!, 2025b).', 'Target habit-formation moments (college, first job).'],
  ['Technological', 'Quick commerce, digital shelf analytics, creator platforms (Nestlé India, 2026b).', 'Invest in digital shelf, retail media and creator recipes.'],
  ['Environmental', 'Sourcing from ~5,000 Indian farmers via NESCAFÉ Plan-type programmes (Nestlé India, n.d.-c).', 'Origin and farmer stories can deepen brand trust if communicated authentically.'],
  ['Legal', 'FSSAI labelling distinguishes pure coffee from coffee–chicory mixtures.', '“100% pure coffee” is a legally meaningful differentiation claim.'],
], [1.1, 3.2, 3.2], { size: 17 }));
add(H2('4.6 Opportunities and challenges'));
add(T(['Opportunities', 'Challenges'], [
  ['• Low per-capita coffee consumption = headroom\n• Youth adoption, cold coffee becoming year-round\n• Quick commerce enables trial & premium bundles\n• North/West India and Tier-2/3 growth', '• Tea’s cultural dominance and low cost\n• Coffee price inflation compresses margins\n• Premium/D2C brands dilute “real coffee” edge\n• Price-sensitive switching to chicory blends'],
], [1, 1], { size: 18 }));

// 5 Competitors
add(H1('5. Competitor Analysis'));
add(P('Only major competitors with a national presence in branded instant coffee are considered, in line with the brief. Specific retail prices are not tabulated because they vary by pack, channel and promotion; instead, **relative price positioning** is described based on product type (pure vs chicory blend vs premium) and brand communication.'));
add(tableTitle('Competitor comparison — NESCAFÉ Classic vs major instant-coffee rivals'));
add(T(['Dimension', 'NESCAFÉ Classic (Nestlé)', 'BRU Instant / BRU Gold (HUL)', 'Tata Coffee Grand / Grand Premium (Tata Consumer)', 'Continental Xtra / Speciale (CCL Products)'], [
  ['Product characteristics', '100% pure instant coffee; strong aroma (NESCAFÉ India, n.d.)', 'BRU Instant: coffee–chicory blend; BRU Gold: premium pure-coffee variant', 'Coffee powder + “flavour-locked decoction crystals”; Grand Premium is 100% coffee (Tata Consumer Products, n.d.; Adgully, 2023)', 'Xtra: 70% coffee/30% chicory; Speciale: 100% pure; freeze-dried capability since 2005 (CCL Products, 2021)'],
  ['Price positioning*', 'Mid / accessible-premium', 'Instant: value; Gold: premium', 'Value-to-mid; Premium: mid', 'Value (Xtra) to mid (Speciale)'],
  ['Packaging', 'Glass jars (24/45/90 g), pouches, sachets', 'Jars, pouches, sachets', 'Jars, pouches', 'Jars, pouches, sachets'],
  ['Target customer', 'Young adults, students, urban households', 'Mass households; strong in South; Gold for upgraders', 'Coffee drinkers seeking “estate” authenticity', 'Price-conscious households; growing North/West'],
  ['Brand image', 'Youthful, energetic, ambitious; category leader', 'Familiar, warm, South-Indian heritage', 'Plantation heritage, “bean-to-cup”', 'Value; manufacturer credibility'],
  ['Communication', '“Make Your World” rap jingle (McCann); creators, gaming', 'BRU Gold relaunch with Sara Ali Khan & Aditya Roy Kapur (Financial Express, 2025)', 'ASMR “Shik Shik Shik” crystals sound; VR plantation tour (Adgully, 2023; exchange4media, 2015)', 'Low ATL; trade-led'],
  ['Distribution', 'National GT + MT + e-com + quick commerce', 'National, HUL’s deep GT network', 'Tata Consumer’s network; North expansion', 'Selective; growing'],
  ['Strengths', 'Brand leadership, availability, youth relevance', 'Distribution depth, blend taste preference in South', 'Distinct product format, Tata trust', 'Manufacturing scale, value pricing'],
  ['Weaknesses', 'Higher price than blends; less premium than Gold/D2C', 'Ageing image (Financial Express, 2025)', 'Smaller scale and awareness', 'Low brand salience'],
], [1.15, 1.6, 1.55, 1.7, 1.6], { size: 16, firstColFill: true, firstColBold: true }));
add(P('*Relative positioning is the analyst’s judgement from product type and communication, not verified price data.', { run: { size: 17, italics: true, color: C.grey } }));
add(H2('5.1 Where NESCAFÉ Classic differentiates — and where it is exposed'));
add(P('Classic differentiates on three axes at once: **(i) product** — 100% pure coffee versus chicory blends; **(ii) brand** — a youthful “start your ambition” identity that BRU and Tata do not own; and **(iii) availability** — near-universal presence across channels. It is exposed from two directions: from below, where price-sensitive or South-Indian consumers prefer the fuller body and lower price of coffee–chicory blends (BRU Instant, NESCAFÉ’s own Sunrise, Continental Xtra); and from above, where urban upgraders are tempted by BRU Gold, Tata Coffee Grand Premium, NESCAFÉ Gold and D2C specialty instant coffees.'));

// 6 STP
add(H1('6. Segmentation, Targeting and Positioning (STP)'));
add(P('STP is the logic that connects a market to a marketing mix: **segmentation** divides the market into groups with similar needs, **targeting** chooses which groups to serve, and **positioning** designs the offer and image to occupy a distinct place in target consumers’ minds (Kotler et al., 2022).'));
add(...F(FIG + 'fig_stp.png', 6.3, 'STP framework applied to NESCAFÉ Classic (analyst’s synthesis).'));
add(H2('6.1 Segmentation'));
add(tableTitle('Segmentation bases applied to the Indian instant-coffee market'));
add(T(['Base', 'Variables', 'Evidence / rationale', 'Relevance to Classic'], [
  ['Demographic', 'Age 18–35; students, young professionals; household income; life stage (college, first job, new family)', 'Gen Z & millennials are predominant RTD buyers (afaqs!, 2025a); campaign targets college freshers (Manifest Media, 2026)', 'High'],
  ['Geographic', 'North/West vs South; metro vs Tier-2/3 vs rural', 'North and West are now growth engines (afaqs!, 2025c); South prefers chicory/filter styles', 'High (North/West, urban)'],
  ['Psychographic', 'Ambitious/“self-made” achievers; café-culture aspirers; convenience seekers; traditional filter-coffee loyalists', '“Make Your World” lyrics built around Gen Z’s self-made, hustle mindset (afaqs!, 2025b)', 'High for achievers & aspirers'],
  ['Behavioural', 'Occasion (morning, study, work, cold-coffee treat); usage rate; first-time trier vs loyal; benefit sought (energy, taste, aroma, value)', 'Brand recruits new households into coffee (Nestlé India, 2026a)', 'Very high — Classic is the recruitment SKU'],
], [1.1, 2.4, 2.8, 1.3], { size: 16, firstColFill: true, firstColBold: true }));
add(P('Combining these bases yields five candidate segments (analytical, to be validated through interviews):'));
add(N([
  '**Aspiring Starters** — 18–24 students/hostellers, metro & Tier-2, study and social occasions, price-aware, digitally native.',
  '**Hustling Professionals** — 22–35 working adults, WFH/office, energy and focus needs, buy online and on quick commerce.',
  '**Home-Makers & Family Buyers** — buy for the household; value, trust and multi-use (hot and cold coffee).',
  '**Café-Culture Upgraders** — urban 20–35, experiment with cold brew and specialty; risk of trading up away from Classic.',
  '**South-Indian Tradition Seekers** — prefer filter/chicory taste; better served by Sunrise or filter coffee.',
]));
add(H2('6.2 Targeting'));
add(P('Nestlé appears to follow a **differentiated (multi-segment) targeting strategy at portfolio level** — Sunrise for chicory-preferring and value segments, Classic for mainstream pure-coffee adopters, Gold for premium upgraders, and RTD for on-the-go youth — while Classic itself is targeted at young, aspirational adopters.'));
add(tableTitle('Primary and secondary target segments for NESCAFÉ Classic (analysis)'));
add(T(['', 'Primary: Aspiring Starters & young Hustlers (18–30)', 'Secondary: Urban family buyers & first-time coffee triers'], [
  ['Needs', 'Energy for study/work; affordable “real coffee”; self-expression', 'Reliable taste; value; versatility for hot and cold coffee'],
  ['Lifestyle', 'Hostels, PGs, shared flats; long hours; social media heavy', 'Nuclear households; mixed tea/coffee homes'],
  ['Purchase behaviour', 'Small jars, sachets; quick-commerce top-ups; promotions', 'Larger jars/pouches; kirana and supermarket; monthly basket'],
  ['Preferences', 'Strong aroma, quick prep, cold-coffee recipes', 'Trusted brand; consistent quality'],
  ['Motivations', 'Ambition, independence, “my ritual”', 'Family enjoyment; hospitality; value for money'],
  ['Evidence', 'Gen Z rap jingle; college-freshers film (afaqs!, 2025b; Manifest Media, 2026)', 'Household-recruitment focus (Nestlé India, 2026a); family pack sizes on retail sites'],
], [1.2, 3, 3], { size: 16, firstColFill: true, firstColBold: true }));
add(H2('6.3 Positioning'));
add(B([
  '**Brand positioning (NESCAFÉ):** the coffee that kick-starts ambition and change — continuous from “It All Starts with a NESCAFÉ” (2014) to “Make Your World” (exchange4media, 2014; Manifest Media, 2026).',
  '**Product positioning (Classic):** 100% pure coffee with strong aroma — the accessible, everyday “real coffee”.',
  '**Functional benefits:** quick preparation, energy/alertness, aroma and taste, versatile (hot, beaten, cold).',
  '**Emotional benefits:** confidence, independence, a personal ritual, belonging to a youthful brand world.',
  '**Perceived value:** priced above blends but below premium; sachets make trial low-risk.',
  '**Brand associations:** red mug and red cap, the four-note jingle, college life, morning start, “ambition”.',
]));
add(NOTE('Positioning statement (proposed, analyst-written)', ['For **young Indians starting something new** — college, a first job, a side hustle — **NESCAFÉ Classic** is the **100% pure instant coffee** that **turns every ambition into a ready-in-seconds ritual**, because it combines rich aroma and a real-coffee kick with the trust and everywhere-availability of India’s leading coffee brand.']));
add(...F(FIG + 'fig_perceptual_map.png', 5.4, 'Illustrative perceptual map of Indian instant coffees. Positions are the analyst’s judgement based on product type (pure vs chicory blend vs premium/freeze-dried) and communication tone — NOT survey data. To be validated with interview evidence.'));
add(P('**Map assumptions.** The x-axis reflects relative shelf-price tier inferred from product type; the y-axis reflects perceived coffee quality/“coffee-forwardness” (pure > blend; freeze-dried/specialty > spray-dried). Bubble size loosely reflects brand scale. The map shows Classic occupying the upper-middle — a defendable “accessible quality” space — with competitive crowding by BRU Gold and Tata Coffee Grand Premium.'));

// 7 Competitive positioning
add(H1('7. Competitive Positioning'));
add(P('**USP.** “100% pure coffee from India’s leading coffee brand, with an aroma you notice — available everywhere, from a ₹-few sachet to a family jar.” The USP is not any single attribute but the combination of *pure coffee + brand trust + reach*.'));
add(tableTitle('Positioning consistency check — is the marketing mix aligned?'));
add(T(['Element', 'What we observe', 'Consistent with positioning?'], [
  ['Price', 'Above chicory blends, below premium instant; sachets lower the entry ticket', '✔ Consistent with “accessible real coffee”'],
  ['Packaging', 'Iconic red cap/red branding; glass jar signals quality; sachets for trial', '✔ Mostly; jar is premium cue, sachets serve value'],
  ['Communication', 'Youth/ambition themes; rap jingle; college narratives; creators & gaming', '✔ Strongly aligned with primary target'],
  ['Product', '100% pure coffee, strong aroma', '✔ Supports “real coffee” claim; taste may be harsh for chicory-preferring South consumers (gap filled by Sunrise)'],
  ['Distribution', 'GT + MT + e-com + quick commerce; vending/kiosks via Nestlé Professional', '✔ Ubiquity supports “everyday” role; quick commerce fits urban youth'],
], [1.1, 3.4, 3.1], { size: 17, firstColFill: true, firstColBold: true }));
add(P('**Versus BRU:** BRU’s strength is taste familiarity and heritage, particularly in the South; Classic wins on pure-coffee credentials and youth imagery. **Versus Tata Coffee Grand:** Tata differentiates on a product gimmick (decoction crystals and their sound) and plantation provenance; Classic wins on scale and brand salience but could borrow provenance storytelling (it already does so for Sunrise’s farmer campaign). **Versus D2C/premium:** Classic cannot win on craft; it should position as the *reliable daily* coffee rather than the weekend treat.'));

// 8 Product strategy
add(H1('8. Product Strategy'));
add(H2('8.1 Levels of product'));
add(...F(FIG + 'fig_product_levels.png', 4.0, 'Three levels of product for NESCAFÉ Classic (analyst’s application of Kotler et al., 2022).'));
add(H2('8.2 Product mix, lines, width and depth'));
add(P('**Scope matters.** Product mix concepts apply at the *company* level (Nestlé India), product-line concepts at the *category/brand* level (NESCAFÉ coffee), and item depth at the *product* level (NESCAFÉ Classic). The table keeps these levels separate.'));
add(tableTitle('Product mix and line analysis (Nestlé India → NESCAFÉ → Classic)'));
add(T(['Level', 'Concept', 'Application (illustrative, based on public product listings)'], [
  ['Nestlé India (company)', 'Product mix width = number of product lines', 'At least four broad groups: milk products & nutrition; prepared dishes & cooking aids (MAGGI); confectionery (KitKat, Munch); powdered & liquid beverages (NESCAFÉ) (Nestlé India, n.d.-a)'],
  ['NESCAFÉ (brand/line)', 'Product line length = items in the coffee line', 'Classic; Sunrise (coffee–chicory); Gold (premium); RTD cold coffee (Iced Latte, Iced Frappé, Classic/Choco/Caramel Lattes); Nestlé Professional vending/out-of-home'],
  ['NESCAFÉ Classic (product)', 'Depth = variants of one item', 'Jars 24 g / 45 g / 90 g (official); pouches and refill packs; 1.5 g sachets/strips; multi-packs on e-commerce'],
  ['Extensions', 'Line & brand extension', 'Classic → RTD “Classic Latte” can (line extension into cold, on-the-go); cold-coffee recipes extend usage occasions'],
], [1.4, 1.9, 4.3], { size: 17, firstColFill: true, firstColBold: true }));
add(H2('8.3 Packaging, quality and recent changes'));
add(B([
  '**Packaging:** the red cap and red-mug iconography are strong distinctive brand assets; glass jars signal quality and allow aroma retention, while sachets enable low-price trial and portability.',
  '**Quality perception:** “100% pure coffee” and Nestlé’s global quality systems support trust; “strong aroma” is the sensory proof point.',
  '**Range logic:** Classic (mainstream) – Sunrise (value/chicory) – Gold (premium) creates a good–better–best ladder that lets Nestlé capture switchers in both directions.',
  '**Recent changes:** extension into RTD cold coffee (2025); renewed Classic campaign (2025–26). No reformulation of Classic was found in sources reviewed.',
]));

// 9 Branding
add(H1('9. Branding and Communication Strategy'));
add(H2('9.1 Brand identity, personality and image'));
add(T(['Brand element', 'NESCAFÉ Classic'], [
  ['Identity', 'Red NESCAFÉ logotype, red cap/mug, four-note sonic signature'],
  ['Personality (Aaker-style)', 'Excitement (young, spirited), sincerity (warm, dependable), competence (leader)'],
  ['Image', 'The coffee of youth, beginnings and ambition'],
  ['Awareness', 'Very high — category leader with widest availability (inferred from leadership and reach)'],
  ['Associations', 'College, mornings, friends, hustle, aroma, cold coffee at home'],
  ['Loyalty drivers', 'Habit, taste familiarity, trust; threatened by promotions and premium alternatives'],
], [1.4, 4], { size: 18, firstColFill: true, firstColBold: true }));
add(H2('9.2 Campaigns and digital activity'));
add(tableTitle('Selected NESCAFÉ communication in India'));
add(T(['Campaign / activity', 'Year', 'Idea', 'Target fit'], [
  ['“It All Starts with a NESCAFÉ” / #ItAllStarts (McCann)', '2014–', 'Coffee as the start of change; user stories on Twitter (exchange4media, 2014)', 'Youth'],
  ['“Jo Banaye, Special Ban Jaaye” (McCann)', '2023', 'Teen makes NESCAFÉ Classic cold coffee — making great cold coffee is easy (afaqs!, 2023)', 'Teens/young adults; at-home cold coffee'],
  ['“Frappé Jahan, Hangout Wahan”', '2023', 'All-in-one frappé for hangouts (afaqs!, 2023b)', 'Youth social'],
  ['Gaming-streamer launch of RTD', '2025', 'Streamers introduce cold coffee range (Nestlé India, n.d.-b)', 'Gen Z gamers'],
  ['“Make Your World” (McCann)', '2025–26', 'Full rap jingle for Gen Z; first-day-of-college sibling story (afaqs!, 2025b; Manifest Media, 2026)', 'College freshers'],
  ['NESCAFÉ Sunrise farmer packs (sister brand)', '~2024', 'Packs feature Karnataka farmers with QR stories (Nestlé India, n.d.-c)', 'Value/South; trust'],
], [2.3, 0.7, 3.2, 1.4], { size: 16 }));
add(H2('9.3 Is communication synergistic with the target segment?'));
add(P('**Largely yes.** The message (ambition, new beginnings), the brand personality (young, energetic), the media (YouTube, Instagram, gaming streams, quick-commerce retail media) and the primary segment (18–30, urban, digitally native) point in the same direction. Storytelling at life-stage transitions — the first day of college — targets the exact moment when routines and brand habits form, which is a strong consumer-behaviour insight.'));
add(P('**Gaps.** (1) The secondary family segment sees less tailored messaging. (2) Communication emphasises emotion more than the functional “100% pure coffee” proof point, which competitors (BRU Gold, Tata Grand Premium) also now claim. (3) Influencer and UGC activity is visible for RTD but less documented for Classic itself — an opportunity addressed in the recommendations.'));

// 10 Distribution
add(H1('10. Distribution Strategy'));
add(...F(FIG + 'fig_channels.png', 6.3, 'Indicative channel map for NESCAFÉ Classic in India (analyst’s synthesis of public disclosures; intermediary structures simplified).'));
add(tableTitle('Channel analysis and fit with target segments'));
add(T(['Channel', 'Role for Classic', 'Segment served', 'Fit'], [
  ['General trade (kiranas, wholesale, rural stockists)', 'Volume & reach; sachets and small packs; Nestlé reported village coverage of ~2,05,000 in 2024 (Nestlé India, 2024)', 'Family buyers; Tier-2/3; first-time triers', 'High — essential for penetration'],
  ['Modern trade (supermarkets, hypermarkets)', 'Range visibility (jars, refills), promotions, brand blocking', 'Urban family buyers', 'High'],
  ['E-commerce marketplaces', 'Multi-packs, bundles, reviews; digital shelf', 'Young professionals; planned purchases', 'High'],
  ['Quick commerce (Blinkit, Zepto, Instamart)', 'Instant top-ups; impulse; channel-specific assortments; key growth driver (Nestlé India, 2026b)', 'Students, hustlers in metros', 'Very high for primary target'],
  ['Out-of-home (Nestlé Professional vending/kiosks)', 'Sampling and habit at offices, campuses, railway stations (Indian Retailer, n.d.)', 'Professionals, travellers, students', 'Supportive'],
], [1.7, 2.8, 1.6, 1.3], { size: 16, firstColFill: true, firstColBold: true }));
add(P('**Direct vs indirect.** Distribution is overwhelmingly *indirect* (via distributors, retailers and platforms); Nestlé’s closest-to-direct touchpoints are out-of-home vending/cafés and brand stores on marketplaces. **Alignment with segmentation:** the twin engines — kirana depth for penetration and quick commerce for urban youth — mirror the primary/secondary target split. The main risk is channel conflict over pricing between quick commerce and general trade, which must be managed through channel-specific pack sizes.'));
add(...F(IMG + 'kirana.jpg', 4.0, 'A typical Indian kirana store — the backbone of FMCG reach. Photo: Renzilde, Wikimedia Commons, CC BY-SA 3.0.'));

// 11 Qualitative research
add(H1('11. Qualitative Consumer Research Design'));
add(NOTE('Status of primary research', ['Interviews were **not yet completed** at the time of drafting. This section provides the full research design and ready-to-use instruments. All result areas are **placeholders** and must be replaced only with actual interview evidence. No respondents, quotes or findings have been invented.'], 'FCEDEE', C.red));
add(SP());
add(H2('11.1 Research objective and questions'));
add(P('**Objective:** to understand how Indian consumers and trade stakeholders perceive, choose, use and stay loyal to NESCAFÉ Classic relative to alternatives, in order to test the STP and positioning analysis in this report.'));
add(N([
  'RQ1: What motivates consumers to buy and keep using NESCAFÉ Classic?',
  'RQ2: How do consumers perceive Classic’s price, taste and aroma relative to BRU, Tata and other alternatives?',
  'RQ3: What occasions and rituals surround instant-coffee consumption?',
  'RQ4: What role do channels (kirana, supermarket, quick commerce) play in purchase?',
  'RQ5: What would increase satisfaction and loyalty?',
]));
add(H2('11.2 Methodology, sampling and interview approach'));
add(B([
  '**Design:** exploratory, qualitative; semi-structured in-depth interviews (20–30 minutes), in person or by video call.',
  '**Sampling:** purposive, multi-stakeholder, minimum n = 5 (assignment requirement); recommended 6–8 for saturation. Suggested mix: 2 students/hostellers (primary target), 1 young working professional, 1 household/family buyer, 1 kirana or supermarket retailer, 1 lapsed user or competitor-brand user.',
  '**Recording:** audio-record with explicit consent; take field notes on non-verbal cues; transcribe verbatim within 24 hours; anonymise as R1, R2…',
  '**Ethics:** informed consent, voluntary participation, right to withdraw, no personal identifiers, data used only for coursework.',
]));
add(...F(FIG + 'fig_qual_workflow.png', 6.3, 'Qualitative research workflow used in this study.'));
add(H2('11.3 Interview guide (12 open-ended questions)'));
add(tableTitle('Interview guide mapped to research themes'));
add(T(['#', 'Question', 'Theme probed'], [
  ['1', 'Tell me about a typical day — when and how do you drink coffee or tea?', 'Consumption habits'],
  ['2', 'What coffee brands come to mind first? What do you know about NESCAFÉ Classic?', 'Brand awareness'],
  ['3', 'Think about the last time you bought coffee. Where, which pack, and why that one?', 'Purchase motivation; channel'],
  ['4', 'How do you usually prepare it? Hot, beaten, cold, with milk?', 'Product experience'],
  ['5', 'What do you like most and least about NESCAFÉ Classic’s taste and aroma?', 'Product preference'],
  ['6', 'How do you feel about its price compared with other coffees? What would make you switch?', 'Price perception'],
  ['7', 'If NESCAFÉ Classic were a person, how would you describe them?', 'Brand personality/perception'],
  ['8', 'Have you used BRU, Tata Coffee Grand, Continental or café brands? How do they compare?', 'Competitor preference'],
  ['9', 'Do you remember any NESCAFÉ advertising or social-media content? What did it say to you?', 'Communication recall'],
  ['10', 'How satisfied are you overall, and what would make you recommend it to a friend?', 'Satisfaction'],
  ['11', 'Would you keep buying it if a cheaper or newer brand were on offer? Why?', 'Loyalty'],
  ['12', 'If you could change one thing about NESCAFÉ Classic, what would it be?', 'Improvement suggestions'],
], [0.4, 5.2, 2], { size: 17 }));
add(P('*Retailer variant (for stakeholder interviews):* Which coffee brands sell fastest and why? Which pack sizes move most? How do schemes, margins and quick-commerce competition affect your coffee sales?', { run: { size: 19 } }));
add(H2('11.4 Respondent profile template'));
add(T(['ID', 'Stakeholder type', 'Age band', 'Gender', 'City / tier', 'Occupation', 'Usual brand', 'Date & mode'], [
  ['R1', '[e.g., Student]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R2', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R3', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R4', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R5', '[e.g., Kirana retailer]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R6 (opt.)', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
], [0.7, 1.4, 0.8, 0.8, 1, 1.1, 1, 1], { size: 16 }));

// 12 Analysis framework
add(H1('12. Qualitative Analysis Framework'));
add(P('Analysis follows a three-level inductive coding approach consistent with the Gioia methodology (Gioia et al., 2013) and the course example: **verbatim → first-level in-vivo codes → second-level categories → third-level aggregate dimensions**, combined with Braun and Clarke’s (2006) six-phase thematic analysis (familiarisation, coding, theme search, review, definition, write-up). Each aggregate dimension is then linked to a proposition about consumer behaviour and to a marketing implication.'));
add(tableTitle('Coding table — to be completed with actual interview data'));
add(T(['Resp. ID', 'Respondent profile', 'Key verbatim response', 'First-level (in-vivo) code', 'Second-level category', 'Aggregate dimension', 'Consumer insight', 'Marketing implication'], [
  ['R1', '[profile]', '[PLACEHOLDER – insert exact quote]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R2', '[profile]', '[PLACEHOLDER]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R3', '[profile]', '[PLACEHOLDER]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R4', '[profile]', '[PLACEHOLDER]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
  ['R5', '[profile]', '[PLACEHOLDER]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'],
], [0.6, 1, 1.6, 1, 1, 1, 1, 1.2], { size: 15 }));
add(SP());
add(tableTitle('Candidate themes (a priori, NOT findings) and how they would be evidenced'));
add(T(['Potential theme', 'What would count as supporting evidence', 'Interpretation if supported', 'Marketing implication if supported'], [
  ['Convenience', 'Mentions of speed, “just add water/milk”, hostel use', 'Instant format is the core value', 'Lead with ritual-in-seconds; sachets, QC availability'],
  ['Price sensitivity', 'Comparisons of pack prices; switching on offers', 'Value perception fragile', 'Small packs; value bundles; avoid deep discounts'],
  ['Taste & aroma', 'Words like “strong”, “smell”, “bitter”', 'Sensory proof of “pure coffee”', 'Sensory-led communication; sampling'],
  ['Brand trust', '“Always used it”, “Nestlé is safe”', 'Leadership reduces risk', 'Reinforce quality story'],
  ['Habit / ritual', 'Fixed times, routines, “can’t start without it”', 'Loyalty via habit', 'Target life-stage transitions'],
  ['Availability', 'Bought at nearest shop/app', 'Reach drives choice', 'Maintain GT + QC presence'],
  ['Emotional connection', 'Memories, friends, college', 'Brand meaning beyond product', 'Storytelling; UGC'],
  ['Alternatives', 'Tea, BRU, café, RTD', 'Competitive set as perceived', 'Sharpen differentiation'],
], [1.1, 2.1, 1.6, 2], { size: 16, firstColFill: true, firstColBold: true }));
add(H3('12.1 Results area — PLACEHOLDER'));
add(NOTE('Insert findings after interviews', [
  'Theme 1: [name] — supported by R_, R_ — “[quote]” → interpretation → implication.',
  'Theme 2: [name] — …',
  'Proposition P1 (example format only): *[Theme] influences young consumers’ adoption of NESCAFÉ Classic.*',
  'Summary of how findings confirm or challenge the STP analysis in Section 6: [to be written].',
], 'F3F0EA', C.brown));

// 13 Conclusion & recommendations
add(H1('13. Conclusions and Recommendations'));
add(H2('13.1 Evaluation of current marketing'));
add(tableTitle('Scorecard of NESCAFÉ Classic’s marketing (analyst’s judgement)'));
add(T(['Area', 'Assessment', 'Rating'], [
  ['STP', 'Clear youth focus at product level, portfolio-level differentiation via Sunrise/Gold/RTD', 'Strong'],
  ['Positioning', 'Distinct “accessible real coffee + ambition”; crowding from premium-instant competitors', 'Strong, under pressure'],
  ['Product strategy', 'Good–better–best ladder; deep pack range; RTD extension', 'Strong'],
  ['Branding & communication', 'Consistent youth platform; modern media; weaker functional proof and family messaging', 'Strong / improve'],
  ['Distribution', 'Ubiquitous; quick commerce a growth engine', 'Very strong'],
  ['Consumer value', 'Trial-friendly sachets; value perception at risk from price inflation', 'Moderate–strong'],
  ['Competitive advantage', 'Scale, brand assets and reach are hard to replicate', 'Sustainable'],
], [1.5, 4.5, 1.3], { size: 17, firstColFill: true, firstColBold: true }));
add(P('Overall, NESCAFÉ Classic’s marketing is coherent and evidence suggests it is working: Nestlé India attributes volume-led growth to Classic and Sunrise, and Classic remains the brand’s household-recruitment engine. The strategic risk is a **squeeze in the middle** — value blends below and premium/specialty instants above — at a time of input-cost inflation.'));
add(H2('13.2 Recommendations'));
const recs = [
  ['R1. Quick-commerce “First-Cup Kit”', 'QC is a key growth driver; young urban buyers want low-risk trial', 'Bundle a 24 g jar + branded mug + cold-coffee recipe card, exclusive to QC; retail-media and search ads', 'Aspiring Starters, Hustlers (metros)', 'Higher trial and repeat among new households', 'Platform partnerships; channel-exclusive SKU to avoid GT price conflict', 'Kit sell-through; new-to-brand buyers %; 60-day repeat rate'],
  ['R2. Year-round cold-coffee ritual', 'Cold coffee is small (0.2% of cold beverages) but fast-growing; Classic already owns “make it at home” (2023 ad)', 'Creator recipe series (“30-second desk/hostel cold coffee”); winter variants (hot frothy coffee)', 'Students, young professionals', 'More cups per user; reduced seasonality', 'Short-form video; recipe hub; shoppable links', 'Views → add-to-cart rate; off-season sales index'],
  ['R3. Defend value in Tier-2/3 kiranas', 'Price inflation and blend competition threaten switching', 'Sachet strips, ₹-price-point packs, retailer display incentives', 'Family buyers, first-time triers', 'Protected penetration; fewer switches to blends', 'Distributor schemes; POS refresh', 'Numeric distribution; sachet volume; retailer offtake'],
  ['R4. Extend “Make Your World” to campuses', 'Campaign targets college start — the habit-forming moment', 'Campus ambassadors, exam-season sampling, vending tie-ups with Nestlé Professional', 'College freshers', 'Early habit formation; brand love', 'Partner 50+ colleges in 10 cities (illustrative)', 'Samples; QR scans; campus repeat purchase'],
  ['R5. Make “100% pure coffee” tangible', 'Competitors now also claim pure coffee; Classic’s functional proof is under-communicated', 'Origin/aroma storytelling (Indian farmers, aroma test), pack QR to process video', 'All segments, esp. upgraders', 'Stronger quality perception vs BRU Gold/Tata Premium', 'Borrow Sunrise farmer-QR mechanic', 'Brand-attribute scores (“real coffee”); QR scans'],
  ['R6. First-party data & recruitment measurement', 'Growth is volume-led; need to track household recruitment precisely', 'Loyalty/UGC programme with QR codes; link to retail-media data', 'All digital buyers', 'Better targeting and ROI', 'CRM + clean-room partnerships', 'Opt-ins; cost per new household; CLV'],
];
recs.forEach((x) => { add(new Paragraph({ keepNext: true, spacing: { before: 160, after: 60 }, children: [new TextRun({ text: x[0], bold: true, color: C.red, size: 22 })] })); add(T(null, [['Problem / opportunity', x[1]], ['Proposed action', x[2]], ['Target segment', x[3]], ['Expected outcome', x[4]], ['Implementation approach', x[5]], ['KPI', x[6]]], [1.4, 5], { size: 18, firstColFill: true, firstColBold: true })); });

// 14 Marketing plan
add(H1('14. Three-Month Marketing Plan — “My First Mug” (proposed)'));
add(NOTE('Important', ['“My First Mug” is an **original student-proposed campaign concept**. It is not an existing NESCAFÉ campaign. Budget figures are **illustrative assumptions** for planning practice only.'], 'FCEDEE', C.red));
add(SP());
add(H2('14.1 Objectives (SMART, illustrative)'));
add(B([
  'Recruit new households into NESCAFÉ Classic among 18–30-year-olds in 10 metro and Tier-2 cities within 90 days (target to be set against Nielsen/NIQ baseline).',
  'Achieve a 60-day repeat-purchase rate above the category benchmark for First-Cup Kit buyers.',
  'Lift “real/pure coffee” attribute association among the target by a measurable margin in a pre/post brand-lift study.',
]));
add(H2('14.2 Campaign idea'));
add(P('**Insight:** every ambition begins with a first step — the first day of college, the first job, the first rented room — and those “firsts” are when new routines are formed. **Idea:** *My First Mug* invites young Indians to start their new chapter with their own NESCAFÉ Classic ritual. It extends the current “Make Your World” platform rather than replacing it, keeping brand consistency.'));
add(...F(FIG + 'fig_plan_gantt.png', 6.3, 'Indicative 13-week activity timeline for the proposed “My First Mug” plan.'));
add(tableTitle('Month-by-month plan'));
add(T(['', 'Month 1 — Launch & trial', 'Month 2 — Engage', 'Month 3 — Amplify & retain'], [
  ['Objective', 'Drive trial', 'Build habit', 'Repeat & advocacy'],
  ['Activity', 'Launch QC-exclusive First-Cup Kit; teaser reels; creator recipe series begins; kirana POS & sachet strips in Tier-2', 'Campus “Make Your Mug” activations & exam-season sampling (10 cities); gaming-stream integrations', 'UGC “Mug Stories” contest; retarget kit buyers with refill-pack offers; brand-lift study'],
  ['Target audience', 'Students, young professionals; Tier-2 family buyers', 'College freshers', 'Kit buyers, engaged users'],
  ['Channel', 'Blinkit/Zepto/Instamart, Instagram, YouTube Shorts, kiranas', 'Campus events, vending, YouTube Live/streams', 'Instagram, QC retail media, CRM/WhatsApp opt-in'],
  ['KPI', 'Kit units; reach; add-to-cart rate; numeric distribution', 'Samples; QR scans; engagement rate', 'Repeat rate; UGC entries; brand-lift'],
  ['Expected outcome', 'Awareness spike; first purchases', 'Trial converts into routine', 'Loyal users and advocacy'],
], [1.2, 2.2, 2.2, 2.2], { size: 17, firstColFill: true, firstColBold: true }));
add(tableTitle('Illustrative budget allocation (assumption, not company data)'));
add(T(['Head', 'Share of plan budget', 'Rationale'], [
  ['Digital & creator content', '35%', 'Primary target is digital-first'],
  ['Quick-commerce retail media & kit subsidy', '25%', 'Converts attention to trial at point of purchase'],
  ['Campus & sampling activations', '20%', 'Habit formation at life-stage transition'],
  ['Trade (kirana POS, schemes)', '15%', 'Protects penetration in Tier-2/3'],
  ['Measurement (brand-lift, analytics)', '5%', 'Evidence-based optimisation'],
], [2.5, 1.5, 3.5], { size: 17 }));
add(P('**Expected outcomes (directional):** higher trial among new young households, a measurable rise in repeat purchase from kit buyers, and stronger “pure coffee” associations — with learnings to scale nationally in the following quarter.'));

// 15 References
add(H1('15. References'));
add(P('*Note on access:* sources were identified and checked through web search on 26 November 2026. Some pages were reviewed through search summaries because direct access was restricted in the drafting environment; please open each link and confirm details before final submission.', { run: { size: 18, color: C.grey } }));
const refs = [
  'Adgully. (2023). *Tata Consumer Products strengthens its instant coffee portfolio*. https://www.adgully.com/tata-consumer-products-strengthens-it-s-instant-coffee-portfolio-126967.html',
  'afaqs! (2023). *NESCAFÉ showcases the art of becoming special in their new cold coffee campaign “Jo Banaye, Special Ban Jaaye”*. https://www.afaqs.com/news/advertising/nescaf-showcases-the-art-of-becoming-special-in-their-new-cold-coffee-campaign-jo-banaye-special-ban-jaaye',
  'afaqs! (2023b). *NESCAFÉ launches All-in-one Frappé with “Frappé jahan, hangout wahan” campaign*. https://www.afaqs.com/news/advertising/nescaf-launches-all-in-one-frappe-with-frappe-jahan-hangout-wahan-campaign',
  'afaqs! (2025a). *From cafés to quick commerce: Nescafé serves cold coffee to Gen Z*. https://www.afaqs.com/marketing/nescafés-rtd-coffee-market-grows-23-year-on-year-led-by-gen-z-demand-10619538',
  'afaqs! (2025b). *McCann’s new ad for Nescafé aims for Indian Gen Z recall*. https://www.afaqs.com/news/advertising/mccanns-new-ad-for-nescafé-aims-for-indian-gen-z-recall-8800865',
  'afaqs! (2025c). *India’s coffee epicentre moves North as youth choose premium blends*. https://www.afaqs.com/news/mktg/coffees-epicentre-moves-north-as-youth-drive-demand-for-premium-blends-10964562',
  'BestMediaInfo. (2026, October). *Nestlé India hikes advertising and marketing spends 46% in Q2 FY27; sales rise 20.5%*. https://bestmediainfo.com/mediainfo/mediainfo-marketing/nestl%C3%A9-india-hikes-advertising-and-marketing-spends-46-in-q2-fy27-sales-rise-205-12679000',
  'BigBasket. (n.d.). *NESCAFÉ Classic 100% pure instant coffee* [Product listing]. https://www.bigbasket.com/pd/231187/nescafe-classic-100-pure-instant-coffee-100-g-dawn-jar',
  'Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77–101. https://doi.org/10.1191/1478088706qp063oa',
  'Business Standard. (2025a, February 25). *Nestle shares rise 2% after reports suggest company is mulling price hikes*. https://www.business-standard.com/markets/news/nestle-shares-rise-2-after-reports-suggests-company-is-mulling-price-hikes-125022500492_1.html',
  'Business Standard. (2025b, October 16). *Nestle India Q2 results: Profit falls 17 per cent, revenue up 10 per cent*. https://www.business-standard.com/companies/quarterly-results/nestle-india-q2-results-profit-falls-17-percent-revenue-up-10-percent-125101601143_1.html',
  'Business Standard. (2025c, April 24). *Nestle India Q4FY25 results: Profit drops 6.5% to ₹873 crore, sales up 3.7%*. https://www.business-standard.com/amp/companies/quarterly-results/nestle-india-q4fy25-results-profit-drops-6-5-to-873-crore-sales-up-3-7-125042400593_1.html',
  'BusinessWorld. (2026, October). *Nestlé India Q2 profit rises 36.3% on 20.5% sales growth*. https://www.businessworld.in/article/nestl-india-q2-profit-rises-36-3-on-20-5-sales-growth-628681',
  'CCL Products (India) Ltd. (2021). *Company presentation 2020*. https://www.cclproducts.com/wp-content/uploads/2021/07/Company-presentation-2020.pdf',
  'CCL Products (India) Ltd. (2022, January 31). *Earnings conference call transcript* [NSE filing]. https://nsearchives.nseindia.com/corporate/CCL_31012022171203_NSETranscript.pdf',
  'Daily Pioneer. (2026). *FMCG growth moderates in December quarter as GST transition impacts pricing*. https://dailypioneer.com/news/fmcg-growth-moderates-in-december-quarter-as-gst-transition-impacts-pricing',
  'exchange4media. (2014). *Nescafé brews 50 stories of resolve for #ItAllStarts campaign*. https://www.exchange4media.com/advertising-news/nescafe-brews-50-stories-of-resolve-for-itallstarts-campaign-57715.html',
  'exchange4media. (2015). *Consumers are seeking an ‘upgrade’ in the coffee category: Sushant Dash*. https://www.exchange4media.com/marketing-news/consumers-are-seeking-an-upgrade-in-the-coffee-category-sushant-dash-62991.html',
  'Financial Express. (2025). *Storm in a coffee cup* [Newspaper article, via Magzter]. https://www.magzter.com/en/stories/newspaper/Financial-Express-Lucknow/STORM-IN-A-COFFEE-CUP',
  'Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research: Notes on the Gioia methodology. *Organizational Research Methods, 16*(1), 15–31. https://doi.org/10.1177/1094428112452151',
  'Gulfood. (2026). *CCL rolls out UK’s Percol brand in India to push beyond mass-market coffee*. https://www.gulfood.com/gulfood-2026-press-releases/ccl-rolls-out-uks-percol-brand-in-india-to-push-beyond-mass-market-coffee',
  'India Brand Equity Foundation. (2025). *Quick commerce sprints ahead but still a small slice for FMCG giants*. https://ibef.org/news/quick-commerce-sprints-ahead-but-still-a-small-slice-for-fmcg-giants',
  'Indian Retailer. (n.d.). *Nestlé opens first railway NESCAFÉ kiosk*. https://www.indianretailer.com/news/nestle-opens-first-railway-nescafe-kiosk',
  'Indian Retailer. (2025). *Nestlé expands NESCAFÉ ready-to-drink coffee in India and key global markets*. https://indianretailer.com/news/nestle-expands-nescafe-ready-drink-coffee-india-and-key-global-markets',
  'Kotler, P., Keller, K. L., & Chernev, A. (2022). *Marketing management* (16th ed.). Pearson.',
  'Manifest Media. (2026, August 5). *Nescafé stirs up a sibling conversation about ambition*. https://manifest-media.in/video/campaigns/050826/nescaf-stirs-up-a-sibling-conversation-about-ambition.html',
  'Mintel. (2025). *India coffee market report*. https://store.mintel.com/report/india-coffee-market-report',
  'NESCAFÉ India. (n.d.). *NESCAFÉ Classic*. https://nescafe.com/in/coffees/classic',
  'Nestlé India. (n.d.-a). *At a glance*. https://nestle.in/about-us/at-a-glance',
  'Nestlé India. (n.d.-b). *Nestlé India partners with gaming streamers for NESCAFÉ Ready-to-Drink cold coffee range* [Press release]. https://www.nestle.in/media/pressreleases/allpressreleases/nestle-india-partners-gaming-streamers-nescafe-ready-drink-cold-coffee-range',
  'Nestlé India. (n.d.-c). *NESCAFÉ Sunrise unveils new campaign honouring coffee farmers* [Press release]. https://www.nestle.in/media/pressreleases/allpressreleases/nescaf%C3%A9-sunrise-unveils-new-campaign-honouring-coffee-farmers',
  'Nestlé India. (2024, July 25). *Press release: Financial results Q1 2024-25*. https://www.nestle.in/sites/g/files/pydnoa451/files/2024-07/Press%20Release.pdf',
  'Nestlé India. (2026a, April). *Press release: Financial results FY 2025-26*. https://www.nestle.in/sites/g/files/pydnoa451/files/2026-04/Press%20Release.pdf',
  'Nestlé India. (2026b, July). *Unaudited financial results for the quarter ended 30 June 2026*. https://www.nestle.in/sites/g/files/pydnoa451/files/2026-07/BSENSEUFRs30062026signed.pdf',
  'Nestlé Professional India. (n.d.). *NESCAFÉ Classic coffee single serve*. https://nestleprofessional.in/beverages/nescafe-classic-coffee-single-serve',
  'Press Information Bureau. (2025). *[Coffee sector backgrounder]*. https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/jan/doc2025120487201.pdf',
  'Reuters via Yahoo Finance. (2025, February). *Nestle India considering price hikes to counter commodity inflation, executive says*. https://finance.yahoo.com/news/nestle-india-considering-price-hikes-114230767.html',
  'Tata Consumer Products. (n.d.). *Tata Coffee Grand*. https://www.tataconsumer.com/brands/coffee/tata-coffee-grand',
  'Ventura Securities. (2026). *FMCG major Nestle India share price jumps over 7% after Q4 FY26 results*. https://www.venturasecurities.com/news/stocks/fmcg-major-nestle-india-share-price-jumps-over-7-after-q4-fy26-results-details-inside/',
  'Wikipedia. (2026a). *Nescafé*. https://en.wikipedia.org/wiki/Nescaf%C3%A9',
  'Wikipedia. (2026b). *Nestlé India*. https://en.wikipedia.org/wiki/Nestl%C3%A9_India',
];
refs.forEach((r) => body.push(new Paragraph({ children: L.runs(r, { size: 19 }), spacing: { after: 100, line: 264 }, indent: { left: 400, hanging: 400 } })));
add(H2('Image credits'));
add(B([
  'Cover: “Roasted coffee beans on the surface. 01” — A S M Jobaer, Wikimedia Commons, CC BY-SA 4.0.',
  'NESCAFÉ Classic sachets — Marwan Bello, Wikimedia Commons, CC BY-SA 4.0.',
  'Kirana shop — Renzilde, Wikimedia Commons, CC BY-SA 3.0.',
  'All charts and diagrams — created by the author from the cited data.',
]));

// 16 Appendix
add(H1('Appendix'));
add(P('Printable versions of all instruments are also provided in the separate *Interview Toolkit* document.', { run: { italics: true } }));
add(H2('A. Interview consent statement'));
add(NOTE(null, [
  'I am a PGDM student at Goa Institute of Management conducting a short interview for my Foundation of Marketing coursework on coffee buying and NESCAFÉ Classic. The interview takes about 20–30 minutes. Participation is voluntary; you may skip any question or stop at any time. With your permission, I will audio-record the conversation only to transcribe it accurately. Your name will not appear in the report — you will be identified only by a code (e.g., R3). The information will be used only for academic purposes and deleted after evaluation.',
  'Consent: ☐ I agree to participate   ☐ I agree to audio recording',
  'Respondent code: ______   Signature/verbal consent recorded: ______   Date: ______',
]));
add(SP());
add(H2('B. Interview response template (one per respondent)'));
add(T(['Field', 'Response'], [
  ['Respondent code / stakeholder type', ''], ['Date, time, mode, duration', ''], ['Q1 Consumption habits', ''], ['Q2 Brand awareness', ''], ['Q3 Last purchase (where/what/why)', ''], ['Q4 Preparation', ''], ['Q5 Likes / dislikes', ''], ['Q6 Price perception', ''], ['Q7 Brand personality', ''], ['Q8 Competitor experience', ''], ['Q9 Ad recall', ''], ['Q10 Satisfaction / recommendation', ''], ['Q11 Loyalty', ''], ['Q12 Improvement', ''], ['Interviewer observations', ''],
], [2.2, 5], { size: 17, firstColFill: true, firstColBold: true }));
add(H2('C. Three-level coding template (course format)'));
add(T(['Verbatim', 'First-level in-vivo coding', 'Second-level categories', 'Third-level aggregate dimensions'], [
  ['[quote R_]', '[ ]', '[ ]', '[ ]'], ['[quote R_]', '[ ]', '[ ]', '[ ]'], ['[quote R_]', '[ ]', '[ ]', '[ ]'],
  ['Proposition P_: [Category] influences [behaviour] of [segment] towards NESCAFÉ Classic.', '', '', ''],
], [3.4, 1.6, 1.4, 1.6], { size: 17 }));

const doc = new d.Document({
  creator: 'PGDM BDA student, Goa Institute of Management', title: 'NESCAFÉ Classic Marketing Analysis', description: 'Foundation of Marketing assignment report',
  styles, numbering, features: { updateFields: true },
  sections: [
    { properties: { page }, children: cover },
    { properties: { page }, ...headerFooter('NESCAFÉ Classic in India — Marketing Analysis'), children: [...toc, ...body] },
  ],
});
d.Packer.toBuffer(doc).then((b) => { fs.writeFileSync(out, b); console.log('wrote', out); });
