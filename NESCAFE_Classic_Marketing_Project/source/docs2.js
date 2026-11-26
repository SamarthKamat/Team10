const fs = require('fs');
const L = require('./lib');
const { d, C, H1, H2, H3, P, B, N, PB, SP, T, NOTE, styles, numbering, headerFooter, page, Paragraph, TextRun, AlignmentType } = L;

function titleBlock(t, sub) {
  return [new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: t, font: 'Cambria', size: 44, bold: true, color: C.red })] }),
    new Paragraph({ spacing: { after: 300 }, children: [new TextRun({ text: sub, italics: true, size: 24, color: C.brown })] })];
}
function save(name, header, children) {
  const doc = new d.Document({ styles, numbering, sections: [{ properties: { page }, ...headerFooter(header), children }] });
  return d.Packer.toBuffer(doc).then((b) => { fs.writeFileSync(name, b); console.log('wrote', name); });
}

// ================= SCRIPT =================
const slides = [
  [1, 'Cover — NESCAFÉ Classic in India', '0:30',
    'Good morning, Professor. My project is on NESCAFÉ Classic — the red-cap instant coffee that most of us have probably had in a hostel room at midnight before an exam. India is still a tea country, so I wanted to understand how a coffee brand wins people over here — who it targets, how it positions itself, and whether its product, communication and distribution actually fit together. Along with the secondary research, I have designed a qualitative interview study for the viva component.',
    'Hook with a familiar moment; state the question the deck answers.', 'Why did you choose NESCAFÉ Classic rather than the whole NESCAFÉ brand? (Answer: the brief asks for one product; Classic is the flagship and the entry SKU, which makes STP choices very visible.)'],
  [2, 'From Nestlé to NESCAFÉ Classic', '0:35',
    'I want to separate three levels, because they get mixed up easily. Nestlé India is the company — here since 1912, incorporated in 1959, with a portfolio from MAGGI to KitKat. NESCAFÉ is the brand, launched globally in 1938, and in India it covers instant coffee, ready-to-drink cold coffee and vending. NESCAFÉ Classic is my product: 100% pure instant coffee with a strong aroma, sold from a single sachet up to a 90-gram jar. Its value proposition, in one line, is a real-coffee kick in seconds from India’s most available coffee brand.',
    'Company ≠ brand ≠ product.', 'What is the difference between a brand and a product here?'],
  [3, 'Recent developments', '0:40',
    'What has been happening recently? First, Nestlé India’s growth has picked up sharply — total sales grew about 25% in the April-to-June 2026 quarter and 20.5% in July-to-September — and the company says this growth is volume-led, with NESCAFÉ Classic and Sunrise named specifically. Second, Nestlé launched ready-to-drink cold coffee in 2025 using gaming streamers — clearly aimed at Gen Z. Third, the new “Make Your World” campaign uses a full rap jingle and a first-day-of-college story. And on the other side, HUL relaunched BRU Gold with film stars. So the takeaway is: Nestlé is pushing hard on youth and quick commerce, and competitors are responding.',
    'Growth is volume-led → more households, not just higher prices.', 'Is the growth because of price increases? (Answer: management describes it as volume-led; there were price actions in 2025 due to coffee inflation, but recent quarters cite double-digit volume growth.)'],
  [4, 'Industry analysis', '0:40',
    'Now the industry. India consumed about 91,000 tonnes of coffee in 2023, compared with 84,000 tonnes in 2012 — slow growth on a small base. About half of Indians drink coffee, mostly at home. Cold coffee is interesting: it is only 0.2% of the cold-beverage market, but ready-to-drink cold coffee has grown around 23% a year. On the right, you can see that e-commerce — mostly quick commerce — already makes up 18% of FMCG sales in the top eight metros. So the opportunity is creating new coffee drinkers, while the challenges are tea, coffee-price inflation, and cheaper chicory blends.',
    'Small market + youth + new channels = headroom.', 'Why not use market-share numbers? (Answer: published estimates conflict — 40% vs 33% — and use different definitions, so I flagged them rather than present one as fact.)'],
  [5, 'Competitor analysis', '0:40',
    'There are three major national competitors. BRU from HUL — its regular Instant is a coffee–chicory blend with strong South-Indian heritage, and BRU Gold is its premium pure coffee. Tata Coffee Grand uses decoction crystals and plantation storytelling. Continental, from CCL, plays on value. NESCAFÉ Classic’s position is in the middle: it is 100% pure coffee, so it is more coffee-forward than the blends, but it is not as premium as Gold or the D2C brands. That middle is both its strength and its risk — it can be squeezed from below on price and from above on quality.',
    'Squeezed middle: blends below, premium instants above.', 'What is chicory, and why does it matter? (Answer: a roasted root blended with coffee — cheaper, fuller body, preferred in South-Indian filter style; it lowers cost and changes taste.)'],
  [6, 'Segmentation', '0:35',
    'For segmentation I used all four bases. Demographically, 18-to-35-year-olds. Geographically, North and West India are now the growth engines, while the South prefers chicory blends. Psychographically, self-made achievers and café aspirers. And behaviourally — which I think is the most useful base — whether someone is a first-time trier or a loyal user, and the occasion: studying, working, or making cold coffee. Combining these gives five candidate segments, from Aspiring Starters to South-Indian Tradition Seekers. These are hypotheses that my interviews will test.',
    'Behavioural base is most actionable.', 'Which segmentation base is most important for Classic and why?'],
  [7, 'Targeting', '0:35',
    'At the portfolio level, Nestlé uses differentiated targeting — Sunrise for value and chicory lovers, Classic for mainstream young adopters, Gold for premium upgraders and RTD for on-the-go. For Classic itself, the primary target is Aspiring Starters and young Hustlers aged 18 to 30. They need energy and an affordable real coffee, they live in hostels and shared flats, and they buy small packs and top up on quick commerce. The secondary target is urban family buyers and first-time triers, who want value and a trusted brand.',
    'Primary = 18–30 starters; secondary = family buyers.', 'Is this undifferentiated, differentiated or concentrated targeting?'],
  [8, 'Positioning', '0:40',
    'This perceptual map is my own judgement — it is not survey data — with price tier on the x-axis and how coffee-forward the product is on the y-axis. Classic sits upper-middle: accessible quality. My proposed positioning statement is: for young Indians starting something new, NESCAFÉ Classic is the 100% pure instant coffee that turns every ambition into a ready-in-seconds ritual. The functional benefits are speed, energy and aroma; the emotional benefits are confidence and a personal ritual.',
    'Classic owns “accessible real coffee + ambition”.', 'How would you validate this perceptual map? (Answer: ask interviewees to rank brands on price and quality, or run a small survey and use multidimensional scaling.)'],
  [9, 'Product strategy', '0:35',
    'On product, the three levels are: the core benefit — energy and coffee pleasure; the actual product — 100% pure coffee, the aroma, the red-cap jar and sachets; and the augmented product — recipes, availability and Nestlé’s quality assurance. For product mix, I kept scope separate: width is the number of lines Nestlé India has; line length is the items in NESCAFÉ — Classic, Sunrise, Gold and RTD; and depth is the variants of Classic — jars, pouches and sachets. The recent extension is the Classic Latte can in the RTD range.',
    'Width = company; length = NESCAFÉ line; depth = Classic variants.', 'Give an example of product depth for Classic.'],
  [10, 'Branding & communication', '0:40',
    'NESCAFÉ has told one story for over a decade — coffee as the start of something new — from “It All Starts with a NESCAFÉ” in 2014 to “Make Your World” today. I tested synergy on four points: the message is about ambition, the media is YouTube, Instagram and gaming, the personality is young and energetic, and the segment is students and young professionals. All four align. But I found three gaps: family buyers get little tailored messaging, the “100% pure” proof is under-told, and creator content is mostly for RTD rather than Classic.',
    'Message, media, personality and segment all aligned.', 'What does “synergistic with the target segment” mean in practice?'],
  [11, 'Distribution', '0:35',
    'Distribution is indirect and multi-channel. General trade — the kiranas — gives reach, and Nestlé reported covering about two lakh five thousand villages in 2024. Modern trade gives visibility, e-commerce offers multipacks, and quick commerce — Blinkit, Zepto, Instamart — is now a key growth driver. What I like is that the channels mirror the targets: kiranas serve family buyers and Tier-2 towns, while quick commerce serves students and young professionals in metros. The risk is price conflict between channels, which is why channel-specific packs matter.',
    'Channel split mirrors target split.', 'Is quick commerce a threat to kiranas?'],
  [12, 'Qualitative research design', '0:35',
    'For the viva component I designed a qualitative study. It is purposive and multi-stakeholder — at least five interviews: two students, one young professional, one family buyer and one retailer, plus a lapsed user if possible. Interviews are semi-structured, around 25 minutes, recorded with consent and anonymised. My guide has twelve open-ended questions covering habits, awareness, motivation, price, brand personality, competitors, satisfaction, loyalty and improvements.',
    'Purposive, multi-stakeholder, n ≥ 5, consent first.', 'Why include a retailer? (Answer: a retailer sees pack-size, scheme and channel behaviour across many buyers — a view no single consumer has.)'],
  [13, 'Analysis framework (placeholder)', '0:30',
    'I want to be transparent: my interviews are still pending, so this slide shows the framework, not findings. I follow the three-level coding from our class example — the exact verbatim, a first-level in-vivo code in the respondent’s own words, a second-level category like convenience, and an aggregate dimension like attitudinal beliefs. The eight themes shown are only candidates. After the interviews I will replace them with evidence, and write propositions such as: convenience influences young consumers’ adoption of NESCAFÉ Classic.',
    'Framework now, findings only after real interviews.', 'What is in-vivo coding? (Answer: labelling a quote using the respondent’s own words before abstracting into categories.)'],
  [14, 'SWOT', '0:30',
    'The SWOT pulls everything together. Strengths: leadership, pure coffee, reach and a consistent youth platform. Weaknesses: pricier than blends and less premium than Gold. Opportunities: low consumption, year-round cold coffee and habit formation at college and first jobs. Threats: coffee-price inflation and premium competitors like BRU Gold, Tata Grand Premium and Percol. So: a strong engine, but a squeezed middle.',
    'Strong engine, squeezed middle.', 'Which threat is most serious, in your view?'],
  [15, 'Recommendations & 3-month plan', '0:50',
    'My five recommendations each fix a gap I found. One, a quick-commerce First-Cup Kit — a small jar, a mug and a recipe card — to drive trial. Two, make cold coffee a year-round ritual through creator recipes. Three, defend value in Tier-2 kiranas with sachet strips. Four, extend “Make Your World” to campuses at the start of college. Five, make “100% pure” tangible through origin and aroma stories. I combined them into a three-month plan I am calling “My First Mug” — please note this is my own proposal, not an existing NESCAFÉ campaign. Month one drives trial, month two builds habit on campuses, and month three drives repeat purchase and user stories, with a KPI at every stage. The budget split is illustrative.',
    'Trial → habit → advocacy, each with a KPI.', 'How would you measure the success of “My First Mug”? (Answer: new-to-brand buyers, 60-day repeat rate, QR scans and a pre/post brand-lift study on “real coffee”.)'],
  [16, 'Conclusion & references', '0:25',
    'To conclude: NESCAFÉ Classic’s STP, product ladder, communication and distribution are coherent, and growth is volume-led. The risk is being squeezed in the middle during coffee inflation. My recommendation is that Classic should own the “first coffee” moment of every new beginning. All sources are cited in APA style in the report. Thank you — I am happy to take questions.',
    'Own the “first coffee” of every new beginning.', 'If you had to cut one recommendation, which would it be and why?'],
];
const totalSec = slides.reduce((a, s) => { const [m, ss] = s[2].split(':').map(Number); return a + m * 60 + ss; }, 0);

