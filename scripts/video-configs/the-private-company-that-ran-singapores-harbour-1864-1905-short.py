"""Short config for the Tanjong Pagar Dock Company post.

Excerpt: the opening hook (sentences 0-2, 0.0-43.9s) - the 1905 takeover and the
company that "controlled nearly all of the docks and wharves". Ends exactly where
sentence 3 begins in the main config's own timing. Vertical 1080x1920: the album
pages are zoomed to 1.55-1.7 so the window stays inside the photograph.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "MEAL": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Schepen_in_een_dok_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_met_eromheen_personeel_Meal_hour%2C_Tanjong_Pagar_Dock%2C_men_leaving_off_work_%28titel_op_object%29%2C_RP-F-F01140-A.jpg/1920px-thumbnail.jpg",
    "PANW": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tanjong_Pagar_in_Singapore_gezien_vanuit_het_westen_Panoramic_view_of_Tanjong_Pagar_from_the_west_%28titel_op_object%29%2C_RP-F-F01140-AE.jpg/1920px-Tanjong_Pagar_in_Singapore_gezien_vanuit_het_westen_Panoramic_view_of_Tanjong_Pagar_from_the_west_%28titel_op_object%29%2C_RP-F-F01140-AE.jpg",
    "WHARF": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Deel_van_de_scheepswerf_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_View_shewing_section_of_wharf_%28titel_op_object%29%2C_RP-F-F01140-P.jpg/1920px-Deel_van_de_scheepswerf_van_de_Tanjong_Pagar_Dock_Co._Ltd._in_Singapore_View_shewing_section_of_wharf_%28titel_op_object%29%2C_RP-F-F01140-P.jpg",
}

_VA = {"type": "cover", "zoom": [1.6, 1.65, 1.7], "pan": [(0.35, 0.5), (0.45, 0.5), (0.55, 0.5)], "ease": "ease-in-out"}
_VB = {"type": "cover", "zoom": [1.7, 1.65, 1.6], "pan": [(0.6, 0.5), (0.5, 0.5), (0.4, 0.5)], "ease": "ease-in-out"}
_VP = {"type": "cover", "zoom": [1.55, 1.6, 1.65], "pan": [(0.35, 0.42), (0.5, 0.42), (0.65, 0.42)], "ease": "ease-in-out"}

SLIDES = [
    {"img": "MEAL", **_VA},  # s0 title
    {"img": "PANW", **_VB},  # s1 1905 takeover, $755 a share
    {"img": "WHARF", **_VP},  # s2 first local joint-stock company, nearly all the docks and wharves
]

SCHEDULE = [(0.0, 0), (6.525, 1), (25.35, 2)]
TOTAL_DURATION = 43.9
TIMING_JSON = "audio/the-private-company-that-ran-singapores-harbour-1864-1905.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
