"""Build the avatar's mouth/blink track from a narration mp3 (pipeline step 1.5).

    python scripts/build_avatar_track.py audio/<slug>.mp3 [--fps 25]

Writes audio/<slug>.avatar.json: one mouth level (0 closed .. 3 wide) per
video frame, from the narration's loudness, plus deterministic blink start
frames seeded by the slug. Run it after the narration is final (1.2-1.4);
if the mp3 is ever regenerated, run it again - render_avatar_track.py
refuses a mouth file whose duration no longer matches the config.

Loudness-driven on purpose: it doesn't care which TTS voice made the
audio, so a later voice change needs no change here. See
docs/superpowers/specs/2026-10-02-avatar-presenter-design.md.
"""

import argparse
import hashlib
import json
import random
import subprocess
import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avatar_lib import BLINK_FRAMES, MOUTH_FILE_VERSION, mouth_path_for_audio  # noqa: E402

SAMPLE_RATE = 16000
# Frames quieter than this raw RMS are treated as silence when picking the
# normalisation reference, so pauses don't drag the reference down.
SILENCE_FLOOR = 0.01
# Normalised-loudness cut points between mouth levels 0|1|2|3. Set from the
# Barings narration's loudness spread (speech sits fairly evenly in 0.1-0.9),
# so 3 = only the loudest ~10% of frames; final tuning is by eye
# on the lip-sync preview (plan Task 6).
LEVEL_THRESHOLDS = (0.08, 0.45, 0.85)
MIN_HOLD = 2
BLINK_GAP_S = (3.0, 6.0)


def decode_mono(mp3_path):
    out = subprocess.run(["ffmpeg", "-v", "error", "-i", str(mp3_path), "-ac", "1",
                          "-ar", str(SAMPLE_RATE), "-f", "f32le", "-"],
                         check=True, capture_output=True).stdout
    return np.frombuffer(out, dtype="<f4")


def probe_duration(mp3_path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(mp3_path)],
                         check=True, capture_output=True, text=True).stdout
    return float(out.strip())


def frame_rms(samples, sr, fps, n_frames):
    """RMS over a one-frame window centred on each frame's timestamp."""
    half = sr // fps // 2
    rms = np.zeros(n_frames)
    for i in range(n_frames):
        c = int(round(i * sr / fps))
        seg = samples[max(0, c - half):c + half]
        if seg.size:
            rms[i] = float(np.sqrt(np.mean(seg.astype(np.float64) ** 2)))
    return rms


def normalise(rms):
    voiced = rms[rms > SILENCE_FLOOR]
    if voiced.size == 0:
        return np.zeros_like(rms)
    ref = np.percentile(voiced, 95)
    return np.clip(rms / ref, 0.0, 1.0)


def quantise(norm):
    return [int(v) for v in np.digitize(norm, LEVEL_THRESHOLDS)]


def debounce(levels, min_hold=MIN_HOLD):
    """A new level must repeat min_hold frames before it shows, so the
    mouth doesn't buzz; a drop to 0 (a pause) shows immediately."""
    out, cur, pending, count = [], 0, None, 0
    for lv in levels:
        if lv == 0:
            cur, pending, count = 0, None, 0
        elif lv == cur:
            pending, count = None, 0
        elif lv == pending:
            count += 1
            if count >= min_hold:
                cur, pending, count = lv, None, 0
        else:
            pending, count = lv, 1
            if min_hold <= 1:
                cur, pending, count = lv, None, 0
        out.append(cur)
    return out


def blink_schedule(slug, n_frames, fps):
    """Blink start frames, one every 3-6 s. Seeded by the slug so reruns
    (and a future JS renderer reading the same file) blink identically."""
    rng = random.Random(int(hashlib.sha256(slug.encode("utf-8")).hexdigest()[:16], 16))
    blinks, t = [], rng.uniform(*BLINK_GAP_S)
    while True:
        f = int(round(t * fps))
        if f + BLINK_FRAMES > n_frames:
            return blinks
        blinks.append(f)
        t += rng.uniform(*BLINK_GAP_S)


def build_track(samples, sr, fps, duration_s, slug, source):
    n_frames = int(duration_s * fps)  # same count watch_video_lib.render() uses
    levels = debounce(quantise(normalise(frame_rms(samples, sr, fps, n_frames))))
    return {
        "version": MOUTH_FILE_VERSION,
        "fps": fps,
        "frames": n_frames,
        "duration_s": round(duration_s, 3),
        "source": source,
        "mouth": "".join(str(v) for v in levels),
        "blinks": blink_schedule(slug, n_frames, fps),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mp3", help="audio/<slug>.mp3")
    ap.add_argument("--fps", type=int, default=25, help="must match the video config's FPS (default 25)")
    ap.add_argument("--out", help="default: audio/<slug>.avatar.json next to the mp3")
    args = ap.parse_args()

    mp3 = Path(args.mp3)
    out = Path(args.out) if args.out else mouth_path_for_audio(mp3)
    track = build_track(decode_mono(mp3), SAMPLE_RATE, args.fps, probe_duration(mp3),
                        mp3.stem, mp3.as_posix())
    out.write_text(json.dumps(track, separators=(",", ":")), encoding="utf-8")

    hist = Counter(track["mouth"])
    total = track["frames"] or 1
    spread = "  ".join(f"{k}:{100 * hist.get(k, 0) / total:.0f}%" for k in "0123")
    print(f"Wrote {out} - {track['frames']} frames ({track['duration_s']}s @ {args.fps}fps), "
          f"{len(track['blinks'])} blinks, mouth levels {spread}")


if __name__ == "__main__":
    main()
