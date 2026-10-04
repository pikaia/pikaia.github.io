"""Look up Wikimedia Commons files for a post: licence, author, size, a
hotlinkable upload.wikimedia.org thumbnail URL, and a labelled contact sheet.

    python scripts/commons_info.py titles.txt out.json [--width 1280] [--sheet sheet.png]

titles.txt has one "File:..." title per line. out.json maps each title to
{url, thumb, page, w, h, lic, artist, date, desc}; `thumb` is the
upload.wikimedia.org thumbnail at --width (the form posts hotlink), `page` the
Commons file page for the Sources list. --sheet also downloads small previews
and tiles them into one image to look at. Requests are paced and retried on
HTTP 429, which Commons returns when hit too fast.
"""

import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

UA = {"User-Agent": "pikaia-blog-research/1.0 (one-off image research for a blog post)"}
API = "https://commons.wikimedia.org/w/api.php?"


def get(url, tries=6):
    for attempt in range(tries):
        try:
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code != 429 or attempt == tries - 1:
                raise
            time.sleep(10 * (attempt + 1))


def strip_html(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


def upload_url(thumb):
    """Commons sometimes answers with thumb.wikimedia.org; posts hotlink upload.wikimedia.org."""
    return thumb.split("?")[0].replace("https://thumb.wikimedia.org/", "https://upload.wikimedia.org/")


def lookup(titles, width=1280):
    out = {}
    for i in range(0, len(titles), 20):
        q = urllib.parse.urlencode({"action": "query", "prop": "imageinfo", "format": "json",
                                    "iiprop": "url|size|extmetadata|user", "iiurlwidth": width,
                                    "titles": "|".join(titles[i:i + 20])})
        data = json.loads(get(API + q))
        for p in data["query"]["pages"].values():
            if "imageinfo" not in p:
                print("MISSING", p["title"])
                continue
            ii = p["imageinfo"][0]
            m = ii.get("extmetadata", {})
            val = lambda k: strip_html(m.get(k, {}).get("value", ""))  # noqa: E731
            out[p["title"]] = dict(url=ii["url"], thumb=upload_url(ii.get("thumburl", ii["url"])),
                                   page=ii["descriptionurl"], w=ii["width"], h=ii["height"],
                                   lic=val("LicenseShortName"), artist=val("Artist")[:120] or f"(uploader) {ii['user']}",
                                   date=val("DateTimeOriginal")[:60], desc=val("ImageDescription")[:200])
        time.sleep(2)
    return out


def contact_sheet(info, path, cols=4, tile=(380, 260)):
    from PIL import Image, ImageDraw
    import io
    tiles = []
    for title, v in info.items():
        im = Image.open(io.BytesIO(get(v["thumb"]))).convert("RGB")
        im.thumbnail(tile)
        tiles.append((title[5:50], im))
        time.sleep(2)
    rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (tile[0] + 10), rows * (tile[1] + 25)), "white")
    d = ImageDraw.Draw(sheet)
    for n, (label, im) in enumerate(tiles):
        x, y = (n % cols) * (tile[0] + 10), (n // cols) * (tile[1] + 25)
        sheet.paste(im, (x, y + 18))
        d.text((x + 2, y + 2), f"{n:02d} {label}", fill=(200, 0, 0))
    sheet.save(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("titles")
    ap.add_argument("out")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--sheet")
    args = ap.parse_args()
    titles = [t.strip() for t in Path(args.titles).read_text(encoding="utf-8").splitlines() if t.strip()]
    info = lookup(titles, args.width)
    Path(args.out).write_text(json.dumps(info, indent=1, ensure_ascii=False), encoding="utf-8")
    for t, v in info.items():
        print(f"{t}\n   {v['w']}x{v['h']} | {v['lic']} | {v['artist']} | {v['date']}\n   {v['desc'][:120]}")
    if args.sheet:
        contact_sheet(info, args.sheet)
        print("wrote", args.sheet)


if __name__ == "__main__":
    main()
