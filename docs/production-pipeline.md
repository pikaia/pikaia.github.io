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

```
1. Post finished (text + images + gallery)      -- CLAUDE.md
2. Generate narration audio (Kokoro TTS)         -- section 1 below
3. Insert the Listen widget                      -- section 2
4. Write the video config (per post)             -- section 4 (do this before step 5)
5. Generate the Watch widget from that config     -- section 3
6. Check smoothness + review the gap report      -- section 5
7. Render the main video                         -- section 6
8. Render the YouTube Short                      -- section 7
9. Verify both files                             -- section 8
10. Stage the YouTube upload text file            -- section 9
11. Upload to YouTube (Chris does the clicks)     -- section 10
12. Wire the published URLs into the post         -- section 11 (or just re-run step 5's script)
13. Commit and push                               -- section 12
```

Section numbers still match the doc's headings below (unchanged, so
existing cross-references stay valid) - only the *order you actually do
them in* has flipped for steps 4/5, since `build_watch_widget.py`
(section 3) now generates the Watch widget from the video config
(section 4) instead of the other way around.

Steps 2-8 (narration through both renders) should happen only **after**
image-gathering is fully finished — the video's slide list and per-image
dwell time both depend on the final image set, so redesigning the
schedule mid-stream after adding a late image is wasted work. Treat
image-gathering as closed before starting narration.

---

## 1. Generate narration audio

```
python scripts/generate_narration.py _posts/<file>.md audio/<slug>.mp3
```

**Example** (the Jalan Payoh Lai / Kangkar post, used throughout this
doc as a running worked example — slug
`jalan-payoh-lai-kangkar-montfort-nativity-church`):

```
python scripts/generate_narration.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3
```

- Voice defaults to `bm_george` (British male) — this is the sitewide
  standard, don't override it unless explicitly asked to A/B test
  another voice.
- Always sanity-check the extracted text first with `--dry-run` (prints
  exactly what will be synthesized) before committing to a real run —
  catches leaked raw HTML/JS from a chart or floated-image block that
  the parser's tag whitelist doesn't yet cover:
  ```
  python scripts/generate_narration.py _posts/<file>.md audio/<slug>.mp3 --dry-run
  ```
  Example:
  ```
  python scripts/generate_narration.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3 --dry-run
  ```
  If something looks wrong (JS/CSS text leaking into the narration),
  extend `HTML_TAG_RE` in `scripts/generate_narration.py` to whitelist
  the new tag before generating for real.
- Output: `audio/<slug>.mp3`, `audio/<slug>.timing.json` (real
  per-sentence `{text, offset_s, duration_s}`, driven off Kokoro's own
  synthesis — not guessed even splits), and `audio/<slug>.srt`.
- Verify the file is real (not truncated) before moving on:
  ```
  ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio/<slug>.mp3
  ```
  Example (real output for this post — a ~5.5 minute post, so ~343s of
  audio is plausible; not a truncated file):
  ```
  $ ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3
  343.056000
  ```
  Should succeed with no error and print a duration that's plausible for
  the post's word count (a post with several minutes of prose should
  yield several minutes of audio, not a few seconds).
- If synthesis stalls/hangs on a specific post's text (a known
  occasional Kokoro issue), split the post's paragraphs into 2-8 pieces
  and synthesize each separately, then concatenate:
  ```
  ffmpeg -i "concat:part1.mp3|part2.mp3|..." -acodec copy audio/<slug>.mp3
  ```
  Example:
  ```
  ffmpeg -i "concat:jalan-payoh-lai-part1.mp3|jalan-payoh-lai-part2.mp3" -acodec copy audio/jalan-payoh-lai-kangkar-montfort-nativity-church.mp3
  ```

---

## 2. Insert the Listen widget

```
python scripts/insert_listen_widget.py _posts/<file>.md <slug>
```

**Example:**

```
python scripts/insert_listen_widget.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md jalan-payoh-lai-kangkar-montfort-nativity-church
```

