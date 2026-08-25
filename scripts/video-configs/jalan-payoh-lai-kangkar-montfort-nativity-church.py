"""Video config for the Jalan Payoh Lai / Kangkar post's Watch widget /
main video.

Reconstructed from the post's own already-published (pre-canonical-
pipeline) live widget script - this post's real video predates
scripts/video-configs/, so this file did not exist until now. Slide 1
is a route-walk slide (not representable by watch_video_lib.py's
SLIDES contract - see render_route_clip.py and CLAUDE.md's Route
animations section); build_watch_widget.py flags it MANUAL."""

IMAGES = {
    "HOUGANGLOCATION": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Hougang_location.svg",
    "CHURCHOFTHENATIVIT": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary%2C_October_2025.jpg",
    "CHURCHOFTHENATIVIT2": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary%2C_night%2C_July_2017.jpg",
    "CHURCHOFTHENATIVIT3": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary_5%2C_Nov_06.JPG",
    "ZINCROOFEDHOUSEATK": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Zinc_roofed_house_at_Kampong_Lor_Buangkok.jpg",
    "SUNGEISERANGOONPAN": "https://upload.wikimedia.org/wikipedia/commons/f/f1/Sungei_Serangoon%2C_panorama%2C_Nov_06.jpg",
    "PUNGGOLPARKNOV06": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Punggol_Park%2C_Nov_06.JPG",
    "VILLAGEHOUSEWITHVE": "https://upload.wikimedia.org/wikipedia/commons/d/de/Village_house_with_verandah_and_diner.jpg",
    "HOUGANGHDB3": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Hougang_HDB_3.JPG",
    "HOUGANGSINGLEMEMBE": "https://upload.wikimedia.org/wikipedia/commons/0/06/Hougang_Single_Member_Constituency%2C_2025.svg",
    "WORKERSPARTYHOUGAN": "https://upload.wikimedia.org/wikipedia/commons/9/9c/WorkersPartyHougangSupporters.jpg",
}

SLIDES = [
    {"img": "HOUGANGLOCATION", "type": "cover", "zoom": [1.0, 1.08, 1.14], "pan": [(0.5, 0.4), (0.6, 0.55), (0.45, 0.65)], "ease": "ease-in-out"},
    {"type": "route-walk"},  # not renderable by watch_video_lib.py - see render_route_clip.py; build_watch_widget.py flags this as MANUAL
    {"img": "CHURCHOFTHENATIVIT", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.45, 0.3), (0.55, 0.5), (0.65, 0.65)], "ease": "ease-in-out"},
    {"img": "CHURCHOFTHENATIVIT2", "type": "cover", "zoom": [1.15, 1.06, 1.0], "pan": [(0.6, 0.3), (0.5, 0.5), (0.35, 0.65)], "ease": "ease-out"},
    {"img": "CHURCHOFTHENATIVIT3", "type": "cover", "zoom": [1.0, 1.08, 1.15], "pan": [(0.4, 0.55), (0.52, 0.45), (0.62, 0.35)], "ease": "ease-in"},
    {"img": "CHURCHOFTHENATIVIT", "type": "cover", "zoom": [1.16, 1.06, 1.0], "pan": [(0.35, 0.65), (0.5, 0.45), (0.68, 0.3)], "ease": "ease-out"},
    {"img": "ZINCROOFEDHOUSEATK", "type": "cover", "zoom": [1.0, 1.1, 1.17], "pan": [(0.55, 0.65), (0.48, 0.45), (0.38, 0.3)], "ease": "ease-in-out"},
    {"img": "SUNGEISERANGOONPAN", "type": "cover", "zoom": [1.15, 1.06, 1.0], "pan": [(0.65, 0.35), (0.5, 0.55), (0.32, 0.68)], "ease": "ease-out"},
    {"img": "PUNGGOLPARKNOV06", "type": "cover", "zoom": [1.0, 1.08, 1.14], "pan": [(0.45, 0.6), (0.55, 0.45), (0.65, 0.3)], "ease": "linear"},
    {"img": "VILLAGEHOUSEWITHVE", "type": "cover", "zoom": [1.0, 1.12, 1.2], "pan": [(0.6, 0.3), (0.48, 0.5), (0.35, 0.68)], "ease": "ease-in"},
    {"img": "HOUGANGHDB3", "type": "cover", "zoom": [1.15, 1.05, 1.0], "pan": [(0.35, 0.35), (0.5, 0.5), (0.65, 0.65)], "ease": "ease-in-out"},
    {"img": "HOUGANGSINGLEMEMBE", "type": "cover", "zoom": [1.0, 1.1, 1.16], "pan": [(0.4, 0.45), (0.5, 0.5), (0.62, 0.55)], "ease": "ease-out"},
    {"img": "WORKERSPARTYHOUGAN", "type": "cover", "zoom": [1.0, 1.12, 1.2], "pan": [(0.3, 0.55), (0.48, 0.45), (0.68, 0.32)], "ease": "ease-in"},
    {"img": "CHURCHOFTHENATIVIT", "type": "cover", "zoom": [1.0, 1.09, 1.16], "pan": [(0.65, 0.3), (0.5, 0.5), (0.35, 0.68)], "ease": "ease-in-out"},
    {"img": "CHURCHOFTHENATIVIT2", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.4, 0.6), (0.52, 0.48), (0.62, 0.32)], "ease": "ease-out"},
]

SCHEDULE = [(0.0, 0), (24.775, 1), (49.825, 2), (79.125, 3), (97.425, 4), (110.3, 5), (149.05, 6), (183.05, 7), (216.125, 8), (228.425, 9), (269.55, 10), (287.725, 11), (300.45, 12), (312.675, 13), (336.875, 14)]
TOTAL_DURATION = 361.125
TIMING_JSON = "audio/jalan-payoh-lai-kangkar-montfort-nativity-church-kokoro.timing.json"
