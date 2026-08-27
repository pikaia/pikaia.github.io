# Narration pronunciation fixes

Kokoro TTS (via the `misaki` phonemizer) occasionally mispronounces a
specific word — not from anything in our post text or scripts, but
from a bug in misaki's own built-in lexicon. Every confirmed case gets
fixed in
[`scripts/generate_narration.py`](../scripts/generate_narration.py),
in one of two dicts near the top of the file — **this doc is a
human-readable summary of what's there, not a separate source of
truth.** If you're adding a new entry, add it to the code first, then
mirror it here; the two are duplicated by design (same pattern as the
route-walk animation data in `CLAUDE.md`), not auto-generated from
each other.

## Three root causes, two fix mechanisms — not the same axis

These are independent choices, not a 1:1 mapping — "Ng" and "Fr."
share the same root cause but ended up with different fixes, because
the fix follows the *shape* of the problem, not just its origin.

**Root causes seen so far:**

1. **Unknown word or symbol** — misaki's lexicon has no entry at all,
   and it falls back to spelling the word out letter by letter (an
   internal `❓` marker becomes audible letter-by-letter speech), or
   drops a symbol as an audible `❓` on its own. Happens with
   foreign/rare proper nouns ("Ng"), abbreviated titles ("Fr."), and
   currency notation misaki can't parse ("S$", the "$" producing a
   literal `❓` right after "S") alike.
2. **Wrong entry / homograph collision** — misaki *does* have an
   entry, but it's confidently wrong: the phonemes it produces belong
   to a different word or reading entirely. "stung" gets "strung"'s
   phonemes; "graves" (plural, burial sites) gets what looks like the
   Bordeaux wine region's French pronunciation instead of the ordinary
   English plural. These are harder to catch than unknown-word
   failures, since the output sounds like a real (wrong) word rather
   than obviously broken speech — only caught by ear, not by any
   automated signal.
