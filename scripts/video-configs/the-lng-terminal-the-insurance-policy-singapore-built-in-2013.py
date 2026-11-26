"""Video config for the LNG terminal post.

The pool is the post and gallery's eighteen pictures: Jurong
Island from the sea (the hero), the self-made locator map
and import-split chart, the Q-Max carriers Mozah and
Lijmiliya, Melkoya by day and at twilight, two carrier
views from Sembawang, the 2006 Jurong panorama, South Hook
and its jetty, the FSRU Independence, PacificLight's plant,
Negishi's tanks, Sabine Pass's loading arms, Cove Point
and Swinoujscie. There is no Commons photograph of the
SLNG terminal itself (a restricted site); the terminal's
own beats run on Jurong Island views and the locator map.

Named-place audit: the Melkoya pictures sit under the
liquefaction sentences that name the plant; the Mozah,
a Q-Max at Ras Laffan, carries the Qatargas commissioning
cargo; South Hook, a like-for-like import terminal,
carries only generic import-end and world-market
sentences; the FSRU Independence carries the floating-
terminal sentences, which name Jurong Port's ship as a
type, not as this vessel; the West Natuna sentences run
on carriers in Singapore waters, never on another named
place's photograph. Named-person audit: no portraits
exist in the pool; the sentences naming Lim Hng Kiang,
S Iswaran and PM Lee run on island and terminal views.

Every slide carries its discreet photo title (standing
rule, Chris, 2026-11-11): the short form of its image's
post/gallery caption, drawn small in the top corner on a
soft dark backing for the slide's whole run. The two
self-made graphics are letterboxed, not covered (the
Pipelines pattern): the chart fixed, so its heading,
axes and source line stay whole; the map with a modest
zoom. A cover crop clips all three - caught on the
first render's spot frames, 2026-11-26.

64 slides, 846.625s. No slide over 30s; the longest is
the 24 October 2026 sentence at 27.27s. Narration: Kokoro
with the OpenVoice clone. Pronunciation overrides for the
post's names filed 2026-11-26, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Jurong_Island%2C_Singapore_-_20110227-02.jpg/1280px-Jurong_Island%2C_Singapore_-_20110227-02.jpg",
    "MAP": "/assets/images/lng-terminal-locator-map.png",
    "MELKOYA": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/07647_NOR_Hammerfest_Melkoya_LNG_Terminal_V-P.jpg/1280px-07647_NOR_Hammerfest_Melkoya_LNG_Terminal_V-P.jpg",
    "MOZAH": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Mozah%2C_Nakilat%27s_flagship_vessel.JPG/1280px-Mozah%2C_Nakilat%27s_flagship_vessel.JPG",
    "CHART": "/assets/images/lng-import-split-chart.png",
    "SEMBAWANG": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Kapal_Pengangkut_LNG_dilihat_dari_Sembawang.jpg/1280px-Kapal_Pengangkut_LNG_dilihat_dari_Sembawang.jpg",
    "SOUTHHOOK": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/South_Hook_LNG_terminal_above_Little_Wick_-_geograph.org.uk_-_8315622.jpg/1280px-South_Hook_LNG_terminal_above_Little_Wick_-_geograph.org.uk_-_8315622.jpg",
    "FSRU": "https://upload.wikimedia.org/wikipedia/commons/0/05/FSRU_Independence_in_the_port_of_Klaip%C4%97da%2C_Lithuania.jpg",
    "PLP": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/PLPplant.jpg/1280px-PLPplant.jpg",
    "LIJMILIYA": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Lijmiliya_LNG_carrier_QatarGas.jpg/1280px-Lijmiliya_LNG_carrier_QatarGas.jpg",
    "SEMB21": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/LNG_Carriers_dilihat_dari_Sembawang_2021.jpg/1280px-LNG_Carriers_dilihat_dari_Sembawang_2021.jpg",
    "PANO06": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg/1280px-Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg",
    "MELKDAY": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/00919_NOR_Hammerfest_Melkoya_LNG_Terminal_day_V-P.jpg/1280px-00919_NOR_Hammerfest_Melkoya_LNG_Terminal_day_V-P.jpg",
    "NEGISHI": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Negishi_LNG_Terminal_01.jpg/1280px-Negishi_LNG_Terminal_01.jpg",
    "JETTY": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Jetty_and_pipelines.jpg/1280px-Jetty_and_pipelines.jpg",
    "GOLDEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Golden_Pass_LNG%2C_Sabine_Pass.jpg/1280px-Golden_Pass_LNG%2C_Sabine_Pass.jpg",
    "SWIN": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/LNG_terminal%2C_Swinoujscie_%2820250326-P1034516%29.jpg/1280px-LNG_terminal%2C_Swinoujscie_%2820250326-P1034516%29.jpg",
    "COVE": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Cove_Point_LNG_Terminal.jpg/1280px-Cove_Point_LNG_Terminal.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# island, the ship, the plant, the floating future.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "MOZAH", "pan": (0.5, 0.5)},
    {"img": "MELKOYA", "pan": (0.5, 0.5)},
    {"img": "FSRU", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 0  title (5.95s) (s0)
    {"img": "SEMBAWANG", **{"type": "cover", "title": "An LNG carrier seen from Sembawang", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 1  October 2026: Indonesia trims the pipeline gas (13.57s) (s1)
    {"img": "MOZAH", **{"type": "cover", "title": "The Q-Max carrier Mozah, Ras Laffan", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 2  the answer: a terminal built thirteen years earlier (12.6s) (s2)
    {"img": "MAP", **{"type": "letterbox", "title": "The terminal site, Jurong Island", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 3  the story of that terminal (10.55s) (s3)
    {"img": "PANO06", **{"type": "cover", "title": "Jurong Island in 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 4  the 2000s: gas at 80 percent, all of it piped (20.38s) (s4)
    {"img": "PLP", **{"type": "cover", "title": "A gas-fired power station", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 5  two suppliers, three pipes; the 2004 blackouts (13.58s) (s5)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 6  the fields will run down; gas still growing (11.28s) (s7)
    {"img": "MELKDAY", **{"type": "cover", "title": "Melkoya plant, Norway, by day", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 7  7 August 2006: the decision announced (19.88s) (s9)
    {"img": "JETTY", **{"type": "cover", "title": "A receiving terminal's jetty, Wales", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 8  the plan: 3 million tonnes a year, by 2012 (17.52s) (s11)
    {"img": "NEGISHI", **{"type": "cover", "title": "Storage tanks at Negishi, Japan", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 9  what LNG is: cooled to minus 162 degrees (16.13s) (s14)
    {"img": "LIJMILIYA", **{"type": "cover", "title": "The Qatargas carrier Lijmiliya", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 10  a ship anywhere; a pipeline ties you; LNG unties you (16.22s) (s16)
    {"img": "MELKDAY", **{"type": "cover", "title": "Melkoya plant, Norway, by day", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 11  three links, partners not rivals (5.1s) (s19)
    {"img": "MELKOYA", **{"type": "cover", "title": "Melkoya at twilight, Norway", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 12  the export end: liquefaction (14.28s) (s20)
    {"img": "MOZAH", **{"type": "cover", "title": "The Q-Max carrier Mozah", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 13  the middle link: the tanker (5.65s) (s21)
    {"img": "SOUTHHOOK", **{"type": "cover", "title": "South Hook terminal, Wales", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 14  the import end: store and regasify (11.25s) (s22)
    {"img": "FSRU", **{"type": "cover", "title": "An FSRU in service, Lithuania", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 15  the floating counterpart (13.67s) (s24)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 16  the commercial version came first: PowerGas (14.2s) (s25)
    {"img": "LIJMILIYA", **{"type": "cover", "title": "The Qatargas carrier Lijmiliya", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 17  BG appointed aggregator, April 2008 (19.22s) (s27)
    {"img": "PLP", **{"type": "cover", "title": "A gas-fired power station", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 18  the financial crisis arrives (5.22s) (s28)
    {"img": "PANO06", **{"type": "cover", "title": "Jurong Island in 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 19  30 June 2009: the government takes over (14.62s) (s29)
    {"img": "JETTY", **{"type": "cover", "title": "A receiving terminal's jetty, Wales", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 20  SLNG incorporated by the EMA (10.68s) (s30)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 21  PM Lee, looking back: the strategic interest (19.72s) (s31)
    {"img": "GOLDEN", **{"type": "cover", "title": "Loading arms at Sabine Pass, Texas", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 22  Samsung C&T; ground broken March 2010 (14.3s) (s33)
    {"img": "NEGISHI", **{"type": "cover", "title": "Storage tanks at Negishi, Japan", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 23  the design grows: a third tank, 6 Mtpa (12.07s) (s34)
    {"img": "COVE", **{"type": "cover", "title": "Cove Point terminal, Maryland", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 24  a secondary berth; S$1.7 billion in all (10.78s) (s35)
    {"img": "SEMBAWANG", **{"type": "cover", "title": "An LNG carrier seen from Sembawang", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 25  two first cargoes, kept separate (4.77s) (s37)
    {"img": "MOZAH", **{"type": "cover", "title": "The Q-Max carrier Mozah, Ras Laffan", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 26  the commissioning cargo: Umm Slal, 27 March 2013 (20.93s) (s38)
    {"img": "LIJMILIYA", **{"type": "cover", "title": "The Qatargas carrier Lijmiliya", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 27  commercial operations: 7 May 2013 (10.57s) (s39)
    {"img": "MELKDAY", **{"type": "cover", "title": "Melkoya plant, Norway, by day", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 28  the terminal that opened: two tanks, one jetty (12.12s) (s40)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 29  by the opening, a third tank: 6 Mtpa (14.8s) (s41)
    {"img": "SOUTHHOOK", **{"type": "cover", "title": "South Hook terminal, Wales", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 30  the insurance idea: options, security, a buffer (16.75s) (s42)
    {"img": "SEMB21", **{"type": "cover", "title": "LNG carriers in Singapore waters, 2021", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 31  looking ahead: demand, the region's hub (11.1s) (s44)
    {"img": "MAP", **{"type": "letterbox", "title": "The terminal site, Jurong Island", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  a fourth tank announced; the site's ceiling (16.9s) (s45)
    {"img": "NEGISHI", **{"type": "cover", "title": "Storage tanks at Negishi, Japan", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 33  Tank 4: 260,000 cubic metres (15.23s) (s47)
    {"img": "MELKOYA", **{"type": "cover", "title": "Melkoya at twilight, Norway", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 34  the terminal today: four tanks, two jetties (17.8s) (s48)
    {"img": "PLP", **{"type": "cover", "title": "A gas-fired power station", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 35  capacity to meet all present demand (13.43s) (s49)
    {"img": "GOLDEN", **{"type": "cover", "title": "Loading arms at Sabine Pass, Texas", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 36  the side business: truck loading (13.15s) (s50)
    {"img": "JETTY", **{"type": "cover", "title": "A receiving terminal's jetty, Wales", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 37  reloads and the FueLNG Bellina (16.82s) (s52)
    {"img": "SEMBAWANG", **{"type": "cover", "title": "An LNG carrier seen from Sembawang", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 38  about 430 cargoes by September 2023 (11.0s) (s53)
    {"img": "CHART", **{"type": "letterbox", "title": "LNG's share of Singapore's gas imports", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}},  # 39  2013: 11 percent; 2025: 57 percent (14.23s) (s55)
    {"img": "PANO06", **{"type": "cover", "title": "Jurong Island in 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 40  insurance is claimed on: 2021 (9.2s) (s57)
    {"img": "SEMB21", **{"type": "cover", "title": "LNG carriers in Singapore waters, 2021", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 41  West Natuna curtailed, September to December 2021 (14.8s) (s58)
    {"img": "LIJMILIYA", **{"type": "cover", "title": "The Qatargas carrier Lijmiliya", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 42  the difference bought as spot LNG (17.75s) (s59)
    {"img": "PLP", **{"type": "cover", "title": "A gas-fired power station", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 43  the lights stayed on; the bill arrived (4.58s) (s60)
    {"img": "SOUTHHOOK", **{"type": "cover", "title": "South Hook terminal, Wales", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 44  world prices fivefold; the tariff peak (20.27s) (s62)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 45  six retailers left the market (13.62s) (s63)
    {"img": "MOZAH", **{"type": "cover", "title": "The Q-Max carrier Mozah", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 46  the lesson: the route insured, not the price (17.0s) (s64)
    {"img": "MELKDAY", **{"type": "cover", "title": "Melkoya plant, Norway, by day", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 47  the Standby LNG Facility (14.88s) (s66)
    {"img": "JETTY", **{"type": "cover", "title": "A receiving terminal's jetty, Wales", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 48  centralised gas buying announced, 2023 (10.5s) (s68)
    {"img": "SEMBAWANG", **{"type": "cover", "title": "An LNG carrier seen from Sembawang", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 49  Singapore GasCo, April 2025 (17.58s) (s69)
    {"img": "PLP", **{"type": "cover", "title": "A gas-fired power station", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 50  the commercial half of the insurance (8.92s) (s70)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 51  the second door is on its way (11.45s) (s71)
    {"img": "FSRU", **{"type": "cover", "title": "An FSRU in service, Lithuania", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 52  a floating terminal at Jurong Port (22.97s) (s73)
    {"img": "COVE", **{"type": "cover", "title": "Cove Point terminal, Maryland", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 53  steel cut, keel laid, onshore works begun (12.4s) (s74)
    {"img": "MELKOYA", **{"type": "cover", "title": "Melkoya at twilight, Norway", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 54  in service by the end of the decade; up to 15 Mtpa (8.55s) (s75)
    {"img": "GOLDEN", **{"type": "cover", "title": "Loading arms at Sabine Pass, Texas", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 55  a third jetty breaks ground, October 2026 (11.38s) (s76)
    {"img": "MAP", **{"type": "letterbox", "title": "The terminal site, Jurong Island", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 56  back to where it began (3.4s) (s77)
    {"img": "SEMB21", **{"type": "cover", "title": "LNG carriers in Singapore waters, 2021", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 57  24 October 2026: the cut, the answer (27.27s) (s78)
    {"img": "SEMBAWANG", **{"type": "cover", "title": "An LNG carrier seen from Sembawang", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 58  no emergency purchase announced (9.28s) (s79)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 59  a mature policy: nothing happens (12.62s) (s80)
    {"img": "PANO06", **{"type": "cover", "title": "Jurong Island in 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.50, 0.50)] * 3, "ease": _E}},  # 60  the bigger story: never any fuel of its own (14.85s) (s82)
    {"img": "PLP", **{"type": "cover", "title": "A gas-fired power station", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.50)] * 3, "ease": _E}},  # 61  the pipelines made three doors (4.68s) (s83)
    {"img": "MOZAH", **{"type": "cover", "title": "The Q-Max carrier Mozah", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.50)] * 3, "ease": _E}},  # 62  the first door onto the whole world (12.35s) (s84)
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.50, 0.40)] * 3, "ease": _E}},  # 63  the door built in case it stopped (8.3s) (s85)
]

SCHEDULE = [
    (0.000, 0), (5.950, 1), (19.525, 2),
    (32.125, 3), (42.675, 4), (63.050, 5),
    (76.625, 6), (87.900, 7), (107.775, 8),
    (125.300, 9), (141.425, 10), (157.650, 11),
    (162.750, 12), (177.025, 13), (182.675, 14),
    (193.925, 15), (207.600, 16), (221.800, 17),
    (241.025, 18), (246.250, 19), (260.875, 20),
    (271.550, 21), (291.275, 22), (305.575, 23),
    (317.650, 24), (328.425, 25), (333.200, 26),
    (354.125, 27), (364.700, 28), (376.825, 29),
    (391.625, 30), (408.375, 31), (419.475, 32),
    (436.375, 33), (451.600, 34), (469.400, 35),
    (482.825, 36), (495.975, 37), (512.800, 38),
    (523.800, 39), (538.025, 40), (547.225, 41),
    (562.025, 42), (579.775, 43), (584.350, 44),
    (604.625, 45), (618.250, 46), (635.250, 47),
    (650.125, 48), (660.625, 49), (678.200, 50),
    (687.125, 51), (698.575, 52), (721.550, 53),
    (733.950, 54), (742.500, 55), (753.875, 56),
    (757.275, 57), (784.550, 58), (793.825, 59),
    (806.450, 60), (821.300, 61), (825.975, 62),
    (838.325, 63)
]
TOTAL_DURATION = 846.625
TIMING_JSON = "audio/the-lng-terminal-the-insurance-policy-singapore-built-in-2013.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
