"""Video config for the Jurong Island post.

The pool is the post and gallery's thirteen pictures -
the 1945 War Office map extract, the locator map, the
island from the sea in 2011 (two frames) and at sunset,
the night view from Jurong Hill in 2009, the view from
Jurong Hill Tower in 2021, the 2006 panorama with the
highway, the Power Seraya station, the two PacificLight
photographs and the island in June 2026 - plus the six
USGS Landsat frames of 1973, 1989, 2000, 2002, 2009 and
2018 and their grid, which the post itself carries as
the merging animation and the gallery as the grid. The
frames are public domain (US Government) and were
byte-verified against the post's own animation sources
on 2026-11-25. The post's animation file itself is the
one pool item not used here; the grid and the six frames
carry the same content as stills.

Named-place audit: the Power Seraya photograph sits
only under the Seraya power-station sentences. The two
PacificLight photographs sit only under sentences that
name no company (opening day's sixty companies, the
hundred-plus companies of today, the 2025 plan, the
sustainable-output figure). Sentences naming Esso, SPC,
SRC or PCS carry the generic from-the-sea refinery
views, never another firm's plant. Named-person audit:
the pool holds no portraits; sentences naming Ismail,
Hamzah or Goh Chok Tong carry the map, the sea or the
hill views.

Every slide carries its discreet photo title (standing
rule, Chris, 2026-11-11): the short form of its image's
post/gallery caption, drawn small in the top corner on a
soft dark backing for the slide's whole run.

70 slides, 947.225s. No slide over 30s; the longest is
the 2025 reinvention catalogue at 28.95s. Narration:
Kokoro with the OpenVoice clone. Pronunciation overrides
for the post's names filed 2026-11-24, NOT ear-verified
yet. AVATAR: first and last 30s, cartoon with motion.
"""

