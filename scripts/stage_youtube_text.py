"""Assemble a first-draft YouTube upload text file for a post's video + Short.

Local dev tool only - not part of the deployed Jekyll site. Produces
docs/youtube_helper/<slug>-youtube.txt (or wherever --out points), the
staged Title/Description text Chris pastes directly into YouTube Studio
- see docs/production-pipeline.md section 9 for the full staging step
and upload flow this feeds into. Unlike preview-motion/ (untracked
scratch - the rendered mp4s themselves), docs/youtube_helper/ is
git-tracked so these drafts keep real history.

This is a DRAFT generator, not a guarantee of publish-ready copy: the
hook paragraph, Sources list, and da.gd short link come out ready to use
as-is, but the per-image credit lines are extracted from each image's
own caption text with a best-effort regex (captions on this blog aren't
phrased 100% consistently - "(Photo: X / Y, LICENSE)" vs "Photo by X,
licensed under LICENSE." are both in use) - always skim the Images
section before pasting, especially any line ending in "[REVIEW CREDIT]".

Usage:
    python scripts/stage_youtube_text.py \\
        _posts/<file>.md \\
        [scripts/video-configs/<slug>.py] \\
        [scripts/video-configs/<slug>-short.py] \\
        --post-url https://pikaia.github.io/YYYY/MM/DD/<slug>/ \\
        [--voice bm_george] [--out docs/youtube_helper/<slug>-youtube.txt]

The two video-config paths are optional - a post that hasn't been
through the video pipeline yet (no scripts/video-configs/<slug>.py)
still gets a draft with Title/Description/Sources filled in; its Images
list is a placeholder instead of a real credit list, and the Short
section is a placeholder too when only the main config is given (or a
placeholder Images list, same as the main section, when both are given
but a particular one is missing/doesn't exist yet).

--post-url must be the post's real LIVE permalink (check sitemap.xml,
not the filename - a pre-08:00 SGT post date can build one calendar day
earlier than the filename implies, per docs/production-pipeline.md).
"""
import argparse
import importlib.util
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_narration import BOLD_RE, GALLERY_LINK_RE, ITALIC_CAPTION_RE, MD_LINK_RE  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
IMG_TAG_RE = re.compile(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*>')
IMG_ALT_RE = re.compile(r'\balt="([^"]*)"')
MD_IMG_RE = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)$')
EM_TAG_RE = re.compile(r'<em\b[^>]*>(.*?)</em>', re.DOTALL)
ITALIC_RE = re.compile(r'\*([^*]+)\*')
PHOTO_PAREN_RE = re.compile(r'\(Photo:\s*([^)]+)\)')
PHOTO_BY_RE = re.compile(r'Photo by\s+([^,]+),\s*licensed under\s+(.+?)\.?\s*$')
TRAILING_PAREN_RE = re.compile(r'\(([^()]+)\)\s*$')
BACK_LINK_RE = re.compile(r"^\[←\s*Back to all posts\]\(/\)$")
COMMONS_THUMB_RE = re.compile(r'^(https://upload\.wikimedia\.org/wikipedia/commons)/thumb(/.+?)/(?:lossy-page\d+-)?\d+px-[^/]+$')


def normalize_commons_url(url: str) -> str:
    """Wikimedia Commons thumbnail URLs and full-res URLs point at the
    same file but don't match as strings - normalize thumbnails back to
    the canonical form so caption lookups match across both. Handles the
    plain form (".../thumb/8/87/File.jpg/960px-File.jpg") and the
    multi-page form used for .tif/.pdf/.djvu, where the width segment is
    prefixed (".../thumb/3/3d/File.tif/lossy-page1-1280px-File.tif.jpg")
    - a chart/video config often requests a wider thumb than the gallery,
    so those two must still resolve to the same file."""
    m = COMMONS_THUMB_RE.match(url)
    return m.group(1) + m.group(2) if m else url


