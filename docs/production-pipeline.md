# Post & Video Production Pipeline

A step-by-step runbook for producing a full post — narration, in-browser
Watch slideshow, exported MP4, YouTube Short, and the YouTube upload
itself — without Claude. Written so a human (or a Claude session that's
hit its usage limit) can follow it directly. Every command below is
meant to be run from the repo root on this machine (Ruby/Jekyll, Python,
ffmpeg, and the Kokoro TTS packages are already installed locally).

For the parts of writing a post that don't touch narration/video (front
matter, image sourcing, galleries, charts, route-walk slides, the
Straits Times archive/copyright rules, git conventions), see
**`CLAUDE.md`** at the repo root — that file is the source of truth for
those and isn't repeated here. This doc picks up once a post's text,
images, and gallery are finished and approved, and covers everything
from "generate the narration" through "the video is live on YouTube."

## 0. Pipeline overview

Prerequisite: post finished (text + images + gallery) — see CLAUDE.md.

The rest maps 1:1 to this doc's own section numbers:

```
1. Generate narration audio (Kokoro TTS)         -- section 1   [Manual]
2. Insert the Listen widget                      -- section 2   [Manual]
3. Write the video configs (main + Short)        -- section 3   [Claude]
4. Generate the Watch widget from that config     -- section 4   [Manual]
5. Check smoothness + review the gap report      -- section 5   [Manual]
6. Render the main video                         -- section 6   [Manual]
7. Render the YouTube Short                      -- section 7   [Manual]
8. Verify both files                             -- section 8   [Manual]
9. Stage the YouTube upload text file            -- section 9   [Manual]
10. Upload to YouTube (Chris does the clicks)     -- section 10  [Manual]
11. Wire the published URLs into the post         -- section 11  [Manual]
12. Commit and push                               -- section 12  [Claude]
```

**`[Manual]` vs `[Claude]`:** every `[Manual]` step is a single mechanical
script invocation with no real decision to make - safe and fast to run
yourself when Claude's usage limit is hit. Two steps are `[Claude]`,
for different reasons.

**Section 3** (write the video configs) is `[Claude]` because it's
different in kind, not just difficulty: nothing exists yet for a script
to transform, and producing either config requires reading the real
narration text and deciding which image best represents each beat (main
config) or which opening sentences form a self-contained hook (Short
config) - genuine judgment, not something a deterministic script can
stand in for (confirmed in practice: `build_watch_widget.py` only
replaced section 4 because it mechanically transforms an *existing*
config; section 3 has no equivalent input to transform from). Both
configs are written together in section 3, in the same sitting, rather
than the Short's config being written separately later in section 7 -
this used to be split across two sections, but doing both while already
immersed in that post's sentence timings avoids a real failure mode:
reaching section 7's Short render with no `-short.py` config yet
written, because the two steps had drifted apart in practice.

**Section 12** (commit and push) is `[Claude]` because the working tree
at that point is genuinely messy - regenerated `audio/`, new
`video-configs/`/`video-gaps/`/`youtube_helper/` files, and usually
some unrelated tooling or doc edits and stray scratch directories all
mixed together - and sorting what belongs in the post's commit from
what's a separate concern from what's scratch is a `git status` read,
not a fixed `git add` list. It has a mechanical fallback (section 12's
example block), but it goes wrong more often than the other steps when
run on autopilot.

If Claude is unavailable, section 3 is the one true blocker - the video
configs can't be improvised mechanically. Section 12 can be done solo
from its example block, just with a careful eye on `git status` and
`.gitignore`; everything else is a straight script run.

Steps 1-7 (narration through both renders) should happen only **after**
image-gathering is fully finished — the video's slide list and per-image
dwell time both depend on the final image set, so redesigning the
schedule mid-stream after adding a late image is wasted work. Treat
image-gathering as closed before starting narration.

**Logging each step:** every runnable example in this doc is already
built with this pattern baked in — you don't need to add anything
yourself, just copy the block as shown. This section explains what
that pattern is and why, for when you write a command that isn't
already in the doc.

`logs/` is git-ignored, so it won't exist yet on a fresh checkout —
create it once before first use (`mkdir logs` in bash, `New-Item
-ItemType Directory -Force logs` in PowerShell). `tee`/`Tee-Object`
create the log *file* but not a missing parent directory, so piping
into `logs/<slug>.log` before that folder exists fails outright.

Each step in the doc runs as a single brace group piped once to
`tee -a`, so the whole step — its header, the command line, the
command's own output, and its timing — lands in the log as one
contiguous block, with a blank line padding it top and bottom so
sections never run together:

