"""Shorts config for the Jalan Payoh Lai / Kangkar post.

Excerpt: the opening hook, sentences 0-8 (0 -> 55.675s, a real sentence
boundary in the re-run timing.json). Born in 1960 on Jalan Payoh Lai, a
twenty-minute walk to school and church, with a favourite shortcut down
a backlane called Holy Innocents' Lane beside Montfort School - a name
that turned out to trace back to a cluster of Catholic schools, and a
lane that, with the cemetery beside it, is gone from the map.

3 slides: the church-and-school-and-town aerial -> the old Holy
Innocents' English School facade -> the old Nativity church. All three
archive photos are used by permission of the Chancery Archives (see
CREDITS) for this post/video only.
"""

WIDTH, HEIGHT = 1080, 1920

_A = "/assets/images/chancery"

IMAGES = {
    "AERIAL": f"{_A}/nativity-aerial.jpg",
    "HIESFACADE": f"{_A}/hies-facade-1910s.jpg",
    "MARIANSTATUE": f"{_A}/nativity-old-marian-statue.jpg",
}

CREDITS = {
    "AERIAL": ("Aerial shot of the Church of the Nativity of the Blessed Virgin Mary, Hougang, and its "
               "surrounding complex, undated. Rev. Fr. Rene Nicolas Collection, courtesy of the Chancery "
               "Archives, Roman Catholic Archdiocese of Singapore."),
    "HIESFACADE": ("Black and white photograph of the Holy Innocents' English School building facade, "
                   "c. 1910s. Rev. Fr. Rene Nicolas Collection, courtesy of the Chancery Archives, Roman "
                   "Catholic Archdiocese of Singapore."),
    "MARIANSTATUE": ("Black and white photograph of the outdoor statue of the Blessed Virgin Mary, "
                     "Church of the Nativity of the Blessed Virgin Mary, Hougang, Singapore, undated. "
                     "Rev. Fr. Rene Nicolas Collection, courtesy of the Chancery Archives, Roman Catholic "
                     "Archdiocese of Singapore."),
}

SLIDES = [
    {"img": "AERIAL", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HIESFACADE", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "MARIANSTATUE", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the re-run timing.json: s5 at 28.475, s8 at 49.325.
SCHEDULE = [(0.0, 0), (28.475, 1), (49.325, 2)]
TOTAL_DURATION = 55.675
TIMING_JSON = "audio/jalan-payoh-lai-kangkar-montfort-nativity-church.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt. Caption size/position come from the
# DEFAULT_CAPTION_* module constants (small outlined white text, no box).
BURN_CAPTIONS = True
