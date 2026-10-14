"""Video config for the Tani Yutaka post.

Tani's one known photograph (the seated Commons copy, plus the tighter crop
of the same picture, video-only) carries the sentences about him; it is small,
so it is always letterboxed with a modest zoom. The two whole newspaper pages,
the Malaya Tribune of 9 November 1933 and the Syonan Shimbun of 17 July 1943,
are letterboxed, never cropped to one story. Named people get their own
photograph or none: Kamoto Toshio (s30), Fujiwara Iwaichi (s34, and s39 with
the April 1942 Domei photograph of him greeting Giani Pritam Singh) and
General Yamashita (s52-53, a 1943 portrait, video-only). Nakata Koji, Wada Ben
and the girl, Shizuko, have no image, so their sentences get the newspaper
page, the cemetery and Kuala Terengganu. Video-only: the crop of Tani's
photograph, Kuala Terengganu's Chinatown (three more views), Japanese troops
crossing a river, the Fujiwara photograph, the Yamashita portrait and the
Japanese war memorial in the cemetery. The timeline is letterboxed and frozen.

43 slides, 603.875s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HERO": f"{_U}/e/e0/Tani_Yutaka_seated%2C_in_Malay_dress.webp",
    "KT3": f"{_C}/c/c3/KT_Chinatown_3.jpg/1280px-KT_Chinatown_3.jpg",
    "TRIBUNE": f"{_A}/malaya-tribune-1933-11-09-page-7.jpg",
    "KAMOTO": f"{_U}/7/77/Toshio_Kamoto.jpg",
    "BRIDGE": f"{_C}/0/0e/Royal_Engineers_prepare_to_blow_up_a_bridge_in_Malaya.jpg/1280px-Royal_Engineers_prepare_to_blow_up_a_bridge_in_Malaya.jpg",
    "SY1943": f"{_A}/syonan-shimbun-1943-07-17-page-2.jpg",
    "TIMELINE": f"{_A}/tani-timeline-chart.png",
    "CEM1": f"{_C}/1/12/Japanese_Cemetery_Park_1.jpg/1280px-Japanese_Cemetery_Park_1.jpg",
    # Gallery images:
    "FUJIWARA": f"{_U}/8/87/Fujiwara_Iwaichi.jpg",
    "BICYCLE": f"{_C}/9/9a/Japanese_bicycle_troops_crossing_a_river.%2C_Malayan_campaign%2C_1942.jpg/1280px-Japanese_bicycle_troops_crossing_a_river.%2C_Malayan_campaign%2C_1942.jpg",
    "LABIS": f"{_C}/4/4f/Destroyed_bridge_and_temporary_bridge_in_Labis%2C_January_22_1942.jpg/1280px-Destroyed_bridge_and_temporary_bridge_in_Labis%2C_January_22_1942.jpg",
    "KOTA": f"{_U}/3/39/Kota_Bahru_-_Kelantan_1941.jpg",
    "JOHORE": f"{_U}/4/4e/Japanese_troops_at_Johore.jpg",
    "MAP": f"{_U}/b/bf/Pacific_War_-_Malaya_1941-42_-_Map.jpg",
    "JNAT": f"{_C}/7/74/Japanese_nationals_arriving_at_custom_barriers_while_leaving_Singapore%2C_1942_%2823918242273%29.jpg/1280px-Japanese_nationals_arriving_at_custom_barriers_while_leaving_Singapore%2C_1942_%2823918242273%29.jpg",
    "KT1": f"{_C}/4/4c/KT_Chinatown_1.jpg/1280px-KT_Chinatown_1.jpg",
    "KTGATE": f"{_C}/b/b8/Kampung_Cina_Kuala_Terengganu.jpg/1280px-Kampung_Cina_Kuala_Terengganu.jpg",
    "CEMGATE": f"{_C}/6/6c/Japanese_Cemetery_Park.jpg/1280px-Japanese_Cemetery_Park.jpg",
    "PRAYER": f"{_U}/b/bf/Prayer_hall%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg",
    # Not in this post's captions (credited below):
    "HEROC": f"{_U}/a/a8/Yutaka_Tani.png",
    "KT4": f"{_C}/2/24/KT_Chinatown_4.jpg/1280px-KT_Chinatown_4.jpg",
    "KAKILIMA": f"{_C}/2/26/Kaki-Lima-Chinatown.jpg/1280px-Kaki-Lima-Chinatown.jpg",
    "ORNAMENT": f"{_C}/f/f0/Ornamental_facade.jpg/1280px-Ornamental_facade.jpg",
    "KAMPUNG2": f"{_C}/3/33/Kampung_cina_kuala_terengganu.jpg/1280px-Kampung_cina_kuala_terengganu.jpg",
    "TROOPS": f"{_U}/e/e0/Japanese_troops_crossing_a_river.jpg",
    "FKIKAN": f"{_U}/9/9a/Fujiwara_Kikan.jpg",
    "YAMAPORT": f"{_U}/f/f5/Yamashita_Tomoyuki.jpg",
    "WARMEM": f"{_U}/e/ea/Japanese_war_memorial%2C_Japanese_Cemetery_Park%2C_Singapore_-_20070526.jpg",
}

# Credits for images not captioned in the post or its gallery.
CREDITS = {
    "TIMELINE": "Timeline by Lesser Known Singapore",
    "HEROC": "Unknown photographer, public domain, via Wikimedia Commons",
    "KT4": "Fikku fiq, CC BY-SA 4.0, via Wikimedia Commons",
    "KAKILIMA": "Fikku fiq, CC BY-SA 4.0, via Wikimedia Commons",
    "ORNAMENT": "Fikku fiq, CC BY-SA 4.0, via Wikimedia Commons",
    "KAMPUNG2": "Manis leting, CC BY-SA 4.0, via Wikimedia Commons",
    "TROOPS": "Australian War Memorial, public domain, via Wikimedia Commons",
    "FKIKAN": "Domei Tsushin, public domain, via Wikimedia Commons",
    "YAMAPORT": "Unknown Japanese Army photographer, public domain, via Wikimedia Commons",
    "WARMEM": "Aldwinteo, CC BY-SA 3.0, via Wikimedia Commons",
}

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Tani's small photograph, portraits, newspaper pages and tall photos: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}

SLIDES = [
    {"img": "HERO", **_PORT},         # 0  s0   title
    {"img": "CEM1", **_IN},           # 1  s1   died of malaria in a Singapore hospital, March 1942
    {"img": "KT3", **_IN},            # 2  s2   grew up in Kuala Terengganu
    {"img": "HERO", **_PORT_OUT},     # 3  s3   his name was Tani Yutaka
    {"img": "SY1943", **_PORT},       # 4  s4   the wartime film called him Harimau Malai
    {"img": "TRIBUNE", **_PORT},      # 5  s5   the few records from his own time
    {"img": "KT1", **_IN},            # 6  s6   born 1911, a barber's son
    {"img": "KTGATE", **_PORT},       # 7  s7   the family moves to Kuala Terengganu
    {"img": "KT4", **_PORT},          # 8  s8   schooled in Japan, back at 15
    {"img": "HERO", **_PORT},         # 9  s9   became a Muslim; the photograph
    {"img": "JNAT", **_IN},           # 10 s11  back to Japan for his conscription exam
    {"img": "KAKILIMA", **_PORT},     # 11 s14  6 November 1933
    {"img": "TRIBUNE", **_PORT},      # 12 s15  the Malaya Tribune report
    {"img": "ORNAMENT", **_IN},       # 13 s18  an eight-year-old girl killed
    {"img": "TRIBUNE", **_PORT_OUT},  # 14 s20  no motive disclosed; near the Customs Office
    {"img": "KAMPUNG2", **_PORT},     # 15 s22  Japanese accounts name her Shizuko
    {"img": "TIMELINE", **_GFX},      # 16 s23  the Japanese version; the family leaves in 1934
    {"img": "HEROC", **_PORT},        # 17 s26  the next six years, from Japanese books
    {"img": "KOTA", **_IN},           # 18 s28  arrested in Hat Yai, southern Thailand
    {"img": "MAP", **_PORT},          # 19 s29  Japan prepares for war in Southeast Asia
    {"img": "KAMOTO", **_PORT},       # 20 s30  Kamoto Toshio pays his bail
    {"img": "TROOPS", **_PORT},       # 21 s31  the gang; the Jitra line
    {"img": "FUJIWARA", **_PORT},     # 22 s34  the F Kikan under Major Fujiwara
    {"img": "BRIDGE", **_IN},         # 23 s35  removing demolition charges from bridges
    {"img": "BICYCLE", **_IN},        # 24 s36  malaria on the way south; no quinine
    {"img": "JOHORE", **_PORT},       # 25 s38  field hospital in Johor Bahru
    {"img": "FKIKAN", **_IN},         # 26 s39  Fujiwara orders him moved to Singapore
    {"img": "HERO", **_PORT_OUT},     # 27 s40  buried with Muslim rites, place unknown
    {"img": "WARMEM", **_IN},         # 28 s41  recorded as war dead; Yasukuni
    {"img": "CEMGATE", **_IN},        # 29 s42  the memorial stone in the Japanese Cemetery Park
    {"img": "SY1943", **_PORT},       # 30 s43  the Japanese press makes him a hero
    {"img": "TIMELINE", **_GFX},      # 31 s45  Daiei releases Marai no Tora, June 1943
    {"img": "KOTA", **_OUT},          # 32 s46  set in Kota Bharu; shot partly in Singapore
    {"img": "SY1943", **_PORT_OUT},   # 33 s47  the Syonan Shimbun's plot summary
    {"img": "LABIS", **_IN},          # 34 s49  the film's raids and the dam
    {"img": "TRIBUNE", **_PORT_OUT},  # 35 s51  set beside the 1933 report
    {"img": "YAMAPORT", **_PORT},     # 36 s52  General Yamashita, the other Tiger of Malaya
    {"img": "HEROC", **_PORT_OUT},    # 37 s54  Kaiketsu Harimao, modelled on Tani
    {"img": "PRAYER", **_IN},         # 38 s56  the 1989 film Harimao
    {"img": "SY1943", **_PORT},       # 39 s57  Teater Ekamatra re-enacts the 1943 film
    {"img": "CEM1", **_OUT},          # 40 s59  why it matters: the memorial stone
    {"img": "KT3", **_OUT},           # 41 s60  the records of his own time
    {"img": "HERO", **_PORT_OUT},     # 42 s61  reading the story against the newspapers
]

SCHEDULE = [(0.0, 0), (5.375, 1), (16.6, 2), (30.05, 3), (33.175, 4), (42.075, 5), (52.525, 6), (64.65, 7), (73.025, 8), (84.65, 9), (101.8, 10), (123.2, 11), (131.825, 12), (161.25, 13), (172.8, 14), (183.575, 15), (193.3, 16), (221.85, 17), (245.7, 18), (255.6, 19), (262.575, 20), (280.3, 21), (303.675, 22), (311.625, 23), (324.55, 24), (341.2, 25), (346.925, 26), (359.225, 27), (366.75, 28), (378.125, 29), (385.2, 30), (399.75, 31), (409.25, 32), (425.775, 33), (455.225, 34), (477.05, 35), (493.975, 36), (509.15, 37), (531.65, 38), (541.55, 39), (563.05, 40), (577.025, 41), (595.95, 42)]
TOTAL_DURATION = 603.875
TIMING_JSON = "audio/tani-yutaka-the-tiger-of-malaya-the-man-and-the-wartime-legend.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
