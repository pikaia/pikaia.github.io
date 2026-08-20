# Route-walk animation: a new Watch slide type for unphotographable places

## Problem

Some passages describe a specific place or journey that no commercially-licensable
photo can represent — a demolished lane, an unmapped backlane shortcut, a kampong that
was cleared before it was ever photographed. Today the Watch widget's slide system only
supports panning/zooming over sourced photos, so these passages get stuck with a
loosely-related stand-in image (e.g. a river panorama standing in for "the walk from
the Upper Serangoon Road junction... along a backlane... called Holy Innocents' Lane"
in `_posts/2026-08-16-jalan-payoh-lai-kangkar-montfort-nativity-church.md`). This
undersells the moment the narration is actually describing.

## Goal

Add a new Watch slide type, `route-walk`, that depicts a described journey as an
animated route — a line that draws itself and a marker that walks along it — composited
over a real OpenStreetMap tile, instead of requiring a commercially-licensable photo of
a place that may no longer exist or was never photographed. OSM's data is ODbL-licensed,
which explicitly permits commercial reuse with attribution, so the tile gets the same
treatment as a sourced photo: credited, never presented as something else. The type must
work everywhere the existing photo slides work: the live in-browser Watch overlay, and
the baked .mp4s used for YouTube and Shorts.

## Non-goals

- Not AI image generation. No image-generation tool is used or assumed; the route/marker
  overlay is hand-coded SVG/CSS (live) and PIL-drawn frames (video), the same class of
  technique already used for the site's charts.
- Not Google Maps, or any other map source without a license that clears commercial
  reuse. This spec exists specifically to avoid re-introducing the licensing problem it's
  meant to solve — OpenStreetMap (ODbL) is the only map source used, always credited.
- Not a literal, precise historical route. Places like the backlane in the motivating
  example no longer exist on any map; the route drawn over the (present-day) OSM tile is
  an approximate stand-in that conveys a sense of distance and direction, not a claim of
  exact historical accuracy.
- Not a coordinate-picker tool or other new authoring UI. Waypoints and landmark
  positions are hand-set per post by eye against the sourced tile, the same way pan/zoom
  percentages are already hand-set for photo slides today.
- Not a rebuild of the existing photo-pan video pipeline. That pipeline stays exactly
  as it is (ad hoc ffmpeg zoompan, produced interactively); this spec only adds a new,
  separately-committed script for the new slide type.

## Architecture

