# pikaia.github.io

Jekyll blog on Lesser Known Singapore — forgotten facts, obscure history, and overlooked people from Singapore's past and present. Hosted on GitHub Pages, `minima` theme, no local build step.

## Writing a new post

Always brainstorm before drafting. Do not generate post content until the topic, angle, and structure have been confirmed in conversation. Ask one question at a time.

1. **Topic** — confirm the subject if not already given.
2. **Angle** — what lens fits this topic (historical, present-day, policy/systems, person-focused, etc). Propose 2-3 options with a recommendation if it's not obvious.
3. **Structure** — sketch a short outline (e.g. vignette + context, or explainer) and get it approved before writing prose.
4. **Images** — confirm it's OK to source photos (default: yes, from Wikimedia Commons or similarly freely-licensed sources) unless the user says otherwise.

Keep this lightweight — a few chat questions, not a formal spec doc. Only write the post file once the outline is approved.

## Post conventions

- Files live in `_posts/`, named `YYYY-MM-DD-title-slug.md`.
- Front matter: `layout: post`, `title`, `date`, `categories`, `image` (URL of the post's header/thumbnail image — also used as the small thumbnail next to the post link on the homepage, via the custom `_layouts/home.html`).
- The post's **first paragraph must come immediately after the front matter**, before any image or link. `show_excerpts: true` means Jekyll uses the first paragraph as the homepage teaser, so anything placed before it (images, the back-link) would leak onto the homepage instead of a proper excerpt.
- After that first paragraph, include a `[← Back to all posts](/)` link, then the header/thumbnail image as a hero, then 1-2 more images inline near the text they illustrate. Add the back-link again at the very end of the post too.
- Images are hotlinked directly from Wikimedia Commons (`upload.wikimedia.org`) — no binaries committed to the repo. Each image has an italicized caption crediting the author and license, on its own line separated from the image by a blank line (otherwise Markdown merges them into one paragraph and the caption wraps beside the image instead of sitting below it).
- The `image` front matter value should match the header/hero image, and is used as the small thumbnail next to the post link on the homepage.
- Closing line is bolded, tying the post back to the blog's "overlooked/lesser-known" theme (e.g. `**Why it matters today:**`, `**Where it fits in the bigger story:**`).

## Charts

When a post calls for a chart (not just photos), load the `dataviz` skill and follow it — form choice, color-by-job, mark specs, hover interaction, accessibility (table fallback, ARIA label on the SVG). Source real data (e.g. data.gov.sg for HDB figures) rather than approximating from secondary articles when an authoritative dataset exists. Charts are self-contained inline HTML/SVG/JS embedded directly in the post's markdown (kramdown passes raw HTML through) — no external chart libraries, since the site has no JS build step. Preview the chart as a standalone Artifact before embedding, since there's no local Jekyll to render it in.

## Git

Commit and push directly without asking for confirmation for routine content changes (posts, images, about page). Still check before anything destructive (force-push, history rewrite, deleting content).
