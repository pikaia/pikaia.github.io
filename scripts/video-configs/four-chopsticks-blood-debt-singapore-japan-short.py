"""Video config for the "Four Chopsticks and the Blood Debt" post's
YouTube Shorts excerpt.

Self-contained hook: the post's opening (0-38.33s) - the "four
chopsticks" nickname mystery, closing on the reveal: more than 600
remains recovered from mass graves, victims of a massacre Singapore
and Japan spent decades reconciling - a real payoff, not a
mid-sentence cut. (Re-derived a third time after regenerating
narration with the "DD Month" date-ordinal fix - sentences 0-2 are
exactly unchanged, only the cutoff at sentence 3's new start shifts
slightly.)

MEMORIAL (0.667 aspect, portrait) is actually close enough to the
vertical 1080x1920 target (0.5625) to use as cover here, unlike in the
horizontal main video where it needed letterbox. ITEMS (2.141 aspect,
wide landscape) diverges from the vertical target - letterbox.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "MEMORIAL": "https://upload.wikimedia.org/wikipedia/commons/2/27/Civilian_War_Memorial%2C_Singapore-3276.jpg",
    "ITEMS": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Items_found_in_mass_graves_due_to_the_Sook_Ching_massacre_of_1942_by_the_Japanese.jpg",
}

SLIDES = [
    {"img": "MEMORIAL", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
    {"img": "MEMORIAL", "type": "cover", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.45), (0.5, 0.5), (0.5, 0.55)]},
    {"img": "ITEMS", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)]},
]

SCHEDULE = [(0.0, 0), (5.425, 1), (21.125, 2)]
TOTAL_DURATION = 38.325  # real sentence-timing boundary for this post's opening hook
TIMING_JSON = "audio/four-chopsticks-blood-debt-singapore-japan.timing.json"

CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
