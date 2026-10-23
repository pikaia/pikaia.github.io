"""Video config for the Singapore Sweep post.

From the 1881 racecourse sketches to the Pools outlets today: the four
pre-1956 newspaper pages (1930, 1933, 1941, 1951), the Bukit Timah
racecourse buildings as Turf City in 2006, the Occupation lottery ticket,
Happy World in the 1940s, the Victoria and National Theatres, the old
National Stadium, Kranji, and the Pools outlets and head office.

Named-person rule: Choo Poh Keng, Peter Chong, Lim Kim San and Tang See
Chim have no free photographs, so their sentences show the 1930 and 1941
newspaper pages (text and adverts only) or buildings with nobody in them.

The newspaper pages, the sketch of the police officer, the 4-D slip, the
Occupation ticket, Happy World, the Middle Road tower and the portrait-
shaped photos are letterboxed.

44 slides, 731.05s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Totoghimmoh.jpg/1280px-Totoghimmoh.jpg",
    "HQ21": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Singapore_Pools_Head_Office_20210503_125649.jpg/1280px-Singapore_Pools_Head_Office_20210503_125649.jpg",
    "HORSE1881": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Singapore%3B_a_stubborn_horse_at_the_start_of_Singapore_raceco_Wellcome_V0037529.jpg/1280px-Singapore%3B_a_stubborn_horse_at_the_start_of_Singapore_raceco_Wellcome_V0037529.jpg",
    "MIDDLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Sede_de_Singapore_Pools%2C_Middle_Road%2C_Singapur%2C_2023-08-16%2C_DD_02.jpg/1280px-Sede_de_Singapore_Pools%2C_Middle_Road%2C_Singapur%2C_2023-08-16%2C_DD_02.jpg",
    "PRINSEP": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Prinsep_Street_Singapore_Pools_01-12-2024.jpg/1280px-Prinsep_Street_Singapore_Pools_01-12-2024.jpg",
    "POLICE1881": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Singapore%3B_a_police_officer_clearing_two_race-goers_from_the_Wellcome_V0037530.jpg/1280px-Singapore%3B_a_police_officer_clearing_two_race-goers_from_the_Wellcome_V0037530.jpg",
    "TURFCITY3": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Turf_City_3%2C_Dec_06.JPG/1280px-Turf_City_3%2C_Dec_06.JPG",
    "TURFCITY2": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Turf_City_2%2C_Dec_06.JPG/1280px-Turf_City_2%2C_Dec_06.JPG",
    "BETTING": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Betting_on_horses.jpg/1280px-Betting_on_horses.jpg",
    "TURFCITY4": "https://upload.wikimedia.org/wikipedia/commons/8/83/Turf_City_4%2C_Dec_06.JPG",
    "TURFSIGN15": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Singapore_Turf_Club%2C_2015.jpg/1280px-Singapore_Turf_Club%2C_2015.jpg",
    "TURFCITY": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Turf_City%2C_Dec_06.JPG/1280px-Turf_City%2C_Dec_06.JPG",
    "ST1930": "/assets/images/straits-times-1930-06-24-page-14.jpg",
    "RACE25A": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Singapore_Racecourse_09-08-2025%281%29.jpg/1280px-Singapore_Racecourse_09-08-2025%281%29.jpg",
    "ST1933": "/assets/images/straits-times-1933-09-24-page-10.jpg",
    "ST1941": "/assets/images/straits-times-1941-08-27-page-10.jpg",
    "JAPTICKET": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_05.jpg/1280px-JapLotteryTicket-SIN-Occupation_SINMuseum_20171213_05.jpg",
    "HAPPY": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Happy_World_Amusement_Park.jpg",
    "ST1951": "/assets/images/straits-times-1951-03-25-page-1.jpg",
    "SLIP": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/4D_Slip.jpg/1280px-4D_Slip.jpg",
    "RACE25B": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Singapore_Racecourse_09-08-2025%282%29.jpg/1280px-Singapore_Racecourse_09-08-2025%282%29.jpg",
    "HQ21B": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Singapore_Pools_Head_Office_20210503_125657.jpg/1280px-Singapore_Pools_Head_Office_20210503_125657.jpg",
    "VICTORIA": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/010253_00001_Singapore%2C_Victoria_Theatre.jpg/1280px-010253_00001_Singapore%2C_Victoria_Theatre.jpg",
    "KALLANGZZ": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Kallang_stadium_zz.JPG",
    "NATTHEATRE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Singapore-National_Theater-1973-74-WUS08168.jpg/1280px-Singapore-National_Theater-1973-74-WUS08168.jpg",
    "STADIUM07": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/National_Stadium%2C_Singapore_2%2C_May_07.JPG/1280px-National_Stadium%2C_Singapore_2%2C_May_07.JPG",
    "TURF15": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Singapore_Turf_Club_building%2C_2015.jpg/1280px-Singapore_Turf_Club_building%2C_2015.jpg",
    "KRANJI24": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Kranji_Racecourse_05-12-2024.jpg/1280px-Kranji_Racecourse_05-12-2024.jpg",
    "LAVENDER": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Lavender_Singapore_Pools_12-05-2024.jpg/1280px-Lavender_Singapore_Pools_12-05-2024.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "PRINSEP": "LN9267, CC BY-SA 4.0, via Wikimedia Commons",
    "TURFCITY2": "Sengkang, copyrighted free use, via Wikimedia Commons",
    "BETTING": "Eggjeezprata, CC BY-SA 4.0, via Wikimedia Commons",
    "TURFCITY4": "Sengkang, copyrighted free use, via Wikimedia Commons",
    "TURFSIGN15": "dave ho, CC BY 2.0, via Wikimedia Commons",
    "RACE25A": "LN9267, CC BY-SA 4.0, via Wikimedia Commons",
    "JAPTICKET": "Zenwort, public domain, via Wikimedia Commons",
    "RACE25B": "LN9267, CC BY-SA 4.0, via Wikimedia Commons",
    "HQ21B": "ZKang123, CC BY-SA 4.0, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1881 to today: the racecourse sketch,
# Happy World in the 1940s, the National Theatre in 1973-74, and a Pools
# outlet in 2024.
THUMBNAIL = [
    {"img": "HORSE1881", "pan": (0.5, 0.5)},
    {"img": "HAPPY", "pan": (0.5, 0.5)},
    {"img": "NATTHEATRE", "pan": (0.5, 0.45)},
    {"img": "LAVENDER", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Newspaper pages, the sketch, the slip, small or portrait-shaped photos:
# letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},               # 0  s0  title
    {"img": "HQ21", **_IN},               # 1  s1  the monthly draw
    {"img": "HORSE1881", **_IN},          # 2  s2  "sweepstakes", from the racecourse
    {"img": "MIDDLE", **_PORT},           # 3  s3  Singapore Pools, 1968
    {"img": "PRINSEP", **_IN},            # 4  s4  Sweep, Toto and 4-D
    {"img": "POLICE1881", **_PORT},       # 5  s5  racing came early; Farrer Park (s5-6)
    {"img": "TURFCITY3", **_IN},          # 6  s7  Turf Club 1924, Bukit Timah 1933
    {"img": "TURFCITY2", **_IN},          # 7  s8  sweeps by the 1930s
    {"img": "BETTING", **_IN},            # 8  s9  how a sweep worked (s9-10)
    {"img": "TURFCITY4", **_PORT},        # 9  s11 tickets matched to horses (s11-12)
    {"img": "TURFSIGN15", **_IN},         # 10 s13 no advantage; luck twice (s13-14)
    {"img": "TURFCITY", **_IN},           # 11 s15 favourites; private lotteries (s15-16)
    {"img": "ST1930", **_PORT},           # 12 s17 Choo Poh Keng's trial (s17-18)
    {"img": "RACE25A", **_IN},            # 13 s19 the acquittal (no people)
    {"img": "ST1933", **_PORT},           # 14 s20 the 1933 Gold Cup (s20-22)
    {"img": "ST1941", **_PORT},           # 15 s23 the War Fund; Peter Chong (s23-25)
    {"img": "JAPTICKET", **_PORT},        # 16 s26 the Syonan Syoken
    {"img": "HAPPY", **_PORT},            # 17 s27 lotteries for causes; the MCA (s27-28)
    {"img": "ST1951", **_PORT},           # 18 s29 the $250,000 cheque; the ban (s29-30)
    {"img": "SLIP", **_PORT},             # 19 s31 chap ji kee (s31-34)
    {"img": "POLICE1881", **_PORT_OUT},   # 20 s35 the courts; the Malta sweep (s35-36)
    {"img": "TURFCITY3", **_OUT},         # 21 s37 the 1966 announcement (s37-39)
    {"img": "RACE25B", **_IN},            # 22 s40 $1 tickets; the first draw (s40-41)
    {"img": "TURFCITY2", **_OUT},         # 23 s42 Lim Kim San (no people)
    {"img": "TURFCITY4", **_PORT_OUT},    # 24 s43 the club's 4-D (s43-45)
    {"img": "HQ21B", **_IN},              # 25 s46 pool betting; the Bulgarians (s46-48)
    {"img": "MIDDLE", **_PORT_OUT},       # 26 s49 incorporated 23 May 1968
    {"img": "HERO", **_OUT},              # 27 s50 agents and post offices (s50-51)
    {"img": "VICTORIA", **_IN},           # 28 s52 the first Toto draw
    {"img": "KALLANGZZ", **_PORT},        # 29 s53 sportsmen and sportswomen (s53-55)
    {"img": "HQ21", **_OUT},              # 30 s56 Pools takes the Sweep; Tang See Chim (s56-57)
    {"img": "NATTHEATRE", **_IN},         # 31 s58 the National Theatre, 1969
    {"img": "HAPPY", **_PORT_OUT},        # 32 s59 Gay World and the other halls
    {"img": "STADIUM07", **_IN},          # 33 s60 the National Stadium
    {"img": "PRINSEP", **_OUT},           # 34 s61 4-D moves to Pools (s61-62)
    {"img": "SLIP", **_PORT_OUT},         # 35 s63 the under-18 spot checks
    {"img": "TURF15", **_IN},             # 36 s64 the Tote Board, 2004 (s64-65)
    {"img": "HQ21B", **_OUT},             # 37 s66 the only operator (s66-67)
    {"img": "BETTING", **_OUT},           # 38 s68 online bets; the GRA (s68-69)
    {"img": "KRANJI24", **_IN},           # 39 s70 the last race at Kranji (s70-71)
    {"img": "LAVENDER", **_IN},           # 40 s72 the Sweep today (s72-74)
    {"img": "HORSE1881", **_OUT},         # 41 s75 where it fits
    {"img": "NATTHEATRE", **_OUT},        # 42 s76 one state-owned company
    {"img": "KRANJI24", **_OUT},          # 43 s77 close
]

SCHEDULE = [
    (0.0, 0), (3.7, 1), (16.4, 2), (28.1, 3), (41.95, 4), (50.075, 5),
    (62.875, 6), (72.3, 7), (77.525, 8), (85.85, 9), (103.2, 10), (114.7, 11),
    (136.075, 12), (163.925, 13), (172.0, 14), (197.4, 15), (228.0, 16), (238.775, 17),
    (253.225, 18), (285.6, 19), (315.875, 20), (336.1, 21), (362.975, 22), (379.875, 23),
    (398.7, 24), (428.275, 25), (453.0, 26), (461.025, 27), (478.425, 28), (490.575, 29),
    (511.025, 30), (528.5, 31), (537.05, 32), (553.25, 33), (568.975, 34), (588.775, 35),
    (599.375, 36), (621.175, 37), (635.95, 38), (651.775, 39), (667.275, 40), (692.65, 41),
    (704.375, 42), (719.975, 43),
]
TOTAL_DURATION = 731.05
TIMING_JSON = "audio/the-singapore-sweep-how-the-lottery-went-legal.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
