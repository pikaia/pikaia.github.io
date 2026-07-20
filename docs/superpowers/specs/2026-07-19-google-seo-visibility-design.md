# Make pikaia.github.io visible to Google Search

## Problem

The site has never been submitted to Google Search Console and has no `jekyll-seo-tag`
plugin enabled, so pages ship without a meta description, canonical URL, Open Graph
tags, or structured data. Between the missing crawl signal and the missing on-page SEO
metadata, Google has no real way to discover or understand the site.

## Goal

Get the site indexable and discoverable by Google. Not chasing search rankings or
competitive SEO — just making sure Google can find, crawl, and understand the pages
that already exist.

## Approach

1. **Enable `jekyll-seo-tag`** — add to `plugins:` in `_config.yml`, alongside the
   existing `jekyll-sitemap` and `jekyll-feed` entries. Minima's theme already calls
   `{% seo %}` in its head template, so enabling the plugin is sufficient to activate
   meta description, canonical link, Open Graph tags, and JSON-LD `Article` data,
   using the `title`/`description` already set in `_config.yml` and each post's first
   paragraph as the description source.
2. **Add `robots.txt`** at the repo root — explicit allow-all, pointing to
   `/sitemap.xml`. Not required for indexing (default is already crawl-everything) but
   standard practice.
3. **Verify post-deploy** — after GitHub Pages rebuilds, fetch the live homepage HTML
   and confirm the meta tags render as expected.
4. **Submit to Google Search Console** — via browser automation on the user's logged-in
   Chrome: add `pikaia.github.io` as a property, verify ownership, submit the sitemap,
   request indexing for the homepage.

## Explicitly out of scope

- Per-post custom `description` front matter (excerpt-based descriptions are already
  good given the posts' strong opening paragraphs).
- Twitter Card handles / social meta beyond what `jekyll-seo-tag` provides by default.
- Image alt-text audit, internal linking, or other ranking-oriented SEO work.

## Risks / notes

- GitHub Pages requires plugins to be explicitly whitelisted in `plugins:` (it doesn't
  auto-activate a theme's runtime gem dependencies) — same reason `jekyll-sitemap` and
  `jekyll-feed` are already listed there.
- Search Console verification method (HTML tag vs. domain/DNS vs. existing Google
  Analytics property) will be decided live based on what's fastest given the already
  configured GA4 property (`G-RPS2BGYR39`).
