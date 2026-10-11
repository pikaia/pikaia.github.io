# Voice clone of Chris for the narration

**Status:** proposed 2026-10-10, not started. Waiting on the reference
recording (section 2).

## Goal

Narrate the blog's audio and videos in Chris's own voice instead of
Kokoro's `bm_george`, generated locally on this laptop, so that the
cartoon avatar (see `2026-10-02-avatar-presenter-design.md`) speaks with a
voice that sounds like the person it is drawn from. Chris hopes the pair
gives the channel a local Singaporean feel. Accent matters to him: a clone
that keeps George's British accent with Chris's timbre is only a partial
win.

Decided earlier (2026-10-07) and not reopened here: the photo avatar is
shelved, the cartoon stays, and the clone ships with the cartoon.

## Constraints

- **Local only, CPU only.** The laptop is an i5-1240P with 16 GB RAM and
  no NVIDIA GPU. Nothing that needs a rented GPU or a cloud TTS service.
- **Commercial-use licence on both code and weights**, since the channel
  is being monetised. This rules out XTTS-v2 (Coqui Public Model License)
  and F5-TTS (CC-BY-NC weights). Coqui no longer exists to sell a
  commercial licence. Re-check each candidate's licence on the day it is
  installed, because model cards change.
- **No training.** Fine-tuning or training a voice model (RVC and similar)
  needs a GPU. Both candidates below are zero-shot: they take a short
  reference clip and need no training run.
- **The rest of the pipeline should change as little as possible.** It
  depends on three things the narration step produces today: the
  per-sentence `timing.json`, the `.srt`, and the Kokoro phoneme
  durations that `avatar_visemes.py` uses for mouth shapes.

## Candidates

### Option A: Kokoro + OpenVoice v2 tone-colour converter

Kokoro still speaks every sentence exactly as now, then OpenVoice v2's
converter (MIT, code and weights) re-voices the audio towards Chris's
reference clip.

- **Keeps:** every `PRONUNCIATION_OVERRIDES` entry, the sentence cache,
  `timing.json`, and the mouth shapes. The converter works frame by frame
  and keeps the clip length. This must be checked in the bake-off (section
  3): if a converted sentence's length is within a frame (40 ms) of the
  Kokoro original, the timings and visemes carry over unchanged.
- **Risk:** it mostly transfers timbre (how the voice sounds), not accent
  or rhythm. The result may sound like Chris doing a British accent, which
  is the thing Chris most wants to avoid.
- **Cost:** a second model pass per sentence, expected to be cheap on CPU
  (estimate; measure it in the bake-off).

### Option B: Chatterbox zero-shot clone

Chatterbox (Resemble AI, MIT) generates speech directly from text in the
voice of the reference clip.

- **Gains:** Chris's own accent and rhythm, which is the main point.
- **Loses the phoneme overrides.** Chatterbox takes text, not IPA, so
  every override would become a respelling (e.g. "Pillai" written as
  "Pill-eye"). That means a new respelling table maintained alongside, or
  instead of, the IPA one. The existing overrides cannot be converted
  automatically; each would be rewritten by hand, and only for words that
  come up again. New posts would need ear-picks as now, just in respelling
  form.
- **Loses the mouth shapes.** These come from Kokoro's per-phoneme
  durations, which Chatterbox doesn't expose. The mouth track would either
  fall back to loudness only (`build_avatar_track.py --no-shapes`, the
  Phase 1 look Chris already approved) or need a forced aligner. If an
  aligner is wanted later, check its licence too: several wav2vec2-based
  aligners ship CC-BY-NC weights.
- **Speed:** much slower than Kokoro on CPU. A 7-minute narration could
  take tens of minutes; measure it in the bake-off. The sentence cache
  still helps on re-runs.
- **Watermark:** Chatterbox embeds an inaudible watermark ("Perth") in its
  output by default. That is fine and fits the AI disclosure in section 6.
  Note it in case a platform's detector ever flags the audio.
- **Variability:** zero-shot output varies between runs, so the cache key
  must include a fixed seed.

### Not pursued

- **XTTS-v2, F5-TTS:** licences, as above.
- **RVC or any fine-tune:** needs a GPU.
- **Cloud services (ElevenLabs etc.):** break the local-only rule, and
  would be a recurring cost.
- **Option C, Chatterbox for most sentences and Kokoro + OpenVoice for
  sentences with hard names:** mixing two engines in one narration would
  likely be audible. Only consider it if B wins on the voice but fails
  badly on names.

## 1. Setup

Each candidate goes in its **own Python virtual environment**
(`.venv-openvoice/`, `.venv-chatterbox/` at the repo root, gitignored).
Both pin their own `torch` and audio libraries, and neither should touch
the environment Kokoro and the rest of the pipeline run in. Bake-off
scripts live in `scratch/voice-clone/` until a winner is picked.

## 2. The reference recording (Chris)

A **one-off** recording, not a per-post read.

- **Length:** 2–3 minutes of continuous reading. OpenVoice uses the whole
  clip; Chatterbox wants about 10–20 seconds of it, so Claude cuts the
  cleanest stretch.
- **Room:** quiet, with soft furnishings and no fan, aircon hum or traffic
  if possible. Stay the same distance from the mic throughout.
- **Mic:** a phone held about 20 cm away or a headset mic is fine. No
  speakerphone, no Bluetooth earbuds (they compress the voice).
- **Format:** WAV if the recorder offers it, otherwise the highest-quality
  M4A. Mono is fine. Claude converts as needed.
- **Delivery:** Chris's normal speaking voice, at the pace he'd use to
  tell someone a story. The clone copies whatever it hears, so don't read
  in a "presenter" voice unless that is what the videos should sound like.
