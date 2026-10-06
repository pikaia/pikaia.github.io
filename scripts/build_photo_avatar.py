"""Build the photo avatar's PNG layers from nine photos of Chris.

    python scripts/build_photo_avatar.py [--spec assets/avatar/photo/shots.json]
                                         [--photos scratch/avatar-photos]

The photo counterpart of build_avatar.py: writes the same layer names
(body, eyes-open, eyes-closed, mouth-0..3, mouth-M/F/U/E, 512px RGBA) into
assets/avatar/photo/png/, which render_avatar_track.py uses when a config
sets AVATAR "style": "photo". The source photos stay in scratch/ and are
never committed; shots.json (committed) names which file is which shot and
where the face sits in the resting photo, so the layers can be rebuilt.

How: the resting photo is the base. Each other shot is aligned to it (SIFT
on the upper face - glasses, eyes, brows, nose - then a similarity
transform), colour-nudged to the base using the cheeks only, and its mouth
(or, for the blink, eye) area cut out with a feathered ellipse. The base's
background is replaced with the cartoon bubble's dark blue using a person
mask (torchvision DeepLabV3, weights downloaded once from pytorch.org,
refined with GrabCut). Lessons from the first build (2026-10-06): all nine
shots must come from ONE sitting with the camera untouched - mixing
sessions shows as colour and position flicker - and the colour sample must
stay on the cheeks (a ring reaching the shirt tints the patch).
"""

import argparse
import json
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avatar_lib import AVATAR_DIR, PHOTO_PNG_DIR, REPO_ROOT  # noqa: E402

SPEC = AVATAR_DIR / "photo" / "shots.json"
PHOTOS = REPO_ROOT / "scratch" / "avatar-photos"
SHOT_LAYERS = {"slight": "mouth-1", "open": "mouth-2", "wide": "mouth-3", "m": "mouth-M",
               "f": "mouth-F", "oo": "mouth-U", "ee": "mouth-E", "blink": "eyes-closed"}
SHOTS = ["rest"] + list(SHOT_LAYERS)
BG = (46, 72, 89)  # the cartoon bubble's dark blue
SIZE = 512
HALF = 2           # work at half resolution - plenty for a 512px layer


def load_spec(path):
    spec = json.loads(Path(path).read_text(encoding="utf-8"))
    missing = [s for s in SHOTS if s not in spec.get("shots", {})]
    if missing:
        raise ValueError(f"{path}: shots missing {missing} - need one file for each of {SHOTS}")
    for k in ("mouth", "eyes_y", "face_w"):
        if k not in spec:
            raise ValueError(f"{path}: needs '{k}' (full-resolution pixels on the resting photo)")
    return spec


