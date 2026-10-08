"""Short config for the $50 million "gift" post.

The post's opening, sentences 0-5 (0-77.6s, over the 60s TikTok line): the
handover to Yamashita, the "voluntary gift" report, the levy and the loan,
and the prewar fundraising that the Japanese held against the community. The
26 June 1942 page fills the vertical frame on its headline and cheque photo.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_U}/2/21/Yamashita_e_Suzuki.jpg",
    "ST26": f"{_A}/syonan-shimbun-1942-06-26-page-2.jpg",
    "DJ2": f"{_U}/f/ff/Commemoration_of_anniversary_of_occupation_in_Asia_Raya_theatre%2C_Singapore_%28Syonan%29%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._5_%281943-03-01%29%2C_p31.jpg",
    "TKK1946": f"{_U}/a/a6/Tan_Kah_Kee%2C_Lee_Kong_Chian%2C_and_Tan_Lark_Sye%2C_1946.png",
    "BURMA": f"{_U}/6/6c/%E6%BB%87%E7%BC%85%E5%85%AC%E8%B7%AF01.jpg",
}

CREDITS = {
    "TKK1946": "Tan Kah Kee, Lee Kong Chian and Tan Lark Sye in about 1946, Tan Kah Kee Memorial Museum, public domain, via Wikimedia Commons",
    "BURMA": "Lorries on the Yunnan-Burma Road in 1940, Xiao Qian and Kuang Guang, public domain, via Wikimedia Commons",
}

_E = "ease-in-out"


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.05, 1.1], [(0.5, 0.5)] * 3)},                          # s0  title
    {"img": "ST26", **_v([1.7, 1.75, 1.8], [(1.0, 0.04), (1.0, 0.05), (1.0, 0.06)])},  # s1  the cheque, top right
    {"img": "ST26", **_v([1.0, 1.03, 1.06], [(0.85, 0.0), (0.85, 0.02), (0.85, 0.04)])},  # s2  "voluntary gift"
    {"img": "DJ2", "type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E},  # s3  demanded; half borrowed
    {"img": "TKK1946", "type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E},  # s4-5 prewar relief funds
    {"img": "BURMA", **_v([1.0, 1.05, 1.1], [(0.5, 0.5)] * 3)},                         # s5  the Burma Road volunteers
]
SCHEDULE = [(0.0, 0), (4.45, 1), (25.675, 2), (35.65, 3), (49.675, 4), (68.5, 5)]
TOTAL_DURATION = 77.6
TIMING_JSON = "audio/the-50-million-gift-of-1942.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
