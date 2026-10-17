"""Short config for the Thomas Dunman post.

The post's opening, sentences 0-6 (0-65.475s, over the 60s TikTok line): the
road and school named after him, the 1843 handover of the police to a
merchant's clerk, his 28 years in charge, Farquhar's tiny first force and the
merchants' Night Watch Fund. Dunman and Farquhar get their own portraits. The
police court and Grosse's 1866 view fill the frame as covers; Dunman Road,
the portraits and the timeline are letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/8/8c/KITLV_-_103754_-_Lambert_%26_Co._-_Court_of_the_police_at_South_Bridge_Road%2C_Singapore_-_circa_1885.tif/lossy-page1-1280px-KITLV_-_103754_-_Lambert_%26_Co._-_Court_of_the_police_at_South_Bridge_Road%2C_Singapore_-_circa_1885.tif.jpg",
    "DROAD": f"{_C}/6/6d/Dunman_Road_-_Singapura_%2814_Julai_%2724%29.jpg/1280px-Dunman_Road_-_Singapura_%2814_Julai_%2724%29.jpg",
    "DUNMAN": f"{_U}/2/2d/Thomas_Dunman.jpg",
    "TIMELINE": f"{_A}/dunman-timeline-chart.png",
    "FARQ": f"{_U}/f/f9/Portrait_of_William_Farquhar_%28c._1830%29.jpg",
    "GROSSE": f"{_C}/0/07/Singapore_January_20_1866_Frederick_Grosse.jpg/1280px-Singapore_January_20_1866_Frederick_Grosse.jpg",
}

CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "FARQ": "Unknown artist, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},    # s0  title
    {"img": "DROAD", **_LB},                                        # s1  Dunman Road, Dunman High School
    {"img": "DUNMAN", **_LB},                                       # s2  1843: the force handed to a clerk
    {"img": "TIMELINE", **_GFX},                                    # s3  28 years, retired 1871
    {"img": "FARQ", **_LB},                                         # s4  a tiny first force; Farquhar (s5)
    {"img": "GROSSE", **_v([1.0, 1.03, 1.06], [(0.5, 0.5)] * 3)},  # s6  the Night Watch Fund, 1821
]
SCHEDULE = [(0.0, 0), (4.775, 1), (13.5, 2), (30.575, 3), (40.275, 4), (57.175, 5)]
TOTAL_DURATION = 65.475
TIMING_JSON = "audio/thomas-dunman-the-merchants-clerk-who-built-singapores-police.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
