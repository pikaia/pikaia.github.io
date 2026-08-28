"""Video config for "The Doctor Who Shrank Singapore's Families, Then
Became Its President" (Benjamin Sheares) Watch widget and main video.

11 images total: HERO (his 1951 portrait, also front matter), KKH (1950
Kandang Kerbau Hospital group photo), UNESCO (a real 1973 "Stop at Two"
campaign display), ACADEMIC1940S/UNIMALAYA/YEOSEHGEOK (chronological
portraits, 1939-1951), ISTANA_WIDE/ISTANA_CLOSE (his presidency, two
frames from the same 1973-74 rooftop session), FAMILY (1946 family
portrait), TOMB (present-day Kranji grave). ST13May1981 (his death
front page) is gallery-only, not used in the main video - 11 images
across 15 photo slides (YEOSEHGEOK appears twice) is enough variety
without it.

15 photo slides cover the biographical narrative (sentences 0-14),
then a CHART slide (sentences 15-17) animates the post's own total-
fertility-rate line chart drawing itself while the narration discusses
the actual numbers - the post's data payoff, not just another photo.
Closes on TOMB (sentence 18, the reflective "remembered today, if at
all" line).

Aspect check (1280x720 target, 1.778): HERO (0.798), KKH (1.307), UNESCO
(1.352), ACADEMIC1940S (0.594), UNIMALAYA (0.794), YEOSEHGEOK (0.715),
FAMILY (0.811) are all letterbox - below the ~1.44 cover threshold this
project has used elsewhere (see the four-chopsticks post's config).
ISTANA_WIDE/ISTANA_CLOSE (1.500) and TOMB (1.777) are cover.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/0/03/Benjamin_Sheares%2C_1951.jpg",
    "KKH": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Kandang_Kerbau_Hospital_group_photo.jpg",
    "UNESCO": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Family_planning%2C_Singapore_-_UNESCO_-_PHOTO0000000902_0001.tiff/lossy-page1-1280px-Family_planning%2C_Singapore_-_UNESCO_-_PHOTO0000000902_0001.tiff.jpg",
    "ACADEMIC1940S": "https://upload.wikimedia.org/wikipedia/commons/2/22/Benjamin_Sheares_1940s_full_photo.jpg",
    "UNIMALAYA": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Benjamin_Sheares_at_the_University_of_Malaya_in_Singapore%2C_1951.jpg",
    "YEOSEHGEOK": "https://upload.wikimedia.org/wikipedia/commons/0/09/Benjamin_Sheares_and_Yeo_Seh_Geok%2C_1939.jpg",
    "ISTANA_WIDE": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Singapore-Mandarin_Hotel-Istana-1973-74-WUS08140.jpg",
    "ISTANA_CLOSE": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Singapore-Mandarin_Hotel-Istana-1973-74-WUS08214.jpg",
    "FAMILY": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Benjamin_Sheares_and_his_family.jpg",
    "TOMB": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Tomb_of_President_Benjamin_Sheares.jpg",
}

# Singapore's total fertility rate, 1960-2024 - the same data already
# embedded as an SVG chart in the post body (see the post's own
# "From 5.76 to 0.97 children per woman" viz).
TFR_DATA = [
    (1960, 5.76), (1965, 4.66), (1970, 3.07), (1975, 2.07), (1980, 1.82),
    (1986, 1.43), (1990, 1.83), (2000, 1.60), (2010, 1.15), (2020, 1.10),
    (2023, 0.97), (2024, 0.97),
]

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "HERO", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.45), (0.5, 0.5), (0.5, 0.55)], "ease": "ease-out"},
    {"img": "YEOSEHGEOK", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ACADEMIC1940S", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "KKH", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.45, 0.5), (0.5, 0.5), (0.55, 0.5)], "ease": "ease-in-out"},
    {"img": "UNIMALAYA", "type": "letterbox", "zoom": [1.14, 1.07, 1], "pan": [(0.5, 0.55), (0.5, 0.5), (0.5, 0.45)], "ease": "ease-out"},
    {"img": "YEOSEHGEOK", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "UNESCO", "type": "letterbox", "zoom": [1, 1.08, 1.16], "pan": [(0.45, 0.45), (0.5, 0.5), (0.55, 0.55)], "ease": "ease-in-out"},
    {"img": "UNESCO", "type": "letterbox", "zoom": [1.16, 1.08, 1], "pan": [(0.55, 0.5), (0.5, 0.5), (0.45, 0.5)], "ease": "ease-out"},
    {"img": "UNESCO", "type": "letterbox", "zoom": [1, 1.07, 1.14], "pan": [(0.5, 0.55), (0.5, 0.5), (0.5, 0.45)], "ease": "ease-in"},
    {"img": "FAMILY", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ISTANA_WIDE", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)], "ease": "ease-out"},
    {"img": "ISTANA_CLOSE", "type": "cover", "zoom": [1, 1.08, 1.16], "pan": [(0.45, 0.55), (0.50, 0.50), (0.55, 0.45)], "ease": "ease-in"},
    {
        "type": "chart",
        "data": TFR_DATA,
        "x_range": (1960, 2024),
        "y_range": (0, 6),
        "y_tick_step": 1,
        "y_tick_format": "{:.0f}",
        "value_format": "{:.2f} children per woman",
        "title": "Singapore's total fertility rate, 1960-2024",
        "annotations": [
            # "below" here, not "above" like every other annotation on
            # this project's chart slides: the 1960 point sits at the
            # very top-left corner (data start = x_min, close to y_max),
            # the same corner the "6" y-axis tick label occupies - with
            # "above" the two texts visually collided (seen on a
            # rendered test frame). Also shortened to just "5.76", since
            # "(1960)" was redundant with the x-axis's own "1960" tick
            # directly below this point, and a shorter string moved
            # further from the tick-label region helps too.
            (1960, 5.76, "5.76", "below"),
            (1986, 1.43, "1.43 (1986) - 'Have 3 or More'", "below"),
        ],
        # Maps absolute post time -> the chart's current year at a pace
        # matching what each sentence actually says (see
        # piecewise_interp's docstring in watch_video_lib.py), not a
        # uniform year-per-second rate. Sentence 15 (209.225-215.8s) is
        # the topic-setup line with no year mentioned yet, so the chart
        # holds near the start; sentence 16 (215.8-234.1s) explicitly
        # names 1987 and "record lows," so the line sweeps from the
        # 1986 low through to the 2024 end across that stretch; sentence
        # 17 (234.1-244.8s) is a closing reflection with no new year, so
        # the chart holds at its finished state.
        "year_checkpoints": [
            (209.225, 1960), (215.8, 1986), (219.0, 1986),
            (234.1, 2024), (244.8, 2024),
        ],
    },
    {"img": "TOMB", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
]

# Real values from audio/benjamin-sheares-doctor-behind-the-baby-bust.timing.json.
# Schedule points mostly align to sentence starts, skipping the
# shortest sentences (3, 8, 12) so each visual gets a real hold rather
# than a rapid cut - their content still gets shown under the preceding
# slide. The one exception is (21.35, 2): the original HERO hold from
# 5.025 to 46.55 ran 41.5s uninterrupted - flagged by --check-only's
# 30s-hold note - so it's split with a YEOSEHGEOK teaser at sentence
# 2's start (a glimpse of his personal life during the "not a career
# politician... tapped by Lee Kuan Yew" reveal build-up), reused again
# properly at its own slot later once the presidency/legacy theme is
# actually being narrated.
SCHEDULE = [
    (0.0, 0), (5.025, 1), (21.35, 2), (46.55, 3), (52.875, 4),
    (74.275, 5), (90.075, 6), (104.775, 7), (111.525, 8), (131.425, 9),
    (151.85, 10), (163.65, 11), (171.35, 12), (191.0, 13), (209.225, 14),
    (244.8, 15),
]
TOTAL_DURATION = 270.475
TIMING_JSON = "audio/benjamin-sheares-doctor-behind-the-baby-bust.timing.json"
