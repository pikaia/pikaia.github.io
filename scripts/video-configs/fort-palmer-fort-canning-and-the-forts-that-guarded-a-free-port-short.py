"""Short config for the forts post.

The post's opening, sentences 0-4 (0-62.675s, over the 60s TikTok line): the
Governor firing the new 10-inch guns at Mount Palmer in October 1891, the Town
Hall protest seven months earlier, and the question of who should pay. The
narrow 1891 newspaper column fills the vertical frame; album prints are
cropped inside their mounts.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "MP": f"{_C}/1/13/Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg/1920px-Strand_en_badgasten_aan_de_voet_van_Mount_Palmer_%28Mount_Parsee%2C_Parsee_Hill%29_bij_Singapore_Foot_of_Mount_Palmer._S.pore_%28titel_op_object%29%2C_RP-F-F01104-Z.jpg",
    "NHENTR": f"{_C}/7/78/Gezicht_op_de_ingang_van_de_nieuwe_haven_te_Singapore_Entrance_to_New-harbour._S.pore_%28titel_op_object%29%2C_RP-F-F01104-X.jpg/1920px-Gezicht_op_de_ingang_van_de_nieuwe_haven_te_Singapore_Entrance_to_New-harbour._S.pore_%28titel_op_object%29%2C_RP-F-F01104-X.jpg",
    "CANBATT": f"{_C}/6/69/KITLV_-_29173_-_Singapore_city_and_harbor%2C_at_the_right_the_battery_for_the_day_and_evening_shot_-_circa_1860.tif/lossy-page1-3840px-KITLV_-_29173_-_Singapore_city_and_harbor%2C_at_the_right_the_battery_for_the_day_and_evening_shot_-_circa_1860.tif.jpg",
    "OCT1891": f"{_A}/straits-times-1891-10-14-page-2.jpg",
    "MAR1891": f"{_A}/straits-times-1891-03-14-page-3.jpg",
}

_E = "ease-in-out"
SLIDES = [
    {"img": "MP", "type": "cover", "zoom": [1.15, 1.2, 1.25], "pan": [(0.62, 0.45)] * 3, "ease": _E},       # s0  title
    {"img": "NHENTR", "type": "cover", "zoom": [1.15, 1.2, 1.25], "pan": [(0.72, 0.5)] * 3, "ease": _E},    # s1  the party on the hill
    {"img": "OCT1891", "type": "cover", "zoom": [2.2, 2.3, 2.4], "pan": [(1.0, 0.0), (1.0, 0.03), (1.0, 0.06)], "ease": _E},  # s2  the guns fire
    {"img": "MAR1891", "type": "cover", "zoom": [2.2, 2.3, 2.4], "pan": [(0.0, 0.0), (0.0, 0.02), (0.0, 0.04)], "ease": _E},  # s3  the Town Hall protest
    {"img": "CANBATT", "type": "cover", "zoom": [1.3, 1.35, 1.4], "pan": [(0.82, 0.75)] * 3, "ease": _E},  # s4  who should pay
]
SCHEDULE = [(0.0, 0), (4.7, 1), (17.7, 2), (35.15, 3), (50.375, 4)]
TOTAL_DURATION = 62.675
TIMING_JSON = "audio/fort-palmer-fort-canning-and-the-forts-that-guarded-a-free-port.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
