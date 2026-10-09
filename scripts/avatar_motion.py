"""Per-frame motion curves for the cartoon avatar (AVATAR "motion": True).

The cartoon used to be a still face with only the mouth and blinks
changing. These curves move it like a presenter: a slow idle sway and tilt
of the head, small nods on emphasis (from the step-1.5 loudness track),
breathing in the shoulders, an occasional sideways glance and a lift of the
eyebrows at some sentence starts (from timing.json). Everything is a pure
function of the mouth levels, the sentence start frames and a seed, so a
render is reproducible. Units are pixels on the 512 x 512 SVG canvas
(degrees for tilt); render_avatar_track.py scales them to the bubble.
"""

import math
import random

import numpy as np

# Amplitudes, in 512-canvas pixels / degrees. Small on purpose: the bubble
# is ~144 px on screen, so 4 canvas px is ~1 screen px.
SWAY_X = (3.0, 1.5)        # two slow sines, side to side
SWAY_Y = 1.5
TILT_DEG = (1.6, 0.8)
NOD_Y = 7.0                # head dips this much at full emphasis
NOD_TILT_DEG = 1.2
BREATH_RISE = 6.0          # shoulder line (and the head with it) rises on the in-breath
GLANCE_PUPIL = 5.0         # pupils stay inside the glasses at +-5
GLANCE_HEAD = 2.0
GLANCE_P = 0.35            # share of sentence starts that get a glance
GLANCE_S = (0.5, 1.1)
BROW_LIFT = 6.0
BROW_P = 0.45
BROW_EMPHASIS = 0.35       # emphasis level that also lifts the brows
BROW_COOLDOWN_S = 2.0
EASE_FRAMES = 4


def _ema(x, a):
    out = np.empty_like(x)
    acc = x[0] if len(x) else 0.0
    for i, v in enumerate(x):
        acc += (v - acc) * a
        out[i] = acc
    return out


def _smoothstep(u):
    u = np.clip(u, 0.0, 1.0)
    return u * u * (3 - 2 * u)


def _pulse(n, start, attack, hold, release):
    """0..1 envelope over n frames: rises over `attack`, holds, falls."""
    env = np.zeros(n)
    i = np.arange(n, dtype=float)
    up = _smoothstep((i - start) / max(attack, 1))
    down = 1.0 - _smoothstep((i - (start + attack + hold)) / max(release, 1))
    env = np.minimum(up, down)
    env[i < start] = 0.0
    return env


def motion_curves(mouth, sentence_starts, fps, seed):
    """dict of per-frame float arrays: head_dx, head_dy, tilt, breath (0..1),
    pupil_dx, brow_dy. `mouth` is the step-1.5 loudness level per frame
    (0..3); `sentence_starts` are frame numbers."""
    n = len(mouth)
    rng = random.Random(seed)
    t = np.arange(n) / fps
    ph = [rng.uniform(0, 2 * math.pi) for _ in range(6)]

    e = np.asarray(mouth, dtype=float) / 3.0
    emphasis = np.clip(_ema(e, 0.25) - _ema(e, 0.03), -0.3, 0.6) if n else e

    breath = 0.5 + 0.5 * np.sin(2 * math.pi * 0.23 * t + ph[5])
    head_dx = SWAY_X[0] * np.sin(2 * math.pi * 0.061 * t + ph[0]) + SWAY_X[1] * np.sin(2 * math.pi * 0.137 * t + ph[1])
    head_dy = SWAY_Y * np.sin(2 * math.pi * 0.083 * t + ph[2]) + NOD_Y * np.clip(emphasis, 0, None) - BREATH_RISE * breath
    tilt = (TILT_DEG[0] * np.sin(2 * math.pi * 0.047 * t + ph[3]) + TILT_DEG[1] * np.sin(2 * math.pi * 0.11 * t + ph[4])
            + NOD_TILT_DEG * emphasis)

    pupil_dx = np.zeros(n)
    busy_until = -1
    for s in sorted(sentence_starts):
        if s < 0 or s >= n or s <= busy_until:
            continue
        if rng.random() < GLANCE_P:
            direction = rng.choice((-1, 1))
            hold = int(rng.uniform(*GLANCE_S) * fps)
            g = _pulse(n, s, EASE_FRAMES, hold, EASE_FRAMES)
            pupil_dx += direction * GLANCE_PUPIL * g
            head_dx += direction * GLANCE_HEAD * g
            busy_until = s + 2 * EASE_FRAMES + hold

    lifts = [s for s in sorted(sentence_starts) if 0 <= s < n and rng.random() < BROW_P]
    rising = np.flatnonzero((emphasis[1:] >= BROW_EMPHASIS) & (emphasis[:-1] < BROW_EMPHASIS)) + 1 if n > 1 else []
    brow = np.zeros(n)
    last = -10 ** 9
    for s in sorted(set(lifts) | set(int(r) for r in rising)):
        if s - last < BROW_COOLDOWN_S * fps:
            continue
        brow = np.maximum(brow, _pulse(n, s, 3, int(0.35 * fps), 8))
        last = s
    np.clip(pupil_dx, -GLANCE_PUPIL, GLANCE_PUPIL, out=pupil_dx)
    return {"head_dx": head_dx, "head_dy": head_dy, "tilt": tilt, "breath": breath,
            "pupil_dx": pupil_dx, "brow_dy": -BROW_LIFT * brow}


def sentence_start_frames(timing, fps):
    """Frame numbers of each sentence start in a timing.json payload."""
    sents = timing["sentences"] if isinstance(timing, dict) else timing
    return [int(round(s["offset_s"] * fps)) for s in sents]
