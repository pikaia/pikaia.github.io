"""Generate a narration MP3 for a blog post using Kokoro TTS.

Local dev tool only - not part of the deployed Jekyll site. Extracts the
post's narrative paragraphs (skipping images, captions, back-links, and the
Sources section) and synthesizes them with Kokoro (hexgrad/Kokoro-82M,
Apache 2.0 licensed - both code and weights), voice bm_george by default
(British male; switched from af_heart 2026-08-21 after Chris compared it
on the Victoria Memorial Hall post and preferred it - see project memory).

Kokoro replaced edge-tts (2026-08) because edge-tts is an unofficial wrapper
around Microsoft Edge's "Read Aloud" feature with no clear license for
redistributing the synthesized audio in published posts/videos. Kokoro's
Apache 2.0 license resolves that ambiguity outright. Runs fine on CPU - no
GPU needed, quality is identical either way, just slower per-sentence.

Real per-sentence timestamps come free as a byproduct: each sentence is
synthesized as its own Kokoro call (see split_sentences() below - Kokoro's
own internal chunking is phoneme-length-driven, not sentence-aligned, so we
do our own splitting first), and its exact audio duration becomes that
sentence's timing. Written alongside the audio as <out>.timing.json and
<out>.srt - use these instead of guessing at even timing splits when
syncing captions/video to the audio.

Requires: pip install kokoro soundfile
(torch is a kokoro dependency; CPU-only build is fine: pip install torch
--index-url https://download.pytorch.org/whl/cpu)
First run downloads the model from Hugging Face (hexgrad/Kokoro-82M).

Usage:
    python scripts/generate_narration.py _posts/<file>.md audio/<slug>.mp3 [--voice bm_george]
"""
import argparse
import json
import os
import re
import sys
import warnings

BACK_LINK_RE = re.compile(r"^\[←\s*Back to all posts\]\(/\)$")
GALLERY_LINK_RE = re.compile(r"\[See[^\]]*\]\([^)]*\)")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_CAPTION_RE = re.compile(r"^\*[^*].*[^*]\*$", re.DOTALL)

# Raw-HTML block tags used in this codebase (floated images, charts, the
# listen widget). Whitelisted rather than matching any "<tag" generically,
# so JS/CSS content inside those blocks (e.g. "year < xMax") can't be
# mistaken for markup and thcorw off the depth count.
HTML_TAG_RE = re.compile(r"<(/?)(div|script|style|svg|audio|span|button|table|tr|td|th)\b", re.IGNORECASE)