3. **Correct entry, wrong number-reading convention** — misaki *can*
   pronounce the numeral fine, but defaults to the wrong reading for
   context. A bare day-of-month numeral ("25 August") gets read as a
   cardinal ("twenty-five August"), but spoken English always reads
   the day-of-month as an ordinal regardless of how it's written ("the
   twenty-fifth of August") — the year, by contrast, stays cardinal
   ("nineteen sixty-three," never "the one thousand nine hundred
   sixty-third"). Misaki can't tell from a bare numeral alone which
   convention applies; nothing is missing or mispronounced in
   isolation, so like the wrong-entry category this is only caught by
   ear (or, here, by deliberately reading a rendered date aloud against
   how a person would actually say it).

**Fix mechanisms available:**

- **`PRONUNCIATION_OVERRIDES`** — patches misaki's `lexicon.golds`
  dict with a phoneme string directly. The default choice: works for
  both root causes above, and is required for anything with no natural
  full-word text substitute (a name, or a wrong-entry case like
  "stung"/"graves" where the *word itself* is already correct, only
  its pronunciation is wrong).
- **`ABBREVIATION_EXPANSIONS`** — substitutes the narration *text*
  itself before synthesis, for an unknown-word/symbol case that has an
  unambiguous natural-language equivalent (e.g. "Fr." → "Father", "S$"
  → reordering the amount and appending "Singapore dollars"). Required
  whenever the fix needs to *reorder* or restructure the surrounding
  words, not just swap in different phonemes for one token — a
  phoneme override can't move "million"/"billion" to a different
  position in the sentence. Also the right choice when a phoneme
  override alone would still leave an audible artifact: "Fr." tested
  with a phoneme override still left an audible pause from the
  abbreviation's literal period; text substitution removes the period
  entirely instead of working around it.

Both dicts are meant to grow **reactively** — one confirmed
mispronunciation at a time, verified by ear against a real render (or
a quick standalone synthesis test), never added speculatively. Several
common abbreviations (`St.`, `No.`, etc.) are deliberately *not*
pre-expanded, since they're ambiguous out of context and a wrong guess
would sound worse than the gap it "fixes" — see the comment above
`ABBREVIATION_EXPANSIONS` in the code.

## What these fixes touch, and what they don't

`ABBREVIATION_EXPANSIONS` (and `PRONUNCIATION_OVERRIDES`) only ever
apply inside the narration pipeline's own extraction step
(`extract_narrative()` in `generate_narration.py`) — they never modify
the post file on disk. That extraction step feeds two downstream
outputs which therefore both carry the substituted text, and one
completely separate script which doesn't:

- **The written post** (`_posts/*.md`) is never touched. It still
  reads "25 August 1963" and "S$50 million" exactly as written — the
  substitution exists only in the pipeline's in-memory copy of the
  text, used solely for synthesis.
- **The narration audio** speaks the substituted text, by definition —
  that's the entire point of these fixes.
- **The subtitles** (`<slug>.srt`, and the burned-in video captions
  rendered from it) also carry the substituted text, and this is
  deliberate, not a side effect: `synthesize_with_timing()` records
  each sentence's *already-substituted* string as both what Kokoro
  speaks and what `_build_srt()` writes to the `.srt` file, from the
  same `sentences_out` list — see the loop around `sentences_out.append(...)`
  in `generate_narration.py`. Captions are supposed to match the audio
  word-for-word; a caption reading "25 August" under audio saying "the
  twenty-fifth of August" would look like a captioning bug, not a
  stylistic choice.
- **The YouTube title/description** (`docs/youtube_helper/<slug>-youtube.txt`,
  staged by `scripts/stage_youtube_text.py`) are generated by a
  completely different code path that reads the post's front-matter
  `title` and its own first paragraph straight from the markdown file
  (`extract_hook()` / `clean_text()` in that script) — neither
  `ABBREVIATION_EXPANSIONS` nor `PRONUNCIATION_OVERRIDES` is in that
  script's import list, so nothing staged for YouTube is ever
  substituted. If a date or "S$" amount ever appears in a post's title
  or opening paragraph, it will show up there exactly as written.

## Automated scan for the "unknown word or symbol" category

`scan_for_unknown_tokens()` in `generate_narration.py` runs automatically
as part of `--dry-run` (section 1.1 of `docs/production-pipeline.md`) —
it phonemizes every sentence via misaki directly (text only, no audio,
near-instant) and flags any that contain a literal `❓` token, printing
each flagged sentence so you know exactly where to look. This closes off
the *entire* "unknown word or symbol" root cause automatically, on every
post, for free — no more waiting to catch it by ear.

It found 4 real cases in one pass on the four-chopsticks post ("Kuan" as
in "Lee Kuan Yew", "Yasukuni", "rallied", "Siglap" — see the table below)
that would otherwise have needed 4 separate listen-catch-fix-redo cycles.
"Kuan" in particular is worth noting: since Lee Kuan Yew is mentioned
across many posts on this blog, this fix likely improves narration on
posts far beyond the one that surfaced it, not just this one.

It does **not** catch the "wrong entry / homograph collision" category
(stung, graves) or the "wrong number-reading convention" category (DD
Month dates) — both produce fluent, confident, and wrong output with no
distinguishing signal to scan for. Those categories still need a human
ear.

## Confirmed fixes

| Word/phrase | Root cause | What misaki produces | Fix | Mechanism | Caught on |
|---|---|---|---|---|---|
| "Ng" (surname) | Unknown word | Spelled out letter by letter ("N, G") — no lexicon entry | `əŋ` (anglicized "ung", schwa + ng) | `PRONUNCIATION_OVERRIDES` | the-fishball-noodle-that-exposed-singapores-hawker-rent-gap |
| "Fr." (title) | Unknown word | Spelled out letter by letter ("F, R") — no lexicon entry | Text expanded to "Father" before synthesis | `ABBREVIATION_EXPANSIONS` | jalan-payoh-lai-kangkar-montfort-nativity-church (real name: Fr. Ambroise Maistre) |
| "stung" | Wrong entry / homograph collision | `stɹˈʌŋ` — identical to "strung", an extra "r" sound baked in | `stˈʌŋ` | `PRONUNCIATION_OVERRIDES` | the-fishball-noodle-that-exposed-singapores-hawker-rent-gap |
| "graves" (plural) | Wrong entry / homograph collision | `ɡɹˈɑːv` — wrong vowel *and* drops the plural entirely, sounds like "grahv" (every other `-aves` word — caves, waves, saves, staves, braves, shaves — phonemizes correctly; likely a lexicon entry misfiled to the Bordeaux wine region's French pronunciation) | `ɡɹˈAvz` | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan |
| "S$" (Singapore dollar notation, e.g. "S$50 million") | Unknown symbol | "S" + a literal `❓` for the "$" ("S, [garbled], fifty million") | Reordered to "\<amount\> \<million/billion/thousand\> Singapore dollars" ("S$50 million" → "50 million Singapore dollars"). Tried "SGD" first — spells out as individual letters ("S, G, D"), not "Sing Dollar" as hoped, confirmed by testing directly | `ABBREVIATION_EXPANSIONS` | four-chopsticks-blood-debt-singapore-japan |
| "Kuan" (as in "Lee Kuan Yew") | Unknown word | Spelled out letter by letter — no lexicon entry | `kwˈɑːn` | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`, not by ear — likely affects other posts mentioning Lee Kuan Yew too) |
| "Yasukuni" (the Tokyo shrine) | Unknown word | Spelled out letter by letter — no lexicon entry | `jˌasuːkˈuːni` (anglicized 4-syllable approximation) | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`) |
| "rallied" | Unknown word | Spelled out letter by letter — no lexicon entry, even though the root "rally" phonemizes fine on its own | `ɹˈalɪd` (rally's root + the regular "-ied" ending pattern from "carried"/"hurried"/"married") | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`) |
| "Siglap" (the Singapore neighbourhood) | Unknown word | Spelled out letter by letter — no lexicon entry | `sˈɪɡlap` (built from "signal"'s "sig-" onset + "lap") | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`) |
| "DD Month" dates (e.g. "25 August 1963") | Correct entry, wrong number-reading convention | Day numeral read as cardinal ("twenty-five August") instead of the ordinal spoken English always uses for a day-of-month ("the twenty-fifth of August") | Text expanded to "the \<day\>\<ordinal suffix\> of \<Month\>" before synthesis (suffix computed per day: 1st/2nd/3rd/4th…11th-13th always "th") | `ABBREVIATION_EXPANSIONS` | four-chopsticks-blood-debt-singapore-japan (caught by ear, not by `scan_for_unknown_tokens()` — nothing is unknown or wrong in isolation, only in spoken-date context; likely affects most other posts too, since "DD Month YYYY" is the house style for dates in prose) |

**How to verify a new candidate fix** before adding it: test directly
against misaki, no post/pipeline involvement needed —

```python
from misaki import en
g2p = en.G2P(british=True)  # bm_george is a British voice
ps, toks = g2p("your test sentence here")
print(ps)
```

First figure out which root cause you're looking at — does the word
come back as a `❓`/spelled-out mess (unknown word), or as fluent but
wrong-sounding phonemes (wrong entry)? That determines which fix
mechanism fits. For a wrong-entry case, compare the output for the
suspect word against a similar word you know phonemizes correctly
(e.g. "stung" vs. "sung"/"flung"; "graves" vs. "caves"/"waves") to spot
the exact difference before picking a fix. Once you have a candidate
phoneme string, apply it via `g2p.lexicon.golds["word"] = "..."` and
re-run the same test to confirm it's fixed *before* touching
`generate_narration.py`.
