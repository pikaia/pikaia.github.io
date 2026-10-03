"""Video config for the UOB / United Chinese Bank post.

The early years are well covered: Raffles Place and Chulia Street from the
1870s to the 1920s, the Bonham Building where the bank opened, and three 1935
newspaper pages (the Straits Times opening report, with photos of Wee Kheng
Chiang and Chua Keh Hai, and the Malaya Tribune's advertisement and "New bank
opens" report). Newspaper pages are whole-page `cover` with a push-in on the
relevant story, pan/zoom worked out from real cover_crop test frames
(scratch/uob/pans.py), zoom capped at 2.4x.

After 1960 the pool is thin (the 1978 skyline, the OUB godown, the towers and
the history plaque), so the towers photos appear twice. Tall photos are
letterboxed. Named people get their own photo or none: Wee Kheng Chiang and
Chua Keh Hai from the 1935 page, Aw Boon Haw from the Aw Brothers post;
Wee Cho Yaw, Ong Piah Teng, Lien Ying Chow and Wee Ee Cheong have no free
photo, so their sentences sit on places or pages.

31 slides, 440.3s. AVATAR: first and last 30s (avatar test #2).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "RP1920S": f"{_C}/7/7c/KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff/lossy-page1-1280px-KITLV_A723_-_Raffles_Place_te_Singapore%2C_KITLV_87929.tiff.jpg",
    "BONHAM": f"{_U}/a/a1/Bonham_Building_1907.jpg",
    "TOWERS": f"{_U}/3/38/UOBnOUB.JPG",
    "KATZ": f"{_U}/4/4b/Katz_Bros._Bonham_Street_1902.png",
    "KLING1870": f"{_C}/4/44/Kling_Street_in_Singapore%2C_RP-F-AA3188-BM.jpg/1920px-Kling_Street_in_Singapore%2C_RP-F-AA3188-BM.jpg",
    "KLING1907": f"{_C}/d/d0/Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg/1920px-Kling_Street%2C_Singapore_%28NYPL_Hades-2359713-4044478%29.jpg",
    "RP1910": f"{_C}/c/c7/KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "RP1920": f"{_U}/a/a4/Raffles_Place_c._1920.jpg",
    "RPCARS": f"{_C}/8/87/Raffles_Place_Singapore%2C_KITLV_1404977.tiff/lossy-page1-1280px-Raffles_Place_Singapore%2C_KITLV_1404977.tiff.jpg",
    "CHARTERED": f"{_C}/5/59/The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff/lossy-page1-1280px-The_Chartered_Bank_aan_Raffles_Place_te_Singapore%2C_KITLV_104795.tiff.jpg",
    "BOATQUAY": f"{_C}/e/e7/Boat_Quay_Singapore%2C_KITLV_1404940.tiff/lossy-page1-1280px-Boat_Quay_Singapore%2C_KITLV_1404940.tiff.jpg",
    "SKY1978": f"{_C}/c/c0/153_Singapore%2C_Jan_1978_%2852023517826%29.jpg/1280px-153_Singapore%2C_Jan_1978_%2852023517826%29.jpg",
    "OUBGODOWN": f"{_C}/9/99/Former_Overseas_Union_Bank%2C_near_Robertson_Quay%2C_Singapore.jpg/1280px-Former_Overseas_Union_Bank%2C_near_Robertson_Quay%2C_Singapore.jpg",
    "PLAZA_OUB": f"{_C}/c/c9/Oub-uob-towers_cropped.jpg/1280px-Oub-uob-towers_cropped.jpg",
    "PLAZA1": f"{_U}/0/0b/United_Overseas_Bank_Plaza_One.jpg",
    "PLAQUE": f"{_C}/3/36/United_Overseas_Bank_History_Plaque.jpg/1280px-United_Overseas_Bank_History_Plaque.jpg",
    "AWBH": f"{_U}/8/87/Hu_Wenhu.jpg",
    "CHART": f"{_A}/uob-banks-timeline-chart.png",
    "ST351001": f"{_A}/straits-times-1935-10-01-page-12.jpg",
    "MT3": f"{_A}/malaya-tribune-1935-10-02-page-3.jpg",
    "MT13": f"{_A}/malaya-tribune-1935-10-02-page-13.jpg",
    "ST32": f"{_A}/straits-times-1932-08-30-page-9.jpg",
}

# Credits for images that aren't captioned in the post or its gallery.
_NSG = "Singapore Press Holdings, via NewspaperSG, National Library Board Singapore, public domain"
CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, figures per the post's own Sources list",
    "KLING1907": "Kling Street (now Chulia Street), postcard of 1907 (New York Public Library, public domain, via Wikimedia Commons)",
    "AWBH": "Aw Boon Haw, from a 1941 Japanese biographical volume (public domain, via Wikimedia Commons)",
    "ST32": f"The Straits Times, 30 August 1932, page 9 ({_NSG})",
}

_E = "ease-in-out"
# Photos (roughly landscape): gentle push-in / pull-back.
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.35, 0.45)] * 3, "ease": _E}
_INR = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.65, 0.45)] * 3, "ease": _E}
# Tall photos (towers, plaque, portrait): letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Graphics (chart): letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _page(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins (scratch/uob/pans.py test frames).
_ST_HEAD = _page([2.16, 2.28, 2.4], [(0.481, 0.0), (0.482, 0.0), (0.483, 0.0)])
# Kept tight and high so Chua Keh Hai's photo, just below, stays out of frame.
_ST_WKC = _page([2.28, 2.34, 2.4], [(0.68, 0.12), (0.655, 0.12), (0.63, 0.12)])
_ST_BODY = _page([2.09, 2.2, 2.32], [(0.481, 0.107), (0.482, 0.112), (0.482, 0.117)])
_ST_CHUA = _page([2.16, 2.28, 2.4], [(0.346, 0.32), (0.35, 0.322), (0.354, 0.325)])
_MT3_AD = _page([2.16, 2.28, 2.4], [(0.03, 0.449), (0.03, 0.45), (0.03, 0.451)])
_MT3_TOP = _page([1.0, 1.04, 1.08], [(0.5, 0.0)] * 3)
_MT13 = _page([1.64, 1.73, 1.82], [(0.045, 0.108), (0.079, 0.116), (0.106, 0.122)])
_ST32 = _page([2.16, 2.28, 2.4], [(0.174, 0.004), (0.188, 0.011), (0.2, 0.016)])
# The 1870s print sits small on an album page: crop to the print itself.
_KLING1870 = _page([2.05, 2.18, 2.3], [(0.44, 0.5), (0.47, 0.5), (0.5, 0.5)])
# The c. 1920 print has a black border: start zoomed past it.
_RP1920 = _page([1.18, 1.23, 1.28], [(0.5, 0.45)] * 3)

SLIDES = [
    {"img": "RP1920S", **_IN},          # 0  s0      title
    {"img": "BONHAM", **_IN},           # 1  s1      opened 1 Oct 1935, Chulia / Bonham Street
    {"img": "MT13", **_MT13},           # 2  s2      seven founders, $1 million paid up ("New bank opens")
    {"img": "PLAZA_OUB", **_PORT},      # 3  s3      ninety years later, UOB
    {"img": "PLAQUE", **_PORT},         # 4  s4      growth by buying other banks (the plaque lists them)
    {"img": "ST351001", **_ST_WKC},     # 5  s5-7    Wee Kheng Chiang: founder, Kuching, chairman
    {"img": "ST351001", **_ST_HEAD},    # 6  s8      "Chinese Bank Opened Today"
    {"img": "ST351001", **_ST_BODY},    # 7  s9-10   capital; Ong Piah Teng and the directors
    {"img": "ST351001", **_ST_CHUA},    # 8  s11     Chua Keh Hai, the manager
    {"img": "MT3", **_MT3_AD},          # 9  s12     the bank's advertisement, 31-A Chulia Street
    {"img": "KLING1907", **_INR},       # 10 s13     a single office, Hokkien traders
    {"img": "ST32", **_ST32},           # 11 s14-15  a crowded field; the 1932 OCBC merger
    {"img": "KATZ", **_IN},             # 12 s16     little published on the Occupation
    {"img": "RP1910", **_INL},          # 13 s17     Wee Cho Yaw, Karimun (no photo of him)
    {"img": "CHARTERED", **_IN},        # 14 s18-20  board 1958, managing director 1960, aged 31
    {"img": "RPCARS", **_OUT},          # 15 s21-22  small steps: mobile branch, Beach Road, women
    {"img": "RP1920S", **_INL},         # 16 s23-24  renamed United Overseas Bank, 1965
    {"img": "RP1920", **_RP1920},       # 17 s25     from 1971, growth by acquisition
    {"img": "AWBH", **_PORT},           # 18 s26-27  Chung Khiaw Bank, Aw Boon Haw
    {"img": "KLING1870", **_KLING1870}, # 19 s28-29  Lee Wah (1920), Far Eastern, ICB
    {"img": "SKY1978", **_IN},          # 20 s30-31  1974: chairman; the 30-storey tower
    {"img": "PLAZA1", **_PORT},         # 21 s32     UOB Plaza One, 1995
    {"img": "BOATQUAY", **_IN},         # 22 s33-34  2001; OUB, founded by Lien Ying Chow, 1949
    {"img": "TOWERS", **_PORT},         # 23 s35-36  the DBS bid, UOB's counter-bid
    {"img": "PLAZA1", **_PORT_OUT},     # 24 s37     the win: the largest local bank
    {"img": "OUBGODOWN", **_IN},        # 25 s38     the OUB name gone by 2003
    {"img": "PLAZA_OUB", **_PORT_OUT},  # 26 s39-40  Wee Cho Yaw steps down; Wee Ee Cheong
    {"img": "CHART", **_GFX},           # 27 s41     the chart
    {"img": "MT3", **_MT3_TOP},         # 28 s42     1935: one of many small Chinese banks
    {"img": "TOWERS", **_PORT_OUT},     # 29 s43-44  three large local banks today
    {"img": "BONHAM", **_OUT},          # 30 s45-46  closing: a single rented office
]

SCHEDULE = [
    (0.0, 0), (6.375, 1), (21.475, 2), (34.275, 3), (41.6, 4), (47.275, 5),
    (72.175, 6), (79.85, 7), (99.4, 8), (111.375, 9), (121.35, 10), (128.45, 11),
    (143.075, 12), (148.975, 13), (159.675, 14), (175.1, 15), (197.825, 16),
    (215.95, 17), (225.675, 18), (249.375, 19), (272.575, 20), (289.225, 21),
    (295.225, 22), (313.975, 23), (334.925, 24), (351.9, 25), (356.425, 26),
    (372.9, 27), (382.1, 28), (394.175, 29), (414.175, 30),
]
TOTAL_DURATION = 440.3
TIMING_JSON = "audio/uob-the-united-chinese-bank-of-1935-and-the-family-that-built-it.timing.json"

# The avatar presenter, Phase 1 test #2: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
