"""Short config for the St John's Island post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py st-johns-island-the-quarantine-island 1,7,23,31,33,40,46,58,62,69,75,82,87
(13 sentences, 171.875s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The doorstep: for a century, arrivals by sea began their Singapore story on this island. (s1)
2. 1819: Raffles' fleet anchors off St John's the day before the landing. (s7)
3. The founding: cholera forces a station; it opens in November 1874 with the Milton's passengers. (s23)
4. How it worked: muster sheds, disinfection, camps, vaccination. (s31)
5. The class system: the steerage were held, cabin passengers walked ashore. (s33)
6. The scale: 8 million inspected, 300,000 quarantined in twenty years. (s40)
7. The voices: Teo Choon Hong on the lower deck, 1937. (s46)
8. Detention: Devan Nair's "St John's University" and Lee Kuan Yew's 1952 visit. (s58)
9. The other cure: the Opium Treatment Centre, 1955. (s62)
10. The end of quarantine: the station closes on 14 January 1976. (s69)
11. The island today: ferries, the Lodge in the old camps, the marine laboratories (folded into this beat). (s75)
12. The cats: over a hundred in 2014, a small ageing colony now. (s82)
13. The close: the door has closed; the doorstep remains. (s87)

Every slide is letterboxed and carries its photo title, as
in the main config. The pool holds no portraits, so the
named-person rule is met by construction.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HILL": "https://upload.wikimedia.org/wikipedia/commons/9/93/St._John%27s_Island%2C_Singapore%3B_the_Quarantine_Station%2C_Wellcome_V0030663.jpg",
    "SEA": "https://upload.wikimedia.org/wikipedia/commons/6/68/The_Quarantine_Station%2C_St._John%27s_Island%2C_Singapore._Wellcome_V0030662.jpg",
    "HOUSE": "https://upload.wikimedia.org/wikipedia/commons/7/70/The_Quarantine_Station%2C_St._John%27s_Island%2C_Singapore_Wellcome_V0030660.jpg",
    "DISINFECT": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Quarantine_Centre_disinfection_buildings_on_St_John_Island_by_FR_Sayers_%281930%29.jpg",
    "VACCINATE": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Photo_of_vaccination_of_male_passengers_on_St_John_Island_by_FR_Sayers_%281930%29.jpg",
    "JETTY": "https://upload.wikimedia.org/wikipedia/commons/0/0d/St_John%27s_Island_jetty.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/a/a6/St._John%27s_Island%2C_Singapore%2C_2023_1.jpg",
    "LAB": "https://upload.wikimedia.org/wikipedia/commons/5/5d/St._John%27s_Island%2C_Singapore%2C_2023_4.jpg",
    "SKYLINE": "https://upload.wikimedia.org/wikipedia/commons/0/0e/St._John%27s_Island%2C_Singapore%2C_2023_3.jpg",
    "BEACH2": "https://upload.wikimedia.org/wikipedia/commons/7/74/St._John%27s_Island%2C_Singapore%2C_2023_2.jpg",
    "DOWNHILL": "https://upload.wikimedia.org/wikipedia/commons/8/86/St._John%27s_Island%2C_Singapore%2C_2023_5.jpg",
    "NORTHVIEW": "https://upload.wikimedia.org/wikipedia/commons/9/91/St._John%27s_Island%2C_Singapore%2C_2023_7.jpg",
    "BEACHWATER": "https://upload.wikimedia.org/wikipedia/commons/4/44/St._John%27s_Island%2C_Singapore%2C_2023_8.jpg",
    "TOWERS": "https://upload.wikimedia.org/wikipedia/commons/4/40/St._John%27s_Island%2C_Singapore%2C_2023_6.jpg",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/8/8a/St_John%27s_Island_Panorama.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HILL", "pan": (0.5, 0.5)},
    {"img": "DISINFECT", "pan": (0.5, 0.5)},
    {"img": "JETTY", "pan": (0.5, 0.5)},
    {"img": "SKYLINE", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HILL", **_LB, "title": "The quarantine station from the hill, 1909"},   # s1 every stranger who came by sea began their Singapore story here (13.57s),
    {"img": "SEA", **_LB, "title": "St John's Island from the water, 1909"},   # s7 28 January 1819: Raffles' fleet anchors off the island (15.53s),
    {"img": "HILL", **_LB, "title": "The quarantine station from the hill, 1909"},   # s23 November 1874: the station opens; the cholera ship Milton is its first intake (19.35s),
    {"img": "VACCINATE", **_LB, "title": "Vaccination on landing, 1930"},   # s31 the camps: disinfection, vaccination, and the wait (15.72s),
    {"img": "HOUSE", **_LB, "title": "A station house among the trees, 1909"},   # s33 the class system: cabin passengers walk ashore (13.50s),
    {"img": "HILL", **_LB, "title": "The quarantine station from the hill, 1909"},   # s40 8 million inspected and 300,000 quarantined, 1903-1923 (11.93s),
    {"img": "HOUSE", **_LB, "title": "A station house among the trees, 1909"},   # s46 Teo Choon Hong, 1937: the lower deck was quarantined (9.97s),
    {"img": "SEA", **_LB, "title": "St John's Island from the water, 1909"},   # s58 Devan Nair's St John's University; Lee Kuan Yew's visit, 1952 (17.02s),
    {"img": "HOUSE", **_LB, "title": "A station house among the trees, 1909"},   # s62 1955: the Opium Treatment Centre opens (14.88s),
    {"img": "HILL", **_LB, "title": "The quarantine station from the hill, 1909"},   # s69 14 January 1976: the quarantine station closes (9.72s),
    {"img": "JETTY", **_LB, "title": "The island's jetty from above, 2022"},   # s75 today: ferries from Marina South Pier, the Lodge in the old camps (17.50s),
    {"img": "BEACH2", **_LB, "title": "Pier Beach, the landing shore, 2023"},   # s82 the cats: over a hundred in 2014, an ageing colony now (9.53s),
    {"img": "SKYLINE", **_LB, "title": "Singapore from St John's Island, 2023"},   # s87 the door has closed; the doorstep remains (3.65s)
]
SCHEDULE = [
    (0.000, 0), (13.575, 1), (29.100, 2), (48.450, 3), (64.175, 4), (77.675, 5),
    (89.600, 6), (99.575, 7), (116.600, 8), (131.475, 9), (141.200, 10), (158.700, 11),
    (168.225, 12)
]
TOTAL_DURATION = 171.875
TIMING_JSON = "audio/st-johns-island-the-quarantine-island-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
