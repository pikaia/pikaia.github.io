"""Video config for "The Japanese Garden That Reconciliation Built, Then
Forgot" (Seiwaen, Jurong) - Watch widget and main video.

No chart in this post, but there is a locations map: an annotated
OpenStreetMap tile (assets/images/japanese-garden-jurong-lake-map.png,
committed per the OSM / route-walk convention, "Map data (c)
OpenStreetMap contributors" on the image and in Sources) showing the
Japanese Garden and the neighbouring Chinese Garden on Jurong Lake. It
runs three times - the "artificial island in Jurong Lake" beat, the
"folded into Jurong Lake Gardens" beat, and the close.

Images (3 post + the map + 5 gallery):
  REDBRIDGE  - the red arched bridge, 2012 (post hero)
  JGMAP      - the Jurong Lake locations map
  GARDEN2015 - a general view of the garden, 2015
  MOONBRIDGE - the moon bridge in the reopened garden, 2024
  DBLBEAUTY  - the Double Beauty Bridge to the Chinese Garden, 2024
  NICHES     - horticultural-showcase niches added in the 2024 redesign
  GARDEN2012 - a view of the garden, 2012 (the years of quiet decline)
  BRIDGE2012 - a bridge within the original garden, 2012
  GROUNDS2015- another view of the grounds, 2015

18 slides, 320.25s. Aspect check (1280x720, ~1.44 cover threshold):
  REDBRIDGE 3911x2458 (1.59)  -> cover, horizontal pan
  JGMAP 1242x666 (1.86)       -> letterbox (near-16:9), near-zero zoom
  GARDEN2015 4592x2866 (1.60) -> cover, horizontal pan
  MOONBRIDGE 3948x2504 (1.58) -> cover, horizontal pan
  DBLBEAUTY 4009x2564 (1.56)  -> cover, horizontal pan
  NICHES 3236x3068 (1.05)     -> letterbox (near-square)
  GARDEN2012 3648x2736 (1.33) -> letterbox
  BRIDGE2012 1600x1200 (1.33) -> letterbox
  GROUNDS2015 4504x3330 (1.35)-> letterbox
Letterbox slides use zero pan (blurred-bg zoom only), so --check-only
flags them JERKY - the documented letterbox false positive (pipeline
section 5); the near-static JGMAP slides read JERKY for the same reason.
Several slides run 24-28s over one or two long sentences with no closer
internal timing.json boundary; slow zooms carry them.
"""

_C = "https://upload.wikimedia.org/wikipedia/commons"

IMAGES = {
    "REDBRIDGE": f"{_C}/0/08/Redbridge_%288166305323%29.jpg",
    "JGMAP": "/assets/images/japanese-garden-jurong-lake-map.png",
    "GARDEN2015": f"{_C}/1/1c/Singapore_Japanischer_Garten_3.jpg",
    "MOONBRIDGE": f"{_C}/a/ac/Moon_bridge%2C_Japanese_Garden%2C_Singapore_202409.jpg",
    "DBLBEAUTY": f"{_C}/4/41/Double_Beauty_Bridge%2C_Singapore.jpg",
    "NICHES": f"{_C}/9/92/Niches_with_horticultural_showcase%2C_Japanese_Garden%2C_Singapore_202409.jpg",
    "GARDEN2012": f"{_C}/f/fc/2012-07-07_Jurong_East_26.JPG",
    "BRIDGE2012": f"{_C}/1/1a/Bridge_at_Japanese_Gardens_%288153514054%29.jpg",
    "GROUNDS2015": f"{_C}/3/3d/Singapore_Japanischer_Garten_5.jpg",
}

CREDITS = {
    "JGMAP": "Locations map by Lesser Known Singapore; base map data © OpenStreetMap contributors",
}

