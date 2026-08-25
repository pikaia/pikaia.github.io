"""Video config for the Bugis Street post's full-length Watch video.

No freely-licensed historical photographs of old Bugis Street's nightlife
survive on Wikimedia Commons - the real ones (Alain Soldeville's 1981
photos, See Mun Wah's 1950s-1980s souvenir photos, the one NAS archival
photo) are all held under conventional copyright. This video leans on
the post's own honest solution: the 1890 guide map for the naming/vice-
district history, the Bugis Junction fountain for the toilet-ritual site
(a direct location match), Bugis Junction itself for the redevelopment
result, and the "today's market" photos reused across the sections that
describe what used to be there instead. All 7 available images are
landscape enough (aspect 1.125-1.51) to use `cover` throughout - no
letterbox needed, unlike the Japanese Cemetery Park post's portrait
sources.

Mirrors the post's own <script> `slides`/`imageSchedule` arrays by hand -
this duplication is intentional (same pattern as the route-walk feature),
not a shared-source parse, so keep both in sync if either changes.
"""

IMAGES = {
    "MARKET2014A": "https://upload.wikimedia.org/wikipedia/commons/e/ec/New_Bugis_Street%2C_Singapore%2C_2014_%2801%29.JPG",
    "MAP1890": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Guide_map_of_Singapore_Town_from_The_Stranger%27s_Guide_to_Singapore_%281890%29.jpg",
    "FOUNTAIN": "https://upload.wikimedia.org/wikipedia/commons/e/ea/BugisJunction_Fountain.JPG",
    "MARKET2014B": "https://upload.wikimedia.org/wikipedia/commons/4/4a/New_Bugis_Street%2C_Singapore%2C_2014_%2803%29.JPG",
    "MARKET2006": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Bugis_Street%2C_Aug_06.JPG",
    "JUNCTION2016": "https://upload.wikimedia.org/wikipedia/commons/0/0a/2016-04-05_Bugis_Junction_01.jpg",
    "MARKETINSIDE2020": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Bugis_Street_Market.jpg",
}

SLIDES = [
    {"img": "MARKET2014A", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-in-out"},
    {"img": "MAP1890", "type": "cover", "zoom": [1, 1.1, 1.2], "pan": [(0.30, 0.40), (0.50, 0.50), (0.70, 0.60)], "ease": "linear"},
    {"img": "MAP1890", "type": "cover", "zoom": [1.2, 1.1, 1], "pan": [(0.65, 0.60), (0.50, 0.50), (0.35, 0.40)], "ease": "linear"},
    {"img": "MARKET2006", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.35, 0.50), (0.50, 0.50), (0.65, 0.50)], "ease": "ease-out"},
    {"img": "MARKET2006", "type": "cover", "zoom": [1.16, 1.06, 1], "pan": [(0.65, 0.55), (0.50, 0.50), (0.35, 0.45)], "ease": "ease-in"},
    {"img": "MARKETINSIDE2020", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.40), (0.50, 0.50), (0.50, 0.60)], "ease": "ease-in-out"},
    {"img": "MARKETINSIDE2020", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.45, 0.55), (0.50, 0.50), (0.55, 0.45)], "ease": "ease-in"},
    {"img": "MARKET2014B", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.40, 0.50), (0.50, 0.45), (0.60, 0.40)], "ease": "ease-out"},
    {"img": "FOUNTAIN", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)], "ease": "ease-in-out"},
    {"img": "JUNCTION2016", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.35, 0.50), (0.50, 0.50), (0.65, 0.50)], "ease": "ease-out"},
    {"img": "JUNCTION2016", "type": "cover", "zoom": [1.16, 1.06, 1], "pan": [(0.65, 0.55), (0.50, 0.50), (0.35, 0.45)], "ease": "ease-in"},
    {"img": "MARKET2014A", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)], "ease": "ease-in"},
    {"img": "MARKET2014B", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.45, 0.50), (0.50, 0.55), (0.55, 0.60)], "ease": "ease-in-out"},
    {"img": "MARKETINSIDE2020", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.50), (0.48, 0.50), (0.46, 0.50)], "ease": "linear"},
    {"img": "FOUNTAIN", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)], "ease": "ease-in-out"},
]

SCHEDULE = [
    (0.0, 0), (35.825, 1), (68.55, 2), (94.85, 3), (126.675, 4),
    (154.6, 5), (176.575, 6), (213.5, 7), (259.825, 8), (288.475, 9),
    (319.75, 10), (341.175, 11), (372.525, 12), (397.075, 13), (405.6, 14),
]
TOTAL_DURATION = 444.725
TIMING_JSON = "audio/bugis-street-before-redevelopment.timing.json"
