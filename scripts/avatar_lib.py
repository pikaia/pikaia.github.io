"""Shared helpers for the avatar presenter overlay.

See docs/superpowers/specs/2026-10-02-avatar-presenter-design.md. Used by
build_avatar.py (SVG -> PNG layers), build_avatar_track.py (mp3 -> mouth
file), render_avatar_track.py (step 6a) and overlay_avatar.py (step 6b).
A video config opts in with an AVATAR dict; with none, nothing here runs.
"""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AVATAR_DIR = REPO_ROOT / "assets" / "avatar"
SVG_PATH = AVATAR_DIR / "avatar.svg"
PNG_DIR = AVATAR_DIR / "png"

# One PNG per name, all the same square canvas, stacked
# body -> eyes-open|eyes-closed -> mouth-N.
LAYER_NAMES = ["body", "eyes-open", "eyes-closed", "mouth-0", "mouth-1", "mouth-2", "mouth-3"]
BLINK_FRAMES = 3
MOUTH_FILE_VERSION = 1
# 1 = loudness only; 2 adds a per-frame "shape" string (M F U E or .) from
# avatar_visemes.py. The renderer reads both.
MOUTH_FILE_VERSIONS = (1, 2)

CORNERS = {"bottom-right", "bottom-left", "top-right", "top-left"}
DEFAULTS = {"corner": "bottom-right", "size": 0.20, "margin": 0.03, "fade": 0.3}


def resolve_ranges(ranges, total):
    """[(start, end)] in seconds -> sorted absolute ranges. A negative start
    or end counts back from the end of the video; end None = the end.
    Out-of-bounds, empty or overlapping ranges are errors, not clamps."""
    out = []
    for raw in ranges:
        start, end = raw
        s = total + start if start < 0 else float(start)
        if end is None:
            e = float(total)
        else:
            e = total + end if end < 0 else float(end)
        if not (0 <= s < e <= total):
            raise ValueError(f"AVATAR range {raw!r} resolves to ({s}, {e}) - "
                             f"empty or outside the video's 0..{total}s")
        out.append((s, e))
    out.sort()
    for (s1, e1), (s2, e2) in zip(out, out[1:]):
        if s2 < e1:
            raise ValueError(f"AVATAR ranges overlap: ({s1}, {e1}) and ({s2}, {e2})")
    return out


def avatar_settings(cfg):
    """The config's AVATAR dict merged over DEFAULTS, ranges resolved
    against TOTAL_DURATION. None when the config has no AVATAR."""
    raw = getattr(cfg, "AVATAR", None)
    if raw is None:
        return None
    if not raw.get("ranges"):
        raise ValueError("AVATAR needs a non-empty 'ranges' list")
    s = {**DEFAULTS, **raw}
    if s["corner"] not in CORNERS:
        raise ValueError(f"AVATAR corner {s['corner']!r} - use one of {sorted(CORNERS)}")
    if not 0 < s["size"] <= 0.5:
        raise ValueError(f"AVATAR size {s['size']} - must be in (0, 0.5] of frame height")
    if s["margin"] < 0:
        raise ValueError(f"AVATAR margin {s['margin']} - must be >= 0")
    if s["fade"] < 0:
        raise ValueError(f"AVATAR fade {s['fade']} - must be >= 0")
    s["ranges"] = resolve_ranges(raw["ranges"], cfg.TOTAL_DURATION)
    return s


def bubble_geometry(settings, out_w, out_h):
    """(diameter, x, y) of the bubble's top-left corner in pixels. The
    diameter is rounded down to even so yuv420p chroma lines up."""
    d = int(round(settings["size"] * out_h)) // 2 * 2
    m = int(round(settings["margin"] * out_h))
    x = out_w - d - m if settings["corner"].endswith("right") else m
    y = out_h - d - m if settings["corner"].startswith("bottom") else m
    return d, x, y


def alpha_at(t, ranges, fade):
    """Bubble opacity at time t: 1 inside a range, ramping over `fade`
    seconds at each range edge, 0 outside every range."""
    for s, e in ranges:
        if s <= t < e:
            if fade <= 0:
                return 1.0
            return max(0.0, min(1.0, (t - s) / fade, (e - t) / fade))
    return 0.0


def mouth_path_for_audio(mp3_path):
    return Path(mp3_path).with_suffix(".avatar.json")


def mouth_path_for_config(cfg):
    # Same base name as the config's TIMING_JSON (audio/<slug>.timing.json),
    # the convention watch_video_lib.render() uses to find the mp3.
    return REPO_ROOT / Path(cfg.TIMING_JSON).with_suffix("").with_suffix(".avatar.json")


def video_dims(cfg):
    return getattr(cfg, "WIDTH", 1280), getattr(cfg, "HEIGHT", 720), getattr(cfg, "FPS", 25)


def load_mouth_file(path, fps, total_duration):
    """Load and validate audio/<slug>.avatar.json against the config it is
    about to drive. Every mismatch names the step that fixes it."""
    path = Path(path)
    rerun = f"re-run step 1.5 (python scripts/build_avatar_track.py audio/{path.name.replace('.avatar.json', '.mp3')})"
    if not path.exists():
        raise FileNotFoundError(f"no mouth file at {path} - {rerun}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("version") not in MOUTH_FILE_VERSIONS:
        raise ValueError(f"{path}: version {data.get('version')} not one of {MOUTH_FILE_VERSIONS} - {rerun}")
    if data["fps"] != fps:
        raise ValueError(f"{path}: fps {data['fps']} != config fps {fps} - {rerun} with --fps {fps}")
    if len(data["mouth"]) != data["frames"]:
        raise ValueError(f"{path}: mouth has {len(data['mouth'])} entries but frames={data['frames']} - {rerun}")
    if "shape" in data and len(data["shape"]) != data["frames"]:
        raise ValueError(f"{path}: shape has {len(data['shape'])} entries but frames={data['frames']} - {rerun}")
    if abs(data["duration_s"] - total_duration) > 1.0 / fps:
        raise ValueError(f"{path}: built for {data['duration_s']}s audio but TOTAL_DURATION is "
                         f"{total_duration}s - narration changed since; {rerun}")
    return data
