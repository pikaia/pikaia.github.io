"""Short config for the early banks post.

Excerpt: the opening hook (sentences 0-3, 0.0-32.05 s): twenty-one years with no
bank, the agency houses and moneylenders, and the first bank in 1840. Ends
exactly where sentence 4 begins in the main config's own timing. Vertical
1080x1920.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "BATTERY": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif.jpg",
    "PIER": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/KITLV_-_1404900_-_Johnston%27s_Pier_and_H._M._Bank._Singapore_-_1895-1906.tif/lossy-page1-1920px-KITLV_-_1404900_-_Johnston%27s_Pier_and_H._M._Bank._Singapore_-_1895-1906.tif.jpg",
    "COINSG": "https://upload.wikimedia.org/wikipedia/commons/3/33/1789_Charles_IV_Spanish_dollar_countermarked_with_Chinese_words_meaning_%22Singapore%22.jpg",
    "HSBC": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/KITLV_-_50198_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Building_of_the_Hong_Kong_and_Shanghai_Bank_in_Singapore_-_circa_1900.tif/lossy-page1-1920px-KITLV_-_50198_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Building_of_the_Hong_Kong_and_Shanghai_Bank_in_Singapore_-_circa_1900.tif.jpg",
}

_VA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.25, 0.5), (0.4, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_VP = {"type": "cover", "zoom": [1.3, 1.32, 1.35], "pan": [(0.3, 0.2), (0.4, 0.2), (0.5, 0.2)], "ease": "ease-in-out"}
_VC = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}
_VH = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.3, 0.5), (0.45, 0.5), (0.6, 0.5)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "BATTERY", **_VA},  # s0 title
    {"img": "PIER", **_VP},  # s1 no bank at all
    {"img": "COINSG", **_VC},  # s2 borrowed, lent, paid
    {"img": "HSBC", **_VH},  # s3 first bank 1840
]

SCHEDULE = [(0.0, 0), (4.325, 1), (11.85, 2), (24.35, 3)]
TOTAL_DURATION = 32.05
TIMING_JSON = "audio/before-the-banks-how-singapores-merchants-kept-their-money.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
