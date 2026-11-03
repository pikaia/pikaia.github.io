"""Video config for the Force Z post: the sinking of HMS Prince of
Wales and HMS Repulse, 10 December 1941.

The ten-picture pool, all captioned in the post or its gallery: the
battleship's arrival at Singapore (A6784) and in port; Phillips and
Palliser on the quay (IWM FE 487 - the only faces in the pool, used
only where one of them is named); Repulse in 1916 (NH 525), at sea
(AWM 044777) and leaving Singapore; the bombing attack (NH 60566)
and the two ships underway on the day (80-G-413520); Nakamura's
1942 painting of the battle; and the National Memorial at Alrewas.

Named-person rule: Phillips is shown where he is named (s20, s21,
s58) and Palliser where he is named (s39-40). Leach, Tennant,
Pulford, Vigors, Percival, Churchill and Haruki Iki have no
photographs in the pool, so their sentences show ships, the sea or
the memorial - never Phillips' or Palliser's faces. The pool is
thin for an eighteen-minute narration, so images return at new
story beats with different pans, as on the Bank of China post; the
memorial bookends the hook (s5) and the close (s93).

71 slides, 938.30s of story (the timing file's two Sources
entries are excluded - the post's Sources divider was restored
before the narration rerun). Narration: Kokoro with the OpenVoice
clone. AVATAR: first and last 30s, cartoon with motion.
"""

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

# The channel's 2x2 thumbnail grid, in story order: the arrival,
# the sailing, the attack, and the memorial today.
THUMBNAIL = [
    {"img": "ARRIVE", "pan": (0.5, 0.5)},
    {"img": "LEAVE", "pan": (0.5, 0.5)},
    {"img": "TORP", "pan": (0.5, 0.5)},
    {"img": "MEM", "pan": (0.5, 0.5)},
]

_E = "ease-in-out"
_IN = {"type": "cover", "zoom": [1.0, 1.06, 1.12], "pan": [(0.5, 0.5)] * 3, "ease": _E}
_OUT = {"type": "cover", "zoom": [1.12, 1.06, 1.0], "pan": [(0.5, 0.5)] * 3, "ease": _E}

