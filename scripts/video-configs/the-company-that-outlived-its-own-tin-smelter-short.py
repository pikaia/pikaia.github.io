"""Short config for the Straits Trading Company post.

Excerpt: the opening hook (sentences 0-4, 0.0-42.77s) - "By 1912, a company
most Singaporeans today have never heard of was smelting roughly a third of
the world's tin ... still around, still listed, still making money, more
than a century after the furnaces on Pulau Brani first lit." Ends exactly
where sentence 5 begins in the main config's own timing.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SMELTER": f"{_U}/thumb/5/56/Gezicht_op_de_tinsmelterijen_op_het_eiland_Pulau_Brani_bij_Singapore_View_of_Pulo_Brani_tin_smelting_works_%28titel_op_object%29%2C_RP-F-F01140-AH.jpg/1920px-Gezicht_op_de_tinsmelterijen_op_het_eiland_Pulau_Brani_bij_Singapore_View_of_Pulo_Brani_tin_smelting_works_%28titel_op_object%29%2C_RP-F-F01140-AH.jpg",
    "BRANI1910": f"{_U}/thumb/a/ad/KITLV_-_79928_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_industry_at_the_island_of_Pulau_Brani%2C_Singapore_-_circa_1910.tif/lossy-page1-1920px-KITLV_-_79928_-_Kleingrothe%2C_C.J._-_Medan_-_Tin_industry_at_the_island_of_Pulau_Brani%2C_Singapore_-_circa_1910.tif.jpg",
}

_SMA = {"type": "cover", "zoom": [1.5, 1.55, 1.6], "pan": [(0.55, 0.5)] * 3, "ease": "ease-in-out"}
_SMB = {"type": "cover", "zoom": [1.7, 1.65, 1.6], "pan": [(0.62, 0.5)] * 3, "ease": "ease-out"}
_BRA = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.6, 0.6)] * 3, "ease": "ease-in-out"}

SLIDES = [
    {"img": "SMELTER", **_SMA},    # s0-1 title + smelting a third of the world's tin
    {"img": "SMELTER", **_SMB},    # s2-3 Straits Tin, smelter gone, island a naval base
    {"img": "BRANI1910", **_BRA},  # s4   still around, still listed
]

SCHEDULE = [(0.0, 0), (15.12, 1), (33.08, 2)]
TOTAL_DURATION = 42.77
TIMING_JSON = "audio/the-company-that-outlived-its-own-tin-smelter.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
