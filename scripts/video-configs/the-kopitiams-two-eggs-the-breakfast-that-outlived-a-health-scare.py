"""Video config for the kopitiam two-eggs post.

The pool is all thirteen pictures from the post and its gallery:
the kaya toast set and the soft-boiled eggs eaten the local way,
Chin Mee Chin Confectionery in Katong (today and in 2025), kaya
toast on a plate and dipped into the egg, a cup of kopi-o, the
Ya Kun sets of 2016 and January 2025, cream crackers with kaya,
kopitiam toast, and the Kasumi Dining entrance of Tokyo's
Kasumigaseki Building. Thirteen pictures for just under eighteen
minutes: images recur at new story beats with varied pans and
alternating zoom direction, never twice in a row.

Named-person rule: the pool holds no portraits at all. Sentences
naming Loi Ah Koon, Woon Tek Seng, Khir Johari or Ancel Keys
show the food, the shops and the sets of their stories, never
another named person's likeness.

Every slide carries its discreet photo title (standing rule,
Chris, 2026-11-11): the short form of its image's post/gallery
caption, drawn small in the top corner on a soft dark backing
for the slide's whole run.

66 slides, 1071.03s. Narration: Kokoro with the OpenVoice clone.
Pronunciations ear-verified by Chris 2026-11-18 (kopitiam as
three even beats; Kasumigaseki as two even triplets).
AVATAR: first and last 30s, cartoon with motion.
"""

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

