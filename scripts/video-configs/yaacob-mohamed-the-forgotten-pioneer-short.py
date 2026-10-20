"""Short config for the Ya'acob Mohamed post.

The post's opening, sentences 0-7 (0-69.025s, over the 60s TikTok line): Lee
Kuan Yew's 1980 tribute, the 1958 move from UMNO to the PAP, the Southern
Islands, and his birth in Kelantan and childhood in Johor. No portrait of
Ya'acob exists, so the sentences show places: the Blakang Mati ferry and the
Old Parliament House fill the frame as covers; the timeline, the Pulau Brani
village and Johor Bahru are letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "FERRY": f"{_C}/f/f8/Blakang_Mati_Ferry_1951.jpg/1280px-Blakang_Mati_Ferry_1951.jpg",
    "OPH": f"{_C}/7/7c/Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG/1280px-Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG",
    "TIMELINE": f"{_A}/yaacob-timeline-chart.png",
    "BRANI": f"{_C}/5/50/KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105809_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malay_village_on_the_island_of_Pulau_Brani_near_Singapore_-_circa_1900.tif.jpg",
    "JB": f"{_U}/0/04/Johor_Bahru_town_in_the_1920s.jpg",
}

CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "FERRY", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},  # s0  title
    {"img": "OPH", **_v([1.0, 1.03, 1.06], [(0.5, 0.5)] * 3)},    # s1  Lee Kuan Yew's tribute, 1980
    {"img": "TIMELINE", **_GFX},                                   # s2  UMNO to PAP, minister, envoy
    {"img": "BRANI", **_LB},                                       # s3  the Southern Islands
    {"img": "JB", **_LB},                                          # s4  born in Kelantan, raised in Johor (s5-7)
]
SCHEDULE = [(0.0, 0), (3.45, 1), (18.05, 2), (31.975, 3), (44.375, 4)]
TOTAL_DURATION = 69.475
TIMING_JSON = "audio/yaacob-mohamed-the-forgotten-pioneer.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