# Words Kokoro's phonemizer (misaki) doesn't recognize and falls back to
# spelling out letter-by-letter instead of pronouncing - e.g. "Ng" (a
# Chinese surname, a syllabic nasal English can't say word-initially) came
# out as "N, G" on the fishball-noodle post. Keys match the exact casing
# as it appears in post text (misaki's lexicon lookup is case-sensitive
# unless the word is ALL CAPS); values are misaki/espeak-style IPA-ish
# phoneme strings, found by testing candidates against
# `misaki.en.G2P(british=False)` directly (e.g. borrowing the "-ing" ending
# from a known word like "sing" -> "sˈɪŋ") until the output sounds right.
# Add new entries here as they're caught, rather than guessing indefinitely
# from the doc/CLAUDE.md - always verify by ear against the real render.
# Mirror every new entry into docs/pronunciation-fixes.md too - that doc
# is a human-readable summary of this dict, not a separate source of
# truth, and the two are duplicated by design (keep them in sync by
# hand, same as the route-walk animation data described in CLAUDE.md).
PRONUNCIATION_OVERRIDES = {
    "Ng": "əŋ",  # anglicized "ung" (schwa + ng), closer to how the Chinese
                 # surname is actually said than the "ing" ending tried
                 # first - Chris confirmed by ear it's more "ung" than
                 # "ing". Applies to "Ng" and "Ng's" (misaki appends the
                 # possessive itself)
    "stung": "stˈʌŋ",  # misaki's own lexicon wrongly gives "stung" the same
                        # phonemes as "strung" (an extra "r" sound baked in,
                        # confirmed by testing both against misaki.en.G2P
                        # directly - not a post-text or code issue, an
                        # upstream dictionary bug) - caught by ear on the
                        # fishball-noodle post ("what stung was...")
    "graves": "ɡɹˈAvz",  # misaki gives plural "graves" the wrong vowel AND
                          # drops the plural entirely ("ɡɹˈɑːv", sounds like
                          # "grahv") - every other -aves word (caves, waves,
                          # saves, staves, braves, shaves) phonemizes fine
                          # ("ˈAvz"), so this looks like a lexicon entry
                          # mistakenly keyed to the Bordeaux wine region name
                          # (French pronunciation) instead of the burial-site
                          # plural. Caught by ear on the four-chopsticks post
                          # ("mass graves found around the island in 1962").
    "Kuan": "kwˈɑːn",  # unknown word (no lexicon entry) - "Kuan" as in "Lee
                        # Kuan Yew". Caught by scan_for_unknown_tokens()
                        # (the --dry-run "?" scan), not by ear - this name
                        # almost certainly recurs across other already-
                        # published posts on this blog, worth checking if
                        # any of them get re-narrated for another reason.
    "Yasukuni": "jˌasuːkˈuːni",  # unknown word (no lexicon entry) - the
                                  # Tokyo shrine. Anglicized 4-syllable
                                  # approximation (ya-soo-KOO-ni); caught by
                                  # scan_for_unknown_tokens(), not verified
                                  # by ear yet - flag if it sounds off.
    "rallied": "ɹˈalɪd",  # unknown word (no lexicon entry), even though the
                           # root "rally" phonemizes fine on its own -
                           # misaki is missing the inflected past-tense
                           # form specifically. Built from "rally"'s own
                           # root plus the regular "-ied" ending pattern
                           # (matches "carried"/"hurried"/"married").
                           # Caught by scan_for_unknown_tokens().
    "Siglap": "sˈɪɡlap",  # unknown word (no lexicon entry) - the Singapore
                           # neighbourhood. Built from "signal"'s "sig-"
                           # onset plus "lap"'s own phonemes. Caught by
                           # scan_for_unknown_tokens().
    "tapped": "tˈapt",  # unknown word (no lexicon entry) - surprising for
                         # such a common verb; "mapped" has the same gap,
                         # while "trapped"/"wrapped"/"snapped"/"clapped"/
                         # "napped" all phonemize fine, so this looks like a
                         # narrow lexicon hole for this specific inflection
                         # rather than something wrong with "-apped" in
                         # general. Built by direct analogy with those
                         # working "-apped" words. Caught by
                         # scan_for_unknown_tokens() on the Benjamin Sheares
                         # post.
    "Istana": "ɪstˈɑːnə",  # unknown word (no lexicon entry) - the
                            # President's official residence, mentioned
                            # across many posts on this blog. Anglicized,
                            # stress on the middle syllable, echoing the
                            # "-ana" ending in "banana"/"veranda". Caught by
                            # scan_for_unknown_tokens() on the Benjamin
                            # Sheares post - likely affects other posts
                            # mentioning the Istana too.
    "Kandang": "kˈandaŋ",  # unknown word (no lexicon entry) - half of
                            # "Kandang Kerbau", the historical Singapore
                            # district (and hospital) whose name means
                            # "buffalo pen" in Malay. "Kan-" borrowed from
                            # "Kandy"'s working phonemization, "-dang" from
                            # "hang"/"gang"'s "-ang" ending. Caught by
                            # scan_for_unknown_tokens() on the Benjamin
                            # Sheares post.
    "Kerbau": "kəbˈaʊ",  # unknown word (no lexicon entry) - see "Kandang"
                          # above, same place name. "Ker-" as a schwa,
                          # "-bau" borrowed from "how"/"now"'s "aʊ"
                          # diphthong. Caught by scan_for_unknown_tokens()
                          # on the Benjamin Sheares post.
    # These two are a different root cause from everything else in this
    # dict: not unknown, and not spelled out by mistake - misaki *can*
    # read them, correctly, as letters ("M-I-N-D-E-F", "F-O-F-O"), but
    # that's not how Singaporeans actually say either of them out loud.
    # Confirmed by Chris (2026-08-27): MINDEF is said as a blended word
    # ("min-def"), not spelled out - same for FOFO ("foh-foh"). Caught by
    # scan_for_letter_spelled_words(), which exists specifically for this
    # category (see its docstring) - unlike the unknown-word/symbol scan,
    # this one needs a human to confirm which letter-spelled tokens are
    # actually correct as spelled (e.g. "MRT", "CPF") vs wrong (these
    # two, and "II"/"VII" below).
    "MINDEF": "mˈɪndɛf",  # "min" (mˈɪn) + "def" (dˈɛf), stress only on
                           # the first syllable, matching the
                           # "logo"/"photo"/"hobo" two-syllable-compound
                           # stress pattern. Found on the National
                           # Service post.
    "FOFO": "fˈQfQ",  # "foe" (fˈQ) doubled, matching "logo"'s lˈQɡQ
                       # stress pattern (stress on the first syllable
                       # only). Found on the National Service post
                       # ("FOFO Hill").
    # The following 6 were all caught by scan_for_unknown_tokens() on the
    # Lim Chong Yah post - not this session's original target, but
    # surfaced anyway since the scan runs against the whole narrative,
    # not just the sentence being worked on. "Lim" in particular is worth
    # flagging: it's a common Chinese surname that appears in other posts
    # too (Lim Kim San, and Lim Peng Siang in docs/post-ideas.md), so
    # this fix likely helps narration well beyond the post that surfaced
    # it - the same pattern as "Kuan" earlier.
    "Lim": "lˈɪm",  # unknown word (no lexicon entry), even though
                     # near-identical names "Tim"/"Jim"/"dim" all
                     # phonemize fine (even "Kim" doesn't). Built by
                     # direct analogy with those.
    "Chong": "ʧˈɒŋ",  # unknown word (no lexicon entry) - built from
                       # "check"'s "ʧ" onset plus "song"/"long"/"wrong"/
                       # "gong"'s "-ong" ending.
    "Hainanese": "hˌInənˈiːz",  # unknown word (no lexicon entry), even
                                 # though "Hainan" alone phonemizes fine
                                 # (hInˈan) - the "-ese" demonym suffix is
                                 # the gap. Built by the same stress-shift
                                 # pattern "Chinese"/"Japanese"/
                                 # "Cantonese" all follow (secondary
                                 # stress on the country name, primary
                                 # stress moves to "-ese", middle syllable
                                 # reduces to a schwa).
    "Siow": "sˈW",  # unknown word (no lexicon entry) - a Chinese surname
                     # (Hokkien/Teochew romanization). Built by analogy
                     # with "how"/"now"/"cow"'s "-ow" diphthong as a
                     # single syllable rhyming with those - not verified
                     # by ear yet, flag if it sounds off (this romanized
                     # spelling could plausibly also be two syllables,
                     # "SEE-ow").
    "Nanyang": "nˌanjˈaŋ",  # unknown word (no lexicon entry) - as in
                             # Nanyang Technological University. Built
                             # from "Nan" (nˈan) + "yang" (jˈaŋ, as in
                             # yin-yang), secondary stress on the first
                             # syllable matching typical two-part
                             # Chinese-name compounds.
    "paycheck": "pˈAʧɛk",  # unknown word (no lexicon entry) - surprising
                            # for such a common compound, given "pay" and
                            # "check" both phonemize fine on their own;
                            # "daycare" has the same gap, so this looks
                            # like a narrow hole in misaki's compound-word
                            # handling rather than anything specific to
                            # payroll vocabulary. Built from "pay" + the
                            # existing "check" phonemes, stress pattern
                            # matching "payday"'s (pˈAdA).
    "paychecks": "pˈAʧɛks",  # see "paycheck" above - misaki doesn't
                              # reliably derive the plural from a fixed
                              # singular override, so both forms need
                              # their own entry.
    "Winsemius": "wɪnsˈiːmiəs",  # unknown word (no lexicon entry) -
                                  # Albert Winsemius, the Dutch economist
                                  # central to Singapore's early economic
                                  # development (likely to recur in other
                                  # posts on that topic). Anglicized:
                                  # "win" (wˈɪn) + "seem" (sˈiːm) +
                                  # "-ius" (from "genius"/"radius"'s
                                  # ending) - not verified by ear yet,
                                  # flag if it sounds off.
    "Kang": "kˈʌŋ",  # unknown word (no lexicon entry) - part of "Peng
                      # Kang Hill" on the National Service post. Chris
                      # confirmed by ear it rhymes with "hung"/"sung"/
                      # "rung" (an "-ung" vowel, not the "-ang" of
                      # "hang"/"gang" the surrounding letters suggest -
                      # verified by sending a synthesized "Peng Kang
                      # Hill" sample directly, not guessed from spelling
                      # alone).
    # "Dr Goh Keng Swee" - the economist/Deputy PM behind Jurong's
    # industrialization (likely to recur in other posts on that topic,
    # same as "Winsemius" above). All three names on the National
    # Service post; all three confirmed by ear against synthesized
    # samples, not just derived by analogy and left unverified.
    "Goh": "ɡˈQ",  # unknown word - "go"'s own vowel (as in "logo"'s
                    # "-go" ending, already used for "FOFO" above).
    "Keng": "kˈAŋ",  # unknown word - first guessed as "-ɛŋ" (matching
                      # "Sheng"/"Peng"'s working "-eng" pattern), but
                      # Chris corrected this by ear: it's actually the
                      # "cane"/"lane" vowel, not "bed"/"ten"'s - a good
                      # example of why guessing from a similar-looking
                      # name isn't reliable, only confirming by ear is.
    "Swee": "swˈiː",  # unknown word - straightforward, rhymes with
                       # "tree"/"free" plus an "sw" onset.
    # The following Malay place names are all on the National Service
    # post. First attempt at these was guessed by English-word analogy
    # and came back "mostly wrong" per Chris - standard Malay has its
    # own vowel system that doesn't map cleanly onto English vowels, so
    # guessing from spelling alone isn't reliable here the way it was
    # for Chinese-surname romanizations above. Rebuilt from real IPA
    # (Wiktionary's Malay entries where available) plus Chris's own
    # corrections by ear, not guessed a second time.
    "Pulau": "pˈuːlaʊ",  # confirmed correct by ear - matches Wiktionary
                          # IPA /ˈpulaw/ (POO-lau, stress first syllable).
    "Tekong": "təkˈɒŋ",  # no Wiktionary entry (a Singapore-specific place
                          # name) - Chris confirmed by ear: "tuh-KONG",
                          # stress on the second syllable, matching the
                          # IPA [təˈkɔŋ] he separately found.
    "Jurong": "ʤˈuːrɒŋ",  # confirmed correct by ear - matches Wiktionary
                           # IPA /dʒuːrɒŋ/ (JOO-rong). First guess used
                           # the "tour"/"poor" ʊə diphthong instead of a
                           # plain long "oo" - wrong vowel, corrected
                           # once the real IPA was checked. "Pulau" above
                           # is worth flagging the same way as "Lim"/
                           # "Istana"/"Winsemius" - it's a common word
                           # across many Singapore-history posts, not
                           # specific to this one.
    "Taman": "tˈaman",  # confirmed correct by ear. First guess
                         # ("tˈɑːmən") reduced the second syllable to a
                         # schwa, an English habit that doesn't apply to
                         # Malay - Malay keeps fuller vowels in
                         # unstressed syllables than English does. That
                         # same fix (schwa -> full "a") is what corrected
                         # the whole batch below too.
    "Bukit": "bˈuːkɪt",  # confirmed correct by ear.
    "Gombak": "ɡˈɒmbak",  # confirmed correct by ear.
    "Pasir": "pˈɑːsA",  # confirmed correct by ear - "PAH-say" (the
                         # "A" symbol is misaki's own for the "day"/"say"
                         # diphthong, not a plain "ah"). Also common
                         # across many Singapore place names (Pasir Ris,
                         # Pasir Panjang) beyond this post.
    "Laba": "lˈɑːbˌɑː",  # confirmed correct by ear - "LAH-bah", two full
                          # "ah" syllables (the second "ɑː" needed a
                          # stress mark of its own, or misaki reduced it
                          # to a schwa the same way "Taman" was wrong the
                          # first time).
    "Besar": "bəsˈɑː",  # confirmed correct by ear.
    "Kechil": "kətʃˈiːl",  # confirmed correct by ear.
    "Ris": "ɹˈɪs",  # unknown word - not actually used on the National
                     # Service post, but caught while verifying "Pasir"
                     # (as in the well-known "Pasir Ris" housing estate)
                     # and confirmed by ear, so fixed pre-emptively for
                     # whichever future post mentions it first.
    "Selabin": "sˌɜːlˈɑːbɪn",  # unknown word - one of three former
                                # kampong names on Pulau Tekong (National
                                # Service post), now repurposed as
                                # military training-area names. Confirmed
                                # by ear: "sir-LAH-bin".
    "Permatang": "pˌəmˌɑːtˈɑːŋ",  # unknown word - see "Selabin" above,
                                   # same context. Confirmed by ear:
                                   # "per-mah-tahng".
    "Sanyongkong": "sˌɑːnjˌɒŋkˈɒŋ",  # unknown word - see "Selabin"
                                      # above, but a different origin:
                                      # per Wikipedia, this was a Chinese
                                      # settlement (rubber-plantation era),
                                      # not a Malay kampong like the other
                                      # two - which likely explains why
                                      # the name doesn't follow standard
                                      # Malay phonetics. Confirmed by ear:
                                      # "sahn-yohng-kohng".
    "tri-service": "trˌIsˈɜːvɪs",  # unknown word (no lexicon entry for
                                    # the hyphenated compound), even
                                    # though "tri-" and "service" both
                                    # phonemize fine separately (matches
                                    # "try"/"triangle"/"tricycle"'s "tɹˈI"
                                    # onset). Ordinary English gap, not
                                    # Malay/Chinese like the entries
                                    # above.
    "outgrown": "ˌWtɡɹˈQn",  # unknown word (no lexicon entry for the
                              # compound), even though "out" and "grown"
                              # both phonemize fine separately - the same
                              # kind of narrow compound-word gap as
                              # "paycheck"/"daycare" above.
    "portering": "pˈɔːtəɹɪŋ",  # unknown word (no lexicon entry), even
                                # though "porter" phonemizes fine on its
                                # own. Built from "porter" (pˈɔːtə) plus
                                # the regular "-ering" pattern from
                                # "catering"/"watering" (restores the
                                # linking "r" before the vowel-initial
                                # "-ing", same non-rhotic-linking rule
                                # those words already follow). Found on
                                # the silver-generation post.
    "majie": "mˈɑːʤɛ",  # unknown word (no lexicon entry) - 妈姐/媽姐, the
                         # Cantonese domestic-servant term on the amah post.
                         # "MAH-jeh": "ma" (mˈɑː, "father"/"spa" vowel) +
                         # "jie" as "jeh" (ʤɛ), following the Cantonese
                         # reading (姐 = ze2) and the variant spelling
                         # "mahjeh" - not the Mandarin-pinyin "jiě"/"jay".
                         # Confirmed by Chris (2026-08-28).
    "Jetstar": "ʤˈɛtstɑː",  # unknown word (no lexicon entry) - the budget
                              # airline, on the travel-bug post. "jet"
                              # (ʤˈɛt) + "star" (stɑː), stress on the first
                              # syllable, the same compound-word gap as
                              # "paycheck"/"outgrown" above.
    "phrasebook": "fɹˈAzbʊk",  # unknown word (no lexicon entry) - "phrase"
                                # (fɹˈAz, "A" = the "day"/"say" diphthong)
                                # + "book" (bʊk). Same compound gap.
                                # Travel-bug post.
    "Changi": "ʧɑːŋˈiː",  # unknown word (no lexicon entry) - the Singapore
                           # airport/district, appears across many posts on
                           # this blog. "chah-NGEE": "ch" onset + "ah"
                           # (ɑː) + "-ngee" with the /ŋ/ of "singer" (not a
                           # hard /ndʒ/), stress on the second syllable, long
                           # "ee". Confirmed by Chris by ear (2026-08-28),
                           # picked from three synthesized samples - the
                           # first-syllable-stress reading was the other
                           # main candidate.
}

