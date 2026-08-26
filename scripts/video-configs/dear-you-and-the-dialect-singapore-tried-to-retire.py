"""Video config for the Dear You / Speak Mandarin Campaign post's Watch
widget and main video.

15 slides across all 7 real images used in the post + gallery (temple
hero, film logo, KITLV/Commons dialect-culture photos). No chart slide -
the post's inline lang-chart is a 3-series comparison (English/Mandarin/
Dialect), but compose_chart_frame() in watch_video_lib.py only supports
a single (x, y) series (see HDB's chart slide) - extending it for
multi-series wasn't in scope here, so this stretch uses photo variety
instead. TEMPLE (1600x1200, 1.33) and LAICHUNYUEN/GREATWORLD/OLDTEMPLE
are landscape enough for cover; VENDOR (0.70), THEATRE (0.76), and LOGO
(3.26, a wide banner) all diverge enough from 16:9 to need letterbox.
"""

IMAGES = {
    "TEMPLE": "https://upload.wikimedia.org/wikipedia/commons/7/71/Yueh_Hai_Ching_Temple_8%2C_Mar_06.JPG",
    "VENDOR": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif/lossy-page1-960px-KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif.jpg",
    "LOGO": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Dear_You_film_logo.png",
    "LAICHUNYUEN": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Former_Lai_Chun_Yuen%2C_Singapore.jpg",
    "THEATRE": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/KITLV_-_106226_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_theater_in_the_Straits_Settlements_-_circa_1900.tif/lossy-page1-960px-KITLV_-_106226_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Chinese_theater_in_the_Straits_Settlements_-_circa_1900.tif.jpg",
    "GREATWORLD": "https://upload.wikimedia.org/wikipedia/commons/7/70/Great_World_Amusement_Park.jpg",
    "OLDTEMPLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/KITLV_-_29181_-_Chinese_temple_in_Singapore_-_1895.tif/lossy-page1-960px-KITLV_-_29181_-_Chinese_temple_in_Singapore_-_1895.tif.jpg",
}

SLIDES = [
    {"img": "TEMPLE", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-in-out"},
    {"img": "VENDOR", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "TEMPLE", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.45, 0.40), (0.50, 0.50), (0.55, 0.60)], "ease": "ease-out"},
    {"img": "LOGO", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "LAICHUNYUEN", "type": "cover", "zoom": [1, 1.06, 1.1], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-in"},
    {"img": "TEMPLE", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)], "ease": "ease-in-out"},
    {"img": "THEATRE", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "GREATWORLD", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)], "ease": "ease-in"},
    {"img": "OLDTEMPLE", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)], "ease": "ease-out"},
    {"img": "LOGO", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "GREATWORLD", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)], "ease": "ease-in"},
    {"img": "THEATRE", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "VENDOR", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OLDTEMPLE", "type": "cover", "zoom": [1, 1.08, 1.14], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)], "ease": "ease-in"},
    {"img": "TEMPLE", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.60, 0.50), (0.50, 0.50), (0.40, 0.50)], "ease": "ease-in-out"},
]

# Real values from audio/dear-you-and-the-dialect-singapore-tried-to-retire.timing.json.
SCHEDULE = [
    (0.0, 0), (5.83, 1), (19.90, 2), (32.88, 3), (47.00, 4),
    (51.48, 5), (63.48, 6), (80.58, 7), (85.90, 8), (100.53, 9),
    (125.10, 10), (140.97, 11), (162.20, 12), (182.53, 13), (191.15, 14),
]
TOTAL_DURATION = 215.475
TIMING_JSON = "audio/dear-you-and-the-dialect-singapore-tried-to-retire.timing.json"
