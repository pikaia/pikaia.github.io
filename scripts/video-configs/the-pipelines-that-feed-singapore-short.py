"""Short config for the gas pipelines post.

The post's opening, sentences 0-7 (0-60.65s, over the 60s line): the
October 2026 cut that came to under 2% of daily gas, the three pipes
under the sea, and the PUB most Singaporeans remember. No sentence names
a person. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "SENOKO07": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Senoko_Power_Station.JPG/1280px-Senoko_Power_Station.JPG",
    "SUNSET": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg/1280px-Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg",
    "JI2011": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Jurong_Island%2C_Singapore_-_20110227-01.jpg/1280px-Jurong_Island%2C_Singapore_-_20110227-01.jpg",
    "MAP": "/assets/images/gas-pipelines-map.png",
    "PASIR18": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pasir_Panjang_Power_Station.jpg/1280px-Pasir_Panjang_Power_Station.jpg",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Panorama_view_of_Singapore_Senoko_power_station_from_in_front_of_Zon_Hotel_in_Malaysia_-_panoramio.jpg/1280px-Panorama_view_of_Singapore_Senoko_power_station_from_in_front_of_Zon_Hotel_in_Malaysia_-_panoramio.jpg",  # thumbnail only
    "JNIGHT": "https://upload.wikimedia.org/wikipedia/commons/7/72/Aerial_view_of_Jurong_Island_from_Hill_top.jpg",  # thumbnail only
    "JHILL": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg/1280px-Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PASIR18", "pan": (0.5, 0.5)},
    {"img": "PANO", "pan": (0.5, 0.5)},
    {"img": "JNIGHT", "pan": (0.5, 0.5)},
    {"img": "JHILL", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "SENOKO07", **_LB},   # s0
    {"img": "SUNSET", **_LB},     # s1
    {"img": "JI2011", **_LB},     # s3
    {"img": "MAP", **_LB},        # s4
    {"img": "PASIR18", **_LB},    # s5
]
SCHEDULE = [(0.0, 0), (2.975, 1), (19.925, 2), (30.45, 3), (42.4, 4)]
TOTAL_DURATION = 60.65
TIMING_JSON = "audio/the-pipelines-that-feed-singapore.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
