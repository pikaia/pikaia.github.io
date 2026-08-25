"""Assemble a first-draft YouTube upload text file for a post's video + Short.

Local dev tool only - not part of the deployed Jekyll site. Produces
preview-motion/<slug>-youtube.txt (or wherever --out points), the staged
Title/Description text Chris pastes directly into YouTube Studio - see
docs/production-pipeline.md section 9 for the full staging step and
upload flow this feeds into.

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
        scripts/video-configs/<slug>.py \\
        scripts/video-configs/<slug>-short.py \\
        --post-url https://pikaia.github.io/YYYY/MM/DD/<slug>/ \\
        [--voice bm_george] [--out preview-motion/<slug>-youtube.txt]

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
COMMONS_THUMB_RE = re.compile(r'^(https://upload\.wikimedia\.org/wikipedia/commons)/thumb(/.+)/\d+px-[^/]+$')


def normalize_commons_url(url: str) -> str:
    """Wikimedia Commons thumbnail URLs (used in galleries for bandwidth,
    e.g. ".../thumb/8/87/File.jpg/960px-File.jpg") and full-res URLs
    (used in video configs, ".../8/87/File.jpg") point at the same file
    but don't match as strings - normalize thumbnails back to the
    canonical full-res form so caption lookups match across both."""
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
        return f"{m.group(1).strip()} [REVIEW CREDIT]"
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

        if pending_url and ITALIC_CAPTION_RE.match(block) and not block.startswith("**"):
            result[pending_url] = {"alt": pending_alt, "credit": extract_image_credit(block.strip("*").strip())}
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


def images_used_in_order(config_path: Path) -> list[str]:
    cfg = load_video_config(config_path)
    seen, ordered = set(), []
    for slide in cfg.SLIDES:
        key = slide.get("img")
        if not key:
            continue  # chart/route-walk slides have no single source image
        url = cfg.IMAGES[key]
        if url not in seen:
            seen.add(url)
            ordered.append(url)
    return ordered


def build_credit_lines(urls: list[str], captions: dict[str, dict[str, str]]) -> list[str]:
    lines = []
    for url in urls:
        info = captions.get(normalize_commons_url(url))
        if info:
            desc = info["alt"] or Path(urllib.parse.urlparse(url).path).stem
            lines.append(f"- {desc} — {info['credit']}")
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


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("post_path")
    ap.add_argument("main_config_path")
    ap.add_argument("short_config_path")
    ap.add_argument("--post-url", required=True, help="The post's real live permalink (check sitemap.xml first)")
    ap.add_argument("--voice", default="bm_george")
    ap.add_argument("--shortener", choices=["dagd", "tinyurl", "none"], default="dagd")
    ap.add_argument("--out", help="Defaults to preview-motion/<slug>-youtube.txt")
    args = ap.parse_args()

    post_path = Path(args.post_path)
    main_config_path = Path(args.main_config_path)
    short_config_path = Path(args.short_config_path)
    slug = main_config_path.stem

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

    main_images = images_used_in_order(main_config_path)
    short_images = images_used_in_order(short_config_path)

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
    out_lines.append("Images (Wikimedia Commons and NewspaperSG, credited individually):")
    out_lines.extend(build_credit_lines(main_images, captions))
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
    out_lines.append("Images (Wikimedia Commons):")
    out_lines.extend(build_credit_lines(short_images, captions))

    out_text = "\n".join(out_lines) + "\n"

    out_path = Path(args.out) if args.out else REPO_ROOT / "preview-motion" / f"{slug}-youtube.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out_text, encoding="utf-8")
    print(f"Wrote {out_path}", file=sys.stderr)

    review_count = out_text.count("[REVIEW CREDIT")
    if review_count:
        print(f"NOTE: {review_count} image credit(s) need manual review (marked [REVIEW CREDIT]).",
              file=sys.stderr)


if __name__ == "__main__":
    main()
