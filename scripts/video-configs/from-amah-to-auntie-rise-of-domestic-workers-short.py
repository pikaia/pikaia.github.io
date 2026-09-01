"""Video config for the amah post's YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-43.95s, sentences 0-4) - the
amah/majie era, its 1970s decline as women moved into factories and
offices, and the setup line "Singapore's households still needed the
help. It just had to come from somewhere else." Ends on that cliffhanger
at a real sentence boundary, before the 1978 scheme is named.

3 slides, all from the post's own images. SERVANTS (colonial domestic
servants, c.1900) carries the amah era; DHOBY (washing field, c.1880)
the older service economy fading; HERO (Lucky Plaza) is the visual
pivot under "somewhere else" - the modern answer, un-narrated yet.

Vertical 1080x1920 target: SERVANTS (1.362), DHOBY (1.365) and HERO
(1.333) are all far below the cover threshold at this aspect, so all
three are letterbox (blurred-bg zoom, zero pan - reads JERKY in
--check-only, the documented false positive).
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "SERVANTS": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/KITLV_-_29190_-_Ten_domestic_servants_of_various_ethnic_origins%2C_each_with_an_object_relating_tot_their_task%2C_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_29190_-_Ten_domestic_servants_of_various_ethnic_origins%2C_each_with_an_object_relating_tot_their_task%2C_Singapore_-_circa_1900.tif.jpg",
    "DHOBY": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/KITLV_-_103979_-_Washing_and_bleaching_field%2C_Singapore_-_circa_1880.tif/lossy-page1-1280px-KITLV_-_103979_-_Washing_and_bleaching_field%2C_Singapore_-_circa_1880.tif.jpg",
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/0/04/Lucky_Plaza%2C_Orchard_Road%2C_Singapore.jpg",
}

SLIDES = [
    {"img": "SERVANTS", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "DHOBY", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
]

# Real sentence boundaries from the post's timing.json: slide 0 covers
# the title + sentence 1, slide 1 sentence 2, slide 2 sentences 3-4.
SCHEDULE = [(0.0, 0), (18.9, 1), (37.475, 2)]
TOTAL_DURATION = 43.95  # end of sentence 4, "...come from somewhere else."
TIMING_JSON = "audio/from-amah-to-auntie-rise-of-domestic-workers.timing.json"

BURN_CAPTIONS = True