const scriptKids = [
  ...titleBlock('Presentation Script', 'NESCAFÉ Classic in India — Foundation of Marketing · Prof. Shantanu Prasad'),
  NOTE('How to use this script', [
    `Total speaking time ≈ ${Math.floor(totalSec / 60)} min ${totalSec % 60} s for 16 slides (target 8–10 minutes).`,
    'Do not read the script word for word — learn the **key point** for each slide and speak around it.',
    'Pause after each slide’s takeaway. Point to the chart or diagram while you explain it.',
    'If time is short, shorten slides 6, 9 and 14; never skip slide 13’s honesty point about pending interviews.',
  ]),
  SP(),
  H1('60-second project introduction'),
  P('“Good morning. For this assignment I studied NESCAFÉ Classic — Nestlé India’s flagship instant coffee. I chose it because India is still a tea-drinking country, so a coffee brand has to *create* customers, which makes its STP and consumer-behaviour choices really visible. I covered all the sections in the brief: an introduction to Nestlé and the product, recent developments, the industry, competitors like BRU, Tata Coffee Grand and Continental, segmentation, targeting and positioning, product strategy, branding and communication, and distribution. Then I evaluated what is working, gave five recommendations and built a three-month marketing plan. For the viva, I designed a qualitative interview study with at least five stakeholders — students, a professional, a family buyer and a retailer. My central argument is simple: NESCAFÉ Classic is strongest when it owns the *first coffee* of every new beginning — the first day of college, the first job — and that is where its future marketing should focus.”'),
  H1('Slide-by-slide script'),
];
slides.forEach(([n, t, time, script, key, q]) => {
  scriptKids.push(H2(`Slide ${n}: ${t}`));
  scriptKids.push(new Paragraph({ spacing: { after: 100 }, children: [new TextRun({ text: `⏱ Approx. ${time} min`, bold: true, color: C.gold, size: 20 })] }));
  scriptKids.push(P('“' + script + '”'));
  scriptKids.push(T(null, [['**Key point to remember**', key], ['**Possible professor question**', q]], [1.5, 5], { size: 19, firstColFill: true }));
  scriptKids.push(SP(60));
});
scriptKids.push(H1('30-second project conclusion'));
scriptKids.push(P('“To sum up, NESCAFÉ Classic’s marketing is coherent: it targets young starters, positions itself as accessible real coffee, uses a good–better–best product ladder, speaks to youth through the right media, and reaches them through both kiranas and quick commerce. Its main risk is a squeeze between cheaper blends and premium instants during coffee inflation. My recommendation is to own the first-coffee moment — trial through quick commerce, habit through campuses and cold coffee, and value through kiranas. Once my interviews are complete, I will test these conclusions with real consumer evidence. Thank you.”'));
scriptKids.push(H1('Timing summary'));
scriptKids.push(T(['Slide', 'Title', 'Time'], slides.map((s) => [String(s[0]), s[1], s[2]]).concat([['', '**Total**', `**${Math.floor(totalSec / 60)}:${String(totalSec % 60).padStart(2, '0')}**`]]), [0.6, 4.5, 1], { size: 18 }));

