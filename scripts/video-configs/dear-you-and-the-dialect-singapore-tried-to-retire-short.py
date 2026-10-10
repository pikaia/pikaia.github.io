"""Video config for the Dear You / Speak Mandarin Campaign post's YouTube
Shorts excerpt.

Self-contained hook: the post's opening (0-63.475s since 2026-10-10, when it
was extended through sentences 5-6, the census record of the gap, to pass the
60s TikTok line and given the 0.70 caption height) - the title, the
"understand but can't speak" gap most 40-and-50-something Singaporeans
recognize, "not an accident... the direct result of a 1979 language
policy", Dear You selling out its original-dialect screenings, then "the
'why' behind that gap is a matter of public record" and the census going
back to 1980, right when the Speak Mandarin Campaign began.

TEMPLE (1600x1200 = 1.33) is close to 4:3, far from the vertical
1080x1920 target (0.5625) - letterbox here, same lesson as every prior
Short. OLDTEMPLE and VENDOR are 960px KITLV scans, so letterbox too rather
than a deep vertical crop.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "TEMPLE": "https://upload.wikimedia.org/wikipedia/commons/7/71/Yueh_Hai_Ching_Temple_8%2C_Mar_06.JPG",
    "OLDTEMPLE": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/KITLV_-_29181_-_Chinese_temple_in_Singapore_-_1895.tif/lossy-page1-960px-KITLV_-_29181_-_Chinese_temple_in_Singapore_-_1895.tif.jpg",
    "VENDOR": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif/lossy-page1-960px-KITLV_-_103776_-_Chinese_street_vendor_in_Singapore_-_circa_1890.tif.jpg",
}

SLIDES = [
    {"img": "TEMPLE", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "TEMPLE", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "TEMPLE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "OLDTEMPLE", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "VENDOR", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (15.7, 1), (31.4, 2), (47.0, 3), (51.475, 4)]
TOTAL_DURATION = 63.475  # end of sentence 6; extended 2026-10-10 past the 60s TikTok line
TIMING_JSON = "audio/dear-you-and-the-dialect-singapore-tried-to-retire.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
