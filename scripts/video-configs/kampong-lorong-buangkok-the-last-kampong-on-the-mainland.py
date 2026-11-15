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

46 slides, 622.55s. RERUN 2026-11-15: the post gained a re-anchored
opening and Chris's personal closing note after the first render;
this config is re-timed against the new narration.
SOFTEN re-render 2026-11-15: re-timed once more after the rent
sentence was softened; sentence 4 grew from 9.3s to 17.0s. Narration:
Kokoro with the OpenVoice clone.
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
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  s0-1 title + 'It survived.' (6.4s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 1  s2-3 rent: $6.50 a month, $30 at most (15.3s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 2  s4 the rent figures barely moved in decades; rice or fruit if a tenant is short (17.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 3  s5 twenty-five families behind the Buangkok Green blocks (12.0s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  s6 the landlady: Sng Mui Hong, seventy-one (names her: a house, no portrait) (12.0s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 5  s7-9 'As long as I have enough to live, that's already fine' (12.2s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  s10 the last kampong on mainland Singapore (10.2s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 7  s11 1956: Sng Teow Koon buys the swamp from Huang Yu Tu (names them: the land) (12.7s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s12-13 a medicine seller; the first houses go up (14.0s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 9  s14 gotong royong: sand hauled, each other's houses raised (19.9s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 10  s15 Woodbridge Hospital and rubber-plantation workers (12.3s)
    {"img": "METER", **{"type": "cover", "title": "Power to a wooden house, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  s16-17 the 1960s peak, forty families; water and power, 1962 (10.9s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s18 Kampong Selak Kain: lift up your sarong (13.9s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 13  s19 the floods never left; March 2004 (16.2s)
    {"img": "SURAU", **{"type": "cover", "title": "Surau Al-Firdaus, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 14  s20-21 the stream fenced; Surau Al-Firdaus, built 1953 (18.2s)
    {"img": "ABLUTION", **{"type": "cover", "title": "The surau's washing area, 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 15  s22 the surau draws worshippers from outside too (7.9s)
    {"img": "SURAU", **{"type": "cover", "title": "Surau Al-Firdaus, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  s23 Awe Bin Ludin, the 2004 headman (names him: the surau) (12.9s)
    {"img": "SHOO", **{"type": "cover", "title": "Pigeons take flight, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 17  s24 chickens, gardens, dirt tracks, old signs (16.2s)
    {"img": "SIGN", **{"type": "cover", "title": "House sign: 23-C Lorong Buangkok, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 18  s25-26 'Lorong Buang Kok 1954' is a postal code, not a founding year (16.5s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 19  s27 a nation rehoused; the kampongs went one by one (10.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 20  s28-30 a legal reason and a human one (16.6s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 21  s31-32 1997: the land passes to four children; Mui Hong stays (12.0s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 22  s33-34 her promise to her father; $300 a month in 2007 (15.1s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 23  s35 no new tenants since the 1990s (12.6s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 24  s36-37 tenants own their houses; the $33 million valuation (16.6s)
    {"img": "STOVE", **{"type": "cover", "title": "The earthenware stove, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 25  s38 'simplicity and freedom' (her words: the stove) (8.8s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 26  s39 the New York Times, 2009: 'a deep attachment to my neighbours' (16.7s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 27  s40-41 'like my own parents... Malay or Chinese' (8.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 28  s42-43 fame: the flood, the valuation, the Times, the BBC (18.6s)
    {"img": "EXPLORERS", **{"type": "cover", "title": "Young explorers, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 29  s44 documentary crews, school groups and weekend walkers (4.6s)
    {"img": "VERANDAH", **{"type": "cover", "title": "A house with its verandah, 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 30  s45 guided tours meet Sng Mui Hong at home (names her: a house) (13.3s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 31  s46-47 the price of fame: fences, locked doors, curtains drawn (16.6s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s48 private residential land, not a museum (16.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 33  s49-50 the Master Plan: a road, two schools, a park (15.0s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 34  s51 2014: public calls to conserve it instead (7.3s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 35  s52 Parliament, 2017: 'several decades later' (names Mokhtar and Lee: the village) (19.6s)
    {"img": "TYPICAL", **{"type": "cover", "title": "A typical kampong house, 2008", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s53 no conservation status; its protection is its owners (7.7s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.12, 1.06, 1.0], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 37  s54-56 Mohamed Sulaiman: 'if can stay, I happy' (names him: a house) (19.2s)
    {"img": "SURAU", **{"type": "cover", "title": "Surau Al-Firdaus, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 38  s57 the village goes on: the surau's green roof, the mango trees (18.0s)
    {"img": "DOOR", **{"type": "cover", "title": "An entrance door, 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 39  s58-60 her advice: 'Don't think so far ahead' (15.8s)
    {"img": "OVERGROWN", **{"type": "cover", "title": "Taken back by green, 2013", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  s61 the bigger story: kampongs cleared by policy (9.0s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 41  s62 a medicine seller bought a swamp; his daughter decided enough was enough (10.2s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 42  s63 no direct offers, does not know or care; still standing (16.6s)
    {"img": "EXPLORERS", **{"type": "cover", "title": "Young explorers, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 43  s64-65 a note of my own: I grew up in Aukang, a few streets away (18.2s)
    {"img": "VILLAGE", **{"type": "cover", "title": "A village house, 2014", "zoom": [1.0, 1.06, 1.12], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 44  s66-67 never thought of it as the last kampong; too far to walk, to a boy (13.6s)
    {"img": "WELCOME", **{"type": "cover", "title": "The way into the kampong, 2013", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 45  s68-69 five miles - my Maryland walk; 'On my next visit home, I intend to walk it' (10.2s)
]

SCHEDULE = [
    (0.000, 0), (6.400, 1), (21.725, 2), (38.700, 3), (50.700, 4), (62.725, 5),
    (74.875, 6), (85.050, 7), (97.750, 8), (111.800, 9), (131.750, 10), (144.075, 11),
    (154.950, 12), (168.875, 13), (185.075, 14), (203.300, 15), (211.200, 16), (224.150, 17),
    (240.350, 18), (256.875, 19), (266.850, 20), (283.475, 21), (295.450, 22), (310.550, 23),
    (323.125, 24), (339.700, 25), (348.475, 26), (365.175, 27), (373.150, 28), (391.775, 29),
    (396.400, 30), (409.700, 31), (426.300, 32), (442.275, 33), (457.225, 34), (464.500, 35),
    (484.075, 36), (491.750, 37), (510.925, 38), (528.925, 39), (544.725, 40), (553.750, 41),
    (563.925, 42), (580.525, 43), (598.750, 44), (612.375, 45)
]
TOTAL_DURATION = 622.55
TIMING_JSON = "audio/kampong-lorong-buangkok-the-last-kampong-on-the-mainland.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
