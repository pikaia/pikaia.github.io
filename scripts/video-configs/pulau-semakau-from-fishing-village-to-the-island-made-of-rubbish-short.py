"""Short config for the Pulau Semakau post — a synopsis re-cut.

Built with: python scripts/build_short_audio.py pulau-semakau-from-fishing-village-to-the-island-made-of-rubbish 1,5,42,43,51,52,54,65,73,74,78,88,96,105,108,121,130,137
(18 sentences, 170.53s — under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. Two fishing villages stood where the rubbish goes; Minah and
   Rani, resettled in 1977, gave away their flat and went home —
   "Our hearts are attached to the island." (s1, s5)
2. Pulau Seking, the older Orang Laut island, was removed for the
   landfill after Kanwaljit Soin's heritage appeal was refused.
   (s42, s43)
3. The mainland ran out of ground: Lorong Halus closed full in
   1999, Semakau opened the next morning behind a seven-kilometre
   bund, and about 2,100 tonnes a day still make the journey.
   (s51, s52, s54, s65)
4. The living island survived: replanted mangroves stand as the
   landfill's leak alarm, giant clams live on the reef, and a reef
   had to be rescued from the island's own lagoon. (s73, s74, s78, s88)
5. The clock and the turn: full by about 2035, so the ash itself
   becomes a resource — already under Singaporeans' feet in a real
   road — and TREASURES turns the landfill into a research subject.
   (s96, s105, s108, s121)
6. The people endure: Hari Orang Pulau reunites the island
   families, and the story closes on Minah's sentence. (s130, s137)

Every slide is letterboxed. Named-person rule as in the main
config: no portraits exist in the pool, so named sentences show
the island and its works.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/4/40/Pulau_Semakau%2C_panorama%2C_Nov_06.jpg",
    "STATION": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Semakaustation.jpg",
    "PS10": "https://upload.wikimedia.org/wikipedia/commons/8/82/Pulau_Semakau_10%2C_Nov_06.JPG",
    "CLAM": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Tridacna_squamosa_%28Giant_clam%29_brown_and_blue.jpg",
    "PANO3": "https://upload.wikimedia.org/wikipedia/commons/c/c6/Pulau_Semakau%2C_panorama_3%2C_Nov_06.jpg",
    "PS32": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Pulau_Semakau_32%2C_Nov_06.JPG",
    "STAR": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Knobbly_sea_star_%28Protoreaster_nodosus%29.jpg",
    "SEAGRASS": "https://upload.wikimedia.org/wikipedia/commons/b/be/Enhalus_acoroides_%2830774220094%29.jpg",
    "HERON": "https://upload.wikimedia.org/wikipedia/commons/4/44/Great-billed_heron_%28Ardea_sumatrana_sumatrana%29_Danum_Valley.jpg"
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PANO3", "pan": (0.5, 0.5)},
    {"img": "STATION", "pan": (0.5, 0.5)},
    {"img": "CLAM", "pan": (0.5, 0.5)},
    {"img": "PANO", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "PANO3", **_LB},   # s1 Minah and Rani resettled to Telok Blangah (13.2s)
    {"img": "PANO", **_LB},   # s5 'Our hearts are attached to the island' (3.5s)
    {"img": "PS10", **_LB},   # s42 Kanwaljit Soin's heritage appeal for Seking (7.8s)
    {"img": "PANO", **_LB},   # s43 the appeal refused: another S$130 million (10.4s)
    {"img": "PS32", **_LB},   # s51 Lorong Halus closed, completely full, 31 March 1999 (7.2s)
    {"img": "STATION", **_LB},   # s52 Semakau Landfill opened the next morning (3.6s)
    {"img": "PS32", **_LB},   # s54 the seven-kilometre bund; 350 hectares enclosed (15.4s)
    {"img": "STATION", **_LB},   # s65 2,100 tonnes a day make the journey (17.5s)
    {"img": "PANO3", **_LB},   # s73 the replanted mangroves thrive — combined with s74 (12.1s)
    {"img": "CLAM", **_LB},   # s78 giant clams live on the reef (11.7s)
    {"img": "STAR", **_LB},   # s88 they had to rescue a reef from the island's own lagoon (6.0s)
    {"img": "PS10", **_LB},   # s96 full by about 2035 at current rates (7.4s)
    {"img": "PS32", **_LB},   # s105 some of it is already under Singaporeans' feet (4.0s)
    {"img": "PS10", **_LB},   # s108 the ash road opened in April 2022 and performed (9.1s)
    {"img": "PANO", **_LB},   # s121 TREASURES: the centre devoted to the landfill's transformation (24.8s)
    {"img": "PS32", **_LB},   # s130 the first Hari Orang Pulau reunites the island families (13.8s)
    {"img": "PANO", **_LB},   # s137 closing bookend: 'Our hearts are attached to the island' (2.9s)
]
SCHEDULE = [
    (0.000, 0), (13.225, 1), (16.675, 2), (24.475, 3), (34.925, 4), (42.175, 5),
    (45.775, 6), (61.150, 7), (78.625, 8), (90.750, 9), (102.475, 10), (108.525, 11),
    (115.925, 12), (119.975, 13), (129.075, 14), (153.875, 15), (167.625, 16)
]
TOTAL_DURATION = 170.53
TIMING_JSON = "audio/pulau-semakau-from-fishing-village-to-the-island-made-of-rubbish-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
