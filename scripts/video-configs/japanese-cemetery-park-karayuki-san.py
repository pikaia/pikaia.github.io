"""Video config for the Japanese Cemetery Park post's full-length Watch video.

Mirrors the post's own <script> `slides`/`imageSchedule` arrays by hand -
this duplication is intentional (same pattern as the route-walk feature),
not a shared-source parse, so keep both in sync if either changes.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Japanese_Cemetery_Park.jpg",
    "CEM1": "https://upload.wikimedia.org/wikipedia/commons/1/12/Japanese_Cemetery_Park_1.jpg",
    "LOCATOR": "/assets/images/osm-japanese-cemetery-park-location.png",
    "KARAYUKI": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Karayukisan_in_Saigon.JPG",
    "OTOKICHI_PORTRAIT": "https://upload.wikimedia.org/wikipedia/commons/7/74/Otokichi.jpg",
    "OTOKICHI_GRAVE": "https://upload.wikimedia.org/wikipedia/commons/4/4f/Yamamoto_Otokichi_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg",
    "WARMEM": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Japanese_war_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg",
    "TERAUCHI_PORTRAIT": "https://upload.wikimedia.org/wikipedia/commons/8/83/General_Hisaichi_Terauchi%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._13_%281943-07-01%29%2C_p11.jpg",
    "TERAUCHI_GRAVE": "https://upload.wikimedia.org/wikipedia/commons/5/59/Hisaichi_Terauchi_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg",
    "PRAYERHALL": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Prayer_hall%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg",
    "CARETAKER": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Caretaker%27s_quarters%2C_Japanese_Cemetery_Park%2C_Singapore.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)]},
    {"img": "CEM1", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.35, 0.50), (0.50, 0.50), (0.65, 0.50)]},
    {"img": "LOCATOR", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.50), (0.48, 0.50), (0.46, 0.50)]},
    {"img": "KARAYUKI", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)]},
    {"img": "KARAYUKI", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.55, 0.50), (0.50, 0.50), (0.45, 0.50)]},
    {"img": "CEM1", "type": "cover", "zoom": [1.16, 1.06, 1], "pan": [(0.65, 0.55), (0.50, 0.50), (0.35, 0.45)]},
    {"img": "CEM1", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.50, 0.35), (0.50, 0.50), (0.50, 0.65)]},
    {"img": "HERO", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.45, 0.55), (0.50, 0.50), (0.55, 0.45)]},
    {"img": "KARAYUKI", "type": "letterbox", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.50), (0.50, 0.50), (0.50, 0.50)]},
    {"img": "PRAYERHALL", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.45), (0.50, 0.50), (0.50, 0.55)]},
    {"img": "OTOKICHI_PORTRAIT", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.50), (0.50, 0.50), (0.50, 0.50)]},
    {"img": "OTOKICHI_GRAVE", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)]},
    {"img": "WARMEM", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.50, 0.40), (0.50, 0.50), (0.50, 0.60)]},
    {"img": "WARMEM", "type": "cover", "zoom": [1.18, 1.09, 1], "pan": [(0.60, 0.45), (0.50, 0.50), (0.40, 0.55)]},
    {"img": "TERAUCHI_PORTRAIT", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.50), (0.50, 0.50), (0.50, 0.50)]},
    {"img": "CARETAKER", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)]},
    {"img": "TERAUCHI_GRAVE", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.50), (0.50, 0.50), (0.50, 0.50)]},
    {"img": "HERO", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.50, 0.60), (0.50, 0.50), (0.50, 0.40)]},
]

SCHEDULE = [
    (0.0, 0), (20.025, 1), (42.15, 2), (49.2, 3), (77.95, 4), (107.05, 5),
    (129.725, 6), (155.425, 7), (181.25, 8), (194.3, 9), (202.4, 10),
    (213.0, 11), (223.1, 12), (243.725, 13), (260.025, 14), (273.925, 15),
    (286.25, 16), (303.275, 17),
]
TOTAL_DURATION = 329.675
TIMING_JSON = "audio/japanese-cemetery-park-karayuki-san.timing.json"
