# pikaia.github.io

Jekyll blog on Lesser Known Singapore — forgotten facts, obscure history, and overlooked people from Singapore's past and present. Hosted on GitHub Pages, `minima` theme. No Gemfile is committed (GitHub Pages builds it directly), but a local Jekyll install (Ruby + `jekyll`/`minima`/`jekyll-feed`/`jekyll-sitemap`/`jekyll-seo-tag` gems) is available on this machine for previewing posts before publishing — run `jekyll serve --config _config.yml,_config_dev.yml` from the repo root and view at `http://127.0.0.1:4000`. The `--config` flag layers `_config_dev.yml` (a local-only override, not read by GitHub Pages) on top, which prefixes the site title with "LOCAL —" in the browser tab so the local preview is never mistaken for the live site.

## Writing a new post

Always brainstorm before drafting. Do not generate post content until the topic, angle, and structure have been confirmed in conversation. Ask one question at a time.

1. **Topic** — confirm the subject if not already given.
2. **Angle** — what lens fits this topic (historical, present-day, policy/systems, person-focused, etc). Propose 2-3 options with a recommendation if it's not obvious.
3. **Structure** — sketch a short outline (e.g. vignette + context, or explainer) and get it approved before writing prose.
4. **Images** — confirm it's OK to source photos (default: yes, from Wikimedia Commons or similarly freely-licensed sources) unless the user says otherwise.

Keep this lightweight — a few chat questions, not a formal spec doc. Only write the post file once the outline is approved.

Keep the tone of posts objective and balanced — temper subjective commentary, since it could unnecessarily provoke reactions.

## Post conventions

- Files live in `_posts/`, named `YYYY-MM-DD-title-slug.md`.
- Front matter: `layout: post`, `title`, `date`, `last_modified_at`, `categories`, `image` (URL of the post's header/thumbnail image — also used as the small thumbnail next to the post link on the homepage, via the custom `_layouts/home.html`).
- `date` includes a time (e.g. `2026-07-18 09:00:00 +0800`), not just a day, so new posts sort correctly even when published the same calendar day. `last_modified_at` starts equal to `date`. The homepage (`_layouts/home.html`) sorts posts by `last_modified_at` descending, so it reflects post/update recency, not just original publish date.
- **Whenever an existing post's content is substantively edited** (not routine site-wide convention changes like this one), bump that post's `last_modified_at` to the current time — the homepage will then correctly move it to the top and show "Updated <date>" instead of the original publish date.
- The post's **first paragraph must come immediately after the front matter**, before any image or link. `show_excerpts: true` means Jekyll uses the first paragraph as the homepage teaser, so anything placed before it (images, the back-link) would leak onto the homepage instead of a proper excerpt.
- After that first paragraph, include a `[← Back to all posts](/)` link, then the header/thumbnail image as a hero, then 1-2 more images inline near the text they illustrate. Add the back-link again at the very end of the post too.
- Images are hotlinked directly from Wikimedia Commons (`upload.wikimedia.org`) — no binaries committed to the repo. Each image has an italicized caption crediting the author and license, on its own line separated from the image by a blank line (otherwise Markdown merges them into one paragraph and the caption wraps beside the image instead of sitting below it).
- **Any image narrower than half the post's content width must float** (e.g. a portrait-oriented photo sized to ~250-320px) so body text wraps beside it instead of leaving blank space on both sides — use a raw HTML `<div style="float: left; max-width: ...; margin: 0 1.5em 1em 0;">` wrapping the `<img>` and its caption `<em>`, and add `clear: both;` to whatever block follows (e.g. a chart's wrapper) so it doesn't overlap the floated image. Place the floated div *before* the paragraph that discusses it (not after), so that paragraph is the one that actually flows into the whitespace beside the image — putting the float after its paragraph leaves the image with nothing to wrap next to and wastes the space. Full-width landscape hero/inline images (e.g. skyline shots) don't need this — just center them normally.
- The `image` front matter value should match the header/hero image, and is used as the small thumbnail next to the post link on the homepage.
- Closing line is bolded, tying the post back to the blog's "overlooked/lesser-known" theme (e.g. `**Why it matters today:**`, `**Where it fits in the bigger story:**`).
- After the closing line, add a `---` divider and a **Sources** section: a bulleted list of markdown links to every fact source and image credit page actually used while researching/writing the post (article/dataset pages, not just the image URLs — link to the Wikimedia Commons file page, not the raw `upload.wikimedia.org` URL). Only list sources actually consulted. This goes before the final back-link.

## Photo galleries

Every post needs a companion gallery page with additional historical/vintage photos beyond the ones inline in the post itself. Aim for up to 20 images total across the whole post where possible — hero + inline images + gallery combined (this also gives posts with a Ken Burns-style "Watch" slideshow widget enough source images for a dynamic result). Fewer is fine if the topic is genuinely thin on real historical photography — never pad with weak or irrelevant images to hit the count.

- Gallery pages live in `_gallery/<slug>.md` (same slug as the post, no date prefix), rendered by `_layouts/gallery.html` via the `gallery` collection registered in `_config.yml` (permalink `/gallery/:path/`).
- Front matter: `layout: gallery`, `title` (e.g. `"More Historical Photos: <short topic label>"`), `post_url` (the post's actual permalink), `post_title` (must match the post's title exactly).
- Body: a one-sentence intro, then each photo as `### <short heading>`, the image via markdown `![alt](url)`, then an italicized caption on its own line (blank line separating it from the image, same rule as inline post images) crediting author/source/license exactly as shown on the image's Commons file page.
- Never duplicate an image URL that's already used inline in the post itself.
- In the post, add one line linking to the gallery (e.g. `[See more historical photos related to this post →](/gallery/<slug>/)`, adjusting the wording to the actual count), placed naturally in the prose near the end, before the closing bolded line. Append the gallery images' Commons file-page links to the post's own Sources list.
- Adding a gallery to an already-published post is a site-wide convention rollout, not a substantive content edit — don't bump `last_modified_at` for it.

## Charts

When a post calls for a chart (not just photos), load the `dataviz` skill and follow it — form choice, color-by-job, mark specs, hover interaction, accessibility (table fallback, ARIA label on the SVG). Source real data (e.g. data.gov.sg for HDB figures) rather than approximating from secondary articles when an authoritative dataset exists. Charts are self-contained inline HTML/SVG/JS embedded directly in the post's markdown (kramdown passes raw HTML through) — no external chart libraries, since the site has no JS build step. Preview the chart standalone as an Artifact first (fast iteration on an isolated chart), then check it again in place in the full post via the local Jekyll preview (see above) before publishing.

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

## Git

Commit and push directly without asking for confirmation for routine content changes (posts, images, about page). Still check before anything destructive (force-push, history rewrite, deleting content).
