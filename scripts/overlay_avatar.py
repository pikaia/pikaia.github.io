"""Lay the avatar bubble over the finished main video (pipeline step 6b).

    python scripts/overlay_avatar.py --config scripts/video-configs/<slug>.py \\
        --in preview-motion/<slug>.mp4 --out preview-motion/<slug>-avatar.mp4

One ffmpeg pass: overlay preview-motion/<slug>-avatar.mov (step 6a) at the
AVATAR corner, copy the audio untouched, re-encode video with the same
settings watch_video_lib.render() uses. The track already carries its own
transparency and fades, so this is a plain overlay. Always the last video
step (after any route-walk splices), and it never overwrites its input -
the plain <slug>.mp4 survives for A/B comparison. A config without AVATAR
is skipped (exit 0).
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avatar_lib import avatar_settings, bubble_geometry, video_dims  # noqa: E402
from render_avatar_track import default_track_path  # noqa: E402
from watch_video_lib import load_config  # noqa: E402


def build_overlay_cmd(in_path, track_path, out_path, x, y):
    return ["ffmpeg", "-y", "-v", "error", "-i", str(in_path), "-i", str(track_path),
            "-filter_complex", f"[0:v][1:v]overlay=x={x}:y={y}:format=auto,format=yuv420p[v]",
            "-map", "[v]", "-map", "0:a?",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "copy",
            str(out_path)]


def frame_count(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
                          "-show_entries", "stream=nb_read_frames", "-of", "json", str(path)],
                         check=True, capture_output=True, text=True).stdout
    return int(json.loads(out)["streams"][0]["nb_read_frames"])


def track_width(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                          "-show_entries", "stream=width", "-of", "csv=p=0", str(path)],
                         check=True, capture_output=True, text=True).stdout
    return int(out.strip())


def verify_same_frames(in_path, out_path):
    """Full-decode frame count of the overlaid video must equal the plain
    one's - the two-input re-encode is where dropped/duplicated frames
    would come from (see docs/production-pipeline.md section 8)."""
    a, b = frame_count(in_path), frame_count(out_path)
    if a != b:
        raise RuntimeError(f"frame count mismatch: {in_path} has {a}, {out_path} has {b}")
    return a


def overlay(cfg, in_path, track_path, out_path):
    settings = avatar_settings(cfg)
    if settings is None:
        print("No AVATAR in this config - step 6b skipped.")
        return False
    in_path, track_path, out_path = Path(in_path), Path(track_path), Path(out_path)
    if in_path.resolve() == out_path.resolve():
        raise ValueError(f"--out must differ from --in; refusing to overwrite {in_path}")
    if not track_path.exists():
        raise FileNotFoundError(f"no avatar track at {track_path} - run step 6a "
                                f"(python scripts/render_avatar_track.py --config ...) first")
    out_w, out_h, _ = video_dims(cfg)
    d, x, y = bubble_geometry(settings, out_w, out_h)
    if track_width(track_path) != d:
        raise ValueError(f"{track_path} is {track_width(track_path)}px wide but AVATAR now gives a "
                         f"{d}px bubble - the config changed since; re-run step 6a")
    subprocess.run(build_overlay_cmd(in_path, track_path, out_path, x, y), check=True)
    n = verify_same_frames(in_path, out_path)
    print(f"Wrote {out_path} - {n} frames, same as {in_path}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--in", dest="in_path", required=True, help="preview-motion/<slug>.mp4 (step 6 output)")
    ap.add_argument("--out", required=True, help="preview-motion/<slug>-avatar.mp4")
    ap.add_argument("--track", help="default: preview-motion/<config-stem>-avatar.mov")
    args = ap.parse_args()
    cfg = load_config(args.config)
    overlay(cfg, args.in_path, Path(args.track) if args.track else default_track_path(args.config), args.out)


if __name__ == "__main__":
    main()