IMAGES = {
    "HERO": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Jurong_Island%2C_Singapore_-_20110227-01.jpg",
    "JACKLEE02": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Jurong_Island%2C_Singapore_-_20110227-02.jpg/1280px-Jurong_Island%2C_Singapore_-_20110227-02.jpg",
    "SUNSET": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg/1280px-Ships_near_Jurong_Island%2C_Singapore%2C_at_sunset_-_20110227-01.jpg",
    "MAP1945": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Singapore_-_Jurong_Islands_1945.jpg",
    "LOCATOR": "https://upload.wikimedia.org/wikipedia/commons/1/15/Jurong_Island_locator_map.png",
    "SERAYA": "https://upload.wikimedia.org/wikipedia/commons/d/db/Power_Seraya_Power_Station.jpg",
    "NIGHT": "https://upload.wikimedia.org/wikipedia/commons/7/72/Aerial_view_of_Jurong_Island_from_Hill_top.jpg",
    "SEA2026": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Jurong_Island_June_2026.jpg/1280px-Jurong_Island_June_2026.jpg",
    "HILL2021": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg/1280px-Jurong_Island_viewed_from_the_top_of_Jurong_Hill_Tower.jpg",
    "PANORAMA": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg/1920px-Jurong_Industrial_Estate_and_Jurong_Island%2C_panorama%2C_Nov_06.jpg",
    "PLP2016": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/PLPPowerPlant.jpg/1280px-PLPPowerPlant.jpg",
    "PLPFOO": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/PLPplant.jpg/1280px-PLPplant.jpg",
    "GRID": "https://pikaia.github.io/assets/images/jurong-landsat-grid.jpg",
    "L73": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/1973_Jurong%28chs.%201%2C4%2C2%29.png",
    "L89": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/1989_Jurong%28chs.%207%2C4%2C2%29.png",
    "L00": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/2000_Jurong%28chs.%207%2C4%2C2%29.png",
    "L02": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/2002_Jurong%28chs.%207%2C4%2C2%29.png",
    "L09": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/2009_Jurong%28chs.%207%2C4%2C2%29.png",
    "L18": "https://eros.usgs.gov/sites/eros.usgs.gov/files/2020-12/5-24-2018_Jurong%28chs_7%2C5%2C4%29.png",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The channel's 2x2 thumbnail grid, in story order: the
# seven islands in 1945, the kampong-era strait, the
# island today, the satellite's finished island.
THUMBNAIL = [
    {"img": "MAP1945", "pan": (0.5, 0.5)},
    {"img": "SUNSET", "pan": (0.5, 0.5)},
    {"img": "HERO", "pan": (0.5, 0.5)},
    {"img": "L18", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"

SLIDES = [
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 0  title (3.62s) (s0 title),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 1  the island everyone depends on, none will visit (6.75s) (s1),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 2  petrol, gas, plastic: everything passes through it (16.75s) (s2),
    {"img": "LOCATOR", **{"type": "cover", "title": "Jurong Island, south-west Singapore", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 3  it is not one island at all (5.35s) (s3),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.3, 0.5)] * 3, "ease": _E}},  # 4  seven joined into one fortress; the strait was Selat Sembilan (22.23s) (s4-5),
    {"img": "SUNSET", **{"type": "cover", "title": "Ships near Jurong Island at sunset, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 5  Ismail the penghulu counts nine islands (17.30s) (s6),
    {"img": "HILL2021", **{"type": "cover", "title": "Jurong Island from Jurong Hill Tower, 2021", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 6  his account recorded in 1981, after his own relocation (11.93s) (s7),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 7  the count does not hold: the 1939 map shows fourteen (10.65s) (s8-9),
    {"img": "LOCATOR", **{"type": "cover", "title": "Jurong Island, south-west Singapore", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 8  the name is older: Sinbolan, Samulun, Semulun (22.07s) (s10),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 9  an open question: the sea people's own geography (10.78s) (s11),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.7, 0.5)] * 3, "ease": _E}},  # 10  the seven islands that were merged, named (18.10s) (s12),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 11  smaller islets absorbed; 991 hectares together (8.62s) (s13-14),
    {"img": "SUNSET", **{"type": "cover", "title": "Ships near Jurong Island at sunset, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 12  every island lived on: the Orang Laut groups (25.57s) (s15),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 13  the kampong names are the map of that lost world (19.35s) (s16-18),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.7, 0.5)] * 3, "ease": _E}},  # 14  Merlimau's villages: the lime names repeated (17.00s) (s19),
    {"img": "SUNSET", **{"type": "cover", "title": "Ships near Jurong Island at sunset, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 15  Seraya, the largest village island, four kampongs (11.72s) (s20),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.3, 0.5)] * 3, "ease": _E}},  # 16  Sakra's Tanah Merah; Pesek's Kampong Pesek (5.25s) (s21),
    {"img": "SUNSET", **{"type": "cover", "title": "Ships near Jurong Island at sunset, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 17  some names keep their stories: the well that never ran dry (19.35s) (s22-23),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.7, 0.5)] * 3, "ease": _E}},  # 18  Ayer Chawan: the glass cups dug from its soil (8.60s) (s24),
    {"img": "SUNSET", **{"type": "cover", "title": "Ships near Jurong Island at sunset, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 19  Pesek's two name stories; Sakra's monkeys or shikra (16.15s) (s25-26),
    {"img": "HILL2021", **{"type": "cover", "title": "Jurong Island from Jurong Hill Tower, 2021", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 20  Hamzah, Seraya's last penghulu; his voice in the Archives (22.07s) (s27-28),
    {"img": "SEA2026", **{"type": "cover", "title": "Jurong Island, June 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 21  the memory still gathered, a generation on (7.65s) (s29),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 22  industry did not arrive on an empty shore (5.70s) (s30),
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 23  1968: Ayer Chawan acquired and leased to Esso (18.30s) (s31),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 24  the refinery starts, 1970; village island to refinery island (11.18s) (s32-33),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 25  Merlimau followed: SPC on stream, July 1973 (11.68s) (s34-35),
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 26  the oil shock; SPC, BP and Caltex form SRC, 1979 (14.80s) (s36),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 27  SRC still there, at 1 Merlimau Road (15.80s) (s37),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 28  the ambition widened in the 1980s (3.75s) (s38),
    {"img": "HILL2021", **{"type": "cover", "title": "Jurong Island from Jurong Hill Tower, 2021", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 29  PCS: Southeast Asia's first ethylene plant, 1984 (23.98s) (s39),
    {"img": "SERAYA", **{"type": "cover", "title": "Power Seraya Power Station, 2019", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 30  Seraya merged 1979; the first offshore power station, 1988 (26.73s) (s40),
    {"img": "SERAYA", **{"type": "cover", "title": "Power Seraya Power Station, 2019", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 31  finished in stages by 1997; now YTL PowerSeraya's (6.80s) (s41),
    {"img": "L73", **{"type": "cover", "title": "Landsat view, 1973 (USGS)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 32  the islands had already begun to merge, plot by plot (19.50s) (s42),
    {"img": "LOCATOR", **{"type": "cover", "title": "Jurong Island, south-west Singapore", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 33  the 1990s amalgamation generalised what industry started (6.75s) (s43),
    {"img": "SUNSET", **{"type": "cover", "title": "Ships near Jurong Island at sunset, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 34  and the villages? rehoused in HDB flats, jobs provided (19.55s) (s44-45),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 35  one group resettled three times over (13.88s) (s46),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.3, 0.5)] * 3, "ease": _E}},  # 36  no total count exists, and none is invented; the shape of it (13.50s) (s47-48),
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 37  25 October 1988: fire at an SRC naphtha tank on Merlimau (25.18s) (s49-50),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 38  the worst refinery fire in Singapore's history; no lives lost (16.10s) (s51-53),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 39  the 2011 fire people remember was Bukom, not here (19.40s) (s54),
    {"img": "L89", **{"type": "cover", "title": "Landsat view, 1989 (USGS)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 40  the amalgamation plan conceived; JTC takes charge, 1991 (18.88s) (s55),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 41  reclamation began 1995; Penta-Ocean's Phase 3 (21.30s) (s56-57),
    {"img": "L00", **{"type": "cover", "title": "Landsat view, 2000 (USGS)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 42  finished 25 September 2009, twenty years early (6.67s) (s58),
    {"img": "L02", **{"type": "cover", "title": "Landsat view, 2002 (USGS)", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 43  991 hectares became 3,000 hectares of new land (11.90s) (s59),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 44  the road link came first: the highway, 1999-2000 (11.05s) (s60),
    {"img": "PLPFOO", **{"type": "cover", "title": "PacificLight Power plant", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 45  opened 14 October 2000; sixty companies, S$20 billion in (21.05s) (s61-62),
    {"img": "GRID", **{"type": "cover", "title": "Landsat views of the merger, 1973-2018 (USGS)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 46  the Landsat satellites watched it happen (5.80s) (s63),
    {"img": "L09", **{"type": "cover", "title": "Landsat view, 2009 (USGS)", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 47  their frames: the only honest before-and-after (15.03s) (s64),
    {"img": "L18", **{"type": "cover", "title": "Landsat view, 2018 (USGS)", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 48  what the satellites saw needs no commentary (3.65s) (s65),
    {"img": "SEA2026", **{"type": "cover", "title": "Jurong Island, June 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 49  the island the satellites see is only the top layer (4.15s) (s66),
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 50  beneath Banyan Basin: five rock caverns, 130 m down (17.98s) (s67),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 51  the Jurong Rock Caverns opened, September 2014 (13.93s) (s68),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 52  the southern tip: the reason Pipelines readers know (9.50s) (s69),
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 53  until 2013, all gas arrived by pipeline (8.78s) (s70),
    {"img": "HILL2021", **{"type": "cover", "title": "Jurong Island from Jurong Hill Tower, 2021", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 54  the LNG terminal: commercial operation, May 2013 (15.55s) (s71),
    {"img": "NIGHT", **{"type": "cover", "title": "Jurong Island at night, 2009", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 55  the insurance policy made concrete (14.00s) (s72),
    {"img": "HILL2021", **{"type": "cover", "title": "Jurong Island from Jurong Hill Tower, 2021", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 56  a protected area since 2001 (6.65s) (s73),
    {"img": "PANORAMA", **{"type": "cover", "title": "Jurong Island Highway and industrial estate, 2006", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 57  a pass needs a sponsor; biometrics at the checkpoint (13.07s) (s74),
    {"img": "HILL2021", **{"type": "cover", "title": "Jurong Island from Jurong Hill Tower, 2021", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 58  the Army guards the land, the Police Coast Guard the water (13.10s) (s75),
    {"img": "PLP2016", **{"type": "cover", "title": "PacificLight Power station, 2015", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 59  over a hundred companies, a hundred kilometres of pipe racks (11.05s) (s76),
    {"img": "NIGHT", **{"type": "cover", "title": "Jurong Island at night, 2009", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 60  every photograph taken from outside the fence (14.07s) (s77-78),
    {"img": "HILL2021", **{"type": "cover", "title": "Jurong Island from Jurong Hill Tower, 2021", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 61  the most consequential place Singaporeans cannot see (6.85s) (s79),
    {"img": "SEA2026", **{"type": "cover", "title": "Jurong Island, June 2026", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 62  twenty-five in 2025: a change of direction (9.50s) (s80),
    {"img": "PLPFOO", **{"type": "cover", "title": "PacificLight Power plant", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 63  the refreshed plan: specialty chemicals, sustainable materials (17.02s) (s81),
    {"img": "PLP2016", **{"type": "cover", "title": "PacificLight Power station, 2015", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}},  # 64  sustainable products up 1.4 times since 2019 (6.17s) (s82),
    {"img": "SEA2026", **{"type": "cover", "title": "Jurong Island, June 2026", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 65  SAF rig, ammonia, solar, a low-carbon data centre park (28.95s) (s83),
    {"img": "JACKLEE02", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.0, 1.06, 1.12], "pan": [(0.65, 0.5)] * 3, "ease": _E}},  # 66  the island built for oil, retooled for after oil (5.88s) (s84),
    {"img": "HERO", **{"type": "cover", "title": "Jurong Island from the sea, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.4)] * 3, "ease": _E}},  # 67  where it fits in the bigger story (14.40s) (s85),
    {"img": "MAP1945", **{"type": "cover", "title": "The Jurong islands in 1945", "zoom": [1.0, 1.06, 1.12], "pan": [(0.3, 0.5)] * 3, "ease": _E}},  # 68  the seven islands gone from the map, present in the names (13.30s) (s86),
    {"img": "SUNSET", **{"type": "cover", "title": "Ships near Jurong Island at sunset, 2011", "zoom": [1.12, 1.06, 1.0], "pan": [(0.35, 0.5)] * 3, "ease": _E}},  # 69  nine were really fourteen, and are now one (8.57s) (s87),
]

SCHEDULE = [
    (0.000, 0), (3.625, 1), (10.375, 2),
    (27.125, 3), (32.475, 4), (54.700, 5),
    (72.000, 6), (83.925, 7), (94.575, 8),
    (116.650, 9), (127.425, 10), (145.525, 11),
    (154.150, 12), (179.725, 13), (199.075, 14),
    (216.075, 15), (227.800, 16), (233.050, 17),
    (252.400, 18), (261.000, 19), (277.150, 20),
    (299.225, 21), (306.875, 22), (312.575, 23),
    (330.875, 24), (342.050, 25), (353.725, 26),
    (368.525, 27), (384.325, 28), (388.075, 29),
    (412.050, 30), (438.775, 31), (445.575, 32),
    (465.075, 33), (471.825, 34), (491.375, 35),
    (505.250, 36), (518.750, 37), (543.925, 38),
    (560.025, 39), (579.425, 40), (598.300, 41),
    (619.600, 42), (626.275, 43), (638.175, 44),
    (649.225, 45), (670.275, 46), (676.075, 47),
    (691.100, 48), (694.750, 49), (698.900, 50),
    (716.875, 51), (730.800, 52), (740.300, 53),
    (749.075, 54), (764.625, 55), (778.625, 56),
    (785.275, 57), (798.350, 58), (811.450, 59),
    (822.500, 60), (836.575, 61), (843.425, 62),
    (852.925, 63), (869.950, 64), (876.125, 65),
    (905.075, 66), (910.950, 67), (925.350, 68),
    (938.650, 69),
]
TOTAL_DURATION = 947.225
TIMING_JSON = "audio/jurong-island-seven-islands-into-one.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