```
# bash
{ echo; date; echo "=== <section>.<n> <short name> ==="
  cmd=(<command> <arg> <arg>)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

Piece by piece:

- **`echo; date; echo "=== ... ==="`** — a leading blank line, then a
  timestamp (`date`) marking when this step ran, then the header naming
  the subsection (e.g. `1.1 Generate narration audio (dry run)`, `1.2
  Generate narration audio`, `1.3 Verify audio file`). Within a section
  that has more than one distinct command,
  each gets its own `<section>.<n>` number and a short descriptive
  name, so the log reads as a clear timeline instead of a wall of
  undifferentiated output; a section with only one command purpose
  (e.g. section 2) just uses the bare section number as its label.
- **`cmd=(...)` then `echo "\$ ${cmd[*]}"`** — the command is defined
  once as an array and echoed back verbatim before it runs, so the
  log always records exactly what was executed. Defining it once,
  rather than also typing it out inside a separate `echo`, is
  deliberate: the echoed line then can't drift from the real command
  as the doc gets edited over time.
- **`time "${cmd[@]}"`** — runs the command, and prints bash's
  built-in `real`/`user`/`sys` timing breakdown after it finishes.
  `real` is wall-clock time, `user`+`sys` is actual CPU time; a `real`
  much larger than `user`+`sys` points at I/O or network waiting
  rather than computation. This is what makes bottlenecks visible in
  the log after the fact, without having to watch the run live.
- **trailing `echo`** — the closing blank line.
- **`} 2>&1 | tee -a logs/<slug>.log`** — the whole group lands in the
  log file *and* still streams to the console as normal; `2>&1` is
  what makes that work (see below).

Every step runs `date` just before its header, so the log reads as a
timestamped timeline — you can see when each step ran and, from the
gaps, how long the manual bits in between took. `[Claude]` steps (3 and
12) get the same treatment: prefix the `=== N. … === [Claude]` header
with the current `date` output.

The PowerShell equivalent (only section 6's `Start-Process` render
genuinely needs PowerShell — every other step has a bash form):

```powershell
# PowerShell - Measure-Command would work too, but it swallows the
# block's live console output by design (it only returns a TimeSpan) -
# a plain Stopwatch avoids that and still streams output normally:
"", "=== <section>.<n> <short name> ===", "`$ <command>" | Tee-Object -FilePath logs\<slug>.log -Append
$sw = [Diagnostics.Stopwatch]::StartNew()
<command> 2>&1 | Tee-Object -FilePath logs\<slug>.log -Append
"took $($sw.Elapsed)", "" | Tee-Object -FilePath logs\<slug>.log -Append
```

Use `-a`/`-Append` (bash) or `-Append` (PowerShell) throughout so every
step's output accumulates into the same file rather than overwriting
the previous step's.

**`2>&1` is not optional** — most of these scripts print their real
status (`OK: ...`, `NOTE: ...`, gap-report/smoothness results) to
stderr, not stdout. Without `2>&1` merging stderr into the piped
stream first, `tee` only ever sees stdout: the command still looks
completely normal on your own screen (stderr always prints straight to
the terminal, pipe or not), but the log file silently ends up empty —
this happened on the very first real use of this feature, caught only
because the log came back blank after an otherwise fully successful
run.

`logs/` is git-ignored scratch, same treatment as `preview-motion/` —
nothing here needs to be committed. Once you've run a step, just tell
Claude "done with steps 1-3 of `<slug>`" and point at `logs/<slug>.log`
instead of pasting the console output directly — Claude can read the
file itself and pick up from there.

---

## 1. Generate narration audio

**Always sanity-check the extracted text first with `--dry-run`**
(prints exactly what will be synthesized) before committing to a real
run — catches leaked raw HTML/JS from a chart or floated-image block
that the parser's tag whitelist doesn't yet cover:

```
{ echo; date; echo "=== 1.1 Generate narration audio (dry run) ==="
  cmd=(python scripts/generate_narration.py _posts/<file>.md audio/<slug>.mp3 --dry-run)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example** (the Jalan Payoh Lai / Kangkar post, used throughout this
doc as a running worked example — slug
`jalan-payoh-lai-kangkar-montfort-nativity-church`):

```
{ echo; date; echo "=== 1.1 Generate narration audio (dry run) ==="
  cmd=(python scripts/generate_narration.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3 --dry-run)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

If something looks wrong (JS/CSS text leaking into the narration),
extend `HTML_TAG_RE` in `scripts/generate_narration.py` to whitelist
the new tag before generating for real.

**Also check that the dry-run output reaches the post's closing
line** — every post has one, bolded, right before the `---`/Sources
divider (per CLAUDE.md's post-writing conventions), phrased as either
`**Why it matters today:**` or `**Where it fits in the bigger
story:**` (19 and 11 real posts respectively — both are valid, this
isn't a single fixed phrase). If neither shows up in the dry-run text,
extraction stopped early somewhere — this is exactly how a real bug
was caught (`extract_narrative()`'s HTML-depth tracker silently
swallowing everything after a Watch widget's script block, see section
13's gotchas). The reverse doesn't hold: seeing the closing line only
rules out *truncation*, it doesn't confirm the rest of the extraction
is otherwise correct.

**`--dry-run` also automatically scans for the "unknown word or
symbol" pronunciation-bug category** — see
`docs/pronunciation-fixes.md` for what that means — and prints a
`WARNING:` line naming every flagged sentence, or a clean "No unknown
words/symbols found" line if none. This is a real, near-instant check
(text only, no audio), not just a lint — it catches the exact class of
bug that would otherwise need a full listen-through to notice, and has
already found real cases (Ng, Fr., S$, Kuan, Yasukuni, rallied,
Siglap) before they ever reached synthesized audio. It does *not*
catch the other bug category (a confidently wrong existing
pronunciation, e.g. "stung"/"graves") — that one still needs a human
ear against the real render.

**Standard step whenever `--dry-run` flags a word (or a suspected
mispronunciation surfaces any other way): prepare candidate audio
samples in `scratch/` for Chris to ear-review before locking in a
fix.** Don't just commit a guessed phoneme override and move on — a
guessed reading of a place name or foreign word is wrong as often as
not (see the Malay-place-name batch in `docs/pronunciation-fixes.md`).
For each flagged word, synthesize 2-3 short samples of the actual
sentence it appears in, one per candidate reading, into
`scratch/<slug>-<word>/` (git-ignored) named so the reading is
obvious (e.g. `A_chah-ngee.wav`, `B_chan-jee.wav`,
`C_char-ngee-stress2.wav`). Put the current/leading candidate in the
code so `--dry-run` passes, mark it `# NOT ear-verified yet` in the
comment, and hand Chris the folder. He picks one by ear; then update
the override to the chosen reading and drop the "not verified" note.
This is [Claude]'s job as part of step 1, same as the video configs
in step 3.

Once the dry-run output looks right, generate for real (same command,
without `--dry-run`):

```
{ echo; date; echo "=== 1.2 Generate narration audio ==="
  cmd=(python scripts/generate_narration.py _posts/<file>.md audio/<slug>.mp3)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

Example:

```
{ echo; date; echo "=== 1.2 Generate narration audio ==="
  cmd=(python scripts/generate_narration.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

- Voice defaults to `bm_george` (British male) — this is the sitewide
  standard, don't override it unless explicitly asked to A/B test
  another voice.
- Synthesis runs sentences across a few worker processes by default
  (`--jobs`, default CPU count − 2 capped at 4; `--jobs 1` for a
  single process) and prints a dot per sentence so a long run visibly
  progresses. Each sentence's audio is cached in `.narration-cache/`
  keyed by its text + voice + the pronunciation overrides that touch
  it, so a re-run after a pronunciation fix only re-synthesizes the
  handful of changed sentences (seconds, not minutes) — the earlier
  rerun-the-whole-post cost is gone. `timing.json` / `.srt` are
  identical regardless of `--jobs`; the mp3 audio varies slightly run
  to run (Kokoro is not seeded), which the cache freezes. `--no-cache`
  forces a full re-synthesis.
- Output: `audio/<slug>.mp3`, `audio/<slug>.timing.json` (real
  per-sentence `{text, offset_s, duration_s}`, driven off Kokoro's own
  synthesis — not guessed even splits), and `audio/<slug>.srt` — the
  YouTube caption track (section 10). `_build_srt()` segments each
  narration sentence into ~2-line, ~5-6s cues at clause boundaries
  (checked against timedsubs.com's SRT QA rules), so the `.srt` is not
  one-sentence-per-cue and does **not** line up 1:1 with `timing.json`.
- Verify the file is real (not truncated) before moving on:
  ```
  { echo; date; echo "=== 1.3 Verify audio file ==="
    cmd=(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio/<slug>.mp3)
    echo "\$ ${cmd[*]}"; echo
    time "${cmd[@]}"
    echo
  } 2>&1 | tee -a logs/<slug>.log
  ```
  Example:
  ```
  { echo; date; echo "=== 1.3 Verify audio file ==="
    cmd=(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3)
    echo "\$ ${cmd[*]}"; echo
    time "${cmd[@]}"
    echo
  } 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
  ```
  Real output for this post — a ~5.5 minute post, so ~343s of audio is
  plausible, not a truncated file: `343.056000`.

  Should succeed with no error and print a duration that's plausible for
  the post's word count (a post with several minutes of prose should
  yield several minutes of audio, not a few seconds).
- **[FALLBACK — only if synthesis actually stalled/hung; skip entirely
  if the normal command above already succeeded]** If synthesis
  stalls/hangs on a specific post's text (a known occasional Kokoro
  issue), split the post's paragraphs into 2-8 pieces and synthesize
  each separately, then concatenate:
  ```
  { echo; date; echo "=== 1.4 [FALLBACK] Concatenate split narration ==="
    cmd=(ffmpeg -y -i "concat:part1.mp3|part2.mp3|..." -acodec copy audio/<slug>.mp3)
    echo "\$ ${cmd[*]}"; echo
    time "${cmd[@]}"
    echo
  } 2>&1 | tee -a logs/<slug>.log
  ```
  Example — note `part1.mp3`/`part2.mp3` here are placeholder pieces
  you'd have generated yourself while working around a stall, not real
  files that exist for every post; don't just swap in your own slug and
  run this if your synthesis completed normally the first time:
  ```
  { echo; date; echo "=== 1.4 [FALLBACK] Concatenate split narration ==="
    cmd=(ffmpeg -y -i "concat:jalan-payoh-lai-part1.mp3|jalan-payoh-lai-part2.mp3" -acodec copy audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3)
    echo "\$ ${cmd[*]}"; echo
    time "${cmd[@]}"
    echo
  } 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
  ```

---

## 2. Insert the Listen widget

```
{ echo; date; echo "=== 2. Insert the Listen widget ==="
  cmd=(python scripts/insert_listen_widget.py _posts/<file>.md <slug>)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example:**

```
{ echo; date; echo "=== 2. Insert the Listen widget ==="
  cmd=(python scripts/insert_listen_widget.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md jalan-payoh-lai-kangkar-montfort-nativity-church)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

Inserts the clickable headphones-icon widget right after the post's
first `[← Back to all posts](/)` link. Skips posts that already have
one. If the post is getting the full Watch widget too (section 4), the
Listen markup gets folded into that combined block anyway — running
this first is still fine, or skip straight to hand-authoring the
combined block below.

---

## 3. Write the video configs (main + Short)

**[Claude] — needs judgment, not just execution** (see section 0's
legend). If Claude is unavailable, this is the one step to leave
queued rather than attempt solo. Both the main video's config and the
Short's config get written here, in the same sitting — see section 0's
legend for why that matters.

Video rendering is driven by a **shared engine**,
`scripts/watch_video_lib.py`, with per-post data in
`scripts/video-configs/<slug>.py` (main video) and
`scripts/video-configs/<slug>-short.py` (Shorts). Never copy the engine
itself into a scratch/per-post script — that's exactly how a real
jerky-panning bug regressed in the past (a fix landed in one copy and
not the others). Only the config module is per-post.

**Main video config first:**

**Config module contract:**

```python
IMAGES = {
    "KEY": "https://upload.wikimedia.org/...",  # or "/assets/images/..." (site-root path)
                                                    # or a path relative to the config file's own dir
}

SLIDES = [
    {"img": "KEY", "type": "cover", "zoom": [z0, z1, z2], "pan": [(x0,y0), (x1,y1), (x2,y2)]},
    {"img": "KEY2", "type": "letterbox", "zoom": [...], "pan": [...]},
    # A "chart" slide instead has no img/zoom/pan - see CLAUDE.md's
    # Charts section and compose_chart_frame()'s docstring in
    # watch_video_lib.py for the {"type": "chart", "data": [...], ...}
    # contract, including year_checkpoints for narration-paced motion.
]

SCHEDULE = [(0.0, 0), (23.7, 1), ...]   # (absolute_time, slide_index) pairs - must match
                                          # the Watch widget's imageSchedule (section 4) by value
TOTAL_DURATION = 322.625                 # must match the Watch widget's TOTAL_DURATION
TIMING_JSON = "audio/<slug>.timing.json" # path relative to repo root

# Optional, default 1280x720x25:
WIDTH, HEIGHT, FPS = 1280, 720, 25

# Optional. Credit lines (keyed by IMAGES key) for slides whose image
# isn't a captioned Commons file - a chart PNG the site renders itself,
# say. scripts/stage_youtube_text.py uses these in the YouTube
# description instead of flagging the image [REVIEW CREDIT].
CREDITS = {"CHART": "Chart by Lesser Known Singapore, data: <source>"}
```

`pan` values here are `(x, y)` floats in 0-1 (fraction of image width/
height), **not** the `"50% 50%"` CSS strings the Watch widget's JS
uses for the same slide — same values, different literal syntax, keep
both in sync when you tune a slide's motion.

Write one `SLIDES`/`SCHEDULE` entry per image *appearance* (an image
can repeat with different zoom/pan for a bookend effect — two separate
entries pointing at the same `IMAGES` key). Aim for roughly 8-15s+ dwell
time per slide for an engaging pace; shorter bursts are fine for a
quick enumeration-style sentence.

Copy an existing config (e.g.
`scripts/video-configs/japans-quiet-hand-in-building-jurong.py`) as a
starting template rather than writing one from scratch.

**Example** (`scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py`
— this specific file doesn't exist yet, since this post's real,
published video predates the `scripts/video-configs/` system and was
built by an earlier per-post scratch script instead; shown here as a
worked example of what a config for it would look like, translated
directly from the real `slides`/`imageSchedule` data still sitting in
the post's own Watch-widget `<script>` block — the first 4 of its real
15 slides, trimmed for length):

```python
IMAGES = {
    "MAP": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Hougang_location.svg",
    "CHURCH_DAY": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary%2C_October_2025.jpg",
    "CHURCH_NIGHT": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary%2C_night%2C_July_2017.jpg",
    "CHURCH_INTERIOR": "https://upload.wikimedia.org/wikipedia/commons/1/1f/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary_5%2C_Nov_06.JPG",
    # ... 11 more keys for the remaining real slides (kampong houses,
    # Sungei Serangoon, Punggol Park, HDB blocks, the SMC map, a WP
    # rally crowd photo) - see the post's own <script> block for all 15.
}

SLIDES = [
    {"img": "MAP", "type": "cover", "zoom": [1, 1.08, 1.14], "pan": [(0.50, 0.40), (0.60, 0.55), (0.45, 0.65)]},
    # Slide 1 in the real post is a "route-walk" slide (Jalan Payoh Lai
    # to Montfort School, no photo exists for this demolished backlane)
    # - see CLAUDE.md's Route animations section for that slide type's
    # own {"type": "route-walk", "path": ..., "nodes": [...]} contract,
    # not shown here.
    {"img": "CHURCH_DAY", "type": "cover", "zoom": [1, 1.1, 1.18], "pan": [(0.45, 0.30), (0.55, 0.50), (0.65, 0.65)]},
    {"img": "CHURCH_NIGHT", "type": "cover", "zoom": [1.15, 1.06, 1], "pan": [(0.60, 0.30), (0.50, 0.50), (0.35, 0.65)]},
    {"img": "CHURCH_INTERIOR", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.40, 0.55), (0.52, 0.45), (0.62, 0.35)]},
    # ... remaining 11 slides
]

SCHEDULE = [
    (0.0, 0), (24.775, 1), (49.825, 2), (79.125, 3), (97.425, 4),
    (110.3, 5), (149.05, 6), (183.05, 7), (216.125, 8), (228.425, 9),
    (269.55, 10), (287.725, 11), (300.45, 12), (312.675, 13), (336.875, 14),
]  # real values from the published post's imageSchedule
TOTAL_DURATION = 361.125  # real value, matches the post's own TOTAL_DURATION
TIMING_JSON = "audio/jalan-payoh-lai-kangkar-montfort-nativity-church.timing.json"
```

Note this `361.125` won't match section 1's `343.056` example — they're two
different Kokoro narration runs for the same post. `361.125` is the
original narration behind the *live, already-published* video (what its
own widget script's `TOTAL_DURATION` says); `343.056` is a fresh re-run of
`generate_narration.py` against the post's current text, done later while
walking through section 1. A live post's original narration and a freshly
regenerated one for the same text won't line up to the second — that's
expected, not a sign either number is wrong.

**Now the Short's config, while still working from the same sentence
timings:**

Pick a self-contained excerpt — not a mid-sentence truncation. Look for
a real hook→payoff (→cliffhanger) arc in the real sentence timings: the
post's opening few sentences almost always work well (title hook
through the first strong beat). Write a second config,
`scripts/video-configs/<slug>-short.py`:

```python
WIDTH, HEIGHT = 1080, 1920

IMAGES = { "HERO": "..." }   # usually a subset of the main config's images

SLIDES = [
    {"img": "HERO", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5,0.5)]*3},
    # 2-3 slides is typical for a ~30-50s Short
]

SCHEDULE = [(0.0, 0), (16.2, 1), (32.4, 2)]
TOTAL_DURATION = 48.65          # the excerpt's own length, not the full post's
TIMING_JSON = "audio/<slug>.timing.json"

# Shorts keep burned-in captions (main videos don't, section 6); these
# size the box, smaller/higher than the landscape default:
BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
```

**Example** (`scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church-short.py`
— again illustrative, since this post's real, already-published Short
at `youtube.com/shorts/rVX4caKw0os` predates this config system; the
excerpt boundary below is a real one, though — the post's own sentence
timings put a clean beat right at 24.775s, "...took about twenty
minutes.", which is also where the real published video's first slide
transition already happens):

```python
WIDTH, HEIGHT = 1080, 1920

IMAGES = {
    "MAP": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Hougang_location.svg",
    "CHURCH_DAY": "https://upload.wikimedia.org/wikipedia/commons/a/a6/Church_of_the_Nativity_of_the_Blessed_Virgin_Mary%2C_October_2025.jpg",
}

SLIDES = [
    {"img": "MAP", "type": "letterbox", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3},
    {"img": "CHURCH_DAY", "type": "cover", "zoom": [1, 1.08, 1.15], "pan": [(0.5, 0.4), (0.5, 0.5), (0.5, 0.6)]},
]

SCHEDULE = [(0.0, 0), (12.4, 1)]
TOTAL_DURATION = 24.775  # real sentence-timing boundary for this post's opening hook
TIMING_JSON = "audio/jalan-payoh-lai-kangkar-montfort-nativity-church.timing.json"

BURN_CAPTIONS = True
CAPTION_FONT_RATIO = 0.032
CAPTION_MAX_WIDTH_FRAC = 0.86
CAPTION_Y_FRAC = 0.80
```

The exact same zoom/pan **percentage** values from a landscape slide
carry over unchanged to the vertical 1080x1920 target — cover-crop
normalizes to whatever `WIDTH`/`HEIGHT` is set, no per-image rework
needed. A landscape source used as `letterbox` in a vertical Short is
the one case worth a speed sanity-check (see
`LETTERBOX_WORK_SCALE` in `watch_video_lib.py`) — this was a real past
slowdown (~0.2fps), already fixed in the shared engine, but worth
knowing about if a future render looks unusually slow.

**Lint before moving on.** Both config files are Python, so run `ruff`
over them (config in `pyproject.toml`, see CLAUDE.md's *Python linting*
section):

```bash
ruff check scripts/video-configs/<slug>.py scripts/video-configs/<slug>-short.py
```

It must print `All checks passed!` — fix anything it flags before
section 4. If this step also had you write a static-chart renderer
(`scripts/render_<slug>_*.py`, per CLAUDE.md's *Charts* section) or edit
`scripts/generate_narration.py` for a pronunciation override, lint those
too — or just run `ruff check .` from the repo root to cover everything
at once. The rule set is a bug-catching net only (pyflakes, syntax,
import/statement footguns); it does not enforce formatting, so match the
surrounding style by reading it.

---

## 4. Author the Watch widget (live in-browser slideshow)

`scripts/build_watch_widget.py` generates the widget FROM the video
config written in section 3 (translating Python pan tuples to CSS
percentage strings, SCHEDULE to imageSchedule, pasting in the real
sentences from TIMING_JSON) - write that config first if you haven't.

```
{ echo; date; echo "=== 4. Author the Watch widget ==="
  cmd=(python scripts/build_watch_widget.py _posts/<file>.md scripts/video-configs/<slug>.py)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example:**

```
{ echo; date; echo "=== 4. Author the Watch widget ==="
  cmd=(python scripts/build_watch_widget.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

- **Safe to re-run** — the generated block is wrapped in
  `<!-- WATCH-WIDGET:BEGIN -->`/`END` marker comments; a second run
  replaces the block in place (e.g. to add the YouTube/Shorts URLs
  once they exist) rather than duplicating it. Re-running with only a
  new `--youtube-url` (no `--shorts-url`) keeps a previously-set Shorts
  URL — it reads whichever links are already in the post before
  regenerating, so a partial re-run never blanks the other button.
- **First run on a post that already has the site-wide bare Listen
  widget** (every post does, from the original rollout) upgrades it
  in place — this is the normal, expected case, not something to work
  around by deleting the Listen widget by hand first.
- **Chart slides are auto-generated** — a `{"type": "chart", ...}`
  config entry becomes a full JS chart object plus the generic
  `buildChartSlide()` SVG library, translated straight from the config
  (including a Python-format-string → JS-formatter converter for
  `y_tick_format`/`value_format`). A re-run regenerates it cleanly, so
  there's nothing to re-apply after section 11. A chart whose format
  strings the converter can't handle falls back to a `/* MANUAL: ... */`
  placeholder rather than emitting broken JS.
- **Route-walk slides still aren't auto-generated** — their JS is more
  bespoke; they get the `/* MANUAL: ... */` placeholder and need hand
  authoring per CLAUDE.md's Route animations section. The script reports
  the count of such slides on exit.
- **Refuses rather than guesses** if the post already has a full Watch
  widget that wasn't generated by this script (no marker comments) —
  that widget may carry real hand-tuned data (published URLs, tuned
  pan/zoom) this script can't safely tell apart from something stale.
  Remove it by hand first, or add the marker comments yourself.
- **Give a new slide a real `"ease"` value in the config, not just
  `zoom`/`pan`** — the Python contract has always allowed an optional
  per-slide `"ease"` key (`"ease-in"`/`"ease-out"`/`"ease-in-out"`/
  `"linear"`, see CLAUDE.md's Motion variety note), but it's easy to
  forget since `watch_video_lib.py`'s renderer ignores it. Skipping it
  isn't a bug — the script just defaults to `"ease-in-out"` for every
  slide — but it does lose the deliberate motion variety a hand-tuned
  mix gives the finished widget. All 6 existing configs' real ease
  values were audited and backfilled (see below); keep doing this for
  new slides going forward.

Verify locally (`jekyll serve`, see CLAUDE.md's intro) after running
it: click Watch, confirm the image/caption/progress bar all advance
with zero console errors. This class of bug (a variable valid in one
`<script>` block's scope but not the other) only surfaces by actually
running the page — the generator removes the most common instance of
it by construction (see the gotchas in section 13), but still verify.

The rest of this section shows exactly what the script generates — useful
for understanding the output, or as a hand-authoring fallback for a
route-walk slide the script flagged (charts are auto-generated). Copy
it from an existing post with one (e.g.
`_posts/2026-07-28-japans-quiet-hand-in-building-jurong.md`) rather
than retyping from memory if you ever do need to hand-edit.

**Audited against all 10 posts that already have real, published
widgets** (regenerate + diff against the live markup, nothing written
to the actual posts) — every remaining difference is cosmetic (JS
formatting style, auto-generated vs. hand-picked gradient IDs, JSON
key spacing, trailing commas) or the one documented, by-design
exception (a chart/route-walk slide's flagged placeholder). No
functional bugs remain, but two real ones were caught and fixed along
the way — worth knowing about since they were subtle:
- **Lost per-slide `ease` variety** — the generator defaulted every
  slide to `"ease-in-out"` since none of the 6 originally-config'd
  posts populated the (always-optional) `"ease"` key. Fixed by
  backfilling real values into all 10 configs.
- **Wrong/OS-broken `<audio>` source path** — the generator derived
  the audio filename from the config's slug, but a post that was
  A/B-tested between TTS engines can have a differently-suffixed
  canonical audio file (two of the 4 older posts really do). Fixed by
  deriving it from `TIMING_JSON` instead (matches
  `watch_video_lib.py`'s own `render()`); a first attempt at that fix
  used `pathlib.Path`, which renders backslashes on Windows and broke
  the path a different way - fixed with plain string manipulation.

Six of the ten configs (Jurong, HDB, Bugis Street, Japanese Cemetery
Park, Syonan Jinja, Victoria Memorial Hall) were authored fresh through
the normal section-4 workflow. The other four (Fort Canning, Merlion,
Jalan Payoh Lai/Kangkar, Lim Kim San) predate `scripts/video-configs/`
entirely — their configs were reverse-engineered from each post's own
already-published widget script, which is also how a real bug in that
process got caught: an auto-derived `IMAGES` key from a Commons
filename starting with a digit produced invalid JS (`var 2005... =
...;`) that only Python's dict syntax tolerated. Fixed the one real
occurrence and added a defensive check in `build_watch_script()` so an
invalid key fails loudly at generation time instead of shipping.

**Row markup** (place right after the first back-link, replacing a
bare Listen-only widget if one exists):

```html
<div style="display: flex; gap: 2em; margin: 0.5em 0 1.5em 0; align-items: flex-end;">
  <div id="listen-widget" role="button" tabindex="0" aria-label="Play audio narration of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; user-select: none;">
    <span id="listen-icon" aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.1em; height: 2.1em; border-radius: 50%; border: 1px solid #888; font-size: 1.1em;">&#127911;</span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Listen</span>
  </div>
  <div id="watch-widget" role="button" tabindex="0" aria-label="Watch an animated version of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; user-select: none;">
    <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.1em; height: 2.1em; border-radius: 50%; border: 1px solid #888; font-size: 1.1em;">&#127916;</span>
    <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Watch</span>
  </div>
  <!-- YouTube and Shorts buttons get added in section 11, once URLs exist -->
</div>

<audio id="listen-audio" preload="none" style="display: none;">
  <source src="/audio/<slug>.mp3" type="audio/mpeg">
</audio>

<div id="watch-viewer" style="position: fixed; inset: 0; background: #000; z-index: 9999; display: none;">
  <div id="watch-stage" style="position: absolute; inset: 0; overflow: hidden;"></div>
  <div style="position: absolute; left: 0; right: 0; bottom: 12%; text-align: center; padding: 0 5%; z-index: 2;">
    <span id="watch-caption" style="display: inline-block; background: rgba(0,0,0,0.55); color: #fff; font-size: 1.3em; font-weight: 600; padding: 0.5em 0.8em; border-radius: 4px; max-width: 700px;"></span>
  </div>
  <button id="watch-close" aria-label="Close" style="position: absolute; top: 1em; right: 1.2em; color: #fff; font-size: 1.6em; cursor: pointer; background: none; border: none; z-index: 2;">&times;</button>
  <div style="position: absolute; bottom: 0; left: 0; right: 0; padding: 1em 1.5em; display: flex; align-items: center; gap: 1em; background: linear-gradient(transparent, rgba(0,0,0,0.6)); z-index: 2;">
    <button id="watch-play" aria-label="Play/Pause" style="background: none; border: none; color: #fff; font-size: 1.4em; cursor: pointer; line-height: 1; padding: 0.2em;">&#10074;&#10074;</button>
    <div id="watch-progress" style="flex: 1; height: 4px; background: rgba(255,255,255,0.25); border-radius: 2px; overflow: hidden; cursor: pointer;">
      <div id="watch-progress-fill" style="height: 100%; width: 0%; background: #fff;"></div>
    </div>
    <span id="watch-time" style="color: #fff; font-size: 0.85em; font-variant-numeric: tabular-nums; opacity: 0.8;">0:00 / 0:00</span>
  </div>
</div>
```

**Listen script** (this block never changes between posts — copy
verbatim):

```html
<script>
(function () {
  var widget = document.getElementById('listen-widget');
  var icon = document.getElementById('listen-icon');
  var audio = document.getElementById('listen-audio');

  function setIcon(playing) {
    icon.innerHTML = playing ? '&#10074;&#10074;' : '&#127911;';
  }
  function toggle() {
    if (audio.paused) { audio.play(); } else { audio.pause(); }
  }

  widget.addEventListener('click', toggle);
  widget.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
  });
  audio.addEventListener('play', function () { setIcon(true); });
  audio.addEventListener('pause', function () { setIcon(false); });
  audio.addEventListener('ended', function () { setIcon(false); });
})();
</script>
```

**Watch script** — this is the part that needs real per-post
authoring. Skeleton (fill in the placeholders):

```html
<script>
(function () {
  // One `var NAME = "url";` per image used in the video, same keys as
  // the video config's IMAGES dict (section 3) so the two stay easy to
  // cross-reference.
  var HERO = "https://upload.wikimedia.org/...";

  // One entry per slide appearance (an image can repeat with different
  // zoom/pan for a bookend effect - see section 3's SLIDES contract).
  // pan values are CSS background-position strings ("50% 50%"), NOT the
  // 0-1 floats the Python video config uses for the same slide - the
  // two are written in different formats by design, keep them in sync
  // by value, not by literal syntax.
  var slides = [
    { src: HERO, type: "cover", zoom: [1, 1.08, 1.15], pan: ["50% 45%", "50% 50%", "50% 55%"], ease: "ease-in-out" }
    // ...
  ];

  // Paste the *exact* array from audio/<slug>.timing.json here verbatim
  // (it's already valid JS array-of-objects syntax).
  var sentences = [{"text":"...", "offset_s":0.0, "duration_s":3.6}, /* ... */];

  // Long-sentence caption chunker - copy verbatim, do not rewrite.
  var MAX_CHARS = 100;
  function splitLongSentence(text, offset, duration) {
    if (text.length <= MAX_CHARS) return [{ text: text, offset_s: offset, duration_s: duration }];
    var parts = text.split(/(?<=[:;])\s+/);
    var chunks = [];
    parts.forEach(function (p) {
      if (p.length <= MAX_CHARS) { chunks.push(p); return; }
      var words = p.split(' ');
      var cur = '';
      words.forEach(function (w) {
        if ((cur + ' ' + w).trim().length > MAX_CHARS) { chunks.push(cur.trim()); cur = w; }
        else { cur = (cur + ' ' + w).trim(); }
      });
      if (cur) chunks.push(cur.trim());
    });
    var totalChars = chunks.reduce(function (a, c) { return a + c.length; }, 0);
    var t = offset;
    return chunks.map(function (c) {
      var share = duration * (c.length / totalChars);
      var entry = { text: c, offset_s: t, duration_s: share };
      t += share;
      return entry;
    });
  }
  var captionChunks = [];
  sentences.forEach(function (s) {
    captionChunks = captionChunks.concat(splitLongSentence(s.text, s.offset_s, s.duration_s));
  });

  // Hand-mapped {t, slide} pairs - one per SLIDES entry, t = the real
  // sentence offset (from timing.json) where that image should appear.
  // This is the one genuinely manual step: read the sentence timings,
  // decide which image best represents each narrative beat, pick cut
  // points. Must match the Python config's SCHEDULE (section 3) exactly
  // in timing (same values, different variable name/shape).
  var imageSchedule = [
    { t: 0, slide: 0 } /* ... */
  ];
  var TOTAL_DURATION = 0; // total narration length in seconds

  var slideDurations = imageSchedule.map(function (entry, i) {
    var next = imageSchedule[i + 1];
    return (next ? next.t : TOTAL_DURATION) - entry.t;
  });

  var viewer = document.getElementById('watch-viewer');
  var stage = document.getElementById('watch-stage');
  var captionEl = document.getElementById('watch-caption');
  var closeBtn = document.getElementById('watch-close');
  var playBtn = document.getElementById('watch-play');
  var progress = document.getElementById('watch-progress');
  var progressFill = document.getElementById('watch-progress-fill');
  var timeEl = document.getElementById('watch-time');
  var watchWidget = document.getElementById('watch-widget');

  // CRITICAL: use a SEPARATE Audio object from the Listen widget's
  // <audio> element, never the same `audio` variable - the two IIFEs
  // are separate scopes, so referencing Listen's `audio` from here
  // throws ReferenceError and the viewer opens black with nothing
  // populated. Also deliberate: keeps Listen/Watch playback state from
  // interfering with each other.
  var listenAudio = document.getElementById('listen-audio');
  var watchAudio = new Audio(listenAudio.querySelector('source').src);
  watchAudio.preload = 'none';

  var styleEl = document.createElement('style');
  document.head.appendChild(styleEl);

  var slideEls = slides.map(function (s, i) {
    var el = document.createElement('div');
    el.style.cssText = 'position:absolute;inset:0;opacity:0;transition:opacity 0.8s ease;';
    var ease = s.ease || 'linear';
    var dur = slideDurations[imageSchedule.findIndex(function (e) { return e.slide === i; })];

    if (s.type === 'letterbox') {
      var bg = document.createElement('div');
      bg.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-position:center;filter:blur(30px) brightness(0.55);background-image:url(\'' + s.src + '\');';
      bg.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      var fg = document.createElement('div');
      fg.style.cssText = 'position:absolute;inset:6%;background-size:contain;background-position:center;background-repeat:no-repeat;background-image:url(\'' + s.src + '\');';
      el.appendChild(bg); el.appendChild(fg);
      el._animTargets = [bg]; // only the blurred background animates - foreground stays static/centered
    } else {
      var layer = document.createElement('div');
      layer.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-image:url(\'' + s.src + '\');';
      layer.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      el.appendChild(layer);
      el._animTargets = [layer];
    }
    styleEl.textContent += '@keyframes kb' + i + ' { 0% { transform: scale(' + s.zoom[0] + '); background-position: ' + s.pan[0] + '; } 50% { transform: scale(' + s.zoom[1] + '); background-position: ' + s.pan[1] + '; } 100% { transform: scale(' + s.zoom[2] + '); background-position: ' + s.pan[2] + '; } }\n';
    stage.appendChild(el);
    return el;
  });
  slides.forEach(function (s) { var img = new Image(); img.src = s.src; });

  var currentIndex = -1, currentSentenceIndex = -1;
  function fmtTime(t) {
    if (!isFinite(t)) return '0:00';
    var m = Math.floor(t / 60), s = Math.floor(t % 60);
    return m + ':' + (s < 10 ? '0' : '') + s;
  }
  function slideIndexForTime(t) {
    var idx = 0;
    for (var i = 0; i < imageSchedule.length; i++) { if (imageSchedule[i].t <= t) idx = imageSchedule[i].slide; else break; }
    return idx;
  }
  function sentenceIndexForTime(t) {
    var idx = 0;
    for (var i = 0; i < captionChunks.length; i++) { if (captionChunks[i].offset_s <= t) idx = i; else break; }
    return idx;
  }
  function updateForTime(t) {
    var sIdx = slideIndexForTime(t);
    if (sIdx !== currentIndex) {
      if (currentIndex >= 0) slideEls[currentIndex].style.opacity = '0';
      slideEls[sIdx].style.opacity = '1';
      currentIndex = sIdx;
    }
    var cIdx = sentenceIndexForTime(t);
    if (cIdx !== currentSentenceIndex) { captionEl.textContent = captionChunks[cIdx].text; currentSentenceIndex = cIdx; }
    var pct = Math.min(100, (t / TOTAL_DURATION) * 100);
    progressFill.style.width = pct + '%';
    timeEl.textContent = fmtTime(t) + ' / ' + fmtTime(TOTAL_DURATION);
  }
  function openViewer() {
    viewer.style.display = 'block';
    currentIndex = -1; currentSentenceIndex = -1;
    slideEls.forEach(function (el) { el.style.opacity = '0'; });
    watchAudio.currentTime = 0;
    updateForTime(0);
    watchAudio.play();
  }
  function closeViewer() { viewer.style.display = 'none'; watchAudio.pause(); }

  watchWidget.addEventListener('click', openViewer);
  watchWidget.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openViewer(); } });
  closeBtn.addEventListener('click', closeViewer);
  playBtn.addEventListener('click', function () { if (watchAudio.paused) watchAudio.play(); else watchAudio.pause(); });
  watchAudio.addEventListener('play', function () { playBtn.innerHTML = '&#10074;&#10074;'; });
  watchAudio.addEventListener('pause', function () { playBtn.innerHTML = '&#9654;'; });
  watchAudio.addEventListener('timeupdate', function () { updateForTime(watchAudio.currentTime); });
  watchAudio.addEventListener('ended', closeViewer);
  progress.addEventListener('click', function (e) {
    var rect = progress.getBoundingClientRect();
    var pct = (e.clientX - rect.left) / rect.width;
    watchAudio.currentTime = pct * TOTAL_DURATION;
  });
})();
</script>
```

**Slide type rule of thumb:** use `cover` (pan/zoom crop, fills the
frame) when the source image's aspect ratio is reasonably close to the
target (16:9 for the main widget). Use `letterbox` (blurred cover
background + sharp static contained foreground) whenever a source
diverges substantially from that — most commonly a portrait-oriented
photo in the landscape widget. A `cover` crop forced onto a narrow
portrait produces an unusable extreme close-up (verified concretely on
the Lim Kim San post: a 448×733 portrait at `cover` came out as a
grainy forehead-and-eyes crop). Check the actual aspect ratio numbers
against the actual target frame each time — don't just eyeball "is this
a portrait photo."

For a chart-driven post or a route-walk slide (no photo available for a
demolished/unmapped place), see CLAUDE.md's **Charts** and **Route
animations** sections — those slide types have their own dedicated
build process and are cross-referenced from the video config contract
in section 3 above.

Verify locally (`jekyll serve`, see CLAUDE.md's intro) before pushing:
click Watch, confirm the image/caption/progress bar all advance with
zero console errors. This class of bug (a variable valid in one
`<script>` block's scope but not the other) only surfaces by actually
running the page — static review won't catch it.

---

## 5. Check smoothness and review the gap report

Before committing to a full render (a few minutes on a many-core
machine, longer on fewer cores), run the cheap pre-check:

```
{ echo; date; echo "=== 5. Check smoothness and review the gap report ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --check-only)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example:**

```
{ echo; date; echo "=== 5. Check smoothness and review the gap report ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --check-only)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

This does two things, both instantly (no rendering of the real video):

1. **Gap report** — writes `docs/video-gaps/<slug>-gap.txt`, flagging
   any slide held on screen longer than 30 seconds, with the actual
   narration text spoken during that stretch (pulled straight from
   `audio/<slug>.timing.json`). Review this file and consider whether
   any flagged section needs another image before finalizing — it
   always writes, even with zero gaps ("No slide held longer than
   30s."), so a later re-render that fixes a gap shows a real diff.
2. **Smoothness check** — renders ~4s of test frames per slide through
   the real frame-compose code path and flags any slide where
   consecutive frames go near-identical for 2+ frames in a row
   (JERKY). **Known false positives, not bugs:** a `letterbox` slide
   with zero pan (foreground pinned) always reads JERKY because the
   static foreground dominates the pixel-diff metric regardless of how
   smoothly the blurred background is actually moving; a `chart` slide
   reads JERKY for the same reason (mostly-static gridlines/background
   dominate the frame). Real jerkiness only shows up on `cover`-type
   slides or any slide with genuine pan movement — don't block a
   render on the two false-positive cases above, but do treat a JERKY
   `cover` slide as a real problem to fix (usually means too little
   supersampling headroom for that slide's pan distance/duration —
   see `WORK_SCALE`/`LETTERBOX_WORK_SCALE` at the top of
   `watch_video_lib.py` if this ever needs deeper investigation).

---

## 6. Render the main video

**The main video has no burned-in captions** (changed 2026-09). The
render engine skips the on-frame caption; viewers get YouTube's
auto-captions, or the uploaded `audio/<slug>.srt` when a post warrants
it (see section 10). The `.srt` is still generated in section 1 and
committed in section 12 regardless, so it's there when needed.
**Shorts keep burned-in captions** — every `-short.py` config sets
`BURN_CAPTIONS = True` (muted autoplay, and a `.srt` upload to a Short
is unreliable). The module default in `watch_video_lib.py` is `False`,
so a landscape config needs no flag. Chart PNGs no longer have to keep
their bottom third clear for a burned caption, though a small bottom
margin is still worth leaving for YouTube's own caption overlay (see
CLAUDE.md Charts).

A full render composes frames across CPU cores (a `multiprocessing`
pool) and pipes raw RGB into a single ffmpeg encode; it takes roughly
4-6 minutes for a 5-6 minute video on a many-core machine. `--jobs N`
tunes the worker count (default: CPU count - 2, capped at 10); `--jobs
1` forces the old single-process path. Output is byte-identical
regardless of `--jobs`. Lower it if a cover-heavy post (many slides at
`WORK_SCALE=4`) makes the machine swap — each worker holds its own
prepared-image cache.

**Running it yourself, in your own terminal** — the normal case — just
run the plain form and let it tie up that window for the few minutes it
takes; it streams progress live and tees into the log as it goes, so
there's nothing to poll:

```
{ echo; date; echo "=== 6. Render the main video ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --out preview-motion/<slug>.mp4)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example:**

```
{ echo; date; echo "=== 6. Render the main video ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --out preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church.mp4)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

**Detached, via PowerShell `Start-Process`** — since parallel
rendering brought a full main video under ~5 minutes on a many-core
machine, a plain foreground call usually finishes inside Claude's
10-minute tool timeout; reach for `Start-Process` only when a render
actually runs long (fewer cores, a Short at 1080x1920, `--jobs 1`).
When it might: run it detached, never as a plain foreground call and
never via `run_in_background` (both are capped at that 10-minute tool
timeout — `run_in_background` doesn't bypass it, it just unblocks
Claude's turn — and the render gets silently killed mid-flight; a
half-dead render has already cost a wasted restart). That cap is
specific to Claude's own tool invocations — a human-run terminal has
no such limit, and a "stuck at 10 minutes" symptom there points at
something else (a crash, the window closing, the machine sleeping).
It's also handy in your own terminal if you'd rather not tie up the
window — it detaches the render so it survives the window closing:

```powershell
# 6. Render the main video
Start-Process -FilePath python -ArgumentList "scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --out preview-motion/<slug>.mp4" -WindowStyle Hidden -RedirectStandardOutput preview-motion/<slug>-render.log -RedirectStandardError preview-motion/<slug>-render.err
```

**Example:**

```powershell
# 6. Render the main video
Start-Process -FilePath python -ArgumentList "scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --out preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church.mp4" -WindowStyle Hidden -RedirectStandardOutput preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church-render.log -RedirectStandardError preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church-render.err
```

The command inside `-ArgumentList` is the same one `watch_video_lib.py`
always takes — only the detach-and-redirect wrapper differs. When
detached, poll progress with `tail -n 20
preview-motion/<slug>-render.log` (PowerShell: `Get-Content ... -Tail
20`) or by checking whether the python process is still alive — don't
kill it just because the output file's size looks flat between two
checks a few minutes apart; ffmpeg's writes are bursty, and a false
"stall" diagnosis has cost a wasted re-render before. Look for an
actual completion signal (`Wrote <path>` in the log, or the process
genuinely gone) before concluding it's stuck.

`preview-motion/` is untracked scratch (confirmed via `git log --all --
"*.mp4"` — never committed) — the blog embeds YouTube links, not local
video files, so nothing here needs to go in git except the config
scripts and gap reports that produced it.

---

## 7. Render the YouTube Short

**[Manual]** — the `-short.py` config should already exist from section
3. If it doesn't (e.g. you're resuming a post where only the main
config was written), go back and write it there first rather than
improvising it here — picking the excerpt is a judgment call, not a
mechanical part of this step.

Run the same `--check-only` then render commands as sections 5-6, but
**pointing at the `-short.py` config, not the main one** — same
`watch_video_lib.py` invocation, different config file — and a
`preview-motion/<slug>-short.mp4` output path (Shorts are short enough
to usually finish within the 10-minute tool timeout, but the
`Start-Process` pattern is still safe to use):

```
{ echo; date; echo "=== 7.1 Check smoothness (Short) ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/<slug>-short.py --check-only)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
{ echo; date; echo "=== 7.2 Render the Short ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/<slug>-short.py --out preview-motion/<slug>-short.mp4)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example** (note the `-short` suffix on the config path in both lines
below — it's easy to instead reuse the main `<slug>.py` config out of
habit from sections 5-6, which silently renders the full-length video
again instead of the Short):

```
{ echo; date; echo "=== 7.1 Check smoothness (Short) ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church-short.py --check-only)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
{ echo; date; echo "=== 7.2 Render the Short ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church-short.py --out preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church-short.mp4)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

---

## 8. Verify both files

Don't trust that a render "looks done" — verify:

```
{ echo; date; echo "=== 8.1 Verify frame count ==="
  cmd=(ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 preview-motion/<slug>.mp4)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

Example:

```
{ echo; date; echo "=== 8.1 Verify frame count ==="
  cmd=(ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church.mp4)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

Compare against the expected frame count, `TOTAL_DURATION * FPS`
(e.g. `322.625 * 25 = 8065.625` → expect `8066`, off-by-one from
rounding is fine; for this post, `361.125 * 25 = 9028.125` → expect
`9028` or `9029`). This is a **full decode**, not a spot-check — if the
video ever needs trimming/concatenation with ffmpeg's `-c copy` path, a
full-decode verify is mandatory (a real past bug: non-monotonic source
DTS silently truncated the video track during a trim+concat, completely
undetectable by spot-check frame extraction alone). Then eyeball one
rendered frame against what the config says should be there —
`--spot-frame` picks the timestamp, pulls the frame out of the `.mp4`,
and prints the slide's image key plus the exact narration line playing
at that instant, so there's nothing to construct by hand:

```
{ echo; date; echo "=== 8.2 Verify spot frame ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --spot-frame)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

Example:

```
{ echo; date; echo "=== 8.2 Verify spot frame ==="
  cmd=(python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --spot-frame)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

It defaults to **slide 2** — slide 0 is usually the hero / front-matter
image (already vetted), so the first ordinary content slide is the best
canary for a stale `timing.json`, a wrong `IMAGES` url, or an
off-by-one in `SCHEDULE`. It writes `preview-motion/<slug>-spot-slide2.png`
and prints a line like:

```
slide 2  |  t=110.3s  (on screen 97.4-149.1s)  |  CHURCH_EXTERIOR (cover)
  narration then: "Montfort School opened on the site in 1916 ..."
```

Claude opens that PNG during the pre-upload log review (the Read tool
renders images) and confirms it's the right image for that narration
line — the frame is just the Ken Burns image, captions are no longer
burned in. Pass `--slide 5` (or `--slide 2,5,9` for several, e.g. ones
a review flagged) to check other slides; a `-short.py` config
automatically reads `preview-motion/<slug>-short.mp4`.

---

## 9. Stage the YouTube upload text file

Generate the draft with `scripts/stage_youtube_text.py`:

```
{ echo; date; echo "=== 9. Stage the YouTube upload text file ==="
  cmd=(python scripts/stage_youtube_text.py
      _posts/<file>.md
      scripts/video-configs/<slug>.py
      scripts/video-configs/<slug>-short.py
      --post-url https://pikaia.github.io/YYYY/MM/DD/<slug>/)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example** (same running-example slug as every other section, so a
global find-replace of `jalan-payoh-lai-kangkar-montfort-nativity-church`
→ your post's slug produces the command as-is — with both video-config
paths, which is the normal case; **without** them the script can't
build the real per-image credit list and drops in a "no video built
yet" placeholder instead):

```
{ echo; date; echo "=== 9. Stage the YouTube upload text file ==="
  cmd=(python scripts/stage_youtube_text.py
      _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md
      scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py
      scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church-short.py
      --post-url https://pikaia.github.io/2026/08/15/jalan-payoh-lai-kangkar-montfort-nativity-church/)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

(The Kangkar post itself has no `scripts/video-configs/` file — its
published video predates the config system, per section 3's note — so
its own real run drops those two lines and adds `--out ...`. For a post
whose video already exists, the script reads the YouTube links straight
out of the widget markup and reports "already published at
`https://youtu.be/...`, predates the pipeline" rather than the "no
video built yet" placeholder.)

For that Kangkar run the script detected both existing YouTube links in
the post's own widget markup and reported "video already published at
`https://youtu.be/GTIpKWDZBNA`, but predates the
`scripts/video-configs/` pipeline" — not the generic "no video built
yet" placeholder it shows for a post with no video at all.

It writes `docs/youtube_helper/<slug>-youtube.txt` (override with
`--out`) — unlike `preview-motion/`, this folder is git-tracked, so
these drafts keep real history — with both `=== FULL VIDEO ===` and
`=== SHORT ===` sections, assembled from data already sitting in the
repo:

- **Title** — the post's front-matter `title`.
- **Description hook** — the post's own opening paragraph (the first
  block after the front matter), markdown-cleaned.
- **`Full story:` link** — shortened automatically via da.gd (see
  below).
- **Narration credit** — fixed template line, `--voice` overrides the
  `bm_george` default if a post used a different voice.
- **Images list** — derived from the *actual* `IMAGES`/`SLIDES` used in
  each video config (main vs. Short get separate, correctly-scoped
  lists), each image's author/license pulled from its own caption in
  the post (or the gallery page, if the image only appears there).
- **Sources** — copied straight from the post's own `**Sources:**`
  section (full video only; the Short doesn't get one).
- **`Full-length video:` placeholder** — left as `<paste the main
  video's URL here after uploading it>`, same as before; there's no
  way to know this before the main video is actually uploaded.

**This is a draft, not guaranteed publish-ready copy** — skim it before
pasting into Studio, especially any line ending in `[REVIEW CREDIT]`.
Caption phrasing isn't 100% consistent across older posts ("(Photo: X /
Y, LICENSE)" vs "Photo by X, licensed under LICENSE." are both in use,
plus some captions don't follow either pattern), so the credit-line
extraction is best-effort regex, not a guarantee — a flagged line just
means the script fell back to a looser extraction and wants a human
glance, not that anything is necessarily wrong.

**Before shortening, double-check the post's actual live permalink**
via `sitemap.xml` (`http://127.0.0.1:4000/sitemap.xml` locally, or the
real production sitemap) and pass that as `--post-url` — don't assume
it from the filename. A post timestamped before 08:00 SGT can build one
calendar day earlier than the filename date, on both local preview and
the real GitHub Pages UTC build.

**Shortening** happens automatically via da.gd inside the script
(`--shortener dagd`, the default) — a raw `pikaia.github.io` URL has
repeatedly hit a real YouTube-side rendering bug where the description
truncates mid-URL even after expanding "...more", so this step isn't
optional. da.gd's click-through interstitial (a one-click "this link
was created recently" gate on fresh links) is the least confusing of
the options tried and is the settled default. The script retries 3
times before giving up; if da.gd is down, pass `--shortener tinyurl`
(`curl "https://tinyurl.com/api-create.php?url=<urlencoded-url>"` is
the equivalent manual fallback — e.g.
`curl "https://tinyurl.com/api-create.php?url=https%3A%2F%2Fpikaia.github.io%2F2026%2F08%2F15%2Fjalan-payoh-lai-kangkar-montfort-nativity-church%2F"`)
— but don't switch over a single blip.
is.gd/v.gd outright refuse to shorten any `pikaia.github.io` URL
(domain-level block, not worth trying).

If the script's output for a post looks wrong in a way worth fixing
generally (a new caption phrasing pattern it doesn't recognize, a new
image layout convention), fix the parser in
`scripts/stage_youtube_text.py` rather than hand-editing just that
post's output — the whole point is that this stays generic across
posts.

---

## 10. Upload to YouTube

**Division of labor:** the human does the two irreversible/manual
steps — the file-select click (native OS picker) and the final
Publish click — pasting straight from the staged text file above for
everything else. This is the default flow; there is no need for
Claude/browser-automation to drive Studio directly unless the file is
small enough to fit the automation tool's 10MB cap and a hands-off
upload is specifically wanted.

**Channel:** "Lesser Known Singapore" (studio.youtube.com — confirm
you're on the right channel, top-left of Studio, before uploading).

**Settings, every upload:**
- Visibility: **Public**
- Not made for kids
- Category: **Education**
- Comments/moderation: leave at YouTube's defaults
- **Captions (main video):** captions are no longer burned into the
  file. YouTube's auto-captions are fine for most posts — leave them
  on and move on. Upload `audio/<slug>.srt` as the subtitle track only
  when a post leans on exact wording or a lot of names/foreign terms
  the auto-captioner will mangle: Studio → the video's **Subtitles**
  tab → Add language (English), **let that selection settle** (don't
  upload into the same click — that has raced YouTube's state and
  failed), then → **Upload file** → "With timing" → pick the `.srt`,
  before Publish or from the edit page afterwards. Wait for the
  "Subtitle published" toast. The `.srt` is UTF-8 with a BOM; if an
  upload errors out, the video is usually still processing — retry
  once it finishes.
- **Captions (Short):** nothing to do. The Short already carries
  burned-in captions for the muted-autoplay scroll, and there is no
  Short-scoped `.srt` (it would need to be just the first few cues,
  re-timed from zero). Studio *does* accept a subtitle upload on a
  Short if you ever want one, but it would only show on caption-toggle
  and would double up with the burned text — so skip it.

**Shorts note:** YouTube auto-detects a Short from aspect ratio +
duration, no explicit toggle — confirm the upload dialog's link field
shows `youtube.com/shorts/...` once recognized. Shorts don't appear
under Channel Content's "Videos" tab, only under the separate "Shorts"
tab — check there (or the Short's own edit page) to confirm publish
status and grab the video ID. Typing `#Shorts` into the title or
description triggers a hashtag-autocomplete dropdown — dismiss it with
Escape before clicking elsewhere, but only if a dropdown is actually
visible (Escape with no dropdown open can close the entire upload
dialog instead — screenshot/check first).

**No in-place replace exists.** If a video needs updating later,
there's no "swap the file, keep the URL" option on this channel — it's
always delete-old + upload-new, which changes the URL. Update the
post's widget links (section 11) whenever this happens.

There's no dedicated "AI-generated/altered content" disclosure toggle
that's been found to reliably apply to these uploads (synthetic
voiceover without synthetic imagery) — not chased further unless it
resurfaces in a changed upload UI.

---

## 11. Wire the published URLs into the post

**The easiest path is re-running section 4's script** with
`--youtube-url`/`--shorts-url` now that both are known — it replaces
the whole widget block in place (safe, idempotent) and adds the row's
YouTube/Shorts buttons as part of that, so the manual markup edit below
is now a fallback, not the default: use it only when hand-patching a
widget the script didn't generate (no marker comments), or when only
adding the two buttons without wanting to touch anything else the
script would also regenerate.

**If the post has a hand-authored `route-walk` slide** (the `MANUAL:`
case from section 4 — charts are auto-generated now and survive a
re-run), that re-run wipes it: the script regenerates the whole block
from the config and only knows how to emit the placeholder. So for a
route-walk post, do the URL re-run *first*, then re-apply the
hand-authored slide as the last edit to the block, and commit it that
way. The exported video isn't affected either way — it renders from the
Python video config, which carries the full slide definition.

```
{ echo; date; echo "=== 11. Wire the published URLs into the post ==="
  cmd=(python scripts/build_watch_widget.py _posts/<file>.md scripts/video-configs/<slug>.py --youtube-url https://youtu.be/... --shorts-url https://youtube.com/shorts/...)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/<slug>.log
```

**Example** (section 4's `build_watch_widget.py` again, this time with
both real URLs in hand — same command, re-run in place):

```
{ echo; date; echo "=== 11. Wire the published URLs into the post ==="
  cmd=(python scripts/build_watch_widget.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --youtube-url https://youtu.be/GTIpKWDZBNA --shorts-url https://youtube.com/shorts/rVX4caKw0os)
  echo "\$ ${cmd[*]}"; echo
  time "${cmd[@]}"
  echo
} 2>&1 | tee -a logs/jalan-payoh-lai-kangkar-montfort-nativity-church.log
```

Once both the video and the Short are live, add the YouTube + Shorts
icon buttons to the post's widget row (section 4's row markup),
between the Watch button and the closing `</div>`:

```html
<a href="<video-url>" target="_blank" rel="noopener" aria-label="Watch this story as a video on YouTube" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
  <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
    <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true"><rect x="1" y="4" width="22" height="16" rx="5" fill="#FF0000"/><path d="M10 8.5l6 3.5-6 3.5z" fill="#fff"/></svg>
  </span>
  <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">YouTube</span>
</a>
<a href="<shorts-url>" target="_blank" rel="noopener" aria-label="Watch a short version of this story on YouTube Shorts" style="display: inline-flex; flex-direction: column; align-items: center; gap: 0.2em; text-decoration: none; color: inherit;">
  <span aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888;">
    <svg width="1.4em" height="1.4em" viewBox="0 0 24 24" aria-hidden="true">
      <defs>
        <linearGradient id="shortsGrad<UniquePerPost>" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#FF0000"/>
          <stop offset="100%" stop-color="#FF4E8B"/>
        </linearGradient>
      </defs>
      <rect x="1" y="1" width="22" height="22" rx="7" fill="url(#shortsGrad<UniquePerPost>)"/>
      <path d="M13 6 L7.5 13.5 H11.5 L10.5 18 L16.5 10 H12.5 Z" fill="#fff"/>
    </svg>
  </span>
  <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Shorts</span>
</a>
```

The `linearGradient id` must be unique per post (e.g. `shortsGradJurong`)
— SVG gradient IDs collide globally across a page if two posts' widgets
ever render in the same DOM (not currently possible on this site's
per-post pages, but keep the convention anyway; it costs nothing).

Don't guess a URL from an earlier message without reconfirming — grab
it fresh from Chris or from Channel Content once the upload is
genuinely published.

---

## 12. Commit and push

**[Claude]** — not because committing is hard, but because the working
tree here is messy (see section 0's legend). Since the last commit
you'll typically have: the regenerated `audio/` files, the new
`video-configs/` / `video-gaps/` / `youtube_helper/` files, whatever
unrelated doc or tooling edits rode along, and untracked scratch
(`preview-motion/`, `scratch/`, one-off `docs/` drafts). The work is
reading `git status` and deciding what goes where.

Per CLAUDE.md's Git section, commit and push directly for routine
content changes without asking first. Rough shape:

- **The post's commit** — the post `.md`, both video-config `.py`
  files, the gap report(s) under `docs/video-gaps/`, the
  `docs/youtube_helper/` draft, and the `audio/` files (`.mp3`,
  `.timing.json`, `.srt` — all tracked for every post so far).
- **Separate commits** for anything unrelated that rode along —
  pipeline/script changes, other posts, `.gitignore` additions.
- **Never commit** `preview-motion/` or `scratch/` (both `.gitignore`d
  already); check that nothing new outside them is scratch too, and
  `.gitignore` it if so rather than committing it.
- **Before staging any `.py`** — video configs, a `render_<slug>_*.py`
  renderer, a `generate_narration.py` override edit — run `ruff check .`
  from the repo root and confirm `All checks passed!`. Section 3 already
  lints the configs; this is the catch-all for anything Python that rode
  along since.

**Solo fallback** (Claude unavailable) — the straightforward case is
just the post's own commit:

```
# 12. Commit and push
git add _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md \
        scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py \
        scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church-short.py \
        docs/video-gaps/jalan-payoh-lai-kangkar-montfort-nativity-church-gap.txt \
        docs/youtube_helper/jalan-payoh-lai-kangkar-montfort-nativity-church-youtube.txt \
        audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3 \
        audio/jalan-payoh-lai-kangkar-montfort-nativity-church.timing.json \
        audio/jalan-payoh-lai-kangkar-montfort-nativity-church.srt
git commit -m "Add Watch widget, video, and Short for the Kangkar post"
git push
```

---

## 13. Known gotchas (read before debugging from scratch)

- **Watch viewer opens blank/black, console shows `audio is not
  defined`.** The Watch script's own IIFE must create its own
  `watchAudio = new Audio(...)`, never reference the Listen widget's
  `audio` variable — they're separate script scopes. See the CRITICAL
  comment in section 4's skeleton. This exact bug has shipped twice
  before by copying an incomplete version of the pattern by hand —
  `scripts/build_watch_widget.py` (section 4) generates this correctly
  every time, so this specific bug shouldn't recur for any widget the
  script produced; still worth knowing about if ever hand-editing one.
- **Rendered video plays with no sound.** `render()` in
  `watch_video_lib.py` mixes in `audio/<slug>.mp3` automatically
  (derived from `TIMING_JSON`'s path) — if this ever breaks again,
  check that the mp3 file actually exists at the derived path and that
  ffmpeg's `-map 0:v -map 1:a -c:a aac -shortest` args are present in
  the command it builds.
- **A slide reads "JERKY" in `--check-only`.** Check whether it's a
  `letterbox` slide with zero pan or a `chart` slide first — both are
  documented false positives (section 5). Only investigate further if
  it's a `cover` slide or a slide with real pan movement.
- **A render "looks stalled".** Don't kill it on a flat file-size
  reading alone — check for a genuine completion signal (log line,
  process actually gone) first; ffmpeg's disk writes are bursty.
- **Narration synthesis hangs on one specific post's full text.** Some
  posts deterministically stall Kokoro on full-length synthesis for
  reasons never fully diagnosed. Split into pieces and concatenate
  (section 1) rather than retrying the same full-text call repeatedly.
- **Local Jekyll audio playback looks broken.** The bundled WEBrick dev
  server intermittently stalls serving `.mp3` to an `<audio>` element
  specifically (plain `fetch()`/curl of the same URL works fine) — this
  is a known local-only quirk, not proof the file or markup is broken.
  Verify via `fetch()`/curl first, then just restart `jekyll serve` if
  playback still looks stuck.
- **Straits Times / SPH archive images** have their own dedicated
  copyright rules (two independent PD bases, a $300/yr licensing fee
  for anything not covered by either) — see CLAUDE.md's "Straits Times
  archive check" section before using any NewspaperSG-sourced image.
- **Narration dry-run text stops partway through the post, with no
  error.** `extract_narrative()`'s HTML-depth tracker scans every line
  inside a `<script>` block for tag-like patterns, with no awareness of
  JS comment context — a real comment in `build_watch_widget.py`'s
  generated skeleton once mentioned an `<audio>` element in prose,
  which got matched as an unclosed opening tag and left the depth
  counter stuck above zero for the rest of the file, silently
  swallowing every paragraph after the widget. Only ever triggers on a
  post that already has a Watch widget installed when narration gets
  regenerated (never happens on a fresh post, since narration normally
  comes before the widget in the pipeline order) — fixed by skipping
  tag-scanning on any standalone `//`-only line, but this is exactly
  the class of bug the "check for the closing line" step in section 1
  exists to catch if a similar one ever recurs.
- **Kokoro mispronounces a specific word.** Not every mispronunciation
  is a real/unknown-word problem — misaki's own lexicon can just have a
  wrong entry for a common word, confirmed by testing it directly
  against `misaki.en.G2P` and comparing to similar words that
  phonemize correctly. See `docs/pronunciation-fixes.md` for the
  growing list of confirmed cases (e.g. "Ng", "stung", "graves") and
  how to verify a new one before adding it — the actual fixes live in
  `PRONUNCIATION_OVERRIDES`/`ABBREVIATION_EXPANSIONS` at the top of
  `scripts/generate_narration.py`, with that doc as a human-readable
  summary kept in sync by hand. Add a new override only after verifying
  by ear against a real render, not preemptively.
- **Re-running a command hangs with no output.** Only two commands in
  this doc write a file without `-y` risk in mind: the section 1.4
  fallback concat and section 8's spot-frame `ffmpeg -ss` check (both
  now include `-y`, but if you're running an older or hand-typed
  variant, watch for this). Without `-y`, re-running either against an
  output path that already exists hits ffmpeg's own "File already
  exists. Overwrite? [y/N]" prompt — which hangs forever in a
  non-interactive shell, since nothing will ever type `y`. Every other
  file-producing step is either safe to re-run by design (post/text
  writers replace their own content in place; `watch_video_lib.py`'s
  own `render()` already passes `-y` internally) or doesn't write a
  reusable output path at all.

---

## 14. File/script reference

| Purpose | Path |
|---|---|
| Narration generator | `scripts/generate_narration.py` |
| Narration pronunciation fixes (human-readable summary) | `docs/pronunciation-fixes.md` |
| Listen-widget inserter | `scripts/insert_listen_widget.py` |
| Watch-widget generator | `scripts/build_watch_widget.py` |
| Shared video render engine | `scripts/watch_video_lib.py` |
| Per-post video config (main) | `scripts/video-configs/<slug>.py` |
| Per-post video config (Short) | `scripts/video-configs/<slug>-short.py` |
| Route-walk clip renderer | `scripts/render_route_clip.py` |
| YouTube upload text stager | `scripts/stage_youtube_text.py` |
| Narration audio + timing | `audio/<slug>.mp3`, `.timing.json`, `.srt` |
| Rendered video/Short (untracked scratch) | `preview-motion/<slug>.mp4`, `<slug>-short.mp4` |
| Per-post step logs, `tee`'d (git-ignored scratch) | `logs/<slug>.log` |
| Staged YouTube upload text (tracked) | `docs/youtube_helper/<slug>-youtube.txt` |
| Gap report (auto-generated, tracked) | `docs/video-gaps/<slug>-gap.txt` |
| Post-writing conventions, charts, route animations, copyright rules | `CLAUDE.md` |
