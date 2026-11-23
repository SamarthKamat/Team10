# -*- coding: utf-8 -*-
"""Report content, part A: front matter text, introduction and Sections 1-5.

Markup used inside strings:
  [[key]] or [[key1;key2]]  -> in-text citation linked to the reference list
  **text**                  -> bold
Block types: see build_report.py
"""

TITLE = "NIKE RUNNING FOOTWEAR"
SUBTITLE = "A Comprehensive Marketing Management Analysis of Nike Running Footwear in the Indian Sports Footwear Market"

EXEC_SUMMARY = [
    "This report analyses Nike's running footwear business in India, using the core Nike Pegasus road-running shoe as the anchor product and the new India-built Vegam Run as the most important recent development. It applies the frameworks taught in the Marketing Management course (needs and value, consumer behaviour, research process, 5C and PESTEL, STP, POPs and PODs, product, brand, price, place and promotion) to verified secondary data from Nike, regulators, competitors and the business press.",
    "Running is Nike's strongest category worldwide right now. Nike reported five consecutive quarters of double-digit growth in Running, roughly $1 billion of added running revenue over that period, and double-digit growth again in Q1 FY27, led by the Vomero franchise [[nike_fy26;nike_q1fy27]]. In India the picture is different. Nike India's reported sales of about Rs 1,380 crore in FY25 sit well behind adidas (about Rs 3,259 crore) and Puma (about Rs 3,200 crore) [[fe_fit;open_decathlon]], after years of store closures and partner cuts [[outlook_nike;insideretail]].",
    "2026 marks a reset of Nike's India playbook. Nike moved its Indian online store to Nykaa from February 2026 [[nike_in_changes;afaqs_nykaa]], and on 1 November 2026 it launched Vegam Run, its first running shoe designed for India, at a reported Rs 3,795 through Flipkart and select stores [[nike_vegam;open_vegam]]. This is a clear shift from pure premium positioning towards a good-better-best price ladder.",
    "Our main finding is that Nike owns the most aspirational running brand in urban India but under-serves the fastest-growing group: first-time and early-stage runners in metros and tier-2 cities. These runners are price sensitive, fit-conscious and community-driven, and specialist rivals (ASICS in performance, Decathlon's Kiprun on value) are winning them [[fe_asics;fatm_kiprun]]. The proposed 12-month plan (Section 11) uses Vegam Run as the entry point, community running as the engine and authenticated, fit-led retail as the conversion point, with measurable KPIs at every step.",
    "The qualitative interviews required for the viva (minimum five stakeholders) are designed in the Interview Toolkit. Their findings will be added to Sections 5, 6 and 10 once the real interviews are complete. No interview results have been invented in this report.",
]

EXEC_FIGURES = [
    ("$46.4 bn", "Nike Inc. FY26 revenue, flat year on year [[nike_fy26]]"),
    ("Rs 1,380 cr", "Nike India FY25 sales, +14% [[fe_fit]]"),
    ("Rs 3,795", "Vegam Run launch price, Nov 2026 [[open_vegam]]"),
    ("69,000+", "Tata Mumbai Marathon 2026 runners [[tmm_2026]]"),
]

ABBREVIATIONS = [
    ("AOV", "Average order value"), ("ASP", "Average selling price"),
    ("BIS", "Bureau of Indian Standards"), ("D2C", "Direct to consumer"),
    ("EBO", "Exclusive brand outlet"), ("FY", "Financial year"),
    ("GST", "Goods and Services Tax"), ("GT", "General trade"),
    ("IMC", "Integrated marketing communications"), ("KPI", "Key performance indicator"),
    ("MBO", "Multi-brand outlet"), ("MRP", "Maximum retail price"),
    ("MT", "Modern trade"), ("NRC", "Nike Run Club"),
    ("PESTEL", "Political, Economic, Social, Technological, Environmental, Legal"),
    ("PLC", "Product life cycle"), ("POD / POP", "Point of difference / Point of parity"),
    ("QCO", "Quality Control Order"), ("Q-commerce", "Quick commerce (10-30 minute delivery)"),
    ("STP", "Segmentation, targeting and positioning"), ("SWOT", "Strengths, weaknesses, opportunities, threats"),
]

