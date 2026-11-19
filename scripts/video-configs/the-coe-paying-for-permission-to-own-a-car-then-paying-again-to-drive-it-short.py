"""Short config for the COE post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py the-coe-paying-for-permission-to-own-a-car-then-paying-again-to-drive-it 1,3,4,8,20,28,35,43,49,57,71,86
(12 sentences, 176.075s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The gantries are coming down: the last working ones charge
   until 31 December 2026, and satellite charging starts on
   1 January 2027. (s1, s3)
2. The system itself: pay for permission to own a car, then
   pay again, per trip, to drive it. (s4)
3. The paper licence of 1975: the world's first congestion
   pricing, checked by eye. (s8)
4. The COE from 1990: no car registered without first winning
   the right to. (s20)
5. The long tightening: the growth allowance cut in stages
   to zero. (s28)
6. The rollercoaster: October 2023's all-time records, the
   certificate costing more than most cars. (s35)
7. ERP's effect: expressway volumes fell, and speeds rose
   from 35 to 55 kilometres an hour. (s43)
8. The pair of levers, in the LTA's own words: the quota
   regulates ownership, ERP manages usage. (s49)
9. The result: the most expensive place in the world to buy
   a car, by a wide margin. (s57)
10. The widower's daughter: her sums on the daily drive made
    renting near work cheaper than the family home. (s71)
11. ERP 2: satellite charging from 1 January 2027, at the
    same locations, under the same framework. (s86)

Every slide is letterboxed and carries its photo title, as in
the main config. The pool holds no portraits, so the
named-person rule is met by construction.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/1/14/ERP_gantry_on_the_BKE.jpg",
    "ALSSIGN": "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/89/Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ALS%29.svg/960px-Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ALS%29.svg.png",
    "NIGHT": "https://upload.wikimedia.org/wikipedia/commons/6/65/Singapore%27s_ERP_gantry_at_night.jpg",
    "IU": "https://upload.wikimedia.org/wikipedia/commons/2/2d/ERP_IU_unit_back_side.JPG",
    "ERPNEW": "https://upload.wikimedia.org/wikipedia/commons/0/03/ERP_new.jpg",
    "OBU": "https://upload.wikimedia.org/wikipedia/commons/e/e4/ERP2.0_On_Board_Unit_display.jpg",
    "DUNEARN": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Dunearn_Rd_-_Wayang_Satu_flyover_20060402.JPG",
    "G_MULTI": "https://upload.wikimedia.org/wikipedia/commons/5/5c/ERP_in_Singapore.jpg",
    "G_TOLL": "https://upload.wikimedia.org/wikipedia/commons/3/35/ERP_toll_station.jpg",
    "G_SIGN": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Singapore%27s_ERP_gantry.jpg",
    "G_BUGIS": "https://upload.wikimedia.org/wikipedia/commons/7/7a/ERPBugis.JPG",
    "G_EARLY": "https://upload.wikimedia.org/wikipedia/commons/c/c7/027_ERP_gantry.jpg",
    "G_PORTRAIT": "https://upload.wikimedia.org/wikipedia/commons/9/90/Electronic_Road_Pricing_gantry_in_Singapore.jpg",
    "G_OBUSET": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Car_On_Board_Unit_Singapore.jpg",
    "G_OBUPROC": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Car_On_Board_Processing_Unit_Singapore.jpg",
    "G_ERPSIGN": "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/61/Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ERP%29.svg/960px-Singapore_Road_Signs_-_Warning_Sign_-_Restricted_Zone_%28ERP%29.svg.png",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "ALSSIGN", "pan": (0.5, 0.5)},
    {"img": "IU", "pan": (0.5, 0.5)},
    {"img": "OBU", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "G_TOLL", **_LB, "title": "An ERP toll station gantry"},   # s1 the gantries are coming down (2.83s)
    {"img": "G_MULTI", **_LB, "title": "An ERP gantry over a multi-lane road"},   # s3 the last working gantries; satellite from 1 Jan 2027 (17.73s)
    {"img": "ERPNEW", **_LB, "title": "A gantry of the current generation"},   # s4 pay to own, pay again to drive (13.78s)
    {"img": "ALSSIGN", **_LB, "title": "The Restricted Zone sign of the ALS era"},   # s8 1975: the paper licence, the world's first (22.1s)
    {"img": "G_TOLL", **_LB, "title": "An ERP toll station gantry"},   # s20 1990: no car registered without winning the right (15.05s)
    {"img": "G_MULTI", **_LB, "title": "An ERP gantry over a multi-lane road"},   # s28 the growth allowance cut to zero (19.77s)
    {"img": "HERO", **_LB, "title": "An ERP gantry over the Bukit Timah Expressway"},   # s35 October 2023: the all-time records (17.68s)
    {"img": "NIGHT", **_LB, "title": "An ERP gantry after dark"},   # s43 ERP's effect: speeds rose from 35 to 55 (14.32s)
    {"img": "ERPNEW", **_LB, "title": "A gantry of the current generation"},   # s49 a pair of levers, in the LTA's words (12.07s)
    {"img": "G_SIGN", **_LB, "title": "An ERP gantry in the city"},   # s57 the dearest place in the world to buy a car (6.2s)
    {"img": "G_BUGIS", **_LB, "title": "The ERP gantry at Bugis"},   # s71 the daughter's sums on the daily drive (15.12s)
    {"img": "OBU", **_LB, "title": "The ERP 2.0 on-board unit display"},   # s86 1 Jan 2027: charging by satellite, same framework (19.43s)
]
SCHEDULE = [
    (0.000, 0), (2.825, 1), (20.550, 2), (34.325, 3), (56.425, 4), (71.475, 5),
    (91.250, 6), (108.925, 7), (123.250, 8), (135.325, 9), (141.525, 10), (156.650, 11)
]
TOTAL_DURATION = 176.075
TIMING_JSON = "audio/the-coe-paying-for-permission-to-own-a-car-then-paying-again-to-drive-it-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
