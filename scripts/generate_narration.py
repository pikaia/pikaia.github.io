"""Generate a narration MP3 for a blog post using edge-tts.

Local dev tool only - not part of the deployed Jekyll site. Extracts the
post's narrative paragraphs (skipping images, captions, back-links, and the
Sources section) and synthesizes them with a Microsoft Edge neural voice.

Also captures real per-sentence timestamps for free from edge-tts's
SentenceBoundary events (same API call, no extra cost) and writes them
alongside the audio as <out>.timing.json and <out>.srt - use these instead
of guessing at even timing splits when syncing captions/video to the audio.

Usage:
    python scripts/generate_narration.py _posts/<file>.md audio/<slug>.mp3 [--voice en-US-AvaMultilingualNeural]
"""
import argparse
import asyncio
import json
import os
import re
import sys

import edge_tts

BACK_LINK_RE = re.compile(r"^\[←\s*Back to all posts\]\(/\)$")
GALLERY_LINK_RE = re.compile(r"\[See[^\]]*\]\([^)]*\)")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_CAPTION_RE = re.compile(r"^\*[^*].*[^*]\*$", re.DOTALL)

# Raw-HTML block tags used in this codebase (floated images, charts, the
# listen widget). Whitelisted rather than matching any "<tag" generically,
# so JS/CSS content inside those blocks (e.g. "year < xMax") can't be
# mistaken for markup and thcorw off the depth count.
HTML_TAG_RE = re.compile(r"<(/?)(div|script|style|svg|audio|span|button|table|tr|td|th)\b", re.IGNORECASE)


def _process_block(block: str, narrative: list[str]) -> bool:
    """Returns False if this block signals the Sources divider (stop)."""
    if block == "---":
        return False
    if block.startswith("!["):
        return True  # image
    if BACK_LINK_RE.match(block):
        return True
    if ITALIC_CAPTION_RE.match(block) and not block.startswith("**"):
        return True  # image caption

    cleaned = GALLERY_LINK_RE.sub("", block)
    cleaned = MD_LINK_RE.sub(r"\1", cleaned)
    cleaned = BOLD_RE.sub(r"\1", cleaned)
    cleaned = cleaned.strip()
    if cleaned:
        narrative.append(cleaned)
    return True


def extract_narrative(markdown_text: str) -> list[str]:
    # Drop front matter
    parts = markdown_text.split("---", 2)
    if markdown_text.startswith("---") and len(parts) >= 3:
        front_matter, body = parts[1], parts[2]
    else:
        front_matter, body = "", markdown_text

    title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', front_matter, re.MULTILINE)
    title = title_match.group(1) if title_match else ""

    narrative = [title] if title else []
    buf: list[str] = []
    html_depth = 0

    def flush() -> bool:
        """Flush buffered prose lines as one block. Returns False to stop."""
        text = "\n".join(buf).strip()
        buf.clear()
        if not text:
            return True
        return _process_block(text, narrative)

    for line in body.strip("\n").split("\n"):
        if html_depth > 0:
            for m in HTML_TAG_RE.finditer(line):
                html_depth += -1 if m.group(1) else 1
            html_depth = max(html_depth, 0)
            continue

        if line.strip().startswith("<"):
            if not flush():
                return narrative
            for m in HTML_TAG_RE.finditer(line):
                html_depth += -1 if m.group(1) else 1
            html_depth = max(html_depth, 0)
            continue

        if line.strip() == "":
            if not flush():
                return narrative
            continue

        buf.append(line)

    flush()
    return narrative


async def synthesize(text: str, voice: str, out_path: str) -> None:
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(out_path)


async def synthesize_with_timing(text: str, voice: str, out_path: str) -> list[dict]:
    """Like synthesize(), but also captures real per-sentence timestamps
    from edge-tts's SentenceBoundary events (free, same API call). Writes
    <out_path>.timing.json (list of {text, offset_s, duration_s}) and
    <out_path>.srt alongside the audio. Returns the sentence list."""
    communicate = edge_tts.Communicate(text, voice)
    submaker = edge_tts.SubMaker()
    sentences: list[dict] = []

    with open(out_path, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                submaker.feed(chunk)
                sentences.append({
                    "text": chunk["text"],
                    "offset_s": chunk["offset"] / 10_000_000,
                    "duration_s": chunk["duration"] / 10_000_000,
                })

    base = os.path.splitext(out_path)[0]
    with open(f"{base}.timing.json", "w", encoding="utf-8") as f:
        json.dump(sentences, f, indent=2, ensure_ascii=False)
    with open(f"{base}.srt", "w", encoding="utf-8") as f:
        f.write(submaker.get_srt())

    return sentences


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("post_path")
    parser.add_argument("out_path")
    parser.add_argument("--voice", default="en-US-AvaMultilingualNeural")
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
    sentences = asyncio.run(synthesize_with_timing(full_text, args.voice, args.out_path))
    base = os.path.splitext(args.out_path)[0]
    print(f"Wrote {args.out_path}, {base}.timing.json, {base}.srt ({len(sentences)} sentences)", file=sys.stderr)


if __name__ == "__main__":
    main()