INTRO = [
    ("h2", "Purpose and scope"),
    ("p", "This report is the individual Marketing Management assignment for Term II of the PGDM (Big Data Analytics) programme. The faculty brief asks for one company and one product with a presence in the Indian market, analysed across 11 sections, with secondary sources acknowledged and qualitative interviews of at least five stakeholders for the viva."),
    ("table", "Scope of the study: company, brand and selected product", ["Level", "What it is", "Why it matters for this report"], [
        ["Company", "NIKE, Inc. (Beaverton, Oregon, USA), operating in India through its Indian subsidiary and appointed retail partners", "Sets global strategy, innovation pipeline and brand communication"],
        ["Brand", "Nike (the Swoosh), including the Nike Running sub-brand", "Carries the equity; Jordan and Converse are excluded"],
        ["Product category", "Nike road-running footwear sold in India", "The market the brief asks us to analyse"],
        ["Core product (focus)", "Nike Pegasus (current version Pegasus 42), Nike's everyday road-running shoe", "Deep product analysis in Section 7; comparable to rivals' core daily trainers"],
        ["Key new product", "Nike Vegam Run, launched 1 November 2026, designed for India", "The most important recent development and the basis of the proposed plan"],
    ], "Source: Author's scoping, based on Nike (2026a) and Nike India product pages.", None),
    ("h2", "Research approach"),
    ("p", "The study combines **exploratory secondary research** (company releases, regulator notices, competitor product pages, business press and industry report summaries) with **qualitative primary research** (semi-structured interviews with consumers, a parent, retailers and a channel partner). This follows the marketing research process from the course: define the problem, design the research, collect data, analyse it and present findings."),
    ("p", "The research problem is: **how can Nike grow its running footwear business in India when its global running momentum has not yet translated into Indian market leadership?** Three research questions follow from it: (1) who buys running shoes in India today and why; (2) how Nike's offer compares with ASICS, adidas, Puma, Skechers and Decathlon; and (3) which marketing actions would convert India's running boom into Nike sales."),
    ("fig", "sources", "Mix of secondary sources used in this report", "Source: Author's classification of the reference list (see References and the workbook Source_Log)."),
    ("h2", "How evidence is labelled"),
    ("ul", [
        "**Verified fact**: stated by an official or independent source, cited in the text.",
        "**Company claim**: stated by Nike or a competitor about itself (for example market-share gains). These are reported as claims.",
        "**Indicative**: prices and figures from retailer pages or trade press that change often. Prices were checked in November 2026 and are MRPs unless stated.",
        "**Author's analysis / proposal**: clearly marked, especially in Sections 10 and 11.",
    ]),
    ("box", "Note on data limits", [
        "No audited India market size or brand market share for running footwear is publicly available. Paid reports (Statista, Euromonitor, IMARC) were seen only as summaries, so this report does not estimate Nike's India market share.",
        "Most pages were accessed through search-engine copies because the research environment blocked direct access. Every link is listed in the workbook so it can be opened and checked before submission.",
    ]),
]

S1 = [
    ("h2", "1.1 NIKE, Inc.: company background"),
    ("p", "NIKE, Inc. began in 1964 as Blue Ribbon Sports, founded by runner Phil Knight and his University of Oregon track coach Bill Bowerman. It took the name Nike, after the Greek goddess of victory, and adopted the NIKE mark and the Swoosh in 1971 [[nike_about;lawbeat_nike]]. Running is therefore Nike's origin category: the brand was built on running shoes before basketball or sportswear."),
    ("p", "Today Nike is the world's largest sportswear company. In fiscal 2026 (year ending 31 May 2026) it reported revenue of **$46.4 billion**, flat on a reported basis and down 2% currency-neutral. Wholesale grew 4% while NIKE Direct fell, reflecting a deliberate return to retail partners [[nike_fy26]]. CEO Elliott Hill calls the turnaround plan **\"Win Now\"**, and it puts sport, and running first, back at the centre of the company [[nike_q4call]]."),
    ("table", "NIKE, Inc. at a glance (latest reported)", ["Indicator", "Value", "Source"], [
        ["FY26 revenue", "$46.4 bn (flat reported; -2% currency-neutral)", "Nike (2026b)"],
        ["FY26 net income", "$1.1 bn (includes tariff-refund benefit)", "Nike (2026b)"],
        ["Wholesale vs Direct, FY26", "Wholesale up; NIKE Direct down about 6-7%", "Nike (2026b)"],
        ["Running performance", "5 straight quarters of double-digit growth; about $1 bn added", "Nike (2026c)"],
        ["Q1 FY27 revenue (Jun-Aug 2026)", "$11.2 bn, -4%; Running up double digits, led by Vomero", "Nike (2026d)"],
        ["FY27 outlook", "Revenue expected to decline high single digits", "Nike (2026d)"],
    ], "Source: Compiled from Nike (2026b, 2026c, 2026d).", None),
    ("h2", "1.2 Nike in India"),
    ("p", "Nike entered India in the mid-1990s through a licensing arrangement with Sierra Industrial Enterprises (SSIPL). Sources differ on whether this was 1995 or 1996 [[outlook_nike;ssipl]]. SSIPL became Nike's first authorised Indian manufacturer and opened India's first Nike store in New Delhi in 1998 [[ssipl]]. Nike later ended the licence and operated through a wholly owned Indian subsidiary, while retail partners ran most stores [[bs_nike_stores]]."),
    ("p", "From around 2017 Nike sharply reduced its Indian footprint. It cut retail partners from about 350 to about 150 and closed around 200 outlets [[insideretail;outlook_nike]]. Current store counts vary by source, from 93 (June 2025) to more than 120 exclusive stores [[scrapehero;indiaretailing]]. Nike India's reported FY25 sales were about **Rs 1,380 crore, up 14%**, which is well behind adidas and Puma [[fe_fit]]."),
    ("fig", "timeline", "Nike in India: key milestones", "Source: Author's compilation from SSIPL Group (n.d.), Outlook Business (n.d.), Nike India (2026a) and Nike (2026a)."),
    ("h2", "1.3 Nike Running footwear: the product"),
    ("p", "Running footwear is a **shopping good** in the course's product classification. Buyers compare fit, cushioning, price and style across brands before buying, and many try shoes on in store. For serious runners the premium end behaves almost like a **specialty good**: they insist on a specific model (such as Pegasus or Vomero) and will search for it."),
    ("p", "Nike structures its running range by use. The **Pegasus** is the everyday trainer and has been in continuous production since 1983. **Vomero** is the max-cushion trainer that is driving Nike's current running growth [[nike_q1fy27]]. **Vaporfly and Alphafly** are race shoes, and from late 2026 Nike is adding the Swooshfly and Nike Apex to a \"race-day system\" for everyday runners [[nike_raceday;nike_swooshfly]]. Entry models complete the range, now led in India by the **Vegam Run** [[nike_vegam]]."),
    ("table", "Nike road-running range available in India (indicative MRPs, November 2026)", ["Tier", "Model(s)", "Purpose", "India MRP (Rs)", "Source"], [
        ["Entry / India-specific", "Vegam Run", "Accessible daily trainer for new runners", "3,795 (reported)", "Open Magazine (2026a)"],
        ["Core daily trainer", "Pegasus 42", "Everyday training, all distances", "12,995", "Nike India (n.d.-b)"],
        ["Previous core", "Pegasus 41", "Everyday training (older version)", "11,895", "Nike India (n.d.-c)"],
        ["Max cushion", "Vomero 18", "Comfort on long, easy runs", "13,295-14,995", "Nike India (n.d.-d)"],
        ["Premium daily", "Pegasus Premium", "Premium cushioning upgrade", "19,295", "[[nike_in_pegprem]]"],
        ["Race / super shoe", "Alphafly 4, Vaporfly, Swooshfly", "Racing", "Not verified for India", "Nike (2026e, 2026f)"],
    ], "Source: Nike India product pages and press reports, accessed November 2026. Prices change often and are indicative.", None),
    ("photo", "nike_cover.jpg", "Nike Pegasus 42 (student's own photograph)"),
    ("h2", "1.4 Brand identity, purpose and personality"),
    ("p", "Nike's stated mission is \"to bring inspiration and innovation to every athlete in the world\", with the line \"if you have a body, you are an athlete\" [[nike_about]]. The brand identity rests on three assets: the **Swoosh**, the **\"Just Do It\"** line (revived for a new generation as **\"Why Do It?\"** in September 2025 [[nike_whydoit]]) and its **athletes**. Using Aaker's brand-personality dimensions, Nike scores highest on **excitement** (daring, spirited) and **competence** (winning, reliable), with a strong edge of **ruggedness**."),
    ("h2", "1.5 Target consumers and geographic presence"),
    ("p", "In India, Nike Running has historically targeted urban, higher-income runners and aspirational sneaker buyers in the metros. Partner stores and the Nykaa-run nike.com reach most of the country, but physical presence is concentrated in tier-1 cities [[nike_in_care;nike_in_changes]]. Vegam Run's launch on Flipkart signals a deliberate push towards younger and tier-2 buyers [[open_vegam]]."),
    ("box", "Key takeaways: Section 1", [
        "Running is Nike's founding category and its fastest-growing category worldwide today.",
        "In India, Nike is a premium brand with a reduced store network and sales well below adidas and Puma.",
        "The analysis focuses on the Pegasus as the core product and the Vegam Run as Nike's new India-specific entry product.",
    ]),
]

