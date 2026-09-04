"""Shorts config for the pineapple-kings post.

Excerpt: the opening hook, sentences 0-4 (0 -> 49.975s, a real sentence
boundary in the timing.json) - the "world's largest exporter of canned
pineapple" claim, the fruit's near-total absence from how Singapore
tells its own story now, and the payoff that it seeded three lasting
fortunes.

3 slides: the 1946 group photo (Tan Kah Kee, Lee Kong Chian, Tan Lark
Sye) -> young Tan Kah Kee -> Lim Nee Soon. GROUP is the one landscape-ish
source (933x674) here, so it uses cover (a portrait source letterboxed
into a vertical frame already fills most of the height; a landscape one
would shrink to a band across the middle - see CLAUDE.md/production
pipeline notes on this).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "GROUP": f"{_C}/a/a6/Tan_Kah_Kee%2C_Lee_Kong_Chian%2C_and_Tan_Lark_Sye%2C_1946.png",
    "TKKYOUNG": f"{_C}/0/03/%E5%B9%B4%E8%BD%BB%E7%9A%84%E9%99%88%E5%98%89%E5%BA%9A.jpg",
    "NEESOON": f"{_C}/2/24/Lim_Nee_Soon.png",
}

SLIDES = [
    {"img": "GROUP", "type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "TKKYOUNG", "type": "letterbox", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "NEESOON", "type": "letterbox", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s2 at 19.875, s4 at 31.8.
SCHEDULE = [(0.0, 0), (19.875, 1), (31.8, 2)]
TOTAL_DURATION = 49.975
TIMING_JSON = "audio/singapore-canned-pineapple-kings.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
