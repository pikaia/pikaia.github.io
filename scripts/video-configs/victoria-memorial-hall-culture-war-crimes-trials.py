"""Video config for the Victoria Memorial Hall post's full-length Watch video.

Mirrors the post's own <script> `slides`/`imageSchedule` arrays by hand -
this duplication is intentional (same pattern as the route-walk feature),
not a shared-source parse, so keep both in sync if either changes.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/e/e6/Victoria_Theatre_and_Victoria_Memorial_Hall_-_c_1930.jpg",
    "CIRCA1900": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/KITLV_-_33196_-_Victoria_Theatre_and_Memorial_Hall_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_33196_-_Victoria_Theatre_and_Memorial_Hall_in_Singapore_-_circa_1900.tif.jpg",
    "STADHUIS1915": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/KITLV_A740_-_Stadhuis_te_Singapore%2C_KITLV_90268.tiff/lossy-page1-1280px-KITLV_A740_-_Stadhuis_te_Singapore%2C_KITLV_90268.tiff.jpg",
    "LOCATOR": "/assets/images/osm-victoria-theatre-concert-hall-location.png",
    "RAFFLES2004": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Victoria_Theatre_and_Concert_Hall_-_Stamford_Raffles_Statue_2004.jpg",
    "PHOTO1973": "https://upload.wikimedia.org/wikipedia/commons/7/78/Singapore-Victoria_Theatre_and_Concert_Hall-1973-74-WUS08256.jpg",
    "PHOTO1960": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Victoria_Theatre_Singapore_May_1960.jpg",
    "PHOTO1965": "https://upload.wikimedia.org/wikipedia/commons/2/29/VictoriaTheatreandMemorialHall-Singapore-1965.jpg",
    "FRONT2014": "https://upload.wikimedia.org/wikipedia/commons/5/54/Front_of_Victoria_Theatre%2C_Singapore_-_20141101-01.JPG",
    "ATRIUM2014": "https://upload.wikimedia.org/wikipedia/commons/8/80/Entrance_to_the_atrium_of_Victoria_Theatre_and_Concert_Hall%2C_Singapore_-_20141101-01.JPG",
    "PHOTO2023": "https://upload.wikimedia.org/wikipedia/commons/c/c9/Victoria_Memorial_Hall%2C_Singapore%2C_August_2023.jpg",
}

SLIDES = [
    {"img": "HERO", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.40), (0.45, 0.45), (0.40, 0.50)]},
    {"img": "CIRCA1900", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.45, 0.50), (0.50, 0.50), (0.55, 0.50)]},
    {"img": "STADHUIS1915", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.45), (0.50, 0.50), (0.45, 0.55)]},
    {"img": "LOCATOR", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.50, 0.50), (0.48, 0.50), (0.46, 0.50)]},
    {"img": "HERO", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.55), (0.50, 0.50), (0.45, 0.45)]},
    {"img": "RAFFLES2004", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.35), (0.50, 0.45), (0.50, 0.55)]},
    {"img": "PHOTO1973", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.40, 0.50), (0.50, 0.50), (0.60, 0.50)]},
    {"img": "PHOTO1973", "type": "cover", "zoom": [1.16, 1.06, 1], "pan": [(0.60, 0.45), (0.50, 0.50), (0.40, 0.55)]},
    {"img": "PHOTO1960", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.45, 0.50), (0.50, 0.45), (0.55, 0.40)]},
    {"img": "PHOTO1965", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.55, 0.40), (0.50, 0.50), (0.45, 0.60)]},
    {"img": "FRONT2014", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.50, 0.55), (0.50, 0.50), (0.50, 0.40)]},
    {"img": "ATRIUM2014", "type": "cover", "zoom": [1, 1.09, 1.16], "pan": [(0.45, 0.45), (0.50, 0.50), (0.55, 0.55)]},
    {"img": "PHOTO2023", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.50, 0.50), (0.48, 0.45), (0.46, 0.40)]},
]

SCHEDULE = [
    (0.0, 0), (37.75, 1), (43.75, 2), (66.35, 3), (94.225, 4), (124.7, 5),
    (152.1, 6), (194.225, 7), (217.0, 8), (239.4, 9), (264.0, 10), (285.8, 11),
    (299.9, 12),
]
TOTAL_DURATION = 331.625
TIMING_JSON = "audio/victoria-memorial-hall-culture-war-crimes-trials.timing.json"
