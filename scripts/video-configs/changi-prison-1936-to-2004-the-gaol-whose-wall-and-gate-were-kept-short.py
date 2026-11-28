"""Short config for the Changi Prison post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py changi-prison-1936-to-2004-the-gaol-whose-wall-and-gate-were-kept 0,2,9,18,29,38,40,45,46,50,54,60,74,78,81
(15 sentences, 173.90s - under the 3-minute
Shorts ceiling with margin, and well over TikTok's
1-minute floor.)

The post's points, and the sentences that carry each:
1. The fragment kept, a monument behind wire. (s2)
2. The model prison of 1936, built for 600. (s9)
3. The internees marched in, February 1942. (s18)
4. The quilts: names sent out of the wire. (s29)
5. The Double Tenth, and the fifteen who died. (s38, s40)
6. May 1944: the POWs moved in, five to a cell. (s45, s46)
7. Liberation, September 1945. (s50)
8. The reckoning: executions at Changi. (s54)
9. The peacetime main prison. (s60)
10. Demolition, the fragment kept, the 2016 gazetting. (s74, s78)
11. The closing line: the threshold remains. (s81)

Compression casualties, noted honestly: Shenton Thomas,
POW WOW, the war-crimes trials in detail, the prison
farm, the Cold Store detainees by name, and the new
complex are carried by their neighbours or dropped;
the spine - model prison, internees, quilts, Double
Tenth, five to a cell, liberation, reckoning, the
peacetime gaol, demolition and the monument - is intact.

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24). All four THUMBNAIL
keys (DOOR, POW, GATES, TURRET) are in IMAGES and used
by slides, for the step-8.3 grid.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "GATES": "https://upload.wikimedia.org/wikipedia/commons/9/91/Allied_prisoners_of_war_after_the_liberation_of_Changi_Prison%2C_Singapore_-_c._1945_-_02_edited.jpg",
    "TURRET": "/assets/images/changi-turret-2025.jpg",
    "DOOR": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Changi_Prison_cell_door_%28exterior%29%2C_Singapore_History_Gallery%2C_National_Museum_of_Singapore_-_20151125.jpg",
    "DOORIN": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Changi_Prison_cell_door_%28interior%29%2C_Singapore_History_Gallery%2C_National_Museum_of_Singapore_-_20151125.jpg",
    "POW": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Krijgsgevangene_van_de_Japanners_in_Changi_gevangenis_in_Singapore%2C_Bestanddeelnr_935-3623.jpg",
    "BANNER": "https://upload.wikimedia.org/wikipedia/commons/4/45/Banner_on_a_wall_of_Changi_Prison%2C_Singapore_-_20090116.jpg",
}

CREDITS = {}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "GATES", **_LB, "title": "Changi Prison"},  # 0  title (6.62s) (s0)
    {"img": "TURRET", **_LB, "title": "A monument behind wire"},  # 1  the fragment: a national monument in a restricted area (10.28s) (s2)
    {"img": "DOOR", **_LB, "title": "Built for 600 men"},  # 2  the model prison of 1936: 600 men, a light and a latrine per cell (18.50s) (s9)
    {"img": "DOORIN", **_LB, "title": "The civilians marched in"},  # 3  17 February 1942: the civilians rounded up and marched in (8.45s) (s18)
    {"img": "DOOR", **_LB, "title": "The quilts: names in thread"},  # 4  the quilts' real purpose: the men must know they were alive (10.95s) (s29)
    {"img": "POW", **_LB, "title": "The Double Tenth"},  # 5  10 October 1943: the Kempeitai raid the gaol (11.90s) (s38)
    {"img": "POW", **_LB, "title": "Fifteen died"},  # 6  fifteen of the 57 died under torture (1.93s) (s40)
    {"img": "POW", **_LB, "title": "The POWs moved in, 1944"},  # 7  May 1944: the POWs concentrated at the gaol (9.15s) (s45)
    {"img": "POW", **_LB, "title": "Five men to a cell"},  # 8  5,000 in the building, five to a cell built for one (25.02s) (s46)
    {"img": "GATES", **_LB, "title": "Liberation, 1945"},  # 9  released on 6 September 1945 (12.85s) (s50)
    {"img": "DOORIN", **_LB, "title": "Executions at Changi"},  # 10  one published count: 135 executed there (5.65s) (s54)
    {"img": "BANNER", **_LB, "title": "Singapore's main prison"},  # 11  the peacetime half-century (10.57s) (s60)
    {"img": "TURRET", **_LB, "title": "The fragment that was kept"},  # 12  the 2004 compromise: gate, 180 metres of wall, two turrets (12.53s) (s74)
    {"img": "TURRET", **_LB, "title": "A national monument, 2016"},  # 13  gazetted the 72nd National Monument, 15 February 2016 (17.15s) (s78)
    {"img": "GATES", **_LB, "title": "The threshold remains"},  # 14  the closing line: the gate every prisoner passed through (12.35s) (s81)
]

SCHEDULE = [
    (0.000, 0), (6.625, 1), (16.900, 2),
    (35.400, 3), (43.850, 4), (54.800, 5),
    (66.700, 6), (68.625, 7), (77.775, 8),
    (102.800, 9), (115.650, 10), (121.300, 11),
    (131.875, 12), (144.400, 13), (161.550, 14)
]
TOTAL_DURATION = 173.900
TIMING_JSON = "audio/changi-prison-1936-to-2004-the-gaol-whose-wall-and-gate-were-kept-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
