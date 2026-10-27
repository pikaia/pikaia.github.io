"""Build the avatar profile pictures in assets/avatar/profile/.

Stacks the cartoon avatar's exported layers (assets/avatar/png/, built by
build_avatar.py) into two flat 512x512 PNGs on white, for account and
channel profile pictures:

  lesser-known-singapore-cartoon-smile.png   eyes open, mouth closed (matches the channel icon)
  lesser-known-singapore-cartoon.png         eyes open, mouth slightly open

The SVG itself can't be used as a picture: it holds every mouth shape and
both eye states at once, so a browser draws them all on top of each other.

    python scripts/build_avatar_profile.py
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
LAYERS = ROOT / "assets" / "avatar" / "png"
OUT = ROOT / "assets" / "avatar" / "profile"

PICTURES = {
    "lesser-known-singapore-cartoon-smile.png": ["eyes-open", "mouth-0"],
    "lesser-known-singapore-cartoon.png": ["eyes-open", "mouth-1"],
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, layers in PICTURES.items():
        face = Image.open(LAYERS / "body.png").convert("RGBA")
        for layer in layers:
            face.alpha_composite(Image.open(LAYERS / f"{layer}.png").convert("RGBA"))
        flat = Image.new("RGBA", face.size, (255, 255, 255, 255))
        flat.alpha_composite(face)
        flat.convert("RGB").save(OUT / name, optimize=True)
        print(f"wrote {OUT / name}  ({face.size[0]}x{face.size[1]})")


if __name__ == "__main__":
    main()
