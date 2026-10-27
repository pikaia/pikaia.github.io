"""Video config for the gas pipelines post.

Senoko Power Station in 2007 and 2020, Senoko across the Johor Strait from
Malaysia, the old Pasir Panjang Power Station in 2018 and 2025, Jurong
Island from the sea, from Jurong Hill and at night, a Jurong Island power
station, the Kertih River in Terengganu, a 1968 Admiralty chart of the
Natuna Islands and a 2017 map of the Natuna Sea, two pipelaying ships and
LNG carriers (stand-ins, captioned as such in the post and gallery), the
pipeline map, the gas-share chart and the timeline.

Named-person rule: Lawrence Wong and Tan See Leng have no photos here, so
their sentences show power stations and Jurong Island with no people.

The maps, the charts, the small Power Seraya photo and the timeline are
letterboxed; the chart and timeline are fixed.

34 slides, 605.25s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "SENOKO07": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Senoko_Power_Station.JPG/1280px-Senoko_Power_Station.JPG",
    "SUNSET": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg/1280px-Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg",
    "JI2011": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Jurong_Island%2C_Singapore_-_20110227-01.jpg/1280px-Jurong_Island%2C_Singapore_-_20110227-01.jpg",
    "MAP": "/assets/images/gas-pipelines-map.png",
    "PASIR18": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Pasir_Panjang_Power_Station.jpg/1280px-Pasir_Panjang_Power_Station.jpg",
    "PLP": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/PLPPowerPlant.jpg/1280px-PLPPowerPlant.jpg",
    "SERAYA": "https://upload.wikimedia.org/wikipedia/commons/d/db/Power_Seraya_Power_Station.jpg",
    "JHILL": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg/1280px-Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg",
    "JI2026": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Jurong_Island_June_2026.jpg/1280px-Jurong_Island_June_2026.jpg",
    "PASIR25": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Pasir_Panjang_Power_Station_%28decommissioned%29_20251015_150041.jpg/1280px-Pasir_Panjang_Power_Station_%28decommissioned%29_20251015_150041.jpg",
    "SENOKO20": "https://upload.wikimedia.org/wikipedia/commons/4/49/Senoko_Power_Station_located_on_the_northern_coast_of_Singapore.jpg",
    "KERTIH": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Kertih_05.04.12.JPG/1280px-Kertih_05.04.12.JPG",
    "PANO": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Panorama_view_of_Singapore_Senoko_power_station_from_in_front_of_Zon_Hotel_in_Malaysia_-_panoramio.jpg/1280px-Panorama_view_of_Singapore_Senoko_power_station_from_in_front_of_Zon_Hotel_in_Malaysia_-_panoramio.jpg",
    "ADM68": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Admiralty_Chart_No_1348_Kepulauan_Natuna%2C_Published_1968.jpg/1280px-Admiralty_Chart_No_1348_Kepulauan_Natuna%2C_Published_1968.jpg",
    "NATMAP": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Map_North_Natuna_Sea.jpg/1280px-Map_North_Natuna_Sea.jpg",
    "SAPURA": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Pipelay_vessel_Sapura_Jade_-_Heijplaat_-_Heysehaven_-_Rotterdam_%2822416866235%29.jpg/1280px-Pipelay_vessel_Sapura_Jade_-_Heijplaat_-_Heysehaven_-_Rotterdam_%2822416866235%29.jpg",
    "SEVENSUN": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Pipelay_vessel_Seven_Sun_-_Koninklijke_IHC_-_Kinderdijk_%2818346811469%29.jpg/1280px-Pipelay_vessel_Seven_Sun_-_Koninklijke_IHC_-_Kinderdijk_%2818346811469%29.jpg",
    "CHART": "/assets/images/gas-share-electricity-chart.png",
    "LNGDSME": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/LNG_Carrier_DSME.jpg/1280px-LNG_Carrier_DSME.jpg",
    "JNIGHT": "https://upload.wikimedia.org/wikipedia/commons/7/72/Aerial_view_of_Jurong_Island_from_Hill_top.jpg",
    "TL": "/assets/images/gas-pipelines-timeline-chart.png",
}

# The timeline PNG and the gas-share chart are not captioned as images in the post.
CREDITS = {
    "TL": "Timeline by Lesser Known Singapore, from the National Archives of Singapore, NLB Infopedia, the New Straits Times, the Oil & Gas Journal, the Singapore Government, METI and Bloomberg",
    "CHART": "Chart by Lesser Known Singapore, from SG101 and the Energy Market Authority's Singapore Energy Statistics",
}

# The channel's 2x2 thumbnail grid, from the oil years to today: the old
# Pasir Panjang Power Station, Senoko across the Johor Strait in 2008,
# Jurong Island at night in 2009 and Jurong Island from Jurong Hill in 2021.
THUMBNAIL = [
    {"img": "PASIR18", "pan": (0.5, 0.5)},
    {"img": "PANO", "pan": (0.5, 0.5)},
    {"img": "JNIGHT", "pan": (0.5, 0.5)},
    {"img": "JHILL", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The maps, portrait and small images and the newspaper pages: letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_PORT_OUT = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The timeline: letterboxed and still, so its labels stay readable.
_FIX = {"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    {"img": "SENOKO07", **_IN},       # 0  s0 title: Senoko
    {"img": "SUNSET", **_IN},         # 1  s1 the October 2026 cut; nothing went dark (s1-2)
    {"img": "JI2011", **_IN},         # 2  s3 EMA: under 2% of daily gas
    {"img": "MAP", **_PORT},          # 3  s4 three pipes under the sea
    {"img": "PASIR18", **_IN},        # 4  s5 the PUB you remember; how it works now (s5-7)
    {"img": "PLP", **_IN},            # 5  s8 95% from gas; all imported (s8-9)
    {"img": "SERAYA", **_PORT},       # 6  s10 the generating companies; the wholesale market (s10-11)
    {"img": "JHILL", **_IN},          # 7  s12 SP Group's grid; your bill (s12-13)
    {"img": "JI2026", **_IN},         # 8  s14 the PUB is water; the new ministry (s14-15)
    {"img": "PASIR25", **_IN},        # 9  s16 the PUB of 1963; oil-fired stations (s16-17)
    {"img": "JI2011", **_OUT},        # 10 s18 oil and the refineries; prices swing (s18-19)
    {"img": "SENOKO20", **_IN},       # 11 s20 gas burns cleaner; no gas fields of its own (s20-21)
    {"img": "KERTIH", **_IN},         # 12 s22 the answer from Malaysia; Petronas (s22-23)
    {"img": "PANO", **_IN},           # 13 s24 Pasir Gudang to Senoko; January 1992 (s24-25)
    {"img": "SENOKO07", **_OUT},      # 14 s26 the PUB broken up; Singapore Power; EMA (s26-28)
    {"img": "ADM68", **_PORT},        # 15 s29 far out in the South China Sea; West Natuna (s29-30)
    {"img": "NATMAP", **_PORT},       # 16 s31 the 1998 deal with SembGas
    {"img": "SAPURA", **_IN},         # 17 s32 a 640 km pipeline; gas in 2001 (s32-33)
    {"img": "MAP", **_PORT_OUT},      # 18 s34 the third pipe, from the south (s34-35)
    {"img": "SEVENSUN", **_IN},       # 19 s36 PowerGas and PGN; opened August 2003 (s36-37)
    {"img": "CHART", **_FIX},         # 20 s38 gas takes over: 26% to almost all (s38-40)
    {"img": "LNGDSME", **_IN},        # 21 s41 two neighbours; the 2006 LNG decision (s41-42)
    {"img": "JNIGHT", **_IN},         # 22 s43 the terminal's first cargo, 2013 (s43-44)
    {"img": "JHILL", **_OUT},         # 23 s45 57% LNG, 43% pipeline; the 2022 agreement (s45-46)
    {"img": "ADM68", **_PORT_OUT},    # 24 s47 the October cut from Natuna and Sumatra (s47-48)
    {"img": "SUNSET", **_OUT},        # 25 s49 the Batam blackout
    {"img": "PLP", **_OUT},           # 26 s50 EMA: under 2%; GasCo can import more LNG
    {"img": "JI2026", **_OUT},        # 27 s51 Lawrence Wong (names him: no people)
    {"img": "LNGDSME", **_OUT},       # 28 s52 the Qatar shock (s52-53)
    {"img": "SENOKO20", **_OUT},      # 29 s54 Tan See Leng (names him: no people)
    {"img": "TL", **_FIX},            # 30 s55 beyond gas: the 2012 study, the 2014 programme (s55-57)
    {"img": "SERAYA", **_PORT_OUT},   # 31 s58 the four agreements; no decision yet (s58-59)
    {"img": "PANO", **_OUT},          # 32 s60 where it fits: always imported (s60-61)
    {"img": "SENOKO07", **_IN},       # 33 s62 under 2% of a day's demand
]

SCHEDULE = [
    (0.0, 0), (2.975, 1), (19.925, 2), (30.45, 3), (42.4, 4), (60.95, 5),
    (73.725, 6), (91.2, 7), (114.55, 8), (132.425, 9), (158.225, 10), (172.05, 11),
    (182.75, 12), (198.95, 13), (219.55, 14), (248.775, 15), (265.5, 16), (282.4, 17),
    (300.1, 18), (322.425, 19), (346.15, 20), (362.475, 21), (383.9, 22), (396.525, 23),
    (423.3, 24), (445.65, 25), (458.975, 26), (477.325, 27), (488.6, 28), (507.425, 29),
    (518.95, 30), (548.8, 31), (572.025, 32), (596.425, 33),
]
TOTAL_DURATION = 605.25
TIMING_JSON = "audio/the-pipelines-that-feed-singapore.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