`route-walk` becomes a third slide type alongside the existing `cover` and `letterbox`,
sharing the same per-post `slides` array and the same `imageSchedule` timeline that
already syncs slides to sentence-level narration offsets (see the `jalan-payoh-lai...`
post's inline script for the current pattern). A `route-walk` slide is rendered by two
independent implementations that both read the same waypoint/timing data for a given
post — mirroring how pan/zoom already exists twice today (CSS keyframes for the live
view, ffmpeg filter args for the video export) without the two drifting apart:

- **Live renderer** — inline SVG/CSS added to the post's own `<script>` block, following
  the existing per-post inline-widget convention (no shared JS file, no build step).
- **Video renderer** — a new committed Python script, `scripts/render_route_clip.py`,
  that produces an .mp4 segment via PIL + ffmpeg, spliced into the final video the same
  way photo-pan segments are today.

## Data model

A `route-walk` slide carries:

- **Map tile** — a single OSM export/screenshot covering the relevant area, saved
  alongside the post's other assets, credited as "Map data © OpenStreetMap contributors."
- **Nodes** — an ordered list of `{ label, x%, y% }` landmarks the route passes through,
  positioned as percentages of the tile image (e.g. "Jalan Payoh Lai", "Upper Serangoon
  Rd Junction", "Holy Innocents' Lane", "Montfort School").
- **Path** — an ordered list of `{x%, y%}` waypoints tracing the route between nodes,
  hand-plotted by Claude against the tile image, informed by whatever reference the user
  supplies in chat (old map, annotated screenshot, verbal description, or corrections
  against the tile itself).
- **Duration** — comes from the same sentence-offset schedule (`imageSchedule`) that
  already drives every other slide's timing; no new timing mechanism.

## Live rendering (Watch widget)

The widget's slide-building code gets a branch for `type: "route-walk"`. It reuses the
existing `letterbox` compositing already built for portrait/off-aspect photos: a
blurred, darkened full-bleed copy of the tile behind, and a sharp copy scaled to fit
("contain") in front. On top, an SVG `<path>` traces the route with a light halo stroke
behind a solid color stroke (so the line reads clearly regardless of what part of the
tile it crosses), animated via `stroke-dasharray`/`stroke-dashoffset` so it draws itself
over the slide's duration, plus a small pulsing marker that walks along the same path.
Landmark labels fade in as the marker passes each node — the same fade pattern the
widget already uses for captions, just re-triggered per-node instead of per-sentence. A
small always-visible attribution line ("Map data © OpenStreetMap contributors") sits in
a corner of the frame.

Validated in an Artifact prototype (three iterations: illustrated linework → real OSM
tile → corrected node placement) — see the "Open questions" resolution below for the
settled visual details.

## Video rendering

`scripts/render_route_clip.py` takes a post's `route-walk` slide data (tile image, nodes,
path, duration, target fps/resolution) and:

1. Composites the static letterboxed background (blurred full-bleed copy + sharp
   contained copy) from the tile image once with PIL, including the OSM attribution
   text baked in.
2. Renders N frames, each showing progressively more of the path stroked in (halo +
   color) and the marker advanced to the corresponding position (same easing/timing as
   the live SVG version, computed independently rather than shared code — consistent
   with the existing CSS/ffmpeg duality).
3. Pipes frames to ffmpeg (`image2pipe`) to encode an .mp4 segment at whatever
   resolution the target needs (16:9 for the YouTube cut, 9:16 crop for Shorts).

The resulting segment is concatenated into the final video the same way the existing
photo-pan segments are today (interactively, as has been done for prior posts) — this
spec does not change how segments get assembled, only adds a new kind of segment.

## Authoring workflow

Per post, when a passage has no free/commercially-licensable photo:

1. User (or Claude) sources an OSM export/screenshot covering the relevant area —
   Google Maps or any other non-freely-licensed map source is not an option (see
   Non-goals).
2. User supplies whatever additional reference helps Claude understand the route/
   geography (an old map, an annotated screenshot, a verbal description, corrections
   against the tile itself) — used only to inform node/path placement.
3. Claude hand-plots the node list and path waypoints as percentages against the tile
   image, the same way pan/zoom values are hand-set for photo slides today, and checks
   real street/landmark names against the tile rather than assuming.
4. Claude adds a short "Route animations" convention to `CLAUDE.md`, alongside the
   existing Charts/Photo galleries sections, documenting when to reach for this over
   sourcing a photo.

## Testing / preview

Same pattern as charts (per `CLAUDE.md`'s Charts convention): preview the `route-walk`
slide standalone as an Artifact first for fast iteration, then check it in place inside
the full post via local Jekyll preview (`jekyll serve --config _config.yml,_config_dev.yml`)
before publishing. For the video renderer, spot-check the exported clip before splicing
it into the final YouTube/Shorts video.

## Resolved during Artifact prototyping

- **Visual style**: settled via three prototype iterations. Base layer is a real OSM
  tile (not illustrated linework — too plain on its own). Route line is a solid color
  stroke over a lighter halo stroke, for legibility against the tile's own colors. Type
  pairing is Fraunces (italic, for landmark label pills) + IBM Plex Sans (UI/captions) +
  IBM Plex Mono (timestamps). Marker is a small pulsing dot, not a walking-figure icon.
- **Label/caption mechanism**: fade-in landmark labels driven by simple time thresholds
  against the same duration the route-draw animation uses worked fine in the prototype;
  no changes needed to the shared `imageSchedule`/`captionChunks` logic.
- **Live playback trigger**: the standalone prototype needed its own play button since
  it has no real audio to sync to. In the actual post, `route-walk` has no button of its
  own — it reads `watchAudio.currentTime` through the existing `updateForTime()` /
  `imageSchedule` machinery exactly like photo slides do.

## Open questions for implementation

- Whether the video renderer's route-draw easing needs to visually match the live SVG
  version closely, or just needs to look smooth on its own — not tested in the
  browser-only prototype.