# Abbreviated titles that misaki can't pronounce (falls back to "?", same
# failure mode as PRONUNCIATION_OVERRIDES above) - fixed by expanding the
# text itself before synthesis instead of a phoneme override, since a
# phoneme override still leaves the abbreviation's period as a literal
# mid-sentence pause token (tested: "Fr." -> phoneme override still
# produced an audible full-stop pause right after the word; text expansion
# to "Father" avoids the period entirely). Deliberately NOT pre-expanding
# every entry in ABBREVIATIONS above - several are ambiguous out of context
# ("St." = Saint or Street, "No." = Number or the word "no") and would risk
# a wrong expansion sounding worse than the original gap. Add an entry here
# only once actually heard mispronounced in a real render, matching
# PRONUNCIATION_OVERRIDES's policy above. Mirror new entries into
# docs/pronunciation-fixes.md too - see the note above that dict.
def _ordinal_suffix(n: int) -> str:
    """"st"/"nd"/"rd"/"th" for a day-of-month number (11-13 are always
    "th", including 11, 12, 13 - not just 11 - since "-teen" numbers don't
    follow the last-digit pattern the way 21, 22, 23... do)."""
    if 11 <= (n % 100) <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


ABBREVIATION_EXPANSIONS = {
    re.compile(r"\bFr\.(?=\s)"): "Father",
    # "S$" (Singapore dollar notation) - misaki produces a literal "?"
    # token for the "$" right after "S" ("S$50 million" -> "S <unknown>
    # fifty million"). Tried "SGD" as a fix first, but it spells out as
    # individual letters ("S, G, D") rather than saying "Sing Dollar" -
    # confirmed by testing directly against misaki.en.G2P. Reordering to
    # "<amount> <million/billion/thousand> Singapore dollars" (moving the
    # unit word after the amount, dropping the "S$" prefix, appending the
    # full phrase at the end) phonemizes correctly and reads naturally.
    # Plain "$" (used elsewhere for prices, e.g. "$2.70") is untouched -
    # this only matches the "S$" prefix specifically.
    re.compile(r"S\$(\d[\d,]*(?:\.\d+)?)(\s+(?:million|billion|thousand))?"): r"\1\2 Singapore dollars",
    # "DD Month" dates (the house style throughout post prose, e.g. "25
    # August 1963") - misaki reads the bare day numeral as a cardinal
    # ("twenty-five August"), but spoken English always reads the day-of-
    # month as an ordinal regardless of how it's written ("the twenty-fifth
    # of August"); the year stays cardinal ("nineteen sixty-three"), which
    # is why only the day gets touched here, not the whole date. Confirmed
    # by testing directly against misaki.en.G2P: appending the correct
    # ordinal suffix and restoring "the ... of" both phonemize correctly,
    # including misaki's own "a"/"an"-style linking of "the" to "ði" before
    # a vowel (e.g. "the 18th of February" -> "ði ˌAtˈiːnθ"). This is a
    # third, distinct root cause from the two in PRONUNCIATION_OVERRIDES's
    # dict comment above: not an unknown word, not a wrong lexicon entry,
    # but a correct entry read under the wrong number-reading convention -
    # misaki can't tell from a bare numeral alone whether it's a cardinal
    # or ordinal context. Matched as a function (not a static string) since
    # the correct suffix depends on the day's value.
    re.compile(r"\b(\d{1,2}) (January|February|March|April|May|June|July|August|September|October|November|December)\b"):
        lambda m: f"the {m.group(1)}{_ordinal_suffix(int(m.group(1)))} of {m.group(2)}",
    # "King Edward VII" (the college of medicine named after him) - misaki
    # applies its letter-spelling fallback to the Roman numeral after the
    # name ("V, I, I") instead of the ordinal a regnal number is actually
    # read as ("the Seventh"). This is the "letter-spelling fallback
    # applied to the wrong token" root cause (see the comment above
    # KNOWN_LETTER_SPELLED / scan_for_letter_spelled_words() further down
    # this file) - fixed as a literal phrase match here instead of a
    # general Roman-numeral pattern, since a Roman numeral after a name
    # is genuinely context-dependent: "World War II" is read as "World
    # War Two" (cardinal), not "World War the Second" (ordinal), so a
    # blanket regnal-number rule would get other cases wrong. Add another
    # literal entry here if a different regnal number is ever caught
    # mispronounced, rather than generalizing early.
    re.compile(r"\bKing Edward VII\b"): "King Edward the Seventh",
    # "Shock Therapy II" (the 1979 wage policy's own nickname, as used on
    # the Lim Chong Yah post) - same root cause as "King Edward VII"
    # above, but the *other* reading direction: a Roman numeral after a
    # program/sequel name is read as a cardinal ("World War Two"), not an
    # ordinal, unlike a person's regnal number. Caught by
    # scan_for_letter_spelled_words(), not scan_for_unknown_tokens() -
    # misaki reads "II" as fluent, confident letters ("I, I"), it just
    # doesn't know that's wrong here.
    re.compile(r"\bShock Therapy II\b"): "Shock Therapy Two",
    # A four-digit year range written with an en-dash or hyphen
    # ("2020-2021", "1997-2025") - misaki drops the dash as an audible
    # "?" and mushes the two years together ("twenty twenty? twenty
    # twenty one"). Spoken as "<year> to <year>", each year read as the
    # usual cardinal. Text substitution rather than a phoneme override
    # since the dash sits between two separate tokens. First hit: the
    # "2020-2021 collapse" on the travel-bug post.
    re.compile(r"\b(\d{4})[–-](\d{4})\b"): r"\1 to \2",
}