# The channel's 2x2 thumbnail grid, in story order: the set,
# the saucer, the cup, and the Tokyo footnote.
THUMBNAIL = [
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "EGGS", "pan": (0.5, 0.5)},
    {"img": "KOPIO", "pan": (0.5, 0.5)},
    {"img": "KASUMI", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  s0 title (4.8s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 1  s1 the set, barely changed in a century (16.0s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 2  s2 heritage-listed 2019 (11.7s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 3  s3 fifty years of guidance against the eggs (15.0s)
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 4  s4-5 the guidance swung; the breakfast never moved (6.4s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 5  s6-7 steeped, not boiled (21.2s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  s8-9 cracked into a saucer; soy and pepper (14.2s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 7  s10-12 why two? nobody wrote it down (14.6s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  s13-14 folk reasons; a documented custom (20.7s)
    {"img": "G_TOAST", **{"type": "cover", "title": "Kopitiam toast", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 9  s15 the toast: charcoal-grilled, kaya and butter (16.9s)
    {"img": "KOPIO", **{"type": "cover", "title": "A cup of kopi-o", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 10  s16 the kopi vocabulary (16.6s)
    {"img": "CMC", **{"type": "cover", "title": "Chin Mee Chin Confectionery, Katong", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  s17 the word kopitiam; a Hainanese enterprise (8.1s)
    {"img": "G_CMC25", **{"type": "cover", "title": "Chin Mee Chin Confectionery, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  s18 Hainanese from 1821, arriving late (11.2s)
    {"img": "CMC", **{"type": "cover", "title": "Chin Mee Chin Confectionery, Katong", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 13  s19 cooks and kitchen hands in other men's houses (15.1s)
    {"img": "G_CMC25", **{"type": "cover", "title": "Chin Mee Chin Confectionery, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 14  s20 the coffee shop became their niche (12.1s)
    {"img": "CMC", **{"type": "cover", "title": "Chin Mee Chin Confectionery, Katong", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 15  s21-22 the pioneer at 67 Killiney Road, 1919 (16.9s)
    {"img": "G_CMC25", **{"type": "cover", "title": "Chin Mee Chin Confectionery, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 16  s23 1992: Woon Tek Seng, Killiney Kopitiam (21.7s)
    {"img": "G_YAKUN16", **{"type": "cover", "title": "Kaya toast from Ya Kun, 2016", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 17  s24 the other name: one stall to a chain (5.4s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 18  s25-26 Loi Ah Koon, 1926; his wife's kaya (25.0s)
    {"img": "YAKUN25", **{"type": "cover", "title": "A Ya Kun breakfast set, 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 19  s27 Ya Kun international: Jakarta to Tokyo (6.6s)
    {"img": "KASUMI", **{"type": "cover", "title": "Kasumi Dining, Kasumigaseki Building, Tokyo", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  s28 the Kasumigaseki Building footnote (14.8s)
    {"img": "G_YAKUN16", **{"type": "cover", "title": "Kaya toast from Ya Kun, 2016", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 21  s29 Loi could not have imagined it (7.7s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 22  s30-31 kaya the egg jam; two styles (21.8s)
    {"img": "G_CRACK", **{"type": "cover", "title": "Cream crackers with kaya and butter", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 23  s32-33 two birthplaces: the Portuguese account (17.1s)
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  s34 the revisionist account: serikaya first (21.7s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 25  s35 evidence on both sides (6.0s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 26  s36-37 the case against the egg, built in America (16.9s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 27  s38-39 1968: three eggs a week, like medicine (22.1s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 28  s40 1977 Senate goals; Time's cover; 1995 convergence (24.6s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 29  s41-42 weigh the saucer: the numbers (24.9s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 30  s43-44 two eggs bust the day's budget (17.7s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 31  s45 over the limit for fifty years (9.3s)
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  s46 1999: the science begins to move (20.3s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 33  s47-48 2002 the egg limit dropped; 2013 the cap (24.2s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 34  s49 February 2015: not a nutrient of concern (20.1s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 35  s50-52 too simple a story; the caution stayed; not ended (24.5s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 36  s53 March 2019: the JAMA swing back (one long sentence) (34.2s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 37  s54 December 2019: the Science Advisory settles (18.4s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 38  s55 2020: the BMJ's 1.72 million (15.6s)
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 39  s56 associations, not proofs (6.4s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  s57-59 the fair summary; the saucer did not move (19.0s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 41  s60 Singapore did not follow the swing (5.5s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 42  s61 HealthHub keeps the old numbers (26.9s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 43  s62 My Healthy Plate; the Heart Foundation table (14.7s)
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  s63 revision since 2021 unconfirmed (15.9s)
    {"img": "YAKUN25", **{"type": "cover", "title": "A Ya Kun breakfast set, 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 45  s64 Singaporeans went on ordering the two eggs (11.0s)
    {"img": "KOPIO", **{"type": "cover", "title": "A cup of kopi-o", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 46  s65-66 and the kopi-o? not ordinary coffee (11.9s)
    {"img": "G_TOAST", **{"type": "cover", "title": "Kopitiam toast", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 47  s67 the Nanyang roast: margarine, 180 degrees (21.2s)
    {"img": "KOPIO", **{"type": "cover", "title": "A cup of kopi-o", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 48  s68-69 the sock; beans pre-sweetened by the roast (14.5s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 49  s70-71 1991: coffee in Group 2B (19.8s)
    {"img": "KOPIO", **{"type": "cover", "title": "A cup of kopi-o", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 50  s72 2016: moved to Group 3 (18.9s)
    {"img": "G_TOAST", **{"type": "cover", "title": "Kopitiam toast", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 51  s73-74 absence of evidence; the heat, not the drink (19.9s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 52  s75 2017: more benefit than harm (24.8s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 53  s76 the live issue is the sugar (5.2s)
    {"img": "KOPIO", **{"type": "cover", "title": "A cup of kopi-o", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 54  s77 the sugar figures, with their health warning (23.4s)
    {"img": "YAKUN25", **{"type": "cover", "title": "A Ya Kun breakfast set, 2025", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 55  s78 Nutri-Grade: A kosong to D ga dai (23.1s)
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 56  s79-80 kosong by default; graded, not banned (15.6s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 57  s81-82 2,259 million eggs a year (24.1s)
    {"img": "PLATE", **{"type": "cover", "title": "Kaya toast on a plate", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 58  s83 2004: the bird-flu dependence shows (12.7s)
    {"img": "CMC", **{"type": "cover", "title": "Chin Mee Chin Confectionery, Katong", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 59  s84 Killiney's 4,000 eggs a day, halved (18.5s)
    {"img": "DIP", **{"type": "cover", "title": "Kaya toast dipped in soft-boiled egg", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 60  s85-86 not a guideline - a shortage (8.9s)
    {"img": "G_SET", **{"type": "cover", "title": "Ya Kun kaya toast, eggs and coffee", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 61  s87 the set endures, graded but intact (10.9s)
    {"img": "YAKUN25", **{"type": "cover", "title": "A Ya Kun breakfast set, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 62  s88 heritage-listed, capped, listed, de-listed, graded (16.1s)
    {"img": "HERO", **{"type": "cover", "title": "Kaya toast with coffee", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 63  s89 revised by nobody, one morning at a time (6.2s)
    {"img": "G_CMC25", **{"type": "cover", "title": "Chin Mee Chin Confectionery, 2025", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 64  s90-91 the bigger story; advice on weak evidence (20.9s)
    {"img": "EGGS", **{"type": "cover", "title": "Soft-boiled eggs, Singapore", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 65  s92-94 the custom outlasted it; nobody decided (13.2s)
]

SCHEDULE = [
    (0.000, 0), (4.775, 1), (20.775, 2), (32.475, 3), (47.450, 4), (53.825, 5),
    (75.050, 6), (89.300, 7), (103.900, 8), (124.575, 9), (141.500, 10), (158.125, 11),
    (166.225, 12), (177.375, 13), (192.425, 14), (204.550, 15), (221.475, 16), (243.175, 17),
    (248.550, 18), (273.550, 19), (280.150, 20), (294.900, 21), (302.600, 22), (324.400, 23),
    (341.500, 24), (363.175, 25), (369.200, 26), (386.075, 27), (408.200, 28), (432.800, 29),
    (457.750, 30), (475.425, 31), (484.700, 32), (505.000, 33), (529.225, 34), (549.325, 35),
    (573.800, 36), (608.025, 37), (626.450, 38), (642.025, 39), (648.450, 40), (667.425, 41),
    (672.950, 42), (699.900, 43), (714.575, 44), (730.450, 45), (741.475, 46), (753.350, 47),
    (774.525, 48), (789.050, 49), (808.800, 50), (827.725, 51), (847.575, 52), (872.350, 53),
    (877.525, 54), (900.900, 55), (924.000, 56), (939.550, 57), (963.675, 58), (976.375, 59),
    (994.875, 60), (1003.750, 61), (1014.650, 62), (1030.750, 63), (1036.950, 64), (1057.825, 65)
]
TOTAL_DURATION = 1071.03
TIMING_JSON = "audio/the-kopitiams-two-eggs-the-breakfast-that-outlived-a-health-scare.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
