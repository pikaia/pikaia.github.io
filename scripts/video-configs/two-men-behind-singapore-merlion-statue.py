"""Video config for the Merlion post's Watch widget / main video.

Reconstructed from the post's own already-published (pre-canonical-
pipeline) live widget script - this post's real video predates
scripts/video-configs/, so this file did not exist until now."""

IMAGES = {
    "MERLIONSINGAPORE": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Merlion%2C_Singapore.JPG",
    "MERLIONCLOSEUPLARG": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Merlion_Closeup_Large.JPG",
    "LIMNANGSENG": "https://upload.wikimedia.org/wikipedia/commons/8/81/Lim_Nang_Seng.jpg",
    "MERLIONANDTHESINGA": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Merlion_and_the_Singapore_Skyline.JPG",
    "REARVIEWOFTHEMERLI": "https://upload.wikimedia.org/wikipedia/commons/2/20/Rear_view_of_the_Merlion_statue_at_Merlion_Park%2C_Singapore%2C_with_Marina_Bay_Sands_in_the_distance_-_20140307.jpg",
    "SINGAPOREMINIMERLI": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Singapore_Mini_Merlion.JPG",
    "MERLIONSTATUEATTOU": "https://upload.wikimedia.org/wikipedia/commons/2/24/Merlion_statue_at_Tourism_Court%2C_Singapore_-_20150329.jpg",
    "PANORAMIO2005": "https://upload.wikimedia.org/wikipedia/commons/8/80/2005_%E6%96%B0%E5%8A%A0%E5%9D%A1_-_panoramio_%282%29.jpg",
    "SINGAPOREMERLIONIN": "https://upload.wikimedia.org/wikipedia/commons/5/51/Singapore_Merlion_in_1978.jpg",
    "FORMERMERLIONPARK": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Former_Merlion_Park.JPG",
}

SLIDES = [
    {"img": "MERLIONSINGAPORE", "type": "cover", "zoom": [1.0, 1.12, 1.18], "pan": [(0.45, 0.35), (0.62, 0.55), (0.72, 0.45)], "ease": "ease-in-out"},
    {"img": "MERLIONCLOSEUPLARG", "type": "cover", "zoom": [1.0, 1.1, 1.22], "pan": [(0.55, 0.6), (0.4, 0.45), (0.28, 0.4)], "ease": "ease-in"},
    {"img": "LIMNANGSENG", "type": "letterbox", "zoom": [1.0, 1.02, 1.05], "pan": [(0.5, 0.5), (0.54, 0.46), (0.58, 0.42)], "ease": "linear"},
    {"img": "MERLIONANDTHESINGA", "type": "cover", "zoom": [1.18, 1.08, 1.0], "pan": [(0.6, 0.25), (0.5, 0.5), (0.4, 0.75)], "ease": "ease-out"},
    {"img": "REARVIEWOFTHEMERLI", "type": "cover", "zoom": [1.0, 1.1, 1.16], "pan": [(0.35, 0.72), (0.55, 0.5), (0.65, 0.28)], "ease": "ease-in-out"},
    {"img": "SINGAPOREMINIMERLI", "type": "cover", "zoom": [1.0, 1.12, 1.2], "pan": [(0.75, 0.6), (0.5, 0.45), (0.25, 0.35)], "ease": "ease-in"},
    {"img": "MERLIONSTATUEATTOU", "type": "cover", "zoom": [1.0, 1.08, 1.15], "pan": [(0.4, 0.3), (0.55, 0.5), (0.45, 0.65)], "ease": "ease-in"},
    {"img": "PANORAMIO2005", "type": "cover", "zoom": [1.16, 1.06, 1.0], "pan": [(0.3, 0.65), (0.5, 0.45), (0.72, 0.3)], "ease": "ease-out"},
    {"img": "SINGAPOREMERLIONIN", "type": "cover", "zoom": [1.14, 1.06, 1.0], "pan": [(0.55, 0.6), (0.48, 0.45), (0.35, 0.35)], "ease": "ease-out"},
    {"img": "FORMERMERLIONPARK", "type": "cover", "zoom": [1.0, 1.08, 1.14], "pan": [(0.45, 0.3), (0.55, 0.55), (0.65, 0.75)], "ease": "linear"},
]

SCHEDULE = [(0.0, 0), (38.09, 1), (109.51, 2), (181.13, 3), (190.0, 4), (198.0, 5), (204.0, 6), (210.03, 9), (230.52, 7), (250.35, 8)]
TOTAL_DURATION = 259.2
TIMING_JSON = "audio/two-men-behind-singapore-merlion-statue.timing.json"