Inserts the clickable headphones-icon widget right after the post's
first `[← Back to all posts](/)` link. Skips posts that already have
one. If the post is getting the full Watch widget too (section 3), the
Listen markup gets folded into that combined block anyway — running
this first is still fine, or skip straight to hand-authoring the
combined block below.

---

## 3. Author the Watch widget (live in-browser slideshow)

**This step depends on section 4's video config already existing** —
`scripts/build_watch_widget.py` generates the widget FROM that config
(translating Python pan tuples to CSS percentage strings, SCHEDULE to
imageSchedule, pasting in the real sentences from TIMING_JSON), so
write the video config first (skip ahead to section 4, then come back
here) rather than following the pipeline's numbering literally.

```
python scripts/build_watch_widget.py _posts/<file>.md scripts/video-configs/<slug>.py
```

**Example:**

```
python scripts/build_watch_widget.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py
```

- **Does not require a YouTube/Shorts URL** — those almost never exist
  yet at this point in the pipeline (the video isn't rendered, let
  alone uploaded). Omit `--youtube-url`/`--shorts-url` and the row
  simply gets Listen+Watch only; the script prints a reminder to
  re-run once the URL(s) exist:
  ```
  python scripts/build_watch_widget.py _posts/<file>.md scripts/video-configs/<slug>.py --youtube-url https://youtu.be/... --shorts-url https://youtube.com/shorts/...
  ```
  Example, once both are known (this is exactly section 11's "wire the
  URLs in" step, now folded into the same command instead of a separate
  hand-edit):
  ```
  python scripts/build_watch_widget.py _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --youtube-url https://youtu.be/GTIpKWDZBNA --shorts-url https://youtube.com/shorts/rVX4caKw0os
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
- **Chart and route-walk slides aren't auto-generated** — their JS is
  structurally different from a plain image slide (an SVG chart or
  route line, not a `background-image` div) and still needs hand
  authoring, copied from an existing post with one (see CLAUDE.md's
  Charts/Route animations sections). The script fills in a flagged
  `/* MANUAL: ... */` placeholder for any such slide instead of
  producing something silently wrong, and reports the count on exit.
- **Refuses rather than guesses** if the post already has a full Watch
  widget that wasn't generated by this script (no marker comments) —
  that widget may carry real hand-tuned data (published URLs, tuned
  pan/zoom) this script can't safely tell apart from something stale.
  Remove it by hand first, or add the marker comments yourself.

Verify locally (`jekyll serve`, see CLAUDE.md's intro) after running
it: click Watch, confirm the image/caption/progress bar all advance
with zero console errors. This class of bug (a variable valid in one
`<script>` block's scope but not the other) only surfaces by actually
running the page — the generator removes the most common instance of
it by construction (see the gotchas in section 13), but still verify.

The rest of this section shows exactly what the script generates — useful
for understanding the output, or as a hand-authoring fallback for a
chart/route-walk slide the script flagged. Copy it from an existing
post with one (e.g.
`_posts/2026-07-28-japans-quiet-hand-in-building-jurong.md`) rather
than retyping from memory if you ever do need to hand-edit.

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
  // the video config's IMAGES dict (section 4) so the two stay easy to
  // cross-reference.
  var HERO = "https://upload.wikimedia.org/...";

  // One entry per slide appearance (an image can repeat with different
  // zoom/pan for a bookend effect - see section 4's SLIDES contract).
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
  // points. Must match the Python config's SCHEDULE (section 4) exactly
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
in section 4 below.

Verify locally (`jekyll serve`, see CLAUDE.md's intro) before pushing:
click Watch, confirm the image/caption/progress bar all advance with
zero console errors. This class of bug (a variable valid in one
`<script>` block's scope but not the other) only surfaces by actually
running the page — static review won't catch it.

---

## 4. Write the video config

**In practice, write this before section 3** — since
`scripts/build_watch_widget.py` (section 3) generates the Watch widget
FROM this file, this is the config that should exist first, even
though it's numbered after the widget step in this doc's overview.

Video rendering is driven by a **shared engine**,
`scripts/watch_video_lib.py`, with per-post data in
`scripts/video-configs/<slug>.py` (main video) and
`scripts/video-configs/<slug>-short.py` (Shorts, section 7). Never
copy the engine itself into a scratch/per-post script — that's exactly
how a real jerky-panning bug regressed in the past (a fix landed in one
copy and not the others). Only the config module is per-post.

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
                                          # the Watch widget's imageSchedule (section 3) by value
TOTAL_DURATION = 322.625                 # must match the Watch widget's TOTAL_DURATION
TIMING_JSON = "audio/<slug>.timing.json" # path relative to repo root

# Optional, default 1280x720x25:
WIDTH, HEIGHT, FPS = 1280, 720, 25
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

---

## 5. Check smoothness and review the gap report

Before committing to a full render (which can take 15-25+ minutes),
run the cheap pre-check:

```
python scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --check-only
```

**Example:**

```
python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --check-only
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

