"""Video config for "Singapore's National Symbols Were All Written on a
Deadline" - Watch widget and main video.

No chart in this post. The two flags are SVGs, so the video uses
Wikimedia's PNG renderings (the ".../<size>px-<name>.svg.png" thumb
form). The low-res 1933 Yusof Ishak gallery photo (324px) is left
gallery-only - the ST 4 Dec 1959 front page carries the installation
beat better.

Images (2 post + the ST front page + 6 gallery, minus the crest and the
1933 Yusof photo):
  FLAG       - the flag of Singapore (post hero), PNG rendering
  OLDFLAG    - the Colony of Singapore flag, 1952-1959 (gallery), PNG
  ST1959     - The Straits Times, 4 Dec 1959, p.1 - the Yang di-Pertuan
               Negara installation, the day flag + anthem went public
  ST1966     - The Straits Times, 10 Aug 1966, p.1 - the first National
               Day, the year the pledge was written
  ZUBIR      - Zubir Said sitting for a portrait bust, 1960
  RAJARATNAM - S. Rajaratnam, c.1940s
  VICTORIA   - Victoria Theatre and Concert Hall - where the anthem was
               first performed, at the 1958 reopening
  CITYHALL   - the former City Hall and the Padang - the installation and
               the seat of the government that assembled the symbols

21 slides, 362.05s. Aspect check (1280x720, ~1.44 cover threshold):
  FLAG 1280x853 (1.50)       -> letterbox (show the whole flag)
  OLDFLAG 1280x853 (1.50)    -> letterbox (show the whole flag)
  ST1959 1000x1428 (0.70)    -> letterbox (portrait newspaper page)
  ST1966 1000x1436 (0.70)    -> letterbox (portrait newspaper page)
  ZUBIR 1212x1618 (0.75)     -> letterbox (portrait)
  RAJARATNAM 512x744 (0.69)  -> letterbox (low-res portrait)
  VICTORIA 3872x2592 (1.49)  -> cover, horizontal pan
  CITYHALL 3776x2520 (1.50)  -> cover, horizontal pan
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5). Several flag/newspaper slides hold 22-27s over one long
sentence with no closer boundary; slow zooms carry them.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"
_T = "https://upload.wikimedia.org/wikipedia/commons/thumb"

IMAGES = {
    "FLAG": f"{_T}/4/48/Flag_of_Singapore.svg/1280px-Flag_of_Singapore.svg.png",
    "OLDFLAG": f"{_T}/2/20/Flag_of_Singapore_%281952%E2%80%931959%29.svg/1280px-Flag_of_Singapore_%281952%E2%80%931959%29.svg.png",
    "ST1959": f"{_C}/0/0e/ST4December1959.jpg",
    "ST1966": f"{_C}/c/ca/ST10August1966.jpg",
    "ZUBIR": f"{_C}/0/0d/Zubir_Said_in_1960_%28cropped%29.jpg",
    "RAJARATNAM": f"{_C}/0/09/S_Rajaratnam_c._1940s.jpg",
    "VICTORIA": f"{_C}/3/34/Rear_entrance_of_Victoria_Theatre_and_Concert_Hall%2C_Singapore_-_20141101-02.JPG",
    "CITYHALL": f"{_C}/7/70/Old_Supreme_Court_Building_and_City_Hall_from_the_Padang%2C_Singapore_-_20110205.jpg",
}

SLIDES = [
    {"img": "VICTORIA", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"},
    {"img": "FLAG", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "OLDFLAG", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CITYHALL", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"},
    {"img": "OLDFLAG", "type": "letterbox", "zoom": [1.08, 1.04, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "FLAG", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "ZUBIR", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "VICTORIA", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-in-out"},
    {"img": "ZUBIR", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "VICTORIA", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in-out"},
    {"img": "CITYHALL", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.75, 0.5), (0.5, 0.5), (0.25, 0.5)], "ease": "ease-out"},
    {"img": "ST1959", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ST1966", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "CITYHALL", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.25, 0.5), (0.5, 0.5), (0.75, 0.5)], "ease": "ease-in-out"},
    {"img": "RAJARATNAM", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "ST1966", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "FLAG", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "OLDFLAG", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "CITYHALL", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"},
    {"img": "FLAG", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "ST1959", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
]

# Real values from
# audio/singapore-flag-anthem-pledge-written-on-deadline.timing.json.
# Every point is a real sentence start.
#   0  s0-2   title; the anthem was written for a concert-hall reopening
#   1  s3     flag, anthem and pledge all exist because two governments
#             needed something on a deadline - 1959 and 1966
#   2  s4-5   the flag came first; the Union Jack of 140 years needed
#             replacing; Toh Chin Chye put in charge
#   3  s6     he studied every UN flag, then brought designs to cabinet
#   4  s7-8   the plain red field read as communist; three stars too close
#             to the Malayan Communist Party flag
#   5  s9     the compromise: stripes, a crescent for Malay Singaporeans,
#             five stars for the Chinese majority
#   6  s10-11 first sketch to unveiling in two months; the anthem's path
#             was stranger still
#   7  s12    1958: the Municipal Council commissions Zubir Said to set
#             its motto, Majulah Singapura, for the Victoria Theatre gala
#   8  s13-14 he took two weeks; a short singable melody, words plain
#             enough for every race
#   9  s15    premiered at the 6 Sept 1958 reopening concert - civic
#             pageantry, nothing more
#   10 s16    a year on, Toh Chin Chye's search for an anthem lands on the
#             council's old tune
#   11 s17    MAP -> ST1959: Majulah Singapura made the anthem on 3 Dec
#             1959, the day the flag was unveiled at Yusof bin Ishak's
#             installation
#   12 s18-19 the pledge came from something darker: expulsion in Aug
#             1965, the race riots that killed 23
#   13 s20-21 two months after independence, the task falls to Foreign
#             Minister S. Rajaratnam
#   14 s22-23 three drafts; a fractured country must name its divisions;
#             an early "forget differences of race, language and religion"
#   15 s24    revised to "regardless of race, language or religion" -
#             honest about what was possible
#   16 s25    translated three ways; first recited 24 Aug 1966 by ~500,000
#             students, right hands raised to the flag
#   17 s26-27 not how symbols are meant to form - anthems accrue over
#             generations, flags descend from old battles
#   18 s28    Singapore's happened in a hurry, under duress, by a handful
#             of people solving an immediate problem
#   19 s29    they are saluted so often they feel like they always existed
#   20 s30    but they were assembled under time pressure by namable
#             people - and survive, largely unchanged
SCHEDULE = [
    (0.0, 0), (13.075, 1), (39.95, 2), (62.075, 3), (74.3, 4),
    (93.2, 5), (116.825, 6), (126.0, 7), (148.7, 8), (161.8, 9),
    (172.9, 10), (185.325, 11), (202.95, 12), (223.6, 13), (235.7, 14),
    (253.5, 15), (268.325, 16), (291.025, 17), (316.825, 18), (330.35, 19),
    (346.05, 20),
]
TOTAL_DURATION = 362.05
TIMING_JSON = "audio/singapore-flag-anthem-pledge-written-on-deadline.timing.json"
