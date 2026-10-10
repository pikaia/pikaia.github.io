"""Short config for the remittance-houses post.

The post's opening, sentences 0-5 (0-65.625s, over the 60s TikTok line): the
labourer sending wages home through a remittance house, the qiaopi, Singapore
as the hub, the 1876 riot, and the settlers from Fujian and Guangdong. The
tall qiaopi envelope and the 1876 newspaper page fill the vertical frame;
the 1890 vendor portrait, North Bridge Road and Amoy harbour are letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/3/32/%E4%BE%A8%E6%89%B91.jpg/1280px-%E4%BE%A8%E6%89%B91.jpg",
    "VENDOR": f"{_C}/1/10/KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif.jpg",
    "NBR1900": f"{_C}/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
    "ENV": f"{_C}/0/02/%E4%BE%A8%E6%89%B92.jpg/1280px-%E4%BE%A8%E6%89%B92.jpg",
    "ST1876": f"{_A}/straits-times-1876-12-16-page-5.jpg",
    "AMOY69": f"{_C}/2/2e/Amoy_Harbour_MET_DP165636.jpg/1280px-Amoy_Harbour_MET_DP165636.jpg",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.45, 0.5), (0.5, 0.5), (0.55, 0.5)])},   # s0   title: the letter
    {"img": "VENDOR", **_LB},                                                           # s1   a labourer sending wages home
    {"img": "NBR1900", **_LB},                                                          # s2   a remittance house in the back streets
    {"img": "ENV", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)},                          # s3   the qiaopi
    {"img": "ST1876", **_v([1.0, 1.06, 1.12], [(0.5, 0.0), (0.5, 0.05), (0.5, 0.1)])},  # s4   the 1876 riot
    {"img": "AMOY69", **_LB},                                                           # s5   from Fujian and Guangdong
]
SCHEDULE = [(0.0, 0), (6.1, 1), (15.775, 2), (31.425, 3), (45.3, 4), (54.475, 5)]
TOTAL_DURATION = 65.625
TIMING_JSON = "audio/letters-with-money-singapores-remittance-houses.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