- **Where it goes:** `scratch/voice/`. It is never committed and is
  exempt from the per-post scratch clean-up, like the avatar reference
  photos. A recording of someone's voice is enough to clone it, so it is
  treated as private.

**Reading text.** Any text works. This passage mixes plain narration,
numbers, dates and the kinds of names the posts use, so the bake-off can
compare how each option handles them:

> When I was growing up in Hougang in the nineteen-sixties, the bus to
> town took almost an hour, and the conductor punched your ticket by hand.
> My parents talked about the Occupation in a low voice, as if the
> Japanese might still be listening. Most of what I know about those years
> came from them, and from the old shophouses along Upper Serangoon Road.
>
> Singapore's history is full of people who built something and were then
> forgotten. Lim Boon Keng, Tan Kah Kee and Eu Tong Sen are names on roads
> and buildings today, but few people can say what they actually did.
> Others, like P. Govindasamy Pillai on Serangoon Road, or the Chettiars of
> Market Street, are remembered mostly by the families who knew them.
>
> In 1965 the population was just under two million. By 1990 it had passed
> three million, and the kampongs at Kangkar, Punggol and Bukit Timah had
> mostly given way to new towns. Some of the change was planned years
> ahead; some of it happened almost overnight.
>
> I worked in banking from 1987 to 1997, at Security Pacific and then Bank
> of America, and I remember the trading floor going quiet the week the
> Barings news broke. That is the kind of story this blog is for: things
> that happened here, to real people, that most of us have never heard
> about.

Chris may change or replace any of it: the content doesn't matter, only
the voice.

## 3. Bake-off (Claude, then Chris by ear)

Claude produces, in `scratch/voice-clone/samples/`:

1. Three **test sentences** taken from recent posts: one plain, one with
   Chinese names, one with Tamil names (from the P. Govindasamy Pillai
   post). Each is rendered three ways: `kokoro.wav` (today's George, the
   baseline), `openvoice.wav` (option A) and `chatterbox.wav` (option B).
2. A **30-second excerpt** of a real post's opening read by A and by B,
   to judge how it sounds over a stretch rather than one sentence.
3. A short **numbers sheet**: synthesis time per minute of audio for each
   option on this laptop, and for A, the length difference against Kokoro
   per sentence (the 40 ms check above).

Chris listens and judges, in this order:

1. **Does it sound like me?**
2. **Accent:** is George's British accent still there (mainly an A
   question)?
3. **Names:** are the Chinese and Tamil names acceptable?
4. **Glitches:** clicks, robotic patches, breaths in odd places, words
   swallowed.

Speed is a tie-breaker only. A slow render runs once per post, in the
background.

Possible outcomes:

- **A sounds right:** take A. It is a small pipeline change (section 4).
- **A keeps the British accent and B sounds right:** take B and accept the
  respelling and loudness-only mouth costs (section 5).
- **Neither sounds right:** stay on George, note why in this spec, and
  re-check in a few months; zero-shot models are improving quickly.

## 4. Pipeline changes if A wins

- **`generate_narration.py`:** a new `--clone openvoice` flag (default
  off, so every existing command and cache entry is unaffected), with the
  reference clip at `scratch/voice/`. Each Kokoro sentence passes
  through the converter before it is cached.
- **Cache key:** add `{"c": "openvoice", "r": <sha256 of the reference
  clip>}` to `_sentence_cache_key`, so a new reference recording busts
  the cache and George-only entries stay valid.
- **`timing.json`, `.srt`, step 1.5:** unchanged, provided the length
  check holds. If a sentence drifts by more than a frame, the step stops
  and names the sentence rather than producing an out-of-sync mouth.
- **Command file / template:** step 1.2 gains the flag. Tell Chris the
  command changed (standing rule).

## 5. Pipeline changes if B wins

- **`generate_narration.py`:** a `--clone chatterbox` flag that sends
  each sentence to Chatterbox (in its own environment, called as a
  subprocess) instead of Kokoro. `timing.json` and the `.srt` come from
  the real audio lengths as now, so nothing downstream changes shape.
- **Respellings:** a new `RESPELLINGS` table (word → respelled text),
  applied as a text rewrite before synthesis. It works like the existing
  `ABBREVIATION_EXPANSIONS` and is fed by the same dry-run flagging.
  Ear-pick samples (`make_pronunciation_samples.py`) gain a Chatterbox
  mode with two or three respelling candidates.
- **Cache key:** the text after respelling + `"c": "chatterbox"` +
  reference hash + seed.
- **Mouth track:** step 1.5 runs with `--no-shapes` automatically when the
  narration came from Chatterbox (it can tell from the cache provenance it
  already checks). Adding a forced aligner is a later, separate decision.
- **Speed:** step 1.2 runs in Chris's own terminal, in the background, like
  the video renders.

## 6. Disclosure and release

- **Labels:** from the first video narrated by the clone, tick YouTube's
  "altered or synthetic content" box, add TikTok's AI-generated label,
  and add a line to the video description (e.g. "Narrated by an AI clone
  of the author's voice"). Add this to `stage_youtube_text.py` so it isn't
  forgotten.
- **The blog:** add a short note to the About page that the Listen audio
  is an AI clone of Chris's voice.
- **Existing videos:** stay on George. No re-renders, in line with the
  rollout-order rule (finish the pipeline on every post first, rerun
  batches later). Whether to re-voice old posts is a later decision.
- **The retention read on 2026-10-14** measures the cartoon with George.
  Don't switch voices before that read, or the two changes get mixed up
  in the numbers.

## Open questions

- Whether Chris wants the clone on Shorts and TikTok as well as the main
  video. The default is yes, since the Short is cut from the same
  narration.
- If B wins, whether the loudness-only mouth looks flat enough next to the
  shaped mouths to justify adding a forced aligner.
