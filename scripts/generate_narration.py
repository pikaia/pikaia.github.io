"""Generate a narration MP3 for a blog post using edge-tts.

Local dev tool only - not part of the deployed Jekyll site. Extracts the
post's narrative paragraphs (skipping images, captions, back-links, and the
Sources section) and synthesizes them with a Microsoft Edge neural voice.

Usage:
    python scripts/generate_narration.py _posts/<file>.md audio/<slug>.mp3 [--voice en-SG-WayneNeural]
"""
import argparse
import asyncio
import re
import sys

import edge_tts

BACK_LINK_RE = re.compile(r"^\[←\s*Back to all posts\]\(/\)$")
GALLERY_LINK_RE = re.compile(r"\[See[^\]]*\]\([^)]*\)")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_CAPTION_RE = re.compile(r"^\*[^*].*[^*]\*$", re.DOTALL)


def extract_narrative(markdown_text: str) -> list[str]:
    # Drop front matter
    parts = markdown_text.split("---", 2)
    if markdown_text.startswith("---") and len(parts) >= 3:
        front_matter, body = parts[1], parts[2]
    else:
        front_matter, body = "", markdown_text

    title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', front_matter, re.MULTILINE)
    title = title_match.group(1) if title_match else ""

    blocks = [b.strip() for b in body.strip().split("\n\n")]

    narrative = [title] if title else []
    for block in blocks:
        if not block:
            continue
        if block == "---":
            break  # Sources divider - stop
        if block.startswith("!["):
            continue  # image
        if BACK_LINK_RE.match(block):
            continue
        if ITALIC_CAPTION_RE.match(block) and not block.startswith("**"):
            continue  # image caption

        cleaned = GALLERY_LINK_RE.sub("", block)
        cleaned = MD_LINK_RE.sub(r"\1", cleaned)
        cleaned = BOLD_RE.sub(r"\1", cleaned)
        cleaned = cleaned.strip()
        if cleaned:
            narrative.append(cleaned)

    return narrative


async def synthesize(text: str, voice: str, out_path: str) -> None:
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(out_path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("post_path")
    parser.add_argument("out_path")
    parser.add_argument("--voice", default="en-SG-WayneNeural")
    parser.add_argument("--dry-run", action="store_true", help="print extracted text only")
    args = parser.parse_args()

    with open(args.post_path, "r", encoding="utf-8") as f:
        markdown_text = f.read()

    narrative = extract_narrative(markdown_text)
    full_text = "\n\n".join(narrative)

    if args.dry_run:
        print(full_text)
        return

    print(f"Extracted {len(full_text)} characters, {len(narrative)} paragraphs.", file=sys.stderr)
    asyncio.run(synthesize(full_text, args.voice, args.out_path))
    print(f"Wrote {args.out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
