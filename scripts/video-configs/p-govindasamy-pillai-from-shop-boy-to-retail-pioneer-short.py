"""Short config for the P. Govindasamy Pillai post.

The post's opening, sentences 0-5 (0-65.725s, over the 60s TikTok line): the
runaway landing at Tanjong Pagar in 1905, the provision shop he worked in and
later bought, the PGP stores, their closing in 1998, and his home village.
The hero gopuram fills the vertical frame; the c.1890 portrait suits it too;
the tram, Little India Arcade, the postcard and the Mayiladuthurai temple are
letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/0/0e/Templo_Sri_Srinivasa_Perumal%2C_Singapur%2C_2023-08-17%2C_DD_04.jpg/1280px-Templo_Sri_Srinivasa_Perumal%2C_Singapur%2C_2023-08-17%2C_DD_04.jpg",
    "MAN": f"{_C}/f/f4/KITLV_-_103785_-_Indian_man%2C_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103785_-_Indian_man%2C_Singapore_-_circa_1890.tif.jpg",
    "TRAM": f"{_U}/6/6e/Electric_Tram_Singapore_about_1910.png",
    "ARCADE": f"{_C}/8/81/Little_India_Arcade%2C_2023_%2801%29.jpg/1280px-Little_India_Arcade%2C_2023_%2801%29.jpg",
    "GREET": f"{_C}/f/f5/KITLV_-_1404957_-_Greetings_from_Singapore_-_1895-1908.tif/lossy-page1-1280px-KITLV_-_1404957_-_Greetings_from_Singapore_-_1895-1908.tif.jpg",
    "MAYU": f"{_U}/2/24/Mayuranathar8.jpg",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},                       # s0  title: the gopuram
    {"img": "MAN", **_v([1.0, 1.04, 1.08], [(0.5, 0.4), (0.5, 0.42), (0.5, 0.44)])},  # s1  the runaway lands, 1905
    {"img": "TRAM", **_LB},                                                           # s2  a provision shop on Serangoon Road
    {"img": "ARCADE", **_LB},                                                         # s3  a chain of stores
    {"img": "GREET", **_LB},                                                          # s4  closed in 1998
    {"img": "MAYU", **_LB},                                                           # s5  Koorainadu, near Mayavaram
]
SCHEDULE = [(0.0, 0), (5.875, 1), (16.875, 2), (28.0, 3), (40.95, 4), (52.325, 5)]
TOTAL_DURATION = 65.725
TIMING_JSON = "audio/p-govindasamy-pillai-from-shop-boy-to-retail-pioneer.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
