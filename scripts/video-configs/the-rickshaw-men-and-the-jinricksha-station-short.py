"""Shorts config for the rickshaw-men post.

Excerpt: the opening hook, sentences 0-6 (0 -> 49.725s, a real sentence
boundary in the timing.json) - the ornate building still on the Tanjong
Pagar corner, built in 1903 to register every rickshaw and license the
men who pulled them; close to 30,000 rickshaws and perhaps 50,000 men
at the peak; the building preserved, the men leaving almost nothing.

4 slides: the station's corner tower today -> its arcaded facade today
-> a c.1930 Chinatown rickshaw rank -> a puller between the shafts,
c.1890. All landscape, so they cover the 1080x1920 frame; the chart is
skipped (16:9, and it falls outside the excerpt anyway).
"""

WIDTH, HEIGHT = 1080, 1920

_C = "https://upload.wikimedia.org/wikipedia/commons/thumb"

IMAGES = {
    "STATION_TOWER": f"{_C}/e/e5/Jinrikisha_Station_Singapore.jpg/1280px-Jinrikisha_Station_Singapore.jpg",
    "STATION_FACADE": f"{_C}/1/1e/Jinrikisha_Station_%2812848777624%29.jpg/1280px-Jinrikisha_Station_%2812848777624%29.jpg",
    "RANK1930": f"{_C}/3/3b/Jinricksha_Station_aan_Neil_Road_te_Singapore%2C_KITLV_104799.tiff/lossy-page1-1280px-Jinricksha_Station_aan_Neil_Road_te_Singapore%2C_KITLV_104799.tiff.jpg",
    "PULLER1890": f"{_C}/0/09/KITLV_-_377462_-_Bengal_man_in_a_Chinese_rickshaw_at_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377462_-_Bengal_man_in_a_Chinese_rickshaw_at_Singapore_-_circa_1890.tif.jpg",
}

SLIDES = [
    {"img": "STATION_TOWER", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "STATION_FACADE", "type": "cover", "zoom": [1.10, 1.05, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"},
    {"img": "RANK1930", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "PULLER1890", "type": "cover", "zoom": [1.0, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
]

# Real sentence starts from the timing.json: s1 3.325, s3 24.325, s5 44.3.
SCHEDULE = [(0.0, 0), (3.325, 1), (24.325, 2), (44.3, 3)]
TOTAL_DURATION = 49.725
TIMING_JSON = "audio/the-rickshaw-men-and-the-jinricksha-station.timing.json"

# Shorts keep burned-in narration captions (muted autoplay); main videos do not -
# they rely on the uploaded .srt.
BURN_CAPTIONS = True
