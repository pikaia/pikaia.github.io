"""Video config for the Jurong post's full-length Watch video.

16 slides across all 9 images used in the post (hero signage, Goh Keng
Swee, Albert Winsemius, the 1945 surrender ceremony, 1963 roadstead,
Tengah village, the 1964 Straits Times foundation-stone spread, and two
1967 Jurong staff-housing photos). Winsemius (0.75 aspect) and the ST
scan (0.671 aspect) are both portrait-oriented and use letterbox; every
other image is landscape enough for cover.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/0/04/Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg",
    "GOH": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Goh_Keng_Swee_in_Australia%2C_1967.jpg",
    "WINSEMIUS": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Albert_Winsemius_%281971%29.jpg",
    "SURRENDER1945": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Signing_of_the_Japanese_Surrender_at_Singapore%2C_1945_CF720.jpg",
    "ROADSTEAD1963": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Singapore_roadstead_1963_01.jpg",
    "TENGAH1964": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Malay_village_near_Tengah_Singapore_October_1964.jpg",
    "STPAGE": "/assets/images/straits-times-19640220-jurong-shipyard-foundation-stone.jpg",
    "STAFFQUARTERS1967": "https://upload.wikimedia.org/wikipedia/commons/4/47/Jurong_Staff_Quarters.jpg",
    "WINDINGROAD1967": "https://upload.wikimedia.org/wikipedia/commons/0/06/1967_-_Winding_Road_to_Jurong_Staff_Quarters.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)]},
    {"img": "SURRENDER1945", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.35, 0.50), (0.50, 0.50), (0.65, 0.50)]},
    {"img": "ROADSTEAD1963", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.40), (0.50, 0.50), (0.50, 0.60)]},
    {"img": "WINSEMIUS", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "GOH", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)]},
    {"img": "TENGAH1964", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)]},
    {"img": "HERO", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)]},
    {"img": "STPAGE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "STAFFQUARTERS1967", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)]},
    {"img": "ROADSTEAD1963", "type": "cover", "zoom": [1.16, 1.06, 1], "pan": [(0.65, 0.55), (0.50, 0.50), (0.35, 0.45)]},
    {"img": "SURRENDER1945", "type": "cover", "zoom": [1.16, 1.06, 1], "pan": [(0.65, 0.45), (0.50, 0.50), (0.35, 0.55)]},
    {"img": "WINDINGROAD1967", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)]},
    {"img": "HERO", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)]},
    {"img": "STAFFQUARTERS1967", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)]},
    {"img": "WINSEMIUS", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "HERO", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)]},
]

SCHEDULE = [
    (0.0, 0), (23.7, 1), (48.65, 2), (70.125, 3), (86.225, 4),
    (113.325, 5), (123.775, 6), (138.4, 7), (173.75, 8), (190.375, 9),
    (213.7, 10), (247.575, 11), (257.375, 12), (270.275, 13), (293.625, 14),
    (303.775, 15),
]
TOTAL_DURATION = 322.625
TIMING_JSON = "audio/japans-quiet-hand-in-building-jurong.timing.json"
