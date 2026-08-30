"""Video config for "He Wrote Singapore's Economics Textbook, Then Spent
30 Years Defying It" (Lim Chong Yah) - Watch widget and main video.

No chart in this post. The image pool is genuinely thin - Lim has no
free-licensed portrait, and there is no imagery of the National Wages
Council - so the labour-economy photos carry most of the run through
reuse.

Images (3 post + the textbook cover + 5 gallery):
  OEI       - the Oei Tiong Ham Building, NUS Bukit Timah (post hero) -
              the campus (ex-University of Malaya in Singapore) where Lim
              taught and was Dean
  TEXTBOOK  - the cover of "Elements of Economic Theory" (NLB book-cover
              service, not a Commons file)
  STRIKE    - Singapore Glass Manufacturers strikers picketing, 21 Jul
              1951 - the adversarial labour disputes the NWC replaced
  JOINER    - a joiner at work, 1973-74 - the low-wage economy
  MANASSEH  - the Manasseh Meyer Building, NUS Bukit Timah (gallery)
  POTTER    - a potter at work, 1973-74 (gallery)
  COFFIN    - a coffin maker's shop, 1973-74 (gallery)
  BARBER    - a sidewalk barber, 1973-74 (gallery)
  SETRON    - a Setron TV set, assembled in Singapore 1964-86 (gallery) -
              the higher-value manufacturing the 1979 wage-correction
              policy was pushing the economy toward

23 slides, 398.075s. Aspect check (1280x720, ~1.44 cover threshold):
  OEI 4000x2250 (1.78)      -> cover, horizontal pan
  TEXTBOOK ~330px wide      -> letterbox (a small book-cover image)
  STRIKE 749x512 (1.46)     -> letterbox (low-res 1951 press photo)
  JOINER 5876x3917 (1.50)   -> cover, horizontal pan
  MANASSEH 4000x2250 (1.78) -> cover, horizontal pan
  POTTER 3896x5844 (0.67)   -> letterbox (portrait)
  COFFIN 3941x5912 (0.67)   -> letterbox (portrait)
  BARBER 5839x3893 (1.50)   -> cover, horizontal pan
  SETRON 3964x2993 (1.32)   -> letterbox
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5). Slide 16 (POTTER) holds 34.6s: it covers the single very
long sentence describing the 2012 "Shock Therapy II" proposal, which
has no internal timing.json boundary to cut on; a very slow push-in
carries it.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "OEI": f"{_C}/4/4a/Oei_Tiong_Ham_Building.jpg",
    "TEXTBOOK": "https://eservice.nlb.gov.sg/bookcoverwrapper/cover/0195846125?s=LG",
    "STRIKE": f"{_C}/d/d3/Singapore_Glass_Factory_1951_strike.jpg",
    "JOINER": f"{_C}/b/b1/Singapore-Joiner-1973-74-WUS08244.jpg",
    "MANASSEH": f"{_C}/f/f4/Manasseh_Meyer_Building%2C_National_University_of_Singapore_Bukit_Timah_Campus%2C_October_2025.jpg",
    "POTTER": f"{_C}/e/ef/Singapore-Potter-1973-74-WUS08246.jpg",
    "COFFIN": f"{_C}/d/d3/Singapore-Coffin_Maker-1973-74-WUS08245.jpg",
    "BARBER": f"{_C}/3/39/Singapore-Sidewalk_barber_in_1973-74-WUS08232.jpg",
    "SETRON": f"{_C}/3/38/Setron_TV_Set.jpg",
}

CREDITS = {
    "TEXTBOOK": "Book cover of 'Elements of Economic Theory': National Library Board Singapore",
}

SLIDES = [
    {"img": "OEI", "type": "cover", "zoom": [1, 1.04, 1.08], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"},
    {"img": "TEXTBOOK", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "OEI", "type": "cover", "zoom": [1.08, 1.04, 1], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-out"},
    {"img": "POTTER", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "COFFIN", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "MANASSEH", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"},
    {"img": "TEXTBOOK", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OEI", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"},
    {"img": "MANASSEH", "type": "cover", "zoom": [1, 1.04, 1.08], "pan": [(0.75, 0.5), (0.5, 0.5), (0.25, 0.5)], "ease": "linear"},
    {"img": "JOINER", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.35, 0.5), (0.5, 0.5), (0.65, 0.5)], "ease": "ease-in"},
    {"img": "STRIKE", "type": "letterbox", "zoom": [1, 1.04, 1.08], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "JOINER", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-out"},
    {"img": "SETRON", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "BARBER", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"},
    {"img": "SETRON", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "TEXTBOOK", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "POTTER", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "COFFIN", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "STRIKE", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "OEI", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "MANASSEH", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.25, 0.5), (0.5, 0.5), (0.75, 0.5)], "ease": "ease-in-out"},
    {"img": "TEXTBOOK", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "JOINER", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-out"},
]

# Real values from
# audio/lim-chong-yah-textbook-national-wages-council-shock-therapy.timing.json.
# Every point is a real sentence start.
#   0  s0        title
#   1  s1        the textbook: Elements of Economic Theory, 1971
#   2  s2-3      its lead author taught free-market logic, then spent 30
#                years deciding when to overrule it
#   3  s4-5      born Malacca 1932; mother dies; the family business
#                collapses under the occupation; he manages the finances
#   4  s6-7      tapioca and fish to feed his siblings; jailed at ten;
#                five languages before English, at ACS Malacca
#   5  s8        1951 scholarship to the University of Malaya in Singapore;
#                then Oxford under John Hicks, a doctorate in two years
#   6  s9        by 1971 he co-writes the textbook with Lee Sheng Yi and
#                Chia Siow Yue
#   7  s10       OUP publishes it; it becomes the standard text
#   8  s11       Dean, department head, senior professor, then the NTU
#                Winsemius chair
#   9  s12       but the job that mattered more was the one he took in 1972
#   10 s13       founding chairman of the NWC - consensus wage guidelines,
#                a break from the picket lines of the 1950s-60s
#   11 s14-15    30 years to 2001; real wages +4.6%/yr; invisible work
#   12 s16       1979: the aggressive "wage correction", three years of 20%
#                to push the economy upmarket
#   13 s17       wages rise through 1981, overshoot through 1983-84 as the
#                dollar appreciates
#   14 s18       by 1985 competitiveness has eroded - a cause of that year's
#                recession, on the wage council's own watch
#   15 s19       which makes 2012 hard to read as an aberration
#   16 s20       at 80, retired, he proposes "Shock Therapy II": +50% over
#                three years under $1,500/mo, a freeze on the top salaries
#   17 s21       he warns the Gini coefficient is nearing dangerous ground
#   18 s22       the labour movement turns on it; economists call it
#                impractical
#   19 s23-24    the NWC never adopts it; Lim dies July 2023, aged 91
#   20 s25       the manpower minister's tribute; the NTUC's
#   21 s26       the textbook said wages are just another price
#   22 s27       its author spent three decades showing Singapore never let
#                the market alone set that price - and twice moved it by
#                decree
SCHEDULE = [
    (0.0, 0), (5.45, 1), (24.65, 2), (40.625, 3), (63.775, 4),
    (83.625, 5), (102.65, 6), (115.875, 7), (130.05, 8), (157.7, 9),
    (166.225, 10), (191.7, 11), (215.475, 12), (239.825, 13), (254.4, 14),
    (273.525, 15), (279.45, 16), (314.05, 17), (323.075, 18), (341.55, 19),
    (350.575, 20), (373.3, 21), (382.425, 22),
]
TOTAL_DURATION = 398.075
TIMING_JSON = "audio/lim-chong-yah-textbook-national-wages-council-shock-therapy.timing.json"
