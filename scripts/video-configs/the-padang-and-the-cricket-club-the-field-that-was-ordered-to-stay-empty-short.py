"""Short config for the Padang and the Singapore Cricket Club post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py the-padang-and-the-cricket-club-the-field-that-was-ordered-to-stay-empty 0,3,9,20,28,42,51,52,60,65,76,79
(12 sentences, 167.18s - under the 3-minute
Shorts ceiling with margin, and well over TikTok's
1-minute floor.)

The post's points, and the sentences that carry each:
1. The kept field: a monument made of emptiness. (s3)
2. Raffles's order: the building stopped, 1822. (s9)
3. The Cricket Club founded, 1852. (s20)
4. The colour line: Europeans only. (s28)
5. Occupation: the assembly ground, 1942. (s42)
6. The surrender signed inside, not on the steps. (s51, s52)
7. 1959: "times have changed". (s60)
8. The first National Day Parade, 1966. (s65)
9. Gazetted the 75th National Monument, 2022. (s76)
10. The closing line: nothing there. (s79)

Compression casualties, noted honestly: the "Open
Square" label itself, the pavilion lineage, the SRC's
founding in detail (the colour line is carried, the
answer club is not), the statue, the INA review and the
tapioca year, the 1959 swearing-in (the taunt carries
1959), the rain of 1968, the F1 race, the National
Gallery, and cricket still played today - the spine -
kept field, the order, the club, the colour line,
occupation, the corrected surrender, 1959, the first
parade, the monument - is intact.

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24). All four THUMBNAIL
keys (CITYHALL, PHOTOCHROME, INSPECT, CRICKETMBS) are in
IMAGES; CRICKETMBS is carried for the step-8.3 thumbnail
grid and is not used by a Short slide.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "CITYHALL": "https://upload.wikimedia.org/wikipedia/commons/7/70/Old_Supreme_Court_Building_and_City_Hall_from_the_Padang%2C_Singapore_-_20110205.jpg",
    "PADANG2025": "https://upload.wikimedia.org/wikipedia/commons/3/3d/The_Padang%2C_October_2025.jpg",
    "ESPLANADE": "https://upload.wikimedia.org/wikipedia/commons/2/25/Park_met_wandelaars_in_Singapore_Esplanade%2C_S.pore_%28titel_op_object%29%2C_RP-F-F01197-AG.jpg",
    "PHOTOCHROME": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Singapore._Esplanade_Cricket_Club_LCCN2017657648.jpg",
    "SCC2016": "https://upload.wikimedia.org/wikipedia/commons/9/91/Singapore_Cricket_Club_building_2016.jpg",
    "PADANG7374": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Singapore-Padang-1973-74-WUS01252.jpg",
    "ADDRESS": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Mountbatten_address%2C_Singapore_1945.jpg",
    "INSPECT": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Louis_Mountbatten_Inspection%2C_Singapore_1945.jpg",
    "MUNICIPAL": "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b6/The_Municipal_Building_te_Singapore%2C_KITLV_104790.tiff/lossy-page1-1280px-The_Municipal_Building_te_Singapore%2C_KITLV_104790.tiff.jpg",
    "NDP1968": "https://upload.wikimedia.org/wikipedia/commons/e/eb/NationalDayParade-Singapore-1968.jpg",
    "CRICKETMBS": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Cricket_match_and_Marina_Bay_Sands_Hotel_in_Singapore.jpg",
}

CREDITS = {}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "CITYHALL", **_LB, "title": "The Padang and the Cricket Club"},  # 0  title (5.28s) (s0)
    {"img": "PADANG2025", **_LB, "title": "A monument made of emptiness"},  # 1  the gazetted emptiness, 2022 (5.58s) (s3)
    {"img": "ESPLANADE", **_LB, "title": "Raffles stops the building, 1822"},  # 2  the 1822 rebuke: the land was ordered kept public (8.95s) (s9)
    {"img": "PHOTOCHROME", **_LB, "title": "The Cricket Club, 1852"},  # 3  the founding; the first fixture in March 1853 (17.20s) (s20)
    {"img": "SCC2016", **_LB, "title": "Europeans only"},  # 4  the colour line at the southern end (16.00s) (s28)
    {"img": "PADANG7374", **_LB, "title": "The assembly ground, 1942"},  # 5  17 February 1942: held and interrogated on the field (22.43s) (s42)
    {"img": "ADDRESS", **_LB, "title": "Not signed on the steps"},  # 6  the surrender's popular shorthand, corrected (6.40s) (s51)
    {"img": "INSPECT", **_LB, "title": "Signed inside the chamber"},  # 7  11.10 am, 12 September 1945 (18.10s) (s52)
    {"img": "MUNICIPAL", **_LB, "title": "“Times have changed”, 1959"},  # 8  Lee's taunt at the victory rally (15.25s) (s60)
    {"img": "NDP1968", **_LB, "title": "The first National Day Parade"},  # 9  9 August 1966 (photo: the 1968 parade) (19.70s) (s65)
    {"img": "PADANG2025", **_LB, "title": "A national monument, 2022"},  # 10  the 75th National Monument, the first green one (11.35s) (s76)
    {"img": "CITYHALL", **_LB, "title": "Nothing there"},  # 11  the closing line (20.95s) (s79)
]

SCHEDULE = [
    (0.000, 0), (5.275, 1), (10.850, 2),
    (19.800, 3), (37.000, 4), (53.000, 5),
    (75.425, 6), (81.825, 7), (99.925, 8),
    (115.175, 9), (134.875, 10), (146.225, 11)
]
TOTAL_DURATION = 167.175
TIMING_JSON = "audio/the-padang-and-the-cricket-club-the-field-that-was-ordered-to-stay-empty-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
