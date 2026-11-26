"""Short config for the Pulau Ubin post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py pulau-ubin-the-island-singapore-decided-to-keep 0,1,11,14,27,31,35,52,59,65,71,76,81,88
(14 sentences, 178.025s - under the 3-minute Shorts
ceiling with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The hook: ten minutes by bumboat, another country. (s1)
2. The stone: Ubin granite built the lighthouses, the
   Istana and the Causeway. (s11)
3. The quarries at scale: Ketam alone supplied 30 to
   40 percent of Singapore's granite in the 1990s. (s14)
4. The emptying: 2,028 people in 1970, 38 by 2012. (s27)
5. The legend: the German girl of 1914. (s31)
6. The unravelling: on the evidence, not true. (s35)
7. The school: Outward Bound founded on Ubin in 1967. (s52)
8. The personal thread: thunderflashes in the bunk. (s59)
9. The saved shore: Chek Jawa, 2001. (s65)
10. The self-powered island: the micro-grid, 2013. (s71)
11. The honest coda: 2025 still ran mostly on diesel. (s76)
12. The promise: rustic for as long as possible. (s81)
13. The close: its own beginning. (s88)

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24).
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "SOLARHOUSE": "https://upload.wikimedia.org/wikipedia/commons/6/60/Kampong_house%2C_Pulau_Ubin%2C_Singapore_-_20090801.jpg",
    "MAP1945": "https://upload.wikimedia.org/wikipedia/commons/d/dc/P_Ubin_1945_map.jpg",
    "QUARRY": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Ubin_Quarry_01.jpg",
    "ELDER": "https://upload.wikimedia.org/wikipedia/commons/0/09/Elderly_Chinese_man%2C_Pulau_Ubin%2C_Singapore_-_20070225.jpg",
    "SHRINE": "https://upload.wikimedia.org/wikipedia/commons/e/e5/German_Girl_Shrine_%28526020601%29.jpg",
    "BIKESHOP": "https://upload.wikimedia.org/wikipedia/commons/4/43/Bicycle_rental_shop%2C_Pulau_Ubin%2C_Singapore_-_20071102-01.jpg",
    "CJPANO": "https://upload.wikimedia.org/wikipedia/commons/e/e8/Chek_Jawa%2C_panorama_6%2C_Aug_07.jpg",
    "BUMBOATS": "https://upload.wikimedia.org/wikipedia/commons/4/4d/SINGAPOREAN_BUMBOATS.jpg",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/2/22/Singapore_Pulau_Ubin_02.jpg",
    "KHOUSE": "https://upload.wikimedia.org/wikipedia/commons/4/45/Pulau_Ubin_kampong_house.jpg",
    "NHOUSE": "https://upload.wikimedia.org/wikipedia/commons/b/bb/House_near_the_northern_coast_of_Pulau_Ubin%2C_Singapore_-_20050803.jpg",
    "CYCLEHIRE": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Pulau_Ubin_cycle_hire.jpg",
    "TAXI": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Toyota_Crown_%28S110%29%2C_Pulau_Ubin%2C_Singapore_-_20071102.jpg",
    "SHRINEIN": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Inside_German_Girl_Shrine_%28525927644%29.jpg",
    "BARBIE": "https://upload.wikimedia.org/wikipedia/commons/0/01/German_girl_shrine_a.k.a._Barbie_doll_shrine_-singapore_%2816664410223%29.jpg",
    "CJ2": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Chek_Jawa_2%2C_Aug_07.JPG",
    "HOUSE1": "https://upload.wikimedia.org/wikipedia/commons/0/01/Chek_Jawa_Visitor_Centre%2C_Pulau_Ubin_%E2%80%93_Singapore_%283817430741%29.jpg",
    "NIGHTJETTY": "https://upload.wikimedia.org/wikipedia/commons/0/00/Leaving_Pulau_Ubin_jetty_on_a_bumboat_%2814043336260%29.jpg",
    "CROSS2025": "https://upload.wikimedia.org/wikipedia/commons/6/6a/SC3619D_Changi_Point_to_Pulau_Ubin_10-08-2025%281%29.jpg",
    "BOAR": "https://upload.wikimedia.org/wikipedia/commons/6/64/Pulau_Ubin_tame_wild_boar.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "MAP1945", "pan": (0.5, 0.5)},
    {"img": "QUARRY", "pan": (0.5, 0.5)},
    {"img": "SHRINE", "pan": (0.5, 0.5)},
    {"img": "SOLARHOUSE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "SOLARHOUSE", **_LB, "title": "Kampong house with its own solar, 2009"},   # s0 title (4.25s),
    {"img": "BUMBOATS", **_LB, "title": "Bumboats to Pulau Ubin"},   # s1 ten minutes by bumboat, another country (5.58s),
    {"img": "MAP1945", **_LB, "title": "Pulau Ubin in 1945"},   # s11 Ubin granite built Horsburgh, the Istana, the Causeway (18.52s),
    {"img": "QUARRY", **_LB, "title": "A flooded granite quarry"},   # s14 Ketam: a hundred men, 30 to 40 percent of Singapore's granite (15.28s),
    {"img": "ELDER", **_LB, "title": "An Ubin islander, 2007"},   # s27 2,028 people in 1970; 38 residents by 2012 (16.23s),
    {"img": "SHRINEIN", **_LB, "title": "Inside the German Girl Shrine, 2007"},   # s31 the legend: the girl who fled the soldiers in 1914 (11.35s),
    {"img": "BARBIE", **_LB, "title": "The shrine rebuilt, 2015"},   # s35 on the evidence, not true - and the unravelling is better (5.90s),
    {"img": "PANO", **_LB, "title": "Pulau Ubin from the water"},   # s52 Outward Bound founded on Ubin, 1967 (10.90s),
    {"img": "NIGHTJETTY", **_LB, "title": "The Ubin jetty at night, 2014"},   # s59 a boy in the bunk, woken by thunderflashes (13.90s),
    {"img": "CJPANO", **_LB, "title": "Chek Jawa boardwalk, 2007"},   # s65 Chek Jawa, saved days before reclamation began (13.40s),
    {"img": "SOLARHOUSE", **_LB, "title": "A house that makes its own power"},   # s71 never on the grid: the micro-grid, 2013 (14.22s),
    {"img": "NHOUSE", **_LB, "title": "A house on Ubin's north coast, 2005"},   # s76 the coda: 2025 still ran 90 percent on diesel (21.77s),
    {"img": "KHOUSE", **_LB, "title": "A kampong house on Ubin"},   # s81 the promise: rustic for as long as possible (12.72s),
    {"img": "SOLARHOUSE", **_LB, "title": "Kampong house with its own solar, 2009"},   # s88 one place where Singapore can see its own beginning (14.00s),
]
SCHEDULE = [
    (0.000, 0), (4.250, 1), (9.825, 2),
    (28.350, 3), (43.625, 4), (59.850, 5),
    (71.200, 6), (77.100, 7), (88.000, 8),
    (101.900, 9), (115.300, 10), (129.525, 11),
    (151.300, 12), (164.025, 13),
]
TOTAL_DURATION = 178.025
TIMING_JSON = "audio/pulau-ubin-the-island-singapore-decided-to-keep-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
