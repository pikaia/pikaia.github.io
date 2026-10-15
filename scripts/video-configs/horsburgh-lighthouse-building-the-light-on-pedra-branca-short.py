"""Short config for the Horsburgh Lighthouse post.

The post's opening, sentences 0-5 (0-63.2s, over the 60s TikTok line): the
foundation stone laid on Pedra Branca on 24 May 1850, the party that sailed out
for it, the lighthouse named for James Horsburgh, its architect John Turnbull
Thomson, and what "Pedra Branca" means. Horsburgh gets his own chart and
Thomson his own portrait. Everything is letterboxed except the hero
lithograph, which fills the frame; the paintings are small and the chart and
portrait must not be cropped.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/6/62/Horsburgh_Lighthouse_by_John_T_Thomson_2.jpg/1280px-Horsburgh_Lighthouse_by_John_T_Thomson_2.jpg",
    "STORM": f"{_U}/2/23/PedraBranca-TRobertson-1882.jpg",
    "SEPIA": f"{_U}/8/82/HorsburghLighthouse-JTThomson-1851-02.jpg",
    "HCHART": f"{_C}/9/93/Strait_of_Malacca_Horsburgh_1806_nla.obj-373089850.jpg/1280px-Strait_of_Malacca_Horsburgh_1806_nla.obj-373089850.jpg",
    "THOMSON": f"{_U}/0/03/JohnTurnbullThomson.jpg",
    "DANIELL": f"{_U}/f/ff/PedraBranca-Daniell-c1820.jpg",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},  # s0  title
    {"img": "STORM", **_LB},                                      # s1  24 May 1850, out to a bare rock
    {"img": "SEPIA", **_LB},                                      # s2  the Governor, an admiral, the Freemasons
    {"img": "HCHART", **_LB},                                     # s3  named for James Horsburgh
    {"img": "THOMSON", **_LB},                                    # s4  its architect, John Turnbull Thomson
    {"img": "DANIELL", **_LB},                                    # s5  "white rock"
]
SCHEDULE = [(0.0, 0), (4.35, 1), (15.8, 2), (28.825, 3), (37.825, 4), (55.55, 5)]
TOTAL_DURATION = 63.2
TIMING_JSON = "audio/horsburgh-lighthouse-building-the-light-on-pedra-branca.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
