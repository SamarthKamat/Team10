# -*- coding: utf-8 -*-
"""Interview sets, hypotheses and viva Q&A shared by the toolkit, viva kit and slides."""

HYPOTHESES = [
    ("H1", "Comfort and cushioning, not brand, are the main reasons runners choose a running shoe."),
    ("H1a", "For casual and style-led buyers, the Swoosh and brand image drive the choice."),
    ("H2", "Price is the main barrier to buying a Nike running shoe."),
    ("H2a", "A lower-priced Nike (Vegam Run) or discounts would trigger trial."),
    ("H3", "Regular runners trust ASICS more than Nike for fit and injury prevention."),
    ("H4", "Run clubs, coaches and peers strongly influence brand choice."),
    ("H5", "Fear of counterfeits makes buyers prefer stores or brand sites over marketplaces."),
    ("H6", "Store-staff recommendations decide many purchases in multi-brand stores."),
]

OPENING = ("Hi, I'm a PGDM student at GIM doing a short study on running shoes for my marketing course. "
           "It'll take about two to three minutes. Is it okay if I record this? Your name won't be used anywhere.")
CLOSING = "That's really helpful, thank you. Is there anything else about running shoes you'd like to add?"

# Each set: id, gender, role, who to find, list of (question, probe, captures, hypothesis), optional question
SETS = [
    ("R1", "Female", "Young-adult woman who runs or walks for fitness",
     "Woman, 20-30, runs or brisk-walks at least twice a week (any brand)", [
        ("Tell me a bit about your running. How did you start, and how often do you go?", "What got you started?", "Usage rate, motivation", "H4"),
        ("Which shoes do you run in right now, and how did you end up choosing them?", "Who or what helped you decide?", "Brand choice, decision process", "H1/H4"),
        ("When you think of Nike running shoes, what comes to mind?", "Any three words?", "Brand associations", "H1a"),
        ("What stops you, or would stop you, from buying a Nike running shoe?", "Is it price, fit, style or something else?", "Barriers", "H2"),
        ("Nike just launched a shoe called Vegam Run at around Rs 3,800. Would that interest you? Why or why not?", "Where would you expect to buy it?", "Reaction to entry product", "H2a"),
        ("Do you feel safe and comfortable running in your city? Does that affect when and where you run?", "Would a women's group run help?", "Women runners' needs", "H4"),
     ], "Where do you usually buy shoes: store, brand site or Myntra/Flipkart? Why?"),
    ("R2", "Female", "Mother who buys sports or running shoes for her child",
     "Mother of a 12-19 year old who plays sport or runs", [
        ("When your son or daughter needs new sports shoes, how does it usually happen?", "Who asks, who decides, who pays?", "Consumer vs purchaser", "H1a"),
        ("Which brands does your child ask for, and why do you think they want those?", "Friends? Instagram? Cricketers?", "Influence, brand image", "H1a/H4"),
        ("How much do you normally spend on a pair, and what do you look for?", "Comfort, durability, price?", "Price sensitivity, benefits sought", "H2"),
        ("What do you think of Nike compared with brands like Decathlon, Campus or Puma?", "Worth the extra money?", "Brand perception", "H2"),
        ("Have you ever worried about buying a fake branded shoe online?", "What do you do to avoid it?", "Counterfeit concern, channel", "H5"),
     ], "If Nike had a good shoe for around Rs 4,000, would you consider it for your child?"),
    ("R3", "Male", "Regular runner, club member (10K to half marathon)",
     "Man, 25-45, runs 20+ km a week, part of a running club or Strava group", [
        ("How long have you been running, and what are you training for right now?", "How many km a week?", "Usage rate, involvement", "H4"),
        ("Which running shoes do you own, and why those?", "What made you pick that model?", "Brand choice, benefits", "H1/H3"),
        ("How would you compare Nike with ASICS for running?", "Fit, comfort, durability, injuries?", "Competitive perception", "H3"),
        ("Where do you get advice on shoes: club members, coach, YouTube, store staff?", "Whose advice do you trust most?", "Influencers", "H4/H6"),
        ("Pegasus costs about Rs 13,000 now. How do you feel about that price?", "Do you wait for sales?", "Price perception", "H2"),
        ("What would make you choose Nike for your next pair?", "Anything Nike is missing?", "Unmet needs", "H1/H3"),
     ], "Have you used the Nike Run Club app or joined a Nike run? What was it like?"),
    ("R4", "Male", "College student or beginner runner",
     "Man, 18-24, started running or gym in the last year", [
        ("What made you start running or working out?", "Health, fitness tests, friends?", "Motivation, need recognition", "H4"),
        ("What shoes are you using right now, and how did you choose them?", "Budget?", "Decision process", "H2"),
        ("Do you see yourself as a 'runner'? Why or why not?", "Who counts as a real runner?", "Self-image, barrier", "H2a"),
        ("What does Nike mean to you?", "Running brand or style brand?", "Brand associations", "H1a"),
        ("If you had Rs 4,000 for running shoes, what would you buy and where?", "Would you look at Nike?", "Price point, channel", "H2a/H5"),
     ], "Would a free 5K training plan or group run make you more likely to try a brand?"),
    ("R5", "Male", "Ex-Nike user who switched, or a runner who has never bought Nike",
     "Man, any age, runs regularly and currently uses ASICS, adidas, Puma, Skechers or Decathlon", [
        ("Which brand do you run in now, and how long have you used it?", "What did you use before?", "Brand history", "H3"),
        ("Why did you choose it over Nike?", "Was there a specific moment or experience?", "Switching reasons", "H1/H2/H3"),
        ("What do you think Nike does well and badly in running?", "Any experience with fit or durability?", "Strengths, weaknesses", "H3"),
        ("What would it take for you to buy Nike again, or for the first time?", "Price, fit, advice?", "Win-back levers", "H2/H2a"),
        ("Did anyone recommend your current brand to you?", "Club, coach, shop?", "Influence", "H4/H6"),
     ], "Have you seen any Nike running ads recently? What do you remember?"),
    ("R6", "Male", "Owner of a multi-brand sports or shoe store",
     "Owner or manager of a local sports or footwear shop that stocks several brands", [
        ("Which running-shoe brands sell the most in your store?", "Which sell the least?", "Brand demand", "H2"),
        ("Who buys running shoes here: what kind of customers?", "Age, students, parents, serious runners?", "Customer profile", "H1a"),
        ("Do customers ask for a brand by name, or ask you to suggest one?", "How often do you recommend?", "Staff influence", "H6"),
        ("How does price affect what people buy?", "What's the most common price range?", "Price sensitivity", "H2"),
        ("How easy is it to get Nike stock compared with other brands?", "Margins, schemes, supply?", "Distribution", "-"),
        ("Do fake or 'first copy' shoes affect your business?", "Where do customers buy them?", "Counterfeits", "H5"),
     ], "Have customers asked about Nike's new Vegam Run?"),
    ("R7", "Male", "Staff member at a Nike partner store or mall sports store",
     "Salesperson or store manager at a Nike store or a large sports store", [
        ("Which Nike running models sell best here, and to whom?", "Pegasus, Vomero, entry models?", "Product demand", "H1"),
        ("What questions do customers usually ask before buying a running shoe?", "Fit, cushioning, price?", "Benefits sought", "H1"),
        ("When customers compare Nike with ASICS or adidas, what makes them decide?", "What do they say?", "Competitive decision", "H3/H6"),
        ("How much do sales and discounts drive buying?", "Do people wait for end-of-season sale?", "Promotion sensitivity", "H2"),
        ("Do customers check prices online while in the store?", "Do they buy online afterwards?", "Channel behaviour", "H5"),
     ], "Has anything changed since nike.com moved to Nykaa or since Vegam Run launched?"),
    ("R8", "Male", "Running coach, club organiser or race volunteer",
     "Coach or organiser of a running group, or a regular race volunteer", [
        ("How has running in this city changed in the last few years?", "More beginners? More women?", "Market trend", "H4"),
        ("What do beginners in your group usually run in, and what do you advise them?", "Price range?", "Influence, beginner needs", "H2/H4"),
        ("Which brands are most common in your group, and why?", "Has that changed?", "Brand share in community", "H3/H4"),
        ("How do you see Nike compared with other running brands?", "Anything Nike should do differently?", "Brand perception", "H3"),
        ("Do brands support your group or events? How does that affect members?", "Who does it well?", "Community marketing", "H4"),
     ], "Would a brand-supported 5K or training programme help your group?"),
]

