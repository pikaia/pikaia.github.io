"""Video config for the Fort Canning post's Watch widget / main video.

Reconstructed from the post's own already-published (pre-canonical-
pipeline) live widget script - this post's real video predates
scripts/video-configs/, so this file did not exist until now."""

IMAGES = {
    "FORTCANNINGPARKTRE": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Fort_Canning_Park_Tree_Tunnel.jpg",
    "BATTLEBOXENTRANCE": "https://upload.wikimedia.org/wikipedia/commons/8/8a/BattleBoxEntrance.JPG",
    "DOOROFTHEBATTLEBOX": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Door_of_The_Battle_Box%2C_Singapore_-_20100306.jpg",
    "INTHEBATTLEBOXSING": "https://upload.wikimedia.org/wikipedia/commons/4/4e/In_the_Battle_Box%2C_Singapore_-_panoramio.jpg",
    "FORTCANNINGHILL190": "https://upload.wikimedia.org/wikipedia/commons/9/91/Fort_Canning_Hill-1902.jpg",
    "INTERIOROFTHEBATTL": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Interior_of_the_Battle_Box%2C_Singapore_-_20110506-01.jpg",
    "INTERIOROFTHEBATTL2": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Interior_of_the_Battle_Box%2C_Singapore_-_20120722-01.jpg",
    "LIEUTENANTGENERALA": "https://upload.wikimedia.org/wikipedia/commons/3/39/Lieutenant_General_Arthur_Percival.jpg",
    "YAMASHITAESUZUKI": "https://upload.wikimedia.org/wikipedia/commons/2/21/Yamashita_e_Suzuki.jpg",
}

SLIDES = [
    {"img": "FORTCANNINGPARKTRE", "type": "cover", "zoom": [1.0, 1.1, 1.16], "pan": [(0.5, 0.6), (0.55, 0.4), (0.45, 0.3)], "ease": "ease-in-out"},
    {"img": "BATTLEBOXENTRANCE", "type": "cover", "zoom": [1.0, 1.12, 1.2], "pan": [(0.6, 0.3), (0.5, 0.5), (0.4, 0.7)], "ease": "ease-in"},
    {"img": "DOOROFTHEBATTLEBOX", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.4, 0.7), (0.5, 0.45), (0.6, 0.25)], "ease": "ease-in-out"},
    {"img": "INTHEBATTLEBOXSING", "type": "cover", "zoom": [1.18, 1.08, 1.0], "pan": [(0.3, 0.6), (0.5, 0.45), (0.65, 0.35)], "ease": "ease-out"},
    {"img": "FORTCANNINGHILL190", "type": "cover", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5), (0.55, 0.45), (0.6, 0.4)], "ease": "linear"},
    {"img": "INTERIOROFTHEBATTL", "type": "cover", "zoom": [1.0, 1.1, 1.16], "pan": [(0.35, 0.65), (0.5, 0.45), (0.65, 0.3)], "ease": "ease-in"},
    {"img": "INTERIOROFTHEBATTL2", "type": "cover", "zoom": [1.0, 1.12, 1.18], "pan": [(0.65, 0.35), (0.5, 0.55), (0.35, 0.65)], "ease": "ease-in-out"},
    {"img": "LIEUTENANTGENERALA", "type": "cover", "zoom": [1.0, 1.1, 1.18], "pan": [(0.55, 0.65), (0.45, 0.45), (0.35, 0.3)], "ease": "ease-in"},
    {"img": "YAMASHITAESUZUKI", "type": "cover", "zoom": [1.16, 1.06, 1.0], "pan": [(0.3, 0.4), (0.5, 0.5), (0.7, 0.6)], "ease": "ease-out"},
    {"img": "FORTCANNINGPARKTRE", "type": "cover", "zoom": [1.15, 1.05, 1.0], "pan": [(0.45, 0.4), (0.55, 0.55), (0.65, 0.7)], "ease": "ease-out"},
]

SCHEDULE = [(0.0, 0), (11.26, 1), (22.41, 2), (32.73, 3), (44.56, 4), (48.78, 5), (59.01, 6), (69.75, 7), (76.0, 8), (82.2, 9)]
TOTAL_DURATION = 96.168
TIMING_JSON = "audio/the-bunker-under-fort-canning.timing.json"
