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
        sys.stderr.buffer.write(("\n".join(lines) + "\n").encode("utf-8"))
        return

    print(f"Extracted {len(full_text)} characters, {len(narrative)} paragraphs.", file=sys.stderr)
    sentences = synthesize_with_timing(narrative, args.voice, args.out_path)
    base = os.path.splitext(args.out_path)[0]
    print(f"Wrote {args.out_path}, {base}.timing.json, {base}.srt ({len(sentences)} sentences)", file=sys.stderr)


if __name__ == "__main__":
    main()
