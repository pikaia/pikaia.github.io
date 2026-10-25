"""Short config for the Ghee Hin post.

The post's opening, sentences 0-5 (0-63.85s, over the 60s line): the 1890
law that closed the Ghee Hin, sixty years of the secret societies, the
headmen handing in their seals, and the societies' roots in the Tiandihui.
No sentence names anyone. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "NBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
    "CERT": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Membership_certificate_of_the_Ghee_Hin_Kongsi_from_William_Stirling_Collection.jpg",
    "PROT": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1280px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg",
    "THK1890": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_103742_-_Lambert_%26_Co._-_Thian_Hock_Keng_Temple_in_Singapore_-_circa_1890.tif.jpg",
    "STREET1860": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/KITLV_-_29169_-_Chinese_street_in_Singapore%2C_completely_decorated_on_the_occasion_of_the_visit_of_Prince_Albert_of_Saxe-Coburg_-_Gotha%2C_husband_of_Queen_Victoria_-_1860.tif/lossy-page1-1280px-KITLV_-_29169_-_Chinese_street_in_Singapore%2C_completely_decorated_on_the_occasion_of_the_visit_of_Prince_Albert_of_Saxe-Coburg_-_Gotha%2C_husband_of_Queen_Victoria_-_1860.tif.jpg",  # thumbnail only
    "YING": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Ying_Fo_Fui_Kun%2C_Telok_Ayer_Street%2C_October_2025.jpg/1280px-Ying_Fo_Fui_Kun%2C_Telok_Ayer_Street%2C_October_2025.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "STREET1860", "pan": (0.5, 0.5)},
    {"img": "THK1890", "pan": (0.5, 0.5)},
    {"img": "NBR", "pan": (0.5, 0.5)},
    {"img": "YING", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "NBR", **_LB},        # s0
    {"img": "CERT", **_LB},       # s1
    {"img": "PROT", **_LB},       # s3
    {"img": "THK1890", **_LB},    # s4
]
SCHEDULE = [(0.0, 0), (5.05, 1), (33.125, 2), (42.025, 3)]
TOTAL_DURATION = 63.85
TIMING_JSON = "audio/the-ghee-hin-and-the-1890-ban-on-the-secret-societies.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