def _process_block(block: str, narrative: list[str]) -> bool:
    """Returns False if this block signals the Sources divider (stop)."""
    if block == "---":
        return False
    if block.startswith("!["):
        return True  # image
    if BACK_LINK_RE.match(block):
        return True
    if ITALIC_CAPTION_RE.match(block) and not block.startswith("**"):
        return True  # image caption

    cleaned = GALLERY_LINK_RE.sub("", block)
    cleaned = MD_LINK_RE.sub(r"\1", cleaned)
    cleaned = BOLD_RE.sub(r"\1", cleaned)
    for pattern, replacement in ABBREVIATION_EXPANSIONS.items():
        cleaned = pattern.sub(replacement, cleaned)
    cleaned = cleaned.strip()
    if cleaned:
        narrative.append(cleaned)
    return True


def extract_narrative(markdown_text: str) -> list[str]:
    # Drop front matter
    parts = markdown_text.split("---", 2)
    if markdown_text.startswith("---") and len(parts) >= 3:
        front_matter, body = parts[1], parts[2]
    else:
        front_matter, body = "", markdown_text

    title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', front_matter, re.MULTILINE)
    title = title_match.group(1) if title_match else ""

    narrative = [title] if title else []
    buf: list[str] = []
    html_depth = 0

    def flush() -> bool:
        """Flush buffered prose lines as one block. Returns False to stop."""
        text = "\n".join(buf).strip()
        buf.clear()
        if not text:
            return True
        return _process_block(text, narrative)

    for line in body.strip("\n").split("\n"):
        if html_depth > 0:
            # A standalone "//" comment line inside a <script> block can
            # legitimately mention a tag name in prose (e.g. "the Listen
            # widget's <audio> element" - a real comment generated by
            # build_watch_widget.py) without it being real markup. Skip tag
            # scanning for those lines specifically, rather than any line
            # containing "//" - a URL like "https://..." also contains "//"
            # but never at the start of a line, so this doesn't risk
            # swallowing real tag-count changes elsewhere in the script.
            if not line.strip().startswith("//"):
                for m in HTML_TAG_RE.finditer(line):
                    html_depth += -1 if m.group(1) else 1
                html_depth = max(html_depth, 0)
            continue

        if line.strip().startswith("<"):
            if not flush():
                return narrative
            for m in HTML_TAG_RE.finditer(line):
                html_depth += -1 if m.group(1) else 1
            html_depth = max(html_depth, 0)
            continue

        if line.strip() == "":
            if not flush():
                return narrative
            continue

        buf.append(line)

    flush()
    return narrative


