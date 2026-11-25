"""Short config for the Jurong Island post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py jurong-island-seven-islands-into-one 0,1,4,6,9,23,31,46,49,58,67,71,73,84,87
(15 sentences, 176.400s - under the 3-minute Shorts ceiling
with margin, and well over TikTok's 1-minute floor.)

The post's points, and the sentences that carry each:
1. The hook: everyone depends on the island, almost
   none will ever set foot on it. (s1)
2. The merger: seven islands joined by reclamation
   into a single chemical fortress. (s4)
3. The strait of nine: the penghulu Ismail's count. (s6)
4. The puzzle: the 1939 map shows fourteen. (s9)
5. The kampong world: Ayer Merbau's well that never
   ran dry. (s23)
6. Industry arrives: Esso on Ayer Chawan, 1968-1970. (s31)
7. The cost: one group of islanders resettled three
   times over. (s46)
8. The 1988 Merlimau fire, the worst in Singapore's
   refinery history. (s49)
9. The merger completed: finished 2009, twenty years
   ahead of schedule. (s58)
10. Below ground: the Jurong Rock Caverns. (s67)
11. The LNG terminal: a second way in for gas. (s71)
12. The closed island: a protected area, pass by
    sponsor only. (s73)
13. The reinvention: retooled for what comes after
    oil. (s84)
14. The close: nine were really fourteen, and are
    now one. (s87)

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24).
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Jurong_Island%2C_Singapore_-_20110227-01.jpg",
    "JACKLEE02": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Jurong_Island%2C_Singapore_-_20110227-02.jpg/1280px-Jurong_Island%2C_Singapore_-_20110227-02.jpg",
    "SUNSET": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg/1280px-Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg",
    "MAP1945": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Singapore_-_Jurong_Islands_1945.jpg",
    "LOCATOR": "https://upload.wikimedia.org/wikipedia/commons/1/15/Jurong_Island_locator_map.png",
    "SERAYA": "https://upload.wikimedia.org/wikipedia/commons/d/db/Power_Seraya_Power_Station.jpg",
    "NIGHT": "https://upload.wikimedia.org/wikipedia/commons/7/72/Aerial_view_of_Jurong_Island_from_Hill_top.jpg",
    "SEA2026": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Jurong_Island_June_2026.jpg/1280px-Jurong_Island_June_2026.jpg",
    "HILL2021": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg/1280px-Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg",
    "PANORAMA": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg/1920px-Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg",
    "PLP2016": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/PLPPowerPlant.jpg/1280px-PLPPowerPlant.jpg",
    "PLPFOO": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/PLPplant.jpg/1280px-PLPplant.jpg",
    "GRID": "https://pikaia.github.io/assets/images/jurong-landsat-grid.jpg",
    "L73": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/1973_Jurong%28chs.%201%2C4%2C2%29.png",
    "L89": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/1989_Jurong%28chs.%207%2C4%2C2%29.png",
    "L00": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/2000_Jurong%28chs.%207%2C4%2C2%29.png",
    "L02": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/2002_Jurong%28chs.%207%2C4%2C2%29.png",
    "L09": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/2009_Jurong%28chs.%207%2C4%2C2%29.png",
    "L18": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/5-24-2018_Jurong%28chs_7%2C5%2C4%29.png",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "MAP1945", "pan": (0.5, 0.5)},
    {"img": "SUNSET", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "L18", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "HERO", **_LB, "title": "Jurong Island from the sea, 2011"},   # s0 title (3.62s),
    {"img": "LOCATOR", **_LB, "title": "Jurong Island, south-west Singapore"},   # s1 everyone depends on it; almost none will set foot on it (6.75s),
    {"img": "MAP1945", **_LB, "title": "The Jurong islands in 1945"},   # s4 seven islands joined into a single chemical fortress (14.97s),
    {"img": "SUNSET", **_LB, "title": "Ships near Jurong Island at sunset, 2011"},   # s6 Ismail the penghulu counted nine in the strait (17.30s),
    {"img": "MAP1945", **_LB, "title": "The Jurong islands in 1945"},   # s9 the 1939 map shows fourteen, not nine (7.00s),
    {"img": "SUNSET", **_LB, "title": "Ships near Jurong Island at sunset, 2011"},   # s23 Ayer Merbau's well never ran dry; neighbours came for water (16.68s),
    {"img": "JACKLEE02", **_LB, "title": "Jurong Island from the sea, 2011"},   # s31 1968: Esso takes Ayer Chawan; the refinery starts 1970 (18.30s),
    {"img": "MAP1945", **_LB, "title": "The Jurong islands in 1945"},   # s46 one group of islanders resettled three times over (13.88s),
    {"img": "HERO", **_LB, "title": "Jurong Island from the sea, 2011"},   # s49 October 1988: the worst refinery fire in Singapore's history (16.60s),
    {"img": "L09", **_LB, "title": "Landsat view, 2009 (USGS)"},   # s58 the merger finished in 2009, twenty years early (6.67s),
    {"img": "NIGHT", **_LB, "title": "Jurong Island at night, 2009"},   # s67 beneath the island: five rock caverns, 130 m down (17.98s),
    {"img": "PANORAMA", **_LB, "title": "Jurong Island Highway, 2006"},   # s71 the LNG terminal, 2013: a second way in for gas (15.55s),
    {"img": "HILL2021", **_LB, "title": "Jurong Island from Jurong Hill Tower, 2021"},   # s73 a protected area: entry only with a sponsor's pass (6.65s),
    {"img": "SEA2026", **_LB, "title": "Jurong Island, June 2026"},   # s84 the island built for oil, retooled for after oil (5.88s),
    {"img": "SUNSET", **_LB, "title": "Ships near Jurong Island at sunset, 2011"},   # s87 nine were really fourteen, and are now one (8.57s),
]
SCHEDULE = [
    (0.000, 0), (3.625, 1), (10.375, 2), (25.350, 3), (42.650, 4), (49.650, 5),
    (66.325, 6), (84.625, 7), (98.500, 8), (115.100, 9), (121.775, 10), (139.750, 11),
    (155.300, 12), (161.950, 13), (167.825, 14)
]
TOTAL_DURATION = 176.400
TIMING_JSON = "audio/jurong-island-seven-islands-into-one-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
