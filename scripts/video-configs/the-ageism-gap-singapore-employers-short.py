"""Shorts config for "The Ageism Gap: What Singapore Employers Say vs. What
They Do".

Excerpt: the opening hook -> turn, sentences 1-3 (0 -> 42.525s, a real
sentence boundary in the timing.json). "A 61-year-old is redoing her
resume because CPF doesn't stretch and re-employment runs out at 68" ->
"on paper the whole system says older workers are welcome" -> "in
practice a lot of resumes like hers go nowhere." Self-contained, no
mid-sentence cut.

3 slides, same images / zoom-pan percentages as the main config's
opening: SKYLINE (the CBD, the jobseeker) -> MOL (the policy apparatus)
-> SKYLINE (in practice).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "SKYLINE": f"{_C}/1/1e/Singapore_Skyline_Raffles_Place.jpg",
    "MOL": f"{_C}/a/a3/Former_Ministry_of_Labour_Building%2C_October_2025.jpg",
}

SLIDES = [
    {"img": "SKYLINE", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.30, 0.52), (0.50, 0.50), (0.70, 0.48)], "ease": "ease-in-out"},
    {"img": "MOL", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.35, 0.50), (0.50, 0.50), (0.62, 0.50)], "ease": "ease-in-out"},
    {"img": "SKYLINE", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.68, 0.52), (0.50, 0.50), (0.34, 0.48)], "ease": "ease-out"},
]

# Real sentence starts from the timing.json: s2 at 22.775, s3 at 34.85.
SCHEDULE = [(0.0, 0), (22.775, 1), (34.85, 2)]
TOTAL_DURATION = 42.875
TIMING_JSON = "audio/the-ageism-gap-singapore-employers.timing.json"

# Shorts want smaller/higher captions than the landscape default:
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
