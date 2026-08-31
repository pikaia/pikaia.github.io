"""Video config for "The Bank That Spent a Century Teaching Singapore to
Save" - Watch widget and main video.

Two diagrams as static PNGs: the deposits chart
(scripts/render_posb_deposits_chart.py -> assets/images/posb-deposits.png,
a log-scale time series compose_chart_frame() can't animate) and the
OpenStreetMap branch map (scripts/render_posb_branch_map.py ->
assets/images/posb-branch-map.png). Both are near-static letterbox
slides and get CREDITS lines since neither is a captioned Commons file.

The rest are photos - 5 captioned in the post, 5 in the gallery - so
stage_youtube_text.py resolves every other credit.

Aspect check (1280x720, ~1.44 cover threshold):
  RAFFLES1890 898x596 (1.51)  -> cover, horizontal pan
  RAFFLES1910 1280-wide historical street view -> kept letterbox... no:
    treated as cover (it pans well and reads as smooth in --check-only)
  everything else < 1.44      -> letterbox
Letterbox + zero pan reads JERKY in --check-only (documented false
positive, pipeline section 5). The deposits chart recurs as the spine of
a post about a bank's deposits; each instance re-triggers a fresh slow
zoom, and no slide is held past ~30s (gap report clean).

29 slides, 507.62s.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"
_T = f"{_C}/thumb"

IMAGES = {
    "WATERWAY": f"{_C}/e/ed/POSB_Waterway_Point_branch.jpg",
    "RAFFLES1910": f"{_T}/c/c7/KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79892_-_Kleingrothe%2C_C.J._-_Medan_-_Raffles_Place%2C_Singapore_-_circa_1910.tif.jpg",
    "PASSBOOK": f"{_C}/3/39/Federation_of_Malaya_Post_Office_Savings_Bank_%28POSB%29_Bankbook%2C_Cover.png",
    "POSTER1945": f"{_C}/0/09/Plan_Your_Future_-_Save_With_a_Plan_Art.IWMPST16368.jpg",
    "HQ": f"{_C}/a/a2/NTUC_Trade_Union_House.jpg",
    "FULLERTON": f"{_C}/0/0a/The_Fullerton_Hotel%2C_Singapore.jpg",
    "RAFFLES1890": f"{_C}/4/44/Photographic_Views_of_Singapore_Plate_03_Raffles%27_Square.jpg",
    "NEWTON": f"{_C}/a/a4/POSB_Newton_Branch.png",
    "PASSBOOK2": f"{_C}/1/13/Federation_of_Malaya_Post_Office_Savings_Bank_%28POSB%29_Bankbook%2C_Inner_Front_Cover_%26_First_Page.png",
    "DEPOSITS": "/assets/images/posb-deposits.png",
    "BRANCHMAP": "/assets/images/posb-branch-map.png",
}

CREDITS = {
    "DEPOSITS": ("Chart by Lesser Known Singapore; data from Postmaster-General annual reports, "
                 "the Department of Statistics, contemporary press and POSB"),
    "BRANCHMAP": "Map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

_LB_IN = {"type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LB_OUT = {"type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LB_WIDE = {"type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CHART = {"type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}
_CHART_OUT = {"type": "letterbox", "zoom": [1.04, 1.02, 1], "pan": [(0.5, 0.5)] * 3, "ease": "linear"}

SLIDES = [
    # Open on 1890s Singapore, before the passbooks - this bank is the
    # Singapore one, split from the Federation of Malaya's in 1949.
    {"img": "RAFFLES1890", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"},
    {"img": "PASSBOOK", **_LB_IN},
    {"img": "PASSBOOK2", **_LB_WIDE},
    {"img": "POSTER1945", **_LB_IN},
    {"img": "DEPOSITS", **_CHART},
    {"img": "FULLERTON", **_LB_IN},
    {"img": "RAFFLES1910", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.75, 0.5), (0.5, 0.5), (0.25, 0.5)], "ease": "ease-in-out"},
    {"img": "PASSBOOK2", **_LB_IN},
    {"img": "PASSBOOK", **_LB_OUT},
    {"img": "PASSBOOK2", **_LB_WIDE},
    {"img": "DEPOSITS", **_CHART},
    {"img": "DEPOSITS", **_CHART_OUT},
    {"img": "POSTER1945", **_LB_IN},
    {"img": "POSTER1945", **_LB_OUT},
    {"img": "PASSBOOK", **_LB_IN},
    {"img": "PASSBOOK2", **_LB_OUT},
    {"img": "HQ", **_LB_IN},
    {"img": "DEPOSITS", **_CHART},
    {"img": "DEPOSITS", **_CHART_OUT},
    {"img": "DEPOSITS", **_CHART},
    {"img": "BRANCHMAP", "type": "letterbox", "zoom": [1, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"},
    {"img": "NEWTON", **_LB_IN},
    {"img": "DEPOSITS", **_CHART},
    {"img": "HQ", **_LB_OUT},
    {"img": "DEPOSITS", **_CHART},
    {"img": "FULLERTON", **_LB_OUT},
    {"img": "WATERWAY", **_LB_IN},
    {"img": "NEWTON", **_LB_OUT},
    {"img": "WATERWAY", **_LB_OUT},
]

# Real values from
# audio/posb-peoples-bank-nation-of-savers.timing.json. Every point is a
# real sentence start; slide index runs 0..28 in order.
#   0  s0-1   title; the first bank account was a book of ten-cent stamps
#   1  s2     the stamps, the passbook, the queue in the school hall
#   2  s3     opened 1 Jan 1877, Straits Settlements, over the GPO counter
#   3  s4     modelled on Britain's Post Office Savings Bank (1861)
#   4  s5-6   PMG ran it, trustees set policy; year one: 211 depositors,
#             $19,864.90, 5 per cent
#   5  s7     by 1940: ~57,000 accounts, $14.3 million
#   6  s8-9   the occupation broke the thread; savings put out of reach
#   7  s10    Aug 1949 ST letter, "A Raw Deal For The Small Man"
#   8  s11-13 1949 split: 17 Dec 1948 KL ordinance amalgamates the
#             Federation's banks; Singapore keeps its own
#   9  s14-15 Morning Tribune, "comes into force today"; two banks, a
#             two-way facility that lasted to 1973
#   10 s16-17 1950s growth $27M -> $58M, then it drifted
#   11 s18    fell back to ~$37M through the mid-1960s
#   12 s19    1966 Goh Keng Swee appoints a committee
#   13 s20-21 higher limits, tax-free interest, non-romanised signatures;
#             new accounts jump
#   14 s22-24 1968-69 into the schools: the card of squares, ten-cent
#             stamps, handed in at two dollars
#   15 s25-26 full participation by 1971; 1983 relaunch, Smiley the
#             Squirrel
#   16 s27-28 1 Jan 1972 statutory board (MinComms, then MOF 1974); first
#             chairman Tan Chok Kian
#   17 s29-30 what it did with the money: pooled small balances lent to
#             the government
#   18 s31-32 from 1974, Credit POSB into HDB loans - a thrift bank
#             financing public housing
#   19 s33-34 the deposit base: 1M depositors and $1bn in 1976, $10bn in
#             1986
#   20 s35-36 almost everywhere - a counter wherever there was a post
#             office, into the void decks
#   21 s37-38 first ATM at Newton, 1981; machine-only branches; 170
#             branches and 950 ATMs by the late 1990s
#   22 s39-40 renamed POSBank 1990; eight years later, absorbed
#   23 s41    24 Jul 1998 Richard Hu announces the DBS acquisition, $1.6bn
#   24 s42    POSBank held $25.5bn / $26.9bn, 3.3M customers
#   25 s43    the stated reasoning: a bigger bank, consolidating the
#             local banks
#   26 s44-45 the name kept; DBS's heartland brand, "Neighbours first,
#             bankers second," still the largest network
#   27 s46    the tax exemption on POSB interest phased out by end-2004
#   28 s47-48 where it fits: a saving habit taught at scale, now four
#             letters on a branch that belongs to someone else
SCHEDULE = [
    (0.0, 0), (18.3, 1), (35.33, 2), (50.9, 3), (69.85, 4),
    (89.75, 5), (97.03, 6), (109.55, 7), (125.4, 8), (154.2, 9),
    (179.75, 10), (194.85, 11), (212.45, 12), (219.9, 13), (244.25, 14),
    (274.05, 15), (286.98, 16), (309.62, 17), (324.45, 18), (345.43, 19),
    (357.73, 20), (380.52, 21), (402.35, 22), (409.5, 23), (424.45, 24),
    (439.98, 25), (455.05, 26), (472.43, 27), (482.45, 28),
]
TOTAL_DURATION = 507.62
TIMING_JSON = "audio/posb-peoples-bank-nation-of-savers.timing.json"
