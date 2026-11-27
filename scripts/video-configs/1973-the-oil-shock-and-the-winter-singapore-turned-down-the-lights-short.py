"""Short config for the 1973 oil shock post - a synopsis re-cut.

Built with: python scripts/build_short_audio.py 1973-the-oil-shock-and-the-winter-singapore-turned-down-the-lights 0,1,5,17,31,39,43,46,51,56,57,59,69,80,83,87
(16 sentences, 170.22s - under the 3-minute
Shorts ceiling with margin, and well over TikTok's
1-minute floor.)

The post's points, and the sentences that carry each:
1. The hook: the lights stayed on, deliberately. (s0, s1)
2. A top-three refining centre on imported oil. (s5)
3. The price: $3.00 to $11.65 in three months. (s17)
4. Embargo discipline: not another Rotterdam. (s31)
5. The stocks decision: two years in the tanks. (s39)
6. The position: take the cut, pay the full price. (s43)
7. No rationing. (s46)
8. Save a litre a day. (s51)
9. The contrast: America dry, Singapore queue-free. (s56, s57)
10. The lights: sodium lamps from January 1974. (s59)
11. The bill: inflation at 22.4 percent. (s69)
12. Conservation made permanent. (s80)
13. The second shock answered the same way, 1979. (s83)
14. The close: the answers built since. (s87)

Compression casualties, noted honestly: the cables'
10-to-20-percent expectation, the 98-percent oil quote,
the Reagan aircraft refusal, the consumption
fall in tonnes, and the Plaza Singapura / hospital colour
are carried by their neighbours or dropped; the embargo
itself is carried by the cables and Rotterdam sentences.

Every slide is letterboxed and carries its photo title,
as in the main config. All Short titles are 42 characters
or under (standing rule, 2026-11-24). NOGAS is in IMAGES
for the step-8.3 thumbnail grid, which reuses the main
config's THUMBNAIL keys; no Short slide uses it.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "STREET": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Singapore-Street_Scene-1973-74-WUS08222.jpg",
    "NOGAS": "https://upload.wikimedia.org/wikipedia/commons/4/4f/%22NO_GAS%22_SIGNS_WERE_A_COMMON_SIGHT_IN_OREGON_DURING_THE_FALL_OF_1973%2C_SUCH_AS_AT_THIS_STATION_IN_LINCOLN_CITY_ALONG..._-_NARA_-_555416.jpg",
    "CHART": "/assets/images/crude-oil-prices-1970-1980.png",
    "HDBNIGHT": "https://upload.wikimedia.org/wikipedia/commons/b/b9/HDB_at_night_%288144994286%29.jpg",
    "RIVER": "https://upload.wikimedia.org/wikipedia/commons/4/42/Singapore-Singapore_River-1973-74-WUS08203.jpg",
    "BUKOM": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Pulau_Bukom_from_Sentosa.JPG",
    "JURONGPANO": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Jurong_Hill_aerial_panorama.jpg",
    "ESSO": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Esso_Singapore.JPG",
    "DRY": "https://upload.wikimedia.org/wikipedia/commons/0/01/GASOLINE_SHORTAGE_HIT_THE_STATE_OF_OREGON_IN_THE_FALL_OF_1973_BY_MIDDAY_GASOLINE_WAS_BECOMING_UNAVAILABLE_ALONG..._-_NARA_-_555405.jpg",
    "SENOKO": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Senoko_Power_Station.JPG",
}

CREDITS = {}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "STREET", **_LB, "title": "1973: The Oil Shock"},  # 0  title (5.67s) (s0)
    {"img": "RIVER", **_LB, "title": "The lights did not go out"},  # 1  the hook: no oil of its own, lights stayed on (6.40s) (s1)
    {"img": "BUKOM", **_LB, "title": "A top-three refining centre"},  # 2  top three alongside Houston and Rotterdam (9.47s) (s5)
    {"img": "CHART", **_LB, "title": "From $3.00 to $11.65"},  # 3  the posted price quadruples (17.52s) (s17)
    {"img": "JURONGPANO", **_LB, "title": "Not another Rotterdam"},  # 4  no onward shipments to embargoed destinations (5.97s) (s31)
    {"img": "BUKOM", **_LB, "title": "Enough in the tanks for two years"},  # 5  the stocks decision, Lee's figure (10.22s) (s39)
    {"img": "STREET", **_LB, "title": "Take the cut, pay the price"},  # 6  no special privilege; full market price (11.75s) (s43)
    {"img": "RIVER", **_LB, "title": "No rationing"},  # 7  no rationing, no lower speed limits (4.10s) (s46)
    {"img": "ESSO", **_LB, "title": "Save a litre a day"},  # 8  BP's campaign: 49.5 cents a day (12.62s) (s51)
    {"img": "DRY", **_LB, "title": "Dry by midday, Oregon"},  # 9  America: stations dry, No Gas signs (10.22s) (s56)
    {"img": "STREET", **_LB, "title": "No queues in Singapore"},  # 10  tax schedules and leaflets instead (9.80s) (s57)
    {"img": "HDBNIGHT", **_LB, "title": "Sodium lamps from 1974"},  # 11  the lights changed, dimmed by technology (14.88s) (s59)
    {"img": "RIVER", **_LB, "title": "Inflation hits 22.4 percent"},  # 12  the World Bank series, 1974 (18.38s) (s69)
    {"img": "SENOKO", **_LB, "title": "Conservation becomes permanent"},  # 13  a standing feature of policy by 1981 (6.80s) (s80)
    {"img": "HDBNIGHT", **_LB, "title": "Save Electricity, 1979"},  # 14  the second shock's named campaign (10.80s) (s83)
    {"img": "JURONGPANO", **_LB, "title": "The answers built since"},  # 15  the close: pipelines and the LNG terminal (15.60s) (s87)
]

SCHEDULE = [
    (0.000, 0), (5.675, 1), (12.075, 2),
    (21.550, 3), (39.075, 4), (45.050, 5),
    (55.275, 6), (67.025, 7), (71.125, 8),
    (83.750, 9), (93.975, 10), (103.775, 11),
    (118.650, 12), (137.025, 13), (143.825, 14),
    (154.625, 15)
]
TOTAL_DURATION = 170.225
TIMING_JSON = "audio/1973-the-oil-shock-and-the-winter-singapore-turned-down-the-lights-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
