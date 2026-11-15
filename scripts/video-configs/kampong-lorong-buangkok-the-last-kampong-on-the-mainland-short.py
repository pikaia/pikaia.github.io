"""Short config for the Kampong Lorong Buangkok post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py kampong-lorong-buangkok-the-last-kampong-on-the-mainland 2,4,5,6,7,11,29,37,38,44,50,52,55,56,62,65,69
(17 sentences, 176.30s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)
RERUN 2026-11-15: re-picked against the new narration (the
post gained a re-anchored opening and a personal closing note).
SOFTEN re-render 2026-11-15: the softened rent sentence (s4)
grew from 9.3s to 17.0s and pushed the old pick over the
180s ceiling (180.23s); s46 was cut, leaving 17 sentences
at 176.30s.

The post's points, and the sentences that carry each:
1. The rent hook: $6.50 a month, the figures barely moved
   in decades, payment in kind accepted. (s2, s4)
2. The place and its keeper: twenty-five families - twelve
   Chinese, thirteen Malay - behind the Buangkok Green blocks;
   the landlady, Sng Mui Hong; her rule: "As long as I have
   enough to live, that's already fine." (s5, s6, s7)
3. The founding: in 1956 Sng Teow Koon, a medicine seller,
   bought 12,248 square metres of swamp. (s11)
4. Why it survived: the land was private - and when it was
   valued at $33 million in 2007, the family's answer was "My
   family ties are not for sale"; simplicity and freedom over
   money. (s29, s37, s38)
5. Fame: documentary crews, school groups and weekend
   walkers followed. (s44) The attention-has-a-price sentence
   (s46) was the cut that kept this Short under the ceiling.
6. The drawn future: Master Plan parcels - a road, two schools,
   a park - and Parliament told in 2017 that redevelopment
   would likely come only "several decades later". (s50, s52)
7. The close: a resident's contentment - "if can stay, I
   happy" - and the reason the village stands: a medicine
   seller bought a swamp, and his youngest daughter decided
   enough money was enough. (s55, s56, s62)
8. The author's own note: he grew up in Aukang, a few streets
   from the kampong, and on his next visit home he intends to
   walk the five miles he once thought unwalkable. (s65, s69)

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
    {"img": "VILLAGE", **_LB, "title": "A village house, 2014"},   # s2 rent: $6.50 a month (11.7s)
    {"img": "TYPICAL", **_LB, "title": "A typical kampong house, 2008"},   # s4 the rent figures barely moved in decades; rice or fruit if a tenant is short (17.0s)
    {"img": "WELCOME", **_LB, "title": "The way into the kampong, 2013"},   # s5 twenty-five families behind the Buangkok Green blocks (12.0s)
    {"img": "VERANDAH", **_LB, "title": "A house with its verandah, 2026"},   # s6 the landlady: Sng Mui Hong, seventy-one (names her: a house) (12.0s)
    {"img": "DOOR", **_LB, "title": "An entrance door, 2026"},   # s7 'As long as I have enough to live, that's already fine' (4.7s)
    {"img": "OVERGROWN", **_LB, "title": "Taken back by green, 2013"},   # s11 1956: Sng Teow Koon buys the swamp (names him: the land) (12.7s)
    {"img": "WELCOME", **_LB, "title": "The way into the kampong, 2013"},   # s29 the legal reason: the land was private (6.7s)
    {"img": "VERANDAH", **_LB, "title": "A house with its verandah, 2026"},   # s37 the $33 million valuation; 'My family ties are not for sale' (11.6s)
    {"img": "TYPICAL", **_LB, "title": "A typical kampong house, 2008"},   # s38 'simplicity and freedom' (8.8s)
    {"img": "EXPLORERS", **_LB, "title": "Young explorers, 2013"},   # s44 documentary crews, school groups and weekend walkers (4.6s)
    {"img": "OVERGROWN", **_LB, "title": "Taken back by green, 2013"},   # s50 the Master Plan: a road, two schools, a park (10.8s)
    {"img": "WELCOME", **_LB, "title": "The way into the kampong, 2013"},   # s52 Parliament, 2017: 'several decades later' (names Mokhtar and Lee: the village) (19.6s)
    {"img": "VILLAGE", **_LB, "title": "A village house, 2014"},   # s55 Mohamed Sulaiman: 'if can stay, 20 year...' (names him: a house) (8.4s)
    {"img": "TYPICAL", **_LB, "title": "A typical kampong house, 2008"},   # s56 '...but if can stay, I happy' (5.8s)
    {"img": "VERANDAH", **_LB, "title": "A house with its verandah, 2026"},   # s62 a medicine seller bought a swamp; his daughter decided enough was enough (10.2s)
    {"img": "EXPLORERS", **_LB, "title": "Young explorers, 2013"},   # s65 a note of my own: I grew up in Aukang, a few streets away (16.1s)
    {"img": "WELCOME", **_LB, "title": "The way into the kampong, 2013"},   # s69 'On my next visit home, I intend to walk it' (3.7s)
]
SCHEDULE = [
    (0.000, 0), (11.700, 1), (28.675, 2), (40.675, 3), (52.700, 4), (57.375, 5),
    (70.075, 6), (76.725, 7), (88.300, 8), (97.075, 9), (101.700, 10), (112.500, 11),
    (132.075, 12), (140.500, 13), (146.325, 14), (156.500, 15), (172.575, 16)
]
TOTAL_DURATION = 176.30
TIMING_JSON = "audio/kampong-lorong-buangkok-the-last-kampong-on-the-mainland-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
