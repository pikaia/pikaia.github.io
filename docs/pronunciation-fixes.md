# Narration pronunciation fixes

Kokoro TTS (via the `misaki` phonemizer) occasionally mispronounces a
specific word — not from anything in our post text or scripts, but
from a bug in misaki's own built-in lexicon. Every confirmed case gets
fixed in
[`scripts/generate_narration.py`](../scripts/generate_narration.py),
in one of two dicts plus one allowlist set near the top of the file —
**this doc is a human-readable summary of what's there, not a
separate source of truth.** If you're adding a new entry, add it to
the code first, then mirror it here; the two are duplicated by design
(same pattern as the route-walk animation data in `CLAUDE.md`), not
auto-generated from each other.

## Four root causes, two fix mechanisms — not the same axis

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
4. **Letter-spelling fallback applied to the wrong token** — misaki
   has a real, deliberate internal rule for a short ALL-CAPS token: spell
   it out as its own letters ("H-D-B"). That rule is *correct* for a
   genuine initialism ("HDB," "CPF," "MRT") but wrong whenever the
   token isn't actually meant to be read as letters — a Roman numeral
   after a name ("King Edward VII" → "V, I, I" instead of "the
   Seventh"; "Shock Therapy II" → "I, I" instead of "Two"), or an
   acronym Singaporeans actually say as a blended word rather than
   spelling out ("MINDEF" → "M-I-N-D-E-F" instead of "min-def"; "FOFO"
   → "F-O-F-O" instead of "foh-foh"). Unlike categories 1-3, this one
   *is* programmatically detectable — see `scan_for_letter_spelled_words()`
   below — but not fully automatically fixable: misaki has no way to
   know that "HDB" is correct as letters while "VII" is not, since both
   get identical internal treatment, so a human has to judge each new
   case once before it goes on the allowlist.
5. **Correct phonemes, wrong acoustic rendering** — the phonemizer is
   right (verified: `KPipeline(lang_code="b").g2p(...)` returns the
   intended reading), but the Kokoro *voice model* realises those
   phonemes wrong anyway, and the error shifts with the surrounding
   sentence. Seen once, on the amah post: "live-in workers" — the g2p
   hands `bm_george` the adjective reading `lˈIvˌɪn` (/laɪv/, the same
   token it uses in "live music" / "drive-in"), but the model collapses
   the `/aɪ/` to the verb's short vowel in that sentence's context.
   Because the phoneme string is already correct, a
   `PRONUNCIATION_OVERRIDES` entry to the *same* phonemes does nothing,
   and every alternate spelling tried (`lˈIvɪn`, `lˈIv ˌɪn`,
   `lˈaɪ.vɪn`, `lˈIv-ɪn`, …) still came out wrong. Only caught by ear.

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
- **Reword the post itself** — the only fix for root cause 5 (correct
  phonemes, wrong acoustic rendering), and a clean, scalable dodge
  whenever a word fights the voice model and no phoneme spelling wins.
  Swap the offending word for a synonym that carries the same meaning
  and phonemizes cleanly — "live-in workers" → "resident domestic
  workers" on the amah post. This edits the post file on disk (unlike
  the two dicts above), so it's a real content change; if it's an
  invisible meaning-preserving swap, `last_modified_at` doesn't need
  bumping. Confirmed as the preferred move by Chris (2026-08-28):
  "avoiding the use is a clean scalable way to dodge this."

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
near-instant) and flags any sentence containing an unknown word/symbol.
This closes off the *entire* "unknown word or symbol" root cause
automatically, on every post, for free — no more waiting to catch it by
ear.

**The warning names the exact word(s), not just the sentence.** Earlier
versions only flagged the whole sentence, which turned out to be nearly
useless on a long sentence with several rare proper nouns in it (a real
case: the Benjamin Sheares post flagged two ~50-word sentences with no
indication of which word in each was the actual culprit — Chris had to
ask before it got tracked down by hand). The function now walks misaki's
per-token output directly: an unknown word/proper noun gets
`phonemes=None` from misaki, while an unknown symbol embedded inside a
larger token (e.g. "S$50" tokenizes as one token whose `phonemes` is
`"?s fifty"`, not `None`) still carries a literal `❓` inside that
token's own phonemes string — both cases are checked, since neither
alone covers both, and the flagged word(s) are printed right next to
the sentence they're in.

It found 4 real cases in one pass on the four-chopsticks post ("Kuan" as
in "Lee Kuan Yew", "Yasukuni", "rallied", "Siglap" — see the table below)
that would otherwise have needed 4 separate listen-catch-fix-redo cycles.
"Kuan" in particular is worth noting: since Lee Kuan Yew is mentioned
across many posts on this blog, this fix likely improves narration on
posts far beyond the one that surfaced it, not just this one.

It does **not** catch the "wrong entry / homograph collision" category
(stung, graves), the "wrong number-reading convention" category (DD
Month dates), or the "letter-spelling fallback applied to the wrong
token" category (VII, MINDEF) — all three produce fluent, confident, and
wrong output with no distinguishing signal to scan for. The first two
still need a human ear; the third has its own separate scan, next.

## Automated scan for the "letter-spelling fallback" category

`scan_for_letter_spelled_words()` runs alongside
`scan_for_unknown_tokens()` in the same `--dry-run` step. It flags every
ALL-CAPS token misaki reads by spelling out its own letters that isn't
already on the `KNOWN_LETTER_SPELLED` allowlist — detected by
comparison, not by guessing from capitalization alone: it builds the
phoneme string spelling a token's own letters out one by one (from
misaki's own single-letter phonemizations, not a hand-typed table) and
checks whether the token's *actual* phonemes match that reconstruction.
A token read as a real word instead (e.g. "NASA," "COVID") won't match
and is left alone.

**This scan is not fully automatic the way the unknown-word one is.**
Misaki treats "HDB" (correct as spelled letters) and "VII" (wrong -
should be "the Seventh") identically internally, so the scan can only
flag "this token gets spelled out" — a human has to judge, once per new
token, whether that's actually correct. `KNOWN_LETTER_SPELLED` holds
every token confirmed correct so far; anything letter-spelled that's
*not* on that list gets printed for review on every future `--dry-run`,
the same format as the unknown-word warning. Seeded 2026-08-27 from a
survey of every already-published post's real narration text.

