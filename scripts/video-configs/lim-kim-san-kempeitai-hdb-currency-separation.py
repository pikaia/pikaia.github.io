"""Video config for the Lim Kim San post's Watch widget / main video.

Reconstructed from the post's own already-published (pre-canonical-
pipeline) live widget script - this post's real video predates
scripts/video-configs/, so this file did not exist until now."""

IMAGES = {
    "LIM": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Lim_Kim_San_in_the_1940s.jpg",
    "RAFFLES": "https://upload.wikimedia.org/wikipedia/commons/2/28/Raffles_College_graduates_1934.webp",
    "WEDDING": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Lim_Kim_San%2C_1940.jpg",
    "SHONAN": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Street_in_Shonan.JPG",
    "MEMORIAL": "https://upload.wikimedia.org/wikipedia/commons/2/27/Civilian_War_Memorial%2C_Singapore-3276.jpg",
    "BLOCK45": "https://upload.wikimedia.org/wikipedia/commons/d/dd/Block_45_Stirling_Road%2C_Singapore.jpg",
    "FIRE": "https://upload.wikimedia.org/wikipedia/commons/3/39/ST27May1961.jpg",
    "QUEENSTOWN": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Queenstown_hdb.jpg",
    "GOH": "https://upload.wikimedia.org/wikipedia/commons/4/49/Goh_Keng_Swee%2C_1967_%283x4_crop%29.jpg",
    "LIMC": "https://upload.wikimedia.org/wikipedia/commons/d/d9/Lim_Kim_San%2C_1940_%28cropped%29.jpg",
    "NOTE": "https://upload.wikimedia.org/wikipedia/commons/2/22/Banknote_%28AM_786991-1%29.jpg",
    "ST1959": "https://upload.wikimedia.org/wikipedia/commons/9/95/ST31May1959.jpg",
}

CREDITS = {
    "LIMC": "Lim Kim San, public domain, via Wikimedia Commons",
    "NOTE": "Auckland Museum, CC BY 4.0, via Wikimedia Commons",
    "ST1959": "The Straits Times, public domain, via Wikimedia Commons",
}

SLIDES = [
    {"img": "LIM", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s0
    {"img": "BLOCK45", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in-out"},  # s2
    {"img": "LIMC", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s4
    {"img": "RAFFLES", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.4, 0.5), (0.5, 0.45), (0.6, 0.4)], "ease": "ease-out"},  # s5
    {"img": "GOH", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s6
    {"img": "WEDDING", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s7
    {"img": "SHONAN", "type": "cover", "zoom": [1.0, 1.12, 1.2], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "linear"},  # s8
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s10
    {"img": "LIMC", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s11
    {"img": "ST1959", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s13
    {"img": "BLOCK45", "type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.65, 0.5), (0.5, 0.5), (0.35, 0.5)], "ease": "ease-in-out"},  # s14
    {"img": "QUEENSTOWN", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in-out"},  # s15
    {"img": "FIRE", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s16
    {"img": "BLOCK45", "type": "cover", "zoom": [1.0, 1.08, 1.15], "pan": [(0.5, 0.5), (0.5, 0.45), (0.5, 0.4)], "ease": "ease-in-out"},  # s17
    {"img": "LIM", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s18
    {"img": "QUEENSTOWN", "type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.65, 0.5), (0.5, 0.5), (0.35, 0.5)], "ease": "ease-in-out"},  # s20
    {"img": "NOTE", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s21
    {"img": "NOTE", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in-out"},  # s22
    {"img": "LIMC", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s23
    {"img": "GOH", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s24
    {"img": "NOTE", "type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.65, 0.5), (0.5, 0.5), (0.35, 0.5)], "ease": "ease-in-out"},  # s25
    {"img": "QUEENSTOWN", "type": "cover", "zoom": [1.15, 1.06, 1.0], "pan": [(0.6, 0.6), (0.5, 0.5), (0.4, 0.4)], "ease": "ease-out"},  # s26
    {"img": "NOTE", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s27
    {"img": "LIM", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s28
    {"img": "BLOCK45", "type": "cover", "zoom": [1.1, 1.05, 1.0], "pan": [(0.65, 0.5), (0.5, 0.5), (0.35, 0.5)], "ease": "ease-in-out"},  # s29
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},  # s30
]

SCHEDULE = [(0.0, 0), (23.825, 1), (39.3, 2), (52.55, 3), (63.925, 4), (76.475, 5), (92.65, 6), (116.725, 7), (134.05, 8), (152.275, 9), (168.45, 10), (189.325, 11), (207.575, 12), (225.6, 13), (249.525, 14), (270.4, 15), (280.425, 16), (292.525, 17), (315.225, 18), (336.5, 19), (345.725, 20), (370.475, 21), (386.75, 22), (404.75, 23), (418.375, 24), (431.225, 25)]
TOTAL_DURATION = 453.325
TIMING_JSON = "audio/lim-kim-san-kempeitai-hdb-currency-separation.timing.json"
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
