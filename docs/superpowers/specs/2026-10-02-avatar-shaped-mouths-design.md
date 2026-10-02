# Avatar presenter: shaped mouths (visemes) — design

Date: 2026-10-02
Status: approved in conversation, awaiting written-spec review
Builds on: `docs/superpowers/specs/2026-10-02-avatar-presenter-design.md` (Phase 1, shipped)

## Goal

Phase 1's mouth only opens and closes with loudness. Add four shaped mouth
positions so the avatar visibly forms the sounds viewers notice most:
closed lips on m/b/p, lip-on-teeth on f/v (e.g. the end of "five"), pursed
lips on oo/w/o, and a wide mouth on ee. Loudness still drives how open the
mouth is everywhere else.

**Hard requirement (unchanged):** everything runs locally; no external
services.

## Out of scope

A fuller animation set (tongue-up l/th, separate o vs oo, narrow e);
expressions; Shorts and the Watch widget (they consume the same file later);
a forced aligner for a future cloned voice (see "Future voices").

## Feasibility (probed 2026-10-02, throwaway scripts in `scratch/viseme-probe/`)

- Kokoro 0.9.4's `KPipeline` result exposes `tokens` (per word: text,
  phonemes, `start_ts`, `end_ts`), `phonemes` (the sentence's phoneme
  string) and `pred_dur` (one duration per phoneme character, plus one
  leading and one trailing boundary entry — `len(pred_dur) ==
  len(phonemes) + 2`).
- One `pred_dur` unit is exactly **600 samples = 25 ms** at 24 kHz;
  `sum(pred_dur) * 600 == len(audio)` exactly.
- `pred_dur` is **deterministic**: identical across repeated runs of the
  same sentence (Kokoro's run-to-run randomness is in the decoder's audio,
  not the duration predictor), and the audio length is identical too.
- `timing.json` stores each sentence's text exactly as synthesized
  (abbreviation rewrites already applied), so feeding it back reproduces
  the same phonemes and durations.

## 1. Phoneme timings and shapes (step 1.5, extended)

**Command unchanged:** `python scripts/build_avatar_track.py audio/<slug>.mp3`
now also computes shapes. New flag `--no-shapes` skips this (loudness-only,
today's behaviour, no model load). Shapes cost one Kokoro model load, about
20–30 s.

**New module `scripts/avatar_visemes.py`** (pure logic, testable without
Kokoro, plus one thin Kokoro-calling function):

1. Read `audio/<slug>.timing.json` (list of `{text, offset_s, duration_s}`),
   next to the mp3.
2. For each sentence, run it through a `KPipeline` built by
   `generate_narration._build_pipeline(lang_code)` (so
   `PRONUNCIATION_OVERRIDES` match synthesis), voice from a `--voice` flag
   (default `bm_george`, matching `generate_narration`), with
   `split_pattern=None`. A sentence may yield several results (Kokoro's own
   long-input chunking); concatenate them in order. No audio is kept.
3. Per result, drop `pred_dur`'s first and last (boundary) entries; the
   remaining entries pair 1:1 with the characters of `result.phonemes`.
   Each character's time span starts at the sentence's `offset_s` plus the
   cumulative duration before it, including the leading boundary entry's
   duration (units × 0.025 s).
4. **Integrity check per sentence:** total units × 0.025 s must equal the
   sentence's `duration_s` within 0.001 s. On mismatch (e.g. an override
   changed after the sentence was cached), that sentence gets no shapes
   (falls back to loudness) and the script lists it.
5. Map each phoneme character to a shape:

   | Shape | Characters | Examples |
   |---|---|---|
   | `M` closed lips | `m b p` | bank, Singapore |
   | `F` lip on teeth | `f v` | five, of |
   | `U` pursed | `u ʊ w O Q ɔ ɒ` | two, we, over |
   | `E` wide | `i ɪ` | see, Leeson |
   | `.` none | everything else | — |

   The length mark `ː` takes the previous character's shape; stress marks
   `ˈ ˌ` take the next character's shape; spaces and punctuation are `.`.
