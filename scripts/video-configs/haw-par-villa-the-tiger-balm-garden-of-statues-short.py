"""Short config for the Haw Par Villa post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py haw-par-villa-the-tiger-balm-garden-of-statues 0,1,7,12,37,40,44,57,59,64,67
(11 sentences, 170.10s - under the 3-minute
Shorts ceiling with margin, and well over TikTok's
1-minute floor.)

The post's points, and the sentences that carry each:
1. The hook: the strangest garden in Singapore. (s0, s1)
2. The founding: the 1937 villa, Boon Haw's gift. (s7)
3. The purpose: advertisement and moral school. (s12)
4. War and rebuilding: the famous garden is post-war. (s37)
5. The Ten Courts of Hell. (s40, s44)
6. Dragon World, the failed theme park. (s57)
7. A free public park again from 2001. (s59)
8. Hell's Museum, 2021. (s64)
9. The present limbo: partly closed since Dec 2025. (s67)

Compression casualties, noted honestly: the Swatow
craftsmen, the four tiers and the zoo, Cheng Chye and
the million-visitor peak, the 1985 donation terms, the
schoolchildren and the statues-come-alive legend, the
MRT station and Haw Ror Villa are carried by their
neighbours or dropped; the spine - founding, purpose,
war and rebuilding, the Courts, the theme park, the
free park, the museum, the closure - is intact.

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24). All four THUMBNAIL
keys (PAIFANG, COURT1, GARDEN1963, HELLGATE) are in
IMAGES and used by slides, for the step-8.3 grid.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "PAIFANG": "https://upload.wikimedia.org/wikipedia/commons/1/14/Haw_Par_Villa_Paifang.jpg",
    "HILLS": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Hilly_grounds_of_Haw_Par_Villa_%2814813779273%29.jpg",
    "ARCH2014": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Chinese_arch_at_entrance_of_Haw_Par_Villa_%2814791657844%29.jpg",
    "LANE": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Virtues_and_Vices_lane%2C_Haw_Par_Villa_%2814607157740%29.jpg",
    "GARDEN1963": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Haw_Par_Villa_Tiger_Balm_Gardens_Singapore_1963_01.jpg",
    "COURTCU": "https://upload.wikimedia.org/wikipedia/commons/d/db/Chinese_Court_of_Hell.jpg",
    "COURT1": "https://upload.wikimedia.org/wikipedia/commons/4/48/First_Court_of_Hell%2C_Haw_Par_Villa_%2814607331868%29.jpg",
    "HELLGATE": "https://upload.wikimedia.org/wikipedia/commons/4/45/Entrance_to_10_Courts_of_Hell.jpg",
}

CREDITS = {}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "PAIFANG", **_LB, "title": "Haw Par Villa"},  # 0  title (4.03s) (s0)
    {"img": "HILLS", **_LB, "title": "The strangest garden in Singapore"},  # 1  the hook: the hillside of painted statues (20.38s) (s1)
    {"img": "ARCH2014", **_LB, "title": "The gift to Boon Par"},  # 2  the Art Deco villa of 1937, Boon Haw's gift (10.05s) (s7)
    {"img": "LANE", **_LB, "title": "A school in statues"},  # 3  a school: piety, charity, judgement after death (14.30s) (s12)
    {"img": "GARDEN1963", **_LB, "title": "Rebuilt after the war"},  # 4  Boon Haw rebuilds and enlarges the garden (13.70s) (s37)
    {"img": "COURTCU", **_LB, "title": "The Ten Courts of Hell"},  # 5  the walk-through of the underworld (16.48s) (s40)
    {"img": "COURT1", **_LB, "title": "The First Court of Hell"},  # 6  the bridges and the Mirror of Retribution (14.32s) (s44)
    {"img": "HELLGATE", **_LB, "title": "Dragon World, 1990"},  # 7  the theme park; the Courts inside a dragon (17.38s) (s57)
    {"img": "HILLS", **_LB, "title": "A free public park again"},  # 8  free again in 2001, as in the family's day (11.50s) (s59)
    {"img": "HELLGATE", **_LB, "title": "Hell's Museum, 2021"},  # 9  the world's first museum of death and the afterlife (24.65s) (s64)
    {"img": "PAIFANG", **_LB, "title": "Partly closed, awaiting its future"},  # 10  the contract ends; the park partly closes (23.32s) (s67)
]

SCHEDULE = [
    (0.000, 0), (4.025, 1), (24.400, 2),
    (34.450, 3), (48.750, 4), (62.450, 5),
    (78.925, 6), (93.250, 7), (110.625, 8),
    (122.125, 9), (146.775, 10)
]
TOTAL_DURATION = 170.100
TIMING_JSON = "audio/haw-par-villa-the-tiger-balm-garden-of-statues-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
