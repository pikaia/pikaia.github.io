"""Video config for "The Travel Bug: How Travelling Overseas Stopped Being
Rare" - Watch widget and main video.

Images: the 7 already in the post/hero + 6 from the companion gallery, of
which 10 are used here (the 3 unused gallery shots - MSA at Zurich detail,
the two later SIA-at-Changi frames, the cruise ship - stay gallery-only).
1 CHART appears 3 times, drawn at a narration-paced rate each time:

  ST1955     - Straits Times front page, 21 Aug 1955 (Paya Lebar opens) -
               the once-in-a-lifetime era the opening describes
  MSA_707    - Malaysia-Singapore Airlines B707, Zurich 1972 - the formal
               full-service carrier
  CHANGI_HALL- Changi T1 departure hall (post front matter + hero) - the
               ordinary, crowded present
  CHANGI_1982- SIA 727 + Garuda DC-10, Changi's first year, 1982
  TIGERAIR   - Tigerair A319 arriving at Bangkok
  JETSTAR    - Jetstar Asia A320 at Osaka, 2018
  SCOOT      - Scoot Boeing 787 at Taipei, 2026
  PAYALEBAR_TOWER - Paya Lebar control tower + terminal, c.1969-71
  SAS_CARAVELLE   - SAS Caravelle on the Paya Lebar tarmac, c.1969-71
  JEWEL      - the Rain Vortex at Jewel Changi - travel as a day out
  CHART      - the post's own air-departures line (1997-2025), 3 slides:
               A (s4-6)   draws the clean 1997->2019 growth story
               B (s12)    redraws, lingering on the 2003 SARS dip
               C (s17-18) recaps to 2019, drops through the 2020-21
                          COVID cliff, then sweeps to the 2025 record

15 slides. Aspect check (1280x720, ~1.44 cover threshold):
  ST1955 1000x1398 (0.72, portrait)      -> letterbox
  MSA_707 734x404 (1.82)                 -> letterbox (low-res, zoom only)
  CHANGI_HALL 1600x1200 (1.33)           -> letterbox
  CHANGI_1982 1200x827 (1.45)            -> letterbox
  PAYALEBAR_TOWER 1644x1030 (1.60)       -> letterbox
  JEWEL 5475x3650 (1.50, tall waterfall) -> letterbox (no vertical crop)
  TIGERAIR 2670x1519 (1.76)              -> cover, gentle pan
  SAS_CARAVELLE 1650x850 (1.94)          -> cover, horizontal pan
  JETSTAR 2338x960 (2.44)                -> cover, horizontal pan
  SCOOT 5891x3311 (1.78)                 -> cover, gentle pan
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5). The 3 CHART slides read JERKY for the same documented reason.
CHART C holds ~28.5s - acceptable for a moving chart per
report_slide_gaps' own docstring, not a static hold to break up.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "ST1955": f"{_C}/a/a8/ST21August1955.jpg",
    "MSA_707": f"{_C}/0/0d/Malaysia-Singapore_Airlines_B707_at_Zurich_1972.jpg",
    "CHANGI_HALL": f"{_C}/0/05/Changi_Airport%2C_Terminal_1%2C_Departure_Hall.JPG",
    "CHANGI_1982": f"{_C}/2/29/Singapore_Airlines_Boeing_727_Martin.jpg",
    "TIGERAIR": f"{_C}/d/d8/9V-TRB_%2827682638542%29.jpg",
    "JETSTAR": f"{_C}/6/63/9V-JSU_%2845258845642%29.jpg",
    "SCOOT": f"{_C}/2/2f/Scoot_Boeing_787_9V-OJG_Taiwan_Taoyuan_2026_%2801%29.jpg",
    "PAYALEBAR_TOWER": f"{_C}/d/d3/Singapore_International_Airport_control_tower_and_terminal_building%2C_photographed_February_1969_%C3%97_July_1971.jpg",
    "SAS_CARAVELLE": f"{_C}/9/9a/SAS_airliner_at_Singapore_International_Airport%2C_photographed_February_1969_%C3%97_July_1971.jpg",
    "JEWEL": f"{_C}/1/14/HSBC_Rain_Vortex_and_Shiseido_Forest_Valley.jpg",
}

# The post's own chart data - ICA outbound air departures of Singapore
# residents, annual, in millions (data.gov.sg). Same series as the post's
# inline SVG, including the 2020-21 COVID cliff (8.58M -> 1.22M -> 0.53M)
# and the record 8.85M in 2025.
AIR_DEPARTURES = [
    (1997, 2.39), (1998, 2.20), (1999, 2.32), (2000, 2.56), (2001, 2.48),
    (2002, 2.62), (2003, 2.34), (2004, 3.00), (2005, 3.44), (2006, 3.74),
    (2007, 4.15), (2008, 4.85), (2009, 4.96), (2010, 5.62), (2011, 6.08),
    (2012, 6.49), (2013, 6.96), (2014, 7.16), (2015, 7.37), (2016, 7.77),
    (2017, 8.10), (2018, 8.36), (2019, 8.58), (2020, 1.22), (2021, 0.53),
    (2022, 4.22), (2023, 7.87), (2024, 8.84), (2025, 8.85),
]

_CHART_BASE = {
    "type": "chart",
    "data": AIR_DEPARTURES,
    "x_range": (1997, 2025),
    "y_range": (0, 10),
    "y_tick_step": 2,
    "y_tick_format": "{:.0f}M",
    "value_format": "{:.2f}M trips",
    "title": "Singapore resident departures by air, annual (1997-2025)",
    "annotations": [
        (1997, 2.39, "2.39M", "above"),
        (2021, 0.53, "0.53M (2021)", "below"),
        (2025, 8.85, "8.85M", "above"),
    ],
}

CHART_A = {
    **_CHART_BASE,
    # s4 "the actual numbers back this up" / s5 "immigration data ... shows
    # the shift clearly" / s6 "two things happened". First look: draw the
    # clean 1997->2019 growth only, so the COVID cliff is held back for
    # CHART C. Hold at 2019 through s6.
    "year_checkpoints": [(43.85, 1997), (53.5, 2019), (59.45, 2019)],
}

CHART_B = {
    **_CHART_BASE,
    # s12 "you can see both the SARS-driven dip in 2003 and this
    # budget-airline effect ... departures barely move until 2004, then
    # climb almost every year after." Redraw from 1997, linger 2003->2004,
    # then climb to 2019 and hold.
    "year_checkpoints": [
        (113.825, 1997), (117.5, 2003), (119.5, 2004),
        (125.0, 2019), (126.55, 2019),
    ],
}

CHART_C = {
    **_CHART_BASE,
    # s17 "the 2020 to 2021 collapse ... borders shut for COVID-19 ... the
    # exception that proves the point" / s18 "the recovery by 2023 - and
    # the record set in 2025". Quick recap draw to 2019, drop through the
    # cliff as "2020 ... to 2021" is said, hold at the 0.53M trough, then
    # sweep the recovery so "8.85M" lands on "the record set in 2025".
    "year_checkpoints": [
        (174.125, 1997), (180.5, 2019), (183.5, 2020), (186.0, 2021),
        (195.0, 2021), (198.5, 2023), (202.625, 2025),
    ],
}

SLIDES = [
    {"img": "ST1955", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MSA_707", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "CHANGI_HALL", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    CHART_A,
    {"img": "CHANGI_1982", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "TIGERAIR", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.36, 0.52), (0.5, 0.5), (0.64, 0.48)], "ease": "linear"},
    {"img": "JETSTAR", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.30, 0.5), (0.5, 0.5), (0.70, 0.5)], "ease": "ease-in-out"},
    {"img": "SCOOT", "type": "cover", "zoom": [1, 1.07, 1.14], "pan": [(0.44, 0.46), (0.52, 0.5), (0.60, 0.54)], "ease": "ease-in-out"},
    {"img": "JETSTAR", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.70, 0.5), (0.5, 0.5), (0.34, 0.5)], "ease": "ease-out"},
    CHART_B,
    {"img": "PAYALEBAR_TOWER", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SAS_CARAVELLE", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.34, 0.5), (0.5, 0.5), (0.62, 0.5)], "ease": "ease-in-out"},
    {"img": "CHANGI_HALL", "type": "letterbox", "zoom": [1.14, 1.07, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    CHART_C,
    {"img": "JEWEL", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
]

# Real values from
# audio/the-travel-bug-rise-of-travelling-among-singaporeans.timing.json.
# Every point is a real sentence start. Slide 0 holds through the title +
# s1; CHART A covers s4-6, CHART B covers s12, CHART C covers s17-18.
SCHEDULE = [
    (0.0, 0), (17.95, 1), (25.65, 2), (43.85, 3), (59.45, 4),
    (78.45, 5), (83.275, 6), (94.175, 7), (100.925, 8), (113.825, 9),
    (126.55, 10), (143.325, 11), (156.85, 12), (174.125, 13), (202.625, 14),
]
TOTAL_DURATION = 221.225
TIMING_JSON = "audio/the-travel-bug-rise-of-travelling-among-singaporeans.timing.json"
