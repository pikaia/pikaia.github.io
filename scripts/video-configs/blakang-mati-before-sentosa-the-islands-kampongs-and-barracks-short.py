"""Short config for the Blakang Mati post.

The post's opening, sentences 0-6 (0-67.5s, over the 60s TikTok line): the island
before Sentosa, its kampongs, the renaming, and the old name on Erédia's 1604 map.
The 1880 watercolour fills the vertical frame as a cover; the photos and the Erédia
map are letterboxed; the three-stage map's "today" view is letterboxed and frozen.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Singapore%3B_a_view_across_part_of_Blakang_Mati_Island._Waterc_Wellcome_V0037528.jpg/1280px-Singapore%3B_a_view_across_part_of_Blakang_Mati_Island._Waterc_Wellcome_V0037528.jpg",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Panorama_of_Sentosa%2C_Singapore_-_March_2018.jpg/1280px-Panorama_of_Sentosa%2C_Singapore_-_March_2018.jpg",
    "KEPPEL": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Singapore_-_Keppel_Harb_1952.jpg/1280px-Singapore_-_Keppel_Harb_1952.jpg",
    "MAP2": "/assets/images/blakang-mati-map-2.png",
    "EREDIA": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Map_of_Singapura_by_Godinho_de_Er%C3%A9dia_1604.jpg",
    "PORT1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/KITLV_-_377455_-_Port_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377455_-_Port_at_Singapore_-_circa_1890.tif.jpg",
}

CREDITS = {
    "MAP2": "Map by Lesser Known Singapore; map data © OpenStreetMap contributors",
    "PANO": "Banej, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},# s0  title
    {"img": "PANO", **_LB},                                 # s1  the island we now call Sentosa
    {"img": "KEPPEL", **_LB},                               # s2  1,000 people in two kampongs by 1959
    {"img": "MAP2", **_GFX},                                # s3  renamed Sentosa; what is left today
    {"img": "EREDIA", **_LB},                               # s4  the name is old; Eredia's 1604 map (his work, no portrait)
    {"img": "PORT1890", **_LB},                             # s6  behind death, dead back
]
SCHEDULE = [(0, 0), (5.15, 1), (19.075, 2), (28.55, 3), (39.4, 4), (58.9, 5)]
TOTAL_DURATION = 67.5
TIMING_JSON = "audio/blakang-mati-before-sentosa-the-islands-kampongs-and-barracks.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
