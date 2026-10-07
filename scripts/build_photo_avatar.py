"""Build the photo avatar's PNG layers from nine photos of Chris.

    python scripts/build_photo_avatar.py [--spec assets/avatar/photo/shots.json]
                                         [--photos scratch/avatar-photos]

The photo counterpart of build_avatar.py: writes the same layer names
(body, eyes-open, eyes-closed, mouth-0..3, mouth-M/F/U/E, 512px RGBA) into
assets/avatar/photo/png/, which render_avatar_track.py uses when a config
sets AVATAR "style": "photo". The source photos stay in scratch/ and are
never committed; shots.json (committed) names which file is which shot, so
the layers can be rebuilt. Where the face sits in the resting photo (mouth,
eyes_y, face_w) is measured from its landmarks unless shots.json gives it.

How: the resting photo is the base. Each other shot is aligned to it on face
landmarks that hold still while the mouth moves (MediaPipe Face Landmarker:
eye corners and nose, then a similarity transform), colour-nudged to the base using the cheeks only, and its mouth
(or, for the blink, eye) area cut out with a feathered ellipse. The base's
background is replaced with the cartoon bubble's dark blue using a person
mask (MediaPipe's selfie multiclass segmenter, model downloaded once; it
replaced DeepLabV3 + GrabCut on 2026-10-07). Lessons from the first build (2026-10-06): all nine
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
    given = [k for k in ("mouth", "eyes_y", "face_w") if k in spec]
    if given and len(given) < 3:
        raise ValueError(f"{path}: give all of mouth/eyes_y/face_w or none (none = measured from landmarks)")
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
        # kept below the nostrils and inside the jaw
        self.mouth = ellipse_mask(shape, (mx, my + f * 0.06), (f * 0.32, f * 0.25), f * 0.045)
        ring = ellipse_mask(shape, (mx, my + f * 0.07), (f * 0.46, f * 0.40), 0) > 0.5
        ring &= self.mouth < 0.05
        ring[my:, :] = False  # cheeks only: below the mouth line the ring reaches the shirt
        self.mouth_ring = ring
        self.eyes = ellipse_mask(shape, (mx, self.eyes_y), (f * 0.50, f * 0.15), f * 0.05)
        self.eyes_ring = (cv2.dilate(self.eyes, np.ones((25, 25))) > 0.05) & (self.eyes < 0.05)


MODEL = Path.home() / ".cache" / "mediapipe" / "face_landmarker.task"
MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/face_landmarker/"
             "face_landmarker/float16/1/face_landmarker.task")
# Face-mesh points that hold still while the mouth and eyelids move: eye
# corners, the bridge and ridge of the nose, the nostril wings.
STABLE = [33, 133, 362, 263, 168, 6, 197, 195, 5, 4, 1, 98, 327]
LIPS_INNER = (13, 14)
EYES = (33, 133, 362, 263)
CHEEKS = (234, 454)
LIP_CORNERS = (61, 291)
LEVEL_MAX = 6.0  # degrees; a bigger lip-line difference means a wrong shot, not a slant


UPPER_LIP = 0      # face-mesh point at the top of the upper lip
CENTRE_MAX = 0.10  # cap on the centring nudge, as a fraction of face width


def lip_centre_x(pts):
    return float((pts[LIP_CORNERS[0], 0] + pts[LIP_CORNERS[1], 0]) / 2)


def lip_angle(pts):
    a, b = pts[LIP_CORNERS[0]], pts[LIP_CORNERS[1]]
    return float(np.degrees(np.arctan2(b[1] - a[1], b[0] - a[0])))


def landmarks(path, _cache={}):
    """(478, 2) face-mesh points in full-resolution pixels (MediaPipe Face
    Landmarker, runs locally; model fetched once into ~/.cache/mediapipe)."""
    if path in _cache:
        return _cache[path]
    import mediapipe as mp
    from mediapipe.tasks.python import vision
    from mediapipe.tasks.python.core.base_options import BaseOptions
    if not MODEL.exists():
        import urllib.request
        MODEL.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(MODEL_URL, MODEL)
    if "lm" not in _cache:
        _cache["lm"] = vision.FaceLandmarker.create_from_options(
            vision.FaceLandmarkerOptions(base_options=BaseOptions(model_asset_path=str(MODEL)), num_faces=1))
    rgb = np.array(ImageOps.exif_transpose(Image.open(path)).convert("RGB"))
    res = _cache["lm"].detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb))
    if not res.face_landmarks:
        raise RuntimeError(f"{Path(path).name}: no face found")
    h, w = rgb.shape[:2]
    pts = np.array([(p.x * w, p.y * h) for p in res.face_landmarks[0]], np.float32)
    _cache[path] = pts
    return pts


def face_spec(path):
    """mouth / eyes_y / face_w for the resting photo, from its landmarks."""
    pts = landmarks(path)
    mouth = pts[list(LIPS_INNER)].mean(0)
    return {"mouth": [int(mouth[0]), int(mouth[1])], "eyes_y": int(pts[list(EYES), 1].mean()),
            "face_w": int(np.linalg.norm(pts[CHEEKS[0]] - pts[CHEEKS[1]]))}


def aligner(base_path, geo):
    """Line each shot up with the resting photo on face landmarks that do not
    move with the mouth (eye corners, nose), by a similarity transform (shift,
    turn, scale - no shear). Handles leaning in and small nods, where the
    earlier SIFT matching lost track (2026-10-06 shirt sets)."""
    h, w = geo.shape
    base_pts = landmarks(base_path) / HALF
    dst = base_pts[STABLE]
    base_lips = lip_angle(base_pts)

    def align(path, name):
        pts = landmarks(path) / HALF
        src = pts[STABLE]
        M, _ = cv2.estimateAffinePartial2D(src, dst, method=cv2.LMEDS)
        resid = np.abs(cv2.transform(src[None], M)[0] - dst).max()
        if resid > geo.f * 0.06:
            raise RuntimeError(f"{name}: face points disagree with the resting photo by {resid:.0f}px - "
                               "check it is the right shot")
        # Level the lip line to the resting photo's. A relaxed closed mouth
        # sits a degree or two off level, an open one doesn't, and switching
        # between them read as the mouth moving on a slant (2026-10-06).
        turn = 0.0
        if name != "blink":
            turn = float(np.clip(base_lips - lip_angle(cv2.transform(pts[None], M)[0]), -LEVEL_MAX, LEVEL_MAX))
            R = cv2.getRotationMatrix2D((float(geo.mx), float(geo.my)), -turn, 1.0)
            M = (np.vstack([R, [0, 0, 1]]) @ np.vstack([M, [0, 0, 1]]))[:2]
        # Centre the mouth on the resting mouth: across by the lip corners'
        # midpoint, down by the top of the upper lip (the jaw drops when the
        # mouth opens, the upper lip does not). A head turned a little
        # between shots puts the mouth off to one side after a 2D alignment.
        shift = np.zeros(2)
        if name != "blink":
            q = cv2.transform(pts[None], M)[0]
            shift = np.array([lip_centre_x(base_pts) - lip_centre_x(q), base_pts[UPPER_LIP, 1] - q[UPPER_LIP, 1]])
            shift = np.clip(shift, -geo.f * CENTRE_MAX, geo.f * CENTRE_MAX)
            M = M.copy()
            M[:, 2] += shift
        print(f"  {name}: aligned on {len(STABLE)} landmarks, scale {np.hypot(M[0, 0], M[1, 0]):.3f}, "
              f"worst point off by {resid:.1f}px, lips levelled {turn:+.1f} deg, "
              f"mouth centred by {shift[0]:+.0f},{shift[1]:+.0f}px")
        return cv2.warpAffine(load_photo(path), M, (w, h), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    return align


def colour_match(img, base, region):
    out = img.astype(np.float32)
    for c in range(3):
        out[..., c] += base[..., c][region].mean() - out[..., c][region].mean()
    return np.clip(out, 0, 255)


SEG_MODEL = Path.home() / ".cache" / "mediapipe" / "selfie_multiclass_256x256.tflite"
SEG_MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/image_segmenter/"
                 "selfie_multiclass_256x256/float32/latest/selfie_multiclass_256x256.tflite")


def soft_edge_mask(p):
    """Person mask from a 0-1 person-confidence map: the largest region above
    0.5, holes closed, solid inside, with the model's own soft values kept only
    in a thin band round the outline (hair, ears). The raw confidence alone
    never reaches 0 on the background, so used directly it ghosts the room."""
    hard = (p > 0.5).astype(np.uint8)
    _, lab, stats, _ = cv2.connectedComponentsWithStats(hard)
    hard = (lab == 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    hard = cv2.morphologyEx(hard, cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    soft = np.clip((p - 0.3) / 0.4, 0, 1)
    k = np.ones((9, 9), np.uint8)
    band = cv2.dilate(hard, k) - cv2.erode(hard, k)
    return cv2.GaussianBlur(np.where(band > 0, soft, hard.astype(np.float32)), (0, 0), 1.5)


def person_mask(base):
    """Soft 0-1 mask of the person (MediaPipe selfie multiclass segmenter,
    runs locally; model fetched once into ~/.cache/mediapipe). Replaced
    DeepLabV3 + GrabCut on 2026-10-07, which let a strip of door frame beside
    the jaw through as 'person'."""
    import mediapipe as mp
    from mediapipe.tasks.python import vision
    from mediapipe.tasks.python.core.base_options import BaseOptions
    if not SEG_MODEL.exists():
        import urllib.request
        SEG_MODEL.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(SEG_MODEL_URL, SEG_MODEL)
    seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(
        base_options=BaseOptions(model_asset_path=str(SEG_MODEL)), output_confidence_masks=True))
    res = seg.segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(base.astype(np.uint8))))
    background = np.squeeze(res.confidence_masks[0].numpy_view()).astype(np.float32)  # class 0
    return soft_edge_mask(1 - background)


def to_layer(rgb, alpha, crop):
    circle = Image.new("L", (SIZE, SIZE), 0)
    ImageDraw.Draw(circle).ellipse((1, 1, SIZE - 2, SIZE - 2), fill=255)
    im = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8)).crop(crop).resize((SIZE, SIZE), Image.LANCZOS)
    a = Image.fromarray((np.clip(alpha, 0, 1) * 255).astype(np.uint8)).crop(crop).resize((SIZE, SIZE), Image.LANCZOS)
    im.putalpha(Image.fromarray(np.minimum(np.array(a), np.array(circle))))
    return im


def build(spec, photos, out_dir):
    rest = Path(photos) / spec["shots"]["rest"]
    if not all(k in spec for k in ("mouth", "eyes_y", "face_w")):
        spec = {**spec, **face_spec(rest)}
        print(f"Face position from landmarks: mouth {spec['mouth']}, eyes_y {spec['eyes_y']}, face_w {spec['face_w']}")
    base = load_photo(rest)
    geo = Geometry(spec, base.shape[:2])
    align = aligner(Path(photos) / spec["shots"]["rest"], geo)
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
        img = align(Path(photos) / spec["shots"][shot], shot)
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
