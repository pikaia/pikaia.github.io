"""Video config for the Bank of China Building post.

The seven-picture pool: the palazzo in the Photoglob photochrom of
about 1900 (the scene hero) and in a period postcard view; Battery
Road about 1905 (Lambert) and about 1910 (Kleingrothe/KITLV); the
Singapore River in September 1960 with the new tower standing over
the bumboats; and two CC0 photographs of September 2025 - the 1953
block from its own corner, entrance and lion included, and the same
block with the 2000 tower rising behind it.

Named-person rule: no portraits exist in the pool for Meikle,
Arbenz, the Gian Singh brothers, Lazarus Rayman, Rodolfo Nolli or
S. Rajaratnam, so their sentences show the building or the street,
never another person. Nolli's sentence (s53) shows the entrance of
the 1953 block panned low, where his lion stands. The pool is thin
for a 14-minute narration, so images repeat at new story beats
with different pans - bookends, not convenience repeats: the
photochrom opens the story and returns for the demolition (s39)
and the summing-up (s72); the lions are panned low at s53 and
again, as a closing beat, at s70.

62 slides, 843.17s. Narration: Kokoro with the OpenVoice clone.
AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "PHOTO": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Singapore._Chartered_Bank_Buildings._Battery_Road_LCCN2017657651.jpg/1920px-Singapore._Chartered_Bank_Buildings._Battery_Road_LCCN2017657651.jpg",
    "PAL": "https://upload.wikimedia.org/wikipedia/commons/7/79/Chartered_Bank_Building_Singapore.jpg",
    "KITLV": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif/lossy-page1-1280px-KITLV_-_79890_-_Kleingrothe%2C_C.J._-_Medan_-_Battery_Road_at_Singapore_-_circa_1910.tif.jpg",
    "ROAD": "https://upload.wikimedia.org/wikipedia/commons/4/42/Battery_Road%2C_c._1905.jpg",
    "RIVER": "https://upload.wikimedia.org/wikipedia/commons/5/57/SingaporeRiver-196009.jpg",
    "TODAY1": "https://upload.wikimedia.org/wikipedia/commons/2/22/Original_Bank_of_China_Building%2C_Singapore_20250903.jpg",
    "TODAY2": "https://upload.wikimedia.org/wikipedia/commons/3/34/Bank_of_China_Building%2C_Singapore_20250903.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the palazzo in
# colour, the palazzo again as the postcard age saw it, the tower
# over the working river in 1960, and the two buildings today.
THUMBNAIL = [
    {"img": "PHOTO", "pan": (0.5, 0.5)},
    {"img": "PAL", "pan": (0.5, 0.5)},
    {"img": "RIVER", "pan": (0.35, 0.45)},
    {"img": "TODAY2", "pan": (0.5, 0.35)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}
# The tall 2025 photographs: pans toward the top (the tower) or the
# bottom (the entrance and the lion).
_INT = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.22)] * 3, "ease": _E}
_OUTT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.22)] * 3, "ease": _E}
_INL = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.8)] * 3, "ease": _E}
_OUTL = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.8)] * 3, "ease": _E}
# One slow downward drift for the long extension sentence (s68):
# the 2000 tower first, settling to the old block at street level.
_DRIFT = {"type": "cover", "zoom": [1.0, 1.05, 1.1], "pan": [(0.5, 0.25), (0.5, 0.45), (0.5, 0.65)], "ease": _E}

SLIDES = [
    {"img": "PHOTO", **_IN},  # 0  s0 title: the Bank of China Building on Battery Road (3.7s)
    {"img": "PAL", **_OUT},  # 1  s1 the hook: $715,000 for a palace, May 1937 (16.0s)
    {"img": "ROAD", **_IN},  # 2  s2 the palace stayed a store; the bank stayed in Cecil Street (12.2s)
    {"img": "TODAY2", **_INT},  # 3  s3-4 the tower it built on the site; the forgotten half (12.1s)
    {"img": "PAL", **_IN},  # 4  s5 built for another bank entirely (4.0s)
    {"img": "PHOTO", **_OUT},  # 5  s6 the 1893 lease; McAlister and McKerrow's godowns; Meikle (names men: the building) (25.8s)
    {"img": "PHOTO", **_IN},  # 6  s7 the bank moved in, 6 February 1895 (4.8s)
    {"img": "PAL", **_OUT},  # 7  s8 the palazzo described: pilasters, urns, sixty feet (22.4s)
    {"img": "PHOTO", **_OUT},  # 8  s9 the banking hall within (12.6s)
    {"img": "KITLV", **_IN},  # 9  s10 readers met it in the exchange banks post (10.2s)
    {"img": "ROAD", **_OUT},  # 10  s11-12 the Chartered outgrows it and moves out, 1916 (13.2s)
    {"img": "KITLV", **_OUT},  # 11  s13 the Bank of Taiwan and Mitsui Bussan Kaisha take the floors (9.7s)
    {"img": "PAL", **_IN},  # 12  s14 vacant into 1933; Arbenz; Publicity House (names him: the building) (14.6s)
    {"img": "ROAD", **_IN},  # 13  s15 Gian Singh & Co. opens, October 1934 (names the brothers: the street) (18.0s)
    {"img": "PHOTO", **_IN},  # 14  s16 the bullion palace had become a shop (4.0s)
    {"img": "KITLV", **_OUT},  # 15  s17-18 the Bank of China arrives by a different door; founded 1912 for remittances (19.6s)
    {"img": "ROAD", **_OUT},  # 16  s19 the branch opens in Cecil Street, 15 June 1936 (11.3s)
    {"img": "KITLV", **_IN},  # 17  s20 a thousand guests; nine RAF planes circle (10.9s)
    {"img": "PAL", **_OUT},  # 18  s21-22 a year later: the $715,000 land deal announced (19.5s)
    {"img": "PHOTO", **_IN},  # 19  s23-24 numbered 4-6 Battery Road; a name on a deed, nothing more (10.7s)
    {"img": "ROAD", **_IN},  # 20  s25 four years of lease to run; the palace trades on (10.4s)
    {"img": "PAL", **_IN},  # 21  s26-27 the war of the lease, 1940: eviction sought (21.4s)
    {"img": "ROAD", **_OUT},  # 22  s28-29 refused; only a cigarette stall goes (15.3s)
    {"img": "KITLV", **_OUT},  # 23  s30-31 the larger war: the branch closes, the stores trade on, the Mutsumi restaurant (26.0s)
    {"img": "PAL", **_OUT},  # 24  s32 the army's requisition ends, November 1946 (9.6s)
    {"img": "ROAD", **_IN},  # 25  s33-34 Singapore's 'squat' drama: out by 15 January 1947 (14.3s)
    {"img": "KITLV", **_IN},  # 26  s35 they stayed put; Lazarus Rayman restores the water and power (names him: the street) (16.2s)
    {"img": "PAL", **_IN},  # 27  s36 goods worth $30,000 stolen from the new premises (10.8s)
    {"img": "ROAD", **_OUT},  # 28  s37-38 sued in February; both stores gone by March (14.6s)
    {"img": "PHOTO", **_OUT},  # 29  s39 demolition under way by May 1947 (the palace's bookend) (10.8s)
    {"img": "RIVER", **_IN},  # 30  s40 the plans: fourteen storeys, 200 feet (12.0s)
    {"img": "TODAY1", **_INT},  # 31  s41 foundations from November 1948, slow out of care for the neighbours (15.8s)
    {"img": "TODAY1", **_OUT},  # 32  s42-43 the most dated document: Peking approves the superstructure, May 1950 (13.8s)
    {"img": "RIVER", **_OUT},  # 33  s44 the head office was now in Peking (16.5s)
    {"img": "TODAY1", **_IN},  # 34  s45 the revolution arriving in paperwork (7.9s)
    {"img": "RIVER", **_IN},  # 35  s46 tenders March 1951; construction from April; $3 million (9.7s)
    {"img": "TODAY2", **_OUTT},  # 36  s47 Palmer and Turner of Hong Kong, building the same bank's premises there (8.6s)
    {"img": "TODAY1", **_IN},  # 37  s48 finished December 1953; the bank moves in on the 28th (11.2s)
    {"img": "RIVER", **_OUT},  # 38  s49 seventeen years after Cecil Street, sixteen after buying the site (9.0s)
    {"img": "TODAY1", **_IN},  # 39  s50 like Shanghai and Hong Kong, with Chinese touches of its own (16.0s)
    {"img": "TODAY2", **_IN},  # 40  s51 the lowest three and top three floors; safe deposits below (7.8s)
    {"img": "TODAY1", **_OUTT},  # 41  s52 a building of firsts: mail chute, document lifts, central air-conditioning (14.4s)
    {"img": "TODAY1", **_INL},  # 42  s53 Nolli's lions at the Battery Road entrance (names him: his lions, panned low) (13.9s)
    {"img": "TODAY2", **_OUT},  # 43  s54 still on guard at the door today (5.8s)
    {"img": "TODAY2", **_IN},  # 44  s55 about the tower's height, one careful paragraph (10.0s)
    {"img": "RIVER", **_OUT},  # 45  s56 200 feet; the Heritage Board's claim, fairly made (20.6s)
    {"img": "TODAY2", **_IN},  # 46  s57 but never the tallest building in Singapore (taller neighbours in frame) (3.7s)
    {"img": "RIVER", **_IN},  # 47  s58 the Cathay Building was already taller in 1939; Asia Insurance followed (17.1s)
    {"img": "RIVER", **_OUT},  # 48  s59 what it genuinely was: tallest on the Singapore River waterfront (11.7s)
    {"img": "ROAD", **_IN},  # 49  s60-61 the hardest test came from politics; Malaya's branches closed in 1959 (22.2s)
    {"img": "KITLV", **_OUT},  # 50  s62 December 1964: Kuala Lumpur announces the closure (18.5s)
    {"img": "ROAD", **_OUT},  # 51  s63 Singapore opposed it; Rajaratnam criticised it (names him: the street) (21.1s)
    {"img": "RIVER", **_IN},  # 52  s64-65 never carried out; independence lets the branch continue (20.6s)
    {"img": "TODAY1", **_IN},  # 53  s66 the tower had survived its second change of flags (5.2s)
    {"img": "TODAY2", **_OUTT},  # 54  s67 the building today is two buildings (3.2s)
    {"img": "TODAY2", **_DRIFT},  # 55  s68 the $90 million extension; ground broken 1994; the tower of 2000 (28.2s)
    {"img": "TODAY1", **_IN},  # 56  s69 the old block still stands: headquarters, main branch, historical gallery (21.2s)
    {"img": "TODAY1", **_OUTL},  # 57  s70 the lions remain at the entrance (bookend with s53) (3.1s)
    {"img": "TODAY2", **_OUT},  # 58  s71 no conservation status; unlisted and largely unremarked (22.8s)
    {"img": "PHOTO", **_IN},  # 59  s72 where it fits in the bigger story: back to the corner (10.0s)
    {"img": "PAL", **_OUT},  # 60  s73 its second life: a site bought in 1937 as an option on the future (24.9s)
    {"img": "TODAY2", **_IN},  # 61  s74 few corners carry the whole arc in a single address (11.8s)
]

SCHEDULE = [
    (0.000, 0), (3.725, 1), (19.700, 2), (31.850, 3), (44.000, 4), (47.950, 5),
    (73.775, 6), (78.575, 7), (101.000, 8), (113.600, 9), (123.825, 10), (137.075, 11),
    (146.775, 12), (161.375, 13), (179.375, 14), (183.425, 15), (202.975, 16), (214.325, 17),
    (225.275, 18), (244.800, 19), (255.525, 20), (265.900, 21), (287.325, 22), (302.675, 23),
    (328.650, 24), (338.225, 25), (352.525, 26), (368.700, 27), (379.475, 28), (394.100, 29),
    (404.900, 30), (416.925, 31), (432.725, 32), (446.550, 33), (463.050, 34), (470.975, 35),
    (480.700, 36), (489.325, 37), (500.475, 38), (509.450, 39), (525.475, 40), (533.225, 41),
    (547.675, 42), (561.625, 43), (567.450, 44), (577.475, 45), (598.025, 46), (601.725, 47),
    (618.775, 48), (630.450, 49), (652.700, 50), (671.225, 51), (692.350, 52), (712.925, 53),
    (718.100, 54), (721.275, 55), (749.500, 56), (770.700, 57), (773.800, 58), (796.550, 59),
    (806.575, 60), (831.425, 61)
]
TOTAL_DURATION = 843.175
TIMING_JSON = "audio/the-bank-of-china-building-on-battery-road.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
