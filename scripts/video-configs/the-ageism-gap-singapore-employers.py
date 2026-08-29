"""Video config for "The Ageism Gap: What Singapore Employers Say vs. What
They Do" - Watch widget and main video.

The post's chart is a 3-category horizontal bar comparison (52% / 65% /
22%), which compose_chart_frame() can't animate (it only does a
time-series line). It's rendered once to a static PNG by
scripts/render_ageism_hire_chart.py -> assets/images/the-ageism-gap-hire-chart.png
and used here as a normal (near-static) image slide at the survey beat.

6 of the post's 8 photos are used (the Jek Yeun Thong 1964 portrait is
216px wide, and the S. Rajaratnam c.1940s photo predates his labour
portfolio by decades - both stay gallery-only):

  SKYLINE    - Raffles Place skyline (post hero) - the CBD / the resident
               workforce, a quarter of it now 55+
  MOL        - former Ministry of Labour Building (1928), now the Family
               Justice Courts - the policy apparatus "on paper"
  MOM        - the current Ministry of Manpower building - the retirement
               and re-employment ages
  CPF_OLD    - the CPF Building on Robinson Road (demolished 2015) - the
               retirement savings older jobseekers depend on
  NTUC       - the NTUC Centre - one of the three partners behind the
               2023 employer survey
  DEVAN_NAIR - Devan Nair, 1953 - "the ministers and institutions that
               built it"
  CHART      - the static hire-chart PNG (the survey payoff)

13 slides, 252.25s. This is an abstract present-day topic with little
dedicated imagery, so photos are reused with bookend zoom/ease the way
the amah post handles the same problem; SKYLINE recurs 4x as the neutral
CBD backdrop, each with a distinct cover-pan path.

Aspect check (1280x720, ~1.44 cover threshold):
  SKYLINE 3840x2400 (1.60)  -> cover, gentle pan (skyline has headroom)
  MOL 1920x1080 (1.78)      -> cover, horizontal pan
  MOM 1600x1200 (1.33)      -> letterbox
  CPF_OLD 1200x1600 (0.75)  -> letterbox
  NTUC 1200x1600 (0.75)     -> letterbox
  DEVAN_NAIR 703x938 (0.75) -> letterbox
  CHART 1280x720 (1.78)     -> letterbox (exact fit), near-zero zoom
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5). The near-static CHART slide reads JERKY for the same reason.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SKYLINE": f"{_C}/1/1e/Singapore_Skyline_Raffles_Place.jpg",
    "MOL": f"{_C}/a/a3/Former_Ministry_of_Labour_Building%2C_October_2025.jpg",
    "MOM": f"{_C}/9/97/Ministry_of_Manpower.JPG",
    "CPF_OLD": f"{_C}/6/63/CPF_Building%2C_Jan_06.JPG",
    "NTUC": f"{_C}/a/ae/NTUC_Centre.JPG",
    "DEVAN_NAIR": f"{_C}/f/f6/Devan_Nair%2C_1953_%283x4_crop%29.png",
    "CHART": "/assets/images/the-ageism-gap-hire-chart.png",
}

SLIDES = [
    {"img": "SKYLINE", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.30, 0.52), (0.50, 0.50), (0.70, 0.48)], "ease": "ease-in-out"},
    {"img": "MOL", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.35, 0.50), (0.50, 0.50), (0.62, 0.50)], "ease": "ease-in-out"},
    {"img": "MOM", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CPF_OLD", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "SKYLINE", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.68, 0.55), (0.50, 0.50), (0.34, 0.45)], "ease": "ease-out"},
    {"img": "NTUC", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "MOL", "type": "cover", "zoom": [1.08, 1.04, 1], "pan": [(0.65, 0.50), (0.50, 0.50), (0.38, 0.50)], "ease": "ease-out"},
    {"img": "MOM", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "SKYLINE", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.60, 0.35), (0.50, 0.50), (0.40, 0.62)], "ease": "ease-in-out"},
    {"img": "CPF_OLD", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "DEVAN_NAIR", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "SKYLINE", "type": "cover", "zoom": [1.14, 1.07, 1.0], "pan": [(0.50, 0.50), (0.50, 0.50), (0.50, 0.50)], "ease": "linear"},
]

# Real values from audio/the-ageism-gap-singapore-employers.timing.json.
# Every point is a real sentence start.
#   0  title + s1  the 61-year-old in the CBD
#   1  s2-3   policy on paper / resumes go nowhere
#   2  s4     retirement age 63 -> 64 -> 65 and 70
#   3  s5     a quarter of the workforce 55+, thinner CPF
#   4  s6     senior employment rates 70.8% / 31.5%
#   5  s7-8   ask employers directly / the 2023 survey, 52%
#   6  s9-11  CHART - split by existing older staff / 3x more likely /
#             familiarity, not principle, behind the topline number
#   7  s12-14 the 52% hides / complaint data / TAFEP 77 a year
#   8  s15-16 age discrimination #1 by 2023 / top hiring barrier
#   9  s17-18 not deliberate / managers' unconscious assumptions
#   10 s19    the quieter bias, alongside official messaging
#   11 s20-21 none of it appeared overnight / built over decades by a
#             succession of officials and the institutions they built
#   12 s22    why it matters today
SCHEDULE = [
    (0.0, 0), (22.775, 1), (42.875, 2), (60.35, 3), (77.05, 4),
    (93.95, 5), (115.0, 6), (143.4, 7), (169.125, 8), (187.55, 9),
    (208.375, 10), (218.775, 11), (229.5, 12),
]
TOTAL_DURATION = 252.25
TIMING_JSON = "audio/the-ageism-gap-singapore-employers.timing.json"

# Credit lines for slides whose image isn't a captioned Commons file, read
# by scripts/stage_youtube_text.py for the YouTube description (keyed by
# IMAGES key). CHART is rendered by this site, not sourced.
CREDITS = {
    "CHART": ("Employer-hiring bar chart by Lesser Known Singapore, from the NTUC, "
              "Singapore University of Social Sciences & Tsao Foundation 2023 employer survey"),
}
