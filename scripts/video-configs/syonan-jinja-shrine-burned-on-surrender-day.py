"""Video config for the Syonan Jinja post's full-length Watch video.

Mirrors the post's own <script> `slides`/`imageSchedule` arrays by hand -
this duplication is intentional (same pattern as the route-walk feature),
not a shared-source parse, so keep both in sync if either changes.
"""

IMAGES = {
    "CONSTRUCTION": "https://upload.wikimedia.org/wikipedia/commons/8/80/Shinto_shrine_in_Shonan_%28Singapore%29_-_194210.jpg",
    "OFFICERS": "https://upload.wikimedia.org/wikipedia/commons/4/43/%E6%98%AD%E5%8D%97%E7%A5%9E%E7%A4%BE-%E9%99%B8%E6%B5%B7%E5%B0%86%E6%98%9F%E3%81%AE%E5%8F%82%E6%8B%9D.jpg",
    "DJAWA": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Syonan_Shrine_in_Singapore%2C_Djawa_Baroe%2C_Vol._1%2C_Iss._11_%281943-06-01%29%2C_p31.jpg",
    "STAMP": "https://upload.wikimedia.org/wikipedia/commons/8/8f/%E6%98%AD%E5%8D%97%E7%A5%9E%E7%A4%BE%E9%82%AE%E7%A5%A8%EF%BC%88%E6%97%A5%E6%B2%BB%E9%A9%AC%E6%9D%A5%EF%BC%89.jpg",
    "BRIDGE1": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Remains_of_Divine_Bridge_leading_to_Synonan_Jinja_at_MacRitchie_Reservoir%2C_Singapore%2C_1_-_2022-07-02.jpg",
    "BRIDGE2": "https://upload.wikimedia.org/wikipedia/commons/3/33/Remains_of_Divine_Bridge_leading_to_Synonan_Jinja_at_MacRitchie_Reservoir%2C_Singapore%2C_2_-_2022-07-02.jpg",
    "BRIDGE3": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Remains_of_Divine_Bridge_leading_to_Synonan_Jinja_at_MacRitchie_Reservoir%2C_Singapore%2C_3_-_2022-07-02.jpg",
    "LOCATOR": "/assets/images/osm-syonan-jinja-singapore-locator.png",
}

SLIDES = [
    {"img": "CONSTRUCTION", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.40), (0.45, 0.45), (0.40, 0.50)]},
    {"img": "CONSTRUCTION", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)]},
    {"img": "CONSTRUCTION", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.40, 0.45), (0.50, 0.50), (0.60, 0.55)]},
    {"img": "STAMP", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.50, 0.50), (0.50, 0.50), (0.50, 0.50)]},
    {"img": "DJAWA", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.45, 0.40), (0.50, 0.50), (0.55, 0.60)]},
    {"img": "OFFICERS", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)]},
    {"img": "OFFICERS", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.40, 0.55), (0.50, 0.50), (0.60, 0.45)]},
    {"img": "BRIDGE1", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.50, 0.55), (0.50, 0.50), (0.50, 0.40)]},
    {"img": "BRIDGE2", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)]},
    {"img": "BRIDGE3", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)]},
    {"img": "LOCATOR", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.50), (0.48, 0.50), (0.46, 0.50)]},
    {"img": "CONSTRUCTION", "type": "cover", "zoom": [1, 1.1, 1.2], "pan": [(0.50, 0.50), (0.45, 0.45), (0.40, 0.40)]},
]

SCHEDULE = [
    (0.0, 0), (38.325, 1), (62.825, 2), (91.1, 3), (104.2, 4), (129.775, 5),
    (144.0, 6), (172.475, 7), (195.0, 8), (210.1, 9), (223.175, 10), (244.875, 11),
]
TOTAL_DURATION = 271.525
TIMING_JSON = "audio/syonan-jinja-shrine-burned-on-surrender-day.timing.json"
