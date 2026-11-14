"""Video config for the Kampong Lorong Buangkok post.

The pool is all thirteen pictures from the post and its gallery:
Erwin Soo's 2013 black-and-white photo journal of the village, two
2014 house photographs, a 2008 kampong house from the English
Wikipedia, Muhammad Adrian's 2025 surau pair and M. Adrian
Jurhami's 2026 pair. Thirteen pictures for nine and a half
minutes is a comfortable pool; images recur at new story beats
with varied pans and alternating zoom direction, never twice
in a row.

Named-person rule: the pool holds no portrait of Sng Mui Hong,
Sng Teow Koon, Huang Yu Tu, Awe Bin Ludin, Mohamed Sulaiman,
Intan Azura Mokhtar or Desmond Lee, so every sentence naming a
person shows the village, its houses or its surau - never
another person.

This is the first post whose slides carry the discreet photo
titles (Chris, 2026-11-11): each slide's "title" is the short
form of its image's post/gallery caption, drawn small in the top
corner on a soft dark backing for the slide's whole run.

43 slides, 564.45s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

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

# The channel's 2x2 thumbnail grid, in story order: the way in,
# a village home, the surau, and the old house sign.
THUMBNAIL = [
    {"img": "WELCOME", "pan": (0.5, 0.5)},
    {"img": "VILLAGE", "pan": (0.5, 0.5)},
    {"img": "SURAU", "pan": (0.5, 0.5)},
    {"img": "SIGN", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  s0 title: the last kampong on the mainland (4.7s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 1  s1-2 rent: $6.50 a month, $30 at most (8.8s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 2  s3 frozen forty years; rice or fruit if a tenant is short (9.1s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 3  s4 twenty-five families behind the Buangkok Green blocks (12.0s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  s5 the landlady: Sng Mui Hong, seventy-one (names her: a house, no portrait) (12.0s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 5  s6-8 'As long as I have enough to live, that's already fine' (12.2s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  s9 the last kampong on mainland Singapore (10.2s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 7  s10 1956: Sng Teow Koon buys the swamp from Huang Yu Tu (names them: the land) (12.7s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s11-12 a medicine seller; the first houses go up (14.1s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 9  s13 gotong royong: sand hauled, each other's houses raised (19.9s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 10  s14 Woodbridge Hospital and rubber-plantation workers (12.3s)
    {"img": "METER", **{"type": "cover", "title": "Power to a wooden house, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  s15-16 the 1960s peak, forty families; water and power, 1962 (10.9s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s17 Kampong Selak Kain: lift up your sarong (13.9s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 13  s18 the floods never left; March 2004 (16.2s)
    {"img": "SURAU", **{"type": "cover", "title": "Surau Al-Firdaus, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 14  s19-20 the stream fenced; Surau Al-Firdaus, built 1953 (18.2s)
    {"img": "ABLUTION", **{"type": "cover", "title": "The surau's washing area, 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 15  s21 the surau draws worshippers from outside too (7.9s)
    {"img": "SURAU", **{"type": "cover", "title": "Surau Al-Firdaus, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  s22 Awe Bin Ludin, the 2004 headman (names him: the surau) (12.9s)
    {"img": "SHOO", **{"type": "cover", "title": "Pigeons take flight, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 17  s23 chickens, gardens, dirt tracks, old signs (16.2s)
    {"img": "SIGN", **{"type": "cover", "title": "House sign: 23-C Lorong Buangkok, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 18  s24-25 'Lorong Buang Kok 1954' is a postal code, not a founding year (16.5s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 19  s26 a nation rehoused; the kampongs went one by one (10.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 20  s27-29 a legal reason and a human one (16.6s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 21  s30-31 1997: the land passes to four children; Mui Hong stays (12.0s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 22  s32-33 her promise to her father; $300 a month in 2007 (15.1s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 23  s34 no new tenants since the 1990s (12.6s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 24  s35-36 tenants own their houses; the $33 million valuation (16.6s)
    {"img": "STOVE", **{"type": "cover", "title": "The earthenware stove, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 25  s37 'simplicity and freedom' (her words: the stove) (8.8s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 26  s38 the New York Times, 2009: 'a deep attachment to my neighbours' (16.7s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 27  s39-40 'like my own parents... Malay or Chinese' (8.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 28  s41-42 fame: the flood, the valuation, the Times, the BBC (18.6s)
    {"img": "EXPLORERS", **{"type": "cover", "title": "Young explorers, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 29  s43 documentary crews, school groups and weekend walkers (4.6s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 30  s44 guided tours meet Sng Mui Hong at home (names her: a house) (13.3s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 31  s45-46 the price of fame: fences, locked doors, curtains drawn (16.6s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s47 private residential land, not a museum (16.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 33  s48-49 the Master Plan: a road, two schools, a park (14.9s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 34  s50 2014: public calls to conserve it instead (7.3s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 35  s51 Parliament, 2017: 'several decades later' (names Mokhtar and Lee: the village) (19.6s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s52 no conservation status; its protection is its owners (7.7s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 37  s53-55 Mohamed Sulaiman: 'if can stay, I happy' (names him: a house) (19.2s)
    {"img": "SURAU", **{"type": "cover", "title": "Surau Al-Firdaus, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 38  s56 the village goes on: the surau's green roof, the mango trees (18.0s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 39  s57-59 her advice: 'Don't think so far ahead' (15.8s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  s60 the bigger story: kampongs cleared by policy (9.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 41  s61 a medicine seller bought a swamp; his daughter decided enough was enough (10.2s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 42  s62 no direct offers, does not know or care; still standing (16.6s)
]

SCHEDULE = [
    (0.000, 0), (4.725, 1), (13.500, 2), (22.625, 3), (34.625, 4), (46.650, 5),
    (58.800, 6), (68.975, 7), (81.675, 8), (95.725, 9), (115.675, 10), (128.000, 11),
    (138.875, 12), (152.800, 13), (169.000, 14), (187.225, 15), (195.125, 16), (208.075, 17),
    (224.275, 18), (240.800, 19), (250.775, 20), (267.400, 21), (279.375, 22), (294.475, 23),
    (307.050, 24), (323.625, 25), (332.400, 26), (349.100, 27), (357.075, 28), (375.700, 29),
    (380.325, 30), (393.625, 31), (410.225, 32), (426.200, 33), (441.150, 34), (448.425, 35),
    (468.000, 36), (475.675, 37), (494.850, 38), (512.850, 39), (528.650, 40), (537.675, 41),
    (547.850, 42)
]
TOTAL_DURATION = 564.45
TIMING_JSON = "audio/kampong-lorong-buangkok-the-last-kampong-on-the-mainland.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