def load_photo(path):
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    return np.array(im.resize((im.width // HALF, im.height // HALF), Image.LANCZOS))


def ellipse_mask(shape, centre, axes, blur):
    m = np.zeros(shape, np.float32)
    cv2.ellipse(m, (int(centre[0]), int(centre[1])), (int(axes[0]), int(axes[1])), 0, 0, 360, 1.0, -1)
    return cv2.GaussianBlur(m, (0, 0), blur) if blur else m


class Geometry:
    """Where the face sits in the base photo (half-res pixels) and the masks
    and crop derived from it."""

    def __init__(self, spec, shape):
        self.shape = shape
        self.mx, self.my = spec["mouth"][0] // HALF, spec["mouth"][1] // HALF
        self.eyes_y = spec["eyes_y"] // HALF
        self.f = spec["face_w"] // HALF
        f, mx, my = self.f, self.mx, self.my
        self.crop = (mx - int(f * 1.2), my - int(f * 1.5), mx + int(f * 1.2), my + int(f * 0.9))
        self.mouth = ellipse_mask(shape, (mx, my + f * 0.07), (f * 0.34, f * 0.30), f * 0.05)
        ring = ellipse_mask(shape, (mx, my + f * 0.07), (f * 0.46, f * 0.40), 0) > 0.5
        ring &= self.mouth < 0.05
        ring[my:, :] = False  # cheeks only: below the mouth line the ring reaches the shirt
        self.mouth_ring = ring
        self.eyes = ellipse_mask(shape, (mx, self.eyes_y), (f * 0.50, f * 0.15), f * 0.05)
        self.eyes_ring = (cv2.dilate(self.eyes, np.ones((25, 25))) > 0.05) & (self.eyes < 0.05)
        upper = np.zeros(shape, np.uint8)
        cv2.rectangle(upper, (mx - f, self.eyes_y - f), (mx + f, my - f // 5), 255, -1)
        self.upper_face = upper


def aligner(base, geo):
    sift = cv2.SIFT_create(4000)
    gray = cv2.cvtColor(base, cv2.COLOR_RGB2GRAY)
    kb, db = sift.detectAndCompute(gray, geo.upper_face)
    bf = cv2.BFMatcher()
    h, w = geo.shape

    def align(img, name):
        k, d = sift.detectAndCompute(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), geo.upper_face)
        good = [a for a, b in bf.knnMatch(db, d, k=2) if a.distance < 0.7 * b.distance]
        if len(good) < 12:
            raise RuntimeError(f"{name}: only {len(good)} face matches with the resting photo - "
                               "was it taken in the same sitting, camera untouched?")
        src = np.float32([k[x.trainIdx].pt for x in good])
        dst = np.float32([kb[x.queryIdx].pt for x in good])
        M, inliers = cv2.estimateAffinePartial2D(src, dst, method=cv2.RANSAC, ransacReprojThreshold=4)
        print(f"  {name}: {int(inliers.sum())} matched points, scale {np.hypot(M[0, 0], M[1, 0]):.3f}")
        return cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    return align


def colour_match(img, base, region):
    out = img.astype(np.float32)
    for c in range(3):
        out[..., c] += base[..., c][region].mean() - out[..., c][region].mean()
    return np.clip(out, 0, 255)


def person_mask(base):
    """Soft 0-1 mask of the person (DeepLabV3 'person', refined by GrabCut)."""
    import torch
    from torchvision.models.segmentation import DeepLabV3_ResNet101_Weights, deeplabv3_resnet101
    h, w = base.shape[:2]
    weights = DeepLabV3_ResNet101_Weights.DEFAULT
    model = deeplabv3_resnet101(weights=weights).eval()
    x = weights.transforms()(torch.from_numpy(base).permute(2, 0, 1)).unsqueeze(0)
    with torch.no_grad():
        prob = torch.softmax(model(x)["out"][0], 0)[15].numpy()  # VOC class 15 = person
    prob = cv2.resize(prob, (w, h), interpolation=cv2.INTER_LINEAR)
    gc = np.full((h, w), cv2.GC_PR_BGD, np.uint8)
    gc[prob > 0.3] = cv2.GC_PR_FGD
    gc[prob > 0.9] = cv2.GC_FGD
    gc[prob < 0.02] = cv2.GC_BGD
    cv2.grabCut(cv2.cvtColor(base, cv2.COLOR_RGB2BGR), gc, None, np.zeros((1, 65)), np.zeros((1, 65)),
                4, cv2.GC_INIT_WITH_MASK)
    hard = np.isin(gc, (cv2.GC_FGD, cv2.GC_PR_FGD)).astype(np.uint8)
    _, lab, stats, _ = cv2.connectedComponentsWithStats(hard)
    hard = (lab == 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    hard = cv2.morphologyEx(hard, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    return cv2.GaussianBlur(hard.astype(np.float32), (0, 0), 2.0)


def to_layer(rgb, alpha, crop):
    circle = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(circle).ellipse((1, 1, SIZE - 2, SIZE - 2), fill=255)
    im = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).crop(crop).resize((SIZE, SIZE), Image.LANCZOS)
    a = Image.fromarray((np.clip(alpha, 0, 1) * 255).astype(np.uint8)).crop(crop).resize((SIZE, SIZE), Image.LANCZOS)
    im.putalpha(Image.fromarray(np.minimum(np.array(a), np.array(circle))))
    return im


def build(spec, photos, out_dir):
    base = load_photo(Path(photos) / spec["shots"]["rest"])
    geo = Geometry(spec, base.shape[:2])
    align = aligner(base, geo)
    out_dir.mkdir(parents=True, exist_ok=True)
    print("Person mask (background -> dark blue) ...")
    pm = person_mask(base)[..., None]
    body_rgb = base.astype(np.float32) * pm + np.array(BG, np.float32) * (1 - pm)
    body = to_layer(body_rgb, np.ones(geo.shape), geo.crop)
    ImageDraw.Draw(body).ellipse((3, 3, SIZE - 4, SIZE - 4), outline=(240, 240, 240, 255), width=10)
    body.save(out_dir / "body.png")
    empty = to_layer(base, np.zeros(geo.shape), geo.crop)
    empty.save(out_dir / "eyes-open.png")
    empty.save(out_dir / "mouth-0.png")  # resting mouth = the base itself
    print("Aligning shots to the resting photo ...")
    for shot, layer in SHOT_LAYERS.items():
        img = align(load_photo(Path(photos) / spec["shots"][shot]), shot)
        mask, ring = (geo.eyes, geo.eyes_ring) if shot == "blink" else (geo.mouth, geo.mouth_ring)
        to_layer(colour_match(img, base, ring), mask, geo.crop).save(out_dir / f"{layer}.png")
    print(f"Wrote {len(SHOTS) + 2} layers to {out_dir}")


def contact_sheet(png_dir, out_path):
    tiles = ["mouth-0", "mouth-1", "mouth-2", "mouth-3", "mouth-M", "mouth-F", "mouth-U", "mouth-E", "eyes-closed"]
    sheet = Image.new("RGBA", (5 * 256, 2 * 256), (30, 30, 30, 255))
    body = Image.open(png_dir / "body.png").convert("RGBA")
    for i, name in enumerate(tiles):
        im = body.copy()
        im.alpha_composite(Image.open(png_dir / f"{name}.png").convert("RGBA"))
        sheet.alpha_composite(im.resize((256, 256)), ((i % 5) * 256, (i // 5) * 256))
    sheet.save(out_path)
    print(f"Contact sheet: {out_path}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spec", default=str(SPEC))
    ap.add_argument("--photos", default=str(PHOTOS))
    ap.add_argument("--out", default=str(PHOTO_PNG_DIR))
    ap.add_argument("--sheet", default=str(PHOTOS / "_layers.png"), help="contact sheet to look at (scratch)")
    args = ap.parse_args()
    build(load_spec(args.spec), args.photos, Path(args.out))
    contact_sheet(Path(args.out), Path(args.sheet))


if __name__ == "__main__":
    main()