S2 = [
    ("p", "The table below lists the most important developments from 2024 to November 2026, each with its date, source and marketing significance. They are grouped into Nike actions, market changes and competitor moves."),
    ("table", "Recent developments and their marketing significance", ["Date", "Development", "Source", "Marketing significance"], [
        ["Summer 2024", "Global campaign \"Winning Isn't for Everyone\", with the running follow-up \"Winning isn't Comfortable\"", "Nike (2024)", "A performance-first, competitive tone. It appeals to serious runners but can feel exclusive to beginners."],
        ["10 May 2025", "Nike After Dark Tour Mumbai 10K: 3,000+ women run from the Gateway of India", "[[nike_afterdark;nike_afterdark_mum]]", "Community-led brand building aimed at women runners, Nike's clearest India running activation."],
        ["10 Jun 2025", "Nike x NorBlack NorWhite India collection with Anshu Malik, Priya Mohan, Jemimah Rodrigues and Shafali Verma", "Nike (2025b)", "Local cultural relevance and Indian women athletes as brand faces."],
        ["Sep 2025", "\"Why Do It?\" relaunches \"Just Do It\" for Gen Z", "Nike (2025a); Marketing Dive (2025)", "Moves the message from winning to starting and keeping going, which suits new runners."],
        ["22 Sep 2025", "GST: footwear up to Rs 2,500 cut to 5%; above Rs 2,500 stays at 18%", "[[pib_gst;bt_gst]]", "Value brands (Campus, Decathlon entry ranges) gain a price advantage. Almost all Nike running shoes stay in the 18% slab."],
        ["Feb 2026", "Nike's India online store relaunches under Nykaa; Nike By You and SNKRS web end in India", "[[nike_in_changes;afaqs_nykaa;sgi_nykaa]]", "Nike outsources e-commerce operations to fix delivery and checkout problems. It also gains speed and loses some direct control."],
        ["Early 2026", "Shubman Gill fronts the global Nike Mind campaign; \"Born to Beat the Odds\" shot in Mumbai and Jaipur", "Marketing Mind (2026); MediaNews4U (2026)", "Cricket remains Nike India's main route to mass awareness, but cricket stars are not running credentials."],
        ["Apr 2026", "Pegasus 42 reaches India at Rs 12,995", "[[nike_in_peg42;fatm_peg42]]", "The core product's price rises about Rs 1,100 over Pegasus 41, widening the gap with value rivals."],
        ["Jun 2026", "BIS non-leather footwear QCO deadline extended to 31 Jul 2027", "[[bis_qco;bt_qco]]", "Compliance cost and supply planning for imported and locally made shoes."],
        ["30 Jun 2026", "Nike FY26 results: Running grows double digits for 5 quarters; \"Win Now\" strategy", "Nike (2026b, 2026c)", "Global priority and innovation budget are flowing to running."],
        ["1 Oct 2026", "Q1 FY27: Running up double digits; Max Cushioning share nearly triples, led by Vomero", "Nike (2026d)", "Vomero is a growth product to push in India's comfort-seeking market."],
        ["Oct 2026 onwards", "Race-day system: Alphafly 4 (Oct 2026), Nike Apex (Jan 2027), Swooshfly (Feb 2027)", "Nike (2026e, 2026f)", "Brings race-shoe benefits to everyday runners at more price points."],
        ["1 Nov 2026", "Vegam Run, Nike's first shoe designed for India, launches at a reported Rs 3,795 on Flipkart and in select stores", "[[nike_vegam;open_vegam;esquire_vegam;channeliam_vegam]]", "The biggest shift in Nike India's pricing and channel strategy in a decade (see Section 7)."],
    ], "Source: As listed in each row.", [1.0, 2.4, 1.3, 2.3]),
    ("h2", "2.1 Industry and competitor developments"),
    ("ul", [
        "**ASICS** expected 35-37% India growth in 2025, said running is growing about 19-20% a year, and aims to be the number one premium athletic footwear brand in India by 2029. It runs about 138 stores [[fe_asics;bt_asics]]. These are management claims.",
        "**Decathlon** brought its Kiprun running brand to India, with a Kipcore daily trainer at about Rs 4,999-5,999 and a carbon race shoe under Rs 20,000 [[fatm_kiprun;decathlon_kipcore]]. Decathlon's India revenue (Rs 4,133 crore in FY25) is larger than any sportswear brand's [[entrackr_decathlon]].",
        "**Quick commerce** is entering sports: Blinkit now sells sports goods from brands such as adidas, and a Zepto x adidas pilot has been reported [[inc42_blinkit;dfu_qc]]. Blinkit, Swiggy Instamart and Zepto together hold more than 85% of quick commerce [[mma_qc]].",
        "**Running participation** keeps rising: the Tata Mumbai Marathon grew from about 47,000 runners in 2019 to more than 65,000 in 2025, and more than 69,000 confirmed for 2026 [[print_marathon;tmm_2026]].",
    ]),
    ("h2", "2.2 What Nike is actually doing: strategies matched to actions"),
    ("p", "The faculty brief asks for actual business strategies and current tactics. The table links each Nike strategy to a dated, cited action."),
    ("table", "Nike's current strategies in India and the actions behind them", ["Strategy", "Actual action (date)", "Source"], [
        ["Return to sport, led by running (\"Win Now\")", "Running given priority in innovation and marketing; double-digit running growth (FY26 to Q1 FY27)", "Nike (2026c, 2026d)"],
        ["Price-ladder extension downwards", "Vegam Run at Rs 3,795, designed with Indian runners in 55 days (Nov 2026)", "Nike (2026a); Open Magazine (2026a)"],
        ["Asset-light digital channel", "nike.com India operated by Nykaa from Feb 2026", "Nike India (2026a)"],
        ["Rebuild wholesale and marketplace partners", "Vegam launched on Flipkart; authorised sellers include Ajio, Myntra, Flipkart, VegNonVeg, Superkicks", "Nike India (n.d.-a); Open Magazine (2026a)"],
        ["Community-led running marketing", "After Dark Tour Mumbai (May 2025); Nike Run Club chapters in Mumbai, Bengaluru and Delhi", "Nike (2025c); Sportskeeda (n.d.)"],
        ["Local cultural relevance", "NorBlack NorWhite collection (Jun 2025); Mumbai and Jaipur grassroots films", "Nike (2025b); MediaNews4U (2026)"],
        ["Protect brand equity", "Court action against counterfeit Swoosh and Jordan shoes (Apr 2024)", "LawBeat (2024)"],
    ], "Source: As listed in each row.", None),
    ("box", "Key takeaways: Section 2", [
        "2025-26 brought Nike's biggest strategic changes in India in a decade: Nykaa e-commerce, the Vegam Run and a return to wholesale.",
        "The GST change favours shoes under Rs 2,500, where Nike has almost no running offer.",
        "Competitors, especially ASICS and Decathlon, are investing heavily in Indian running.",
    ]),
]

