"""Video config for the HDB price-per-square-foot post's Watch video.

6 slides: 4 photos (today's flats, the pre-HDB kampong era, 1973-74
construction, and a 1973-74 skyline aerial) bookend a single long "chart"
slide that spans the whole price-history narration (s5-13, ~117s) -
animating the post's own 1990-2026 line chart drawing itself left to
right in sync with the narration, instead of showing it as a static
image. Requested by Chris, 2026-08-22. The 1961 Straits Times front page
(Bukit Ho Swee fire, the event that created the HDB in the first place)
is portrait-oriented and uses letterbox; every other photo is cover.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/d/d3/HDB_flats_in_Singapore_2.jpg",
    "KAMPONG1964": "https://upload.wikimedia.org/wikipedia/commons/8/81/Kampong_in_Braddell_Hill_Singapore_about_1964.jpg",
    "STPAGE": "https://upload.wikimedia.org/wikipedia/commons/3/39/ST27May1961.jpg",
    "HOUSING1973A": "https://upload.wikimedia.org/wikipedia/commons/8/87/Singapore-Public_Housing-1973-74-WUS08215.jpg",
    "HOUSING1973B": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Singapore-Public_Housing-1973-74-WUS08216.jpg",
}

HDB_DATA = [
    (1990, 80), (1991, 81), (1992, 90), (1993, 132), (1994, 170), (1995, 209),
    (1996, 285), (1997, 293), (1998, 243), (1999, 231), (2000, 242), (2001, 221),
    (2002, 212), (2003, 218), (2004, 226), (2005, 224), (2006, 227), (2007, 246),
    (2008, 298), (2009, 320), (2010, 359), (2011, 408), (2012, 440), (2013, 464),
    (2014, 431), (2015, 419), (2016, 420), (2017, 424), (2018, 420), (2019, 419),
    (2020, 440), (2021, 496), (2022, 538), (2023, 571), (2024, 615), (2025, 658),
    (2026, 662),
]

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)]},
    {"img": "KAMPONG1964", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)]},
    {"img": "HOUSING1973A", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.40), (0.50, 0.50), (0.50, 0.60)]},
    {"img": "STPAGE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {
        "type": "chart",
        "data": HDB_DATA,
        "x_range": (1990, 2026),
        "y_range": (0, 700),
        "title": "Average resale price per square foot, 4-room HDB flats, Singapore-wide (1990–2026 YTD)",
        "annotations": [
            (1990, 80, "$80 (1990)", "below"),
            (1997, 293, "$293 (1997)", "above"),
        ],
    },
    {"img": "HOUSING1973B", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.50, 0.55), (0.50, 0.50), (0.50, 0.45)]},
]

SCHEDULE = [
    (0.0, 0), (22.4, 1), (27.35, 2), (36.25, 3), (44.75, 4), (161.425, 5),
]
TOTAL_DURATION = 176.825
TIMING_JSON = "audio/what-a-square-foot-of-hdb-flat-has-cost.timing.json"