WORD_ASSOC = "Word association: 'When I say Nike running shoes, what are the first three words that come to mind?' Then: 'If Nike were a person, what kind of person would it be?'"
RATING_BRANDS = ["Nike", "ASICS", "adidas", "Puma", "Skechers", "Decathlon (Kiprun)"]
RATING_ATTRS = ["Running-performance credibility", "Comfort", "Value for money", "Style", "Price level (1 = cheap, 10 = expensive)"]

# ---------------- Viva Q&A ----------------
VIVA = [
    # A. Basic
    ("A. Basic questions", [
        ("What is marketing?", "Marketing is creating, communicating and delivering value to customers so the company builds profitable relationships. For Nike Running, that means understanding what Indian runners need (comfort, fit, confidence, price), creating shoes and experiences for them, and reaching them through the right stores, apps and communication."),
        ("What brand and product did you choose?", "Nike, and specifically Nike running footwear in India. I focused on the Pegasus, Nike's everyday road-running shoe, and on the new Vegam Run, Nike's first shoe designed for India, launched on 1 November 2026."),
        ("Which industry does Nike Running belong to?", "The sports and athletic footwear industry, which is part of the wider footwear and sportswear market. Within athletic footwear, running shoes are the largest product type, at about 31.8% according to IMARC."),
        ("Who owns Nike, and how does it operate in India?", "NIKE, Inc. of Beaverton, Oregon. In India it entered in the mid-1990s through a licence with Sierra (SSIPL), later set up its own subsidiary, and now works through appointed retail partners, multi-brand stores, authorised marketplaces and a nike.com store operated by Nykaa since February 2026."),
        ("Who are Nike's main competitors in running in India?", "ASICS (the running specialist), adidas and Puma (the scale players), Skechers (comfort and walking) and Decathlon's Kiprun (value). Campus is a mass-market competitor for first-time buyers."),
        ("What is Nike Running's target market?", "Primary: urban runners and fitness-focused adults, roughly 18-40, in higher socio-economic classes. Secondary: beginners in metros and tier-2 cities, and teenagers whose parents buy for them. Vegam Run extends the target towards beginners."),
        ("How big is Nike in India?", "Nike India's reported FY25 sales were about Rs 1,380 crore, up 14%. That is less than half of adidas (about Rs 3,259 crore) and Puma (about Rs 3,200 crore). Skechers is also bigger, at about Rs 1,971 crore."),
        ("How big is Nike globally?", "FY26 revenue was $46.4 billion, flat on a reported basis. Running has grown double digits for five straight quarters, and again in Q1 FY27, led by the Vomero."),
    ]),
    ("B. Conceptual questions", [
        ("Explain STP using Nike Running.", "Segmentation: I split the market by demographics, geography, psychographics and behaviour, for example performance chasers, fitness balancers, cautious beginners and style-led buyers. Targeting: Nike targets performance chasers and fitness balancers as primary, and beginners and students as secondary. Positioning: innovation that helps every runner go further, with Vegam as the entry point and Pegasus and Vomero as the next step."),
        ("What are the four bases of segmentation?", "Demographic (age, gender, income, occupation), geographic (region, city tier, urban or rural, climate), psychographic (lifestyle, values, personality) and behavioural (usage rate, loyalty, occasion, benefits sought, user status, readiness). For running shoes, behavioural segmentation is the most useful, because a 30 km-a-week runner and a beginner need very different products."),
        ("What is the difference between strategic and tactical targeting?", "Strategic targeting decides whom the company creates value for: for Nike, serious and regular urban runners. Tactical targeting decides how to reach them efficiently: through run clubs, race expos, the NRC app, Strava, and marketplace searches for 'running shoes'."),
        ("What are target attractiveness and target compatibility?", "Attractiveness is how good a segment is: size, growth and profit. Compatibility is how well the company's resources and brand fit it. Beginners are very attractive (large and growing) but were less compatible until Vegam Run. Value-only buyers under Rs 2,500 are big but incompatible with Nike's premium brand, so Nike doesn't target them."),
        ("What are POPs and PODs?", "Points of parity are what you must match to be considered, like comfortable cushioning and durability. Points of difference are what make you better, like Nike's innovation (ZoomX, super shoes), brand aspiration and running community. Each POD should be desirable, deliverable and differentiating."),
        ("Write Nike Running's positioning statement.", "For urban Indian runners who take their running seriously, Nike Running is the performance running brand that helps you run further and faster than you thought you could, because its shoes are built on the innovations elite athletes race in."),
        ("What is customer perceived value?", "It is total benefits minus total costs as the customer sees them. For Nike, the functional benefit is cushioning and durability, the emotional benefit is feeling like a real runner, and the social benefit is recognition. The costs are a high price and the effort of avoiding fakes and finding the right fit."),
        ("Explain the product life cycle with Nike.", "The running category in India is in growth. The Pegasus franchise is in maturity, extended by modifying it every year (41, then 42). The Vomero is in renewed growth. Vegam Run is in introduction, so its priority is awareness, trial and distribution."),
        ("What are the three levels of product for the Pegasus?", "Core: comfortable, injury-free running and confidence. Actual: the shoe itself (ReactX foam, Air Zoom, mesh upper, design, Swoosh, box). Augmented: the NRC app's training plans, store fitting, exchange policy and run-club events."),
        ("Explain brand equity using Nike.", "Using Keller's pyramid: salience is very high; performance associations are strong; imagery is aspirational; judgements are split between 'best quality' and 'overpriced'; feelings are excitement and pride; resonance is strong only where Nike runs communities. In India, Nike's brand equity is ahead of its sales."),
        ("What is the difference between consumer and purchaser?", "The consumer uses the product and the purchaser pays for it. For a teenager's running shoes, the teen is the consumer and influencer and the parent is the purchaser. Communication must therefore convince the teen and reassure the parent on value and genuineness."),
        ("Explain the 7Ps using Nike Running.", "Product: the Vegam, Pegasus and Vomero ladder. Price: Rs 3,795 to Rs 19,295. Place: partner stores, MBOs, the Nykaa-run nike.com and marketplaces. Promotion: campaigns, athletes and community runs. People: store staff and Nike Run Coaches. Process: online ordering, two-day metro delivery and exchanges. Physical evidence: stores, the orange box, the app and reviews."),
        ("Explain the buying decision process for a running shoe.", "Need recognition (start running, old shoes worn out), information search (club members, YouTube, store staff), evaluation of alternatives (fit, cushioning, price, brand), purchase (store or online, often in a sale) and post-purchase (comfort, injury, durability, which drive word of mouth)."),
        ("What is the 5C framework?", "Company, Customers, Competitors, Collaborators and Context. For Nike: a strong brand but a thin Indian network; urban runners and beginners; ASICS, adidas, Puma and Decathlon; Nykaa, Flipkart and run clubs; and GST, BIS rules, counterfeits and the running boom."),
        ("Give one example of each PESTEL factor.", "Political: Fit India. Economic: GST at 18% above Rs 2,500. Social: the running boom and more women running. Technological: super-shoe foams and running apps. Environmental: heat and monsoon. Legal: the BIS footwear Quality Control Order and anti-counterfeit cases."),
        ("What is IMC?", "Integrated marketing communications means all tools (advertising, PR, digital, events, endorsements, sales promotion) carry one consistent message. Nike's best example in India is the After Dark Tour, which combined an event, coaches, social media and PR around one message: women own the city at night."),
    ]),
    ("C. Analytical questions", [
        ("Why did you choose Nike Running?", "Running is India's fastest-growing sport, and Nike is the brand that invented much of modern running footwear. Yet Nike's India sales are far behind adidas and Puma. That gap between brand strength and market performance makes it an interesting marketing problem, and 2026 brought big changes: Nykaa, Vegam Run and the race-day system."),
        ("Why is Nike behind adidas and Puma in India?", "Mainly because of distribution and price. Nike cut its retail partners from about 350 to 150 and closed many stores after 2017, while adidas and Puma kept wide networks and value price points. Nike also had almost no running shoe under Rs 4,000 until Vegam Run."),
        ("How is Nike different from ASICS?", "ASICS is a running specialist known for comfort, fit and injury prevention, and it's strong in run clubs. Nike is broader: it is about innovation, speed, aspiration and athletes. ASICS wins the cautious, serious runner; Nike wins the aspirational one."),
        ("Is Nike Running positioned correctly in India?", "For serious urban runners, yes. For India's huge new-runner market, not fully. Its message feels like it's for 'real runners'. The 'Why Do It?' platform and Vegam Run are the right corrections, but they need local communication and wider distribution."),
        ("What is the significance of Vegam Run?", "It is Nike's first running shoe designed for India, built with Indian runners and taken from brief to product in 55 days. At a reported Rs 3,795 on Flipkart it lowers Nike's entry price by about Rs 9,000 versus the Pegasus. It is a price-ladder extension to recruit beginners."),
        ("Doesn't Vegam Run risk cheapening the brand?", "There is a risk of cannibalisation and dilution. That is why I recommend a clear Good-Better-Best ladder, one national price for Vegam, and a trade-up credit so buyers move to Pegasus or Vomero later rather than Nike discounting its premium shoes."),
        ("What did your interviews reveal?", "[Answer after the interviews. State how many people from which stakeholder groups, the 3-4 main themes with one short quote each, and which hypotheses were supported or not. Do not prepare this answer before the interviews are done.]"),
        ("What is the biggest marketing challenge for Nike Running in India?", "Converting brand love into sales among new runners. They know and like Nike but buy Decathlon or ASICS because of price, fit advice or club recommendations."),
        ("How does the GST change affect Nike?", "From September 2025, footwear up to Rs 2,500 has 5% GST and above that 18%. Nearly all Nike running shoes, including Vegam at Rs 3,795, are in the 18% slab, while value brands sit in the 5% slab, so the price gap is wider after tax."),
        ("Why did Nike move nike.com to Nykaa?", "Reports point to delivery delays, checkout problems, limited local warehousing and regulatory hurdles. Nykaa runs Nike's online store as a local service partner with free shipping and two-day metro delivery. Nike gets operational strength but gives up some direct control and features like Nike By You."),
        ("What improvements would you recommend?", "Four: (1) make Vegam the 'first Nike' with a beginner 5K programme; (2) offer fit labs and an online fit finder; (3) authenticate genuine products with QR codes and verified-seller badges; (4) expand Nike Run Club crews from three to ten cities with an Indian running ambassador."),
        ("What is your proposed marketing plan in one minute?", "A 12-month plan with an assumed Rs 45 crore budget and seven initiatives: First 5K with Vegam, NRC City Crews, Fit Lab, Trade-Up credit, Genuine Swoosh, an Indian running ambassador with After Dark expansion, and a marathon-season burst. Each has an objective, audience, timeline, budget and KPI, like 200,000 new NRC users and 15% trade-up from Vegam to Pegasus."),
        ("How did you build the perceptual map?", "The price axis uses actual India MRPs of each brand's core running shoe. The credibility axis is a provisional reading of positioning, which I'll replace with average ratings from my interview respondents' rating cards. The workbook replots it automatically."),
        ("Where does the Big Data Analytics angle come in?", "In the price comparison, the perceptual map built from respondent ratings, the coded interview analysis with theme counts, and the KPI dashboard for the plan. The plan also uses NRC and Strava data to personalise offers and measure the funnel."),
        ("What is Nike doing well in India?", "Community events like the After Dark Tour, local culture through NorBlack NorWhite, a running-led innovation pipeline (Vomero), and finally an India-specific entry shoe."),
        ("Why not just cut Pegasus prices?", "It would hurt margin and brand value, and Nike would still be far above Decathlon. It's better to compete on community, fit and innovation, and use Vegam as the low-price entry."),
        ("Which segment would you prioritise and why?", "Cautious beginners in metros and tier-2 cities. They are the largest, fastest-growing group, they are not yet loyal to any brand, and Vegam Run now makes them compatible with Nike."),
    ]),
    ("D. Critical questions", [
        ("What are the limitations of your research?", "No audited market size or market share for running shoes is available; prices change often; Nike India's revenue is from press reports of filings; most web pages were accessed through search copies; and the interviews are a small qualitative sample, so they show reasons and themes, not percentages."),
        ("How reliable are your secondary sources?", "I graded them. Nike's releases and government notices are high reliability but company claims are labelled as claims. Business papers like Business Standard and Mint are medium-high. Blogs and data vendors are used only for prices or context and are marked as indicative."),
        ("Why didn't you estimate Nike's market share?", "Because I couldn't verify it. Paid reports use different definitions, and inventing a number would be misleading. I used company revenues as a proxy instead."),
        ("Can five to eight interviews represent India?", "No, and they aren't meant to. Qualitative research explores why people behave as they do. The findings generate hypotheses that a larger quantitative survey could then test."),
        ("How should Nike communicate performance claims responsibly?", "Avoid implying a shoe prevents injury or guarantees speed, back claims with testing, and be honest about who a shoe is for. For beginners, focus on comfort, habit and community rather than records."),
        ("How can Nike respond to changing consumer preferences?", "By following the shift from performance-only to comfort, community and self-expression: growing Vomero for comfort, women's running events, India-specific design like Vegam, and digital community through NRC and Strava."),
        ("Isn't relying on cricketers a mistake for running?", "Cricket gives mass reach, which Nike needs in India. But it does not build running credibility, so I'd add Indian distance runners and club coaches as ambassadors for running."),
        ("What if Vegam Run fails?", "Early warning signs would be poor reviews and low repeat purchase. I'd use a wear-test panel with run clubs, fix issues in the next batch, and keep the community programme brand-led, so it still recruits runners to Pegasus even if Vegam needs changes."),
        ("Is your Rs 45 crore budget realistic?", "It's a planning assumption of about 3% of Nike India's reported FY25 sales. It isn't Nike data. The point is the allocation logic and the KPIs; the total can be scaled."),
        ("What about sustainability?", "Running shoes are hard to recycle. My Trade-Up programme collects old shoes for recycling, which adds a socially responsible angle and lowers the effective cost of upgrading."),
        ("How do counterfeits affect the brand?", "They reduce trust, especially online, and undercut genuine prices. Nike has won court cases in Delhi, but buyers still need a simple way to check authenticity, which is why I propose QR codes and verified-seller badges."),
        ("What would you do differently with more time?", "Run a structured survey of 150-200 runners to quantify the perceptual map, track Google Trends and marketplace review data over time, and observe more stores in tier-2 cities."),
    ]),
]
