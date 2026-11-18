"""Short config for the kopitiam two-eggs post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py the-kopitiams-two-eggs-the-breakfast-that-outlived-a-health-scare 1,7,14,25,27,28,38,44,55,64,80,85,86,93,94
(15 sentences, 170.40s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The set itself: two eggs, kaya toast and kopi, in a form
   barely changed in a century. (s1)
2. The eggs are steeped, not boiled. (s7)
3. Why two eggs: a documented custom with no documented
   origin. (s14)
4. Ya Kun's founding: Loi Ah Koon arrived from Hainan in
   1926 and built a stall into the chain. (s25)
5. The chain went international - and one Tokyo outlet stood
   in the Kasumigaseki Building, where the author once worked
   during his AOTS time. (s27, s28)
6. The scare opens: in 1968 the American Heart Association
   allowed no more than three eggs a week. (s38)
7. Two kopitiam eggs deliver 372 to 480 milligrams - the
   whole day's cholesterol budget in one saucer. (s44)
8. The swing back completes: the 2020 BMJ analysis of 1.72
   million people found no association. (s55)
9. Singapore never swung with it: Singaporeans went on
   ordering the two eggs on the Board's own numbers. (s64)
10. The kopi-o was graded, not banned - the grading points
    at the sugar, not the bean. (s80)
11. The only thing that ever removed the two eggs was not a
    guideline; it was a shortage (the 2004 bird-flu ban).
    (s85, s86)
12. The close: the two eggs survived the scare, and nobody
    ever decided they should. (s93, s94)

Every slide is letterboxed and carries its photo title, as in
the main config. The pool holds no portraits, so the
named-person rule is met by construction.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Kaya_Toast_with_Coffee.jpg",
    "EGGS": "https://upload.wikimedia.org/wikipedia/commons/4/46/EatingSoftBoiledEggs-Singapore-20080509.jpg",
    "KASUMI": "https://upload.wikimedia.org/wikipedia/commons/b/b2/Kasumi_Dining%2C_Kasumigaseki_Building%2C_Tokyo_-_Jun_19%2C_2009.jpg",
    "CMC": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Chin_Mee_Chin_Confectionery.jpg",
    "PLATE": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Kaya_toast_on_a_plate.jpg",
    "KOPIO": "https://upload.wikimedia.org/wikipedia/commons/5/53/Kopi_O.jpg",
    "DIP": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Kaya_toast_dip_into_soft_boiled_egg.jpg",
    "YAKUN25": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Good_morning_Singapore_-_Ya_Kun_Kaya_Toast%2C_January_2025.jpg",
    "G_SET": "https://upload.wikimedia.org/wikipedia/commons/8/85/Ya_Kun_Koya_toast%2C_eggs_and_coffee.jpg",
    "G_YAKUN16": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Kaya_toast_from_Ya_Kun_Kaya_Toast%2C_Singapore_-_20160813.jpg",
    "G_CRACK": "https://upload.wikimedia.org/wikipedia/commons/5/55/Cream_crackers_with_kaya_and_butter%2C_Ya_Kun_Kaya_Toast%2C_Singapore_-_20160807.jpg",
    "G_TOAST": "https://upload.wikimedia.org/wikipedia/commons/0/05/Kopitiam_Toast.jpg",
    "G_CMC25": "https://upload.wikimedia.org/wikipedia/commons/2/27/Chin_Mee_Chin_Confectionery_%282025%29_-_img_01.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "EGGS", "pan": (0.5, 0.5)},
    {"img": "KOPIO", "pan": (0.5, 0.5)},
    {"img": "KASUMI", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "G_SET", **_LB, "title": "Ya Kun kaya toast, eggs and coffee"},   # s1 the set itself (16.0s)
    {"img": "EGGS", **_LB, "title": "Soft-boiled eggs, Singapore"},   # s7 steeped, not boiled (18.2s)
    {"img": "PLATE", **_LB, "title": "Kaya toast on a plate"},   # s14 why two: a documented custom, no documented origin (12.6s)
    {"img": "G_YAKUN16", **_LB, "title": "Kaya toast from Ya Kun, 2016"},   # s25 Loi Ah Koon arrives, 1926 (17.6s)
    {"img": "YAKUN25", **_LB, "title": "A Ya Kun breakfast set, 2025"},   # s27 Ya Kun international (6.6s)
    {"img": "KASUMI", **_LB, "title": "Kasumi Dining, Kasumigaseki Building, Tokyo"},   # s28 the Kasumigaseki Building footnote (14.8s)
    {"img": "DIP", **_LB, "title": "Kaya toast dipped in soft-boiled egg"},   # s38 1968: no more than three eggs a week (16.0s)
    {"img": "G_SET", **_LB, "title": "Ya Kun kaya toast, eggs and coffee"},   # s44 two eggs bust the whole day's budget (15.6s)
    {"img": "HERO", **_LB, "title": "Kaya toast with coffee"},   # s55 2020: no association in 1.72 million people (15.6s)
    {"img": "YAKUN25", **_LB, "title": "A Ya Kun breakfast set, 2025"},   # s64 Singaporeans went on ordering the two eggs (11.0s)
    {"img": "KOPIO", **_LB, "title": "A cup of kopi-o"},   # s80 the kopi-o: graded, not banned (9.0s)
    {"img": "DIP", **_LB, "title": "Kaya toast dipped in soft-boiled egg"},   # s85-s86 only a shortage ever removed them (8.9s)
    {"img": "EGGS", **_LB, "title": "Soft-boiled eggs, Singapore"},   # s93-s94 nobody ever decided they should (8.6s)
]
SCHEDULE = [
    (0.000, 0), (16.000, 1), (34.200, 2), (46.750, 3), (64.400, 4), (71.000, 5),
    (85.750, 6), (101.750, 7), (117.375, 8), (132.950, 9), (143.975, 10), (152.950, 11),
    (161.825, 12)
]
TOTAL_DURATION = 170.40
TIMING_JSON = "audio/the-kopitiams-two-eggs-the-breakfast-that-outlived-a-health-scare-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