6. **Frame assignment:** frame `i` covers `[i/fps, (i+1)/fps)`. It takes the
   highest-priority shape among all phoneme spans overlapping it, priority
   `M > F > U > E > .`, so a sub-frame "b" still shows.

**Mouth file version 2** (`audio/<slug>.avatar.json`): adds `"shape"`, one
character per frame (`M F U E .`), `len(shape) == frames`, plus
`"shape_fallback"`: list of sentence indices that fell back. `--no-shapes`
writes version 1 (no `shape`). `load_mouth_file` accepts versions 1 and 2
and validates `shape`'s length when present.

## 2. Artwork and rendering

**Four new SVG layer groups** in `assets/avatar/avatar.svg`, centred on the
existing mouth point (256, 338):

| Layer | Drawing |
|---|---|
| `mouth-M` | lips pressed together: flat, slightly fuller than `mouth-0`'s relaxed smile |
| `mouth-F` | upper teeth resting on a tucked lower lip |
| `mouth-U` | small rounded pucker, dark centre, narrower than any open level |
| `mouth-E` | wide and fairly flat, upper teeth showing, corners pulled out |

`LAYER_NAMES` grows from 7 to 11; `build_avatar.py` rasterises them
unchanged. Approved by Chris via an Artifact page (each shape beside its
word) before committing.

**Per-frame mouth choice** in `render_avatar_track.py` (step 6a):
- shape `M/F/U/E` → `mouth-M/F/U/E`, even on a loudness-0 frame;
- else → `mouth-{level}` (level 0, a pause, is the closed `mouth-0`).

*Revised during implementation (2026-10-02):* the draft had silence
(level 0) override shapes. On Barings that hid 55% of f/v frames and 45%
of m/b/p frames, because those sounds are quiet (a hiss, a lip closure)
and the loudness meter reads them as silent. Shapes exist only inside
spoken sounds, never in pauses, so letting them win keeps pauses closed.

Version-1 files and fallen-back sentences render exactly as Phase 1. A PNG
set missing the new layers raises the existing "run `build_avatar.py`"
error. Step 6b is unchanged.

## 3. Verification

**pytest (fast):** phoneme→shape mapping incl. `ː`/stress inheritance;
frame assignment (25 ms "b" inside a frame → `M`; priority order);
combination rule (silence wins, shape beats level, `.` → level); integrity
mismatch → fallback listed (Kokoro results injected); version-1 file
renders as before; missing-layer error.

**pytest (`slow` marker, ~20 s, real Kokoro):** "Five hundred and two of
them moved over to Singapore, where Leeson kept his books." → `F` frames at
the end of "five" (~0.45–0.55 s), `U` frames in "two" (~1.35–1.5 s). Run
before each commit of this feature; skipped by default (`-m "not slow"`
configured in `pyproject.toml`).

**Real data (Barings):** step 1.5 on the Barings narration — expect every
sentence to pass the integrity check; report the shape spread (rough
expectation 5–15% of frames each for M, F, U, E).

**Chris by eye:** Artifact page with the four drawings plus a 15 s Barings
clip with shapes beside the loudness-only clip.

**Docs:** pipeline §1.5 (`--no-shapes`, model-load time, what "fell back"
means); Phase 1 spec phasing table notes shaped mouths done.

## Future voices

The shapes come from Kokoro's own phonemes. If narration moves to a cloned
voice, a local forced aligner (e.g. wav2vec2 CTC) can produce the same
per-phoneme spans; everything from step 5 onward stays the same.

## Files

| Path | Change |
|---|---|
| `scripts/avatar_visemes.py` | new: Kokoro durations → phoneme spans → per-frame shapes |
| `scripts/build_avatar_track.py` | calls it; `--no-shapes`, `--voice`; writes v2 |
| `scripts/avatar_lib.py` | `LAYER_NAMES` + 4; `load_mouth_file` accepts v1/v2 |
| `scripts/render_avatar_track.py` | per-frame shape/level choice |
| `assets/avatar/avatar.svg`, `assets/avatar/png/` | 4 new mouth layers |
| `pyproject.toml` | pytest `slow` marker, skipped by default |
| `tests/test_avatar_visemes.py` (+ updates) | tests above |
| `docs/production-pipeline.md` | §1.5 update |
