"""Short config for the Great Depression / contagion post.

The post's opening, sentences 0-5 (0-61.725s, over the 60s TikTok line): the
rubber price falling from 34 cents to 4.95 cents, Singapore living off the
rubber and tin trade, and the hook that later crises followed a pattern worth
knowing now, with growth riding on chips for AI. Ends on the data centre.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "TAP1914": f"{_U}/9/99/Souvenir_of_Singapore%2C_1914_-_Plate_10_-_Rubber_Tapping.jpg",
    "TAPK": f"{_C}/7/7b/Tapping_Rubber%2C_KITLV_1404050.tiff/lossy-page1-1920px-Tapping_Rubber%2C_KITLV_1404050.tiff.jpg",
    "HARB": f"{_C}/3/37/Haven_van_Singapore%2C_KITLV_104789.tiff/lossy-page1-1920px-Haven_van_Singapore%2C_KITLV_104789.tiff.jpg",
    "UOB2001": f"{_U}/a/a8/Evening_view_of_UOB_Plaza%2C_OUB_Centre_and_OCBC_Centre_near_the_Singapore_River_-_20010608.jpg",
    "DATACTR": f"{_C}/5/5d/BalticServers_data_center.jpg/1920px-BalticServers_data_center.jpg",
}

CREDITS = {
    "TAPK": "Tapping rubber, KITLV 1404050, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "HARB": "The harbour of Singapore, KITLV 104789, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "DATACTR": "A data centre, BalticServers.com, CC BY-SA 3.0, via Wikimedia Commons",
}

_E = "ease-in-out"
SLIDES = [
    {"img": "TAP1914", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3, "ease": _E},   # s0  title
    {"img": "TAPK", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.4)] * 3, "ease": _E},      # s1-2 the price
    {"img": "HARB", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.6, 0.5)] * 3, "ease": _E},      # s3  the trade
    {"img": "UOB2001", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3, "ease": _E},   # s4  later recessions
    {"img": "DATACTR", "type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3, "ease": _E},   # s5  chips for AI
]
SCHEDULE = [(0.0, 0), (6.5, 1), (20.275, 2), (37.225, 3), (51.7, 4)]
TOTAL_DURATION = 61.725
TIMING_JSON = "audio/when-america-crashed-singapore-sank-the-great-depression-and-the-contagion-that-still-reaches-us.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
