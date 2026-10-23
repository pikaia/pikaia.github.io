"""Video config for the Turf Club post.

From the 1881 sketches of the course off Serangoon Road to Kranji after the
last race: the three-racecourse OSM map (twice), the four pre-1956
newspaper pages (1842, 1933, 1947, 1949), the Gold Cup prize-money chart
(twice), Farrer Park and Race Course Road in 2006, the Bukit Timah
buildings as Turf City, and Kranji from 2006 to 2025.

Named-person rule: W. H. M. Read, Roland Farrer, Sir Cecil Clementi,
Indranee Rajah and Lawrence Wong have no free photographs, so their
sentences show the newspaper pages (text and adverts only), the 1910
racecourse view, or buildings and grounds with nobody in them.

The map, the chart, the newspaper pages and the portrait-shaped photo are
letterboxed.

38 slides, 587.725s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Kranji_Racecourse_05-12-2024.jpg/1280px-Kranji_Racecourse_05-12-2024.jpg",
    "SIGN15": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Singapore_Turf_Club%2C_2015.jpg/1280px-Singapore_Turf_Club%2C_2015.jpg",
    "TURF15": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Singapore_Turf_Club_building%2C_2015.jpg/1280px-Singapore_Turf_Club_building%2C_2015.jpg",
    "MAP": "/assets/images/turf-club-racecourses-map.png",
    "SFP1842": "/assets/images/singapore-free-press-1842-12-08-page-3.jpg",
    "SKETCH3": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Singapore%3B_two_race-going_celebrities_talk_as_a_race_horse_i_Wellcome_V0037531.jpg/1280px-Singapore%3B_two_race-going_celebrities_talk_as_a_race_horse_i_Wellcome_V0037531.jpg",
    "KITLV1910": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/KITLV_-_79903_-_Kleingrothe%2C_C.J._-_Medan_-_Tanks_and_the_racecourse_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79903_-_Kleingrothe%2C_C.J._-_Medan_-_Tanks_and_the_racecourse_at_Singapore_-_circa_1910.tif.jpg",
    "SKETCH1": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Singapore%3B_a_stubborn_horse_at_the_start_of_Singapore_raceco_Wellcome_V0037529.jpg/1280px-Singapore%3B_a_stubborn_horse_at_the_start_of_Singapore_raceco_Wellcome_V0037529.jpg",
    "SKETCH2": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Singapore%3B_a_police_officer_clearing_two_race-goers_from_the_Wellcome_V0037530.jpg/1280px-Singapore%3B_a_police_officer_clearing_two_race-goers_from_the_Wellcome_V0037530.jpg",
    "FARRERPOOL": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Farrer_Park_Swimming_Complex%2C_Aug_06.JPG/1280px-Farrer_Park_Swimming_Complex%2C_Aug_06.JPG",
    "RACEROAD": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Race_Course_Road%2C_Aug_06.JPG/1280px-Race_Course_Road%2C_Aug_06.JPG",
    "ST1933": "/assets/images/straits-times-1933-04-17-page-12.jpg",
    "TURFCITY3": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Turf_City_3%2C_Dec_06.JPG/1280px-Turf_City_3%2C_Dec_06.JPG",
    "ST1947": "/assets/images/straits-times-1947-11-16-page-1.jpg",
    "TURFCITY": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Turf_City%2C_Dec_06.JPG/1280px-Turf_City%2C_Dec_06.JPG",
    "TURFCITY7": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Turf_City_7%2C_Dec_06.JPG/1280px-Turf_City_7%2C_Dec_06.JPG",
    "BETTING": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Betting_on_horses.jpg/1280px-Betting_on_horses.jpg",
    "ST1949": "/assets/images/straits-times-1949-08-23-page-12.jpg",
    "CHART": "/assets/images/turf-club-gold-cup-prize.png",
    "TURFCITY4": "https://upload.wikimedia.org/wikipedia/commons/8/83/Turf_City_4%2C_Dec_06.JPG",
    "AVENUE": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Turf_Club_Avenue.JPG/1280px-Turf_Club_Avenue.JPG",
    "RACE25A": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Singapore_Racecourse_09-08-2025%281%29.jpg/1280px-Singapore_Racecourse_09-08-2025%281%29.jpg",
    "FLYOVER": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Turf_Club_Flyover.JPG/1280px-Turf_Club_Flyover.JPG",
    "RACE25B": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Singapore_Racecourse_09-08-2025%282%29.jpg/1280px-Singapore_Racecourse_09-08-2025%282%29.jpg",
    "TURFCITY5": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Turf_City_5%2C_Dec_06.JPG/1280px-Turf_City_5%2C_Dec_06.JPG",
    "MRTSITE": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Turf_City_MRT_station_site_081022.jpg/1280px-Turf_City_MRT_station_site_081022.jpg",
    "TURFCITY6": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Turf_City_6%2C_Dec_06.JPG/1280px-Turf_City_6%2C_Dec_06.JPG",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "BETTING": "Eggjeezprata, CC BY-SA 4.0, via Wikimedia Commons",
    "CHART": "Chart by Lesser Known Singapore, figures from newspaper reports via NewspaperSG",
    "TURFCITY4": "Sengkang, copyrighted free use, via Wikimedia Commons",
    "FLYOVER": "Terence Ong, CC BY 2.5, via Wikimedia Commons",
    "TURFCITY5": "Sengkang, copyrighted free use, via Wikimedia Commons",
    "TURFCITY6": "Sengkang, copyrighted free use, via Wikimedia Commons",
}

# The channel's 2x2 thumbnail grid, 1881 to today: race-goers at the
# Serangoon Road course in 1881, the racecourse around 1910, the Bukit
# Timah buildings as Turf City in 2006, and Kranji after the last race.
THUMBNAIL = [
    {"img": "SKETCH3", "pan": (0.5, 0.5)},
    {"img": "KITLV1910", "pan": (0.5, 0.5)},
    {"img": "TURFCITY3", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map, the chart, the newspaper pages and the portrait photo: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_IN},               # 0  s0  title
    {"img": "SIGN15", **_IN},             # 1  s1  the last meeting, 10,000 people
    {"img": "TURF15", **_IN},             # 2  s2  the 100th Gold Cup; 182 years
    {"img": "MAP", **_PORT},              # 3  s3  three courses (s3-4)
    {"img": "SFP1842", **_PORT},          # 4  s5  Read founds the club; the 1842 notice (s5-6)
    {"img": "SKETCH3", **_IN},            # 5  s7  the first meeting, February 1843
    {"img": "KITLV1910", **_IN},          # 6  s8  Read wins the first Singapore Cup (no people) (s8-9)
    {"img": "SKETCH1", **_IN},            # 7  s10 recreation; the first Gold Cup (s10-11)
    {"img": "SKETCH2", **_IN},            # 8  s12 the town grows; the 1927 sale (s12-13)
    {"img": "FARRERPOOL", **_IN},         # 9  s14 Roland Farrer (no people)
    {"img": "RACEROAD", **_IN},           # 10 s15 Race Course Road
    {"img": "ST1933", **_PORT},           # 11 s16 Clementi opens Bukit Timah (s16-18)
    {"img": "TURFCITY3", **_IN},          # 12 s19 the Malayan racing circuit (s19-20)
    {"img": "ST1947", **_PORT},           # 13 s21 the Occupation; the 1947 record crowd (s21-23)
    {"img": "TURFCITY", **_IN},           # 14 s24 the sweep pool passes $1 million
    {"img": "TURFCITY7", **_IN},          # 15 s25 Sunday racing; open to the public
    {"img": "BETTING", **_IN},            # 16 s26 a $5 ticket wins $54,340; the Sweep post (s26-27)
    {"img": "ST1949", **_PORT},           # 17 s28 Gold Cup prize money, 1924-1949 (s28-30)
    {"img": "CHART", **_PORT},            # 18 s31 1961 to Kranji (s31-32)
    {"img": "SIGN15", **_OUT},            # 19 s33 $1.35 million; back to $1 million
    {"img": "CHART", **_PORT_OUT},        # 20 s34 $1.38 million; inflation (s34-35)
    {"img": "TURFCITY4", **_PORT},        # 21 s36 Bukit Timah wanted for housing; last race (s36-37)
    {"img": "AVENUE", **_IN},             # 22 s38 Kranji opens, 31 July 1999
    {"img": "TURF15", **_OUT},            # 23 s39 the grandstand; the first night race
    {"img": "RACE25A", **_IN},            # 24 s40 the official opening; the International Cup (s40-41)
    {"img": "BETTING", **_OUT},           # 25 s42 crowds fall (s42-43)
    {"img": "FLYOVER", **_IN},            # 26 s44 casinos and other sports
    {"img": "MAP", **_PORT_OUT},          # 27 s45 the June 2023 announcement (s45-46)
    {"img": "RACE25B", **_IN},            # 28 s47 Indranee Rajah (no people); staff and horses (s47-48)
    {"img": "HERO", **_OUT},              # 29 s49 the last meeting; Smart Star (s49-51)
    {"img": "RACEROAD", **_OUT},          # 30 s52 Farrer Park today
    {"img": "TURFCITY5", **_IN},          # 31 s53 Turf City closes
    {"img": "MRTSITE", **_IN},            # 32 s54 the URA plan
    {"img": "TURFCITY6", **_IN},          # 33 s55 the North Grandstand; two MRT stations
    {"img": "RACE25A", **_OUT},           # 34 s56 Lawrence Wong (no people): 14,000 homes
    {"img": "SKETCH3", **_OUT},           # 35 s57 where it fits
    {"img": "KITLV1910", **_OUT},         # 36 s58 each move
    {"img": "TURFCITY", **_OUT},          # 37 s59 close
]

SCHEDULE = [
    (0.0, 0), (5.9, 1), (15.425, 2), (26.125, 3), (46.325, 4), (69.3, 5),
    (80.0, 6), (92.8, 7), (108.975, 8), (124.325, 9), (133.925, 10), (138.45, 11),
    (164.975, 12), (184.1, 13), (204.15, 14), (216.0, 15), (224.425, 16), (251.775, 17),
    (273.95, 18), (295.7, 19), (304.425, 20), (319.2, 21), (335.325, 22), (350.125, 23),
    (365.875, 24), (387.425, 25), (407.075, 26), (418.95, 27), (446.35, 28), (468.325, 29),
    (489.225, 30), (495.65, 31), (506.675, 32), (523.2, 33), (537.2, 34), (552.425, 35),
    (562.425, 36), (573.175, 37),
]
TOTAL_DURATION = 587.725
TIMING_JSON = "audio/the-last-race-at-kranji-182-years-of-the-singapore-turf-club.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