S3 = [
    ("h2", "3.1 Industry overview and market structure"),
    ("p", "Running shoes sit inside the athletic or sports footwear market, which is itself part of India's wider footwear market. IMARC estimates that running shoes are the largest product type in Indian athletic footwear, at about **31.8% of the segment in 2025** [[imarc_athletic]]. The market is **two-tier**:"),
    ("ul", [
        "**Premium and performance**: Nike, adidas, Puma, ASICS, Skechers and smaller specialists (New Balance, Brooks, Hoka). Shoes usually cost Rs 6,000-20,000 [[nexdigm_sports]]. GlobalData ranked Nike, adidas and Puma as the top sports-footwear brands by value in 2021 [[globaldata]].",
        "**Mass and value**: Campus, Relaxo (Sparx), Bata (Power) and Decathlon's entry ranges. Shoes usually cost under Rs 3,000. Campus alone sold 24.9 million pairs at an average price of about Rs 639 [[ken_sportswear]].",
    ]),
    ("p", "This structure matters for Nike. Most of India's volume is in the value tier, where Nike has had almost no product until Vegam Run."),
    ("h2", "3.2 Market size and growth: what is and is not known"),
    ("p", "There is no reliable, public, audited figure for the size of India's running-footwear market. Statista and Euromonitor publish estimates behind paywalls [[statista_running;euromonitor]], and published summaries use different definitions. This report therefore uses **company revenues as a proxy for market scale** and does not estimate market share."),
    ("fig", "brand_revenue", "India revenue of major sportswear players (latest reported, Rs crore)", "Source: Financial Express (2026) for Nike; Open Magazine (2026b) for adidas, Puma, Skechers and Decathlon FY26; Financial Express (2025) for ASICS (industry estimate). Figures cover all categories, not only running, and years differ slightly."),
    ("p", "Two signals show the running segment is growing faster than footwear overall. ASICS's management estimates running in India grows about 19-20% a year [[fe_asics]], and race participation has risen steadily (see the chart below). KPMG, cited by Mint, estimates that marathons and distance running generate Rs 250-300 crore of spending a year on gear, travel and entry fees [[mint_running]]."),
    ("fig", "tmm", "Tata Mumbai Marathon participation, 2019-2026", "Source: ThePrint (2025) for 2019 and 2025; Procam International (2026) for 2026; 2024 figure as reported in press coverage. Organiser figures, not audited."),
    ("p", "Globally, running is the fastest-growing footwear category. In the US, running-shoe sales rose 13% in the first half of 2026, against 1% for footwear overall [[circana_run]]. Transaction data suggested Nike lost running share to Hoka, On, New Balance and adidas during 2025 [[yipit_run;sgi_running]], before its own recovery in FY26 [[nike_fy26;sgi_results]]. The same specialist brands are now entering India, so Nike's Indian running business faces global competition as well as local competition."),
    ("p", "After the GST change, footwear stocks such as Bata, Campus and Metro Brands rallied [[bs_gst_stocks]], but retailers reported little immediate lift in demand [[mint_gst]]."),
    ("h2", "3.3 Demand drivers and consumption trends"),
    ("ul", [
        "**Health and fitness after Covid**: running is cheap to start, needs no facility and fits busy schedules.",
        "**Community running**: running clubs have multiplied in every major city. The Delhi Runners Group alone has more than 11,000 members [[print_marathon]]. WhatsApp groups, Strava and weekend club runs make running social [[deccan_running]].",
        "**Women runners**: Nike's After Dark Tour drew more than 3,000 women in Mumbai [[nike_afterdark]], and safety and community are central to women's participation.",
        "**Athleisure**: many \"running shoes\" are bought for walking, gym and daily wear, so style and comfort often matter more than performance.",
        "**Online research and buying**: shoppers compare prices across Flipkart, Myntra, Ajio, Nykaa and brand sites, and watch reviewers before buying.",
    ]),
    ("h2", "3.4 PESTEL analysis"),
    ("table", "PESTEL analysis of the Indian running-footwear market", ["Factor", "Evidence", "Implication for Nike Running"], [
        ["Political", "Fit India and Khelo India programmes; Make in India push for local manufacturing", "Supports participation; favours brands that manufacture locally (ASICS targets 40% local production [[fe_asics]])"],
        ["Economic", "GST: 5% up to Rs 2,500, 18% above (from 22 Sep 2025) [[pib_gst]]; rising urban incomes; high price sensitivity", "Nike's Rs 3,795+ range carries 18% GST, while value rivals under Rs 2,500 pay 5%"],
        ["Social", "Running boom; 2.5 million people run at least one race a year (organiser claim) [[print_marathon]]; more women running; athleisure as daily wear", "A large and growing pool of new runners who need entry products and guidance"],
        ["Technological", "Foam technology (ZoomX, ReactX, Lightstrike, FF Blast); super shoes; running apps; e-commerce and quick commerce", "Innovation is Nike's strength, but rivals now match it at lower prices"],
        ["Environmental", "Heat, humidity and monsoon conditions; poor road surfaces; sustainability expectations", "Need for breathable uppers, grippy outsoles and durability, as Vegam Run's brief recognised [[nike_vegam]]"],
        ["Legal", "BIS QCO for non-leather footwear (deadline 31 Jul 2027) [[bis_qco]]; trademark enforcement against counterfeits [[lawbeat_nike]]; consumer-protection rules for e-commerce", "Compliance costs; counterfeit 'first copies' erode trust and price realisation"],
    ], "Source: Author's analysis using cited sources.", [1.0, 3.0, 3.0]),
    ("h2", "3.5 5C analysis (Session framework)"),
    ("table", "5C framework applied to Nike Running in India", ["C", "Assessment"], [
        ["Company", "Strong global innovation and brand; reduced Indian retail footprint; e-commerce now run by Nykaa; new Vegam Run entry product"],
        ["Customers", "Urban 18-40 runners and fitness walkers; aspirational students; women runners; parents buying for teenagers; price-sensitive tier-2 buyers"],
        ["Competitors", "adidas and Puma (larger India revenue), ASICS (running specialist), Skechers (comfort walking), Decathlon Kiprun (value), Campus (mass)"],
        ["Collaborators", "Nykaa (e-commerce), Flipkart, Myntra, Ajio, mono-brand franchise partners, MBO sports stores, run clubs, race organisers"],
        ["Context", "GST two-slab structure, BIS QCO, running boom, quick commerce, counterfeits, heat and monsoon"],
    ], "Source: Author's analysis.", [1.2, 5.8]),
    ("h2", "3.6 Opportunities and challenges"),
    ("table", "Industry opportunities and challenges", ["Opportunities", "Challenges"], [
        ["Millions of first-time runners entering the category", "High price sensitivity; most volume below Rs 3,000"],
        ["Tier-2 and tier-3 cities joining the running boom", "Counterfeits and grey-market imports"],
        ["Women's running and safety-led community events", "Fit and width issues: many Indian runners need wider fits"],
        ["Max-cushion and comfort shoes for walking and running", "Specialists (ASICS) and value players (Decathlon) taking share"],
        ["Running apps and data for personalised marketing", "Heavy discounting on marketplaces erodes brand value"],
    ], "Source: Author's analysis using Sections 2 and 3 evidence.", None),
    ("box", "Key takeaways: Section 3", [
        "The market is two-tier: Nike competes in the premium tier while most volume sits below Rs 3,000.",
        "Running is the fastest-growing sport in India, but no audited market size exists, so none is estimated here.",
        "GST, counterfeits and local manufacturing are the key context factors for Nike's pricing.",
    ]),
]

