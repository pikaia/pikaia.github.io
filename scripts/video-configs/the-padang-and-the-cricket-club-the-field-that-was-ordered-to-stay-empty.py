"""Video config for the Padang and the Singapore Cricket Club post.

The pool is the post and gallery's twenty pictures:
the civic buildings from the field (2011), Lambert's
Esplanade promenade, the 1890 photochrome of the cricket
ground, the KITLV pavilion views of c.1910 and 1921 (the
1280px JPEG derivatives of the TIFFs, as in the post),
the Raffles statue c.1890 and c.1900, the Municipal
Building c.1930, the two clean public-domain Trusler
frames of the 1945 surrender, the 1968 parade, the 1973-74
field and club, the pavilion in 1963 and 2016, bowls in
2023, the 2024 parade rehearsal, the field in 2025, and
cricket against Marina Bay Sands in 2018.

Named-place audit: the surrender sentences (s50-55) run
on the two Trusler frames of that day - the address
photograph under the not-on-the-steps correction and the
address itself, the inspection photograph under the
signing sentences (no freely licensed photograph of the
signing itself exists; the famous frames are IWM Non
Commercial and excluded, as at Changi). The Municipal
Building sentences (s35-36, s44) run on the building's
own photograph; the SRC beats (s29-31) run on field-wide
views, no SRC clubhouse photograph being freely licensed;
the 1966 parade sentences run on the 1968 parade
photograph, titled for the first parades, there being no
freely licensed 1966 frame.

68 slides, 988.00s. No slide over 30s; the
longest dwell is 26.88s. Narration: Kokoro with the
OpenVoice clone. Pronunciation overrides for the
post's names filed 2026-11-28, NOT ear-verified yet.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "CITYHALL": "https://upload.wikimedia.org/wikipedia/commons/7/70/Old_Supreme_Court_Building_and_City_Hall_from_the_Padang%2C_Singapore_-_20110205.jpg",
    "ESPLANADE": "https://upload.wikimedia.org/wikipedia/commons/2/25/Park_met_wandelaars_in_Singapore_Esplanade%2C_S.pore_%28titel_op_object%29%2C_RP-F-F01197-AG.jpg",
    "PHOTOCHROME": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Singapore._Esplanade_Cricket_Club_LCCN2017657648.jpg",
    "SCC1910": "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/67/KITLV_A887_-_Singapore_Cricket_Club_te_Singapore%2C_KITLV_101724.tiff/lossy-page1-1280px-KITLV_A887_-_Singapore_Cricket_Club_te_Singapore%2C_KITLV_101724.tiff.jpg",
    "RAFFLES1890": "https://thumb.wikimedia.org/wikipedia/commons/thumb/5/56/KITLV_-_377458_-_Statue_of_Sir_Thomas_Stamford_Raffles_in_Singapore_-_circa_1890.tif/lossy-page1-1280px-KITLV_-_377458_-_Statue_of_Sir_Thomas_Stamford_Raffles_in_Singapore_-_circa_1890.tif.jpg",
    "MUNICIPAL": "https://thumb.wikimedia.org/wikipedia/commons/thumb/b/b6/The_Municipal_Building_te_Singapore%2C_KITLV_104790.tiff/lossy-page1-1280px-The_Municipal_Building_te_Singapore%2C_KITLV_104790.tiff.jpg",
    "INSPECT": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Louis_Mountbatten_Inspection%2C_Singapore_1945.jpg",
    "ADDRESS": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Mountbatten_address%2C_Singapore_1945.jpg",
    "NDP1968": "https://upload.wikimedia.org/wikipedia/commons/e/eb/NationalDayParade-Singapore-1968.jpg",
    "CRICKETMBS": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Cricket_match_and_Marina_Bay_Sands_Hotel_in_Singapore.jpg",
    "RAFFLES1900": "https://thumb.wikimedia.org/wikipedia/commons/thumb/6/6d/KITLV_-_105827_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Rafflesmonument_in_Singapore_-_circa_1900.tif/lossy-page1-1280px-KITLV_-_105827_-_Lambert_%26_Co.%2C_G.R._-_Singapore_-_Rafflesmonument_in_Singapore_-_circa_1900.tif.jpg",
    "SOUVENIR": "https://upload.wikimedia.org/wikipedia/commons/4/41/Souvenir_of_Singapore%2C_1914_-_Plate_12_-_Singapore_Cricket_Club%2C_Town_Hall%2C_Supreme_Court_and_Europe_Hotel.jpg",
    "SCC1921": "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d4/Singapore_Cricket_Club%2C_Singapore%2C_KITLV_1404869.tiff/lossy-page1-1280px-Singapore_Cricket_Club%2C_Singapore%2C_KITLV_1404869.tiff.jpg",
    "SCC1963": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Singapore_Cricket_Club_1963.jpg",
    "PADANG7374": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Singapore-Padang-1973-74-WUS01252.jpg",
    "SCC7374": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Singapore-Singapore_Cricket_Club-7973-74-WUS08188.jpg",
    "SCC2016": "https://upload.wikimedia.org/wikipedia/commons/9/91/Singapore_Cricket_Club_building_2016.jpg",
    "BOWLERS": "https://upload.wikimedia.org/wikipedia/commons/6/64/Singapore_Cricket_Club_Bowlers.jpg",
    "NDP2024": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Singapore_NDP_2024_-_Rehearsal.jpg",
    "PADANG2025": "https://upload.wikimedia.org/wikipedia/commons/3/3d/The_Padang%2C_October_2025.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# civic stage, the 1890 ground, the surrender, the game today.
THUMBNAIL = [
    {"img": "CITYHALL", "pan": (0.5, 0.5)},
    {"img": "PHOTOCHROME", "pan": (0.5, 0.5)},
    {"img": "INSPECT", "pan": (0.5, 0.5)},
    {"img": "CRICKETMBS", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Padang and the Cricket Club"},  # 0  title (5.28s) (s0)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "4.3 hectares of grass"},  # 1  the field today: never built on (9.35s) (s1)
    {"img": "INSPECT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Armies, salutes and a surrender"},  # 2  the field's five lives in one sentence (16.27s) (s2)
    {"img": "CRICKETMBS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The emptiness made a monument"},  # 3  gazetted 2022; the two clubs at its ends (12.10s) (s3-4)
    {"img": "ESPLANADE", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The plain near the river"},  # 4  Padang = a field; the Sejarah Melayu plain at Temasek (23.00s) (s5-6)
    {"img": "RAFFLES1900", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The field where the camp stood"},  # 5  the 1819 landing and camp on the plain (19.45s) (s7)
    {"img": "ESPLANADE", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The merchants are stopped, 1822"},  # 6  Raffles returns and halts the building (13.17s) (s8-9)
    {"img": "SOUVENIR", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Jackson's Open Square"},  # 7  the town plan marks the field an Open Square (13.85s) (s10)
    {"img": "PADANG7374", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Plain, Esplanade, Padang"},  # 8  the name's journey to 1907 (12.68s) (s11)
    {"img": "PHOTOCHROME", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Everything outdoors"},  # 9  the square's use decided by the town; the 1824 salute (11.65s) (s12-13)
    {"img": "SCC1910", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Sports on the grass"},  # 10  New Year regattas and races (15.47s) (s14)
    {"img": "PADANG7374", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Bollards and chains, 1845"},  # 11  the green fenced against drunken sailors (14.47s) (s15)
    {"img": "SOUVENIR", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Scandal Point"},  # 12  the gossip knoll at the northern end (13.88s) (s16)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Fourteen centuries under the grass"},  # 13  the 1984 and 2003 digs (14.15s) (s17)
    {"img": "PHOTOCHROME", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Cricket came early"},  # 14  played by 1837; Sunday complaints (12.53s) (s18-19)
    {"img": "SCC1910", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Singapore Cricket Club, 1852"},  # 15  the founding meeting; first fixture March 1853 (17.20s) (s20)
    {"img": "SCC1921", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Second-oldest club in Singapore"},  # 16  a decade younger than the Turf Club (5.58s) (s21)
    {"img": "SCC1921", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A hut under the angsana trees"},  # 17  the pavilion begins: 1860s hut at the southern end (12.53s) (s22-23)
    {"img": "SCC1921", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Membership 98, in 1877"},  # 18  the single-storey bungalow (6.70s) (s24)
    {"img": "SCC1910", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The pavilion of 1884"},  # 19  built on the present site; the core of today's clubhouse (20.02s) (s25)
    {"img": "SCC1963", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Tennis, bowls, hockey, rugby"},  # 20  the other sports follow cricket (16.20s) (s26)
    {"img": "SCC7374", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The touring sides"},  # 21  Macartney 1927, Cahn 1937, Sobers 1964 (18.57s) (s27)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A club for Europeans only"},  # 22  the colour line at the southern end (16.00s) (s28)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Recreation Club answers, 1883"},  # 23  thirty Eurasian men; the northern end granted (26.88s) (s29-30)
    {"img": "PADANG7374", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The SRC opens its doors, 1963"},  # 24  membership opened to all communities (12.78s) (s31)
    {"img": "CRICKETMBS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Two clubs, one field"},  # 25  the unpainted line down the grass (8.18s) (s32)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The field takes its present shape"},  # 26  reclamation roughly doubles it, c.1890 (13.62s) (s33)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "A stage set rises"},  # 27  what rose behind it (4.42s) (s34)
    {"img": "MUNICIPAL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Opened 23 July 1929"},  # 28  the Municipal Building, Meadows and Gordon (26.23s) (s35)
    {"img": "MUNICIPAL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Renamed City Hall, 1951"},  # 29  city status; the backdrop and the steps (8.47s) (s36)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Supreme Court beside it, 1939"},  # 30  on the Hotel de l'Europe site (13.97s) (s37)
    {"img": "RAFFLES1890", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.35], [0.5, 0.35], [0.5, 0.35]]}, "title": "The Raffles statue, 1887"},  # 31  Woolner's bronze, the Golden Jubilee (17.52s) (s38)
    {"img": "RAFFLES1890", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.35], [0.5, 0.35], [0.5, 0.35]]}, "title": "Hit by stray footballs"},  # 32  moved to Empress Place, 1919 (12.38s) (s39)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The field escapes the planners"},  # 33  sale, cathedral and plaza all refused (17.55s) (s40)
    {"img": "SCC7374", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Jubilees on the grass"},  # 34  Silver Jubilee 1935; then war (8.80s) (s41)
    {"img": "PADANG7374", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The assembly ground, 1942"},  # 35  17 February 1942: held and interrogated on the field (22.43s) (s42)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Eurasian assembly, 1942"},  # 36  registered at the SRC clubhouse, 3 March 1942 (13.60s) (s43)
    {"img": "MUNICIPAL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Syonan headquarters"},  # 37  the Municipal Building as Syonan Tokubetsu-si HQ (10.62s) (s44)
    {"img": "SCC1910", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The pavilion becomes the Yamoto"},  # 38  a Japanese restaurant; the clubhouse a tearoom (9.72s) (s45)
    {"img": "SCC7374", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Bose and Tojo review the INA, 1943"},  # 39  the parade of 6 July 1943 (14.78s) (s46)
    {"img": "PADANG7374", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Tapioca on the Padang, 1944"},  # 40  dug up under Grow More Food (11.30s) (s47)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The memorial that stood for weeks"},  # 41  the INA memorial, built and demolished, 1945 (17.82s) (s48-49)
    {"img": "ADDRESS", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Not signed on the steps"},  # 42  the most retold moment, told wrong (11.18s) (s50-51)
    {"img": "INSPECT", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "11.10 am, 12 September 1945"},  # 43  signed inside the chamber (18.10s) (s52)
    {"img": "INSPECT", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Itagaki signs for Terauchi"},  # 44  eleven copies of the Instrument (19.70s) (s53)
    {"img": "ADDRESS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "400 spectators"},  # 45  community leaders, the Sultan, released POWs (8.88s) (s54)
    {"img": "ADDRESS", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The address and the victory parade"},  # 46  the steps and the field get the ceremony (22.07s) (s55)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Decorating the resistance, 1946"},  # 47  Mountbatten and Chin Peng's men (13.43s) (s56)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Maria Hertogh riots, 1950"},  # 48  the other face of civic life (11.90s) (s57)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The victory rally, June 1959"},  # 49  50,000 before City Hall (16.90s) (s58-59)
    {"img": "MUNICIPAL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "“Times have changed”"},  # 50  Lee's taunt to the Europeans who held the field (15.25s) (s60)
    {"img": "MUNICIPAL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "“...and will stay changed”"},  # 51  the rally's conclusion (4.65s) (s61)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Sworn in, in the surrender chamber"},  # 52  5 June 1959, white shirts, no lounge suits (21.62s) (s62)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Yusof Ishak, December 1959"},  # 53  the first Malayan-born head of state (12.72s) (s63)
    {"img": "NDP2024", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "120,000 for reparations, 1963"},  # 54  among the largest gatherings in the island's history (21.82s) (s64)
    {"img": "NDP1968", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The first parades on the Padang"},  # 55  the first NDP, 9 August 1966 (photo: the 1968 parade) (19.70s) (s65)
    {"img": "NDP1968", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Padang years, to 1975"},  # 56  the parade's only home until decentralisation (12.22s) (s66)
    {"img": "PADANG7374", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "1968: the parade in the rain"},  # 57  the rugged society's emblem (12.88s) (s67)
    {"img": "NDP2024", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The parade returns"},  # 58  the five-year cycle and the milestone years (22.62s) (s68)
    {"img": "CRICKETMBS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Ceremony and sport"},  # 59  the double track; the 2008 night race passes (18.83s) (s69-70)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The National Gallery opens, 2015"},  # 60  the two buildings behind the field, joined (7.08s) (s71)
    {"img": "CRICKETMBS", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The only cricket square in Singapore"},  # 61  cricket, sevens, soccer, the marathon (20.93s) (s72)
    {"img": "BOWLERS", **{"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]], "ease": "linear"}, "title": "The co-custodians"},  # 62  the two clubs as the field's custodians (5.40s) (s73)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The law had to change first"},  # 63  the 2019 announcement; the 2021 Act amendment (20.85s) (s74-75)
    {"img": "PADANG2025", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The 75th National Monument, 2022"},  # 64  gazetted on National Day, the first green monument (11.35s) (s76)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Protected as it is"},  # 65  the Minister on what the gazette protects (15.43s) (s77)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "The Padang Civic Ensemble"},  # 66  the UNESCO Tentative List, 2022 (10.38s) (s78)
    {"img": "CITYHALL", **{"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [[0.5, 0.5], [0.5, 0.5], [0.5, 0.5]]}, "title": "Nothing there"},  # 67  the closing line (20.95s) (s79)
]

SCHEDULE = [
    (0.000, 0), (5.275, 1), (14.625, 2),
    (30.900, 3), (43.000, 4), (66.000, 5),
    (85.450, 6), (98.625, 7), (112.475, 8),
    (125.150, 9), (136.800, 10), (152.275, 11),
    (166.750, 12), (180.625, 13), (194.775, 14),
    (207.300, 15), (224.500, 16), (230.075, 17),
    (242.600, 18), (249.300, 19), (269.325, 20),
    (285.525, 21), (304.100, 22), (320.100, 23),
    (346.975, 24), (359.750, 25), (367.925, 26),
    (381.550, 27), (385.975, 28), (412.200, 29),
    (420.675, 30), (434.650, 31), (452.175, 32),
    (464.550, 33), (482.100, 34), (490.900, 35),
    (513.325, 36), (526.925, 37), (537.550, 38),
    (547.275, 39), (562.050, 40), (573.350, 41),
    (591.175, 42), (602.350, 43), (620.450, 44),
    (640.150, 45), (649.025, 46), (671.100, 47),
    (684.525, 48), (696.425, 49), (713.325, 50),
    (728.575, 51), (733.225, 52), (754.850, 53),
    (767.575, 54), (789.400, 55), (809.100, 56),
    (821.325, 57), (834.200, 58), (856.825, 59),
    (875.650, 60), (882.725, 61), (903.650, 62),
    (909.050, 63), (929.900, 64), (941.250, 65),
    (956.675, 66), (967.050, 67)
]
TOTAL_DURATION = 988.000
TIMING_JSON = "audio/the-padang-and-the-cricket-club-the-field-that-was-ordered-to-stay-empty.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