# Sentence splitting for per-sentence synthesis (needed for real timing -
# see module docstring). General-purpose sentence tokenizers (spaCy's
# default sentencizer, NLTK's Punkt) were both tested against this blog's
# actual text and got real cases wrong (e.g. splitting "Fr. Ambroise
# Maistre" into two sentences at "Fr."), so this uses a small deterministic
# abbreviation whitelist instead - a period only ends a sentence if the
# word before it isn't a known abbreviation AND the text after it starts
# with an uppercase letter or a quote. Extend ABBREVIATIONS if a new post's
# text hits another false split.
ABBREVIATIONS = {
    "fr", "mr", "mrs", "ms", "dr", "st", "rev", "prof", "sgt", "capt", "lt", "gen", "col",
    "ave", "blvd", "rd", "no", "vs", "etc", "jr", "sr", "inc", "ltd", "co",
}


def split_sentences(text: str) -> list[str]:
    sentences = []
    start = 0
    for m in re.finditer(r"[.!?]+[\"')\]]*(?=\s|$)", text):
        end = m.end()
        after = text[end:end + 2].lstrip()
        if after and not (after[0].isupper() or after[0] in "\"'"):
            continue
        before = text[:m.start()]
        word_match = re.search(r"(\w+)$", before)
        word = word_match.group(1).lower() if word_match else ""
        if word in ABBREVIATIONS:
            continue
        sentences.append(text[start:end].strip())
        start = end
    tail = text[start:].strip()
    if tail:
        sentences.append(tail)
    return sentences