S4 = [
    ("p", "The brief warns against assuming every brand has equal relevance. Based on India revenue, retail presence and running-specific credibility, the direct competitors are **ASICS, adidas, Puma, Skechers and Decathlon (Kiprun)**. Campus is a mass-market competitor for first-time buyers. New Balance, Brooks, Hoka and On are niche in India and are noted but not analysed in depth."),
    ("table", "Competitor comparison matrix: running footwear in India", ["Dimension", "Nike", "ASICS", "adidas", "Puma", "Skechers", "Decathlon (Kiprun)"], [
        ["Ownership", "NIKE, Inc. (USA)", "ASICS Corp. (Japan)", "adidas AG (Germany)", "PUMA SE (Germany)", "Skechers USA", "Decathlon SA (France)"],
        ["India revenue (latest)", "~Rs 1,380 cr FY25 [[fe_fit]]", "~Rs 430 cr (est.) [[fe_asics]]", "~Rs 3,259 cr FY25 [[open_decathlon]]", "~Rs 3,200 cr [[open_decathlon]]", "~Rs 1,971 cr [[open_decathlon]]", "Rs 4,133 cr FY25, all sports [[entrackr_decathlon]]"],
        ["Core daily trainer (India MRP)", "Pegasus 42: Rs 12,995", "Novablast / Cumulus: ~Rs 12,999-15,999 [[fatm_kiprun;fatm_nova6]]", "Adizero EVO SL: Rs 15,999", "Velocity Nitro (price not verified)", "GoRun range (not verified)", "Kipcore: Rs 4,999-5,999"],
        ["Entry running shoe", "Vegam Run: Rs 3,795", "Entry Gel models", "Duramo / Runfalcon", "Entry softride ranges", "Go Walk / Go Run", "Jogflow: Rs 1,999"],
        ["Key technology", "ZoomX, ReactX, Air Zoom", "GEL, FF Blast", "Lightstrike, Boost", "Nitro foam", "Arch Fit, Ultra Go", "Kalensole and in-house foams"],
        ["Positioning", "Inspiration and innovation for every athlete", "Specialist running, injury prevention, comfort", "Performance plus sport culture", "Fast, sporty, cricket-led", "Comfort and walking", "Value for money, sport for all"],
        ["Brand faces / tactics in India", "Cricket (Shubman Gill), women athletes, After Dark Tour", "Run clubs, race sponsorships, gait analysis", "Cricket kit sponsor, running events", "Cricket and football athletes", "Cricket and Bollywood ambassadors", "In-store trial, own brands, events"],
        ["Distribution", "Partner EBOs, Nykaa-run nike.com, Flipkart, Myntra, Ajio, MBOs", "~138 stores, online [[fe_asics]]", "EBOs, MBOs, online", "EBOs, MBOs, online", "EBOs, MBOs, online", "Large-format own stores, online"],
        ["Main strength", "Brand aspiration and innovation", "Running credibility and fit", "Scale and cricket presence", "Scale and value pricing", "Comfort for walkers", "Price-performance"],
        ["Main weakness", "Price gap; reduced stores; low running specialist trust", "Smaller brand awareness", "Less running focus in India", "Weaker performance-running image", "Not seen as serious running", "Low aspiration"],
    ], "Source: Author's compilation. India prices from brand product pages and Fat Marathoner (2026b, 2026c), November 2026. 'Not verified' means a current India price was not found.", [1.1, 1.0, 1.0, 1.0, 0.9, 0.9, 1.1]),
    ("fig", "price_ladder", "Price ladder: India MRPs of comparable running shoes (November 2026)", "Source: Nike India (n.d.-b, n.d.-d); Open Magazine (2026a); adidas India (n.d.); Decathlon India (n.d.-a, n.d.-b, n.d.-c); Fat Marathoner (2026b, 2026c). Indicative MRPs."),
    ("h2", "4.1 Competitor profiles"),
    ("h3", "ASICS: the running specialist"),
    ("p", "ASICS is the most direct threat in performance running. It positions itself on running science and comfort, is reported to be the third-largest brand in India's high-end running segment after Nike and adidas, and aims to lead premium athletic footwear by 2029 [[fe_asics;fu_asics]]. Its marketing measures \"footprints\": run-club and race activity tracked as funnel metrics [[campaign_asics]]. Runners at clubs often see ASICS as the safe, injury-preventing choice."),
    ("h3", "adidas and Puma: the scale players"),
    ("p", "adidas (about Rs 3,259 crore) and Puma (about Rs 3,200 crore) are more than twice Nike's size in India [[open_decathlon]]. Both lean on cricket for mass awareness and on wide store networks. adidas's Adizero EVO SL (Rs 15,999) competes directly with Nike's performance trainers [[adidas_evo]]. Euromonitor puts Puma (6%) and adidas (5%) at the top of Indian sportswear overall [[euromonitor]]."),
    ("h3", "Skechers: the comfort player"),
    ("p", "Skechers South Asia's revenue (about Rs 1,971 crore) is above Nike India's [[open_decathlon]]. Skechers wins the large \"walking and comfort\" segment, which many Indian consumers think of as running shoes. Nike's Vomero and Vegam compete for this buyer."),
    ("h3", "Decathlon Kiprun: the value disruptor"),
    ("p", "Decathlon is India's largest sporting-goods retailer by revenue [[entrackr_decathlon]]. Its Kiprun range offers credible running shoes at Rs 1,999-9,999 and a carbon race shoe under Rs 20,000 [[decathlon_jogflow;decathlon_kipride;fatm_kiprun]]. For beginners, the Kipcore at about Rs 5,000 is the most direct rival to Vegam Run."),
    ("box", "Key takeaways: Section 4", [
        "Nike leads on brand aspiration but trails adidas, Puma and Skechers on India revenue.",
        "ASICS is the strongest threat with serious runners; Decathlon is the strongest threat with beginners.",
        "Nike's core Pegasus is priced at par with ASICS and adidas, but there is a gap of Rs 7,000-8,000 to value alternatives.",
    ]),
]

