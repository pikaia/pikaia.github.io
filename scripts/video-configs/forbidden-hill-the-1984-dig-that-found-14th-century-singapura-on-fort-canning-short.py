"""Short config for the Forbidden Hill post.

The post's opening, sentences 0-6 (0-76.225s, over the 60s TikTok line): the
ten-day dig of January 1984 beside the Keramat, the porcelain of the 1300s,
the plans for the hill and the museum's invitation to Miksic. The Keramat
pavilion is cropped to fill the vertical frame; the watercolour, the trench
photos, the Yuan plate and Elliot's long view are wide, so they are
letterboxed.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": f"{_C}/0/02/Charles_Dyce%2C_Government_Hill_from_the_New_Harbour_Road%2C_Singapore%2C_1846%2C_Watercolour_%26_Ink_on_paper%2C_27.2_x_44.8_cm.png/1280px-Charles_Dyce%2C_Government_Hill_from_the_New_Harbour_Road%2C_Singapore%2C_1846%2C_Watercolour_%26_Ink_on_paper%2C_27.2_x_44.8_cm.png",
    "KERAMAT11": f"{_C}/f/fb/Keramat_Iskandar_Syah%2C_Fort_Canning_Park%2C_Singapore_-_20110924.jpg/1280px-Keramat_Iskandar_Syah%2C_Fort_Canning_Park%2C_Singapore_-_20110924.jpg",
    "PITS091": f"{_C}/1/12/At_Fort_Canning_2023_091.jpg/1280px-At_Fort_Canning_2023_091.jpg",
    "YUAN": f"{_C}/d/da/Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Plate.jpg/1280px-Yuan_Underglaze_Blue_Jingdezhen_Porcelain_Plate.jpg",
    "VIEW1828": f"{_C}/8/84/View_of_the_town_and_roads_of_Singapore_from_the_government_hill_published_1828.jpg/1280px-View_of_the_town_and_roads_of_Singapore_from_the_government_hill_published_1828.jpg",
    "PITS089": f"{_C}/1/11/At_Fort_Canning_2023_089.jpg/1280px-At_Fort_Canning_2023_089.jpg",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_LB},                                         # s0  title: Government Hill, 1840s
    {"img": "KERAMAT11", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)}, # s1  January 1984, beside the Keramat
    {"img": "PITS091", **_LB},                                      # s2  almost nothing at first
    {"img": "YUAN", **_LB},                                         # s3  blue-and-white porcelain
    {"img": "HERO", **_LB},                                         # s4  a town on the hill
    {"img": "VIEW1828", **_LB},                                     # s5  plans for the hill
    {"img": "PITS089", **_LB},                                      # s6  the museum invites Miksic
]
SCHEDULE = [(0.0, 0), (7.15, 1), (21.4, 2), (25.825, 3), (34.1, 4), (46.575, 5), (58.075, 6)]
TOTAL_DURATION = 76.225
TIMING_JSON = "audio/forbidden-hill-the-1984-dig-that-found-14th-century-singapura-on-fort-canning.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
