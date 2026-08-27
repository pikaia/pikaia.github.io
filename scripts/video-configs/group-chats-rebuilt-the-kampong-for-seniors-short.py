"""Video config for the "How Group Chats Rebuilt the Kampong for
Singapore's Seniors" post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-38.88s) - the title, the
vivid vignette of a 78-year-old checking WhatsApp and sending a
good-morning sticker, closing on the payoff line: a government push to
get seniors online "ended up rebuilding something closer to old
kampong-style closeness than anyone quite planned for" - a real thesis
statement, not a mid-sentence cut.

Pairs a kampong image with the present-day BISHAN image to echo the
post's old-vs-new theme even within 3 slides. Both are landscape
enough (1.28-1.33 aspect) to diverge from the vertical 1080x1920
target - letterbox, same lesson as every prior Short.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "KAMPONGBUGIS": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/KITLV_-_105810_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Buggis%2C_the_Buginese_district_of_Singapore_-_circa_1900.tif/lossy-page1-960px-KITLV_-_105810_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Buggis%2C_the_Buginese_district_of_Singapore_-_circa_1900.tif.jpg",
    "BISHAN": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Bishan_Community_Club.JPG",
    "KAMPONGBARU": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/KITLV_-_105811_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Baru_at_Singapore_-_circa_1890.tif/lossy-page1-960px-KITLV_-_105811_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Baru_at_Singapore_-_circa_1890.tif.jpg",
}

SLIDES = [
    {"img": "KAMPONGBUGIS", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "BISHAN", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "KAMPONGBARU", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (4.42, 1), (25.23, 2)]
TOTAL_DURATION = 38.88  # real sentence-timing boundary for this post's opening hook
TIMING_JSON = "audio/group-chats-rebuilt-the-kampong-for-seniors.timing.json"

CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
