"""Short config for the Nanyang volunteers post.

The post's opening, sentences 0-5 (0-51.075s) plus sentence 6 (to 62.6s, over
the 60s TikTok line): the Nanyang Siang Pau's send-off, the 3,200
volunteers, the third who died, the change in where home was, and the war
that began it. The 1939 page fills the vertical frame on its headline.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_U}/6/6c/%E6%BB%87%E7%BC%85%E5%85%AC%E8%B7%AF01.jpg",
    "NYSP18": f"{_A}/nanyang-siang-pau-1939-02-18-page-6.jpg",
    "HARBPAN": f"{_C}/0/0e/De_haven_van_Singapore%2C_KITLV_29185.tiff/lossy-page1-1920px-De_haven_van_Singapore%2C_KITLV_29185.tiff.jpg",
    "CRASH": f"{_U}/e/e6/%E6%BB%87%E7%BC%85%E5%85%AC%E8%B7%AF%E8%BF%90%E8%BE%93%E6%83%85%E5%86%B501.jpg",
    "TKKSUN": f"{_U}/0/03/Tan_Kah_Kee_and_Sun_Yat-sen.jpg",
}

CREDITS = {
    "HARBPAN": "The harbour of Singapore, KITLV 29185, unknown photographer, CC BY 4.0, via Wikimedia Commons",
}

_E = "ease-in-out"


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.05, 1.1], [(0.5, 0.5)] * 3)},                          # s0  title
    {"img": "NYSP18", **_v([1.2, 1.25, 1.3], [(1.0, 0.0), (1.0, 0.01), (1.0, 0.02)])},  # s1  the send-off
    {"img": "HARBPAN", **_v([1.0, 1.05, 1.1], [(0.45, 0.5)] * 3)},                      # s2  the first 80 of 3,200
    {"img": "CRASH", **_v([1.0, 1.05, 1.1], [(0.4, 0.5)] * 3)},                         # s3-5 a third died; home
    {"img": "TKKSUN", **_v([1.0, 1.03, 1.06], [(0.3, 0.4)] * 3)},                       # s6  the war; the Nanyang responds
]
SCHEDULE = [(0.0, 0), (5.525, 1), (17.8, 2), (37.0, 3), (51.075, 4)]
TOTAL_DURATION = 62.6
TIMING_JSON = "audio/the-nanyang-volunteer-drivers-of-the-burma-road-1939.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
