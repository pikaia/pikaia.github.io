"""Short config for the Learning Nippon-go post.

The post's opening, sentences 0-7 (0-65.7s, over the 60s TikTok line): the
first Nippon Lesson in the Syonan Times on 21 February 1942, six days after
the surrender, its everyday phrases, the novelist Ibuse Masuji as the paper's
publisher, and the three-and-a-half-year drive that followed. The poster, the
newspaper pages, Ibuse's portrait and the 1942 map are letterboxed so nothing
is cropped; the surrender photograph and the street scene fill the frame.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_U}/f/f2/Belajarlah_Pakailah_Bahasa_Nippon.jpg",
    "SURRENDER": f"{_C}/2/22/BritishSurrender.jpg/1280px-BritishSurrender.jpg",
    "FEB21": f"{_A}/syonan-shimbun-1942-02-21-page-4.jpg",
    "IBUSE": f"{_U}/b/b1/Masuji_Ibuse_01.jpg",
    "MAP": f"{_C}/4/4a/SyonanSingapore.jpg/1280px-SyonanSingapore.jpg",
    "STREET": f"{_U}/f/fc/Street_in_Shonan.JPG",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "SURRENDER": "Japanese official photographer, public domain, via Wikimedia Commons",
    "MAP": "Magyer Lohasa, CC BY-SA 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_LB},                                            # s0  title
    {"img": "SURRENDER", **_v([1.0, 1.04, 1.08], [(0.5, 0.4)] * 3)},  # s1  six days after the surrender
    {"img": "FEB21", **_LB},                                           # s2  the first Nippon Lesson
    {"img": "IBUSE", **_LB},                                           # s4  Ibuse Masuji, the publisher
    {"img": "MAP", **_LB},                                             # s6  Singapore and Malaya, 3.5 years
    {"img": "STREET", **_LB},                                          # s7  a lesson almost every day
]
SCHEDULE = [(0.0, 0), (7.8, 1), (18.65, 2), (30.65, 3), (43.625, 4), (60.75, 5)]
TOTAL_DURATION = 65.7
TIMING_JSON = "audio/learning-nippon-go-the-occupations-japanese-language-drive-1942-45.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
