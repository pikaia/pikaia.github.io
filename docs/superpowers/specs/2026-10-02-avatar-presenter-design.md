# Avatar presenter for YouTube videos — design

Date: 2026-10-02
Status: approved in conversation, awaiting written-spec review

## Goal

Add an on-screen presenter to the YouTube videos so they feel less like a
slideshow and hold viewers longer, especially in the first 30 seconds. The
presenter is a stylised, flat-vector caricature of Chris in a circular
corner "bubble", with its mouth driven by the existing narration audio.

**Hard requirement:** everything is scripted and run locally. No external
services, no hosted avatar/lip-sync APIs, no cloud rendering.

## Phasing

| Phase | Scope | Trigger |
|---|---|---|
| **1 (this spec)** | Corner bubble during intro + outro ranges only, main landscape video only, `bm_george` voice | — |
| 2 | Same bubble for the whole video (`"ranges": [(0, None)]`) | Phase 1 retention improves |
| Later, separate projects | Local voice clone of Chris (see voice-clone note below); Shorts; in-post Watch widget (JS, reusing the same SVG + mouth file); phoneme-shaped mouths (**done 2026-10-02**, `docs/superpowers/specs/2026-10-02-avatar-shaped-mouths-design.md`); expressions | Each on its own merits |

Phase 1 design choices are made so the later phases don't need rework: the
mouth file is voice-agnostic (amplitude-based), and the SVG + JSON pair is
renderer-agnostic (Python now, browser later).

