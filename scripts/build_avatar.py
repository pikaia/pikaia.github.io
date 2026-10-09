"""Rasterise the layered avatar SVG into the PNG layers the renderer stacks.

    python scripts/build_avatar.py [--svg assets/avatar/avatar.svg] [--size 512]

Each name in avatar_lib.ALL_LAYER_NAMES is a <g id=...> in the SVG (the
motion parts are optional). For each, every *other* named layer is hidden and the result rendered to a
transparent square PNG in assets/avatar/png/, so all layers share one
canvas and stack with no offsets. The PNGs are committed (a binary
exception, like the OSM tiles), so rendering a video doesn't need
resvg-py; re-run this only when the SVG changes. resvg-py is a
self-contained wheel - no Cairo DLLs, no network.
"""

import argparse
import io
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avatar_lib import ALL_LAYER_NAMES, LAYER_NAMES, PNG_DIR, SVG_PATH  # noqa: E402

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def layer_svg(svg_text, keep):
    """The SVG with every named layer hidden except `keep`, its ancestors and
    its descendants - so a nested motion part (head inside body) renders
    alone, and body still renders with everything inside it."""
    root = ET.fromstring(svg_text)
    parent = {c: p for p in root.iter() for c in p}
    found = {el.get("id"): el for el in root.iter() if el.get("id") in ALL_LAYER_NAMES}
    missing = [n for n in LAYER_NAMES if n not in found]
    if missing:
        raise ValueError(f"avatar SVG is missing layer group(s): {', '.join(missing)}")
    target = found[keep]
    ancestors, el = set(), target
    while el in parent:
        el = parent[el]
        ancestors.add(el)
    descendants = set(target.iter())
    for el in found.values():
        if el is not target and el not in ancestors and el not in descendants:
            el.set("style", "display:none")
    return ET.tostring(root, encoding="unicode")


def render_png(svg_text, size):
    import resvg_py
    data = resvg_py.svg_to_bytes(svg_string=svg_text, width=size, height=size)
    return Image.open(io.BytesIO(bytes(data))).convert("RGBA")


def build_layers(svg_path, png_dir, size=512):
    svg_text = Path(svg_path).read_text(encoding="utf-8")
    png_dir = Path(png_dir)
    png_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    svg_ids = {el.get("id") for el in ET.fromstring(svg_text).iter()}
    for name in [n for n in ALL_LAYER_NAMES if n in LAYER_NAMES or n in svg_ids]:
        img = render_png(layer_svg(svg_text, name), size)
        if img.size != (size, size):
            img = img.resize((size, size), Image.LANCZOS)
        path = png_dir / f"{name}.png"
        img.save(path)
        paths.append(path)
    return paths


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--svg", default=str(SVG_PATH))
    ap.add_argument("--out-dir", default=str(PNG_DIR))
    ap.add_argument("--size", type=int, default=512)
    args = ap.parse_args()
    for p in build_layers(args.svg, args.out_dir, args.size):
        print(f"Wrote {p}")


if __name__ == "__main__":
    main()