def clean_text(text: str) -> str:
    text = GALLERY_LINK_RE.sub("", text)
    text = MD_LINK_RE.sub(r"\1", text)
    text = BOLD_RE.sub(r"\1", text)
    # A caption's own book/publication title can be italicized with single
    # asterisks INSIDE the caption's outer *...* wrapper (e.g. "from
    # *Showa History Vol. 10*, public domain") - strip those too, after
    # BOLD_RE so **already-consumed** double-asterisks don't confuse this.
    text = ITALIC_RE.sub(r"\1", text)
    return text.strip()


def split_blocks(body: str) -> list[str]:
    blocks, buf = [], []
    for line in body.strip("\n").split("\n"):
        if line.strip() == "":
            if buf:
                blocks.append("\n".join(buf).strip())
                buf = []
        else:
            buf.append(line)
    if buf:
        blocks.append("\n".join(buf).strip())
    return blocks


def parse_front_matter(text: str) -> tuple[dict, str]:
    parts = text.split("---", 2)
    if not (text.startswith("---") and len(parts) >= 3):
        return {}, text
    fm_text, body = parts[1], parts[2]
    fm = {}
    for m in re.finditer(r'^(\w+):\s*"?(.+?)"?\s*$', fm_text, re.MULTILINE):
        fm[m.group(1)] = m.group(2)
    return fm, body


def extract_hook(body: str) -> str:
    """First real prose block - the post's own opening paragraph, per the
    'first paragraph comes immediately after front matter' convention."""
    for block in split_blocks(body):
        if block == "---" or BACK_LINK_RE.match(block) or block.startswith(("!", "<")):
            continue
        return clean_text(block)
    return ""


def extract_image_credit(raw_caption: str) -> str:
    """Best-effort author/license extraction from a caption's free text
    (markdown links already stripped by the caller). Tries known phrasing
    patterns in order of reliability, falling through to a flagged trailing
    parenthetical or the raw text when nothing matches cleanly."""
    caption = clean_text(raw_caption)
    m = PHOTO_PAREN_RE.search(caption)
    if m:
        inner = m.group(1)
        if "," in inner:
            source, license_ = inner.rsplit(",", 1)
            author = source.split("/")[0].strip()
            return f"{author}, {license_.strip()}"
        return inner.strip()
    m = PHOTO_BY_RE.search(caption)
    if m:
        return f"{m.group(1).strip()}, {m.group(2).strip()}"
    m = TRAILING_PAREN_RE.search(caption)
    if m:
        inner = m.group(1).strip()
        # An OpenStreetMap map-data credit ("Map data: (c) OpenStreetMap
        # contributors") is already the complete, correct attribution -
        # there's no author/licence to split out, so take it as-is.
        if re.search(r'OpenStreetMap|Map data', inner):
            return re.sub(r'^Map data:\s*', '', inner).strip()
        # "<source> / Wikimedia Commons, public domain" and similar - an
        # institutional/PD credit with no named photographer and no CC
        # licence, so PHOTO_PAREN_RE / PHOTO_BY_RE don't catch it. Split
        # it the same way as the (Photo: ...) branch when it's clearly a
        # credit (mentions a known repository or licence token).
        if "," in inner and re.search(r'Wikimedia Commons|NewspaperSG|public domain|CC[ -]|GFDL|Open Government', inner):
            source, license_ = inner.rsplit(",", 1)
            return f"{source.split('/')[0].strip()}, {license_.strip()}"
        return f"{inner} [REVIEW CREDIT]"
    return f"{caption} [REVIEW CREDIT]"


def _pair_from_block(block: str) -> tuple[str, str, str] | None:
    """If a single block contains both an image and its caption (the
    floated-<div> pattern - <img> and <em>caption</em> with no blank line
    between them), extract (url, alt, raw_caption) directly."""
    em_m = EM_TAG_RE.search(block)
    if not em_m:
        return None
    img_m = IMG_TAG_RE.search(block) or MD_IMG_RE.search(block)
    if not img_m:
        return None
    url = img_m.group(1) if img_m.re is IMG_TAG_RE else img_m.group(2)
    alt = ""
    if img_m.re is IMG_TAG_RE:
        alt_m = IMG_ALT_RE.search(block)
        alt = alt_m.group(1) if alt_m else ""
    else:
        alt = img_m.group(1)
    return url, alt, em_m.group(1)