// ================= VIVA =================
const viva = [
  ['What is marketing, in one line?', 'Creating, communicating and delivering value to chosen customers profitably. For NESCAFÉ Classic, that means making a quick, real-coffee experience valuable to young Indians and getting it to them everywhere.'],
  ['Explain STP.', 'Segmentation divides the market into groups with similar needs; targeting chooses which groups to serve; positioning designs the offer and image so the target sees it as distinct. STP comes before the 4Ps because the mix must fit the chosen segment.'],
  ['What bases did you use for segmentation?', 'All four: demographic (age 18–35, life stage), geographic (North/West vs South, metro vs Tier-2/3), psychographic (achievers, café aspirers) and behavioural (trier vs loyal, occasion, benefit sought). Behavioural is the most actionable for Classic.'],
  ['Who is Classic’s primary target and why?', '18–30-year-old “starters” — students and young professionals. Coffee habits form at life-stage changes, the brand’s current campaign is built around college freshers, and these consumers buy through quick commerce, where Nestlé is growing fastest.'],
  ['Is Nestlé using differentiated or concentrated targeting?', 'Differentiated at portfolio level — Sunrise, Classic, Gold and RTD serve different segments. Classic on its own is focused on young mainstream adopters, with families as a secondary target.'],
  ['What is Classic’s positioning?', 'Accessible, 100% pure “real coffee” that fuels ambition. It is above chicory blends on quality and below premium instants on price — the upper-middle of the map.'],
  ['What assumptions are behind your perceptual map?', 'It is my judgement, not survey data: price tier inferred from product type and communication; quality inferred from pure vs blend and freeze-dried vs spray-dried. I would validate it by asking interviewees to rank brands.'],
  ['Explain product mix width, line length and depth with this example.', 'Width = number of product lines Nestlé India has (dairy, prepared foods, confectionery, beverages). Length = items in the NESCAFÉ line (Classic, Sunrise, Gold, RTD). Depth = variants of Classic (24/45/90 g jars, pouches, sachets).'],
  ['What are the three levels of product for Classic?', 'Core: energy and coffee pleasure. Actual: 100% pure coffee, aroma, red-cap jar, sachets, brand name. Augmented: recipes, availability, Nestlé quality assurance, vending.'],
  ['What is a product line extension? Give an example.', 'Adding new items under an existing line/brand. The NESCAFÉ RTD “Classic Latte” can (2025) extends the Classic name into ready-to-drink cold coffee.'],
  ['How is NESCAFÉ’s communication synergistic with its target?', 'Message (ambition, new beginnings), media (YouTube, Instagram, gaming streams, quick-commerce ads), personality (young, energetic) and segment (students, young professionals) all point in the same direction.'],
  ['What gaps did you find in branding?', 'Little tailored messaging for family buyers, under-communicated “100% pure” proof, and creator content focused on RTD rather than Classic.'],
  ['Describe the distribution strategy.', 'Indirect and multi-channel: general trade for reach (~2,05,000 villages in 2024), modern trade for visibility, e-commerce for multipacks and quick commerce for urban top-ups. The channels mirror the target split.'],
  ['Who are the major competitors and how does Classic differ?', 'BRU (HUL), Tata Coffee Grand and Continental (CCL). Classic differs on 100% pure coffee, youthful brand imagery and availability; it is exposed to cheaper blends below and premium instants above.'],
  ['Why did you not quote a single market-share figure?', 'Sources conflict (about 40% for NESCAFÉ vs 33% for BRU) and use different definitions. Presenting one as fact would be misleading; syndicated data like NielsenIQ would be needed.'],
  ['Why qualitative interviews, and why these stakeholders?', 'Qualitative interviews reveal motivations and meanings that numbers miss. Multiple stakeholders — students, a professional, a family buyer and a retailer — give consumer and trade perspectives.'],
  ['How will you analyse the interviews?', 'Transcribe verbatim, assign in-vivo codes, group them into second-level categories, then aggregate dimensions (Gioia method), and finally link each theme to an insight and a marketing implication.'],
  ['What did your interviews find?', 'Be honest: “The interviews are [pending / completed]. [If pending:] I have prepared the guide, consent form and coding framework; I have not reported findings because I do not want to present assumptions as evidence. [If completed: summarise the 2–3 strongest themes with respondent codes.]”'],
  ['Explain your marketing plan.', '“My First Mug” is my own proposed 3-month plan — not a real NESCAFÉ campaign. Month 1 drives trial (quick-commerce kit), Month 2 builds habit (campus sampling), Month 3 drives repeat and advocacy (UGC contest, refill retargeting).'],
  ['Which KPIs would you track?', 'Trial: new-to-brand buyers and kit sell-through. Habit: 60-day repeat rate, QR scans. Distribution: numeric distribution in Tier-2 kiranas. Brand: “real coffee” attribute score in a brand-lift study. Efficiency: cost per new household.'],
];
const vivaKids = [
  ...titleBlock('Viva Preparation', '20 likely questions with student-friendly answers — NESCAFÉ Classic in India'),
  NOTE('Tips', ['Answer in two parts: the **concept** first, then the **NESCAFÉ Classic example**.', 'If you do not know a number, say so and explain where you would find it — never guess.', 'Always label the perceptual map, budget and campaign as your own analysis or proposal.']),
  SP(),
];
viva.forEach(([q, a], i) => {
  vivaKids.push(new Paragraph({ keepNext: true, spacing: { before: 180, after: 60 }, children: [new TextRun({ text: `Q${i + 1}. ${q}`, bold: true, color: C.red, size: 23 })] }));
  vivaKids.push(P(a));
});