S5 = [
    ("p", "This section applies the four bases of consumer-market segmentation taught in class, then the Session 9 targeting concepts: strategic versus tactical targeting, target attractiveness versus target compatibility, and single- versus multi-segment targeting. Following the brief, it separates **consumers (who run)** from **purchasers (who pay)**."),
    ("h2", "5.1 Demographic segmentation"),
    ("table", "Demographic segmentation", ["Variable", "Segments relevant to Nike Running", "Evidence / rationale"], [
        ["Age", "15-22 students; 23-35 young professionals; 36-50 fitness-focused adults; 50+ walkers", "Running clubs are mostly 25-45; teenagers buy for style and school sport"],
        ["Gender", "Men (largest current buyer group); women (fastest-growing runners)", "3,000+ women at Nike After Dark Mumbai [[nike_afterdark]]"],
        ["Income / socio-economic class (ISEC)", "Upper classes (A1-A2) for Pegasus/Vomero; A3-B for Vegam Run", "Pegasus at Rs 12,995 is unaffordable for most households"],
        ["Occupation", "IT and corporate professionals, students, doctors, armed forces and police aspirants, coaches", "Corporate running clubs; fitness tests for uniformed services"],
        ["Education", "Graduate and above for performance runners", "Higher research involvement before purchase"],
        ["Family size and life cycle", "Young singles (self-purchase); young couples; parents with teenagers (buy for children)", "Parents act as purchasers for teen consumers"],
    ], "Source: Author's analysis; to be validated by interviews.", [1.2, 2.8, 3.0]),
    ("h2", "5.2 Geographic segmentation"),
    ("table", "Geographic segmentation", ["Variable", "Segments", "Implication"], [
        ["Region", "West (Mumbai, Pune), South (Bengaluru, Hyderabad, Chennai), North (Delhi NCR, Chandigarh)", "Running culture is strongest in Mumbai, Bengaluru and Delhi, where Nike Run Club operates [[nrc_delhi]]"],
        ["City tier", "Metros; tier-2 (Jaipur, Indore, Kochi, Goa, Lucknow); tier-3 and towns", "Tier-2 is the growth frontier; Vegam on Flipkart reaches it [[open_vegam]]"],
        ["Urban vs rural", "Urban dominant for performance running; rural for sports aspirants", "Rural buyers rely on local sports stores and are very price-driven"],
        ["Density and climate", "Hot and humid coasts; cold north in winter; monsoon months", "Breathability and grip matter; marathon season runs Nov-Feb"],
    ], "Source: Author's analysis.", [1.2, 2.9, 2.9]),
    ("h2", "5.3 Psychographic segmentation"),
    ("table", "Psychographic segments", ["Segment", "Lifestyle and values", "What they want from a running shoe"], [
        ["Performance chasers", "Train for half/full marathons, track pace on Strava, follow reviewers", "Proven performance, light weight, race shoes, data"],
        ["Fitness balancers", "Run or walk 3-4 times a week for health, busy jobs", "Comfort, cushioning, durability, value"],
        ["Social runners", "Join clubs for friendship and motivation", "Shoes that peers use; brand belonging; events"],
        ["Style-led aspirers", "Brand-conscious students and young professionals", "Swoosh visibility, colourways, gym-to-street use"],
        ["Cautious beginners", "Just starting, fear injury, unsure what to buy", "Guidance, affordable price, fit help"],
    ], "Source: Author's analysis; to be tested in interviews.", [1.4, 2.8, 2.8]),
    ("h2", "5.4 Behavioural segmentation"),
    ("table", "Behavioural segmentation", ["Variable", "Segments", "Nike relevance"], [
        ["Usage rate", "Heavy (30+ km/week), medium (10-30 km), light (<10 km or walking)", "Heavy users replace shoes every 6-9 months and are the most valuable"],
        ["Brand loyalty", "Nike loyal; switchers (Nike/ASICS/adidas); value-loyal (Decathlon, Campus)", "Switchers are the main battleground"],
        ["Purchase occasion", "Race-season preparation; New Year resolutions; festive sales; school/college start; gifting", "Time campaigns for Nov-Jan and festive sales"],
        ["Benefits sought", "Cushioning/comfort, speed, injury prevention, style, price", "Vomero = comfort; Pegasus = versatility; Vegam = price"],
        ["User status", "Non-user, first-time runner, regular user, ex-user", "First-time runners are under-served by Nike today"],
        ["Buyer-readiness stage", "Unaware, aware, interested, desire, action", "Beginners know Nike but don't see an affordable Nike running shoe"],
    ], "Source: Author's analysis.", [1.3, 2.9, 2.8]),
    ("h2", "5.5 Consumer versus purchaser and family influence"),
    ("p", "Running shoes are often bought by someone other than the runner. For teenagers and students, the **parent is the purchaser and payer** while the teenager is the **consumer and influencer** who names the brand. Gifting (birthdays, festivals) creates a similar split. For working adults, consumer and purchaser are usually the same person, but **influencers** (club leaders, coaches, YouTube reviewers, store staff) shape the choice. The buying decision process (need recognition, information search, evaluation, purchase, post-purchase) is long for performance shoes and short for style-led purchases."),
    ("h2", "5.6 Targeting strategy"),
    ("table", "Target attractiveness and target compatibility (Session 9)", ["Segment", "Attractiveness (size, growth, profit)", "Compatibility (fit with Nike resources and brand)", "Decision"], [
        ["Performance chasers (urban A1-A2)", "Medium size, high value, growing", "Very high: innovation, race shoes, Vomero/Pegasus", "Primary target"],
        ["Fitness balancers (urban A2-B)", "Large and growing", "High: Pegasus, Vomero, Vegam", "Primary target"],
        ["Cautious beginners (metro + tier-2, A3-B)", "Very large, fast growing, lower margin", "Medium, improving with Vegam Run", "Secondary target (growth)"],
        ["Style-led aspirers (students)", "Large; often bought by parents", "High brand fit, low performance need", "Secondary target"],
        ["Value-only buyers (below Rs 2,500)", "Very large volume, very low margin", "Low: would dilute premium image", "Not targeted"],
    ], "Source: Author's analysis using Session 9 framework.", [1.6, 1.8, 2.1, 1.3]),
    ("ul", [
        "**Strategic targeting** (who Nike creates value for): urban runners and fitness-focused adults who value innovation and performance. The Pegasus and Vomero are built for them.",
        "**Tactical targeting** (how Nike reaches them): run clubs, race expos, Strava and NRC app users, marketplace search ads for \"running shoes\", and partner stores near running hubs.",
        "**Targeting approach**: Nike uses **differentiated multi-segment targeting**, with a product tier per segment (Vegam for beginners, Pegasus for regular runners, Vomero for comfort seekers, Alphafly/Vaporfly for racers).",
    ]),
    ("h2", "5.7 Target personas"),
    ("table", "Illustrative target personas (composites for planning, not interview respondents)", ["Persona", "Profile", "Need", "Nike offer"], [
        ["\"Pune Pacer\"", "29, software engineer, runs 35 km a week, training for a half marathon", "Durable daily trainer plus a race-day shoe", "Pegasus 42 + Vomero 18; NRC training plans"],
        ["\"Bengaluru Balancer\"", "38, manager and parent, runs 3 times a week for health", "Comfort and injury prevention", "Vomero 18"],
        ["\"Jaipur Beginner\"", "21, college student, starting with a 5K, budget about Rs 4,000", "Affordable, trustworthy first shoe", "Vegam Run on Flipkart; beginner 5K plan"],
    ], "Source: Author's construction for planning. Personas are not research findings.", None),
    ("box", "Key takeaways: Section 5", [
        "Nike targets several segments, with a product tier for each.",
        "The biggest gap is cautious beginners in metros and tier-2 cities. Vegam Run is Nike's first real answer.",
        "Parents, coaches and club leaders influence purchases, so communication must reach them, not just runners.",
    ]),
]