def extract_image_captions(text: str) -> dict[str, dict[str, str]]:
    """Walks a post/gallery's markdown blocks, pairing each image (markdown
    ![]() or raw HTML <img src=...>) with its caption. Handles two layouts
    used on this blog: a plain image block followed by a separate italic
    (*...*) caption block, and the floated-<div> pattern where <img> and
    <em>caption</em> sit together with no blank line between them. Returns
    {url: {"alt": ..., "credit": ...}}."""
    result: dict[str, dict[str, str]] = {}
    blocks = split_blocks(text)
    pending_url = None
    pending_alt = None
    for block in blocks:
        combined = _pair_from_block(block)
        if combined:
            url, alt, raw_caption = combined
            result[normalize_commons_url(url)] = {"alt": alt, "credit": extract_image_credit(raw_caption)}
            pending_url = None
            continue

        img_url = None
        alt = ""
        md_m = MD_IMG_RE.match(block)
        if md_m:
            alt, img_url = md_m.group(1), md_m.group(2)
        else:
            html_m = IMG_TAG_RE.search(block)
            if html_m and "<em" not in block:
                img_url = html_m.group(1)
                alt_m = IMG_ALT_RE.search(block)
                alt = alt_m.group(1) if alt_m else ""

        if img_url:
            pending_url, pending_alt = normalize_commons_url(img_url), alt
            continue

        caption = None
        if ITALIC_CAPTION_RE.match(block) and not block.startswith("**"):
            caption = block.strip("*").strip()
        else:
            # A lone <em>...</em> caption block, blank-line-separated from
            # its <img> - the float-<div> convention CLAUDE.md documents
            # ("caption ... on its own line separated from the image by a
            # blank line"), including several stacked <img>/<em> pairs in
            # one div. split_blocks() puts the <em> in its own block,
            # optionally still carrying the div's own opening/closing tag.
            em_m = EM_TAG_RE.search(block)
            if em_m and not IMG_TAG_RE.search(block):
                bare = re.sub(r'</?div\b[^>]*>', '', block).strip()
                if bare.startswith("<em") and bare.endswith("</em>"):
                    caption = em_m.group(1).strip()

        if pending_url and caption is not None:
            result[pending_url] = {"alt": pending_alt, "credit": extract_image_credit(caption)}
        pending_url = None

    return result


# Greedy (not MD_LINK_RE's non-greedy [^)]+) so a URL containing literal
# parentheses - e.g. a Commons File: link like
# ".../File:Albert_Winsemius_(1971).jpg" - doesn't truncate the match at
# the first ")" inside the URL instead of the link's real closing paren.
SOURCE_LINK_RE = re.compile(r'^\[(.+)\]\(.+\)$')


def extract_sources(text: str) -> list[str]:
    m = re.search(r'\*\*Sources:?\*\*\s*\n(.+?)(?:\n\n|\Z)', text, re.DOTALL)
    if not m:
        return []
    lines = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        link_m = SOURCE_LINK_RE.match(line[2:])
        lines.append("- " + (link_m.group(1) if link_m else clean_text(line[2:])))
    return lines