```
python scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --out preview-motion/<slug>.mp4
```

**Example:**

```
python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --out preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church.mp4
```

A full render (frame-by-frame PIL compositing piped to ffmpeg) takes
roughly 15-25 minutes for a 5-6 minute video. **On Windows, do not run
this as a foreground Bash/PowerShell call and do not rely on
`run_in_background`** — both are capped at a 10-minute tool timeout and
will get silently killed mid-render. Launch it as a genuinely
OS-detached process instead:

```powershell
Start-Process -FilePath python -ArgumentList "scripts/watch_video_lib.py --config scripts/video-configs/<slug>.py --out preview-motion/<slug>.mp4" -WindowStyle Hidden -RedirectStandardOutput preview-motion/<slug>-render.log -RedirectStandardError preview-motion/<slug>-render.err
```

Example:

```powershell
Start-Process -FilePath python -ArgumentList "scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church.py --out preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church.mp4" -WindowStyle Hidden -RedirectStandardOutput preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church-render.log -RedirectStandardError preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church-render.err
```

Poll progress with `Get-Content preview-motion/<slug>-render.log -Tail
20` or `Get-Process python` — don't kill it just because the output
file's size looks flat between two checks a few minutes apart; ffmpeg's
writes are bursty, and a false "stall" diagnosis has cost a wasted
re-render before. Look for an actual completion signal (`Wrote
<path>` in the log, or the process genuinely gone) before concluding
it's stuck.

`preview-motion/` is untracked scratch (confirmed via `git log --all --
"*.mp4"` — never committed) — the blog embeds YouTube links, not local
video files, so nothing here needs to go in git except the config
scripts and gap reports that produced it.

---

## 7. Render the YouTube Short

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

# Shorts want smaller/higher captions than the landscape default:
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

Run the same `--check-only` then render commands as sections 5-6,
swapping in the `-short.py` config and a `preview-motion/<slug>-short.mp4`
output path (Shorts are short enough to usually finish within the
10-minute tool timeout, but the `Start-Process` pattern is still safe
to use).

**Example:**

```
python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church-short.py --check-only
python scripts/watch_video_lib.py --config scripts/video-configs/jalan-payoh-lai-kangkar-montfort-nativity-church-short.py --out preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church-short.mp4
```

---

## 8. Verify both files

Don't trust that a render "looks done" — verify:

```
ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 preview-motion/<slug>.mp4
```

Example:

```
ffprobe -v error -count_frames -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church.mp4
```

Compare against the expected frame count, `TOTAL_DURATION * FPS`
(e.g. `322.625 * 25 = 8065.625` → expect `8066`, off-by-one from
rounding is fine; for this post, `361.125 * 25 = 9028.125` → expect
`9028` or `9029`). This is a **full decode**, not a spot-check — if the
video ever needs trimming/concatenation with ffmpeg's `-c copy` path, a
full-decode verify is mandatory (a real past bug: non-monotonic source
DTS silently truncated the video track during a trim+concat, completely
undetectable by spot-check frame extraction alone). Then pull 1-2 spot
frames at meaningful timestamps and eyeball them:

```
ffmpeg -ss <t> -i preview-motion/<slug>.mp4 -frames:v 1 preview-motion/spot-<t>.png
```

