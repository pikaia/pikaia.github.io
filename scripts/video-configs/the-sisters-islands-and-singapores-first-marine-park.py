"""Video config for the Sisters' Islands post.

The islands from John Edmund Taylor's 1879 watercolour to Stefan Fussan's
2025 photographs of the beaches, lagoons and floating boardwalk, the two
islands from St John's in 2010, Pulau Tekukor and St John's Island, the
southern islands from the air, an 1883 engraving of a giant clam from
Singapore, a banded damselfish off Big Sister's Island, hawksbill
hatchlings, the marine park map and the timeline.

Named-person rule: the legend's sentences naming Minah and Linah show the
islands with no people; Desmond Lee's sentence shows the map. The hawksbill
hatchlings (photographed in the Seychelles) appear only under the general
sentences about the species, not the hatchery ones.

The map, the 1883 engraving, Pulau Tekukor, the damselfish, the hatchlings
and the St John's view are letterboxed; the timeline is shown fixed.

23 slides, 393.4s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Sisters_Islands%2C_Singapore_SF0001.jpg/1280px-Sisters_Islands%2C_Singapore_SF0001.jpg",
    "PAINT": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/John_Edmund_Taylor%2C_St._John%27s_Island_%26_the_Sisters._From_Tanjong_Katong_Singapore_%281879%2C_Wellcome_V0037483%29.jpg/1280px-John_Edmund_Taylor%2C_St._John%27s_Island_%26_the_Sisters._From_Tanjong_Katong_Singapore_%281879%2C_Wellcome_V0037483%29.jpg",
    "SW": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Big_Sisters%27_Islands%2C_Southwest_Beach_SF0001.jpg/1280px-Big_Sisters%27_Islands%2C_Southwest_Beach_SF0001.jpg",
    "MAP": "/assets/images/sisters-islands-map.png",
    "PAIR2010": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sisters_Islands.JPG/1280px-Sisters_Islands.JPG",
    "SOUTH_AIR": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Saint_John%27s_Island_in_Singapore_facing_the_city.jpg/1280px-Saint_John%27s_Island_in_Singapore_facing_the_city.jpg",
    "SE": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Big_Sisters%27_Islands%2C_Southeast_Beach_SF0001.jpg/1280px-Big_Sisters%27_Islands%2C_Southeast_Beach_SF0001.jpg",
    "TL": "/assets/images/sisters-islands-timeline-chart.png",
    "CLAM1883": "https://upload.wikimedia.org/wikipedia/commons/5/53/FMIB_33102_%22Great_Oyster%22_%28giant_clam%3B_Tridacna_gigas%29_from_Singapore%2C_International_Fisheries_Exhibition%2C_London%2C_1883.jpg",
    "TEKUKOR": "https://upload.wikimedia.org/wikipedia/commons/6/65/Tekukor-Island-750x500.jpg",
    "SJ_BEACH": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Saint_John%27s_Island_%28Singapore%29_SF0001.jpg/1280px-Saint_John%27s_Island_%28Singapore%29_SF0001.jpg",
    "DAMSEL": "https://upload.wikimedia.org/wikipedia/commons/3/34/Banded_Damselfish%2C_Big_Sisters%27_Island%2C_Southern_Islands%2C_Singapore_imported_from_iNaturalist_photo_457161894.jpg",
    "BOAT": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/STET_Polaris_berthed_at_Sisters%27_Island_in_2015.jpg/1280px-STET_Polaris_berthed_at_Sisters%27_Island_in_2015.jpg",
    "HAWKS": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Hawksbill_turtle_hatchlings_making_their_way_to_the_sea.jpg",
    "BOARD": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/View_from_Big_Sisters%27_Islands_SF0001.jpg/1280px-View_from_Big_Sisters%27_Islands_SF0001.jpg",
    "SJ_CITY": "https://upload.wikimedia.org/wikipedia/commons/c/c7/View_of_Singapore_from_St_John%27s_Island_in_2023.jpg",
}

# The timeline PNG is the only image not captioned in the post or its gallery.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from the Wellcome Collection, The Straits Times, wildsingapore, Ng, Toh and Chou (2013) and NParks",
}

# The channel's 2x2 thumbnail grid, 1860 to today: a Chinese street in 1860,
# Thian Hock Keng around 1890, North Bridge Road around 1900 and the Ying Fo
# Fui Kun clan hall in 2025.
THUMBNAIL = [
    {"img": "PAINT", "pan": (0.5, 0.5)},
    {"img": "CLAM1883", "pan": (0.5, 0.15)},
    {"img": "PAIR2010", "pan": (0.5, 0.5)},
    {"img": "BOARD", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The map and the small or square images: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterboxed and still, so its labels stay readable.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "HERO", **_IN},           # 0  s0 title: the two islands
    {"img": "PAINT", **_IN},          # 1  s1 two islands side by side; the legend (s1-2)
    {"img": "SW", **_IN},             # 2  s3 howitzers, lagoons, a marine park
    {"img": "MAP", **_PORT},          # 3  s4 Subar Laut and Subar Darat; the channel (s4-6)
    {"img": "PAIR2010", **_IN},       # 4  s7 Minah and Linah (names them: no people, s7-9)
    {"img": "HERO", **_OUT},          # 5  s10 two islands appear (s10-11)
    {"img": "PAINT", **_OUT},         # 6  s12 the colonial era; howitzer practice, 1905 (s12-13)
    {"img": "SOUTH_AIR", **_IN},      # 7  s14 recreation; the 1974-75 reclamation (s14-15)
    {"img": "SE", **_IN},             # 8  s16 Belgian contractors; Sentosa Development Corporation; picnics (s16-17)
    {"img": "SW", **_OUT},            # 9  s18 reef flats buried; reclamation and dredging (s18-19)
    {"img": "TL", **_FIX},            # 10 s20 39.85 to 13.25 sq km; visibility (s20-21)
    {"img": "CLAM1883", **_PORT},     # 11 s22 the surviving reefs; the Blue Plan (s22-23)
    {"img": "MAP", **_PORT_OUT},      # 12 s24 the 2014 announcement (names Desmond Lee: no people)
    {"img": "TEKUKOR", **_PORT},      # 13 s25 about 40 hectares, with Tekukor and St John's
    {"img": "SJ_BEACH", **_IN},       # 14 s26 walks, the gallery on St John's, dive trails
    {"img": "DAMSEL", **_PORT},       # 15 s27 research and restoration; Neptune's cup (s27-28)
    {"img": "BOAT", **_IN},           # 16 s29 artificial reefs, 2018
    {"img": "SE", **_OUT},            # 17 s30 the turtle hatchery; nests at risk (s30-31)
    {"img": "HAWKS", **_PORT},        # 18 s32 hawksbills nest; 2026 numbers (s32-33)
    {"img": "BOARD", **_IN},          # 19 s34 the 2024 reopening; the boardwalk (s34-35)
    {"img": "SJ_CITY", **_PORT},      # 20 s36 solar; Small Sister closed; the ferry (s36-38)
    {"img": "TL", **_FIX},            # 21 s39 where it fits
    {"img": "BOARD", **_OUT},         # 22 s40 keeping what remains
]

SCHEDULE = [
    (0.0, 0), (4.4, 1), (18.3, 2), (36.125, 3), (58.5, 4), (78.45, 5),
    (92.9, 6), (111.125, 7), (130.95, 8), (155.0, 9), (172.6, 10), (200.6, 11),
    (218.675, 12), (231.9, 13), (243.6, 14), (260.675, 15), (275.9, 16), (287.65, 17),
    (304.5, 18), (324.325, 19), (348.125, 20), (368.55, 21), (380.275, 22),
]
TOTAL_DURATION = 393.4
TIMING_JSON = "audio/the-sisters-islands-and-singapores-first-marine-park.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
