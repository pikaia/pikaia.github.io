"""Shorts config for "The Travel Bug: How Travelling Overseas Stopped Being
Rare".

Excerpt: the opening hook->payoff arc, sentences 1-3 (0 -> 43.85s, a real
sentence boundary in the timing.json). "Going overseas used to be
once-or-twice-in-a-lifetime and formal" -> "today whole families fly to
Bangkok for a weekend the way an earlier generation took a bus to
Malacca." Self-contained; no chart, no mid-sentence cut.

3 slides, same images and zoom/pan percentages as the main config's first
three (cover/letterbox crop normalizes to the 1080x1920 target):
  ST1955      - the 1955 once-in-a-lifetime era
  MSA_707     - the formal full-service carrier
  CHANGI_HALL - the ordinary, crowded present
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "ST1955": f"{_C}/a/a8/ST21August1955.jpg",
    "MSA_707": f"{_C}/0/0d/Malaysia-Singapore_Airlines_B707_at_Zurich_1972.jpg",
    "CHANGI_HALL": f"{_C}/0/05/Changi_Airport%2C_Terminal_1%2C_Departure_Hall.JPG",
}

SLIDES = [
    {"img": "ST1955", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MSA_707", "type": "letterbox", "zoom": [1.08, 1.04, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "CHANGI_HALL", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 17.95, s3 at 25.65.
SCHEDULE = [(0.0, 0), (17.95, 1), (25.65, 2)]
TOTAL_DURATION = 43.85
TIMING_JSON = "audio/the-travel-bug-rise-of-travelling-among-singaporeans.timing.json"

# Shorts want smaller/higher captions than the landscape default:
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