SAMPLE_RATE = 24000


def synthesize_with_timing(paragraphs: list[str], voice: str, out_path: str) -> list[dict]:
    """Synthesize each sentence separately (see split_sentences() above),
    concatenating the audio and recording each sentence's exact real
    duration as its timing - free, no separate alignment step. Writes
    <out_path>.timing.json (list of {text, offset_s, duration_s}) and
    <out_path>.srt alongside the audio. Returns the sentence list."""
    import numpy as np
    import soundfile as sf
    # Kokoro's lang_code selects the espeak-ng phonemization backend and
    # must match the voice's accent, not just be a fixed default - an
    # American lang_code on a British voice (bf_*/bm_*) mispronounces
    # accent-dependent phonemes. Voice prefixes: af/am=American,
    # bf/bm=British (the only two accents this project has used so far).
    lang_code = "b" if voice.startswith(("bf_", "bm_")) else "a"
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        from kokoro import KPipeline
        pipeline = KPipeline(lang_code=lang_code)
        pipeline.g2p.lexicon.golds.update(PRONUNCIATION_OVERRIDES)

    all_audio = []
    sentences_out: list[dict] = []
    cumulative_s = 0.0

    for para in paragraphs:
        for sent in split_sentences(para):
            if not sent:
                continue
            generator = pipeline(sent, voice=voice, split_pattern=None)
            seg_parts = []
            for result in generator:
                if result.audio is not None:
                    a = result.audio
                    seg_parts.append(a.numpy() if hasattr(a, "numpy") else a)
            if not seg_parts:
                continue
            seg_audio = np.concatenate(seg_parts)
            dur = len(seg_audio) / SAMPLE_RATE
            sentences_out.append({
                "text": sent,
                "offset_s": round(cumulative_s, 4),
                "duration_s": round(dur, 4),
            })
            all_audio.append(seg_audio)
            cumulative_s += dur

    full_audio = np.concatenate(all_audio) if all_audio else np.zeros(0, dtype=np.float32)
    sf.write(out_path, full_audio, SAMPLE_RATE)

    base = os.path.splitext(out_path)[0]
    with open(f"{base}.timing.json", "w", encoding="utf-8") as f:
        json.dump(sentences_out, f, indent=2, ensure_ascii=False)
    with open(f"{base}.srt", "w", encoding="utf-8") as f:
        f.write(_build_srt(sentences_out))

    return sentences_out