It found real problems immediately on two already-published posts
in one pass: "Shock Therapy II" (read as "I, I" instead of "Two," on
the Lim Chong Yah post) and "MINDEF"/"FOFO" (read as individual
letters instead of the blended words Singaporeans actually say, on
the National Service post) — plus, while checking that same National
Service post, a separate and much larger batch of place names (Pasir
Laba, Pulau Tekong, Bukit Gombak, and more) that `scan_for_unknown_tokens()`
had already been flagging as unknown words all along, unrelated to this
new scan, just never chased down until this pass went looking.

## Confirmed fixes

| Word/phrase | Root cause | What misaki produces | Fix | Mechanism | Caught on |
|---|---|---|---|---|---|
| "Ng" (surname) | Unknown word | Spelled out letter by letter ("N, G") — no lexicon entry | `əŋ` (anglicized "ung", schwa + ng) | `PRONUNCIATION_OVERRIDES` | the-fishball-noodle-that-exposed-singapores-hawker-rent-gap |
| "Fr." (title) | Unknown word | Spelled out letter by letter ("F, R") — no lexicon entry | Text expanded to "Father" before synthesis | `ABBREVIATION_EXPANSIONS` | jalan-payoh-lai-kangkar-montfort-nativity-church (real name: Fr. Ambroise Maistre) |
| "stung" | Wrong entry / homograph collision | `stɹˈʌŋ` — identical to "strung", an extra "r" sound baked in | `stˈʌŋ` | `PRONUNCIATION_OVERRIDES` | the-fishball-noodle-that-exposed-singapores-hawker-rent-gap |
| "graves" (plural) | Wrong entry / homograph collision | `ɡɹˈɑːv` — wrong vowel *and* drops the plural entirely, sounds like "grahv" (every other `-aves` word — caves, waves, saves, staves, braves, shaves — phonemizes correctly; likely a lexicon entry misfiled to the Bordeaux wine region's French pronunciation) | `ɡɹˈAvz` | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan |
| "S$" (Singapore dollar notation, e.g. "S$50 million") | Unknown symbol | "S" + a literal `❓` for the "$" ("S, [garbled], fifty million") | Reordered to "\<amount\> \<million/billion/thousand\> Singapore dollars" ("S$50 million" → "50 million Singapore dollars"). Tried "SGD" first — spells out as individual letters ("S, G, D"), not "Sing Dollar" as hoped, confirmed by testing directly. The amount pattern requires proper thousands grouping (`\d+(?:,\d{3})*`), not a loose `[\d,]*` — otherwise "S$1,000, and …" swallowed the trailing comma and rendered "1,000, Singapore dollars and …" (fine-city post) | `ABBREVIATION_EXPANSIONS` | four-chopsticks-blood-debt-singapore-japan (comma fix: fine-city-fine-print) |
| "M$" (Malayan dollar notation, e.g. "M$20 million") | Unknown symbol | Same as S$ — "M" + a literal `❓` for the "$" | Same fix as S$, → "\<amount\> \<unit\> Malayan dollars" (the pre-1967 currency; officially the Malaya and British Borneo dollar, universally shortened to "Malayan dollar") | `ABBREVIATION_EXPANSIONS` | christmas-island-singapore-never-owned |
| "ex-gratia" | Wrong entry / homograph collision (sort of) | misaki keeps "ex-gratia" as one token and can't phonemize the "-gratia" half (`ˈɛks❓`) | `ˌɛksɡɹˈAʃə` ("eks-GRAY-shuh", the standard anglicized legal reading) | `PRONUNCIATION_OVERRIDES` | christmas-island-singapore-never-owned |
| "Abdul" / "Hamid" / "Jumat" (Abdul Hamid Jumat, Acting CM 1958) | Unknown word | All spelled out letter by letter | `ˈabdʊl` / `hɑːmˈiːd` / `dʒʊmˈat` ("AB-dool hah-MEED joo-MAT") | `PRONUNCIATION_OVERRIDES` | christmas-island-singapore-never-owned |
| "Kuan" (as in "Lee Kuan Yew") | Unknown word | Spelled out letter by letter — no lexicon entry | `kwˈɑːn` | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`, not by ear — likely affects other posts mentioning Lee Kuan Yew too) |
| "Yasukuni" (the Tokyo shrine) | Unknown word | Spelled out letter by letter — no lexicon entry | `jˌasuːkˈuːni` (anglicized 4-syllable approximation) | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`) |
| "rallied" | Unknown word | Spelled out letter by letter — no lexicon entry, even though the root "rally" phonemizes fine on its own | `ɹˈalɪd` (rally's root + the regular "-ied" ending pattern from "carried"/"hurried"/"married") | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`) |
| "Siglap" (the Singapore neighbourhood) | Unknown word | Spelled out letter by letter — no lexicon entry | `sˈɪɡlap` (built from "signal"'s "sig-" onset + "lap") | `PRONUNCIATION_OVERRIDES` | four-chopsticks-blood-debt-singapore-japan (caught by `scan_for_unknown_tokens()`) |
| "DD Month" dates (e.g. "25 August 1963") | Correct entry, wrong number-reading convention | Day numeral read as cardinal ("twenty-five August") instead of the ordinal spoken English always uses for a day-of-month ("the twenty-fifth of August") | Text expanded to "the \<day\>\<ordinal suffix\> of \<Month\>" before synthesis (suffix computed per day: 1st/2nd/3rd/4th…11th-13th always "th") | `ABBREVIATION_EXPANSIONS` | four-chopsticks-blood-debt-singapore-japan (caught by ear, not by `scan_for_unknown_tokens()` — nothing is unknown or wrong in isolation, only in spoken-date context; likely affects most other posts too, since "DD Month YYYY" is the house style for dates in prose) |
| "tapped" | Unknown word | Spelled out letter by letter — no lexicon entry, surprising for such a common verb; "mapped" has the same gap, while "trapped"/"wrapped"/"snapped"/"clapped"/"napped" all phonemize fine | `tˈapt` (direct analogy with those working "-apped" words) | `PRONUNCIATION_OVERRIDES` | benjamin-sheares-doctor-behind-the-baby-bust (caught by `scan_for_unknown_tokens()`) |
| "Istana" (the President's official residence) | Unknown word | Spelled out letter by letter — no lexicon entry | `ɪstˈɑːnə` (anglicized, stress on the middle syllable, echoing "banana"/"veranda"'s "-ana" ending) | `PRONUNCIATION_OVERRIDES` | benjamin-sheares-doctor-behind-the-baby-bust (caught by `scan_for_unknown_tokens()` — likely affects other posts mentioning the Istana too) |
| "Kandang" (half of "Kandang Kerbau", the historical district/hospital) | Unknown word | Spelled out letter by letter — no lexicon entry | `kˈandaŋ` ("Kan-" from "Kandy"'s working phonemization, "-dang" from "hang"/"gang"'s "-ang" ending) | `PRONUNCIATION_OVERRIDES` | benjamin-sheares-doctor-behind-the-baby-bust (caught by `scan_for_unknown_tokens()`) |
| "Kerbau" (the other half of "Kandang Kerbau") | Unknown word | Spelled out letter by letter — no lexicon entry | `kəbˈaʊ` ("Ker-" as a schwa, "-bau" from "how"/"now"'s "aʊ" diphthong) | `PRONUNCIATION_OVERRIDES` | benjamin-sheares-doctor-behind-the-baby-bust (caught by `scan_for_unknown_tokens()`) |
| "King Edward VII" (the college of medicine) | Letter-spelling fallback applied to the wrong token | The Roman numeral read as individual letters ("V, I, I") instead of the ordinal a regnal number is actually read as ("the Seventh") | Text expanded to "King Edward the Seventh" (literal phrase match, not a general Roman-numeral rule — context-dependent, e.g. "World War II" stays "World War Two") | `ABBREVIATION_EXPANSIONS` | benjamin-sheares-doctor-behind-the-baby-bust (caught by ear, before `scan_for_letter_spelled_words()` existed) |
| "Shock Therapy II" (the 1979 wage policy's nickname) | Letter-spelling fallback applied to the wrong token | The Roman numeral read as individual letters ("I, I") instead of the cardinal a sequel/program name is actually read as ("Two") | Text expanded to "Shock Therapy Two" (literal phrase match, same reasoning as "King Edward VII" but the other reading direction) | `ABBREVIATION_EXPANSIONS` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_letter_spelled_words()`) |
| "MINDEF" (Ministry of Defence) | Letter-spelling fallback applied to the wrong token | Read as individual letters ("M-I-N-D-E-F") instead of the blended word Singaporeans actually say ("min-def") | `mˈɪndɛf` ("min" + "def", stress on the first syllable) | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong (caught by `scan_for_letter_spelled_words()`, confirmed by Chris by ear) |
| "FOFO" (a training-hill nickname) | Letter-spelling fallback applied to the wrong token | Read as individual letters ("F-O-F-O") instead of the blended word Singaporeans actually say ("foh-foh") | `fˈQfQ` ("foe" doubled, matching "logo"'s stress pattern) | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong (caught by `scan_for_letter_spelled_words()`, confirmed by Chris by ear) |
| "Lim" (a common Chinese surname) | Unknown word | Spelled out letter by letter — no lexicon entry, even though "Tim"/"Jim"/"dim" all phonemize fine | `lˈɪm` (direct analogy with those) | `PRONUNCIATION_OVERRIDES` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_unknown_tokens()` — likely affects other posts mentioning a "Lim," e.g. Lim Kim San) |
| "Chong" | Unknown word | Spelled out letter by letter — no lexicon entry | `ʧˈɒŋ` ("check"'s "ʧ" onset + "song"/"long"/"wrong"'s "-ong" ending) | `PRONUNCIATION_OVERRIDES` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_unknown_tokens()`) |
| "Hainanese" | Unknown word | Spelled out letter by letter — no lexicon entry, even though "Hainan" alone phonemizes fine | `hˌInənˈiːz` (same stress-shift pattern as "Chinese"/"Japanese"/"Cantonese") | `PRONUNCIATION_OVERRIDES` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_unknown_tokens()`) |
| "Siow" (a Chinese surname) | Unknown word | Spelled out letter by letter — no lexicon entry | `sˈW` (analogy with "how"/"now"/"cow" — not verified by ear yet, flag if it sounds off) | `PRONUNCIATION_OVERRIDES` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_unknown_tokens()`) |
| "Nanyang" (Nanyang Technological University) | Unknown word | Spelled out letter by letter — no lexicon entry | `nˌanjˈaŋ` ("Nan" + "yang," as in yin-yang) | `PRONUNCIATION_OVERRIDES` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_unknown_tokens()`) |
| "paycheck"/"paychecks" | Unknown word | Spelled out letter by letter — no lexicon entry, surprising since "pay" and "check(s)" both phonemize fine on their own; "daycare" has the same gap | `pˈAʧɛk` / `pˈAʧɛks` (built from the working parts) | `PRONUNCIATION_OVERRIDES` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_unknown_tokens()`) |
| "Winsemius" (Albert Winsemius, the Dutch economist) | Unknown word | Spelled out letter by letter — no lexicon entry | `wɪnsˈiːmiəs` ("win" + "seem" + "-ius" from "genius"/"radius" — not verified by ear yet) | `PRONUNCIATION_OVERRIDES` | lim-chong-yah-textbook-national-wages-council-shock-therapy (caught by `scan_for_unknown_tokens()` — likely affects other posts about Singapore's early economic development) |
| "Kang" (part of "Peng Kang Hill") | Unknown word | Spelled out letter by letter — no lexicon entry | `kˈʌŋ` — confirmed by ear: rhymes with "hung"/"sung," not the "hang"/"gang" vowel the spelling suggests | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Goh"/"Keng"/"Swee" (Dr Goh Keng Swee, architect of Jurong's industrialization) | Unknown word | Spelled out letter by letter — no lexicon entry | `ɡˈQ` / `kˈAŋ` / `swˈiː` — "Keng" first guessed with the "bed"/"ten" vowel, corrected by ear to the "cane"/"lane" vowel instead | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong (likely affects other posts about Singapore's economic development, same as "Winsemius") |
| "Pulau" (island) | Unknown word | Spelled out letter by letter — no lexicon entry | `pˈuːlaʊ` — confirmed by ear, matches Wiktionary IPA /ˈpulaw/ | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong (common across many Singapore-history posts, not specific to this one) |
| "Tekong" (the island) | Unknown word | Spelled out letter by letter — no lexicon entry, no Wiktionary entry either (Singapore-specific place name) | `təkˈɒŋ` — confirmed by ear: "tuh-KONG," stress on the second syllable | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Jurong" | Unknown word | Spelled out letter by letter — no lexicon entry | `ʤˈuːrɒŋ` — matches Wiktionary IPA /dʒuːrɒŋ/; first guess used the "tour"/"poor" diphthong instead of a plain long "oo," corrected once checked | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Taman" (Malay for "garden/park," as in Taman Jurong) | Unknown word | Spelled out letter by letter — no lexicon entry | `tˈaman` — first guess wrongly reduced the second syllable to a schwa (an English habit; Malay keeps fuller unstressed vowels), corrected by ear | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Bukit"/"Gombak" (Malay for "hill"; Bukit Gombak) | Unknown word | Spelled out letter by letter — no lexicon entry | `bˈuːkɪt` / `ɡˈɒmbak` — confirmed by ear | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Pasir" (Malay for "sand"; Pasir Laba, Pasir Ris) | Unknown word | Spelled out letter by letter — no lexicon entry | `pˈɑːsA` ("PAH-say") — two earlier attempts (a rhotic "-sir" ending, then a non-rhotic "-sia" ending) were both wrong; corrected by ear to the actual local reading | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong (common across many Singapore place names — Pasir Ris, Pasir Panjang) |
| "Laba" (Pasir Laba) | Unknown word | Spelled out letter by letter — no lexicon entry | `lˈɑːbˌɑː` ("LAH-bah") — first guess reduced the second syllable to a schwa, same mistake as "Taman," corrected by ear | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Besar"/"Kechil" (Malay for "big"/"small"; Tekong Besar, Tekong Kechil) | Unknown word | Spelled out letter by letter — no lexicon entry | `bəsˈɑː` / `kətʃˈiːl` — confirmed by ear | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Ris" (Pasir Ris) | Unknown word | Spelled out letter by letter — no lexicon entry | `ɹˈɪs` (rhymes with "miss"/"kiss") — not actually on this post, caught and fixed pre-emptively while verifying "Pasir" | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "Selabin"/"Permatang"/"Sanyongkong" (former kampong names on Pulau Tekong, now training-area names) | Unknown word | Spelled out letter by letter — no lexicon entry | `sˌɜːlˈɑːbɪn` / `pˌəmˌɑːtˈɑːŋ` / `sˌɑːnjˌɒŋkˈɒŋ` — confirmed by ear. "Sanyongkong" was a Chinese settlement (rubber-plantation era), not Malay like the other two, per Wikipedia — likely why it doesn't follow standard Malay phonetics | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "tri-service" | Unknown word | Spelled out letter by letter — no lexicon entry, even though "tri-" and "service" both phonemize fine separately | `trˌIsˈɜːvɪs` | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "outgrown" | Unknown word | Spelled out letter by letter — no lexicon entry, even though "out" and "grown" both phonemize fine separately; same gap pattern as "paycheck"/"daycare" | `ˌWtɡɹˈQn` | `PRONUNCIATION_OVERRIDES` | national-service-cmpb-safti-peng-kang-hill-tekong |
| "portering" | Unknown word | Spelled out letter by letter — no lexicon entry, even though "porter" phonemizes fine on its own | `pˈɔːtəɹɪŋ` ("porter" + the regular "-ering" pattern from "catering"/"watering", restoring the linking "r") | `PRONUNCIATION_OVERRIDES` | a-typical-day-for-singapores-silver-generation |
| "majie" | Unknown word | Spelled out letter by letter — no lexicon entry (妈姐/媽姐, Cantonese domestic-servant term) | `mˈɑːʤɛ` ("MAH-jeh": "ma" + "jie" as Cantonese "jeh" `ʤɛ`, per the variant spelling "mahjeh" — not Mandarin-pinyin "jiě". Confirmed by Chris) | `PRONUNCIATION_OVERRIDES` | from-amah-to-auntie-rise-of-domestic-workers |
| "Jetstar" | Unknown word | Spelled out letter by letter — no lexicon entry, even though "jet" and "star" phonemize fine separately (same compound gap as "paycheck"/"outgrown") | `ʤˈɛtstɑː` | `PRONUNCIATION_OVERRIDES` | the-travel-bug-rise-of-travelling-among-singaporeans |
| "phrasebook" | Unknown word | Spelled out letter by letter — no lexicon entry, even though "phrase" and "book" phonemize fine separately | `fɹˈAzbʊk` | `PRONUNCIATION_OVERRIDES` | the-travel-bug-rise-of-travelling-among-singaporeans |
| "Changi" | Unknown word | Spelled out letter by letter — no lexicon entry (the airport/district; recurs across many posts) | `ʧɑːŋˈiː` ("chah-NGEE": "ch" + "ah" + "-ngee" with the /ŋ/ of "singer", not a hard /ndʒ/; stress on the second syllable, long "ee"). Confirmed by Chris by ear from three synthesized samples — first-syllable-stress `ʧˈɑːŋi` was the runner-up | `PRONUNCIATION_OVERRIDES` | the-travel-bug-rise-of-travelling-among-singaporeans |
| "2020–2021" (any 4-digit year range, en-dash or hyphen) | Unknown symbol | The dash drops as an audible "?" and the two years mush together ("twenty twenty? twenty twenty one") | Text-substituted to "2020 to 2021" (each year then read as the usual cardinal); regex `\b(\d{4})[–-](\d{4})\b` → `\1 to \2` | `ABBREVIATION_EXPANSIONS` | the-travel-bug-rise-of-travelling-among-singaporeans |
| "vs." | Unknown symbol | The abbreviation drops as a literal "?" ("Say vs. What" → "Say ? What") | Text-substituted to "versus" (always the reading, in sport / law / comparisons alike). Also now applied to the **post title**, which bypasses `_process_block()` — a title-level abbreviation was previously never expanded | `ABBREVIATION_EXPANSIONS` | the-ageism-gap-singapore-employers (in the title itself) |
| "topline" | Unknown word | Spelled out letter by letter — no lexicon entry, though "top" and "line" phonemize fine alone (same compound gap as "phrasebook"/"outgrown") | `tˈɒplIn` ("TOP-line", first-syllable stress, "line" as /laɪn/) | `PRONUNCIATION_OVERRIDES` | the-ageism-gap-singapore-employers |
| "Tsao" (the Tsao Foundation) | Unknown word | Spelled out letter by letter — no lexicon entry (Chinese surname 曹) | `tsˈW` ("TSOW", rhymes with "how"/"now"). Confirmed by Chris by ear from three synthesized samples, over "chow" (`ʧˈW`) and "zow" (`zˈW`) | `PRONUNCIATION_OVERRIDES` | the-ageism-gap-singapore-employers |
| "resume" / "resumes" (the CV noun) | Wrong entry / homograph collision | misaki's "resume" entry is the **verb** reading `ɹɪzjˈuːm` ("re-ZYOOM", as in "operations resumed"); it says that for the CV noun too | Context-aware, so the verb stays untouched: `ABBREVIATION_EXPANSIONS` rewrites the *noun* "resume"/"resumes" → the accented "résumé"/"résumés" (singular only after a determiner/possessive/adjective; plural always), and `PRONUNCIATION_OVERRIDES["résumé"] = "ɹˈɛzuːmA"` ("REH-zoo-may") supplies the reading misaki has no entry for. The `.srt`/burned captions then read "résumé" (the correct accented spelling). Bare verb "resume"/"resumed"/"resuming" is never matched. Known gap: a 3rd-person-singular verb "resumes" ("trading resumes Monday") would be miscaught — handle per-post if it comes up | `ABBREVIATION_EXPANSIONS` + `PRONUNCIATION_OVERRIDES` | the-ageism-gap-singapore-employers |
| "passersby" | Unknown word | Spelled out letter by letter — no lexicon entry, though "passers" (`pˈɑːsəz`) and "by" both phonemize fine (same compound gap as "phrasebook"/"topline") | `pˈɑːsəzbI` | `PRONUNCIATION_OVERRIDES` | fine-city-fine-print-singapore-rules-still-stick |
| "plainclothes" | Unknown word | Spelled out letter by letter — no lexicon entry, though "plain" (`plˈAn`) and "clothes" (`klˈQðz`) phonemize fine | `plˈAnklQðz` (dropping the second stress) | `PRONUNCIATION_OVERRIDES` | fine-city-fine-print-singapore-rules-still-stick |
| "quo" | Unknown word | Spelled out letter by letter — no lexicon entry (Latin; only ever appears in "status quo") | `kwˈQ` ("kwoh", /kwəʊ/) | `PRONUNCIATION_OVERRIDES` | fine-city-fine-print-singapore-rules-still-stick |
| "[to]" (editorial square brackets in a quote) | Unknown symbol | misaki reads "[" and "]" as literal "?" tokens ("including ? to? immediate family members") | Regex `\[([A-Za-z][A-Za-z ]*)\]` → `\1` — strip the brackets, keep the word(s). Only matches a bracketed run of letters/spaces, so a "[...]" ellipsis is left untouched. General fix, not just this token | `ABBREVIATION_EXPANSIONS` | skillsfuture-at-ten-promise-vs-practice ("including [to] immediate family members") |
| "Tharman" | Unknown word | Spelled out letter by letter — no lexicon entry (Tamil name of the former DPM / current President) | `tˈɑːmən` ("TAH-mun"; hard "T", not "th"/θ). Confirmed by Chris by ear | `PRONUNCIATION_OVERRIDES` | skillsfuture-at-ten-promise-vs-practice |
| "Shanmugaratnam" | Unknown word | Spelled out letter by letter — no lexicon entry (long Tamil surname) | `ʃˌɑːnmʊɡəɹˈatnəm` ("shahn-moo-guh-RAT-nam", stress on "rat", from Tamil *ratnam*, "jewel"). Picked by Chris by ear from three samples — a hard name people say slightly differently anyway, so "close enough" is the bar | `PRONUNCIATION_OVERRIDES` | skillsfuture-at-ten-promise-vs-practice |
| "codenames" | Unknown word | Spelled out letter by letter — no lexicon entry, though "code" + "names" phonemize fine (compound gap, like "phrasebook") | `kˈQdnAmz` | `PRONUNCIATION_OVERRIDES` | kampongs-under-pulau-tekong |
| Malay / Chinese kampong names on Pulau Tekong: "Yong", "Kong" (San Yong Kong), "Batu", "Koyok", "Merah", "Sungei", "Belang", "Ayer", "Samak", "Pengkalan", "Pakau" | Unknown word | All spelled out letter by letter — no lexicon entries | `jˈɒŋ` / `kˈɒŋ` / `bˈɑːtuː` / `kˈQjɒk` / `mˈɛrɑː` / `sˈʊŋaɪ` / `bˈɛlaŋ` / `ˈaɪə` / `sˈɑːmak` / `pəŋkˈɑːlan` / `pˈɑːkaʊ` — anglicized approximations, same batch pattern as the National Service post's Malay place names. Reviewed by Chris by ear from two grouped samples — all clear enough, no changes. "San Yong Kong" is three words here so "Yong"/"Kong" get their own entries even though the NS post has "Sanyongkong" as one word | `PRONUNCIATION_OVERRIDES` | kampongs-under-pulau-tekong |
| 1840s Singapore proper nouns: "Stamford" (Raffles), "Tock"/"Seng" (Tan Tock Seng), "Tanjong"/"Pagar", "Butterworth" (Governor), "Huay" (Hokkien Huay Kuan), "Thian" (Thian Hock Keng), "Telok" (Telok Ayer), "Chan" (Cham Chan Sang), "Kim" (Tan Kim Ching), "Serangoon", "Balestier" | Unknown word | All spelled out letter by letter — no lexicon entries | `stˈamfəd` / `tˈɒk` / `sˈɛŋ` / `tˈandʒɒŋ` / `pɑːɡˈɑː` / `bˈʌtəwəθ` / `hwˈA` / `tˈiːɛn` / `tˈɛlɒk` / `ʧˈɑːn` / `kˈɪm` / `sˌɛrəŋɡˈuːn` / `bəlˈɛstɪə` — Chinese-surname romanizations built by the same analogy pattern as Lim/Chong/Goh/Keng; Malay place names from Wiktionary/Wikipedia IPA plus the "keep full unstressed vowels" rule. Reviewed by Chris by ear (2026-08-29) from samples in `scratch/tan-tock-seng-samples/` — the leading candidate confirmed for each (Tan Tock Seng "TOK-seng", Huay "hway", Thian "TEE-en", Telok "TEH-lok", Stamford "STAM-fuhd"). Several recur across Singapore-history posts (Stamford, Serangoon, Telok Ayer, Tanjong Pagar, Balestier), like Istana/Changi/Pulau | `PRONUNCIATION_OVERRIDES` | tan-tock-seng-pauper-to-philanthropist |
| Satay Club post place / person names: "Hoi" (Hoi How Road), "Dhoby"/"Ghaut" (Dhoby Ghaut), "Prinsep", "Elizabeth" (Queen Elizabeth Walk), "Nicoll" (Nicoll Highway), "Saiful"/"Juwahir" (Encik Saiful bin Haji Juwahir), "Geylang", "Bahru" (Geylang Bahru), "saté" | Unknown word | All spelled out letter by letter — no lexicon entries; "saté" also loses the accent and is read "sate" (rhymes with "late") | `hˈɔɪ` / `dˈQbi` / `ɡˈɔːt` / `pɹˈɪnsɛp` / `ɪlˈɪzəbəθ` / `nˈɪkəl` / `sˈaɪfʊl` / `dʒʊwˈɑːhɪə` / `ɡˈeɪlʌŋ` / `bˈɑːruː` / `sɑːtˈeɪ`. "Geylang" corrected by Chris to "GAY-lung" (the "hung"/"sung" vowel in the second syllable, not "hang"/"gang" — same pattern as "Kang"). "Ghaut" confirmed "gawt" by Chris; "satay" left as misaki's default `sˈatA` ("SAT-ay") per Chris. Ear-review samples in `scratch/satay-club-samples/`. Geylang, Dhoby Ghaut, Prinsep, Nicoll, Bahru recur across Singapore posts | `PRONUNCIATION_OVERRIDES` | satay-club-esplanade-alhambra-history |
| National symbols post: "Toh"/"Chye" (Toh Chin Chye), "Zubir" + "Said" (Zubir Said), "Majulah"/"Singapura", "Yusof"/"Ishak" (Yusof bin Ishak), "Rajaratnam" (S. Rajaratnam), plus "expelled", "namable" | Unknown word | All spelled out letter by letter; "Said" is read as the English past tense ("sed") so an ABBREVIATION_EXPANSIONS rule rewrites "Zubir Said" -> "Zubir Saeed" | `tˈQ` / `ʧɪn` (de-stressed - misaki's `ʧˈɪn` made the middle of "Toh Chin Chye" pop) / `tʃˈaɪ` / `zˈuːbɪə` / `sɑːˈiːd` ("Saeed") / `mˈɑːdʒʊlɑː` ("MAH-ju-lah", first-syllable stress) / `sˌɪŋɡəpˈuːrɑː` / `jˈuːsɒf` / `ɪshˈɑːk` ("is-HAHK", audible /h/) / `rˌɑːdʒɑːɹˈatnəm` ("rah-JAH-rat-nam" - a schwa there voiced "joo") / `ɪkspˈɛld` / `nˈAməbᵊl`. Malay/Tamil/Chinese-name readings are anglicised approximations, all confirmed by Chris by ear (2026-08-30) from samples in `scratch/national-symbols-samples/`. "-ratnam" matches Shanmugaratnam above | `PRONUNCIATION_OVERRIDES` + `ABBREVIATION_EXPANSIONS` | singapore-flag-anthem-pledge-written-on-deadline |
| Japanese Garden post: "Seiwaen" (the garden's name), "Kinsaku"/"Nakane" (the landscape architect), "Muromachi"/"Momoyama" (art-history periods), "karesansui" (dry rock garden), plus "dammed", "masterplan", "Sentosa" | Unknown word | All spelled out letter by letter — no lexicon entries; "dammed" (past of "to dam") missing though "damned" works; "Sentosa's"/"Nakane's" possessives also need their own entries | `sˈeɪwɑːɛn` / `kˈɪnsɑːkuː` / `nɑːkˈɑːneɪ` / `mˌʊrəmˈɑːtʃi` / `mˌQmQjˈɑːmə` / `kˌarɛsˈansuːi` / `dˈamd` / `mˈɑːstəplˌan` / `sɛntˈQsə`. Japanese readings are romaji-to-English approximations; lead choices confirmed by Chris by ear (2026-08-30) from samples in `scratch/japanese-garden-samples/` (Seiwaen "say-WAH-en", Nakane "nah-KAH-nay", karesansui "kah-reh-SAHN-soo-ee"). "Sentosa" recurs across Singapore posts | `PRONUNCIATION_OVERRIDES` | japanese-garden-jurong-seiwaen-reconciliation |
| JSP (postwar cleanup) post: "Keppel" (Keppel Harbour), "Seletar" (naval base/town), "Klang" (Klang line/river), "Tengah" (RAF Tengah), "Rayman" (1947 Municipal President), "Dilwara" (troopship HMT Dilwara), plus "banned"; and the year range "1941–42" | Unknown word / unknown symbol | Place names and "Rayman"/"Dilwara" spelled out letter by letter; "banned" (past of "to ban") missing though "ban"/"banning" work — same narrow inflection gap as "dammed"/"expelled"; "1941–42" (abbreviated second year) mushes together with the dash as an audible "?" | `kˈɛpəl` / `sˌɜːlˈiːtɑː` ("sir-LEE-tar", per Chris) / `klˈaŋ` ("clang", per Chris) / `tˈɛŋɑː` / `rˈeɪmən` / `dɪlwˈɑːrə` / `bˈand`. Seletar and Klang confirmed by Chris by ear (2026-08-30) from samples in `scratch/jsp-samples/`; Keppel/Tengah/Rayman/Dilwara accepted as-is. The year range is a text expansion: regex `\b(\d{2})(\d{2})[–-](\d{2})\b` → `\g<1>\g<2> to \g<1>\g<3>` ("1941–42" → "1941 to 1942"), placed **after** the existing `\d{4}[–-]\d{4}` rule. Also: the post's photo-caption text "PoWs" was normalised to "POWs" — misaki reads the all-caps form correctly ("pee-oh-double-yews") but chokes on the mixed-case "PoWs". Keppel, Seletar, Tengah recur across Singapore posts | `PRONUNCIATION_OVERRIDES` + `ABBREVIATION_EXPANSIONS` | japanese-surrendered-personnel-singapore-cleanup-1945 |
| POSB post: markdown that leaked into the narration — `## ` section headings (the `#`s spelled out) and single-`*` emphasis (`*The Straits Times*` → the trailing `*` stuck to "Times"); plus "schoolchildren", "Kuala"/"Lumpur", "non-romanised", "Chok"/"Kian" (Tan Chok Kian), "Hu" (Richard Hu), "POSBank"; and "POSB"/"DBS" letter-spelled | Unknown word / stray markdown | Headings were passed through as sentences; `EMPHASIS_RE` (single `*`) wasn't stripped (only `**bold**` was); the rest are ordinary unknown-word gaps | **Extractor fix, not just overrides:** `_process_block()` now skips `HEADING_RE` lines (`^#{1,6}\s+\S`) and strips `EMPHASIS_RE` (`\*([^*\n]+)\*`) after `BOLD_RE`. Overrides: `skˈuːltʃˌɪldrən` (confirmed) / `kwˈɑːlɑː` ("KWAH-lah", per Chris) / `lˈuːmpɔː` ("LOOM-por", per Chris) / `nˌɒnrˈQmənaɪzd` (confirmed) / `tʃˈɒk` / `kˈiːɛn` / `hˈuː` ("hoo", confirmed by Chris) / `pˈQsbaŋk` ("POHSS-bank", +`POSBank's`) — first tried spelled-out `pˌiːQˌɛsbˈaŋk` ("P-O-S-Bank"), but on hearing it in the finished video Chris asked for "Pos Bank" rhyming with "Post Bank" instead. "POSB" and "DBS" added to `KNOWN_LETTER_SPELLED` — Singaporeans say them letter by letter, so misaki's default is correct. All confirmed by Chris by ear (2026-08-30) from samples in `scratch/posb-samples/` — Chok "chock", Kian "KEE-en" (`kˈiːɛn`, over the "KY-en" alternative). Kuala Lumpur recurs across posts | `_process_block()` + `PRONUNCIATION_OVERRIDES` + `KNOWN_LETTER_SPELLED` | posb-peoples-bank-nation-of-savers |
| Yaohan post: Japanese store/brand names ("Yaohan", "Isetan", "Daimaru", "Sogo", "Takashimaya", "Mitsuwa", "Jusco", "Donki"), Japanese personal names ("Kazuo"/"Wada"/"Ryohei"/"Katsu"), Japanese terms ("Atami", "depachika", "Seicho-no-Ie"), and Singapore place names ("Katong", "Thomson", "Timah", "Havelock", "Liang", "Ngee"/"Ann", "Hong" of Hong Kong) | Unknown word | All spelled out letter by letter | `jˈaʊhɑːn` ("YOW-hahn") / `ˌiːsˈeɪtan` ("ee-SAY-tan", per Chris) / `dˈaɪmɑːruː` / `sˈQɡQ` / `tˌɑːkəʃiːmˈɑːjə` / `mɪtsˈuːwə` / `dʒˈʌskQ` / `dˈɒŋki` / `kˈɑːzuːQ` / `wˈɑːdə` / `riˈQheɪ` / `kˈatsuː` / `ɑːtˈɑːmi` / `dˌɛpətʃˈiːkə` / `sˈeɪtʃQnQˌiːˈeɪ` / `kˈɑːtɒŋ` / `tˈɒmsən` / `tˈiːmɑː` / `hˈavlɒk` / `liˈaŋ` / `ŋˈiː` / `ˈɑːn` / `hˈɒŋ` (+ `Yaohan's` / `Isetan's` / `Takashimaya's`). Anglicised approximations; Singaporeans say the store and place names daily so the bar is "close enough". Confirmed by Chris by ear (2026-08-31) from samples in `scratch/yaohan-samples/`, incl. Isetan "ee-SAY-tan" (over "ee-seh-TAHN"). Katong, Thomson, Bukit Timah, Havelock, Hong Kong, Ngee Ann recur across posts | `PRONUNCIATION_OVERRIDES` | yaohan-japanese-department-stores-orchard-road |
| Aw brothers post: proper nouns ("Chu"/"Cheng"/"Cho", "Eng"/"Aun", "Neil", "Chung"/"Khiaw", "Panjang", "Kwong", "Deco", "Lianhe"/"Zaobao") **plus two plain English words misaki has no lexicon entry for** — "rigged" and "Disneyland"; and "UOB"/"UOL" letter-spelled | Unknown word | All spelled out letter by letter (misaki-British genuinely lacks entries for "rigged" and "Disneyland", not just the names) | `tʃˈuː` / `tʃˈɛŋ` / `tʃˈəʊ` / `ˈɛŋ` / `ˈɑːn` (= existing "Ann") / `nˈiːl` / `tʃˈʊŋ` / `kjˈaʊ` ("kyow", per Chris — over "kee-OW") / `pandʒˈaŋ` / `kwˈɒŋ` / `dˈɛkəʊ` ("DECK-oh") / `liˌɛnhˈʌ` ("lee-en-HUH", per Chris) / `dzaʊbˈaʊ` ("dzow-BOW") / `ɹˈɪɡd` / `dˈɪznilˌand`. "UOB"/"UOL" added to `KNOWN_LETTER_SPELLED` — said letter by letter, misaki's default is correct. Khiaw + Lianhe picked by Chris (2026-09-01) from samples in `scratch/aw-brothers-*/`; the rest are single-obvious-reading. Note: **check any plain English word that gets flagged** — misaki's lexicon has real gaps ("rigged"), not only proper-noun ones | `PRONUNCIATION_OVERRIDES` + `KNOWN_LETTER_SPELLED` | aw-brothers-tiger-balm-fortune |
| Malaysian railway-land post: Singapore/Malaysia place and personal names ("Shenton", "Maclaren", "Cecil"/"Clementi", "Kranji", "Rochor"), Malay words ("Keretapi"/"Tanah"/"Melayu", "Khazanah"/"Nasional"), Malaysian ministers ("Daim"/"Zainuddin", "Mahathir"/"Mohamad", "Najib"/"Razak"), "Hsien"/"Loong", "Temasek", "Ibrahim"/"Iskandar", "Chagar" — **plus "initialled"** (plain English, no misaki entry); "FMSR"/"KTM" letter-spelled; "Pte Ltd" text-expanded | Unknown word | Spelled out letter by letter | `ʃˈɛntən` / `məklˈarən` / `sˈɛsɪl` / `kləmˈɛnti` / `krˈandʒi` / `rˈəʊtʃɔː` / `kˌɛrətˈɑːpi` / `tˈɑːnə` / `məlˈɑːjuː` / `kˌɑːzɑːnˈɑː` / `nˌɑːsjɒnˈɑːl` / `dˈaɪm` / `zˌaɪnʊdˈiːn` / `mˌɑːhɑːtˈɪə` / `mɔːhˈaməd` / `nɑːdʒˈiːb` / `rɑːzˈɑːk` / `sjˈɛn` ("syen", one syllable, per Chris) / `lˈɒŋ` ("long", per Chris) / `tˈɛməsɛk` / `ˈɪbrəhiːm` / `ɪskˈandɑː` / `tʃˈɑːɡɑː` / `ɪnˈɪʃəld`. `Pte\.?\s+Ltd\.?` → "Private Limited" via `ABBREVIATION_EXPANSIONS`. "FMSR"/"KTM" added to `KNOWN_LETTER_SPELLED` (universally spelled out). Anglicised approximations; the Malay names and "Maclaren"/"Hsien" are the ones worth an ear-check | `PRONUNCIATION_OVERRIDES` + `ABBREVIATION_EXPANSIONS` + `KNOWN_LETTER_SPELLED` | malaysian-railway-land-inside-singapore |

**How to verify a new candidate fix** before adding it: test directly
against misaki, no post/pipeline involvement needed —

```python
from misaki import en
g2p = en.G2P(british=True)  # bm_george is a British voice
ps, toks = g2p("your test sentence here")
print(ps)
```

First figure out which root cause you're looking at:

- Comes back as a `❓`/spelled-out mess → **unknown word or symbol**.
- Fluent phonemes, but they're a different word's ("stung"/"strung")
  → **wrong entry**.
- Fluent phonemes reading a bare numeral as the wrong cardinal/ordinal
  → **wrong number-reading convention** (dates specifically).
- Fluent phonemes that spell out the token's own letters, and the
  token isn't a genuine initialism → **letter-spelling fallback
  applied to the wrong token** (this is the one
  `scan_for_letter_spelled_words()` finds automatically - see above).

That determines which fix mechanism fits. For a wrong-entry case,
compare the output for the suspect word against a similar word you
know phonemizes correctly (e.g. "stung" vs. "sung"/"flung"; "graves"
vs. "caves"/"waves") to spot the exact difference before picking a
fix. Once you have a candidate phoneme string, apply it via
`g2p.lexicon.golds["word"] = "..."` and re-run the same test to
confirm it's fixed *before* touching `generate_narration.py`.

**For a foreign word (Malay, Chinese, etc.), don't guess from English
spelling-analogy alone.** A batch of Malay place names on the National
Service post (Taman, Bukit, Pasir, and others) came back "mostly
wrong" on the first attempt, guessed the same way as everything else
in this doc - by finding an English word with similar spelling and
borrowing its phonemes. That works for English-derived proper nouns
(surnames, place names spelled with English conventions) but not
reliably for genuinely foreign phonetic systems, since English's
habit of reducing unstressed vowels to a schwa doesn't apply to Malay,
among other mismatches. Two things fixed it: (1) checking a word's
real IPA on Wiktionary before guessing (most common Malay words have
an entry), and (2) synthesizing a short audio sample and sending it
directly for a listen - which is also just the fastest way to close
the loop on *any* candidate fix, foreign or not, rather than describing
phonemes back and forth in text. See `scripts/generate_narration.py`'s
git history around the National Service post fixes for a worked
example of the synthesis snippet used for this.

**Preparing those samples is a standard step now, not a fallback**
(confirmed by Chris, 2026-08-28). Whenever `--dry-run` flags a word,
or a mispronunciation is suspected any other way, [Claude] synthesizes
2-3 short samples of the real sentence — one per candidate reading —
into `scratch/<slug>-<word>/` (git-ignored), named so the reading each
one uses is obvious from the filename (`A_chah-ngee.wav`,
`B_chan-jee.wav`, `C_char-ngee-stress2.wav`). The leading candidate
goes into `PRONUNCIATION_OVERRIDES` straight away with a
`# NOT ear-verified yet` comment so the dry-run passes; Chris picks
the winner by ear, then the override is updated to the chosen reading
and the note dropped. Worked example: the "Changi" row above (three
samples, second-syllable stress chosen). This mirrors the note in
`docs/production-pipeline.md` section 1.

For a confirmed-correct letter-spelled token (the last category
above), the fix isn't a phoneme or text change at all - just add the
token's exact text to `KNOWN_LETTER_SPELLED` in `generate_narration.py`
(near `scan_for_letter_spelled_words()`) so it stops getting flagged.