SLIDES = [
    {"img": "REDBRIDGE", "type": "cover", "zoom": [1, 1.03, 1.06], "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)], "ease": "ease-in-out"},
    {"img": "MOONBRIDGE", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"},
    {"img": "GARDEN2015", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.15, 0.5), (0.5, 0.5), (0.85, 0.5)], "ease": "ease-in-out"},
    {"img": "GROUNDS2015", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "BRIDGE2012", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "JGMAP", "type": "letterbox", "zoom": [1, 1.015, 1.03], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "REDBRIDGE", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.65, 0.5), (0.5, 0.5), (0.35, 0.5)], "ease": "ease-in-out"},
    {"img": "GARDEN2012", "type": "letterbox", "zoom": [1, 1.06, 1.12], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in-out"},
    {"img": "GROUNDS2015", "type": "letterbox", "zoom": [1.10, 1.05, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "GARDEN2015", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.7, 0.5), (0.5, 0.5), (0.3, 0.5)], "ease": "ease-out"},
    {"img": "BRIDGE2012", "type": "letterbox", "zoom": [1.12, 1.06, 1], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-out"},
    {"img": "GARDEN2012", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "JGMAP", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
    {"img": "DBLBEAUTY", "type": "cover", "zoom": [1, 1.05, 1.10], "pan": [(0.2, 0.5), (0.5, 0.5), (0.8, 0.5)], "ease": "ease-in-out"},
    {"img": "NICHES", "type": "letterbox", "zoom": [1, 1.05, 1.10], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "ease-in"},
    {"img": "MOONBRIDGE", "type": "cover", "zoom": [1.10, 1.05, 1], "pan": [(0.8, 0.5), (0.5, 0.5), (0.2, 0.5)], "ease": "ease-out"},
    {"img": "REDBRIDGE", "type": "cover", "zoom": [1, 1.06, 1.12], "pan": [(0.3, 0.5), (0.5, 0.5), (0.7, 0.5)], "ease": "ease-in-out"},
    {"img": "JGMAP", "type": "letterbox", "zoom": [1, 1.02, 1.04], "pan": [(0.5, 0.5), (0.5, 0.5), (0.5, 0.5)], "ease": "linear"},
]

# Real values from
# audio/japanese-garden-jurong-seiwaen-reconciliation.timing.json.
# Every point is a real sentence start.
#   0  s0      title
#   1  s1      the Sept 2024 reopening - water lilies, a sunken garden,
#              a "Breathing Gallery" of terrariums
#   2  s2-3    nothing explained why the garden is there / 50 years on,
#              the 1973 opening was an act of postwar reconciliation
#   3  s4-5    reconciliation was hard: the 1962 mass graves, the blood-
#              debt rallies, the 1966 S$50m settlement - the backdrop
#   4  s6-8    it closed the formal account, required nothing friendlier
#              than a memorial / the garden grew out of the same thaw
#   5  s9      MAP - work began May 1968 on a 32-acre island in the newly
#              dammed Jurong Lake, jointly funded, incl. the local
#              Japanese business community
#   6  s10     Seiwaen, by Kinsaku Nakane - Muromachi/Momoyama aesthetics:
#              karesansui gravel, koi ponds, vermilion bridges
#   7  s11-13  five years, S$3m / opened 16 Feb 1973, Goh Keng Swee cut
#              the ribbon / his speech never said reconciliation, Japan or
#              occupation
#   8  s14     he filed it alongside the Stadium and Sentosa's golf course
#              as leisure infrastructure - "pleasant relaxation", "a
#              notable tourist attraction"
#   9  s15     then spent the speech on having no symphony orchestra and
#              on "the barbarous form of music produced by the steel
#              guitar"
#   10 s16-17  the reconciliation went unspoken at its own opening / for a
#              while it worked as intended
#   11 s18     the gardens aged the way 1970s civic amenities do - dated
#              rather than serene
#   12 s19     MAP - by 2014 both were folded into Jurong Lake Gardens;
#              they closed in May 2019 for a five-year rebuild
#   13 s20     what reopened kept the Double Beauty Bridge and fragments
#              of Nakane's stonework, but the pitch was entirely new
#   14 s21     nowhere in the coverage or the marketing does the original
#              purpose resurface
#   15 s22     a garden built as an unspoken act of peace is now simply a
#              nice place to walk
#   16 s23     the reckoning produced a tribunal, a euphemism-settled
#              dispute, and 32 acres of Muromachi-style garden as an
#              afterthought
#   17 s24     MAP - that it went unstated even at its ribbon-cutting says
#              as much as any memorial built to remember
SCHEDULE = [
    (0.0, 0), (4.8, 1), (23.975, 2), (48.65, 3), (76.45, 4),
    (90.55, 5), (113.55, 6), (133.15, 7), (158.5, 8), (184.8, 9),
    (205.175, 10), (217.85, 11), (234.95, 12), (250.5, 13), (270.25, 14),
    (278.775, 15), (287.45, 16), (306.575, 17),
]
TOTAL_DURATION = 320.25
TIMING_JSON = "audio/japanese-garden-jurong-seiwaen-reconciliation.timing.json"
