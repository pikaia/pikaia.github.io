"""Video config for "From Amah to Auntie: How Singapore Came to Rely on
Foreign Domestic Workers" - Watch widget and main video.

Strict parity with the post: the only visuals used are the 6 elements
already in the post/gallery (confirmed with Chris 2026-08-28 - no new
images sourced, since Wikimedia Commons has effectively nothing for
amahs/majie). 5 photos + 1 CHART slide:

  HERO      - Lucky Plaza, Orchard Road (post front matter + hero) - the
              modern foreign-domestic-worker system
  SERVANTS  - KITLV, ten domestic servants of colonial Singapore, c.1900
  DHOBY     - KITLV, washing/bleaching field at Dhoby Ghaut, c.1880
  TAILOR    - KITLV, itinerant tailor, c.1900 (portrait)
  KNIFE     - KITLV, itinerant knife sharpeners, c.1900
  CHART     - the post's own FDW-count line (2009-2025), drawn as a
              "chart" slide animating itself

12 slides. The 4 colonial-trade photos + Lucky Plaza carry the amah ->
scheme -> present-day arc, each reused once with a different zoom/ease
for a bookend feel; the CHART slide (sentences 7-9) is the data payoff,
the line drawing itself while the narration walks the numbers. Closes
on Lucky Plaza again for the "amah gone, gap remains" line.

Aspect check (1280x720 target, ~1.44 cover threshold): every photo is
below it, so all photo slides are letterbox -
  HERO 2560x1920 (1.333), SERVANTS 1628x1195 (1.362),
  DHOBY 4740x3472 (1.365), TAILOR 1302x1846 (0.705, portrait),
  KNIFE 2993x2236 (1.339).
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
will flag them JERKY - the documented letterbox+zero-pan false positive
(pipeline doc section 5). The CHART slide reads JERKY for the same
documented reason. Slide 5 (CHART) holds ~30.4s, just over the gap
report's 30s line - acceptable for a moving chart per report_slide_gaps'
own docstring, not a static hold to break up.
"""

_THUMB = ("https://upload.wikimedia.org/wikipedia/commons/thumb/{h}/"
          "{n}.tif/lossy-page1-1280px-{n}.tif.jpg")

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/0/04/Lucky_Plaza%2C_Orchard_Road%2C_Singapore.jpg",
    "SERVANTS": _THUMB.format(h="3/3d", n="KITLV_-_29190_-_Ten_domestic_servants_of_various_ethnic_origins%2C_each_with_an_object_relating_tot_their_task%2C_Singapore_-_circa_1900"),
    "DHOBY": _THUMB.format(h="e/ec", n="KITLV_-_103979_-_Washing_and_bleaching_field%2C_Singapore_-_circa_1880"),
    "TAILOR": _THUMB.format(h="9/93", n="KITLV_-_29191_-_Klingalese_tailor_Singapore_-_circa_1900"),
    "KNIFE": _THUMB.format(h="e/e4", n="KITLV_-_50183_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Malaysian_knife_sharpeners_in_Singapore_-_circa_1900"),
}

# The post's own chart data - MOM Work Permit FDW count, year-end.
# 2014-2016 omitted (not in MOM's published annual series), same as the
# post's SVG; the drawn line runs straight 2013 -> 2017 across the gap.
FDW_DATA = [
    (2009, 196000), (2010, 201400), (2011, 206300), (2012, 209600),
    (2013, 214500), (2017, 246800), (2018, 253800), (2019, 261800),
    (2020, 247400), (2021, 246300), (2022, 268500), (2023, 286300),
    (2024, 301600), (2025, 316900),
]

# FDW as a % of Singapore's total foreign workforce (MOM year-end totals:
# 2009 1,053,500 ... 2019 1,427,500 ... 2025 1,635,700). The point of the
# second panel: the count nearly doubles while the share sits in a 16-20%
# band, ticking up to ~20.5% in 2020-21 as the total workforce fell faster
# than FDW numbers did during COVID.
FDW_PCT = [
    (2009, 18.6), (2010, 18.1), (2011, 17.2), (2012, 16.5), (2013, 16.2),
    (2017, 18.0), (2018, 18.3), (2019, 18.3), (2020, 20.1), (2021, 20.5),
    (2022, 18.9), (2023, 18.8), (2024, 19.1), (2025, 19.4),
]

SLIDES = [
    {"img": "SERVANTS", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "DHOBY", "type": "letterbox", "zoom": [1.13, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "TAILOR", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "HERO", "type": "letterbox", "zoom": [1.14, 1.07, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {
        "type": "chart",
        "data": FDW_DATA,
        "x_range": (2009, 2025),
        "y_range": (0, 350000),
        "y_tick_step": 50000,
        "y_tick_format": "{:,.0f}",
        "value_format": "{:,.0f}",
        "title": "Foreign domestic workers in Singapore, 2009-2025",
        "annotations": [
            (2009, 196000, "196,000", "above"),
        ],
        # Second panel: the share line. Same years / same 2014-16 gap;
        # animates on the same year_checkpoints as the count line above.
        "series2": {
            "data": FDW_PCT,
            "y_range": (0, 25),
            "y_tick_step": 5,
            "y_tick_format": "{:.0f}%",
            "value_format": "{:.0f}%",
            "label": "share of all foreign workers",
        },
        # Absolute post time -> chart year. The slide spans sentences
        # 7-9 (72.125-102.55s): sentence 7 sets up "the official numbers
        # from 2009 onward", so the line starts at 2009 and eases in;
        # sentence 9 ("grew from 1.05 to 1.64 million ... the whole way
        # through") is the sweep to the 2025 end.
        "year_checkpoints": [
            (72.125, 2009), (80.0, 2010.5), (102.55, 2025),
        ],
    },
    {"img": "KNIFE", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "TAILOR", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "SERVANTS", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "KNIFE", "type": "letterbox", "zoom": [1.13, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "DHOBY", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real values from audio/from-amah-to-auntie-rise-of-domestic-workers.timing.json.
# Every point is a real sentence start; slide 0 holds through the title
# + sentence 1, slide 2 covers the two short sentences 3-4, and the
# CHART (slide 5) holds through sentences 7-9.
SCHEDULE = [
    (0.0, 0), (18.9, 1), (37.475, 2), (43.95, 3), (59.825, 4),
    (72.125, 5), (102.55, 6), (121.625, 7), (140.9, 8), (152.125, 9),
    (169.475, 10), (184.425, 11),
]
TOTAL_DURATION = 205.275
TIMING_JSON = "audio/from-amah-to-auntie-rise-of-domestic-workers.timing.json"
