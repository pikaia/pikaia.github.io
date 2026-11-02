"""Short config for the Bank of China Building post - synopsis-first.

A synopsis of the whole story, not a truncation (Chris's rule,
2026-11-01; this post is its first live application). The post
makes eight points, and the Short carries all eight, compressed:

  P1  In 1937 the bank paid $715,000 for a palace it never occupied (s1, s4).
  P2  The palace had been built for the Chartered Bank (s5).
  P3  It spent its last decades as a department store, trading even
      through the Occupation (s16, s31).
  P4  The tenants fought eviction, squatted, and lost; the palace
      was demolished in 1947 (s33, s39).
  P5  The tower that replaced it was approved from Peking in 1950,
      opened in December 1953, and keeps Nolli's lions (s43, s48, s53).
  P6  It was never Singapore's tallest building - only the tallest
      on the river waterfront (s57, s59).
  P7  Kuala Lumpur announced its closure in 1964; it was never
      carried out (s62, s64).
  P8  Today the address holds two buildings, the old one unlisted
      and largely unremarked (s67, s71).

The soundtrack is a re-cut of the full narration (sentences
0, 1, 4, 5, 16, 31, 33, 39, 43, 48, 53, 57, 59, 62, 64, 67, 71),
built by scripts/build_short_audio.py into
audio/the-bank-of-china-building-on-battery-road-short.mp3 with its
own re-based timing file, which TIMING_JSON below points at; the
engine reads the audio and the burned captions from it. 170.5s: over
TikTok's one-minute floor with room, under the three-minute Shorts
cap. Named-person rule as in the main config: no portraits exist,
so named men get the building or the street. Every slide is
letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "PHOTO": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Singapore._Chartered_Bank_Buildings._Battery_Road_LCCN2017657651.jpg/1280px-Singapore._Chartered_Bank_Buildings._Battery_Road_LCCN2017657651.jpg",
    "PAL": "https://upload.wikimedia.org/wikipedia/commons/7/79/Chartered_Bank_Building_Singapore.jpg",
    "KITLV": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif.jpg",
    "ROAD": "https://upload.wikimedia.org/wikipedia/commons/4/42/Battery_Road%2C_c._1905.jpg",
    "RIVER": "https://upload.wikimedia.org/wikipedia/commons/5/57/SingaporeRiver-196009.jpg",
    "TODAY1": "https://upload.wikimedia.org/wikipedia/commons/2/22/Original_Bank_of_China_Building%2C_Singapore_20250903.jpg",
    "TODAY2": "https://upload.wikimedia.org/wikipedia/commons/3/34/Bank_of_China_Building%2C_Singapore_20250903.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PHOTO", "pan": (0.5, 0.5)},
    {"img": "PAL", "pan": (0.5, 0.5)},
    {"img": "RIVER", "pan": (0.35, 0.45)},
    {"img": "TODAY2", "pan": (0.5, 0.35)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The lions slide: letterbox, zoomed and panned toward the entrance
# at the bottom of the tall 2025 photograph.
_LBL = {"type": "letterbox", "zoom": [1.12, 1.17, 1.22], "pan": [(0.5, 0.72)] * 3, "ease": _E}

SLIDES = [
    {"img": "PHOTO", **_LB},   # s0 title (3.7s)
    {"img": "PAL", **_LB},   # s1 P1: the $715,000 purchase, May 1937 (16.0s)
    {"img": "PHOTO", **_LB},   # s4 P1: the palace it bought, and never used (5.2s)
    {"img": "PAL", **_LB},   # s5 P2: built for another bank entirely (4.0s)
    {"img": "PHOTO", **_LB},   # s16 P3: the bullion palace had become a shop (4.0s)
    {"img": "KITLV", **_LB},   # s31 P3: the war - branch closed; the stores traded on; the Mutsumi restaurant (23.4s)
    {"img": "ROAD", **_LB},   # s33 P4: Singapore's 'squat' drama (5.6s)
    {"img": "PHOTO", **_LB},   # s39 P4: demolition under way, May 1947 (the palace's bookend) (10.8s)
    {"img": "TODAY1", **_LB},   # s43 P5: Peking approves the superstructure, May 1950 (9.7s)
    {"img": "RIVER", **_LB},   # s48 P5: finished December 1953; the bank moves in (11.2s)
    {"img": "TODAY1", **_LBL},   # s53 P5: Nolli's lions at the entrance (panned low) (13.9s)
    {"img": "TODAY2", **_LB},   # s57 P6: but never the tallest building in Singapore (3.7s)
    {"img": "RIVER", **_LB},   # s59 P6: tallest on the Singapore River waterfront (11.7s)
    {"img": "KITLV", **_LB},   # s62 P7: December 1964 - the closure announced (18.5s)
    {"img": "RIVER", **_LB},   # s64 P7: the closure was never carried out (3.1s)
    {"img": "TODAY2", **_LB},   # s67 P8: the building today is two buildings (3.2s)
    {"img": "TODAY1", **_LB},   # s71 P8: no conservation status; unlisted and largely unremarked (22.8s)
]
SCHEDULE = [(0.000, 0), (3.725, 1), (19.700, 2), (24.875, 3), (28.825, 4), (32.875, 5), (56.300, 6), (61.925, 7), (72.725, 8), (82.425, 9), (93.575, 10), (107.525, 11), (111.225, 12), (122.900, 13), (141.425, 14), (144.575, 15), (147.750, 16)]
TOTAL_DURATION = 170.500
TIMING_JSON = "audio/the-bank-of-china-building-on-battery-road-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
