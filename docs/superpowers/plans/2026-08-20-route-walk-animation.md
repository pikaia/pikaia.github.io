# Route-walk Animation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `route-walk` Watch slide type — an animated route over a real OpenStreetMap tile — to the Hougang/Kangkar post, replacing the loosely-related photo currently standing in for "the walk from the Upper Serangoon Road junction... called Holy Innocents' Lane," and build the matching video-export renderer.

**Architecture:** Two independent renderers share one hand-plotted route dataset (map tile + landmark nodes + bezier path). The live renderer extends the post's existing inline Watch-widget script with a new slide branch: an SVG (tile image + halo-stroke route path + pulsing marker) driven by CSS keyframes restarted on slide activation exactly like the existing pan/zoom slides, plus HTML label pills positioned via `getScreenCTM()`. The video renderer is a new standalone Python script that draws the same route with PIL frame-by-frame and encodes it with ffmpeg.

**Tech Stack:** Vanilla JS/CSS/SVG (no build step, matches existing per-post widget convention), Python 3 + Pillow + ffmpeg (matches `scripts/generate_narration.py`'s existing style — argparse CLI, no test framework, since none exists in this repo).

**Spec:** `docs/superpowers/specs/2026-08-20-route-walk-animation-design.md`

## Global Constraints

- Map source is OpenStreetMap (ODbL) only — never Google Maps or any other non-freely-licensed map source. Always credited ("Map data © OpenStreetMap contributors") both on-screen and in the post's Sources list.
- No AI image generation anywhere in this feature.
- The route is an approximate stand-in for a walk that can't be precisely reconstructed (the real backlane no longer exists on any map) — it conveys a sense of distance/direction, not literal historical accuracy.
- The `route-walk` slide has no play button or independent timer of its own in production — it reads `watchAudio.currentTime` through the existing `updateForTime()`/`imageSchedule` machinery, exactly like the photo slides.
- This repo has no automated test framework (confirmed: no `pytest`/`unittest` anywhere in the codebase). Verification steps in this plan are manual (local Jekyll preview, visual inspection of rendered frames) — do not introduce a new test framework for this feature.
- Splicing the new clip into the actual published YouTube/Shorts .mp4 stays a manual, interactive step (as the existing video pipeline already works) — out of scope for this plan.

---

### Task 1: Commit the OpenStreetMap tile asset

**Files:**
- Create: `assets/images/jalan-payoh-lai-route-map.png`

**Interfaces:**
- Produces: a 581×688px PNG at `/assets/images/jalan-payoh-lai-route-map.png`, referenced by Task 2's slide data and Task 4's `--tile` argument.

- [ ] **Step 1: Copy the sourced tile image into the repo**

```bash
mkdir -p "C:/Users/chris/projects/pikaia.github.io/assets/images"
cp "C:/Users/chris/.claude/image-cache/37f5955e-a0e4-46b5-9bed-b738d8bdc58a/9.png" \
   "C:/Users/chris/projects/pikaia.github.io/assets/images/jalan-payoh-lai-route-map.png"
```

- [ ] **Step 2: Verify it's the expected file**

```bash
python -c "from PIL import Image; im = Image.open('assets/images/jalan-payoh-lai-route-map.png'); print(im.size, im.format)"
```

Expected: `(581, 688) PNG`. This matches the `TILE_NATIVE_W`/`TILE_NATIVE_H` constants used in Task 2 and Task 4 — if the size differs, every coordinate in this plan needs re-deriving, so stop and re-check before continuing.

- [ ] **Step 3: Commit**

```bash
git add assets/images/jalan-payoh-lai-route-map.png
git commit -m "Add OpenStreetMap tile asset for the route-walk slide

ODbL-licensed (commercial reuse permitted with attribution), covering
Hougang Central / Jalan Payoh Lai / Jalan Naung. Credited on-screen and
in the post's Sources list in the next commit."
```

---

### Task 2: Add the `route-walk` slide type to the Hougang/Kangkar post

**Files:**
- Modify: `_posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md`

**Interfaces:**
- Consumes: `assets/images/jalan-payoh-lai-route-map.png` (Task 1).
- Produces: the route-walk slide, live in the Watch widget at slide index 1 (t=24.775–49.825 in the post's timeline).

- [ ] **Step 1: Replace slide 1's data with the route-walk entry**

In the `slides` array (currently starting at line 98), replace this entry (the second one, currently the Sungei Serangoon panorama):

```js
    { src: "https://upload.wikimedia.org/wikipedia/commons/f/f1/Sungei_Serangoon%2C_panorama%2C_Nov_06.jpg", type: "cover", zoom: [1, 1.1, 1.16], pan: ["30% 60%", "50% 45%", "68% 30%"], ease: "ease-in" },
```

with:

```js
    { type: "route-walk", src: "/assets/images/jalan-payoh-lai-route-map.png", w: 581, h: 688, animS: 7,
      path: "M72,560 C95,555 120,552 145,548 C175,543 190,510 210,460 C230,410 250,400 272,385",
      nodes: [
        { x: 72, y: 560, label: "Jalan Payoh Lai", delayS: 0.1 },
        { x: 145, y: 548, label: "Upper Serangoon Rd Junction", delayS: 1.5 },
        { x: 210, y: 460, label: "Holy Innocents\u2019 Lane", delayS: 4.0 },
        { x: 272, y: 385, label: "Montfort School", delayS: 6.5 }
      ] },
```

(All other entries in `slides` stay exactly as they are — only this one entry changes.)

- [ ] **Step 2: Add the route-walk branch to the slide-building loop**

Find the `slideEls = slides.map(...)` function (currently lines 195–222). Its `if (s.type === 'letterbox') { ... } else { ... }` becomes a three-way branch. Replace:

```js
    if (s.type === 'letterbox') {
      var bg = document.createElement('div');
      bg.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-position:center;filter:blur(30px) brightness(0.55);background-image:url(\'' + s.src + '\');';
      bg.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      var fg = document.createElement('div');
      fg.style.cssText = 'position:absolute;inset:6%;background-size:contain;background-position:center;background-repeat:no-repeat;background-image:url(\'' + s.src + '\');';
      el.appendChild(bg);
      el.appendChild(fg);
      el._animTargets = [bg];
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
```

with:

```js
    if (s.type === 'route-walk') {
      el._routeWalk = buildRouteWalk(el, s);
    } else if (s.type === 'letterbox') {
      var bg = document.createElement('div');
      bg.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-position:center;filter:blur(30px) brightness(0.55);background-image:url(\'' + s.src + '\');';
      bg.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      var fg = document.createElement('div');
      fg.style.cssText = 'position:absolute;inset:6%;background-size:contain;background-position:center;background-repeat:no-repeat;background-image:url(\'' + s.src + '\');';
      el.appendChild(bg);
      el.appendChild(fg);
      el._animTargets = [bg];
    } else {
      var layer = document.createElement('div');
      layer.style.cssText = 'position:absolute;inset:-8%;background-size:cover;background-image:url(\'' + s.src + '\');';
      layer.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
      el.appendChild(layer);
      el._animTargets = [layer];
    }

    if (s.type !== 'route-walk') {
      styleEl.textContent += '@keyframes kb' + i + ' { 0% { transform: scale(' + s.zoom[0] + '); background-position: ' + s.pan[0] + '; } 50% { transform: scale(' + s.zoom[1] + '); background-position: ' + s.pan[1] + '; } 100% { transform: scale(' + s.zoom[2] + '); background-position: ' + s.pan[2] + '; } }\n';
    }
    stage.appendChild(el);
    return el;
  });
```

Now add the `buildRouteWalk` function and the shared route-walk keyframes. Insert this immediately **before** the `var slideEls = slides.map(...)` line:

```js
  styleEl.textContent +=
    '@keyframes routeDraw { from { stroke-dashoffset: 100; } to { stroke-dashoffset: 0; } }\n' +
    '@keyframes markerWalk { from { opacity: 1; offset-distance: 0%; } to { opacity: 1; offset-distance: 100%; } }\n' +
    '@keyframes labelFade { from { opacity: 0; } to { opacity: 1; } }\n';

  var SVG_NS = 'http://www.w3.org/2000/svg';

  function buildRouteWalk(el, s) {
    var svg = document.createElementNS(SVG_NS, 'svg');
    svg.setAttribute('viewBox', '0 0 ' + s.w + ' ' + s.h);
    svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
    svg.style.cssText = 'position:absolute;inset:6%;width:88%;height:88%;overflow:visible;';

    var img = document.createElementNS(SVG_NS, 'image');
    img.setAttributeNS('http://www.w3.org/1999/xlink', 'href', s.src);
    img.setAttribute('x', 0);
    img.setAttribute('y', 0);
    img.setAttribute('width', s.w);
    img.setAttribute('height', s.h);
    svg.appendChild(img);

    var halo = document.createElementNS(SVG_NS, 'path');
    halo.setAttribute('d', s.path);
    halo.setAttribute('pathLength', '100');
    halo.setAttribute('fill', 'none');
    halo.setAttribute('stroke', '#fdf6e8');
    halo.setAttribute('stroke-width', '4');
    halo.setAttribute('stroke-linecap', 'round');
    halo.setAttribute('stroke-linejoin', 'round');
    halo.setAttribute('opacity', '0.85');
    halo.setAttribute('stroke-dasharray', '100');
    halo.setAttribute('stroke-dashoffset', '100');
    svg.appendChild(halo);

    var route = document.createElementNS(SVG_NS, 'path');
    route.setAttribute('d', s.path);
    route.setAttribute('pathLength', '100');
    route.setAttribute('fill', 'none');
    route.setAttribute('stroke', '#e2572e');
    route.setAttribute('stroke-width', '2');
    route.setAttribute('stroke-linecap', 'round');
    route.setAttribute('stroke-linejoin', 'round');
    route.setAttribute('stroke-dasharray', '100');
    route.setAttribute('stroke-dashoffset', '100');
    svg.appendChild(route);

    s.nodes.forEach(function (n) {
      var dot = document.createElementNS(SVG_NS, 'circle');
      dot.setAttribute('cx', n.x);
      dot.setAttribute('cy', n.y);
      dot.setAttribute('r', 3.5);
      dot.setAttribute('fill', '#e2572e');
      dot.setAttribute('stroke', '#fdf6e8');
      dot.setAttribute('stroke-width', '1.5');
      svg.appendChild(dot);
    });

    var marker = document.createElementNS(SVG_NS, 'g');
    marker.style.offsetPath = "path('" + s.path + "')";
    marker.style.opacity = '0';
    var markerHalo = document.createElementNS(SVG_NS, 'circle');
    markerHalo.setAttribute('r', 7);
    markerHalo.setAttribute('fill', '#e2572e');
    markerHalo.setAttribute('opacity', '0.3');
    var markerDot = document.createElementNS(SVG_NS, 'circle');
    markerDot.setAttribute('r', 3.5);
    markerDot.setAttribute('fill', '#e2572e');
    markerDot.setAttribute('stroke', '#2a0f08');
    markerDot.setAttribute('stroke-width', '1');
    marker.appendChild(markerHalo);
    marker.appendChild(markerDot);
    svg.appendChild(marker);

    var credit = document.createElement('div');
    credit.textContent = 'Map data \u00A9 OpenStreetMap contributors';
    credit.style.cssText = 'position:absolute;left:7%;top:7%;font-size:0.68em;color:rgba(255,255,255,0.75);background:rgba(0,0,0,0.45);padding:0.2em 0.5em;border-radius:3px;';

    el.appendChild(svg);
    el.appendChild(credit);

    var labelEls = s.nodes.map(function (n) {
      var lbl = document.createElement('div');
      lbl.textContent = n.label;
      lbl.style.cssText = 'position:absolute;transform:translate(-50%,-120%);background:rgba(0,0,0,0.6);color:#fff;font-size:0.85em;font-weight:600;padding:0.35em 0.6em;border-radius:4px;opacity:0;white-space:nowrap;z-index:1;pointer-events:none;';
      stage.appendChild(lbl);
      return lbl;
    });

    return { svg: svg, halo: halo, route: route, marker: marker, labelEls: labelEls, nodes: s.nodes, animS: s.animS };
  }
```

- [ ] **Step 3: Wire route-walk activation/deactivation into `updateForTime`**

Find the slide-switching block inside `updateForTime` (currently around lines 251–267):

```js
      slideEls.forEach(function (el, i) {
        el.style.opacity = (i === idx) ? '1' : '0';
        if (i === idx) {
          var ease = slides[i].ease || 'linear';
          el._animTargets.forEach(function (target) {
            target.style.animation = 'none';
            void target.offsetWidth;
            target.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
          });
        }
      });
```

Replace with:

```js
      slideEls.forEach(function (el, i) {
        el.style.opacity = (i === idx) ? '1' : '0';
        if (i === idx) {
          if (slides[i].type === 'route-walk') {
            restartRouteWalk(el._routeWalk);
          } else {
            var ease = slides[i].ease || 'linear';
            el._animTargets.forEach(function (target) {
              target.style.animation = 'none';
              void target.offsetWidth;
              target.style.animation = 'kb' + i + ' ' + dur + 's ' + ease + ' forwards';
            });
          }
        } else if (slides[i].type === 'route-walk' && el._routeWalk) {
          el._routeWalk.labelEls.forEach(function (lbl) {
            lbl.style.animation = 'none';
            lbl.style.opacity = '0';
          });
        }
      });
```

Add these two helper functions right after `buildRouteWalk` (defined in Step 2):

```js
  function restartRouteWalk(rw) {
    if (!rw) return;
    var animS = rw.animS + 's linear forwards';
    [rw.halo, rw.route].forEach(function (p) { p.style.animation = 'none'; });
    rw.marker.style.animation = 'none';
    rw.labelEls.forEach(function (lbl) { lbl.style.animation = 'none'; });
    void rw.svg.offsetWidth;
    rw.halo.style.animation = 'routeDraw ' + animS;
    rw.route.style.animation = 'routeDraw ' + animS;
    rw.marker.style.animation = 'markerWalk ' + animS;
    rw.nodes.forEach(function (n, i) {
      rw.labelEls[i].style.animation = 'labelFade 0.5s ease forwards';
      rw.labelEls[i].style.animationDelay = n.delayS + 's';
    });
    positionRouteLabels(rw);
  }

  function positionRouteLabels(rw) {
    var ctm = rw.svg.getScreenCTM();
    if (!ctm) return;
    var pt = rw.svg.createSVGPoint();
    var stageRect = stage.getBoundingClientRect();
    rw.nodes.forEach(function (n, i) {
      pt.x = n.x;
      pt.y = n.y;
      var screenPt = pt.matrixTransform(ctm);
      rw.labelEls[i].style.left = (screenPt.x - stageRect.left) + 'px';
      rw.labelEls[i].style.top = (screenPt.y - stageRect.top) + 'px';
    });
  }

  window.addEventListener('resize', function () {
    if (slides[currentIndex] && slides[currentIndex].type === 'route-walk') {
      positionRouteLabels(slideEls[currentIndex]._routeWalk);
    }
  });
```

- [ ] **Step 4: Add the OpenStreetMap credit to the post's Sources list**

In the `**Sources:**` bulleted list near the end of the post, add:

```markdown
- [OpenStreetMap](https://www.openstreetmap.org/copyright) — map data © OpenStreetMap contributors, ODbL
```

- [ ] **Step 5: Bump `last_modified_at`**

In the front matter, update:

```yaml
last_modified_at: 2026-08-21 04:54:00 +0800
```

to the current time (this is a substantive content edit per `CLAUDE.md`'s convention).

- [ ] **Step 6: Commit**

```bash
git add _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md
git commit -m "Add route-walk animation to the Hougang/Kangkar post's Watch widget

Replaces the loosely-related Sungei Serangoon photo at slide 1 with an
animated route over a real OpenStreetMap tile, tracing the walk from
Jalan Payoh Lai to Montfort School / Holy Innocents' Lane. See
docs/superpowers/specs/2026-08-20-route-walk-animation-design.md."
```

---

### Task 3: Verify the route-walk slide in local Jekyll preview

**Files:** none (manual verification only — this repo has no automated test framework; see Global Constraints).

**Interfaces:**
- Consumes: Task 2's changes to the post.

- [ ] **Step 1: Start the local Jekyll server**

```bash
cd "C:/Users/chris/projects/pikaia.github.io"
jekyll serve --config _config.yml,_config_dev.yml
```

- [ ] **Step 2: Open the post and trigger the Watch overlay**

Navigate to `http://127.0.0.1:4000/2026/08/16/jalan-payoh-lai-kangkar-montfort-nativity-church/`, click "Watch," and let playback run into the second slide (around 0:25).

Check, in order:
1. The OSM tile appears (blurred cover behind, sharp contained copy in front) with the "Map data © OpenStreetMap contributors" credit visible in the corner.
2. The route line draws itself (halo + solid color) over roughly the first 7 seconds of the slide, then holds still while narration continues through the Holy Innocents schools/Montfort history.
3. The four labels ("Jalan Payoh Lai," "Upper Serangoon Rd Junction," "Holy Innocents' Lane," "Montfort School") land at their nodes at the right moments and don't drift off the route.
4. The marker (small pulsing dot) ends at the "Montfort School" node and stays there.

- [ ] **Step 3: Check scrub behavior**

Drag the progress bar to a point in the middle of this slide (roughly 0:35), release, and confirm the slide displays without visual glitches (the route/marker may jump straight to their end state rather than animating from 0 — that's expected given this reuses the existing pan/zoom slides' restart-on-activation behavior, not a bug).

- [ ] **Step 4: Check a resize**

While the route-walk slide is showing, resize the browser window (or open dev tools' device toolbar and switch to a phone-sized viewport) and confirm the labels stay correctly attached to their nodes rather than drifting.

- [ ] **Step 5: Stop the server**

```bash
# Ctrl+C in the terminal running jekyll serve
```

No commit for this task — it's verification only. If any check fails, fix the relevant step in Task 2 and re-run this task before proceeding.

---

### Task 4: Build the video-export renderer

**Files:**
- Create: `scripts/render_route_clip.py`

**Interfaces:**
- Consumes: `assets/images/jalan-payoh-lai-route-map.png` (Task 1).
- Produces: an `.mp4` clip via CLI (`python scripts/render_route_clip.py --tile ... --out ... --duration ...`).

- [ ] **Step 1: Write the script**

```python
"""Render a route-walk slide's animated map segment to an .mp4 clip.

Local dev tool only - not part of the deployed Jekyll site. Draws the
same route-walk data (map tile, path, nodes, labels) used by the live
Watch widget onto video frames with PIL, then encodes them with ffmpeg.
Mirrors the CSS/SVG live renderer's math independently rather than
sharing code - see the design spec's "Architecture" section for why
(same duality already used for the existing pan/zoom slides).

IMPORTANT: node/path coordinates below must be kept in sync by hand with
the matching post's inline <script> if either one changes - see
docs/superpowers/specs/2026-08-20-route-walk-animation-design.md.

Requires: pip install pillow
ffmpeg must be on PATH.

Usage:
    python scripts/render_route_clip.py \
        --tile assets/images/jalan-payoh-lai-route-map.png \
        --out preview-motion/jalan-payoh-lai-route-walk.mp4 \
        --duration 25.05
"""
import argparse
import io
import subprocess
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

# Route data - must match the "route-walk" slide entry in
# _posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md
NODES = [
    {"x": 72, "y": 560, "label": "Jalan Payoh Lai", "delay_s": 0.1},
    {"x": 145, "y": 548, "label": "Upper Serangoon Rd Junction", "delay_s": 1.5},
    {"x": 210, "y": 460, "label": "Holy Innocents\u2019 Lane", "delay_s": 4.0},
    {"x": 272, "y": 385, "label": "Montfort School", "delay_s": 6.5},
]
# Cubic Bezier control points (start, c1, c2, end) per segment - same
# curve as the "d" attribute on the live SVG path.
PATH_SEGMENTS = [
    ((72, 560), (95, 555), (120, 552), (145, 548)),
    ((145, 548), (175, 543), (190, 510), (210, 460)),
    ((210, 460), (230, 410), (250, 400), (272, 385)),
]
ROUTE_COLOR = (226, 87, 46)      # #e2572e
HALO_COLOR = (253, 246, 232)     # #fdf6e8
CREDIT_TEXT = "Map data \u00A9 OpenStreetMap contributors"


def cubic_bezier_points(p0, p1, p2, p3, n=40):
    points = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = (mt ** 3) * p0[0] + 3 * (mt ** 2) * t * p1[0] + 3 * mt * (t ** 2) * p2[0] + (t ** 3) * p3[0]
        y = (mt ** 3) * p0[1] + 3 * (mt ** 2) * t * p1[1] + 3 * mt * (t ** 2) * p2[1] + (t ** 3) * p3[1]
        points.append((x, y))
    return points


def full_path_points():
    points = [PATH_SEGMENTS[0][0]]
    for p0, p1, p2, p3 in PATH_SEGMENTS:
        points.extend(cubic_bezier_points(p0, p1, p2, p3)[1:])
    return points


def load_font(size):
    for candidate in ("arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def compose_frame(tile, canvas_w, canvas_h, elapsed_s, anim_s):
    progress = min(1.0, elapsed_s / anim_s) if anim_s > 0 else 1.0
    scale = min(canvas_w / tile.width, canvas_h / tile.height)
    disp_w, disp_h = int(tile.width * scale), int(tile.height * scale)
    off_x, off_y = (canvas_w - disp_w) // 2, (canvas_h - disp_h) // 2

    bg = tile.resize((canvas_w, canvas_h))
    bg = bg.filter(ImageFilter.GaussianBlur(18))
    bg = ImageEnhance.Brightness(bg).enhance(0.42)

    frame = bg.convert("RGB")
    frame.paste(tile.resize((disp_w, disp_h)), (off_x, off_y))

    draw = ImageDraw.Draw(frame, "RGBA")

    def to_canvas(pt):
        return (off_x + pt[0] * scale, off_y + pt[1] * scale)

    pts = [to_canvas(p) for p in full_path_points()]
    n_shown = max(2, int(len(pts) * progress))
    shown = pts[:n_shown]

    draw.line(shown, fill=HALO_COLOR + (217,), width=max(1, int(4 * scale)), joint="curve")
    draw.line(shown, fill=ROUTE_COLOR + (255,), width=max(1, int(2 * scale)), joint="curve")

    for node in NODES:
        cx, cy = to_canvas((node["x"], node["y"]))
        r = 3.5 * scale
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ROUTE_COLOR + (255,), outline=HALO_COLOR + (255,), width=2)

    if shown:
        mx, my = shown[-1]
        r = 3.5 * scale
        draw.ellipse([mx - r * 2, my - r * 2, mx + r * 2, my + r * 2], fill=ROUTE_COLOR + (77,))
        draw.ellipse([mx - r, my - r, mx + r, my + r], fill=ROUTE_COLOR + (255,))

    font = load_font(max(12, int(16 * scale)))
    for node in NODES:
        if elapsed_s < node["delay_s"]:
            continue
        cx, cy = to_canvas((node["x"], node["y"]))
        label = node["label"]
        bbox = draw.textbbox((0, 0), label, font=font)
        pad = 6
        w, h = bbox[2] - bbox[0] + pad * 2, bbox[3] - bbox[1] + pad * 2
        lx, ly = cx - w / 2, cy - h - 14
        draw.rounded_rectangle([lx, ly, lx + w, ly + h], radius=4, fill=(0, 0, 0, 153))
        draw.text((lx + pad, ly + pad), label, font=font, fill=(255, 255, 255, 255))

    credit_font = load_font(max(10, int(11 * scale)))
    credit_w = draw.textlength(CREDIT_TEXT, font=credit_font)
    draw.rectangle([8, 8, 8 + credit_w + 12, 30], fill=(0, 0, 0, 115))
    draw.text((14, 12), CREDIT_TEXT, font=credit_font, fill=(255, 255, 255, 166))

    return frame


def render(tile_path, out_path, duration_s, anim_s, width, height, fps):
    tile = Image.open(tile_path).convert("RGB")
    total_frames = int(duration_s * fps)

    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-f", "image2pipe", "-vcodec", "png", "-r", str(fps), "-i", "-",
         "-vcodec", "libx264", "-pix_fmt", "yuv420p", "-r", str(fps), out_path],
        stdin=subprocess.PIPE,
    )

    for frame_i in range(total_frames):
        t = frame_i / fps
        frame = compose_frame(tile, width, height, t, anim_s)
        buf = io.BytesIO()
        frame.save(buf, format="PNG")
        proc.stdin.write(buf.getvalue())

    proc.stdin.close()
    proc.wait()
    if proc.returncode != 0:
        print(f"ffmpeg exited with code {proc.returncode}", file=sys.stderr)
        sys.exit(1)
    print(f"Wrote {out_path}: {total_frames} frames @ {fps}fps, {duration_s}s")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tile", required=True, help="path to the OSM tile image")
    parser.add_argument("--out", required=True, help="output .mp4 path")
    parser.add_argument("--duration", type=float, required=True, help="total clip length in seconds")
    parser.add_argument("--anim-seconds", type=float, default=7.0, help="how long the route takes to draw before holding static")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--fps", type=int, default=30)
    args = parser.parse_args()
    render(args.tile, args.out, args.duration, args.anim_seconds, args.width, args.height, args.fps)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Commit**

```bash
git add scripts/render_route_clip.py
git commit -m "Add render_route_clip.py: video-export renderer for route-walk slides"
```

---

### Task 5: Verify the rendered clip

**Files:** none (manual verification only — see Global Constraints).

**Interfaces:**
- Consumes: `scripts/render_route_clip.py` (Task 4), `assets/images/jalan-payoh-lai-route-map.png` (Task 1).

- [ ] **Step 1: Render a short test clip**

```bash
cd "C:/Users/chris/projects/pikaia.github.io"
python scripts/render_route_clip.py \
  --tile assets/images/jalan-payoh-lai-route-map.png \
  --out preview-motion/jalan-payoh-lai-route-walk-test.mp4 \
  --duration 9 --anim-seconds 7
```

Expected: script prints `Wrote preview-motion/jalan-payoh-lai-route-walk-test.mp4: 270 frames @ 30fps, 9.0s` and exits 0.

- [ ] **Step 2: Extract frames at key moments and inspect them**

```bash
ffmpeg -y -i preview-motion/jalan-payoh-lai-route-walk-test.mp4 -ss 0.5 -vframes 1 preview-motion/frame-start.png
ffmpeg -y -i preview-motion/jalan-payoh-lai-route-walk-test.mp4 -ss 4 -vframes 1 preview-motion/frame-mid.png
ffmpeg -y -i preview-motion/jalan-payoh-lai-route-walk-test.mp4 -ss 8 -vframes 1 preview-motion/frame-end.png
```

Read each of `preview-motion/frame-start.png`, `preview-motion/frame-mid.png`, `preview-motion/frame-end.png` and confirm:
- `frame-start.png`: tile visible, route barely started, no/first label only.
- `frame-mid.png`: route roughly half-drawn, marker partway along, 2-3 labels visible.
- `frame-end.png`: full route drawn, marker at the Montfort School node, all four labels visible, OSM credit visible in the corner.

- [ ] **Step 3: Confirm the render matches the live version's visual language**

Compare `frame-end.png` against the Task 3 browser check (same route shape, same color treatment — solid vermilion route with a light halo, dark label pills). Minor easing/timing differences between the CSS and PIL renderers are expected and acceptable per the spec's "two independent implementations" design — flag only if the route shape, colors, or label content actually diverge.

- [ ] **Step 4: Clean up the test artifacts**

```bash
rm preview-motion/jalan-payoh-lai-route-walk-test.mp4 preview-motion/frame-start.png preview-motion/frame-mid.png preview-motion/frame-end.png
```

(`preview-motion/` is untracked/gitignored-in-spirit per its own `index.html` note — nothing here needs committing.)

No commit for this task — it's verification only.

---

### Task 6: Document the "Route animations" convention

**Files:**
- Modify: `CLAUDE.md`

**Interfaces:** none (documentation only).

- [ ] **Step 1: Add the convention section**

In `CLAUDE.md`, immediately after the existing `## Charts` section, add:

```markdown
## Route animations

When a passage describes a specific place or journey with no commercially-licensable
photo available (a demolished lane, an unmapped backlane, a walk through a place that
no longer exists), use a `route-walk` Watch slide instead of forcing an unrelated
stand-in photo: an animated route line over a real OpenStreetMap tile (ODbL-licensed,
commercial reuse permitted with attribution — never Google Maps or any other
non-freely-licensed map source). The route is hand-plotted against the tile as an
approximate stand-in that conveys a sense of distance and direction, not a claim of
precise historical accuracy.

Source an OSM export/screenshot covering the relevant area, then hand-plot landmark
nodes and a connecting path as pixel coordinates against that image (the same way
pan/zoom values are hand-set for photo slides). Preview the slide standalone as an
Artifact first, then check it in place via local Jekyll preview before publishing —
same pattern as Charts. Always credit "Map data © OpenStreetMap contributors" both
on-screen (small corner overlay) and in the post's Sources list. See
`docs/superpowers/specs/2026-08-20-route-walk-animation-design.md` for the full design,
and `scripts/render_route_clip.py` for the matching video-export renderer.
```

- [ ] **Step 2: Commit and push**

```bash
git add CLAUDE.md
git commit -m "Document the Route animations convention in CLAUDE.md"
git push
```

---

## Plan self-review notes

- **Spec coverage:** Architecture (Task 2 live renderer + Task 4 video renderer), Data model (node/path constants embedded in both, kept in sync by comment reference), Live rendering (Task 2), Video rendering (Task 4), Authoring workflow (Task 6 convention doc + this plan's own Task 1-2 sequence as the worked example), Testing/preview (Tasks 3 and 5). Non-goals (OSM-only, no AI generation, no coordinate-picker tool, no video-pipeline rebuild) are respected throughout — nothing in this plan introduces a coordinate picker, calls an image-generation API, or touches the existing photo-pan assembly process.
- **Open question left in the spec** ("does the video renderer's easing need to match the live SVG closely") is addressed pragmatically in Task 5 Step 3: visual language must match, frame-for-frame timing does not need to.
