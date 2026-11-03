"""Short config for the Force Z post - synopsis-first.

A synopsis of the whole story, not a truncation (Chris's rule,
2026-11-01). The post makes twelve points, and the Short carries
all twelve, compressed:

  P1  The deterrent arrives - and eight days later both ships are
      on the seabed (s1, s3).
  P2  Force Z would go to Singapore with no carrier at all (s13).
  P3  Japan reinforced Indochina and trained its crews, for the
      first time, to kill fast ships under way at sea (s15).
  P4  Phillips sailed anyway - no fighter cover, strict radio
      silence (s34).
  P5  Palliser's report of a landing at Kuantan turned him north;
      the report was false (s41, s42).
  P6  The attack: one torpedo aft cripples Prince of Wales; the
      last wave catches Repulse in a pincer (s52, s61).
  P7  Repulse sinks at twelve thirty-three, the flagship at one
      eighteen (s62, s64).
  P8  At that very minute the Buffaloes of 453 Squadron arrive
      (s65).
  P9  Eight hundred and forty men were not saved (s71).
  P10 The first capital ships in history, steaming and fighting in
      the open sea, sunk by air power alone (s78).
  P11 The wrecks are war graves, and are being damaged for their
      pre-atomic steel (s86).
  P12 In September 2025 the new Prince of Wales and a Japanese
      officer laid wreaths over the wrecks together (s92).

Compressed out, as colour rather than points: the I-65 and I-58
submarine episodes, the rescue in detail, Iki's wreaths, the
Churchill telephone call and the 2023 detention narrative (its
point rides on s86).

The soundtrack is a re-cut of the full narration (sentences
0, 1, 3, 13, 15, 34, 41, 42, 52, 61, 62, 64, 65, 71, 78, 86, 92), built by scripts/build_short_audio.py into
audio/force-z-the-sinking-of-the-prince-of-wales-and-repulse-short.mp3
with its own re-based timing file, which TIMING_JSON below points
at; the engine reads the audio and the burned captions from it.
175.1s: over TikTok's one-minute floor with room, under the
three-minute Shorts cap. Named-person rule as in the main config:
Palliser's sentence shows the quay photograph, in which he stands;
everyone else named gets a ship, the sea or the memorial. Every
slide is letterboxed.
"""

WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "ARRIVE": "https://upload.wikimedia.org/wikipedia/commons/7/7f/HMS_PRINCE_OF_WALES_arrives_at_Singapore%2C_4_December_1941._A6784.jpg",
    "QUAY": "https://upload.wikimedia.org/wikipedia/commons/7/78/IWM_FE_487_Admirals_Phillips_and_Palliser.jpg",
    "POWSG": "https://upload.wikimedia.org/wikipedia/commons/f/f9/HMS_Prince_Of_Wales_in_Singapore.jpg",
    "REPSEA": "https://s3-ap-southeast-2.amazonaws.com/awm-media/collection/044777/screen/4086207.JPG",
    "REPOLD": "/assets/images/hms-repulse-1916-nh525.jpg",
    "LEAVE": "https://upload.wikimedia.org/wikipedia/commons/a/a5/HMS_Repulse_leaving_Singapore.jpg",
    "BOMB": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Japanese_high-level_bombing_attack_on_HMS_Prince_of_Wales_and_HMS_Repulse_on_10_December_1941_%28NH_60566%29.jpg",
    "TORP": "https://upload.wikimedia.org/wikipedia/commons/f/f6/HMS_Prince_of_Wales_and_HMS_Repulse_underway_with_a_destroyer_on_10_December_1941_%2880-G-413520%29.jpg",
    "PAINT": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Sea_Battle_off_Malaya%2C_Japanese_painting%2C_1942_%28SC_301094%29.jpg",
    "MEM": "https://upload.wikimedia.org/wikipedia/commons/e/e3/National_Memorial_to_the_Prince_of_Wales_and_Repulse.jpg",
}

# Every image is captioned in the post or its gallery.
CREDITS = {}

# The main video's thumbnail grid, re-panned for tall cells.
THUMBNAIL = [
    {"img": "ARRIVE", "pan": (0.5, 0.5)},
    {"img": "LEAVE", "pan": (0.5, 0.5)},
    {"img": "TORP", "pan": (0.5, 0.5)},
    {"img": "MEM", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_LB = {"type": "letterbox", "zoom": [1.0, 1.03, 1.06], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "ARRIVE", **_LB},   # s0 title (4.3s)
    {"img": "POWSG", **_LB},   # s1 P1: the arrival, 2 December 1941 (11.5s)
    {"img": "TORP", **_LB},   # s3 P1: eight days later both ships were on the seabed (9.5s)
    {"img": "POWSG", **_LB},   # s13 P2: no carrier - the shield was lost before she sailed (13.3s)
    {"img": "PAINT", **_LB},   # s15 P3: Tokyo's answer: crews trained to kill fast ships at sea (16.1s)
    {"img": "LEAVE", **_LB},   # s34 P4: he sailed anyway, in radio silence, cover refused (10.2s)
    {"img": "QUAY", **_LB},   # s41 P5: Palliser's report turns him north to Kuantan (named: his photograph) (10.4s)
    {"img": "TORP", **_LB},   # s42 P5: the report was false (2.4s)
    {"img": "TORP", **_LB},   # s52 P6: one torpedo aft cripples Prince of Wales (10.1s)
    {"img": "BOMB", **_LB},   # s61 P6: the last wave catches Repulse in a pincer (15.8s)
    {"img": "REPSEA", **_LB},   # s62 P7: twelve thirty-three, Repulse goes down (7.0s)
    {"img": "PAINT", **_LB},   # s64 P7: one eighteen, the flagship sinks (3.2s)
    {"img": "REPSEA", **_LB},   # s65 P8: at that very minute, the Buffaloes arrive (8.4s)
    {"img": "MEM", **_LB},   # s71 P9: 840 were not saved (14.1s)
    {"img": "TORP", **_LB},   # s78 P10: the first capital ships sunk by air power alone at sea (13.1s)
    {"img": "TORP", **_LB},   # s86 P11: the wrecks, war graves, damaged by scrap-metal explosives (8.0s)
    {"img": "MEM", **_LB},   # s92 P12: 2025 - British and Japanese officers lay wreaths together (17.6s)
]
SCHEDULE = [(0.000, 0), (4.350, 1), (15.875, 2), (25.375, 3), (38.700, 4), (54.850, 5), (65.025, 6), (75.475, 7), (77.850, 8), (87.950, 9), (103.750, 10), (110.750, 11), (113.975, 12), (122.350, 13), (136.450, 14), (149.525, 15), (157.525, 16)]
TOTAL_DURATION = 175.125
TIMING_JSON = "audio/force-z-the-sinking-of-the-prince-of-wales-and-repulse-short.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.70

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
