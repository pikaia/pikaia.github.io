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

Add a new Watch slide type, `route-walk`, that depicts a described journey as original
vector art — simplified roads/landmarks with a route line that draws itself and a
marker that walks along it — instead of requiring a real photo. Because the art is
drawn by hand (by Claude, per-post) rather than sourced, it sidesteps image licensing
entirely: there is nothing to credit or clear. The type must work everywhere the
existing photo slides work: the live in-browser Watch overlay, and the baked .mp4s used
for YouTube and Shorts.

## Non-goals

- Not AI image generation. No image-generation tool is used or assumed; this is
  hand-coded SVG/CSS (live) and PIL-drawn frames (video), the same class of technique
  already used for the site's charts.
- Not a literal redraw of any sourced map or copyrighted reference. Any map, screenshot,
  or sketch the user provides is used only as private compositional reference for the
  route's shape — never published, never a background layer in the final art.
- Not a coordinate-picker tool or other new authoring UI. Waypoints and landmark
  positions are hand-set per post, the same way pan/zoom percentages are already
  hand-set for photo slides today.
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

A `route-walk` slide carries, in illustration space (percentages, not real-world
coordinates):

- **Nodes** — an ordered list of `{ label, x%, y% }` landmarks the route passes through
  (e.g. "Upper Serangoon Rd junction", "Holy Innocents' Lane", "Montfort School").
- **Path** — an ordered list of `{x%, y%}` waypoints tracing the route between nodes,
  hand-composed by Claude from whatever reference the user supplies in chat (old map,
  annotated screenshot, verbal description).
- **Duration** — comes from the same sentence-offset schedule (`imageSchedule`) that
  already drives every other slide's timing; no new timing mechanism.

## Live rendering (Watch widget)

The widget's slide-building code gets a branch for `type: "route-walk"`: it renders an
SVG containing simplified line-art (roads as strokes, landmark nodes as small
labeled markers) composited per-post, plus a `<path>` for the route animated via
`stroke-dasharray`/`stroke-dashoffset` so it draws itself over the slide's duration, and
a marker element animated along the same path via `<animateMotion>`. Landmark labels
fade in as the marker passes each node — the same fade pattern the widget already uses
for captions, just re-triggered per-node instead of per-sentence.

## Video rendering

`scripts/render_route_clip.py` takes a post's `route-walk` slide data (nodes, path,
duration, target fps/resolution) and:

1. Draws the static line-art background once with PIL.
2. Renders N frames, each showing progressively more of the path stroked in and the
   marker advanced to the corresponding position (same easing/timing as the live SVG
   version, computed independently rather than shared code — consistent with the
   existing CSS/ffmpeg duality).
3. Pipes frames to ffmpeg (`image2pipe`) to encode an .mp4 segment at whatever
   resolution the target needs (16:9 for the YouTube cut, 9:16 crop for Shorts).

The resulting segment is concatenated into the final video the same way the existing
photo-pan segments are today (interactively, as has been done for prior posts) — this
spec does not change how segments get assembled, only adds a new kind of segment.

## Authoring workflow

Per post, when a passage has no free/commercially-licensable photo:

1. User supplies whatever reference helps Claude understand the route/geography (an old
   map, an annotated screenshot, a verbal description) — shared only in chat, never
   published or used as a background layer.
2. Claude hand-composes the node list and path waypoints in illustration-space
   percentages, the same way pan/zoom values are hand-set for photo slides today.
3. Claude adds a short "Route animations" convention to `CLAUDE.md`, alongside the
   existing Charts/Photo galleries sections, documenting when to reach for this over
   sourcing a photo.

## Testing / preview

Same pattern as charts (per `CLAUDE.md`'s Charts convention): preview the `route-walk`
slide standalone as an Artifact first for fast iteration, then check it in place inside
the full post via local Jekyll preview (`jekyll serve --config _config.yml,_config_dev.yml`)
before publishing. For the video renderer, spot-check the exported clip before splicing
it into the final YouTube/Shorts video.

## Open questions for implementation

- Exact visual style (line weight, color palette, marker design — dot vs. simple
  walking-figure icon) is not fixed here; first implementation should propose a look
  consistent with the rest of the site and confirm via the Artifact preview step above.
- Whether the fade-in caption/label mechanism needs any changes to the shared
  `imageSchedule`/`captionChunks` logic, or can piggyback on it unmodified, will be
  clarified during implementation of the first real post that uses this slide type.
