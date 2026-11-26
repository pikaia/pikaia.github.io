"""Short config for the LNG terminal post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py the-lng-terminal-the-insurance-policy-singapore-built-in-2013 0,1,5,10,18,29,36,38,43,49,56,59,64,70,72,75,86
(17 sentences, 172.15s - under the 3-minute Shorts
ceiling with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The hook: October 2026, Indonesia trims the gas. (s1)
2. The dependence: two suppliers, three pipes. (s5)
3. The decision: diversify, August 2006. (s10)
4. The untying: the supplier becomes whoever has a cargo. (s18)
5. The takeover: the state builds it, 2009. (s29)
6. The cost: S$1.7 billion in all. (s36)
7. The first cargo: the commissioning cargo, March 2013. (s38)
8. The buffer: options and a strategic buffer, 2014. (s43)
9. The capacity: enough for all present demand. (s49)
10. The shift: LNG passes half of gas imports. (s56)
11. The claim: West Natuna curtailed, 2021. (s59)
12. The lesson: the route insured, not the price. (s64)
13. The buyer: GasCo, the standing buyer. (s70)
14. The second door: a floating terminal. (s72)
15. The scale: up to 15 Mtpa together. (s75)
16. The close: the door built in case it stopped. (s86)

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24).
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Jurong_Island%2C_Singapore_-_20110227-02.jpg/1280px-Jurong_Island%2C_Singapore_-_20110227-02.jpg",
    "SEMBAWANG": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Kapal_Pengangkut_LNG_dilihat_dari_Sembawang.jpg/1280px-Kapal_Pengangkut_LNG_dilihat_dari_Sembawang.jpg",
    "PLP": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/PLPplant.jpg/1280px-PLPplant.jpg",
    "MELKDAY": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/00919_NOR_Hammerfest_Melkoya_LNG_Terminal_day_V-P.jpg/1280px-00919_NOR_Hammerfest_Melkoya_LNG_Terminal_day_V-P.jpg",
    "LIJMILIYA": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Lijmiliya_LNG_carrier_QatarGas.jpg/1280px-Lijmiliya_LNG_carrier_QatarGas.jpg",
    "PANO06": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg/1280px-Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg",
    "COVE": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Cove_Point_LNG_Terminal.jpg/1280px-Cove_Point_LNG_Terminal.jpg",
    "MOZAH": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Mozah%2C_Nakilat%27s_flagship_vessel.JPG/1280px-Mozah%2C_Nakilat%27s_flagship_vessel.JPG",
    "SOUTHHOOK": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/South_Hook_LNG_terminal_above_Little_Wick_-_geograph.org.uk_-_8315622.jpg/1280px-South_Hook_LNG_terminal_above_Little_Wick_-_geograph.org.uk_-_8315622.jpg",
    "CHART": "/assets/images/lng-import-split-chart.png",
    "SEMB21": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/LNG_Carriers_dilihat_dari_Sembawang_2021.jpg/1280px-LNG_Carriers_dilihat_dari_Sembawang_2021.jpg",
    "MELKOYA": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/07647_NOR_Hammerfest_Melkoya_LNG_Terminal_V-P.jpg/1280px-07647_NOR_Hammerfest_Melkoya_LNG_Terminal_V-P.jpg",
    "GOLDEN": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Golden_Pass_LNG%2C_Sabine_Pass.jpg/1280px-Golden_Pass_LNG%2C_Sabine_Pass.jpg",
    "FSRU": "https://upload.wikimedia.org/wikipedia/commons/0/05/FSRU_Independence_in_the_port_of_Klaip%C4%97da%2C_Lithuania.jpg",
    "NEGISHI": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Negishi_LNG_Terminal_01.jpg/1280px-Negishi_LNG_Terminal_01.jpg",
}

CREDITS = {}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB, "title": "Jurong Island from the sea, 2011"},  # 0  title (5.95s) (s0)
    {"img": "SEMBAWANG", **_LB, "title": "An LNG carrier seen from Sembawang"},  # 1  the hook: October 2026 (13.57s) (s1)
    {"img": "PLP", **_LB, "title": "A gas-fired power station"},  # 2  the dependence: two suppliers, three pipes (7.35s) (s5)
    {"img": "MELKDAY", **_LB, "title": "Melkoya plant, Norway, by day"},  # 3  the decision: diversify, 2006 (9.77s) (s10)
    {"img": "LIJMILIYA", **_LB, "title": "The Qatargas carrier Lijmiliya"},  # 4  LNG unties you (5.65s) (s18)
    {"img": "PANO06", **_LB, "title": "Jurong Island in 2006"},  # 5  the takeover: the state builds it, 2009 (14.62s) (s29)
    {"img": "COVE", **_LB, "title": "Cove Point terminal, Maryland"},  # 6  the cost: S$1.7 billion (5.62s) (s36)
    {"img": "MOZAH", **_LB, "title": "The Q-Max carrier Mozah, Ras Laffan"},  # 7  the first cargo: commissioning, March 2013 (20.92s) (s38)
    {"img": "SOUTHHOOK", **_LB, "title": "South Hook terminal, Wales"},  # 8  the buffer: PM Lee's opening words (11.38s) (s43)
    {"img": "HERO", **_LB, "title": "Jurong Island from the sea, 2011"},  # 9  capacity for all present demand (13.43s) (s49)
    {"img": "CHART", **_LB, "title": "LNG's share of gas imports"},  # 10  2025: LNG passes half of imports (7.5s) (s56)
    {"img": "SEMB21", **_LB, "title": "Carriers in Singapore waters, 2021"},  # 11  the claim: West Natuna, 2021 (17.75s) (s59)
    {"img": "MELKOYA", **_LB, "title": "Melkoya at twilight, Norway"},  # 12  the lesson: the route, not the price (8.07s) (s64)
    {"img": "GOLDEN", **_LB, "title": "Loading arms at Sabine Pass"},  # 13  the buyer: GasCo, the standing buyer (8.93s) (s70)
    {"img": "FSRU", **_LB, "title": "An FSRU in service, Lithuania"},  # 14  the second door: a floating terminal (8.53s) (s72)
    {"img": "NEGISHI", **_LB, "title": "Storage tanks at Negishi, Japan"},  # 15  up to 15 Mtpa together (8.55s) (s75)
    {"img": "HERO", **_LB, "title": "Jurong Island from the sea, 2011"},  # 16  the close: the door built in case it stopped (4.55s) (s86)
]

SCHEDULE = [
    (0.000, 0), (5.950, 1), (19.525, 2),
    (26.875, 3), (36.650, 4), (42.300, 5),
    (56.925, 6), (62.550, 7), (83.475, 8),
    (94.850, 9), (108.275, 10), (115.775, 11),
    (133.525, 12), (141.600, 13), (150.525, 14),
    (159.050, 15), (167.600, 16)
]
TOTAL_DURATION = 172.15
TIMING_JSON = "audio/the-lng-terminal-the-insurance-policy-singapore-built-in-2013-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
