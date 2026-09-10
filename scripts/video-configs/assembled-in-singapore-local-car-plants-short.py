"""Shorts config for the "Assembled in Singapore" car-plants post.

Excerpt: the opening hook, sentences 0-4 (0 -> 47.225s, a real sentence
boundary in the timing.json) - Hyundai has been building electric cars
in Jurong since 2023, the first time cars have been assembled in
Singapore in more than forty years; the country looks like a place that
has no car industry and taxes cars harder than almost anywhere, but for
about half a century it did assemble them, and the last plant shut in
1980.

3 slides: an Ioniq 5 -> the Former Ford Factory -> the Former Ford
Factory in 2025. All landscape / wide, so they cover the 1080x1920 frame.
"""

WIDTH, HEIGHT = 1080, 1920

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "IONIQ5": f"{_C}/4/4d/Hyundai_Ioniq_5.jpg/1280px-Hyundai_Ioniq_5.jpg",
    "HERO_FORD": f"{_C}/2/22/Old_Ford_Motor_Factory_-_www.joyofmuseums.com_-_external.jpg/1280px-Old_Ford_Motor_Factory_-_www.joyofmuseums.com_-_external.jpg",
    "FORD2025": f"{_C}/7/7c/Former_Ford_Factory%2C_October_2025.jpg/1280px-Former_Ford_Factory%2C_October_2025.jpg",
}

SLIDES = [
    {"img": "IONIQ5", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "HERO_FORD", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.4)] * 3, "ease": "ease-in-out"},
    {"img": "FORD2025", "type": "cover", "zoom": [1.10, 1.05, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s2 19.025, s4 35.975.
SCHEDULE = [(0.0, 0), (19.025, 1), (35.975, 2)]
TOTAL_DURATION = 47.225
TIMING_JSON = "audio/assembled-in-singapore-local-car-plants.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
