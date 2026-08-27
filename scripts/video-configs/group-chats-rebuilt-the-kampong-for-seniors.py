"""Video config for the "How Group Chats Rebuilt the Kampong for
Singapore's Seniors" post's Watch widget and main video.

6 real images: BISHAN (2020s, the present-day Digital Ambassador/
community-club context, inline in the post) and 5 gallery images
tracing the "kampong spirit" metaphor's literal history - two real
kampongs (Kampong Bugis ~1900, Kampong Baru ~1890), a hand-tinted
postcard of everyday kampong path life, a kampong on the eve of
redevelopment (Braddell Hill, 1964), and the public housing that
replaced it (1973-74). 14 slides across those 6 images, opening and
closing on the kampong imagery to bookend the metaphor, with BISHAN
carrying the present-day/programme-mechanics stretch in the middle.
All 6 images are landscape enough (1.28-1.55 aspect) for "cover" - no
letterbox needed.
"""

IMAGES = {
    "BISHAN": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Bishan_Community_Club.JPG",
    "KAMPONGBUGIS": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/KITLV_-_105810_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Buggis%2C_the_Buginese_district_of_Singapore_-_circa_1900.tif/lossy-page1-960px-KITLV_-_105810_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Buggis%2C_the_Buginese_district_of_Singapore_-_circa_1900.tif.jpg",
    "KAMPONGBARU": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/KITLV_-_105811_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Baru_at_Singapore_-_circa_1890.tif/lossy-page1-960px-KITLV_-_105811_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Baru_at_Singapore_-_circa_1890.tif.jpg",
    "MALAYDWELLING": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Malay_Dwelling_House_Singapore.%2C_KITLV_1404990.tiff/lossy-page1-960px-Malay_Dwelling_House_Singapore.%2C_KITLV_1404990.tiff.jpg",
    "BRADDELLHILL": "https://upload.wikimedia.org/wikipedia/commons/8/81/Kampong_in_Braddell_Hill_Singapore_about_1964.jpg",
    "PUBLICHOUSING": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Singapore-Public_Housing-1973-74-WUS08215.jpg/960px-Singapore-Public_Housing-1973-74-WUS08215.jpg",
}

SLIDES = [
    {"img": "KAMPONGBUGIS", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-in-out"},
    {"img": "BISHAN", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)], "ease": "ease-out"},
    {"img": "BISHAN", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)], "ease": "linear"},
    {"img": "BISHAN", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.60, 0.40), (0.50, 0.50), (0.40, 0.60)], "ease": "ease-in"},
    {"img": "KAMPONGBARU", "type": "cover", "zoom": [1.15, 1.07, 1], "pan": [(0.45, 0.55), (0.50, 0.50), (0.55, 0.45)], "ease": "ease-in-out"},
    {"img": "BISHAN", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.50, 0.40), (0.50, 0.50), (0.50, 0.60)], "ease": "ease-out"},
    {"img": "BISHAN", "type": "cover", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "BRADDELLHILL", "type": "cover", "zoom": [1.1, 1.05, 1], "pan": [(0.40, 0.45), (0.50, 0.50), (0.60, 0.55)], "ease": "ease-in"},
    {"img": "PUBLICHOUSING", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.55, 0.50), (0.50, 0.50), (0.45, 0.50)], "ease": "ease-in-out"},
    {"img": "BISHAN", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)], "ease": "ease-out"},
    {"img": "MALAYDWELLING", "type": "cover", "zoom": [1.12, 1.06, 1], "pan": [(0.45, 0.40), (0.50, 0.50), (0.55, 0.60)], "ease": "linear"},
    {"img": "BISHAN", "type": "cover", "zoom": [1, 1.09, 1.18], "pan": [(0.60, 0.55), (0.50, 0.50), (0.40, 0.45)], "ease": "ease-in"},
    {"img": "KAMPONGBUGIS", "type": "cover", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "PUBLICHOUSING", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-out"},
]

# Real values from audio/group-chats-rebuilt-the-kampong-for-seniors.timing.json.
SCHEDULE = [
    (0.0, 0), (4.42, 1), (25.23, 2), (38.88, 3), (49.33, 4),
    (74.42, 5), (83.47, 6), (97.22, 7), (111.92, 8), (131.6, 9),
    (149.53, 10), (165.15, 11), (175.68, 12), (184.03, 13),
]
TOTAL_DURATION = 200.8
TIMING_JSON = "audio/group-chats-rebuilt-the-kampong-for-seniors.timing.json"