def _srt_timestamp(t: float) -> str:
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = int(t % 60)
    ms = round((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def _build_srt(sentences: list[dict]) -> str:
    blocks = []
    for i, s in enumerate(sentences, 1):
        start = _srt_timestamp(s["offset_s"])
        end = _srt_timestamp(s["offset_s"] + s["duration_s"])
        blocks.append(f"{i}\n{start} --> {end}\n{s['text']}\n")
    return "\n".join(blocks)


def scan_for_unknown_tokens(narrative: list[str], voice: str) -> list[tuple[str, list[str]]]:
    """Run the extracted narrative through misaki's G2P directly - text
    only, no audio synthesis, so this is nearly instant - and flag every
    sentence where it produces its own "unknown word/symbol" marker (a
    literal U+2753 "?" character in the phoneme output). This is the
    "unknown word or symbol" bug category from docs/pronunciation-fixes.md
    (e.g. "Ng", "Fr.", "S$" before each was fixed) - misaki has no
    lexicon entry at all for the word/symbol and falls back to spelling
    it out letter by letter, which is a real, programmatically detectable
    signal, unlike the *other* bug category (a confidently wrong existing
    entry, e.g. "stung"/"graves") where misaki's output looks like
    ordinary fluent phonemes with nothing to scan for - that category can
    only be caught by ear, this function does not attempt it.

    Returns (sentence, [unknown words]) pairs, not just the flagged
    sentence - pinpointing the exact word(s) matters, since a long
    sentence with several rare proper nouns makes "the problem is
    somewhere in here" nearly useless in practice (a real case: the
    Benjamin Sheares post flagged two ~50-word sentences with no
    indication of which word in each was the actual culprit, until
    checked by hand). Found per-token, not by re-searching the
    whole-sentence string for "?": an unknown word/proper-noun token gets
    `phonemes=None` from misaki (checked first), while an unknown symbol
    embedded inside a larger token (e.g. "S$50" tokenizes as one token
    whose `phonemes` is "?s fifty", not None) still carries a literal "?"
    inside that token's own phonemes string - both cases are checked here
    since neither alone covers both.

    Applies PRONUNCIATION_OVERRIDES first so a word already fixed there
    (e.g. "Ng") doesn't get flagged again on every future post that
    happens to use it - this mirrors exactly what synthesize_with_timing()
    does before the real synthesis run, so the scan reflects what will
    actually be produced. ABBREVIATION_EXPANSIONS is already reflected in
    `narrative`, since extract_narrative() applies it during extraction,
    before this function ever sees the text.
    """
    from misaki import en

    lang_code = "b" if voice.startswith(("bf_", "bm_")) else "a"
    g2p = en.G2P(british=(lang_code == "b"))
    g2p.lexicon.golds.update(PRONUNCIATION_OVERRIDES)

    flagged = []
    for para in narrative:
        for sent in split_sentences(para):
            if not sent:
                continue
            _, toks = g2p(sent)
            unknown_words = [
                tok.text for tok in toks
                if tok.phonemes is None or "❓" in tok.phonemes
            ]
            if unknown_words:
                flagged.append((sent, unknown_words))
    return flagged


# Initialisms confirmed, by ear, to genuinely be read as individual
# letters in real speech ("H-D-B", not a blended word) - not a guess from
# the text pattern alone, since misaki can't tell "HDB" (correct as
# letters) from "II" or "VII" (wrong - should be a number word) purely by
# looking at the token; both get the identical letter-by-letter treatment
# internally. Seeded 2026-08-27 from a survey of every post's actual
# narration text; grows reactively like the two dicts above - add an
# entry here only once Chris has confirmed it's actually meant to be
# spelled out, never speculatively. Anything letter-spelled that's NOT in
# this set gets flagged by scan_for_letter_spelled_words() below for
# review, the same way scan_for_unknown_tokens() flags a word/symbol
# misaki has no lexicon entry for at all - a different root cause, same
# "catch it before it ships instead of by ear" idea.
KNOWN_LETTER_SPELLED = {
    "BMT", "CBD", "CC", "CHIJ", "CMPB", "CPF", "EDB", "HDB", "IPPT",
    "MP", "MRT", "NS", "NTUC", "NUS", "NWC", "UK", "UN", "US",
}

_letter_phoneme_cache: dict[str, str] = {}


def _letter_phoneme(letter: str, g2p) -> str:
    """The phoneme misaki itself produces for a single letter name (e.g.
    "V" -> "vˈiː"), stress marks and whitespace stripped - the building
    block scan_for_letter_spelled_words() compares a token's actual
    phonemes against, to tell "read as its own letters spelled out"
    apart from "read as a word". Cached since every letter gets looked up
    repeatedly across a post's many multi-letter tokens."""
    if letter not in _letter_phoneme_cache:
        ps, _ = g2p(letter)
        _letter_phoneme_cache[letter] = re.sub(r"[ˈˌ\s]", "", ps)
    return _letter_phoneme_cache[letter]


def scan_for_letter_spelled_words(narrative: list[str], voice: str) -> list[tuple[str, list[str]]]:
    """Flags every ALL-CAPS token misaki reads by spelling out its own
    letters ("VII" -> "V, I, I") that isn't on the KNOWN_LETTER_SPELLED
    allowlist above - a different, broader root cause than
    scan_for_unknown_tokens(): that function catches a word/symbol
    misaki has *no* lexicon entry for at all (phonemes=None or an
    embedded "?"); this one catches a token misaki *can* phonemize,
    confidently and correctly by its own internal rule for short
    all-caps tokens, but where that rule is simply the wrong one for
    this particular token (a Roman numeral after a name, or a genuine
    acronym Singaporeans actually say as a blended word rather than
    spelling out - "MINDEF", not "M-I-N-D-E-F").

    Detected by comparison, not by guessing from capitalization alone:
    build the phoneme string spelling the token's own letters out one by
    one (via _letter_phoneme(), itself derived from misaki's own output
    for each letter - not a hand-typed table) and check whether the
    token's *actual* phonemes match that reconstruction. A token read as
    a real word instead (e.g. "NASA", "COVID") won't match and is left
    alone.

    Every match gets checked against KNOWN_LETTER_SPELLED - a token on
    that list (confirmed by ear to be genuinely correct as spelled
    letters) is not flagged; anything else is, exactly like
    scan_for_unknown_tokens()'s output. This is *not* a fully automated
    check the way the unknown-word scan is - misaki cannot know that
    "HDB" is correct as letters while "II" (in "Shock Therapy II") is
    not, since both get identical treatment internally; a human has to
    make that call once per new token, then it goes on the allowlist.
    """
    from misaki import en

    lang_code = "b" if voice.startswith(("bf_", "bm_")) else "a"
    g2p = en.G2P(british=(lang_code == "b"))
    g2p.lexicon.golds.update(PRONUNCIATION_OVERRIDES)

    flagged = []
    for para in narrative:
        for sent in split_sentences(para):
            if not sent:
                continue
            _, toks = g2p(sent)
            hits = []
            for tok in toks:
                if tok.phonemes is None or len(tok.text) < 2:
                    continue
                if not tok.text.isalpha() or not tok.text.isupper():
                    continue
                if tok.text in KNOWN_LETTER_SPELLED:
                    continue
                guess = "".join(_letter_phoneme(c, g2p) for c in tok.text)
                actual = re.sub(r"[ˈˌ\s]", "", tok.phonemes)
                if actual == guess:
                    hits.append(tok.text)
            if hits:
                flagged.append((sent, hits))
    return flagged


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("post_path")
    parser.add_argument("out_path")
    parser.add_argument("--voice", default="bm_george")
    parser.add_argument("--dry-run", action="store_true", help="print extracted text only")
    args = parser.parse_args()

    with open(args.post_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()

    narrative = extract_narrative(markdown_text)
    full_text = "\n\n".join(narrative)

    if args.dry_run:
        # sys.stdout's default encoding on Windows is the system codepage
        # (cp1252), not UTF-8 - plain print() silently mangles em-dashes and
        # other non-ASCII characters in the preview. Write UTF-8 bytes
        # directly so --dry-run actually reflects what gets synthesized.
        sys.stdout.buffer.write(full_text.encode("utf-8"))
        sys.stdout.buffer.write(b"\n")

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            flagged = scan_for_unknown_tokens(narrative, args.voice)
            letter_flagged = scan_for_letter_spelled_words(narrative, args.voice)
        # Same cp1252-vs-UTF-8 issue as the dry-run text above applies here
        # too - a flagged sentence containing an em-dash or other non-ASCII
        # character would otherwise get mangled by a plain print().
        if flagged:
            lines = [
                f"\nWARNING: {len(flagged)} sentence(s) contain a word/symbol "
                "misaki can't phonemize (would get spelled out letter by "
                "letter in the real audio) - see docs/pronunciation-fixes.md:"
            ]
            lines += [
                f"  - {', '.join(repr(w) for w in words)} in: {sent}"
                for sent, words in flagged
            ]
        else:
            lines = [
                "\nNo unknown words/symbols found (misaki's own scan) - "
                "this doesn't rule out a wrong-but-confident mispronunciation "
                "(e.g. \"stung\"/\"graves\"), only the letter-spelling kind. "
                "Still worth a listen after synthesis."
            ]
        if letter_flagged:
            lines += [
                f"\nWARNING: {len(letter_flagged)} sentence(s) contain a "
                "word spelled out letter-by-letter that's NOT on the "
                "KNOWN_LETTER_SPELLED allowlist - confirm by ear whether "
                "each is actually correct as spelled (like \"HDB\") or "
                "wrong (like \"II\"/\"VII\", which should be a number "
                "word) - see docs/pronunciation-fixes.md:"
            ]
            lines += [
                f"  - {', '.join(repr(w) for w in words)} in: {sent}"
                for sent, words in letter_flagged
            ]
        else:
            lines += [
                "\nNo unreviewed letter-spelled words found (every "
                "ALL-CAPS token read as its own letters is already on the "
                "KNOWN_LETTER_SPELLED allowlist)."
            ]
        sys.stderr.buffer.write(("\n".join(lines) + "\n").encode("utf-8"))
        return

    print(f"Extracted {len(full_text)} characters, {len(narrative)} paragraphs.", file=sys.stderr)
    sentences = synthesize_with_timing(narrative, args.voice, args.out_path)
    base = os.path.splitext(args.out_path)[0]
    print(f"Wrote {args.out_path}, {base}.timing.json, {base}.srt ({len(sentences)} sentences)", file=sys.stderr)


if __name__ == "__main__":
    main()