**Voice-clone note (2026-10-02):** XTTS-v2 and F5-TTS are **excluded** —
both ship pretrained weights under non-commercial licences (Coqui Public
Model License; CC-BY-NC), incompatible with a monetised channel, and Coqui
no longer exists to sell a commercial licence. Candidates instead, both
MIT and CPU-runnable on the current laptop (i5-1240P, 16 GB, no NVIDIA
GPU): **OpenVoice v2** as a voice-conversion pass over Kokoro output
(keeps the whole pronunciation-override pipeline, but mostly transfers
timbre — accent/rhythm stay Kokoro's), or **Chatterbox** zero-shot cloning
(carries Chris's accent, but loses Kokoro phoneme overrides and is slow on
CPU). Training a model (e.g. RVC) needs a GPU, which breaks the local-only
rule. Re-verify licences at the time; decide by an ear test of ~30 s of
Chris's voice through both.

## Out of scope (Phase 1)

Voice cloning, viseme/phoneme mouth shapes, Shorts, the Watch widget,
facial expressions or gestures, any change to `watch_video_lib.py`.

## 1. Character asset

- **Source of truth:** `assets/avatar/avatar.svg`, a layered SVG traced by
  hand from a front-facing photo of Chris. The reference photo lives only
  in `scratch/` and is never committed.
- **Style:** flat vector, ~6–8 colours, no gradients, framed in a circle
  with a thin border so it separates from any photo behind it.
  Recognisably Chris, clearly an illustration.
- **Layer groups** (SVG `<g id=...>`):

  | Group | Variants | Purpose |
  |---|---|---|
  | `body` | 1 | head-and-shoulders bust, circle frame + border |
  | `eyes` | `eyes-open`, `eyes-closed` | blinking |
  | `mouth` | `mouth-0` (closed) … `mouth-3` (wide open) | lip-sync levels |
  | `brows` | 1 | placeholder for later expressions |

- **Rasterising:** `scripts/build_avatar.py` renders each variant to a
  transparent PNG in `assets/avatar/png/` (`body.png`, `eyes-open.png`,
  `eyes-closed.png`, `mouth-0.png` … `mouth-3.png`), all the same square
  canvas size so they stack without offsets. Uses the `resvg-py` pip wheel
  (offline, no Cairo DLLs). It renders one variant at a time by hiding
  the sibling variants in a copy of the SVG. The PNGs are committed — a
  documented binary exception, like the OSM tiles — so rendering a video
  doesn't depend on `resvg-py` being installed. Render size: 512×512
  (downscaled at overlay time).
- **Likeness workflow:** Chris supplies the photo → Claude drafts the SVG →
  preview as an Artifact → iterate until approved → lock.

## 2. Mouth file

**Script:** `scripts/build_avatar_track.py audio/<slug>.mp3 [--fps 25]`
→ writes `audio/<slug>.avatar.json`. New pipeline step **1.5**, run after
narration is generated and verified (1.2–1.4), so after pronunciation overrides are final.

**Algorithm:**
1. Decode the mp3 to mono 16 kHz float PCM via ffmpeg (subprocess, piped
   to numpy).
2. For each video frame `i` (at `fps`), RMS over a window centred on
   `i / fps` (window = 1/fps, i.e. 40 ms at 25 fps).
3. Normalise: divide by the 95th-percentile RMS of frames above a
   silence floor, clamp to [0, 1].
4. Quantise to levels 0–3 with thresholds (initial: `<0.08 → 0`,
   `<0.35 → 1`, `<0.65 → 2`, else `3`), constants at the top of the script
   so the lip-sync preview can tune them.
5. Debounce: a new level must hold ≥ 2 frames before it replaces the
   current one, except a drop to 0 (silence), which applies immediately so
   pauses close the mouth crisply.
6. Blinks: one every 3–6 s (uniform), 3 frames long, from a
   `random.Random(seed)` where seed is derived from the slug, so reruns
   and future renderers (JS widget) produce identical blinks. Blinks
   aren't suppressed during speech.

**Format:**

```json
{
  "version": 1,
  "fps": 25,
  "frames": 15328,
  "duration_s": 613.12,
  "source": "audio/<slug>.mp3",
  "mouth": "000123321100...",
  "blinks": [87, 201]
}
```

`mouth` is one digit per frame (`len(mouth) == frames`); `blinks` lists
start frames of each 3-frame blink.

## 3. Avatar track + overlay

Step 6 (`watch_video_lib.py` → `preview-motion/<slug>.mp4`) is unchanged
and knows nothing about the avatar.

### Config

Optional `AVATAR` dict in the main video config. Absent = no avatar; steps
6a/6b are skipped and nothing else changes.

```python
AVATAR = {
    "ranges": [(0, 30), (-30, None)],  # seconds; negative = from the end; None = to the end
    "corner": "bottom-right",          # bottom-right | bottom-left | top-right | top-left
    "size": 0.20,                       # bubble diameter as a fraction of frame height
    "margin": 0.03,                     # gap to frame edges, fraction of frame height
    "fade": 0.3,                        # fade in/out seconds at each range boundary
}
```

Ranges are resolved against `TOTAL_DURATION` and validated (start < end,
within the video, non-overlapping after resolution); an invalid range is
an error, not a silent clamp.

### Step 6a — render the avatar track

`python scripts/render_avatar_track.py --config scripts/video-configs/<slug>.py`

- Loads `audio/<slug>.avatar.json` and the PNG layers.
- **Staleness checks (hard errors):** `fps` must match the config's FPS;
  `duration_s` must be within one frame of the config's
  `TOTAL_DURATION` — otherwise tell the user to re-run step 1.5.
- Composes `body` → `eyes-open|closed` → `mouth-N`, scaled to the bubble
  size, with alpha, for frames inside the resolved ranges; frames outside
  them are fully transparent (cheap — a reused blank buffer). Output:
  `preview-motion/<slug>-avatar.mov`, qtrle RGBA, spanning the full video
  duration so its timestamps line up 1:1 with the main video, piped raw
  RGBA into one ffmpeg process.
- Single process; memory footprint is the handful of small PNG layers.

### Step 6b — overlay

`python scripts/overlay_avatar.py --config scripts/video-configs/<slug>.py --in preview-motion/<slug>.mp4 --out preview-motion/<slug>-avatar.mp4`

- One ffmpeg pass: `overlay` filter at the configured corner/margin, with
  the fade applied to the avatar input's alpha at each range boundary
  (`fade=t=in:alpha=1` / `fade=t=out:alpha=1` per range, chained via the
  overlay `enable` expression or a pre-built alpha ramp — implementer's
  choice, verified by spot frames).
- Audio stream copied (`-c:a copy`); video re-encoded with the same codec
  settings `watch_video_lib.render()` uses.
- Never overwrites the input: the plain `<slug>.mp4` survives for A/B.
- Ordering: if the post has route-walk clip splices, they are applied to
  `<slug>.mp4` first; the avatar overlay is always the last video step.

## 4. Verification

No test suite exists; follow the pipeline's verify-cheap-before-expensive
habit.

1. **Mouth file** on an existing narration (Barings): `len(mouth) ==
   frames == round(duration * fps)`; mouth is `0` across the inter-sentence
   gaps in `audio/<slug>.timing.json`; level histogram is plausible
   (mostly 1–2, rarely 3).
2. **Lip-sync preview:** a 15 s clip of the bubble alone on a plain
   background with the real narration audio (`scratch/avatar-preview/`),
   for Chris to judge by eye/ear; thresholds tuned here.
3. **Full dry run on Barings:** step 6 → 6a → 6b; full-decode check
   (`ffmpeg -v error -i <out> -f null -`); duration and frame-count parity
   with the plain video; spot frames (Read tool) at t=0, just inside and
   just outside each range boundary, mid-fade, and mid-video (no bubble).
4. `ruff check .` clean.

## 5. Running the test (Phase 1)

- Apply `AVATAR` with bookend ranges to the main video of the next few new
  posts. Shorts and the Watch widget untouched.
- Compare YouTube Studio first-30 s retention and average view duration
  against recent avatar-free videos of similar length/topic; judge after
  ~4–6 videos.
- Success → Phase 2 (`"ranges": [(0, None)]`), then the later projects in
  the phasing table. Failure → drop `AVATAR` from configs; no other impact.

## 6. Docs and process

- `docs/production-pipeline.md`: new steps 1.5, 6a, 6b (with the tee-to-log
  wrapper form), step 8 verifies `<slug>-avatar.mp4` when present, file
  reference entries for the three new scripts and `assets/avatar/`.
- Flag the new commands to Chris explicitly (he runs from a saved
  template).
- YouTube description: add a disclosure line, e.g. "Presented by an
  illustrated avatar of the author; narration voice is synthetic (Kokoro
  TTS)." `stage_youtube_text.py` appends it when the config has `AVATAR`.
- CLAUDE.md: note `assets/avatar/png/` as a committed-binary exception.

## New files

| Path | Purpose |
|---|---|
| `assets/avatar/avatar.svg` | layered character source |
| `assets/avatar/png/*.png` | rasterised layers (committed) |
| `scripts/build_avatar.py` | SVG → PNG layers (`resvg-py`) |
| `scripts/build_avatar_track.py` | mp3 → `audio/<slug>.avatar.json` |
| `scripts/render_avatar_track.py` | mouth file + layers → transparent `.mov` |
| `scripts/overlay_avatar.py` | ffmpeg overlay → `<slug>-avatar.mp4` |
| `audio/<slug>.avatar.json` | per-post mouth/blink track (committed with the audio) |
