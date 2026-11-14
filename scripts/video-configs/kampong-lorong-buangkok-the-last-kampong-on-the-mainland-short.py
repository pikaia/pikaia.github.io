"""Short config for the Kampong Lorong Buangkok post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py kampong-lorong-buangkok-the-last-kampong-on-the-mainland 1,3,4,6,10,12,28,36,37,44,46,49,51,54,61
(15 sentences, 155.30s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The rent hook: $6.50 a month, frozen about forty years,
   payment in kind accepted. (s1, s3)
2. The place and its keeper: twenty-five families - twelve
   Chinese, thirteen Malay - behind the Buangkok Green blocks;
   the landlady's rule: "As long as I have enough to live,
   that's already fine." (s4, s6)
3. The founding: in 1956 Sng Teow Koon, a medicine seller,
   bought 12,248 square metres of swamp; the first families
   built on rented parcels. (s10, s12)
4. Why it survived: the land was private - and when it was
   valued at $33 million in 2007, the family's answer was "My
   family ties are not for sale"; simplicity and freedom over
   money. (s28, s36, s37)
5. Fame and its price: guided tours bring visitors to meet
   Sng Mui Hong at home, while residents fence their plots and
   lock their doors against the attention. (s44, s46)
6. The drawn future: Master Plan parcels - a road, two schools,
   a park - and Parliament told in 2017 that redevelopment
   would likely come only "several decades later". (s49, s51)
7. The close: a resident's contentment - "if can stay, I
   happy" - and the reason the village stands: a medicine
   seller bought a swamp, and his youngest daughter decided
   enough money was enough. (s54, s61)

Every slide is letterboxed and carries its photo title, as in
the main config. Named-person rule as in the main config: no
portraits exist in the pool, so named sentences show the
village and its houses.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "WELCOME": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Photo_Journal_%28set%29_-_Welcome_to_Kampung_Buangkok_%289723403703%29.jpg",
    "SURAU": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Surau_Al_Firdaus_at_Kampong_Lorong_Buangkok_-_54292246824.jpg",
    "ABLUTION": "https://upload.wikimedia.org/wikipedia/commons/f/f7/Surau_Al_Firdaus_at_Kampong_Lorong_Buangkok_3.jpg",
    "VERANDAH": "https://upload.wikimedia.org/wikipedia/commons/d/de/Village_house_with_verandah_and_diner.jpg",
    "SIGN": "https://upload.wikimedia.org/wikipedia/commons/5/59/Lorong_Buangkok_Singapore_signage.JPG",
    "TYPICAL": "https://upload.wikimedia.org/wikipedia/commons/6/66/A_Typical_Kampong_House.JPG",
    "VILLAGE": "https://upload.wikimedia.org/wikipedia/commons/9/92/Lorong_Buangkok_house.JPG",
    "DOOR": "https://upload.wikimedia.org/wikipedia/commons/d/df/An_entrance_door_in_Kampong_Lorong_Buangkok.jpg",
    "METER": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Photo_Journal_%28Set%29_-_A_power_supply_meter_to_a_wooden_kampung_house_%289682076337%29.jpg",
    "STOVE": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Photo_Journal_%28set%29_-_An_earthernware_stove_%289719616498%29.jpg",
    "SHOO": "https://upload.wikimedia.org/wikipedia/commons/2/29/Photo_Journal_%28Set%29_-_Shoo%21_%289695528234%29.jpg",
    "EXPLORERS": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Photo_Journal_%28Set%29_-_Young_explorers_%289719102704%29.jpg",
    "OVERGROWN": "https://upload.wikimedia.org/wikipedia/commons/6/6a/Photo_Journal_%28Set%29_-_Overgrown_%289685319060%29_%282%29.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "WELCOME", "pan": (0.5, 0.5)},
    {"img": "VILLAGE", "pan": (0.5, 0.5)},
    {"img": "SURAU", "pan": (0.5, 0.5)},
    {"img": "SIGN", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "VILLAGE", **_LB, "title": "A village house, 2014"},   # s1 rent: $6.50 a month (5.2s)
    {"img": "TYPICAL", **_LB, "title": "A typical kampong house, 2008"},   # s3 frozen forty years; rice or fruit if a tenant is short (9.1s)
    {"img": "WELCOME", **_LB, "title": "The way into the kampong, 2013"},   # s4 twenty-five families behind the Buangkok Green blocks (12.0s)
    {"img": "DOOR", **_LB, "title": "An entrance door, 2026"},   # s6 'As long as I have enough to live, that's already fine' (4.7s)
    {"img": "OVERGROWN", **_LB, "title": "Taken back by green, 2013"},   # s10 1956: Sng Teow Koon buys the swamp (names him: the land) (12.7s)
    {"img": "VILLAGE", **_LB, "title": "A village house, 2014"},   # s12 the first families build on rented parcels (9.7s)
    {"img": "WELCOME", **_LB, "title": "The way into the kampong, 2013"},   # s28 the legal reason: the land was private (6.7s)
    {"img": "VERANDAH", **_LB, "title": "A house with its verandah, 2026"},   # s36 the $33 million valuation; 'My family ties are not for sale' (11.6s)
    {"img": "TYPICAL", **_LB, "title": "A typical kampong house, 2008"},   # s37 'simplicity and freedom' (8.8s)
    {"img": "EXPLORERS", **_LB, "title": "Young explorers, 2013"},   # s44 guided tours meet Sng Mui Hong at home (names her: the visitors) (13.3s)
    {"img": "DOOR", **_LB, "title": "An entrance door, 2026"},   # s46 the price of fame: fences, locked doors, curtains drawn (12.7s)
    {"img": "OVERGROWN", **_LB, "title": "Taken back by green, 2013"},   # s49 the Master Plan: a road, two schools, a park (10.8s)
    {"img": "WELCOME", **_LB, "title": "The way into the kampong, 2013"},   # s51 Parliament, 2017: 'several decades later' (names Mokhtar and Lee: the village) (19.6s)
    {"img": "VILLAGE", **_LB, "title": "A village house, 2014"},   # s54 Mohamed Sulaiman: 'if can stay, I happy' (names him: a house) (8.4s)
    {"img": "VERANDAH", **_LB, "title": "A house with its verandah, 2026"},   # s61 a medicine seller bought a swamp; his daughter decided enough was enough (10.2s)
]
SCHEDULE = [
    (0.000, 0), (5.150, 1), (14.275, 2), (26.275, 3), (30.950, 4), (43.650, 5),
    (53.350, 6), (60.000, 7), (71.575, 8), (80.350, 9), (93.650, 10), (106.325, 11),
    (117.125, 12), (136.700, 13), (145.125, 14)
]
TOTAL_DURATION = 155.3
TIMING_JSON = "audio/kampong-lorong-buangkok-the-last-kampong-on-the-mainland-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
