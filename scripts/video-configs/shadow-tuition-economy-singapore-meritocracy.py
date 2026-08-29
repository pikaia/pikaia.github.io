"""Video config for "The Shadow Tuition Economy: Singapore's $1.8 Billion
Bet Against Its Own Meritocracy" - Watch widget and main video.

The post's chart is a 4-bar series (S$680M in 2008 -> S$1.8B in 2023),
which compose_chart_frame() can't animate (single calendar-year line
only). It's rendered once to a static PNG by
scripts/render_shadow_tuition_chart.py ->
assets/images/shadow-tuition-spend.png and used here as a near-static
slide twice: the "$1.8 billion" headline and the walk-the-bars beat.

Images (2 post + the chart + 5 gallery):
  POPULAR    - a Popular bookstore, assessment-book aisles (post hero)
  MOE        - the Ministry of Education headquarters, Buona Vista - the
               "officially it doesn't exist" / "always described as
               optional" thread
  NUS        - University Hall, NUS - the meritocratic prize, and the
               second-language pass rule for university admission
  CHART      - the static tuition-spend PNG
  NANHUA     - encouragement posters by the exam hall, Nan Hua High, 2013
               - exam culture, "more chances to prove they have it"
  BOOKSHOP   - a second-hand bookshop in Bras Basah Complex - paying for
               study materials, the income-bracket spending gap
  DOVERCOURT - a 1970s Singapore classroom
  CHS_SCIENCE- the science building of The Chinese High School, 1952
  BRASBASAH  - Bras Basah Road, c.1906-1930, before it became the book
               district - "streets that grew into book districts"

13 slides, 207.8s. Aspect check (1280x720, ~1.44 cover threshold):
  POPULAR 3920x2204 (1.78)   -> cover, horizontal pan
  MOE 3776x3021 (1.25)       -> letterbox
  NANHUA 3264x2448 (1.33)    -> letterbox
  NUS 4080x3072 (1.33)       -> letterbox
  CHART 1280x720 (1.78)      -> letterbox (exact fit), near-zero zoom
  BOOKSHOP 3120x4681 (0.67)  -> letterbox (portrait)
  DOVERCOURT 1216x706 (1.72) -> cover, horizontal pan
  CHS_SCIENCE 600x595 (1.01) -> letterbox (low-res 1950s archival)
  BRASBASAH 3292x2128 (1.55) -> cover, horizontal pan
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static CHART slides read JERKY for the same reason.
Slide 2 (NANHUA) holds 23.2s - it covers one long single sentence that
can't be split at a real timing.json boundary; a slow zoom carries it.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "POPULAR": f"{_C}/8/83/Popular_Book_Store%2C_Singapore.jpg",
    "MOE": f"{_C}/1/1d/%28SGP-Singapore%29_Ministry_of_Education_Headquarters_2025-05-10.jpg",
    "NUS": f"{_C}/6/65/NUS_University_Hall%2C_Singapore.jpg",
    "CHART": "/assets/images/shadow-tuition-spend.png",
    "NANHUA": f"{_C}/0/02/Encouragement_posters_for_Secondary_4_students_near_the_examination_hall_put_up_by_the_Student_Council_of_Nan_Hua_High_School%2C_Singapore_-_20131028.jpg",
    "BOOKSHOP": f"{_C}/a/a2/Old_Bookshop_in_Bras_Basah_Complex.jpg",
    "DOVERCOURT": f"{_C}/9/9c/Class_at_Dover_Court_Preparatory_School%2C_Singapore.png",
    "CHS_SCIENCE": f"{_C}/d/da/Science_building_of_CHS_in_50s.JPG",
    "BRASBASAH": f"{_C}/thumb/8/8a/Singapore._Brass_Bassa_Road.%2C_KITLV_1404985.tiff/lossy-page1-1280px-Singapore._Brass_Bassa_Road.%2C_KITLV_1404985.tiff.jpg",
}

CREDITS = {
    "CHART": ("Tuition-spend chart by Lesser Known Singapore, from the Household "
              "Expenditure Survey figures cited in the post"),
}

SLIDES = [
    {"img": "POPULAR", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"},
    {"img": "MOE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "NANHUA", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "NUS", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "BOOKSHOP", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "DOVERCOURT", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"},
    {"img": "NANHUA", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "MOE", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "NUS", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "CHS_SCIENCE", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "BRASBASAH", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"},
    {"img": "CHART", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real values from audio/shadow-tuition-economy-singapore-meritocracy.timing.json.
# Every point is a real sentence start.
#   0  title + s1   MOE never made tuition a requirement for anything
#   1  s2      officially it doesn't exist / no school asks
#   2  s3      and yet: S$1.8B in 2023, seven in ten students, the single
#              largest discretionary education expense
#   3  s4-5    a system built on merit let a shadow industry become a
#              lever / the growth traces a straight line
#   4  s6      CHART - S$680M (2008) -> 1.1 -> 1.4 -> 1.8B (2023), more
#              than doubling in fifteen years
#   5  s7-8    the money isn't spread evenly / S$162.60 a month at the top
#              vs S$36.30 at the bottom
#   6  s9      the gap in miniature: merit measures who can afford more
#              shots at demonstrating it
#   7  s10-11  tuition doesn't replace merit / it decides who gets more
#              chances to prove they have it
#   8  s12-13  official messaging never captures it / MOE has always
#              called tuition optional
#   9  s14     but a second-language pass rule for university admission
#              still exists - "optional" reads differently by income
#   10 s15     opting out feels safe only if being wrong is cheap
#   11 s16     the infrastructure - classrooms, book aisles, the streets
#              that grew into book districts - predates the industry
#   12 s17     CHART - close: the meritocracy measures which families can
#              buy more attempts; a shadow economy it never had to own
SCHEDULE = [
    (0.0, 0), (14.125, 1), (22.725, 2), (45.95, 3), (63.55, 4),
    (90.5, 5), (108.85, 6), (124.575, 7), (134.35, 8), (147.925, 9),
    (167.7, 10), (174.0, 11), (186.075, 12),
]
TOTAL_DURATION = 207.8
TIMING_JSON = "audio/shadow-tuition-economy-singapore-meritocracy.timing.json"
