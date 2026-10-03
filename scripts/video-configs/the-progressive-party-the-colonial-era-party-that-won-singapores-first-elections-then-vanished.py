"""Video config for the Progressive Party post.

The party is thin on photographs: the 1951 results-night portraits from the
National Archives (C. C. Tan, John Laycock, Thio Chan Bee, Lim Yew Hock,
Vilasini Menon), two other Laycock portraits, Victoria Memorial Hall (1971)
and the civic district from the air, two results maps and the two party
emblems. The newspaper pages carry most of the story: the 1947 founding
(SFP), the 1948 and 1951 results, the 1955 results, the editorial that
explained the split vote, and the 1956 merger. Each page is shown whole-page
`cover` with a push-in on its headline (pan/zoom worked out from real
cover_crop test frames, scratch/pp/pans.py), zoom capped at 2.4x so the
1600px scans stay sharp.

Named people get their own photo or none: C. C. Tan when he loses Cairnhill,
Thio Chan Bee / Lim Yew Hock / Vilasini Menon on the 1951 sentences that
name them; sentences naming people with no photo (Samat, da Silva, Rajah,
Tan Eng Joo) sit on a newspaper page.

36 slides, 582.05s. AVATAR: first and last 30s (Phase 1 test).
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"
_A = "/assets/images"

IMAGES = {
    "HALL": f"{_C}/b/b6/172a_Victoria_Hall_Singapore_%2851253058494%29.jpg/1280px-172a_Victoria_Hall_Singapore_%2851253058494%29.jpg",
    "AERIAL": f"{_C}/1/13/Collectie_Familie_Khouw%2C_KITLV_D14089.tiff/lossy-page1-1280px-Collectie_Familie_Khouw%2C_KITLV_D14089.tiff.jpg",
    "CCTAN": f"{_U}/b/b6/Tan_Chye_Cheng.png",
    "LAYCOCK48": f"{_U}/8/83/John_Laycock.png",
    "LAYCOCK_LECT": f"{_U}/5/5a/John_Laycock%2C_1951.jpg",
    "LAYCOCK51": f"{_U}/c/cd/John_Laycock_at_the_Legislative_Election%2C_1951.jpg",
    "THIO": f"{_U}/6/69/Thio_Chan_Bee.jpg",
    "LIM": f"{_U}/9/99/Lim_Yew_Hock%2C_1951.jpg",
    "MENON": f"{_U}/b/b9/Vilasini_Menon.jpg",
    "MAP1951": f"{_U}/4/44/Singaporean_election_1951_map.png",
    "MAP1955": f"{_C}/c/c1/Map_of_the_results_of_the_1955_Singaporean_general_election.svg/1280px-Map_of_the_results_of_the_1955_Singaporean_general_election.svg.png",
    "PPLOGO": f"{_C}/0/0d/PP_Logo.svg/1280px-PP_Logo.svg.png",
    "LSPLOGO": f"{_C}/a/ad/LSP_Logo.svg/1280px-LSP_Logo.svg.png",
    "CHART": f"{_A}/progressive-party-vote-seat-share-chart.png",
    "SFP470826": f"{_A}/singapore-free-press-1947-08-26-page-1.jpg",
    "S480320": f"{_A}/straits-times-1948-03-20-page-1.jpg",
    "S480321": f"{_A}/straits-times-1948-03-21-page-1.jpg",
    "S510411": f"{_A}/straits-times-1951-04-11-page-1.jpg",
    "S550403": f"{_A}/straits-times-1955-04-03-page-1.jpg",
    "S550404": f"{_A}/straits-times-1955-04-04-page-1.jpg",
    "S550404P6": f"{_A}/straits-times-1955-04-04-page-6.jpg",
    "S560201P5": f"{_A}/straits-times-1956-02-01-page-5.jpg",
    "S560206": f"{_A}/straits-times-1956-02-06-page-1.jpg",
}

# Credits for images that aren't captioned in the post or its gallery.
_NSG = "Singapore Press Holdings, via NewspaperSG, National Library Board Singapore, public domain"
CREDITS = {
    "CHART": "Chart by Lesser Known Singapore, data: The Straits Times 11 April 1951; Elections Department Singapore",
    "S480320": f"The Straits Times, 20 March 1948, page 1 ({_NSG})",
}

# The two results maps are transparent PNGs with dark legend text; flatten
# them onto a light warm grey (the default drops alpha to black, hiding the
# legend). The emblems stay on black - the Progressive one has white petals.
IMAGE_BG = {"MAP1951": (232, 230, 224), "MAP1955": (232, 230, 224)}

_E = "ease-in-out"
# Photos (roughly landscape): gentle push-in / pull-back.
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.08, 1.16], "pan": [(0.35, 0.45)] * 3, "ease": _E}
# Strong portraits (~300x550 archival prints): letterbox, modest zoom.
_PORT = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# Graphics (maps, emblems, chart): letterbox, frozen.
_GFX = {"type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}


def _page(zoom, pan):
    return {"type": "cover", "zoom": zoom, "pan": pan, "ease": _E}


# Whole-page newspaper push-ins (scratch/pp/pans.py test frames).
_S550404_HEAD = _page([1.06, 1.12, 1.17], [(0.0, 0.0)] * 3)
_S550404_TAN = _page([2.16, 2.28, 2.4], [(0.0, 0.159), (0.0, 0.163), (0.0, 0.167)])
_S560206_HEAD = _page([2.16, 2.28, 2.4], [(0.807, 0.131), (0.794, 0.135), (0.783, 0.139)])
_SFP_HEAD = _page([2.16, 2.28, 2.4], [(0.593, 0.479), (0.589, 0.479), (0.586, 0.479)])
_SFP_BODY = _page([1.88, 1.98, 2.09], [(0.714, 0.646), (0.702, 0.644), (0.692, 0.642)])
_S480321_HEAD = _page([1.18, 1.25, 1.31], [(0.0, 0.0), (0.1, 0.0), (0.162, 0.0)])
_S480321_RES = _page([2.16, 2.28, 2.4], [(0.295, 0.337), (0.304, 0.339), (0.311, 0.341)])
_S480320_HEAD = _page([1.0, 1.04, 1.08], [(0.5, 0.0)] * 3)
_S480320_CHN = _page([2.16, 2.28, 2.4], [(0.0, 0.416), (0.0, 0.417), (0.0, 0.418)])
_S510411_HEAD = _page([1.0, 1.04, 1.08], [(0.5, 0.0)] * 3)
_S510411_PHOTO = _page([1.79, 1.89, 1.99], [(0.0, 0.367), (0.0, 0.369), (0.0, 0.371)])
_S550403_HEAD = _page([1.0, 1.04, 1.08], [(0.5, 0.0)] * 3)
_S550403_RES = _page([1.33, 1.4, 1.48], [(1.0, 0.227), (1.0, 0.232), (1.0, 0.238)])
_P6_HEAD = _page([2.03, 2.14, 2.25], [(0.081, 0.291), (0.101, 0.294), (0.117, 0.296)])
_P6_LOW = _page([1.72, 1.82, 1.91], [(0.0, 0.74), (0.0, 0.735), (0.0, 0.732)])
_S560201_HEAD = _page([2.16, 2.28, 2.4], [(0.835, 0.409), (0.821, 0.41), (0.809, 0.411)])

SLIDES = [
    {"img": "HALL", **_IN},                  # 0  s0      title
    {"img": "S550404", **_S550404_HEAD},     # 1  s1      1955: 4 of 25 seats ("All say no coalition")
    {"img": "S510411", **_S510411_HEAD},     # 2  s2      had won 1948 and 1951
    {"img": "CCTAN", **_PORT},               # 3  s3      C. C. Tan loses Cairnhill to Marshall
    {"img": "S560206", **_S560206_HEAD},     # 4  s4      dissolved ten months later
    {"img": "AERIAL", **_IN},                # 5  s5      who was allowed to vote
    {"img": "SFP470826", **_SFP_HEAD},       # 6  s6-7    founded 25 Aug 1947, reported next morning
    {"img": "LAYCOCK48", **_PORT},           # 7  s8      office-bearers (Laycock among them)
    {"img": "SFP470826", **_SFP_BODY},       # 8  s9      electorate sub-committee
    {"img": "LAYCOCK_LECT", **_PORT},        # 9  s10-11  gradual programme
    {"img": "LAYCOCK51", **_PORT},           # 10 s12     English-educated professionals
    {"img": "S480321", **_S480321_HEAD},     # 11 s13-14  1948: a very small electorate
    {"img": "S480321", **_S480321_RES},      # 12 s15-16  three of six seats
    {"img": "MAP1951", **_GFX},              # 13 s17-18  1951 election, 48,155 voters
    {"img": "THIO", **_PORT},                # 14 s19     six elected, Thio Chan Bee among them
    {"img": "LIM", **_PORT},                 # 15 s20a    Lim Yew Hock defeats A. P. Rajah
    {"img": "MENON", **_PORT},               # 16 s20b    Vilasini Menon, first woman elected
    {"img": "S510411", **_S510411_PHOTO},    # 17 s21-22  most of the elected seats; CPF
    {"img": "HALL", **_INL},                 # 18 s23-24  the limits of the system
    {"img": "S550403", **_S550403_HEAD},     # 19 s25-27  Rendel constitution, roll of 300,000
    {"img": "S480320", **_S480320_CHN},      # 20 s28-29  1948 warning: 100,000 had not registered
    {"img": "CCTAN", **_PORT},               # 21 s30-32  new parties; the vote didn't shrink
    {"img": "MAP1955", **_GFX},              # 22 s33-34  1955 seat results
    {"img": "S550404P6", **_P6_HEAD},        # 23 s35     "Looking For A Party"
    {"img": "S550403", **_S550403_RES},      # 24 s36     combined votes vs seats (results table)
    {"img": "S550404P6", **_P6_LOW},         # 25 s37-38  split votes in three-cornered fights
    {"img": "PPLOGO", **_GFX},               # 26 s39-41  more than arithmetic
    {"img": "S550404", **_S550404_TAN},      # 27 s42     "We stand alone, says C. C. Tan"
    {"img": "S560201P5", **_S560201_HEAD},   # 28 s43-44  the merger
    {"img": "S560206", **_S560206_HEAD},     # 29 s45     the Liberal Socialist council
    {"img": "LSPLOGO", **_GFX},              # 30 s46-47  1959, compulsory voting
    {"img": "AERIAL", **_OUT},               # 31 s48-50  no seats; PAP forms the government
    {"img": "CHART", **_GFX},                # 32 s51-53  the chart
    {"img": "S480320", **_S480320_HEAD},     # 33 s54-55  what changed: registration, compulsory voting
    {"img": "S550404P6", **_P6_HEAD},        # 34 s56-57  first past the post, as the paper worked out
    {"img": "HALL", **_OUT},                 # 35 s58-59  closing
]

SCHEDULE = [
    (0.0, 0), (6.5, 1), (15.3, 2), (25.75, 3), (34.6, 4), (45.15, 5),
    (52.625, 6), (74.175, 7), (88.075, 8), (96.375, 9), (113.075, 10),
    (124.475, 11), (147.975, 12), (157.1, 13), (175.2, 14), (188.95, 15),
    (198.4, 16), (204.65, 17), (221.025, 18), (236.6, 19), (260.125, 20),
    (278.7, 21), (305.0, 22), (332.75, 23), (339.875, 24), (365.5, 25), (384.375, 26),
    (413.0, 27), (419.525, 28), (440.325, 29), (454.05, 30), (472.55, 31),
    (493.375, 32), (512.075, 33), (534.325, 34), (555.35, 35),
]
TOTAL_DURATION = 582.05
TIMING_JSON = "audio/the-progressive-party-the-colonial-era-party-that-won-singapores-first-elections-then-vanished.timing.json"

# The avatar presenter, Phase 1 test: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)]}