Example (a frame at t=110.3s should land on the "church exterior
(reused) - Montfort founding 1916-1958" slide, per this post's real
schedule in section 4):

```
ffmpeg -ss 110.3 -i preview-motion/jalan-payoh-lai-kangkar-montfort-nativity-church.mp4 -frames:v 1 preview-motion/spot-110.3.png
```

Confirm the image and caption match what should be on screen at that
moment.

---

## 9. Stage the YouTube upload text file

Generate the draft with `scripts/stage_youtube_text.py`:

```
python scripts/stage_youtube_text.py \
    _posts/<file>.md \
    scripts/video-configs/<slug>.py \
    scripts/video-configs/<slug>-short.py \
    --post-url https://pikaia.github.io/YYYY/MM/DD/<slug>/
```

**Example** (this one is a real, already-run command — this post has
no `scripts/video-configs/` file, so the two config paths are simply
omitted, per section 4's note; `--out` is shown explicitly even though
it matches the default, for clarity):

```
python scripts/stage_youtube_text.py \
    _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md \
    --post-url https://pikaia.github.io/2026/08/15/jalan-payoh-lai-kangkar-montfort-nativity-church/ \
    --out docs/youtube_helper/jalan-payoh-lai-kangkar-montfort-nativity-church-youtube.txt
```

Real result: `docs/youtube_helper/jalan-payoh-lai-kangkar-montfort-nativity-church-youtube.txt`
— since this post already has a real published video and Short (see
section 4's note), the script detected both existing YouTube links in
the post's own widget markup and correctly reported "video already
published at `https://youtu.be/GTIpKWDZBNA`, but predates the
`scripts/video-configs/` pipeline" instead of the generic "no video
built yet" placeholder it would show for a post with no video at all.

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

**The easiest path is re-running section 3's script** with
`--youtube-url`/`--shorts-url` now that both are known — it replaces
the whole widget block in place (safe, idempotent) and adds the row's
YouTube/Shorts buttons as part of that, so the manual markup edit below
is now a fallback, not the default: use it only when hand-patching a
widget the script didn't generate (no marker comments), or when only
adding the two buttons without wanting to touch anything else the
script would also regenerate.

Once both the video and the Short are live, add the YouTube + Shorts
icon buttons to the post's widget row (section 3's row markup),
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

Per CLAUDE.md's Git section: commit and push directly for routine
content changes (the post file, the two video-config `.py` files, the
gap report under `docs/video-gaps/`) without asking first. `audio/` and
`preview-motion/` — check whether `audio/*.mp3`/`.timing.json`/`.srt`
are tracked in this repo (they have been for every post so far) vs.
`preview-motion/` which is deliberately never committed.

**Example:**

```
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
  comment in section 3's skeleton. This exact bug has shipped twice
  before by copying an incomplete version of the pattern by hand —
  `scripts/build_watch_widget.py` (section 3) generates this correctly
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

---

## 14. File/script reference

| Purpose | Path |
|---|---|
| Narration generator | `scripts/generate_narration.py` |
| Listen-widget inserter | `scripts/insert_listen_widget.py` |
| Watch-widget generator | `scripts/build_watch_widget.py` |
| Shared video render engine | `scripts/watch_video_lib.py` |
| Per-post video config (main) | `scripts/video-configs/<slug>.py` |
| Per-post video config (Short) | `scripts/video-configs/<slug>-short.py` |
| Route-walk clip renderer | `scripts/render_route_clip.py` |
| YouTube upload text stager | `scripts/stage_youtube_text.py` |
| Narration audio + timing | `audio/<slug>.mp3`, `.timing.json`, `.srt` |
| Rendered video/Short (untracked scratch) | `preview-motion/<slug>.mp4`, `<slug>-short.mp4` |
| Staged YouTube upload text (tracked) | `docs/youtube_helper/<slug>-youtube.txt` |
| Gap report (auto-generated, tracked) | `docs/video-gaps/<slug>-gap.txt` |
| Post-writing conventions, charts, route animations, copyright rules | `CLAUDE.md` |