SLIDES = [
    {"img": "ARRIVE", **_IN},  # 0  s0 title (4.3s)
    {"img": "POWSG", **_OUT},  # 1  s1 the arrival: two of the most powerful warships in the world (11.5s)
    {"img": "ARRIVE", **_IN},  # 2  s2 the first battle fleet ever based at Singapore (10.2s)
    {"img": "TORP", **_OUT},  # 3  s3 eight days later, both on the seabed off Kuantan (9.5s)
    {"img": "BOMB", **_IN},  # 4  s4 no shot from the famous guns; the blow came from the air (9.4s)
    {"img": "MEM", **_OUT},  # 5  s5 the deterrent that deterred nothing; the wrecks fought over today (8.8s)
    {"img": "POWSG", **_IN},  # 6  s6 the gesture: Churchill's fleet in being (21.6s)
    {"img": "ARRIVE", **_OUT},  # 7  s7 the force: Prince of Wales, Repulse, Indomitable (14.3s)
    {"img": "POWSG", **_IN},  # 8  s8 Prince of Wales, barely a year old and already famous (16.3s)
    {"img": "REPOLD", **_OUT},  # 9  s9 Repulse, her opposite: a greyhound of the First World War (12.0s)
    {"img": "REPOLD", **_IN},  # 10  s10 then the plan lost its shield (4.2s)
    {"img": "REPSEA", **_OUT},  # 11  s11-12 Indomitable aground at Kingston; she never caught up (14.7s)
    {"img": "POWSG", **_IN},  # 12  s13 no carrier: known in London, and accepted (13.3s)
    {"img": "PAINT", **_OUT},  # 13  s14-15 Tokyo's answer: trained, for the first time, to kill fast ships at sea (20.2s)
    {"img": "ARRIVE", **_IN},  # 14  s16 the arrival was everything the gesture had promised (6.0s)
    {"img": "ARRIVE", **_OUT},  # 15  s17 up the Johore Strait to Sembawang; Percival's thrill (23.3s)
    {"img": "POWSG", **_IN},  # 16  s18-19 the front page; for a few days the island felt protected (8.0s)
    {"img": "QUAY", **_OUT},  # 17  s20 Phillips takes command (named: his photograph) (9.8s)
    {"img": "QUAY", **_IN},  # 18  s21 the desk admiral the fleet called Tom Thumb (12.2s)
    {"img": "POWSG", **_OUT},  # 19  s22 brave, clever and utterly certain of his own judgement (6.3s)
    {"img": "POWSG", **_IN},  # 20  s23-24 the captains: Leach and Tennant (their ship, no other faces) (18.9s)
    {"img": "BOMB", **_OUT},  # 21  s25 war came to Singapore before the fleet could go looking for it (4.3s)
    {"img": "POWSG", **_IN},  # 22  s26 the 8th of December: raids, and the landings at Kota Bharu (17.1s)
    {"img": "LEAVE", **_OUT},  # 23  s27-28 Hawaii kills the last assumption; the two ships cannot fight the Japanese navy (15.0s)
    {"img": "REPSEA", **_IN},  # 24  s29 a fleet in harbour while the army fought was no deterrent at all (10.4s)
    {"img": "LEAVE", **_OUT},  # 25  s30 that evening Force Z sailed (11.6s)
    {"img": "REPSEA", **_IN},  # 26  s31 they sailed handicapped (4.9s)
    {"img": "TORP", **_OUT},  # 27  s32 the flagship's radars dead in the tropical heat (16.9s)
    {"img": "POWSG", **_IN},  # 28  s33-34 fighter cover refused; he sailed anyway, in radio silence (16.6s)
    {"img": "TORP", **_OUT},  # 29  s35-36 the curtain held a day; then I-65 found them (18.9s)
    {"img": "REPSEA", **_IN},  # 30  s37-38 unseen, he turned for home; the two fleets passed in the darkness (18.8s)
    {"img": "QUAY", **_OUT},  # 31  s39-40 the message that killed them: Palliser's report (named: his photograph) (14.7s)
    {"img": "TORP", **_IN},  # 32  s41-42 he turned north to strike it; the report was false (12.8s)
    {"img": "REPSEA", **_OUT},  # 33  s43 Express off Kuantan: empty beaches, the town asleep (7.8s)
    {"img": "TORP", **_IN},  # 34  s44 I-58's five torpedoes missed, and no one ever knew (13.0s)
    {"img": "BOMB", **_OUT},  # 35  s45-46 a scout plane found the fleet in clear sunshine; the bombers were on their way (14.1s)
    {"img": "PAINT", **_IN},  # 36  s47 from eleven thirteen: what followed changed what a warship was (11.4s)
    {"img": "BOMB", **_OUT},  # 37  s48 the first wave: eight level bombers against Repulse alone (12.5s)
    {"img": "TORP", **_IN},  # 38  s49 the torpedo bombers came next, in waves (9.6s)
    {"img": "REPSEA", **_OUT},  # 39  s50-51 Repulse combed nineteen torpedoes; Prince of Wales was not so lucky (10.5s)
    {"img": "TORP", **_IN},  # 40  s52 one torpedo aft, where the propeller shaft left the hull (10.1s)
    {"img": "TORP", **_OUT},  # 41  s53 the spinning shaft tore the glands apart; the sea poured in (13.3s)
    {"img": "PAINT", **_IN},  # 42  s54-55 the Japanese officer's astonishment at the empty sky (18.4s)
    {"img": "POWSG", **_OUT},  # 43  s56 the fighters at Sembawang: 453 Squadron's Buffaloes (12.0s)
    {"img": "LEAVE", **_IN},  # 44  s57 Vigors' standing-cover proposal had been turned down (9.7s)
    {"img": "QUAY", **_OUT},  # 45  s58 no call for help left the flagship: Phillips kept his silence (named: his photograph) (6.8s)
    {"img": "REPSEA", **_IN},  # 46  s59 Tennant, in Repulse, finally broke silence (his ship) (7.8s)
    {"img": "BOMB", **_OUT},  # 47  s60-61 by then his ship was dying; the last wave caught Repulse in a pincer (18.6s)
    {"img": "REPSEA", **_IN},  # 48  s62 Tennant ordered his men over the side; at twelve thirty-three Repulse went down (7.0s)
    {"img": "TORP", **_OUT},  # 49  s63 Prince of Wales: three more torpedoes, and a bomb in the cinema flat (21.0s)
    {"img": "PAINT", **_IN},  # 50  s64-65 at one eighteen the flagship sank; at one eighteen the Buffaloes arrived (11.6s)
    {"img": "REPSEA", **_OUT},  # 51  s66-67 Vigors over the men in the water: 'above human nature' (17.6s)
    {"img": "LEAVE", **_IN},  # 52  s68-69 the destroyers did the rest: Electra alone pulled out 571 men (26.1s)
    {"img": "MEM", **_OUT},  # 53  s70-71 2,081 saved; 840 were not (the memorial for the toll) (17.6s)
    {"img": "REPSEA", **_IN},  # 54  s72-73 Tennant survived; Pulford's apology on the quay (17.0s)
    {"img": "PAINT", **_OUT},  # 55  s74 Haruki Iki flew back alone and dropped two wreaths (14.9s)
    {"img": "POWSG", **_IN},  # 56  s75-76 the shock reached London: 'Tom Phillips is drowned' (19.0s)
    {"img": "ARRIVE", **_OUT},  # 57  s77 Churchill: 'I never received a more direct shock' (12.2s)
    {"img": "TORP", **_IN},  # 58  s78 the first capital ships in history sunk by air power alone at sea (13.1s)
    {"img": "LEAVE", **_OUT},  # 59  s79-80 a land fortress with no fleet; nine weeks later Singapore surrendered (15.9s)
    {"img": "TORP", **_IN},  # 60  s81-82 the ships are still there: the wrecks off Kuantan (22.0s)
    {"img": "MEM", **_OUT},  # 61  s83 every Royal Navy ship that passes holds a service over the site (6.1s)
    {"img": "POWSG", **_IN},  # 62  s84 a war grave of pre-war steel, valuable because it predates the bomb (17.6s)
    {"img": "MEM", **_OUT},  # 63  s85 the bell, brought up in 2002, at the Merseyside Maritime Museum (11.9s)
    {"img": "TORP", **_IN},  # 64  s86 2014: the wrecks reported damaged by explosives (8.0s)
    {"img": "BOMB", **_OUT},  # 65  s87 May 2023: the Fuzhou-registered salvage vessel detained off Johor (19.2s)
    {"img": "MEM", **_IN},  # 66  s88-89 'distressed and concerned... They are designated war graves' (16.9s)
    {"img": "ARRIVE", **_OUT},  # 67  s90 and the remembering goes on (6.8s)
    {"img": "POWSG", **_IN},  # 68  s91 September 2025: the new Prince of Wales stops over the wrecks (the namesake) (14.3s)
    {"img": "MEM", **_OUT},  # 69  s92 a young officer of the Akebono at the rail, honouring the same dead (17.6s)
    {"img": "MEM", **_IN},  # 70  s93 the ships' real garrison is memory, and it has held (bookend with the hook) (12.2s)
]

