"""Video config for the St James Power Station post.

The pool is the post and gallery's sixteen pictures: the
station at night in January 2007 (the hero), the c.1900s
postcard of the pre-station shoreline, Keppel Harbour in
1952 and 1971, the just-converted station in November
2006, the second night view, the 2009 dusk event shot,
Dyson's headquarters by day and night in March 2022, the
building today in October 2025 (both chimneys, and the
Sentosa Gateway streetscape), three Terence Ong
conversion-era exteriors (one portrait), and the two
August 2006 harbour panoramas. No Commons photograph of
the station in its working years (1926-1976) exists; the
working-era beats run on the harbour views and the
building's own later photographs.

Named-place audit: no photograph in the pool depicts a
place other than the station and its own harbour. The
Mackenzie Road sentences name a station of which no
photograph exists; they run on the harbour panorama and
the building that replaced it, under titles that do not
claim the picture is Mackenzie Road. The Pasir Panjang
sentences (the 1955 cost comparison, the 1966 phase-out)
run on Keppel Harbour and the station itself, never on a
photograph of Pasir Panjang. The 1952 and 1971 harbour
views are captioned as the harbour, not the plant.
Named-person audit: no portraits exist in the pool; the
sentences naming Clifford, Goh Keng Swee, Lim Loo Cheong
and Lee Hsien Loong run on the building and harbour.

Every slide carries its discreet photo title (standing
rule, Chris, 2026-11-11). The two panoramas are
letterboxed, not covered: at three-to-one and wider, a
cover crop would cut most of the frame away.

56 slides, 794.1s. No slide over 30s; the
longest is the coal-supply slide at 23.47s. Narration:
Kokoro with the OpenVoice clone. Pronunciation overrides
for the post's names filed 2026-11-26, NOT ear-verified
yet. AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "NIGHT1": "https://upload.wikimedia.org/wikipedia/commons/4/42/St_James_Power_Station%2C_Singapore%2C_at_night_-_20070127-01.jpg",
    "NIGHT2": "https://upload.wikimedia.org/wikipedia/commons/1/16/St_James_Power_Station%2C_Singapore%2C_at_night_-_20070127-02.jpg",
    "POSTCARD": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Singapore._View_from_St._James%2C_KITLV_1404953.tiff/1280px-Singapore._View_from_St._James%2C_KITLV_1404953.jpg",
    "HARB52": "https://upload.wikimedia.org/wikipedia/commons/a/ac/Singapore_-_Keppel_Harb_1952.jpg",
    "HARB71": "https://upload.wikimedia.org/wikipedia/commons/0/0f/160a_Singapore_Harbour_from_Frasers_Hill_1971_%2851253058814%29.jpg",
    "NOV06": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Saint_James_Power_Station%2C_Nov_06.JPG",
    "DUSK09": "https://upload.wikimedia.org/wikipedia/commons/7/75/St_James_Power_Station%2C_Singapore_-_20090926.jpg",
    "DYSONDAY": "https://upload.wikimedia.org/wikipedia/commons/f/f3/SJPSDay.jpg",
    "TODAY25": "https://upload.wikimedia.org/wikipedia/commons/8/82/St._James_Power_Station%2C_October_2025.jpg",
    "DAY06A": "https://upload.wikimedia.org/wikipedia/commons/d/d3/St._James_Power_Station.JPG",
    "DAY06B": "https://upload.wikimedia.org/wikipedia/commons/4/4e/St._James_Power_Station_2.JPG",
    "PORTRAIT": "https://upload.wikimedia.org/wikipedia/commons/4/46/St._James_Power_Station_3.JPG",
    "DYSONNIGHT": "https://upload.wikimedia.org/wikipedia/commons/1/12/SJPSNight.jpg",
    "GATEWAY25": "https://upload.wikimedia.org/wikipedia/commons/f/fc/St._James_Power_Station%2C_Sentosa_Gateway%2C_October_2025.jpg",
    "PANOHF": "https://upload.wikimedia.org/wikipedia/commons/b/b6/HarbourFront_and_Keppel_Harbour%2C_panorama%2C_Aug_06.jpg",
    "PANOKEPPEL": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Keppel_Harbour%2C_panorama%2C_Aug_06.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# nightclub-era hero, the shore before it, the monument
# at dusk, and Dyson's headquarters today.
THUMBNAIL = [
    {"img": "NIGHT1", "pan": (0.5, 0.5)},
    {"img": "POSTCARD", "pan": (0.5, 0.5)},
    {"img": "DUSK09", "pan": (0.5, 0.5)},
    {"img": "DYSONDAY", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "NIGHT1", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "St James Power Station"},  # 0  title (5.67s) (s0)
    {"img": "NIGHT2", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "A nightclub, a headquarters"},  # 1  the hook: the answers people give (11.57s) (s1-2)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Singapore's first municipal power station"},  # 2  began as a coal-fired station; fifty years of power (19.18s) (s3-4)
    {"img": "GATEWAY25", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Its second and third lives"},  # 3  the parties and the headquarters came later (7.67s) (s5)
    {"img": "POSTCARD", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The shore before the station"},  # 4  electricity in small pieces; the 1878 arc lamp (16.98s) (s6-7)
    {"img": "PANOKEPPEL", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The tramway era"},  # 5  Mackenzie Road generates for the trams (20.88s) (s8)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Mackenzie Road runs out of road"},  # 6  overtaxed; the 1921 warning (19.60s) (s9-10)
    {"img": "DAY06A", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "A proper power station"},  # 7  built for the town, not borrowed (7.47s) (s11)
    {"img": "PANOHF", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The site: Cape St James"},  # 8  Preece, Cardew and Rider choose the swamp headland (20.18s) (s12-13)
    {"img": "HARB52", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Sea, wharves and rail"},  # 9  cooling water, sea-borne coal, the railway (17.35s) (s14-17)
    {"img": "PORTRAIT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.4], [0.35, 0.4], [0.35, 0.4]]}, "title": "Bought for $375,000, 1924"},  # 10  the site is bought (9.15s) (s18)
    {"img": "DAY06A", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Foundations by Christmas 1925"},  # 11  reclaimed, levelled, foundations complete (13.10s) (s19)
    {"img": "PORTRAIT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.4], [0.5, 0.4], [0.5, 0.4]]}, "title": "Designed by Alexander Gordon"},  # 12  the Chief Municipal Architect's design (10.25s) (s20)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Brick, boilers and turbines"},  # 13  Edwardian facade, six boilers, three turbines (16.27s) (s21)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "First unit: 30 September 1926"},  # 14  demand would not wait; the 2,000 kilowatt unit (16.95s) (s22-23)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Mackenzie Road goes dark"},  # 15  the old supply ceases, 29 October 1926 (8.18s) (s24)
    {"img": "DAY06A", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The whole system, June 1927"},  # 16  St James supplies everything (7.12s) (s25)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "22,000 kilowatts: seven times more"},  # 17  the additional 10,000 kilowatt set (17.27s) (s26)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Room to reach 40,000 kilowatts"},  # 18  designed to be extended (5.53s) (s27)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Opened by Sir Hugh Clifford, 1927"},  # 19  the official opening, 7 November 1927 (18.98s) (s28)
    {"img": "PORTRAIT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.4], [0.65, 0.4], [0.65, 0.4]]}, "title": "Power for 28,255 people"},  # 20  street lighting, tramways, port and industry (8.70s) (s29)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Teaching Singapore to plug in"},  # 21  tariffs fall; the Orchard Road showroom (19.32s) (s30)
    {"img": "HARB52", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Coal by sea, from Manchuria"},  # 22  Japanese tenderers to the late 1930s, then Malaya (23.48s) (s31-32)
    {"img": "HARB71", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The switch to oil, 1940"},  # 23  coal costs rise; two boilers converted (9.72s) (s33)
    {"img": "DAY06A", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Coal for fourteen years only"},  # 24  the label is not wrong, but coal was brief (20.55s) (s34-35)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Blackouts from 1928"},  # 25  the troubled early years (13.03s) (s36-37)
    {"img": "PORTRAIT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.4], [0.65, 0.4], [0.65, 0.4]]}, "title": "Ten minutes to answer a fault"},  # 26  hard, round-the-clock labour (9.03s) (s38)
    {"img": "HARB71", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Occupation years"},  # 27  local staff keep the station running (21.60s) (s39-40)
    {"img": "HARB52", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Paid in rice and vegetables"},  # 28  Lim Loo Cheong's memory (8.15s) (s41)
    {"img": "DAY06A", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The plant the war wrecked"},  # 29  turbines seriously damaged by 1945 (10.80s) (s42)
    {"img": "HARB71", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Post-war strain"},  # 30  demand up half; the failures make headlines (21.02s) (s43-44)
    {"img": "PANOHF", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The 1950 blackout"},  # 31  babies by lamplight; a play lit by headlamps (19.75s) (s45)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The 1951 accident"},  # 32  a welding accident kills two men (7.38s) (s46)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Monday Syndrome"},  # 33  sets started at three in the morning (9.35s) (s47)
    {"img": "HARB52", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The inefficiency verdict"},  # 34  3.57 cents against Pasir Panjang's 1.4 (14.80s) (s48)
    {"img": "TODAY25", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Reopened by Goh Keng Swee, 1960"},  # 35  closed 1956; reopened with 18,000 kilowatts more (16.43s) (s49)
    {"img": "GATEWAY25", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The chimneys of 1960"},  # 36  the two chimneys date from the rebuild (10.95s) (s50)
    {"img": "DAY06A", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The PUB years"},  # 37  the Public Utilities Board, 1963 (12.65s) (s51)
    {"img": "DAY06B", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Overtaken by newer stations"},  # 38  Pasir Panjang and Jurong pass it by (15.22s) (s52-53)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Decommissioned, 1976"},  # 39  the last gas turbines, fifty years on (11.78s) (s54)
    {"img": "PANOHF", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The warehouse years"},  # 40  PSA's automated warehouse, 1983 to 1992 (21.40s) (s55-56)
    {"img": "DAY06A", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Vacant"},  # 41  the station sits empty while the precinct is replanned (6.70s) (s57)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The S$40 million conversion"},  # 42  Dennis Foo, Dennon and Mapletree (22.25s) (s58-59)
    {"img": "NIGHT1", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Launched as a nightclub, 2006"},  # 43  12 outlets, 24 September 2006 (15.07s) (s60)
    {"img": "NIGHT2", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Eleven venues under one roof"},  # 44  Dragonfly, The Boiler Room (12.60s) (s61)
    {"img": "DUSK09", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A national monument, 2009"},  # 45  gazetted the 60th monument, clubs still trading (20.52s) (s62-63)
    {"img": "NOV06", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The party ends, 2018"},  # 46  the heritage award; the lease expires (12.88s) (s64-65)
    {"img": "GATEWAY25", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Dyson announced, 2019"},  # 47  Mapletree announces the restoration (11.22s) (s66)
    {"img": "DYSONNIGHT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The restoration"},  # 48  floating slabs and atriums in the old halls (14.35s) (s67)
    {"img": "DYSONDAY", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Dyson's world headquarters, 2022"},  # 49  opened by PM Lee, 25 March 2022 (13.25s) (s68)
    {"img": "GATEWAY25", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "1,400 people, 560 engineers"},  # 50  the restored monument at work (19.32s) (s69)
    {"img": "DYSONNIGHT", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A second heritage award"},  # 51  the gallery opens; the 2022 award (14.62s) (s70)
    {"img": "DYSONDAY", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The chimney carries a new name"},  # 52  a century on: a technology headquarters (10.88s) (s71)
    {"img": "HARB71", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The harbour transformed"},  # 53  the coal wharves gone; gas by pipe and ship (20.52s) (s72-73)
    {"img": "POSTCARD", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Where the arc begins"},  # 54  power at municipal scale, on a reclaimed swamp (9.50s) (s74)
    {"img": "NIGHT1", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Famous for everything except power"},  # 55  the close (15.95s) (s75)
]

SCHEDULE = [
    (0.000, 0), (5.675, 1), (17.250, 2),
    (36.425, 3), (44.100, 4), (61.075, 5),
    (81.950, 6), (101.550, 7), (109.025, 8),
    (129.200, 9), (146.550, 10), (155.700, 11),
    (168.800, 12), (179.050, 13), (195.325, 14),
    (212.275, 15), (220.450, 16), (227.575, 17),
    (244.850, 18), (250.375, 19), (269.350, 20),
    (278.050, 21), (297.375, 22), (320.850, 23),
    (330.575, 24), (351.125, 25), (364.150, 26),
    (373.175, 27), (394.775, 28), (402.925, 29),
    (413.725, 30), (434.750, 31), (454.500, 32),
    (461.875, 33), (471.225, 34), (486.025, 35),
    (502.450, 36), (513.400, 37), (526.050, 38),
    (541.275, 39), (553.050, 40), (574.450, 41),
    (581.150, 42), (603.400, 43), (618.475, 44),
    (631.075, 45), (651.600, 46), (664.475, 47),
    (675.700, 48), (690.050, 49), (703.300, 50),
    (722.625, 51), (737.250, 52), (748.125, 53),
    (768.650, 54), (778.150, 55)
]
TOTAL_DURATION = 794.1
TIMING_JSON = "audio/st-james-power-station-the-coal-fired-station-of-1926.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
