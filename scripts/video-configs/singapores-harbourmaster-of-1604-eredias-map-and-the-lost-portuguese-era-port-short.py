"""Short config for the Erédia post.

The post's opening, sentences 0-6 (0-73.0s, over the 60s TikTok line): the
1604 sketch, the word Xabandaria, the port two centuries after Singapura,
and the manuscript it comes from. The map, the self-portrait, the Annals
page and the Malacca plan are small or wide, so they are letterboxed; the
Kallang Basin photo is cropped to fill the vertical frame.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_U}/f/f6/Map_of_Singapura_by_Godinho_de_Er%C3%A9dia_1604.jpg",
    "PORTRAIT": f"{_C}/7/77/Manuel_Godinho_de_Er%C3%A9dia_self_portrait.jpg/1280px-Manuel_Godinho_de_Er%C3%A9dia_self_portrait.jpg",
    "KALLANG": f"{_C}/5/5f/Kallang_Basin_from_Centennial_Tower%2C_2024046%2C_RSKY.jpg/1280px-Kallang_Basin_from_Centennial_Tower%2C_2024046%2C_RSKY.jpg",
    "SULA": f"{_U}/2/2d/Excerpt_from_the_Sulalatus_Salatin_manuscript%2C_copied_in_the_year_1808%2C_chapter_on_the_Death_of_Hang_Tuah.jpg",
    "MALACA": f"{_U}/2/28/Malaca_%28manuel_godinho_de_eredia_1604%29.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "SULA": "Osman bin Kuri bin Amat Utat, the copyist, CC0, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_LB},                                       # s0  title: the 1604 sketch
    {"img": "PORTRAIT", **_LB},                                   # s1  Erédia
    {"img": "KALLANG", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)}, # s2  the shore; Xabandaria
    {"img": "SULA", **_LB},                                       # s3  two centuries after Singapura
    {"img": "HERO", **_LB},                                       # s4  the map's title
    {"img": "MALACA", **_LB},                                     # s5  the Description of Malacca
    {"img": "PORTRAIT", **_LB},                                   # s6  the manuscript in Brussels
]
SCHEDULE = [(0.0, 0), (6.9, 1), (17.125, 2), (32.6, 3), (44.0, 4), (53.725, 5), (62.825, 6)]
TOTAL_DURATION = 73.0
TIMING_JSON = "audio/singapores-harbourmaster-of-1604-eredias-map-and-the-lost-portuguese-era-port.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
