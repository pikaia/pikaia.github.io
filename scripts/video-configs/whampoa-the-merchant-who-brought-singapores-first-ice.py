"""Video config for the Whampoa post.

Ten images for a topic where actual photos of the man/estate are
scarce - two portraits (a formal Wellcome studio photo, and an earlier
lower-quality one), the Keppel friendship (a formal photo plus a Tissot
Vanity Fair caricature), the Boat Quay riverside where his ice house
stood, a genuine 1886 illustration of the garden's own entrance avenue,
a present-day street-sign photo pairing Bendemeer/Whampoa, the
self-made locations map, and two present-day "the name today" shots
(the hawker centre, the park).

  HERO          - Wellcome studio portrait, CMG + second medal (hero)
  HOO_SMALL     - an earlier, lower-quality surviving portrait
  KEPPEL        - Admiral of the Fleet Sir Henry Keppel, formal photo
  KEPPEL_TISSOT - Henry Keppel, Vanity Fair caricature by James Tissot
  BOATQUAY      - Boat Quay, Singapore, c. 1900 postcard
  GARDEN_ILLUS  - "Avenue to Whampoa's Gardens", 1886 illustration
  BENDEMEER_SIGN - Bendemeer Rd, with a "Whampoa South" sign visible
  MAP           - self-made map: Boat Quay / Serangoon Rd / Tanglin / Keppel Harbour
  WHAMPOA_MAKAN - Whampoa Makan Place, lit up at night
  WHAMPOA_PARK  - Whampoa Park entrance sign, present day

Landscape photos use centred cover zoom; the portrait images and the
label-heavy map use letterbox instead (cover would crop the map's text
labels or a portrait photo down to a sliver - see
docs/production-pipeline.md §3).

33 slides, 389.85s.
"""

_U = "https://upload.wikimedia.org/wikipedia/commons"
_C = f"{_U}/thumb"

IMAGES = {
    "HERO": f"{_C}/7/7b/The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg/1280px-The_Hon._Hoh-Ah-Kay_Whampoa%2C_C.M.G.%2C_M.L.C.%2C_and_Consul_for_Wellcome_V0037527.jpg",
    "HOO_SMALL": f"{_U}/c/cc/Hoo_Ah_Kay.jpg",
    "KEPPEL": f"{_U}/9/95/Admiral_of_the_Fleet_Sir_Henry_Keppel.jpg",
    "KEPPEL_TISSOT": f"{_U}/d/d0/Henry_Keppel.JPG",
    "BOATQUAY": f"{_U}/b/b6/Singapore_Boat_Quay_ca._1900.jpg",
    "GARDEN_ILLUS": f"{_U}/f/fb/Avenue_to_Whampoa%27s_Gardens_%281886%29.png",
    "BENDEMEER_SIGN": f"{_C}/e/eb/Bendemeer_Rd_bef_Whampoa_South_20060409.jpg/1280px-Bendemeer_Rd_bef_Whampoa_South_20060409.jpg",
    "MAP": "/assets/images/whampoa-the-merchant-who-brought-singapores-first-ice-map.png",
    "WHAMPOA_MAKAN": f"{_C}/c/c9/Whampoa_Makan_Place%2C_exterior.jpg/1280px-Whampoa_Makan_Place%2C_exterior.jpg",
    "WHAMPOA_PARK": f"{_C}/d/d8/Whampoa_Park.jpg/1280px-Whampoa_Park.jpg",
}

