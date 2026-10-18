"""Short config for the Tanjong Katong post.

The post's opening, sentences 0-6 (0-64.175s, over the 60s TikTok line): the
seaside before reclamation, the sea now several hundred metres away, and the
coconut coast. Taylor's 1879 sunset and the tall KITLV coconut plantation fill
the vertical frame as covers; the beach photo is letterboxed; the shoreline map
and timeline are letterboxed and frozen.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/John_Edmund_Taylor%2C_Singapore._From_Tanjong_Katong._%281879%2C_Wellcome_V0037488%29.jpg/1280px-John_Edmund_Taylor%2C_Singapore._From_Tanjong_Katong._%281879%2C_Wellcome_V0037488%29.jpg",
    "BEACH": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Strand_van_Tanjong_Katong_te_Singapore%2C_KITLV_104808.tiff/lossy-page1-1280px-Strand_van_Tanjong_Katong_te_Singapore%2C_KITLV_104808.tiff.jpg",
    "MAP2": "/assets/images/katong-shore-map-2.png",
    "TIMELINE": "/assets/images/katong-timeline-chart.png",
    "COCO": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Cocoanut_plantation_Tanjong_Katong._Singapore.%2C_KITLV_1404873.tiff/lossy-page1-1280px-Cocoanut_plantation_Tanjong_Katong._Singapore.%2C_KITLV_1404873.tiff.jpg",
}

CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "MAP2": "Map by Lesser Known Singapore; map data (c) OpenStreetMap contributors",
}

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _v(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


SLIDES = [
    {"img": "HERO", **_v([1.0, 1.04, 1.08], [(0.5, 0.5)] * 3)}, # s0  title
    {"img": "BEACH", **_LB},                                    # s1  Singapore's seaside; the seafront roads (s2)
    {"img": "MAP2", **_GFX},                                    # s3  the sea now several hundred metres away
    {"img": "TIMELINE", **_GFX},                                # s4  coconut coast to inland suburb
    {"img": "COCO", **_v([1.0, 1.03, 1.06], [(0.5, 0.5)] * 3)}, # s5  'turtle point'; cotton, then coconuts (s6)
]
SCHEDULE = [(0.0, 0), (5.925, 1), (21.275, 2), (34.4, 3), (49.95, 4)]
TOTAL_DURATION = 64.175
TIMING_JSON = "audio/tanjong-katong-by-the-sea-from-dunmans-bungalows-to-the-seaside-resort.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70