def load_video_config(config_path: Path):
    spec = importlib.util.spec_from_file_location(config_path.stem, config_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def images_used_in_order(config_path: Path | None) -> tuple[list[str] | None, dict[str, str]]:
    """(ordered image URLs, {url: credit}). The URL list is None (not an
    empty list) when no config was given or the path doesn't exist yet -
    the caller needs to tell "video not built" apart from "video built
    with zero photo slides" (e.g. an all-chart config), which render as
    different output. The credit map comes from an optional `CREDITS`
    dict in the config ({IMAGES key: credit line}) - used for a slide
    whose image isn't a captioned Commons file, e.g. a chart PNG the site
    renders itself (assets/images/...). Anything not covered by a
    post/gallery caption or this map still gets flagged [REVIEW CREDIT]."""
    if config_path is None or not config_path.exists():
        return None, {}
    cfg = load_video_config(config_path)
    config_credits = getattr(cfg, "CREDITS", {})
    seen, ordered, credits = set(), [], {}
    for slide in cfg.SLIDES:
        key = slide.get("img")
        if not key:
            continue  # chart/route-walk slides have no single source image
        url = cfg.IMAGES[key]
        if url not in seen:
            seen.add(url)
            ordered.append(url)
            if key in config_credits:
                credits[url] = config_credits[key]
    return ordered, credits


NO_VIDEO_PLACEHOLDER = ("[PLACEHOLDER - no video built yet for this post; run the production "
                         "pipeline first (docs/production-pipeline.md), then re-run this script "
                         "with the resulting scripts/video-configs/<slug>.py]")

# href="..." followed later by an aria-label naming YouTube - matches this
# blog's established widget-row markup (see docs/production-pipeline.md
# section 11) regardless of attribute order.
YOUTUBE_HREF_RE = re.compile(r'href="(https://(?:youtu\.be|(?:www\.)?youtube\.com)/[^"]+)"')


def find_existing_youtube_urls(text: str) -> tuple[str | None, str | None]:
    """A post from BEFORE the scripts/video-configs/ pipeline existed can
    already have a real, published video with no committed config to read
    - that's a different situation from "no video was ever built" and
    deserves a different placeholder message, not a claim that no video
    exists. Classifies by whether the URL itself contains "/shorts/"."""
    main_url, short_url = None, None
    for m in YOUTUBE_HREF_RE.finditer(text):
        url = m.group(1)
        if "/shorts/" in url:
            short_url = short_url or url
        else:
            main_url = main_url or url
    return main_url, short_url


def build_credit_lines(urls: list[str] | None, captions: dict[str, dict[str, str]],
                        config_credits: dict[str, str] | None = None,
                        existing_video_url: str | None = None) -> list[str]:
    if urls is None:
        if existing_video_url:
            return [f"[Video already published at {existing_video_url}, but predates the "
                    f"scripts/video-configs/ pipeline - no committed config exists to auto-generate "
                    f"this Images list. Fill in manually from the post's own image credits, or build "
                    f"a config retroactively and re-run this script.]"]
        return [NO_VIDEO_PLACEHOLDER]
    config_credits = config_credits or {}
    lines = []
    for url in urls:
        info = captions.get(normalize_commons_url(url))
        if info:
            desc = info["alt"] or Path(urllib.parse.urlparse(url).path).stem
            lines.append(f"- {desc} — {info['credit']}")
        elif url in config_credits:
            lines.append(f"- {config_credits[url]}")
        else:
            lines.append(f"- {url} [REVIEW CREDIT - not found in post/gallery captions]")
    return lines


def shorten_url(url: str, method: str) -> str:
    if method == "none":
        return url
    attempts = {
        "dagd": f"https://da.gd/shorten?url={urllib.parse.quote(url, safe='')}",
        "tinyurl": f"https://tinyurl.com/api-create.php?url={urllib.parse.quote(url, safe='')}",
    }
    endpoint = attempts[method]
    for attempt in range(3):
        try:
            with urllib.request.urlopen(endpoint, timeout=15) as resp:
                short = resp.read().decode("utf-8").strip()
                if short.startswith("http"):
                    return short
        except (urllib.error.URLError, TimeoutError):
            continue
    print(f"WARNING: {method} shortening failed after 3 attempts; using the raw URL. "
          f"Retry with --shortener tinyurl or shorten manually.", file=sys.stderr)
    return url


POST_DATE_PREFIX_RE = re.compile(r'^\d{4}-\d{2}-\d{2}-')


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("post_path")
    ap.add_argument("main_config_path", nargs="?", default=None,
                     help="scripts/video-configs/<slug>.py - omit if no video's been built yet")
    ap.add_argument("short_config_path", nargs="?", default=None,
                     help="scripts/video-configs/<slug>-short.py - omit if no Short's been built yet")
    ap.add_argument("--post-url", required=True, help="The post's real live permalink (check sitemap.xml first)")
    ap.add_argument("--voice", default="bm_george")
    ap.add_argument("--shortener", choices=["dagd", "tinyurl", "none"], default="dagd")
    ap.add_argument("--out", help="Defaults to docs/youtube_helper/<slug>-youtube.txt")
    args = ap.parse_args()

    post_path = Path(args.post_path)
    main_config_path = Path(args.main_config_path) if args.main_config_path else None
    short_config_path = Path(args.short_config_path) if args.short_config_path else None
    slug = main_config_path.stem if main_config_path else POST_DATE_PREFIX_RE.sub("", post_path.stem)

    post_text = post_path.read_text(encoding="utf-8")
    fm, body = parse_front_matter(post_text)
    title = fm.get("title", slug)
    hook = extract_hook(body)
    sources = extract_sources(post_text)

    captions = extract_image_captions(post_text)
    gallery_path = REPO_ROOT / "_gallery" / f"{slug}.md"
    if gallery_path.exists():
        captions.update({k: v for k, v in extract_image_captions(gallery_path.read_text(encoding="utf-8")).items()
                          if k not in captions})

    main_images, main_credits = images_used_in_order(main_config_path)
    short_images, short_credits = images_used_in_order(short_config_path)
    existing_main_url, existing_short_url = find_existing_youtube_urls(post_text)

    short_url = shorten_url(args.post_url, args.shortener)
    narration_line = (f"Narration: synthesized voice (Kokoro TTS, open-source, "
                       f"Apache 2.0 license, voice {args.voice})")

    out_lines = []
    out_lines.append("=== FULL VIDEO ===")
    out_lines.append("")
    out_lines.append("Title:")
    out_lines.append(title)
    out_lines.append("")
    out_lines.append("Description:")
    out_lines.append(hook)
    out_lines.append("")
    out_lines.append(f"Full story: {short_url}")
    out_lines.append("")
    out_lines.append(narration_line)
    out_lines.append("")
    if main_images is not None:
        out_lines.append("Images (Wikimedia Commons and NewspaperSG, credited individually):")
    out_lines.extend(build_credit_lines(main_images, captions, main_credits, existing_main_url))
    if sources:
        out_lines.append("")
        out_lines.append("Sources:")
        out_lines.extend(sources)
    out_lines.append("")
    out_lines.append("-" * 70)
    out_lines.append("")
    out_lines.append("=== SHORT ===")
    out_lines.append("")
    out_lines.append("Title:")
    out_lines.append(f"{title} #Shorts")
    out_lines.append("")
    out_lines.append("Description:")
    out_lines.append(f"{hook} #Shorts")
    out_lines.append("")
    out_lines.append(f"Full story: {short_url}")
    out_lines.append("Full-length video: <paste the main video's URL here after uploading it>")
    out_lines.append("")
    out_lines.append(narration_line)
    out_lines.append("")
    if short_images is not None:
        out_lines.append("Images (Wikimedia Commons):")
    out_lines.extend(build_credit_lines(short_images, captions, short_credits, existing_short_url))

    out_text = "\n".join(out_lines) + "\n"

    out_path = Path(args.out) if args.out else REPO_ROOT / "docs" / "youtube_helper" / f"{slug}-youtube.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out_text, encoding="utf-8")
    print(f"Wrote {out_path}", file=sys.stderr)

    review_count = out_text.count("[REVIEW CREDIT")
    if review_count:
        print(f"NOTE: {review_count} image credit(s) need manual review (marked [REVIEW CREDIT]).",
              file=sys.stderr)


if __name__ == "__main__":
    main()
