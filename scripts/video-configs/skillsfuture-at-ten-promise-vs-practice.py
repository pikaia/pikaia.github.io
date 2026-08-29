"""Video config for "SkillsFuture at Ten: The Promise Still Outruns the
Practice" - Watch widget and main video.

The post's chart is a two-series line comparison (2015 Opening Credit vs
2020 top-up) on a "years since the scheme began" x-axis, which
compose_chart_frame() can't animate (single calendar-year line only).
It's rendered once to a static PNG by
scripts/render_skillsfuture_uptake_chart.py ->
assets/images/skillsfuture-uptake.png and used here as a near-static
slide - three times: the slow-build numbers, the top-up's stall, and
the closing summary.

Images (all 7 in the post + gallery):
  PARLIAMENT     - Parliament House (post hero) - the Jan 2026 exchange
                   over unclaimed credits
  OLD_PARLIAMENT - Old Parliament House (1827) - "parliamentary questions
                   have always been this institution's business"
  THARMAN        - Tharman Shanmugaratnam, official 2023 portrait - chaired
                   the SkillsFuture Council behind the 2015 launch
  ITE_COLLEGE    - ITE College Central - where SkillsFuture was announced
  ITE_HQ         - ITE headquarters, 2006 - the older training system
  FESTIVAL       - a 2018 SkillsFuture Festival - the push for sign-ups
  JURONG         - Jurong Industrial Estate signs, 1964 - workforce
                   training as a matter of state, five decades earlier
  CHART          - the static uptake-comparison PNG

14 slides, 289.1s. Aspect check (1280x720, ~1.44 cover threshold):
  PARLIAMENT 1024x768 (1.33)     -> letterbox
  OLD_PARLIAMENT 1600x1200 (1.33)-> letterbox
  THARMAN 2096x2911 (0.72)       -> letterbox
  ITE_COLLEGE 4283x3209 (1.33)   -> letterbox
  ITE_HQ 1600x1200 (1.33)        -> letterbox
  FESTIVAL 960x720 (1.33)        -> letterbox
  CHART 1280x720 (1.78)          -> letterbox (exact fit), near-zero zoom
  JURONG 4917x3253 (1.51)        -> cover, horizontal pan across the signs
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static CHART slides read JERKY for the same reason.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "PARLIAMENT": f"{_C}/8/89/Parliament_House_Singapore.jpg",
    "OLD_PARLIAMENT": f"{_C}/7/7c/Old_Parliament_House%2C_Singapore%2C_Feb_06.JPG",
    "THARMAN": f"{_C}/thumb/8/84/Tharman_Shanmugaratnam_Official_photo_2023.tif/lossy-page1-1280px-Tharman_Shanmugaratnam_Official_photo_2023.tif.jpg",
    "ITE_COLLEGE": f"{_C}/2/2b/ITE_College_Central.jpg",
    "ITE_HQ": f"{_C}/4/42/Institute_of_Technical_Education_Headquarters%2C_Nov_06.JPG",
    "FESTIVAL": f"{_C}/3/3c/2018-skillsfuture-festival.jpg",
    "JURONG": f"{_C}/0/04/Signs_pointing_to_Jurong_Industrial_Estate_in_Singapore_June_1964.jpg",
    "CHART": "/assets/images/skillsfuture-uptake.png",
}

CREDITS = {
    "CHART": ("SkillsFuture uptake chart by Lesser Known Singapore, from MOE parliamentary "
              "replies and SkillsFuture Singapore figures cited in the post"),
}

SLIDES = [
    {"img": "PARLIAMENT", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OLD_PARLIAMENT", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "PARLIAMENT", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "THARMAN", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ITE_COLLEGE", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "FESTIVAL", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "FESTIVAL", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "JURONG", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.34, 0.5), (0.5, 0.5), (0.64, 0.5)], "ease": "ease-in-out"},
    {"img": "ITE_HQ", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "OLD_PARLIAMENT", "type": "letterbox", "zoom": [1.13, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "PARLIAMENT", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.02, 1.05], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real values from audio/skillsfuture-at-ten-promise-vs-practice.timing.json.
# Every point is a real sentence start.
#   0  title + s1-2  the $500 top-up expired end-2025 / sat since 2020
#   1  s3-4    seven in ten let it lapse / an MP asks Parliament (Jan 2026)
#   2  s5      the Ministry: not transferable, "own lifelong learning"
#   3  s6-7    rewind ten years / 2015 launch, Tharman Shanmugaratnam
#   4  s8      every citizen at 25 got an Opening Credit, no expiry
#   5  s9-10   a slow, patient build / 126,000 in the first year
#   6  s11-13  CHART - 20% by 2019, 29% by 2022 / employers doubled
#   7  s14     10th anniversary: more than half, after a full decade
#   8  s15-16  a second, unplanned purpose / pitched as workforce policy
#   9  s17-18  seniors in AI classes / less a career tool, more trying
#             something new
#   10 s19-20  CHART - the 2020 top-up, this time with a five-year deadline
#   11 s21-23  it didn't work: 26% by 2024, ~30% by Sep 2025
#   12 s24     the deadline held; no extension, no transfer
#   13 s25-26  CHART - closing: a quieter purpose, but the take-up gap
#             never closed - it just moved
SCHEDULE = [
    (0.0, 0), (26.75, 1), (49.725, 2), (63.7, 3), (87.425, 4),
    (98.65, 5), (109.1, 6), (137.25, 7), (154.225, 8), (180.925, 9),
    (208.55, 10), (228.125, 11), (247.2, 12), (260.575, 13),
]
TOTAL_DURATION = 289.1
TIMING_JSON = "audio/skillsfuture-at-ten-promise-vs-practice.timing.json"
