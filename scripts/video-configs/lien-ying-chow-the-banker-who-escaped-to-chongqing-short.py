"""Short config for the Lien Ying Chow post.

The post's opening, sentences 0-8 (0-84.275s): the escape on the Gorgon with
two diamonds in his clothes, the bank he opened seven years later, and where
he came from - Dapu, Hong Kong, and a HK$10 ticket to Singapore. The 1949
opening announcement fills the vertical frame on its own column.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "RAFFLES1963": f"{_C}/b/bf/SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg/1920px-SG_Singapore_Raffles_Square_-_1963_%28W63-K27-15%29.jpg",
    "WHARF": f"{_C}/d/dc/KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff/lossy-page1-1920px-KITLV_A1041_-_Haven_van_Singapore%2C_KITLV_140424.tiff.jpg",
    "HARBPAN": f"{_C}/0/0e/De_haven_van_Singapore%2C_KITLV_29185.tiff/lossy-page1-1920px-De_haven_van_Singapore%2C_KITLV_29185.tiff.jpg",
    "FREMANTLE": f"{_U}/8/8a/Fremantle_Harbour%2C_WW2.PNG",
    "ST1949": f"{_A}/straits-times-1949-02-05-page-4.jpg",
    "DAPU": f"{_C}/3/31/Dapu_County_DSC_2199_%284129932675%29.jpg/1920px-Dapu_County_DSC_2199_%284129932675%29.jpg",
    "HK1920": f"{_U}/c/cc/Hong_Kong_Connaught_Road_1920s.jpg",
}

CREDITS = {
    "WHARF": "The harbour of Singapore, KITLV 140424, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "HARBPAN": "The harbour of Singapore, KITLV 29185, unknown photographer, CC BY 4.0, via Wikimedia Commons",
    "DAPU": "Sunset over Dapu County, 2009, Aaron Lai, CC BY 2.0, via Wikimedia Commons",
}

_E = "ease-in-out"


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "RAFFLES1963", **_v([1.0, 1.05, 1.1], [(0.5, 0.5)] * 3)},                  # s0  title
    {"img": "WHARF", **_v([1.0, 1.05, 1.1], [(0.55, 0.5)] * 3)},                       # s1  the Gorgon leaves
    {"img": "HARBPAN", **_v([1.0, 1.05, 1.1], [(0.4, 0.5)] * 3)},                      # s2  two diamonds
    {"img": "FREMANTLE", **_v([1.0, 1.05, 1.1], [(0.5, 0.5)] * 3)},                    # s3  Fremantle
    {"img": "ST1949", **_v([1.15, 1.2, 1.25], [(0.0, 0.0), (0.0, 0.01), (0.0, 0.02)])}, # s4  the new bank
    {"img": "DAPU", **_v([1.0, 1.05, 1.1], [(0.45, 0.5)] * 3)},                        # s5-7 Dapu
    {"img": "HK1920", **_v([1.0, 1.05, 1.1], [(0.4, 0.5)] * 3)},                       # s8  Hong Kong, HK$10
]
SCHEDULE = [(0.0, 0), (3.85, 1), (18.6, 2), (31.55, 3), (38.775, 4), (50.4, 5), (71.4, 6)]
TOTAL_DURATION = 84.275
TIMING_JSON = "audio/lien-ying-chow-the-banker-who-escaped-to-chongqing.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
