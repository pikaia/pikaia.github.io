"""Short config for the Interned in India post.

The post's opening, sentences 0-5 (0-64.0s, over the 60s TikTok line): the
round-up of Singapore's Japanese residents on 8 December 1941, as the
Straits Times reported it that day, the shopkeepers and fishermen shipped to
a fort in Delhi, and Fukuda Kurahachi, who had come to Echigoya in 1916 and
was its manager by 1941. Fukuda gets only the 1955 page that carries his
photograph. Everything is letterboxed except the hero and the fort gate,
which fill the frame; the newspaper pages must not be cropped. No avatar.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/b/b5/Purana_Qila_ramparts%2C_Delhi.jpg/1280px-Purana_Qila_ramparts%2C_Delhi.jpg",
    "ST1941": f"{_A}/straits-times-1941-12-08-page-8.jpg",
    "LAMBERT": f"{_C}/e/e5/KITLV_-_103764_-_Lambert_%26_Co._-_Japanese_women_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103764_-_Lambert_%26_Co._-_Japanese_women_in_Singapore_-_circa_1890.tif.jpg",
    "GATE": f"{_C}/c/cf/Old_Fort%28purana_qila%29_Delhi.jpg/1280px-Old_Fort%28purana_qila%29_Delhi.jpg",
    "SS1955": f"{_A}/singapore-standard-1955-11-08-page-10.jpg",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},  # s0  title
    {"img": "ST1941", **_LB},                                     # s1  8 December 1941, the round-up
    {"img": "LAMBERT", **_LB},                                    # s2  shopkeepers, photographers, families
    {"img": "GATE", **_v([1.08, 1.04, 1.0], [(0.5, 0.5)] * 3)},  # s3  few ever allowed home again
    {"img": "SS1955", **_LB},                                     # s4  Fukuda at Echigoya; manager by 1941 (s5)
]
SCHEDULE = [(0.0, 0), (7.2, 1), (21.075, 2), (43.925, 3), (48.45, 4)]
TOTAL_DURATION = 64.0
TIMING_JSON = "audio/interned-in-india-singapores-japanese-civilians-1941-46.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