_CVZ = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_CVZO = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}
_LTB = {"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3, "ease": "ease-in-out"}
_LTBO = {"type": "letterbox", "zoom": [1.08, 1.04, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": "ease-out"}

SLIDES = [
    {"img": "HERO", **_LTB},            # 0  s0   title
    {"img": "WHAMPOA_MAKAN", **_CVZ},   # 1  s1   Whampoa as a place - housing estate, hawker centre
    {"img": "HERO", **_LTBO},           # 2  s2   almost nobody connects it to Hoo Ah Kay
    {"img": "BENDEMEER_SIGN", **_CVZ},  # 3  s3   I never lived in Whampoa myself
    {"img": "WHAMPOA_PARK", **_CVZO},   # 4  s4   never once wondered who it belonged to
    {"img": "HOO_SMALL", **_LTB},       # 5  s5   born 1816 in Whampoa, Canton
    {"img": "BOATQUAY", **_CVZ},        # 6  s6   arrived 1830, shipchandler to the Royal Navy
    {"img": "KEPPEL", **_LTBO},         # 7  s7   grew into a genuine friendship
    {"img": "KEPPEL_TISSOT", **_LTB},   # 8  s8   Henry Keppel, son of the Earl of Albemarle
    {"img": "KEPPEL", **_LTBO},         # 9  s9   revisited Singapore 1900, Keppel Harbour renamed
    {"img": "HERO", **_LTB},            # 10 s10  Whampoa was his regular provisioner
    {"img": "BOATQUAY", **_CVZO},       # 11 s11  1854, partnered with Gilbert Angus, ice
    {"img": "BOATQUAY", **_CVZ},        # 12 s12  blocks cut from frozen lakes, Tudor's technique
    {"img": "MAP", **_LTBO},            # 13 s13  a bet on demand that didn't exist yet
    {"img": "BOATQUAY", **_CVZO},       # 14 s14  projected 1,000 lbs a day, got 400 to 500
    {"img": "BOATQUAY", **_CVZ},        # 15 s15  30 November 1857, withdrew from the partnership
    {"img": "HOO_SMALL", **_LTBO},      # 16 s16  commercially, a flop
    {"img": "BOATQUAY", **_CVZO},       # 17 s17  the site outlived his failure
    {"img": "BOATQUAY", **_CVZ},        # 18 s18  Tudor Ice took over in 1861
    {"img": "BOATQUAY", **_CVZO},       # 19 s19  the Victorian ice house stood for a century
    {"img": "HOO_SMALL", **_LTB},       # 20 s20  Whampoa & Co itself didn't last
    {"img": "HERO", **_LTBO},           # 21 s21  public career outgrew his balance sheet
    {"img": "HERO", **_LTB},            # 22 s22  1869, first Asian on the Legislative Council
    {"img": "KEPPEL_TISSOT", **_LTBO},  # 23 s23  honorary consul for China, Japan, Russia
    {"img": "KEPPEL", **_LTB},          # 24 s24  none of it came from a title track
    {"img": "GARDEN_ILLUS", **_CVZ},    # 25 s25  a sprawling garden estate on Serangoon Road
    {"img": "GARDEN_ILLUS", **_CVZO},   # 26 s26  a gathering place, distinguished visitors
    {"img": "BENDEMEER_SIGN", **_CVZO}, # 27 s27  Seah Liang Seah, renamed Bendemeer House
    {"img": "MAP", **_LTB},             # 28 s28  1964, government acquired and demolished it
    {"img": "BENDEMEER_SIGN", **_CVZ},  # 29 s29  nothing of the garden survives, only road names
    {"img": "WHAMPOA_MAKAN", **_CVZO},  # 30 s30  why it matters today
    {"img": "WHAMPOA_PARK", **_CVZ},    # 31 s31  his actual businesses didn't survive him
    {"img": "HERO", **_LTBO},           # 32 s32  a smaller, quieter version of the same pattern
]

SCHEDULE = [
    (0.0, 0), (3.975, 1), (15.725, 2), (34.250, 3), (41.950, 4),
    (47.175, 5), (58.250, 6), (78.150, 7), (83.450, 8), (105.575, 9),
    (119.275, 10), (127.925, 11), (136.950, 12), (164.275, 13), (168.200, 14),
    (175.450, 15), (185.600, 16), (190.075, 17), (192.900, 18), (214.075, 19),
    (228.350, 20), (239.850, 21), (243.825, 22), (262.825, 23), (285.575, 24),
    (296.850, 25), (311.075, 26), (322.575, 27), (338.025, 28), (348.350, 29),
    (355.975, 30), (370.275, 31), (377.875, 32),
]
TOTAL_DURATION = 389.85
TIMING_JSON = "audio/whampoa-the-merchant-who-brought-singapores-first-ice.timing.json"
