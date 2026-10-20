"""Short config for the Borneo-to-Singapore post.

The post's opening, sentences 0-8 (0-64.825s, over the 60s TikTok line): Elizabeth
Choy, Hugh Zehnder and Wee Kheng Chiang, all born in Borneo; a century and a half
of traffic; and James Brooke's 1839 voyage from Singapore to Sarawak. The 1896
steamer is letterboxed (it is too wide to crop to a vertical frame), and so are the
portraits, the newspaper page and the two Kuching views.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/4/44/SS_Rajah_Brooke_leaving_Kuching_for_Singapore_on_22_July_1896.jpg/1280px-SS_Rajah_Brooke_leaving_Kuching_for_Singapore_on_22_July_1896.jpg",
    "WEDDING": f"{_U}/0/03/Elizabeth_Choy%2C_1941.jpg",
    "ZEHNDER": f"{_U}/b/b7/H.R.S._Zehnder.png",
    "ST1935": "/assets/images/straits-times-1935-10-01-page-12.jpg",
    "KUCHPANO": f"{_U}/4/42/Kuching_Waterfront_Panorama.jpg",
    "KUCH1844": f"{_C}/f/fa/Kuching_1844.jpg/1280px-Kuching_1844.jpg",
    "BROOKE": f"{_U}/7/73/Sir_James_Brooke_%281847%29_by_Francis_Grant.jpg",
}

CREDITS = {
    "KUCHPANO": "Jin, CC BY 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},       # s0  title
    {"img": "WEDDING", **_LB},    # s1  Elizabeth Choy, born in Kudat
    {"img": "ZEHNDER", **_LB},    # s2  Hugh Zehnder, born in Sarawak
    {"img": "ST1935", **_LB},     # s3  Wee Kheng Chiang (his photo is on the page); not exceptions (s4)
    {"img": "KUCHPANO", **_LB},   # s5  a century and a half of people, money and ships
    {"img": "KUCH1844", **_LB},   # s6  a voyage from Singapore
    {"img": "BROOKE", **_LB},     # s7  James Brooke sails 1839; Rajah by 1841 (s8)
]
SCHEDULE = [(0, 0), (5.85, 1), (15.625, 2), (21.65, 3), (28.625, 4), (44.5, 5), (48.425, 6)]
TOTAL_DURATION = 64.825
TIMING_JSON = "audio/from-borneo-to-singapore-the-sabah-and-sarawak-people-in-singapores-story.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
