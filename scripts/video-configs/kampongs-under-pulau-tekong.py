"""Video config for "The Kampongs Under Tekong: What Every NS Recruit
Marches Through Without Knowing" - Watch widget and main video.

The post's chart is a 3-point population line on a non-numeric x-axis,
rendered once to a static PNG by scripts/render_tekong_population_chart.py
-> assets/images/tekong-population.png and used here as a near-static
slide (twice: the "small town" beat and the close).

The tekong-ferry personal photo in the post is deliberately NOT used
here - permission was for the blog, not a YouTube video.

Images:
  BMTC          - the Basic Military Training Centre on Tekong (post
                  hero) - the training island today; bookends the video
  LOCATOR       - the OSM map of Singapore with Tekong circled (map data
                  (c) OpenStreetMap contributors)
  BUANGKOK      - a wooden kampong house at Lorong Buangkok - what
                  Tekong's own kampongs once looked like
  BRANI         - a Malay fishing village on Pulau Brani, c.1900 - an
                  offshore island kampong like Tekong's
  MALAY1907     - a Malay kampong, Singapore, 1907
  KAMPONG_BARU  - Kampong Baru, c.1890
  KAMPONG_BUGGIS- Kampong Buggis (the Buginese quarter), c.1900
  BRADDELL      - a kampong at Braddell Hill, c.1964 - closest in time
                  to the Tekong villages, just before redevelopment
  CHART         - the static population PNG (4,169 -> ~8,000 -> 0)

16 slides, 258.9s. Aspect check (1280x720, ~1.44 cover threshold):
  BMTC 2816x2112 (1.33)          -> letterbox
  LOCATOR 1254x732 (1.71)        -> letterbox (near-16:9)
  KAMPONG_BARU 6582x5127 (1.28)  -> letterbox
  KAMPONG_BUGGIS 6495x5037 (1.29)-> letterbox
  BRADDELL 973x713 (1.37)        -> letterbox
  CHART 1280x720 (1.78)          -> letterbox (exact), near-zero zoom
  BUANGKOK 3648x2048 (1.78)      -> cover, gentle pan
  BRANI 4595x2988 (1.54)         -> cover, horizontal pan
  MALAY1907 4681x3039 (1.54)     -> cover, horizontal pan
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static CHART slides read JERKY for the same reason.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"
_TIF = (_C + "/thumb/{h}/{n}.tif/lossy-page1-1280px-{n}.tif.jpg")

IMAGES = {
    "BMTC": f"{_C}/d/dd/Pulau_Tekong_BMTC.JPG",
    "LOCATOR": "/assets/images/osm-pulau-tekong-locator.png",
    "BUANGKOK": f"{_C}/4/48/An_old_house_in_Lorong_Buangkok_Singapore.JPG",
    "BRANI": f"{_C}/0/06/Malay_-_village_Pulo_Brani_Singapore_%28NYPL_Hades-2359734-4044499%29.jpg",
    "MALAY1907": f"{_C}/d/da/Malay_village%2C_Singapore_%28NYPL_Hades-2359721-4044486%29.jpg",
    "KAMPONG_BARU": _TIF.format(h="9/91", n="KITLV_-_105811_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Baru_at_Singapore_-_circa_1890"),
    "KAMPONG_BUGGIS": _TIF.format(h="e/e7", n="KITLV_-_105810_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Kampong_Buggis%2C_the_Buginese_district_of_Singapore_-_circa_1900"),
    "BRADDELL": f"{_C}/8/81/Kampong_in_Braddell_Hill_Singapore_about_1964.jpg",
    "CHART": "/assets/images/tekong-population.png",
}

CREDITS = {
    "LOCATOR": "Locator map: map data © OpenStreetMap contributors",
    "CHART": "Population chart by Lesser Known Singapore, from the figures cited in the post",
}

SLIDES = [
    {"img": "BMTC", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "LOCATOR", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "BUANGKOK", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.36, 0.5), (0.5, 0.5), (0.62, 0.5)], "ease": "ease-in-out"},
    {"img": "BRANI", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.32, 0.52), (0.5, 0.5), (0.66, 0.48)], "ease": "ease-in-out"},
    {"img": "MALAY1907", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.66, 0.5), (0.5, 0.5), (0.34, 0.5)], "ease": "ease-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "KAMPONG_BARU", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "BRADDELL", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "BMTC", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "KAMPONG_BUGGIS", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "BMTC", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "BUANGKOK", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.64, 0.5), (0.5, 0.5), (0.36, 0.5)], "ease": "ease-out"},
    {"img": "LOCATOR", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "BMTC", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "BMTC", "type": "letterbox", "zoom": [1.13, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real values from audio/kampongs-under-pulau-tekong.timing.json.
# Every point is a real sentence start.
#   0  title + s1  marching through Selabin, Permatang, San Yong Kong
#   1  s2-3   not codenames / names of kampongs that stood on Tekong
#   2  s4-5   geography still labelled / settlement history goes back far
#   3  s6     migrants fleeing Pahang's civil war / Kampong Pahang, Batu Koyok
#   4  s7     the patchwork of kampongs / Malays, Teochews, Hakkas
#   5  s8-9   CHART - 4,169 in 1957 -> ~8,000 peak / "a small town"
#   6  s10-11 the town didn't survive / 1987 SAF takes the island
#   7  s12    surveyors assess houses, crops, livestock / payouts fell short
#   8  s13    resettled to the mainland / BMTC opens 1999
#   9  s14    the names survive only by bureaucratic convenience
#   10 s15    the SAF kept the kampong names as location labels
#   11 s16    18-year-olds in villages emptied to make room for them
#   12 s17-18 not done being remade / the 2025 below-sea-level polder
#   13 s19-20 more training land / 40 years on, the same purpose
#   14 s21    CHART - photographs of the kampongs are hard to come by
#   15 s22    close - a place nearly every man set foot on, none knew was home
SCHEDULE = [
    (0.0, 0), (21.075, 1), (34.625, 2), (48.1, 3), (66.6, 4),
    (85.025, 5), (102.675, 6), (119.05, 7), (132.4, 8), (150.35, 9),
    (157.15, 10), (171.0, 11), (185.225, 12), (209.275, 13), (227.675, 14),
    (237.475, 15),
]
TOTAL_DURATION = 258.9
TIMING_JSON = "audio/kampongs-under-pulau-tekong.timing.json"
