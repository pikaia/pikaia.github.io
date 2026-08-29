"""Video config for "The Fine City's Fine Print: Which of Singapore's
Famous Rules Still Stick" - Watch widget and main video.

The post's chart is a horizontal rule-timeline (five rules, each a bar
from its start year to today, colour-coded by outcome), which
compose_chart_frame() can't animate (line charts only). It's rendered
once to a static PNG by scripts/render_fine_city_timeline.py ->
assets/images/fine-city-timeline.png and used here as a near-static
slide - twice: once at the "famous ones turned out soft" thesis, once
at the closing summary.

Images (all 8 in the post + gallery):
  MRT_SIGN   - the MRT multi-prohibition sign (post hero) - the "fine
               city" reputation; also bookends the littering opener/close
  GUM        - dental gum on sale at a Singapore pharmacy - the gum ban
               and its 2004 therapeutic-gum carve-out
  PINKDOT    - a Pink Dot crowd at Hong Lim Park - the Section 377A push
  LKY        - Lee Kuan Yew, 1965 - the 1968 "Keep Singapore Clean" law
  KAMPONG    - a Braddell Hill kampong, c.1964 - the conditions that law
               was written for
  VENDOR     - a Singapore street vendor, 1973-74 - informal street life
               the public-order campaigns spent decades regulating
  PARLIAMENT - Parliament House, 2023 - where 377A was repealed in 2022
  SPEAKERS   - the Speakers' Corner sign - the venue for Pink Dot / the
               sustained public pressure behind the repeal
  TIMELINE   - the static rule-timeline PNG

15 slides, 274.325s. Aspect check (1280x720, ~1.44 cover threshold):
  MRT_SIGN 804x1024 (0.79)   -> letterbox
  GUM 988x669 (1.48, low-res)-> letterbox
  LKY 646x861 (0.75)         -> letterbox
  KAMPONG 973x713 (1.37)     -> letterbox
  TIMELINE 1280x720 (1.78)   -> letterbox (exact fit), near-zero zoom
  PINKDOT 4000x3000 (1.33)   -> cover, horizontal pan across the crowd
  PARLIAMENT 4624x3468 (1.33)-> cover, gentle pan
  SPEAKERS 2560x1920 (1.33)  -> cover, slight pan
  VENDOR 5841x3894 (1.50)    -> cover, horizontal pan
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static TIMELINE slides read JERKY for the same
reason.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "MRT_SIGN": f"{_C}/d/dd/Singapore_MRT_Fines.jpg",
    "GUM": f"{_C}/5/52/Chewinggumpharmacysg.jpg",
    "PINKDOT": f"{_C}/6/62/Crowd_at_pink_dot_16.jpg",
    "LKY": f"{_C}/1/13/Lee_Kuan_Yew%2C_1965_%28cropped%29.jpg",
    "KAMPONG": f"{_C}/8/81/Kampong_in_Braddell_Hill_Singapore_about_1964.jpg",
    "VENDOR": f"{_C}/e/ef/Singapore-Street_Vendor_1973-74-WUS08155.jpg",
    "PARLIAMENT": f"{_C}/0/01/Parliament_House%2C_Singapore%2C_August_2023.jpg",
    "SPEAKERS": f"{_C}/9/9b/Speakers%27_Corner_sign%2C_Singapore_-_20050906.jpg",
    "TIMELINE": "/assets/images/fine-city-timeline.png",
}

CREDITS = {
    "TIMELINE": "Rule timeline by Lesser Known Singapore, compiled from the post's cited sources",
}

SLIDES = [
    {"img": "MRT_SIGN", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "GUM", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "MRT_SIGN", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "TIMELINE", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "GUM", "type": "letterbox", "zoom": [1.1, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "VENDOR", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.34, 0.5), (0.5, 0.5), (0.64, 0.5)], "ease": "ease-in-out"},
    {"img": "KAMPONG", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "LKY", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "VENDOR", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.66, 0.5), (0.5, 0.5), (0.34, 0.5)], "ease": "ease-out"},
    {"img": "MRT_SIGN", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "PINKDOT", "type": "cover", "zoom": [1, 1.04, 1.08], "pan": [(0.40, 0.5), (0.5, 0.5), (0.58, 0.5)], "ease": "linear"},
    {"img": "PARLIAMENT", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.40, 0.55), (0.5, 0.5), (0.60, 0.45)], "ease": "ease-in-out"},
    {"img": "SPEAKERS", "type": "cover", "zoom": [1.08, 1.04, 1], "pan": [(0.58, 0.5), (0.5, 0.5), (0.42, 0.5)], "ease": "ease-out"},
    {"img": "TIMELINE", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "MRT_SIGN", "type": "letterbox", "zoom": [1.13, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real values from audio/fine-city-fine-print-singapore-rules-still-stick.timing.json.
# Every point is a real sentence start.
#   0  title + s1     Tang Bo Xiang, S$2,500, Corrective Work Order
#   1  s2-4    13th conviction / no joke about littering / gum ban gentler
#   2  s5      strictest vs five-figure fines - different lists
#   3  s6-7    TIMELINE - "the famous ones turned out to be the soft ones"
#   4  s8-9    chewing never illegal / 2004 therapeutic-gum carve-out
#   5  s10-11  the long hair ban / airport haircuts / Led Zeppelin
#   6  s12-13  enforcement faded / lifted in the 1990s / gone 3 decades
#   7  s14-15  "the boring ones" / 1968 EPHA / Keep Singapore Clean / LKY
#   8  s16     repeat littering S$10,000 / NEA ~3,000 fines in Q1 2026
#   9  s17-18  flush rule S$1,000 / plainclothes NEA spot checks
#   10 s19     "the one genuinely serious rule that fits neither pattern"
#   11 s20     Section 377A: 1938 -> repealed Nov 2022, effective Jan 2023
#   12 s21     formally off the books, after sustained public pressure
#   13 s22-24  TIMELINE - reputation vs reality / relaxed vs still fining
#   14 s25     close - the reputation rode on the two softest rules
SCHEDULE = [
    (0.0, 0), (24.2, 1), (44.075, 2), (55.825, 3), (68.725, 4),
    (91.3, 5), (110.575, 6), (125.75, 7), (144.325, 8), (161.075, 9),
    (183.125, 10), (188.375, 11), (211.825, 12), (231.275, 13), (254.425, 14),
]
TOTAL_DURATION = 274.325
TIMING_JSON = "audio/fine-city-fine-print-singapore-rules-still-stick.timing.json"
