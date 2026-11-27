"""Video config for the 1973 oil shock post.

The pool is the post and gallery's sixteen pictures: two
genuine photographs of Singapore in the embargo winter
itself (Rainer Halama's street scene, the hero, and his
Singapore River view, both 1973/74), the refining shore
(Pulau Bukom from Sentosa; the Jurong panorama from
Jurong Hill), oil-fired Senoko, a modern Esso station,
HDB blocks lit at night, the embargo's two principals
(King Faisal at the White House in 1971; Sheikh Yamani's
CIA portrait), five of David Falconer's Oregon Documerica
photographs of the American crisis, and a self-made chart
of world crude prices 1970-1980 from the BP Statistical
Review benchmark series, held at /assets/images/.

Named-place audit: the Bukom sentences run on the Bukom
photograph; the Laju sentence likewise. The sentences
naming the four refinery sites run on the refining coast
(the Jurong panorama) under a title that names no single
site. The street-lighting sentences name five roads; they
run on the lit HDB blocks and the period street, under
titles that do not claim the pictures are those roads.
The Plaza Singapura sentence runs on the period street
under the beat title "The crisis in odd corners" - the
title does not claim the photograph is the centre.
Named-person audit: Yamani's portrait sits under his own
sentence. Faisal's photograph sits under the embargo
sentences (Saudi Arabia is named; he is not, and the
title does not name him). The Reagan sentences run on the
city street - no portrait exists in the pool - under a
title that does not name him. The Oregon photographs sit
only under the two America sentences and are titled as
America. The chart is letterboxed and held static, per
the graphics rule. The Jurong panorama is letterboxed:
at 3.4-to-1 a cover crop would cut most of it away.

Two gallery photographs are deliberately unused in either
config: the Oregon newspaper reader and "Never on Sunday"
fit no Singapore sentence honestly, and the America beat
already carries three Oregon frames. NOGAS is in IMAGES
for the THUMBNAIL grid; its slide is in the Short.

59 slides, 948.95s. No slide over 30s; the longest is
the consumption slide at 26.30s. Narration: Kokoro with
the OpenVoice clone. Pronunciation overrides for the
post's names filed 2026-11-27, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "STREET": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Singapore-Street_Scene-1973-74-WUS08222.jpg",
    "RIVER": "https://upload.wikimedia.org/wikipedia/commons/4/42/Singapore-Singapore_River-1973-74-WUS08203.jpg",
    "BUKOM": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Pulau_Bukom_from_Sentosa.JPG",
    "JURONGPANO": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Jurong_Hill_aerial_panorama.jpg",
    "SENOKO": "https://upload.wikimedia.org/wikipedia/commons/d/d2/Senoko_Power_Station.JPG",
    "ESSO": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Esso_Singapore.JPG",
    "HDBNIGHT": "https://upload.wikimedia.org/wikipedia/commons/b/b9/HDB_at_night_%288144994286%29.jpg",
    "FAISAL": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Arrival_ceremony_welcoming_King_Faisal_of_Saudi_Arabia_05-27-1971.jpg",
    "YAMANI": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Saudi_Oil_Minister_Ahmed_Zaki_Yamani_%2810729444005%29.jpg",
    "CHART": "/assets/images/crude-oil-prices-1970-1980.png",
    "FLAG": "https://upload.wikimedia.org/wikipedia/commons/9/93/THE_STATE_OF_OREGON_HAD_A_FLAG_SYSTEM_IN_ADDITION_TO_ITS_ODD-EVEN_SYSTEM_OF_ALLOCATING_GASOLINE._A_GREEN_FLAG_MEANT..._-_NARA_-_555485.jpg",
    "ODDEVEN": "https://upload.wikimedia.org/wikipedia/commons/e/e9/THE_STATE_OF_OREGON_WAS_THE_FIRST_TO_GO_TO_A_SYSTEM_OF_ODD_AND_EVEN_NUMBERS_DURING_THE_GASOLINE_CRISIS_IN_THE_FALL..._-_NARA_-_555489.jpg",
    "NOGAS": "https://upload.wikimedia.org/wikipedia/commons/4/4f/%22NO_GAS%22_SIGNS_WERE_A_COMMON_SIGHT_IN_OREGON_DURING_THE_FALL_OF_1973%2C_SUCH_AS_AT_THIS_STATION_IN_LINCOLN_CITY_ALONG..._-_NARA_-_555416.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# winter city, the shock abroad, the price, the lights.
THUMBNAIL = [
    {"img": "STREET", "pan": (0.5, 0.5)},
    {"img": "NOGAS", "pan": (0.5, 0.5)},
    {"img": "CHART", "pan": (0.5, 0.5)},
    {"img": "HDBNIGHT", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "1973: The Oil Shock"},  # 0  title (5.67s) (s0)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The winter the lights stayed on"},  # 1  the hook: no oil of its own (16.80s) (s1-2)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The price quadrupled in three months"},  # 2  the producers cut; the price climbs (17.88s) (s3)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A top-three refining centre"},  # 3  the thesis; top three with Houston and Rotterdam (14.75s) (s4-5)
    {"img": "JURONGPANO", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Four refineries in a decade"},  # 4  Shell, Esso, Mobil, SPC named; the refining coast (23.77s) (s6)
    {"img": "SENOKO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "A third of all manufacturing"},  # 5  output share; crude in, products out (20.70s) (s7-8)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Everything ran on oil"},  # 6  the Horn quote opens (15.10s) (s9-10)
    {"img": "SENOKO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "All electricity from oil"},  # 7  the quote completes; an oil economy exposed (18.65s) (s11-13)
    {"img": "FAISAL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The embargo, October 1973"},  # 8  war, the cut, the embargo; not a target (17.68s) (s14-15)
    {"img": "CHART", **{"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]], "ease": "linear"}, "title": "From $3.00 to $11.65 a barrel"},  # 9  exposure through the world market; the posted price (25.60s) (s16-17)
    {"img": "YAMANI", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.4], [0.5, 0.4], [0.5, 0.4]]}, "title": "Yamani, the embargo's face"},  # 10  his own sentence, his portrait (16.38s) (s18)
    {"img": "STREET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "How much crude, at what price"},  # 11  the refining island's question (9.78s) (s19-20)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The squeeze, in the cables"},  # 12  the declassified record opens (8.75s) (s21)
    {"img": "STREET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "A 10 percent cut, region-wide"},  # 13  the 8 November cable (14.00s) (s22)
    {"img": "SENOKO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Committee and contingency plan"},  # 14  Ngiam Tong Dow's committee (15.18s) (s23)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Expect 10 to 20 percent less crude"},  # 15  the 9 November cable (13.53s) (s24)
    {"img": "JURONGPANO", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "SPC, the newest refinery"},  # 16  SPC's fear of being cut off (16.73s) (s25)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "A 'good guy list'"},  # 17  the approach to Kuwait and Saudi Arabia (16.43s) (s26)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Aramco arithmetic"},  # 18  35 percent to Exxon; 5 to 10 at Esso (16.35s) (s27-28)
    {"img": "SENOKO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "No fuel for the US military"},  # 19  the Saudi condition; force majeure (17.52s) (s29)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Not another Rotterdam"},  # 20  no onward shipments to embargoed destinations (14.42s) (s30-31)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Do not do a thing"},  # 21  the non-aligned line, 29 November (16.75s) (s32-33)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "No fuel for the envoy"},  # 22  Shell refuses the Reagan aircraft (22.48s) (s34)
    {"img": "JURONGPANO", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A warning for ASEAN"},  # 23  the partners who took the products (13.25s) (s35)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The oil in the tanks"},  # 24  the hardest decision: the stocks (12.62s) (s36-37)
    {"img": "STREET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "No special privilege"},  # 25  Lee Kuan Yew's memoir account opens (18.82s) (s38)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Enough for two years"},  # 26  his figure, attributed; no document numbers it (17.10s) (s39-40)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Not a single drop"},  # 27  the 2018 official retelling (17.93s) (s41)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Take the cut, pay the price"},  # 28  the two halves together (23.45s) (s42-44)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "What Singapore did not do"},  # 29  no rationing, no lower speed limits (8.50s) (s45-46)
    {"img": "ESSO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Taxes, tariffs, restrictions"},  # 30  the 1975 survey's summary (25.55s) (s47)
    {"img": "STREET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Persuasion, not rationing"},  # 31  car-pooling; the price mechanism (12.18s) (s48-49)
    {"img": "ESSO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Save a litre a day"},  # 32  BP's campaign; 49.5 cents a day (16.48s) (s50-51)
    {"img": "STREET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Signs off at 10 p.m."},  # 33  the dealers' measures (15.62s) (s52)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "A leaflet in three languages"},  # 34  fifteen hints for every motorist (17.38s) (s53)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Singaporeans heeded the call"},  # 35  Goh Chok Tong, looking back in 2001 (12.70s) (s54)
    {"img": "FLAG", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The contrast: America's flags"},  # 36  the embargoed countries, by contrast (4.05s) (s55)
    {"img": "ODDEVEN", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Rationed by number plate"},  # 37  Oregon first; the No Gas signs (10.22s) (s56)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "No queues to photograph"},  # 38  Singapore's winter of schedules; almost literal (13.85s) (s57-58)
    {"img": "HDBNIGHT", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Sodium lamps for the main roads"},  # 39  the January 1974 conversion (14.88s) (s59)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "500 lamps already installed"},  # 40  Nicoll Highway to Connaught Drive (14.78s) (s60)
    {"img": "HDBNIGHT", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Changed, not switched off"},  # 41  dimmed by technology; the bill opens (9.90s) (s61-62)
    {"img": "ESSO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Petrol up 9 percent"},  # 42  December 1973; most of it tax (15.52s) (s63-64)
    {"img": "CHART", **{"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]], "ease": "linear"}, "title": "Kerosene up 120 percent"},  # 43  the 1973-74 price rises (15.93s) (s65)
    {"img": "SENOKO", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Consumption falls 9.4 percent"},  # 44  19.9 to 18.0 million tonnes; bunkers 70 percent (26.30s) (s66)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The smaller part of the fall"},  # 45  the household share; the wider economy (8.93s) (s67-68)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Inflation: 22.4 percent"},  # 46  the World Bank series' highest figure (18.38s) (s69)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Growth halves; jobs go"},  # 47  6.8 percent growth; 17,000 retrenched (22.25s) (s70-71)
    {"img": "JURONGPANO", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The trade balance swings"},  # 48  surplus to deficit (13.57s) (s72)
    {"img": "STREET", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The crisis in odd corners"},  # 49  Plaza Singapura's $1 showrooms (20.97s) (s73-74)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "The hospital's air-conditioning"},  # 50  the Cabinet strips SGH's cooling (18.80s) (s75)
    {"img": "BUKOM", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Laju attack, January 1974"},  # 51  violence on the refinery shore (15.38s) (s76)
    {"img": "RIVER", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The embargo ends, March 1974"},  # 52  no ending of its own; a change of habit (12.18s) (s77-78)
    {"img": "SENOKO", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "Conservation becomes permanent"},  # 53  1977 campaign; the 1981 Energy Unit (19.98s) (s79-80)
    {"img": "CHART", **{"type": "letterbox", "zoom": [1.0, 1.0, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]], "ease": "linear"}, "title": "The second shock, 1979"},  # 54  the larger disruption; prices up 105 percent (19.30s) (s81-82)
    {"img": "HDBNIGHT", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "Save Electricity, April 1979"},  # 55  the named, dated campaign; PUB warns (22.52s) (s83-84)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.65, 0.5], [0.65, 0.5], [0.65, 0.5]]}, "title": "No subsidies; prices rule"},  # 56  the settled approach (18.12s) (s85)
    {"img": "JURONGPANO", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The oldest weakness, priced"},  # 57  the closing judgement (11.10s) (s86)
    {"img": "STREET", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.35, 0.5], [0.35, 0.5], [0.35, 0.5]]}, "title": "The answers built since"},  # 58  pipelines and the LNG terminal (15.60s) (s87)
]

SCHEDULE = [
    (0.000, 0), (5.675, 1), (22.475, 2),
    (40.350, 3), (55.100, 4), (78.875, 5),
    (99.575, 6), (114.675, 7), (133.325, 8),
    (151.000, 9), (176.600, 10), (192.975, 11),
    (202.750, 12), (211.500, 13), (225.500, 14),
    (240.675, 15), (254.200, 16), (270.925, 17),
    (287.350, 18), (303.700, 19), (321.225, 20),
    (335.650, 21), (352.400, 22), (374.875, 23),
    (388.125, 24), (400.750, 25), (419.575, 26),
    (436.675, 27), (454.600, 28), (478.050, 29),
    (486.550, 30), (512.100, 31), (524.275, 32),
    (540.750, 33), (556.375, 34), (573.750, 35),
    (586.450, 36), (590.500, 37), (600.725, 38),
    (614.575, 39), (629.450, 40), (644.225, 41),
    (654.125, 42), (669.650, 43), (685.575, 44),
    (711.875, 45), (720.800, 46), (739.175, 47),
    (761.425, 48), (775.000, 49), (795.975, 50),
    (814.775, 51), (830.150, 52), (842.325, 53),
    (862.300, 54), (881.600, 55), (904.125, 56),
    (922.250, 57), (933.350, 58)
]
TOTAL_DURATION = 948.95
TIMING_JSON = "audio/1973-the-oil-shock-and-the-winter-singapore-turned-down-the-lights.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
