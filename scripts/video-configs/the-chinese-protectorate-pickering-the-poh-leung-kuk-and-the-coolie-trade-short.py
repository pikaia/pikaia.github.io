"""Short config for the Chinese Protectorate post.

The post's opening, sentences 0-7 (0-69.725s, over the 60s line): the 1887
axe-head attack on Pickering, the secret societies, and the credit-ticket
system that brought the sinkeh to Singapore. Every slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff/lossy-page1-1280px-Chinese_Protectorate%2C_Singapore%2C_KITLV_1404946.tiff.jpg",
    "PICK": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Portrait_of_Pickering%2C_William_Alexander.jpg/1280px-Portrait_of_Pickering%2C_William_Alexander.jpg",
    "NBR": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff/lossy-page1-1280px-KITLV_-_43317_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_The_North_Bridge_Road%2C_Singapore_-_circa_1900.tiff.jpg",
    "PORT90": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_150813_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Port_at_Singapore_-_circa_1890.tif.jpg",
    "SHANTOU": "https://upload.wikimedia.org/wikipedia/commons/d/db/COLLECTIE_TROPENMUSEUM_Chinese_koelies_uit_Shantou_verlaten_het_schip_%27s_Jacob_in_de_haven_van_Belawan_Sumatra_om_in_de_tabakcultuur_te_gaan_werken_TMnr_10001445.jpg",
    "COOL": "https://upload.wikimedia.org/wikipedia/commons/1/13/Photographic_Views_of_Singapore_Plate_13_Group_of_Coolies.jpg",  # thumbnail only
    "MOL25": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Former_Ministry_of_Labour_Building%2C_October_2025.jpg/1280px-Former_Ministry_of_Labour_Building%2C_October_2025.jpg",  # thumbnail only
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "PICK", "pan": (0.5, 0.4)},
    {"img": "COOL", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "MOL25", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB},       # s0
    {"img": "PICK", **_LB},       # s2
    {"img": "NBR", **_LB},        # s4
    {"img": "PORT90", **_LB},     # s5
    {"img": "SHANTOU", **_LB},    # s6
]
SCHEDULE = [(0.0, 0), (18.7, 1), (29.025, 2), (42.725, 3), (56.3, 4)]
TOTAL_DURATION = 69.725
TIMING_JSON = "audio/the-chinese-protectorate-pickering-the-poh-leung-kuk-and-the-coolie-trade.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
