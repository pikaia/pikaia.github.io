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
}

SLIDES = [
    {"img": "LIM", "type": "letterbox", "zoom": [1.0, 1.08, 1.15], "pan": [(0.5, 0.4), (0.55, 0.5), (0.6, 0.6)], "ease": "ease-in-out"},
    {"img": "RAFFLES", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.4, 0.5), (0.5, 0.45), (0.6, 0.4)], "ease": "ease-out"},
    {"img": "WEDDING", "type": "letterbox", "zoom": [1.0, 1.1, 1.2], "pan": [(0.5, 0.3), (0.5, 0.5), (0.5, 0.7)], "ease": "ease-in"},
    {"img": "SHONAN", "type": "cover", "zoom": [1.0, 1.12, 1.2], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "linear"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1.15, 1.06, 1.0], "pan": [(0.6, 0.3), (0.5, 0.5), (0.4, 0.7)], "ease": "ease-in-out"},
    {"img": "LIM", "type": "letterbox", "zoom": [1.0, 1.1, 1.16], "pan": [(0.45, 0.6), (0.5, 0.5), (0.55, 0.4)], "ease": "ease-out"},
    {"img": "BLOCK45", "type": "cover", "zoom": [1.0, 1.08, 1.15], "pan": [(0.35, 0.4), (0.5, 0.5), (0.65, 0.6)], "ease": "ease-in"},
    {"img": "BLOCK45", "type": "cover", "zoom": [1.15, 1.06, 1.0], "pan": [(0.65, 0.6), (0.5, 0.5), (0.35, 0.4)], "ease": "ease-in-out"},
    {"img": "FIRE", "type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.3), (0.5, 0.5), (0.5, 0.7)], "ease": "linear"},
    {"img": "QUEENSTOWN", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.4, 0.6), (0.5, 0.45), (0.6, 0.3)], "ease": "ease-out"},
    {"img": "BLOCK45", "type": "cover", "zoom": [1.0, 1.1, 1.17], "pan": [(0.5, 0.5), (0.55, 0.45), (0.6, 0.4)], "ease": "ease-in-out"},
    {"img": "LIM", "type": "letterbox", "zoom": [1.0, 1.09, 1.16], "pan": [(0.55, 0.45), (0.5, 0.5), (0.45, 0.55)], "ease": "ease-in"},
    {"img": "LIM", "type": "letterbox", "zoom": [1.14, 1.06, 1.0], "pan": [(0.4, 0.55), (0.5, 0.5), (0.6, 0.45)], "ease": "ease-out"},
    {"img": "GOH", "type": "letterbox", "zoom": [1.0, 1.1, 1.18], "pan": [(0.5, 0.35), (0.5, 0.5), (0.5, 0.65)], "ease": "ease-in-out"},
    {"img": "GOH", "type": "letterbox", "zoom": [1.16, 1.06, 1.0], "pan": [(0.6, 0.6), (0.5, 0.5), (0.4, 0.4)], "ease": "ease-in"},
    {"img": "GOH", "type": "letterbox", "zoom": [1.0, 1.08, 1.15], "pan": [(0.45, 0.4), (0.5, 0.5), (0.55, 0.6)], "ease": "ease-out"},
    {"img": "GOH", "type": "letterbox", "zoom": [1.0, 1.12, 1.2], "pan": [(0.5, 0.5), (0.55, 0.45), (0.6, 0.4)], "ease": "linear"},
    {"img": "LIM", "type": "letterbox", "zoom": [1.0, 1.1, 1.17], "pan": [(0.6, 0.4), (0.5, 0.5), (0.4, 0.6)], "ease": "ease-in-out"},
    {"img": "QUEENSTOWN", "type": "cover", "zoom": [1.15, 1.06, 1.0], "pan": [(0.35, 0.55), (0.5, 0.5), (0.65, 0.45)], "ease": "ease-out"},
    {"img": "LIM", "type": "letterbox", "zoom": [1.0, 1.09, 1.16], "pan": [(0.5, 0.6), (0.5, 0.5), (0.5, 0.4)], "ease": "ease-in"},
    {"img": "BLOCK45", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.45, 0.5), (0.5, 0.5), (0.55, 0.5)], "ease": "ease-out"},
    {"img": "MEMORIAL", "type": "letterbox", "zoom": [1.0, 1.12, 1.2], "pan": [(0.4, 0.65), (0.5, 0.5), (0.6, 0.35)], "ease": "ease-in-out"},
]

SCHEDULE = [(0.0, 0), (36.425, 1), (70.425, 2), (86.075, 3), (108.95, 4), (125.0, 5), (155.975, 6), (176.025, 7), (193.275, 8), (210.275, 9), (233.625, 10), (245.075, 11), (262.25, 12), (273.55, 13), (295.675, 14), (316.325, 15), (324.875, 16), (349.65, 17), (364.625, 18), (380.7, 19), (393.55, 20), (405.6, 21)]
TOTAL_DURATION = 426.625
TIMING_JSON = "audio/lim-kim-san-kempeitai-hdb-currency-separation-kokoro.timing.json"