// ================= TOOLKIT =================
const qGuide = [
  ['Tell me about a typical day — when and how do you drink coffee or tea?', 'When? With whom? Why then?'],
  ['What coffee brands come to mind first? What do you know about NESCAFÉ Classic?', 'Where did you first hear of it?'],
  ['Think about the last time you bought coffee. Where, which pack, and why that one?', 'Shop vs app? Pack size? Offer?'],
  ['How do you usually prepare it — hot, beaten, cold, with milk?', 'Any recipes you follow or saw online?'],
  ['What do you like most and least about NESCAFÉ Classic’s taste and aroma?', 'Compared with what?'],
  ['How do you feel about its price compared with other coffees? What would make you switch?', 'Is it worth it? Why?'],
  ['If NESCAFÉ Classic were a person, how would you describe them?', 'Age, personality, job?'],
  ['Have you used BRU, Tata Coffee Grand, Continental or café brands? How do they compare?', 'Why did you switch / not switch?'],
  ['Do you remember any NESCAFÉ advertising or social-media content? What did it say to you?', 'Did it change anything you did?'],
  ['How satisfied are you overall, and would you recommend it to a friend?', 'What exactly would you say?'],
  ['Would you keep buying it if a cheaper or newer brand were on offer? Why?', 'What would make you stay?'],
  ['If you could change one thing about NESCAFÉ Classic, what would it be?', 'Pack, taste, price, communication?'],
];
const blank = (n, cols) => Array.from({ length: n }, (_, i) => [`R${i + 1}`, ...Array(cols - 1).fill('')]);
const toolKids = [
  ...titleBlock('Interview Toolkit', 'Questionnaire · consent · response and analysis templates — NESCAFÉ Classic study'),
  NOTE('Read before interviewing', ['Minimum 5 interviews from different stakeholders (assignment requirement). Recommended mix: 2 students, 1 young professional, 1 family buyer, 1 retailer (+1 lapsed/competitor user).', 'Record only with consent. Use codes R1, R2 … never names. Transcribe within 24 hours.', 'Ask open questions; use probes; avoid leading questions such as “Don’t you think NESCAFÉ is better?”']),
  SP(),
  H1('1. Consent statement (read aloud or share)'),
  P('I am a PGDM student at Goa Institute of Management conducting a short interview for my Foundation of Marketing coursework on coffee buying and NESCAFÉ Classic. It will take about 20–30 minutes. Participation is voluntary; you may skip any question or stop at any time. With your permission, I will audio-record the conversation only to transcribe it accurately. Your name will not appear anywhere — you will be identified by a code. The information is for academic use only and will be deleted after evaluation.'),
  P('☐ I agree to participate      ☐ I agree to audio recording      Respondent code: ______      Date: ____________'),
  H1('2. Interview questionnaire (consumer version)'),
  P('**Warm-up:** Introduce yourself, explain purpose, confirm consent, note profile details (age band, city, occupation).'),
  T(['#', 'Main question', 'Probe'], qGuide.map((q, i) => [String(i + 1), q[0], q[1]]), [0.4, 4.6, 2.2], { size: 18 }),
  H2('Retailer / stakeholder version'),
  ...N(['Which coffee brands sell fastest in your store, and to whom?', 'Which pack sizes of NESCAFÉ Classic move most? Why?', 'How do schemes, margins and company sales visits affect which brand you push?', 'Have quick-commerce apps changed your coffee sales? How?', 'What do customers say when they ask for coffee — do they ask by brand?', 'What could NESCAFÉ do to sell more through your store?']),
  P('**Close:** “Is there anything else about coffee or NESCAFÉ you’d like to add?” Thank the respondent.'),
  H1('3. Respondent profile table'),
  T(['ID', 'Stakeholder type', 'Age band', 'Gender', 'City / tier', 'Occupation', 'Usual brand', 'Date / mode / duration'], blank(6, 8), [0.6, 1.4, 0.8, 0.8, 1, 1.1, 1, 1.3], { size: 17 }),
  H1('4. Interview response template (copy one per respondent)'),
  T(['Field', 'Notes / verbatim'], [['Respondent code & type', ''], ['Date, mode, duration', ''], ...qGuide.map((q, i) => [`Q${i + 1}`, '']), ['Non-verbal observations', ''], ['Interviewer reflections', '']], [1.6, 5.6], { size: 18, firstColFill: true, firstColBold: true }),
  PB(),
  H1('5. Three-level coding table (course format)'),
  P('Copy each meaningful quote verbatim, then code it. Highlight quotes that support a proposition.'),
  T(['Resp.', 'Verbatim', 'First-level in-vivo code', 'Second-level category', 'Third-level aggregate dimension'], blank(10, 5), [0.6, 3, 1.3, 1.3, 1.4], { size: 17 }),
  H1('6. Full analysis framework table'),
  T(['Respondent ID', 'Respondent profile', 'Key response', 'Initial code', 'Identified theme', 'Consumer insight', 'Marketing implication'], blank(6, 7), [0.8, 1.1, 1.6, 1, 1, 1.1, 1.2], { size: 16 }),
  H1('7. Theme analysis table'),
  T(['Theme', 'Supporting respondent evidence (codes + quotes)', 'Interpretation', 'Marketing implication'], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']], [1.2, 2.8, 1.6, 1.6], { size: 17 }),
  P('*Candidate themes to look for (do not assume they will appear):* convenience, price sensitivity, taste, aroma, brand trust, habit, availability, emotional connection, alternatives.', { run: { size: 19 } }),
  H1('8. From responses to marketing insight — step guide'),
  ...N(['**Familiarise:** read each transcript twice; note first impressions.', '**Code:** label each meaningful quote with the respondent’s own words (in-vivo).', '**Categorise:** group similar codes into second-level categories (e.g., “speed”, “no equipment” → Convenience).', '**Aggregate:** group categories into dimensions (e.g., Convenience + Cost → Attitudinal beliefs).', '**Check:** count how many respondents support each theme; note contradictions and outliers.', '**Interpret:** ask “what does this mean for consumer behaviour?” — write one insight per theme.', '**Implicate:** link each insight to STP, product, price, promotion or place.', '**Propose:** write a proposition, e.g., “P1: Convenience influences young consumers’ adoption of NESCAFÉ Classic.”', '**Report:** replace the placeholders in Sections 11–12 of the report and slide 13 of the deck.']),
];

Promise.all([
  save('Script.docx', 'Presentation Script — NESCAFÉ Classic', scriptKids),
  save('Viva.docx', 'Viva Preparation — NESCAFÉ Classic', vivaKids),
  save('Toolkit.docx', 'Interview Toolkit — NESCAFÉ Classic', toolKids),
]).then(() => console.log('total seconds', totalSec));
