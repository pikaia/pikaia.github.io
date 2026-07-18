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
- Each post gets a header image right after the front matter (before the first paragraph) as a thumbnail, plus 1-2 more images inline near the text they illustrate. The `image` front matter value should match this header image.
- Images are hotlinked directly from Wikimedia Commons (`upload.wikimedia.org`) — no binaries committed to the repo. Each image has an italicized caption crediting the author and license, on its own line separated from the image by a blank line (otherwise Markdown merges them into one paragraph and the caption wraps beside the image instead of sitting below it).
- Closing line is bolded, tying the post back to the blog's "overlooked/lesser-known" theme (e.g. `**Why it matters today:**`, `**Where it fits in the bigger story:**`).
- Include a `[← Back to all posts](/)` link right after the front matter (before the thumbnail) and again at the very end, so readers can return to the homepage without using the browser back button.

## Git

Commit and push directly without asking for confirmation for routine content changes (posts, images, about page). Still check before anything destructive (force-push, history rewrite, deleting content).