SCHEDULE = [
    (0.000, 0), (4.350, 1), (15.875, 2), (26.075, 3), (35.575, 4), (44.950, 5),
    (53.800, 6), (75.350, 7), (89.675, 8), (105.975, 9), (118.000, 10), (122.225, 11),
    (136.900, 12), (150.225, 13), (170.400, 14), (176.450, 15), (199.750, 16), (207.750, 17),
    (217.600, 18), (229.825, 19), (236.150, 20), (255.025, 21), (259.375, 22), (276.425, 23),
    (291.450, 24), (301.875, 25), (313.475, 26), (318.400, 27), (335.325, 28), (351.900, 29),
    (370.800, 30), (389.575, 31), (404.275, 32), (417.100, 33), (424.925, 34), (437.925, 35),
    (452.050, 36), (463.475, 37), (476.000, 38), (485.600, 39), (496.075, 40), (506.175, 41),
    (519.500, 42), (537.850, 43), (549.825, 44), (559.525, 45), (566.325, 46), (574.075, 47),
    (592.650, 48), (599.650, 49), (620.625, 50), (632.225, 51), (649.875, 52), (675.975, 53),
    (693.600, 54), (710.575, 55), (725.475, 56), (744.525, 57), (756.675, 58), (769.750, 59),
    (785.650, 60), (807.625, 61), (813.725, 62), (831.375, 63), (843.275, 64), (851.275, 65),
    (870.500, 66), (887.350, 67), (894.175, 68), (908.525, 69), (926.125, 70)
]
TOTAL_DURATION = 938.300
TIMING_JSON = "audio/force-z-the-sinking-of-the-prince-of-wales-and-repulse.timing.json"

# The avatar presenter, cartoon with motion: corner bubble for the first and last 30 s.
AVATAR = {"ranges": [(0, 30), (-30, None)], "motion": True}
