"""Short config for the St James Power Station post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py st-james-power-station-the-coal-fired-station-of-1926 0,3,11,23,26,32,34,37,40,50,54,60,63,71
(14 sentences, 174.25s - under the 3-minute
Shorts ceiling with margin, and well over TikTok's
1-minute floor.)

The post's points, and the sentences that carry each:
1. The hook: a coal-fired station a century old. (s0, s3)
2. Why it was built: for the town, not borrowed. (s11)
3. The first unit: 30 September 1926. (s23)
4. The scale: about 22,000 kilowatts, seven times before. (s26)
5. The coal: from Manchuria, via Japanese tenderers. (s32)
6. The brevity of coal: fourteen years, then oil. (s34)
7. The troubled years: blackouts from 1928. (s37)
8. The Occupation: local staff kept it running. (s40)
9. The rebuild: the chimneys of 1960. (s50)
10. The end of generation: decommissioned 1976. (s54)
11. The second life: a nightclub from 2006. (s60)
12. The monument: gazetted 2009, clubs still inside. (s63)
13. The third life: Dyson's world headquarters. (s71)

Compression casualties, noted honestly: the PSA
warehouse years (1983-1992) and the 1927 opening
ceremony are carried by their neighbours (the 1976
decommissioning and the 2006 launch bracket the
warehouse; the first unit and the scale carry 1927).

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24).
"""

WIDTH, HEIGHT = 1080, 1920

# POSTCARD is in this dict for the step-8.3 thumbnail grid,
# which reuses the main config's THUMBNAIL keys; no Short
# slide uses it.
IMAGES = {
    "NIGHT1": "https://upload.wikimedia.org/wikipedia/commons/4/42/St_James_Power_Station%2C_Singapore%2C_at_night_-_20070127-01.jpg",
    "POSTCARD": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Singapore._View_from_St._James%2C_KITLV_1404953.tiff/1280px-Singapore._View_from_St._James%2C_KITLV_1404953.jpg",
    "NOV06": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Saint_James_Power_Station%2C_Nov_06.JPG",
    "DAY06A": "https://upload.wikimedia.org/wikipedia/commons/d/d3/St._James_Power_Station.JPG",
    "DAY06B": "https://upload.wikimedia.org/wikipedia/commons/4/4e/St._James_Power_Station_2.JPG",
    "PORTRAIT": "https://upload.wikimedia.org/wikipedia/commons/4/46/St._James_Power_Station_3.JPG",
    "HARB52": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Singapore_-_Keppel_Harb_1952.jpg",
    "PANOKEPPEL": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Keppel_Harbour%2C_panorama%2C_Aug_06.jpg",
    "HARB71": "https://upload.wikimedia.org/wikipedia/commons/0/0f/160a_Singapore_Harbour_from_Frasers_Hill_1971_%2851253058814%29.jpg",
    "TODAY25": "https://upload.wikimedia.org/wikipedia/commons/8/82/St._James_Power_Station%2C_October_2025.jpg",
    "DUSK09": "https://upload.wikimedia.org/wikipedia/commons/7/75/St_James_Power_Station%2C_Singapore_-_20090926.jpg",
    "DYSONDAY": "https://upload.wikimedia.org/wikipedia/commons/f/f3/SJPSDay.jpg",
}

CREDITS = {}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "NIGHT1", **_LB, "title": "St James Power Station"},  # 0  title (5.67s) (s0)
    {"img": "NOV06", **_LB, "title": "First municipal power station"},  # 1  the hook: Singapore's first municipal power station (15.22s) (s3)
    {"img": "DAY06A", **_LB, "title": "Built for the town"},  # 2  why: a station built for the town, not borrowed (7.47s) (s11)
    {"img": "DAY06B", **_LB, "title": "First unit: 30 Sep 1926"},  # 3  the first unit, 30 September 1926 (13.47s) (s23)
    {"img": "PORTRAIT", **_LB, "title": "22,000 kilowatts, seven times"},  # 4  the scale: about 22,000 kilowatts (17.27s) (s26)
    {"img": "HARB52", **_LB, "title": "Coal from Manchuria"},  # 5  the coal: Manchuria via Japanese tenderers (14.85s) (s32)
    {"img": "PANOKEPPEL", **_LB, "title": "Coal for 14 years, then oil"},  # 6  coal for fourteen years only, then oil (6.62s) (s34)
    {"img": "NOV06", **_LB, "title": "Blackouts from 1928"},  # 7  the troubled years: blackouts from 1928 (10.28s) (s37)
    {"img": "HARB71", **_LB, "title": "The Occupation years"},  # 8  local staff kept it running through the war (19.52s) (s40)
    {"img": "TODAY25", **_LB, "title": "The chimneys of 1960"},  # 9  the rebuild: the chimneys of 1960 (10.95s) (s50)
    {"img": "DAY06A", **_LB, "title": "Decommissioned, 1976"},  # 10  phased out; the last turbines, 1976 (11.78s) (s54)
    {"img": "NIGHT1", **_LB, "title": "A nightclub from 2006"},  # 11  the second life: launched 24 September 2006 (15.07s) (s60)
    {"img": "DUSK09", **_LB, "title": "National monument, 2009"},  # 12  gazetted in 2009, clubs still inside (15.18s) (s63)
    {"img": "DYSONDAY", **_LB, "title": "Dyson's world HQ today"},  # 13  the third life: Dyson's headquarters (10.88s) (s71)
]

SCHEDULE = [
    (0.000, 0), (5.675, 1), (20.900, 2),
    (28.375, 3), (41.850, 4), (59.125, 5),
    (73.975, 6), (80.600, 7), (90.875, 8),
    (110.400, 9), (121.350, 10), (133.125, 11),
    (148.200, 12), (163.375, 13)
]
TOTAL_DURATION = 174.25
TIMING_JSON = "audio/st-james-power-station-the-coal-fired-station-of-1926-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
