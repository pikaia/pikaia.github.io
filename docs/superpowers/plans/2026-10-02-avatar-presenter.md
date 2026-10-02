# Avatar Presenter Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an optional, locally-rendered, lip-synced cartoon avatar of Chris in a corner bubble over the main YouTube video, shown during configured time ranges (Phase 1: intro + outro).

**Architecture:** Four small scripts around one shared module. `build_avatar.py` rasterises a layered SVG into PNG layers once. `build_avatar_track.py` turns the narration mp3 into a per-frame mouth-level + blink file (`audio/<slug>.avatar.json`). `render_avatar_track.py` stacks the PNG layers per frame into a transparent `.mov` the full length of the video (alpha fades baked in). `overlay_avatar.py` lays that `.mov` over the untouched step-6 `.mp4` with one ffmpeg pass. `watch_video_lib.py` is not modified.

**Tech Stack:** Python 3.12, numpy, Pillow, ffmpeg/ffprobe (already installed), `resvg-py` 0.5.0 (new, pip, offline), pytest 8 (already installed) for unit/integration tests.

**Spec:** `docs/superpowers/specs/2026-10-02-avatar-presenter-design.md`

## Global Constraints

- Everything runs locally. No external services, no network calls, no hosted APIs.
- `scripts/watch_video_lib.py` is not modified. Step 6 output (`preview-motion/<slug>.mp4`) is never overwritten by the avatar steps.
- No `AVATAR` in a config → steps 6a/6b print a "skipped" note and exit 0; every existing config keeps working untouched.
- Frame rate comes from the config's `FPS` (default 25); frame size from `WIDTH, HEIGHT` (default 1280×720); frame count is `int(TOTAL_DURATION * fps)`, same as `watch_video_lib.render()`.
- Video re-encode settings match `watch_video_lib.render()`: `libx264`, `-preset medium`, `-crf 20`, `-pix_fmt yuv420p`.
- The reference photo of Chris lives only in `scratch/` (gitignored) and is never committed.
- `assets/avatar/png/*.png` are committed — a documented binary exception, like the OSM tiles.
- `ruff check .` must pass clean before every commit touching Python. Keep `# noqa: E402` on any `sys.path.insert(...)`-then-import line.
- **Tests:** this feature introduces `tests/` with pytest (already installed). This is a deliberate departure from the route-walk plan's "no test framework" note — the mouth/range/geometry logic is pure and worth pinning. Run with `python -m pytest tests -v`.
- Commit messages end with the two attribution lines:
  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_014vyi5DydGd12SnQWie299V
  ```
  (Shown once here; every `git commit` below must include them.)

## Review Focus

1. **Narration regenerated after the mouth file was built** (e.g. a late pronunciation fix + `--no-cache`) — expect 6a to refuse with a message naming step 1.5, never a silently out-of-sync mouth. Pinned in Task 1 (`test_load_mouth_file_rejects_stale_duration`).
2. **A range that runs past the video, is empty, or overlaps another** (e.g. `(-30, None)` on a 20 s video, or `(0, 30), (20, 40)`) — expect a clear `ValueError` naming the range, not a clamp. Pinned in Task 1.
3. **Long silence or a near-silent mp3** (e.g. a narration that starts with 2 s of silence, or an all-silent test file) — expect mouth level 0 throughout the silence and no divide-by-zero. Pinned in Task 2 (`test_build_track_silent_audio_all_closed`).
4. **Main video without an audio stream** (render warned "no sound") — expect the overlay still to succeed (`-map 0:a?`). Pinned in Task 5 (`test_overlay_without_audio`).
5. **Same output path as input for 6b** — expect a refusal, so the plain video can never be clobbered. Pinned in Task 5 (`test_overlay_refuses_in_equals_out`).

---

## File Structure

| Path | Responsibility |
|---|---|
| `scripts/avatar_lib.py` | Shared: paths, layer names, `AVATAR` config parsing, range resolution, bubble geometry, fade alpha, mouth-file path + load/validate |
| `scripts/build_avatar_track.py` | mp3 → `audio/<slug>.avatar.json` (decode, RMS, normalise, quantise, debounce, blinks) |
| `scripts/build_avatar.py` | `assets/avatar/avatar.svg` → `assets/avatar/png/*.png` via `resvg-py` |
| `scripts/render_avatar_track.py` | config + mouth file + PNG layers → `preview-motion/<slug>-avatar.mov` (qtrle ARGB) |
| `scripts/overlay_avatar.py` | `<slug>.mp4` + `<slug>-avatar.mov` → `<slug>-avatar.mp4` |
| `assets/avatar/avatar.svg` | layered character (placeholder face in Task 3, Chris's likeness in Task 7) |
| `assets/avatar/png/` | rasterised layers, 512×512 RGBA |
| `tests/conftest.py` | puts `scripts/` on `sys.path` |
| `tests/test_avatar_lib.py`, `tests/test_build_avatar_track.py`, `tests/test_build_avatar.py`, `tests/test_render_avatar_track.py`, `tests/test_overlay_avatar.py` | tests |
| `scripts/stage_youtube_text.py` (modify) | avatar disclosure line when the main config has `AVATAR` |
| `docs/production-pipeline.md`, `CLAUDE.md` (modify) | steps 1.5/6a/6b, step 8 note, file reference, binary exception |

---

### Task 1: Shared avatar module

**Files:**
- Create: `scripts/avatar_lib.py`
- Create: `tests/conftest.py`
- Test: `tests/test_avatar_lib.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `REPO_ROOT: Path`, `AVATAR_DIR: Path`, `PNG_DIR: Path`, `SVG_PATH: Path`
  - `LAYER_NAMES: list[str]` = `["body", "eyes-open", "eyes-closed", "mouth-0", "mouth-1", "mouth-2", "mouth-3"]`
  - `BLINK_FRAMES: int = 3`, `MOUTH_FILE_VERSION: int = 1`
  - `resolve_ranges(ranges: list[tuple[float, float | None]], total: float) -> list[tuple[float, float]]`
  - `avatar_settings(cfg) -> dict | None` — keys `ranges` (resolved), `corner`, `size`, `margin`, `fade`
  - `bubble_geometry(settings: dict, out_w: int, out_h: int) -> tuple[int, int, int]` — `(diameter, x, y)`
  - `alpha_at(t: float, ranges: list[tuple[float, float]], fade: float) -> float`
  - `mouth_path_for_audio(mp3_path: Path) -> Path`
  - `mouth_path_for_config(cfg) -> Path`
  - `load_mouth_file(path: Path, fps: int, total_duration: float) -> dict`
  - `video_dims(cfg) -> tuple[int, int, int]` — `(width, height, fps)`

- [ ] **Step 1: Create the test harness**

`tests/conftest.py`:
```python
import sys
from pathlib import Path

# The pipeline scripts aren't a package; tests import them by module name.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
```

- [ ] **Step 2: Write the failing tests**

`tests/test_avatar_lib.py`:
```python
import json
import types

import pytest

import avatar_lib as al


def cfg(**kw):
    base = {"TOTAL_DURATION": 100.0, "TIMING_JSON": "audio/x.timing.json"}
    base.update(kw)
    return types.SimpleNamespace(**base)


def test_resolve_ranges_bookends():
    assert al.resolve_ranges([(0, 30), (-30, None)], 100.0) == [(0, 30), (70.0, 100.0)]


def test_resolve_ranges_negative_end_and_sorting():
    assert al.resolve_ranges([(50, -10), (0, 5)], 100.0) == [(0, 5), (50, 90.0)]


@pytest.mark.parametrize("bad", [[(-30, None)], [(0, 130)], [(40, 40)], [(50, 10)]])
def test_resolve_ranges_rejects_out_of_bounds_or_empty(bad):
    with pytest.raises(ValueError, match="AVATAR range"):
        al.resolve_ranges(bad, 20.0 if bad == [(-30, None)] else 100.0)


def test_resolve_ranges_rejects_overlap():
    with pytest.raises(ValueError, match="overlap"):
        al.resolve_ranges([(0, 30), (20, 40)], 100.0)


def test_avatar_settings_none_when_absent():
    assert al.avatar_settings(cfg()) is None


def test_avatar_settings_defaults_and_resolution():
    s = al.avatar_settings(cfg(AVATAR={"ranges": [(0, 30), (-30, None)]}))
    assert s == {"ranges": [(0, 30), (70.0, 100.0)], "corner": "bottom-right",
                 "size": 0.20, "margin": 0.03, "fade": 0.3}


@pytest.mark.parametrize("bad", [
    {},
    {"ranges": []},
    {"ranges": [(0, 10)], "corner": "middle"},
    {"ranges": [(0, 10)], "size": 0},
    {"ranges": [(0, 10)], "size": 0.6},
    {"ranges": [(0, 10)], "margin": -0.1},
    {"ranges": [(0, 10)], "fade": -1},
])
def test_avatar_settings_rejects_bad_values(bad):
    with pytest.raises(ValueError):
        al.avatar_settings(cfg(AVATAR=bad))


def test_bubble_geometry_corners():
    s = {"size": 0.20, "margin": 0.03}
    assert al.bubble_geometry({**s, "corner": "bottom-right"}, 1280, 720) == (144, 1114, 554)
    assert al.bubble_geometry({**s, "corner": "top-left"}, 1280, 720) == (144, 22, 22)
    assert al.bubble_geometry({**s, "corner": "bottom-left"}, 1280, 720) == (144, 22, 554)
    assert al.bubble_geometry({**s, "corner": "top-right"}, 1280, 720) == (144, 1114, 22)


def test_bubble_geometry_diameter_is_even():
    d, _, _ = al.bubble_geometry({"size": 0.21, "margin": 0.0, "corner": "top-left"}, 1280, 720)
    assert d % 2 == 0


def test_alpha_at_fades_and_gaps():
    r = [(0.0, 10.0), (20.0, 30.0)]
    assert al.alpha_at(5.0, r, 0.5) == 1.0
    assert al.alpha_at(0.25, r, 0.5) == pytest.approx(0.5)
    assert al.alpha_at(9.75, r, 0.5) == pytest.approx(0.5)
    assert al.alpha_at(15.0, r, 0.5) == 0.0
    assert al.alpha_at(30.0, r, 0.5) == 0.0
    assert al.alpha_at(25.0, r, 0.0) == 1.0


def test_mouth_paths():
    from pathlib import Path
    assert al.mouth_path_for_audio(Path("audio/foo.mp3")) == Path("audio/foo.avatar.json")
    assert al.mouth_path_for_config(cfg(TIMING_JSON="audio/foo.timing.json")) == al.REPO_ROOT / "audio/foo.avatar.json"


def _write_track(path, **over):
    data = {"version": 1, "fps": 25, "frames": 250, "duration_s": 10.0,
            "source": "audio/x.mp3", "mouth": "0" * 250, "blinks": [80]}
    data.update(over)
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_load_mouth_file_ok(tmp_path):
    p = _write_track(tmp_path / "x.avatar.json")
    assert al.load_mouth_file(p, 25, 10.0)["frames"] == 250


def test_load_mouth_file_missing_names_step(tmp_path):
    with pytest.raises(FileNotFoundError, match="step 1.5"):
        al.load_mouth_file(tmp_path / "nope.avatar.json", 25, 10.0)


def test_load_mouth_file_rejects_stale_duration(tmp_path):
    p = _write_track(tmp_path / "x.avatar.json")
    with pytest.raises(ValueError, match="step 1.5"):
        al.load_mouth_file(p, 25, 12.0)


def test_load_mouth_file_rejects_fps_mismatch(tmp_path):
    p = _write_track(tmp_path / "x.avatar.json")
    with pytest.raises(ValueError, match="fps"):
        al.load_mouth_file(p, 30, 10.0)


def test_load_mouth_file_rejects_length_mismatch(tmp_path):
    p = _write_track(tmp_path / "x.avatar.json", mouth="0" * 249)
    with pytest.raises(ValueError, match="frames"):
        al.load_mouth_file(p, 25, 10.0)


def test_video_dims_defaults():
    assert al.video_dims(cfg()) == (1280, 720, 25)
    assert al.video_dims(cfg(WIDTH=1080, HEIGHT=1920, FPS=30)) == (1080, 1920, 30)
```

- [ ] **Step 3: Run the tests to verify they fail**

Run: `python -m pytest tests/test_avatar_lib.py -v`
Expected: collection error / FAIL with `ModuleNotFoundError: No module named 'avatar_lib'`.

- [ ] **Step 4: Write the implementation**

`scripts/avatar_lib.py`:
```python
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
    if data.get("version") != MOUTH_FILE_VERSION:
        raise ValueError(f"{path}: version {data.get('version')} != {MOUTH_FILE_VERSION} - {rerun}")
    if data["fps"] != fps:
        raise ValueError(f"{path}: fps {data['fps']} != config fps {fps} - {rerun} with --fps {fps}")
    if len(data["mouth"]) != data["frames"]:
        raise ValueError(f"{path}: mouth has {len(data['mouth'])} entries but frames={data['frames']} - {rerun}")
    if abs(data["duration_s"] - total_duration) > 1.0 / fps:
        raise ValueError(f"{path}: built for {data['duration_s']}s audio but TOTAL_DURATION is "
                         f"{total_duration}s - narration changed since; {rerun}")
    return data
```

- [ ] **Step 5: Run the tests to verify they pass**

Run: `python -m pytest tests/test_avatar_lib.py -v`
Expected: all PASS.

- [ ] **Step 6: Lint and commit**

```bash
ruff check .
git add scripts/avatar_lib.py tests/conftest.py tests/test_avatar_lib.py
git commit -m "Avatar: shared module (AVATAR config, ranges, geometry, mouth-file validation) + tests"
```

---

### Task 2: Mouth file builder (pipeline step 1.5)

**Files:**
- Create: `scripts/build_avatar_track.py`
- Test: `tests/test_build_avatar_track.py`

**Interfaces:**
- Consumes: `avatar_lib.BLINK_FRAMES`, `avatar_lib.MOUTH_FILE_VERSION`, `avatar_lib.mouth_path_for_audio`.
- Produces:
  - `frame_rms(samples: np.ndarray, sr: int, fps: int, n_frames: int) -> np.ndarray`
  - `normalise(rms: np.ndarray) -> np.ndarray` (values in [0, 1])
  - `quantise(norm: np.ndarray) -> list[int]` (0–3)
  - `debounce(levels: list[int], min_hold: int = 2) -> list[int]`
  - `blink_schedule(slug: str, n_frames: int, fps: int) -> list[int]`
  - `build_track(samples, sr, fps, duration_s, slug, source) -> dict` (the mouth-file dict)
  - CLI: `python scripts/build_avatar_track.py audio/<slug>.mp3 [--fps 25] [--out PATH]`

- [ ] **Step 1: Write the failing tests**

`tests/test_build_avatar_track.py`:
```python
import subprocess

import numpy as np
import pytest

import build_avatar_track as bat

SR = 16000


def tone(seconds, amp):
    t = np.arange(int(seconds * SR)) / SR
    return (amp * np.sin(2 * np.pi * 220 * t)).astype(np.float32)


def test_frame_rms_shape_and_silence():
    samples = np.concatenate([np.zeros(SR, np.float32), tone(1.0, 0.5)])
    rms = bat.frame_rms(samples, SR, 25, 50)
    assert rms.shape == (50,)
    assert rms[:20].max() == 0.0
    assert rms[30:].min() > 0.3


def test_normalise_silent_input_is_all_zero():
    assert not bat.normalise(np.zeros(10)).any()


def test_normalise_scales_to_95th_percentile():
    rms = np.array([0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])
    out = bat.normalise(rms)
    assert out.max() == pytest.approx(1.0)
    assert out[0] == 0.0


def test_quantise_thresholds():
    assert bat.quantise(np.array([0.0, 0.07, 0.08, 0.34, 0.35, 0.64, 0.65, 1.0])) == [0, 0, 1, 1, 2, 2, 3, 3]


@pytest.mark.parametrize("levels,expected", [
    ([0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0]),             # opening lags one frame
    ([0, 2, 2, 2, 3, 2, 2], [0, 0, 2, 2, 2, 2, 2]),       # one-frame flicker ignored
    ([0, 2, 2, 2, 0, 2, 2, 2], [0, 0, 2, 2, 0, 0, 2, 2]), # silence closes at once
    ([], []),
])
def test_debounce(levels, expected):
    assert bat.debounce(levels) == expected


def test_blink_schedule_deterministic_and_spaced():
    a = bat.blink_schedule("some-slug", 25 * 600, 25)
    assert a == bat.blink_schedule("some-slug", 25 * 600, 25)
    assert a != bat.blink_schedule("other-slug", 25 * 600, 25)
    gaps = np.diff(a)
    assert gaps.min() >= 3 * 25 - 1 and gaps.max() <= 6 * 25 + 1
    assert a[0] >= 3 * 25 - 1
    assert a[-1] + 3 <= 25 * 600


def test_build_track_shape():
    samples = np.concatenate([np.zeros(SR, np.float32), tone(3.0, 0.4)])
    track = bat.build_track(samples, SR, 25, 4.0, "slug", "audio/slug.mp3")
    assert track["version"] == 1 and track["fps"] == 25
    assert track["frames"] == 100 == len(track["mouth"])
    assert set(track["mouth"]) <= set("0123")
    assert track["mouth"][:20] == "0" * 20
    assert "0" not in track["mouth"][35:95]


def test_build_track_silent_audio_all_closed():
    track = bat.build_track(np.zeros(SR * 2, np.float32), SR, 25, 2.0, "s", "audio/s.mp3")
    assert track["mouth"] == "0" * 50


def test_cli_end_to_end(tmp_path):
    mp3 = tmp_path / "clip.mp3"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono",
                    "-f", "lavfi", "-i", "sine=frequency=220:sample_rate=16000",
                    "-filter_complex", "[0:a]atrim=0:1[s];[1:a]atrim=0:2[t];[s][t]concat=n=2:v=0:a=1",
                    str(mp3)], check=True)
    subprocess.run(["python", "scripts/build_avatar_track.py", str(mp3)], check=True)
    import json
    data = json.loads((tmp_path / "clip.avatar.json").read_text(encoding="utf-8"))
    assert data["frames"] == len(data["mouth"])
    assert abs(data["duration_s"] - 3.0) < 0.1
    assert data["mouth"][:20] == "0" * 20
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_build_avatar_track.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'build_avatar_track'`.

- [ ] **Step 3: Write the implementation**

`scripts/build_avatar_track.py`:
```python
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
# Normalised-loudness cut points between mouth levels 0|1|2|3. Tuned by eye
# on the lip-sync preview (plan Task 6).
LEVEL_THRESHOLDS = (0.08, 0.35, 0.65)
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/test_build_avatar_track.py -v`
Expected: all PASS.

- [ ] **Step 5: Check against a real narration (Barings)**

Run: `python scripts/build_avatar_track.py audio/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank.mp3`
Expected: `frames` = `16274` (`int(650.975 * 25)`); level spread mostly 1–2, `0` in the ~15–30% range (pauses), `3` small. Then check pauses are closed:
```bash
python -c "
import json
t=json.load(open('audio/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank.timing.json',encoding='utf-8'))
m=json.load(open('audio/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank.avatar.json',encoding='utf-8'))['mouth']
items=t if isinstance(t,list) else t.get('sentences',t)
print(type(items), str(items[0])[:200])
"
```
Inspect the printed structure, then for 5 sentence boundaries take the gap midpoint between one sentence's end and the next's start, and confirm `m[int(mid*25)] == '0'`. Record the spread in the commit message. Do not commit the Barings `.avatar.json` yet (Task 6 decides the thresholds first).

- [ ] **Step 6: Lint and commit**

```bash
ruff check .
git add scripts/build_avatar_track.py tests/test_build_avatar_track.py
git commit -m "Avatar: mouth/blink track builder (step 1.5) + tests"
```

---

### Task 3: Placeholder SVG and the PNG layer builder

The likeness comes later (Task 7); a placeholder face lets Tasks 4–6 run end to end now. The layer `id`s are the contract both share.

**Files:**
- Create: `assets/avatar/avatar.svg` (placeholder)
- Create: `scripts/build_avatar.py`
- Create: `assets/avatar/png/*.png` (generated)
- Test: `tests/test_build_avatar.py`

**Interfaces:**
- Consumes: `avatar_lib.SVG_PATH`, `avatar_lib.PNG_DIR`, `avatar_lib.LAYER_NAMES`.
- Produces:
  - `layer_svg(svg_text: str, keep: str) -> str` — SVG text with every other `LAYER_NAMES` group hidden
  - `build_layers(svg_path: Path, png_dir: Path, size: int = 512) -> list[Path]`
  - CLI: `python scripts/build_avatar.py [--svg PATH] [--out-dir DIR] [--size 512]`
  - Files: `assets/avatar/png/{body,eyes-open,eyes-closed,mouth-0..3}.png`, 512×512 RGBA

- [ ] **Step 1: Install resvg-py and confirm its API**

```bash
pip install resvg-py==0.5.0
python -c "import resvg_py, inspect; print(inspect.signature(resvg_py.svg_to_bytes))"
```
Expected: a signature including `svg_string`, `width`, `height`. If the parameter names differ, use the printed ones in Step 4's `render_png` and note it in the commit message.

- [ ] **Step 2: Write the placeholder SVG**

`assets/avatar/avatar.svg`:
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <!-- PLACEHOLDER avatar. Replaced by Chris's likeness in plan Task 7.
       Layer contract: groups with ids body, eyes-open, eyes-closed,
       mouth-0..mouth-3, brows. build_avatar.py renders each of the first
       seven alone onto a 512x512 transparent canvas; brows stays inside body
       for now. Everything must sit inside the r=250 circle. -->
  <g id="body">
    <circle cx="256" cy="256" r="250" fill="#2f4858"/>
    <circle cx="256" cy="256" r="250" fill="none" stroke="#f2f2f2" stroke-width="10"/>
    <path d="M86 470 Q256 350 426 470 L426 512 L86 512 Z" fill="#33658a"/>
    <ellipse cx="256" cy="236" rx="120" ry="140" fill="#e8b996"/>
    <path d="M136 210 Q140 90 256 86 Q372 90 376 210 Q330 140 256 146 Q182 140 136 210 Z" fill="#1d1d1d"/>
    <g id="brows">
      <rect x="182" y="186" width="56" height="10" rx="5" fill="#1d1d1d"/>
      <rect x="274" y="186" width="56" height="10" rx="5" fill="#1d1d1d"/>
    </g>
  </g>
  <g id="eyes-open">
    <ellipse cx="210" cy="226" rx="14" ry="16" fill="#1d1d1d"/>
    <ellipse cx="302" cy="226" rx="14" ry="16" fill="#1d1d1d"/>
  </g>
  <g id="eyes-closed">
    <rect x="194" y="224" width="32" height="6" rx="3" fill="#1d1d1d"/>
    <rect x="286" y="224" width="32" height="6" rx="3" fill="#1d1d1d"/>
  </g>
  <g id="mouth-0"><rect x="226" y="306" width="60" height="8" rx="4" fill="#8a3b3b"/></g>
  <g id="mouth-1"><ellipse cx="256" cy="310" rx="30" ry="9" fill="#5a1e1e"/></g>
  <g id="mouth-2"><ellipse cx="256" cy="312" rx="32" ry="17" fill="#5a1e1e"/></g>
  <g id="mouth-3"><ellipse cx="256" cy="316" rx="34" ry="26" fill="#5a1e1e"/></g>
</svg>
```

- [ ] **Step 3: Write the failing tests**

`tests/test_build_avatar.py`:
```python
import pytest
from PIL import Image, ImageChops

import avatar_lib as al
import build_avatar as ba


def test_layer_svg_hides_other_layers():
    import xml.etree.ElementTree as ET
    out = ba.layer_svg(al.SVG_PATH.read_text(encoding="utf-8"), "mouth-2")
    styles = {el.get("id"): el.get("style") for el in ET.fromstring(out).iter() if el.get("id") in al.LAYER_NAMES}
    assert styles.pop("mouth-2") is None
    assert set(styles.values()) == {"display:none"} and len(styles) == len(al.LAYER_NAMES) - 1


def test_layer_svg_missing_layer_errors():
    with pytest.raises(ValueError, match="mouth-3"):
        ba.layer_svg('<svg xmlns="http://www.w3.org/2000/svg"><g id="body"/></svg>', "body")


def test_build_layers(tmp_path):
    paths = ba.build_layers(al.SVG_PATH, tmp_path, size=128)
    assert [p.stem for p in paths] == al.LAYER_NAMES
    imgs = {p.stem: Image.open(p) for p in paths}
    for im in imgs.values():
        assert im.size == (128, 128) and im.mode == "RGBA"
    assert imgs["body"].getpixel((64, 64))[3] == 255          # opaque centre
    assert imgs["body"].getpixel((1, 1))[3] == 0              # transparent outside circle
    assert imgs["eyes-open"].getpixel((64, 64))[3] == 0       # eyes layer is only the eyes
    assert ImageChops.difference(imgs["mouth-0"], imgs["mouth-3"]).getbbox() is not None
```

- [ ] **Step 4: Run the tests to verify they fail**

Run: `python -m pytest tests/test_build_avatar.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'build_avatar'`.

- [ ] **Step 5: Write the implementation**

`scripts/build_avatar.py`:
```python
"""Rasterise the layered avatar SVG into the PNG layers the renderer stacks.

    python scripts/build_avatar.py [--svg assets/avatar/avatar.svg] [--size 512]

Each name in avatar_lib.LAYER_NAMES is a <g id=...> in the SVG. For each,
every *other* named layer is hidden and the result rendered to a
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
from avatar_lib import LAYER_NAMES, PNG_DIR, SVG_PATH  # noqa: E402

SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def layer_svg(svg_text, keep):
    root = ET.fromstring(svg_text)
    found = {el.get("id"): el for el in root.iter() if el.get("id") in LAYER_NAMES}
    missing = [n for n in LAYER_NAMES if n not in found]
    if missing:
        raise ValueError(f"avatar SVG is missing layer group(s): {', '.join(missing)}")
    for name, el in found.items():
        if name != keep:
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
    for name in LAYER_NAMES:
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
```

- [ ] **Step 6: Run the tests to verify they pass**

Run: `python -m pytest tests/test_build_avatar.py -v`
Expected: all PASS.

- [ ] **Step 7: Generate the committed PNGs and eyeball them**

```bash
python scripts/build_avatar.py
```
Expected: 7 `Wrote assets/avatar/png/<name>.png` lines. View `body.png`, `mouth-3.png` and `eyes-closed.png` with the Read tool and confirm the face, the open mouth and the closed eyes look right.

- [ ] **Step 8: Lint and commit**

```bash
ruff check .
git add assets/avatar/avatar.svg assets/avatar/png scripts/build_avatar.py tests/test_build_avatar.py
git commit -m "Avatar: layered placeholder SVG + PNG layer builder (resvg-py) + tests"
```

---

### Task 4: Avatar track renderer (pipeline step 6a)

**Files:**
- Create: `scripts/render_avatar_track.py`
- Test: `tests/test_render_avatar_track.py`

**Interfaces:**
- Consumes: from `avatar_lib`: `avatar_settings`, `bubble_geometry`, `alpha_at`, `mouth_path_for_config`, `load_mouth_file`, `video_dims`, `PNG_DIR`, `BLINK_FRAMES`, `LAYER_NAMES`. From `watch_video_lib`: `load_config(path)`. PNGs from Task 3.
- Produces:
  - `load_layers(diameter: int, png_dir: Path = PNG_DIR) -> dict[str, Image.Image]`
  - `compose_avatar(layers: dict, mouth_level: int, eyes_closed: bool) -> Image.Image`
  - `with_alpha(img: Image.Image, a: float) -> Image.Image`
  - `blink_frame_set(blinks: list[int]) -> set[int]`
  - `render_track(cfg, out_path: Path, png_dir: Path = PNG_DIR) -> bool` (False = no AVATAR, skipped)
  - `default_track_path(config_path: Path) -> Path` = `REPO_ROOT/preview-motion/<config-stem>-avatar.mov`
  - CLI: `python scripts/render_avatar_track.py --config scripts/video-configs/<slug>.py [--out PATH]`

- [ ] **Step 1: Write the failing tests**

`tests/test_render_avatar_track.py`:
```python
import json
import subprocess
import types

from PIL import Image

import avatar_lib as al
import render_avatar_track as rat


def solid_layers(tmp_path, d=64):
    colours = {"body": (0, 0, 255, 255), "eyes-open": (0, 0, 0, 0), "eyes-closed": (0, 0, 0, 0),
               "mouth-0": (0, 0, 0, 0), "mouth-1": (0, 0, 0, 0), "mouth-2": (0, 0, 0, 0),
               "mouth-3": (255, 0, 0, 255)}
    for name, c in colours.items():
        im = Image.new("RGBA", (d, d), (0, 0, 0, 0))
        if c[3]:
            box = (0, 0, d, d) if name == "body" else (d // 4, d // 2, 3 * d // 4, 3 * d // 4)
            im.paste(c, box)
        im.save(tmp_path / f"{name}.png")
    return tmp_path


def test_compose_stacks_mouth_on_body(tmp_path):
    layers = rat.load_layers(32, solid_layers(tmp_path))
    closed = rat.compose_avatar(layers, 0, False)
    wide = rat.compose_avatar(layers, 3, False)
    assert closed.getpixel((16, 20)) == (0, 0, 255, 255)
    assert wide.getpixel((16, 20)) == (255, 0, 0, 255)


def test_with_alpha_scales_only_alpha():
    im = Image.new("RGBA", (2, 2), (10, 20, 30, 200))
    assert rat.with_alpha(im, 0.5).getpixel((0, 0)) == (10, 20, 30, 100)
    assert rat.with_alpha(im, 1.0) is im


def test_blink_frame_set():
    assert rat.blink_frame_set([10, 50]) == {10, 11, 12, 50, 51, 52}


def fake_cfg(tmp_path, avatar=True):
    timing = tmp_path / "t.timing.json"
    track = {"version": 1, "fps": 25, "frames": 50, "duration_s": 2.0, "source": "x",
             "mouth": "0" * 10 + "3" * 40, "blinks": []}
    (tmp_path / "t.avatar.json").write_text(json.dumps(track), encoding="utf-8")
    kw = {"TOTAL_DURATION": 2.0, "TIMING_JSON": str(timing), "WIDTH": 320, "HEIGHT": 180}
    if avatar:
        kw["AVATAR"] = {"ranges": [(0.4, 1.6)], "size": 0.4, "margin": 0.05, "fade": 0.0}
    return types.SimpleNamespace(**kw)


def probe(path, entries):
    return subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
                           "-show_entries", f"stream={entries}", "-of", "csv=p=0", str(path)],
                          check=True, capture_output=True, text=True).stdout.strip()


def test_render_track_frames_and_alpha(tmp_path):
    png_dir = tmp_path / "png"
    png_dir.mkdir()
    solid_layers(png_dir)
    out = tmp_path / "a.mov"
    assert rat.render_track(fake_cfg(tmp_path), out, png_dir) is True
    info = probe(out, "pix_fmt,nb_read_frames")
    assert info == "argb,50"
    frame = tmp_path / "f.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(out), "-vf", "select=eq(n\\,30)",
                    "-frames:v", "1", str(frame)], check=True)
    im = Image.open(frame).convert("RGBA")
    assert im.size == (72, 72)                     # 0.4 * 180
    assert im.getpixel((36, 4))[3] == 255          # visible inside the range
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(out), "-vf", "select=eq(n\\,2)",
                    "-frames:v", "1", str(frame)], check=True)
    assert Image.open(frame).convert("RGBA").getpixel((36, 4))[3] == 0   # transparent before it


def test_render_track_skips_without_avatar(tmp_path):
    assert rat.render_track(fake_cfg(tmp_path, avatar=False), tmp_path / "a.mov") is False
    assert not (tmp_path / "a.mov").exists()


def test_default_track_path():
    from pathlib import Path
    assert rat.default_track_path(Path("scripts/video-configs/foo.py")) == al.REPO_ROOT / "preview-motion/foo-avatar.mov"
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_render_avatar_track.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'render_avatar_track'`.

- [ ] **Step 3: Write the implementation**

`scripts/render_avatar_track.py`:
```python
"""Render the avatar bubble as a transparent video track (pipeline step 6a).

    python scripts/render_avatar_track.py --config scripts/video-configs/<slug>.py

Reads the config's AVATAR settings, audio/<slug>.avatar.json (step 1.5)
and the PNG layers in assets/avatar/png/, and writes
preview-motion/<slug>-avatar.mov: a bubble-sized qtrle ARGB video the full
length of the main video, transparent outside AVATAR's ranges and faded
at their edges, so step 6b can lay it over <slug>.mp4 frame for frame.
A config without AVATAR is skipped (exit 0). Single process; the work per
frame is stacking three small images, so memory stays tiny.
"""

import argparse
import subprocess
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avatar_lib import (  # noqa: E402
    BLINK_FRAMES, LAYER_NAMES, PNG_DIR, REPO_ROOT, alpha_at, avatar_settings,
    bubble_geometry, load_mouth_file, mouth_path_for_config, video_dims,
)
from watch_video_lib import load_config  # noqa: E402


def load_layers(diameter, png_dir=PNG_DIR):
    png_dir = Path(png_dir)
    layers = {}
    for name in LAYER_NAMES:
        path = png_dir / f"{name}.png"
        if not path.exists():
            raise FileNotFoundError(f"missing avatar layer {path} - run python scripts/build_avatar.py")
        layers[name] = Image.open(path).convert("RGBA").resize((diameter, diameter), Image.LANCZOS)
    return layers


def compose_avatar(layers, mouth_level, eyes_closed):
    img = layers["body"].copy()
    img.alpha_composite(layers["eyes-closed" if eyes_closed else "eyes-open"])
    img.alpha_composite(layers[f"mouth-{mouth_level}"])
    return img


def with_alpha(img, a):
    if a >= 1.0:
        return img
    r, g, b, alpha = img.split()
    return Image.merge("RGBA", (r, g, b, alpha.point(lambda v: int(v * a))))


def blink_frame_set(blinks):
    return {f for b in blinks for f in range(b, b + BLINK_FRAMES)}


def default_track_path(config_path):
    return REPO_ROOT / "preview-motion" / f"{Path(config_path).stem}-avatar.mov"


def render_track(cfg, out_path, png_dir=PNG_DIR):
    settings = avatar_settings(cfg)
    if settings is None:
        print("No AVATAR in this config - step 6a skipped.")
        return False
    out_w, out_h, fps = video_dims(cfg)
    track = load_mouth_file(mouth_path_for_config(cfg), fps, cfg.TOTAL_DURATION)
    d, _, _ = bubble_geometry(settings, out_w, out_h)
    layers = load_layers(d, png_dir)
    blinking = blink_frame_set(track["blinks"])
    mouth = track["mouth"]
    total_frames = int(cfg.TOTAL_DURATION * fps)  # same count watch_video_lib.render() uses
    blank = bytes(d * d * 4)
    cache = {}

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{d}x{d}",
         "-r", str(fps), "-i", "-", "-c:v", "qtrle", "-pix_fmt", "argb", str(out_path)],
        stdin=subprocess.PIPE)
    try:
        for i in range(total_frames):
            a = alpha_at(i / fps, settings["ranges"], settings["fade"])
            if a <= 0.0:
                proc.stdin.write(blank)
                continue
            key = (int(mouth[min(i, len(mouth) - 1)]), i in blinking)
            if key not in cache:
                cache[key] = compose_avatar(layers, *key)
            proc.stdin.write(with_alpha(cache[key], a).tobytes())
            if i % (fps * 60) == 0:
                print(f"frame {i}/{total_frames} t={i / fps:.0f}s", file=sys.stderr)
    finally:
        proc.stdin.close()
        proc.wait()
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg exited {proc.returncode} writing {out_path}")
    print(f"Wrote {out_path} - {total_frames} frames, {d}x{d}, ranges {settings['ranges']}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True)
    ap.add_argument("--out", help="default: preview-motion/<config-stem>-avatar.mov")
    args = ap.parse_args()
    cfg = load_config(args.config)
    render_track(cfg, Path(args.out) if args.out else default_track_path(args.config))


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/test_render_avatar_track.py -v`
Expected: all PASS.

- [ ] **Step 5: Lint and commit**

```bash
ruff check .
git add scripts/render_avatar_track.py tests/test_render_avatar_track.py
git commit -m "Avatar: transparent bubble track renderer (step 6a) + tests"
```

---

### Task 5: Overlay (pipeline step 6b)

**Files:**
- Create: `scripts/overlay_avatar.py`
- Test: `tests/test_overlay_avatar.py`

**Interfaces:**
- Consumes: `avatar_lib.avatar_settings`, `avatar_lib.bubble_geometry`, `avatar_lib.video_dims`; `render_avatar_track.default_track_path`; `watch_video_lib.load_config`.
- Produces:
  - `build_overlay_cmd(in_path: Path, track_path: Path, out_path: Path, x: int, y: int) -> list[str]`
  - `overlay(cfg, in_path: Path, track_path: Path, out_path: Path) -> bool` (False = no AVATAR, skipped)
  - CLI: `python scripts/overlay_avatar.py --config <cfg> --in preview-motion/<slug>.mp4 --out preview-motion/<slug>-avatar.mp4 [--track PATH]`

- [ ] **Step 1: Write the failing tests**

`tests/test_overlay_avatar.py`:
```python
import subprocess
import types

import pytest
from PIL import Image

import overlay_avatar as oa


def make_main(path, audio=True):
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=0x00ff00:s=320x180:r=25:d=2"]
    if audio:
        cmd += ["-f", "lavfi", "-i", "sine=frequency=220:d=2", "-c:a", "aac"]
    cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", str(path)]
    subprocess.run(cmd, check=True)


def make_track(path):
    # 72x72 opaque red bubble, all 50 frames.
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=0xff0000:s=72x72:r=25:d=2",
                    "-vf", "format=argb", "-c:v", "qtrle", "-pix_fmt", "argb", str(path)], check=True)


def cfg():
    return types.SimpleNamespace(TOTAL_DURATION=2.0, TIMING_JSON="audio/x.timing.json", WIDTH=320, HEIGHT=180,
                                 AVATAR={"ranges": [(0, None)], "size": 0.4, "margin": 0.05})


def grab(path, n, tmp_path):
    f = tmp_path / f"g{n}.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-vf", f"select=eq(n\\,{n})",
                    "-frames:v", "1", str(f)], check=True)
    return Image.open(f).convert("RGB")


def test_build_overlay_cmd_keeps_audio_optional():
    cmd = oa.build_overlay_cmd("in.mp4", "a.mov", "out.mp4", 10, 20)
    assert "0:a?" in cmd and "-c:a" in cmd and "copy" in cmd
    assert any("overlay=x=10:y=20" in c for c in cmd)


def test_overlay_places_bubble(tmp_path):
    main, track, out = tmp_path / "m.mp4", tmp_path / "a.mov", tmp_path / "o.mp4"
    make_main(main)
    make_track(track)
    assert oa.overlay(cfg(), main, track, out) is True
    im = grab(out, 25, tmp_path)
    # bottom-right: d=72, m=9 -> x=239, y=99; centre ~ (275, 135)
    r, g, b = im.getpixel((275, 135))
    assert r > 200 and g < 60
    r, g, b = im.getpixel((40, 40))
    assert g > 200 and r < 60
    streams = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type",
                              "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout.split()
    assert streams.count("audio") == 1


def test_overlay_without_audio(tmp_path):
    main, track, out = tmp_path / "m.mp4", tmp_path / "a.mov", tmp_path / "o.mp4"
    make_main(main, audio=False)
    make_track(track)
    assert oa.overlay(cfg(), main, track, out) is True
    assert out.exists()


def test_overlay_refuses_in_equals_out(tmp_path):
    main = tmp_path / "m.mp4"
    make_main(main)
    with pytest.raises(ValueError, match="overwrite"):
        oa.overlay(cfg(), main, tmp_path / "a.mov", main)


def test_overlay_missing_track_names_step(tmp_path):
    main = tmp_path / "m.mp4"
    make_main(main)
    with pytest.raises(FileNotFoundError, match="6a"):
        oa.overlay(cfg(), main, tmp_path / "nope.mov", tmp_path / "o.mp4")


def test_overlay_skips_without_avatar(tmp_path):
    c = cfg()
    del c.AVATAR
    assert oa.overlay(c, tmp_path / "m.mp4", tmp_path / "a.mov", tmp_path / "o.mp4") is False
```

- [ ] **Step 2: Run the tests to verify they fail**

Run: `python -m pytest tests/test_overlay_avatar.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'overlay_avatar'`.

- [ ] **Step 3: Write the implementation**

`scripts/overlay_avatar.py`:
```python
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
    _, x, y = bubble_geometry(settings, out_w, out_h)
    subprocess.run(build_overlay_cmd(in_path, track_path, out_path, x, y), check=True)
    print(f"Wrote {out_path}")
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
```

- [ ] **Step 4: Run the tests to verify they pass**

Run: `python -m pytest tests/test_overlay_avatar.py -v`
Expected: all PASS.

- [ ] **Step 5: Run the whole suite, lint, commit**

```bash
python -m pytest tests -v
ruff check .
git add scripts/overlay_avatar.py tests/test_overlay_avatar.py
git commit -m "Avatar: ffmpeg overlay onto the main video (step 6b) + tests"
```

---

### Task 6: Lip-sync preview and Barings dry run (placeholder face)

Verification on real data; tunes `LEVEL_THRESHOLDS` with Chris. Uses the already-rendered `preview-motion/barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank.mp4` (exists, 1 Oct), so no step-6 re-render. The test config lives in `scratch/` so the published Barings config is untouched.

**Files:**
- Create (uncommitted): `scratch/avatar-test/barings-avatar.py`, `scratch/avatar-test/preview.mp4`
- Possibly modify: `scripts/build_avatar_track.py` (`LEVEL_THRESHOLDS`, `MIN_HOLD`)

**Interfaces:**
- Consumes: all four scripts from Tasks 2–5.
- Produces: tuned constants; a verified end-to-end run.

- [ ] **Step 1: Make the scratch test config**

```bash
S=barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank
mkdir -p scratch/avatar-test
{ cat scripts/video-configs/$S.py; printf '\nAVATAR = {"ranges": [(0, 30), (-30, None)]}\n'; } > scratch/avatar-test/barings-avatar.py
```

- [ ] **Step 2: Build the mouth file and track**

```bash
python scripts/build_avatar_track.py audio/$S.mp3
python scripts/render_avatar_track.py --config scratch/avatar-test/barings-avatar.py --out scratch/avatar-test/track.mov
```
Expected: `Wrote ... 16274 frames, 144x144, ranges [(0, 30), (620.975, 650.975)]`; note the wall-clock time (spec expects well under a minute).

- [ ] **Step 3: Make the 15 s lip-sync preview for Chris**

```bash
ffmpeg -y -v error -f lavfi -i color=c=0x808080:s=640x360:r=25 \
  -i scratch/avatar-test/track.mov -i audio/$S.mp3 \
  -filter_complex "[1:v]scale=288:288[a];[0:v][a]overlay=(W-w)/2:(H-h)/2:format=auto,format=yuv420p[v]" \
  -map "[v]" -map 2:a -t 15 -c:v libx264 -crf 20 -c:a aac scratch/avatar-test/preview.mp4
```
Hand Chris the path `scratch/avatar-test/preview.mp4` to watch. Ask: does the mouth read as speaking, does it lag or lead, too twitchy or too sluggish, too often wide open? Adjust `LEVEL_THRESHOLDS` (raise to open less) or `MIN_HOLD` (raise for calmer) and repeat Steps 2–3 until Chris approves. Each iteration takes seconds.

- [ ] **Step 4: Full overlay dry run**

```bash
python scripts/overlay_avatar.py --config scratch/avatar-test/barings-avatar.py \
  --in preview-motion/$S.mp4 --out scratch/avatar-test/barings-avatar.mp4 --track scratch/avatar-test/track.mov
```
Note the wall-clock time for the docs. This is a full-length encode — if it would exceed Claude's 10-minute tool timeout, hand Chris the command wrapped in the tee-to-log block (see `docs/production-pipeline.md` §0) to run in his own terminal instead.

- [ ] **Step 5: Verify the output**

```bash
ffmpeg -v error -i scratch/avatar-test/barings-avatar.mp4 -f null -    # must print nothing
for f in preview-motion/$S.mp4 scratch/avatar-test/barings-avatar.mp4; do
  ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -show_entries format=duration -of csv=p=0 $f
done
```
Expected: no decode errors; identical frame counts; durations within one frame. Then extract and view (Read tool) frames at t = 0.1 (mid fade-in, faint bubble), 15 (bubble), 29.9 (fading out), 31 (no bubble), 300 (no bubble), 621.1 (faint, fading in), 640 (bubble):
```bash
for t in 0.1 15 29.9 31 300 621.1 640; do
  ffmpeg -y -v error -ss $t -i scratch/avatar-test/barings-avatar.mp4 -frames:v 1 scratch/avatar-test/t$t.png
done
```
Confirm the bubble sits bottom-right with a margin, the border separates it from the photo behind, and the ranges/fades are where expected.

- [ ] **Step 6: Commit any tuning**

If Step 3 changed constants:
```bash
ruff check . && python -m pytest tests -v
git add scripts/build_avatar_track.py tests/test_build_avatar_track.py
git commit -m "Avatar: tune mouth thresholds after lip-sync preview (Chris-approved)"
```
(If `LEVEL_THRESHOLDS` changed, update `test_quantise_thresholds` to the new cut points in the same commit.)

---

### Task 7: Chris's likeness

Blocked on Chris dropping a front-facing head-and-shoulders photo into `scratch/` (neutral expression, plain background, glasses if usually worn). The photo is never committed.

**Files:**
- Modify: `assets/avatar/avatar.svg` (replace placeholder)
- Regenerate: `assets/avatar/png/*.png`

**Interfaces:**
- Consumes: Task 3's layer contract (same group ids, 512×512 viewBox, everything inside the r=250 circle, `body` includes the circle fill + border).
- Produces: the real avatar; no code changes.

- [ ] **Step 1: Study the photo**

View it with the Read tool. Note face shape, hairline/parting, hair colour, glasses shape, skin tone, typical shirt/collar. Pick a 6–8 colour flat palette from it.

- [ ] **Step 2: Draft the SVG**

Rewrite `assets/avatar/avatar.svg` with the same group ids as the placeholder: `body` (circle background + border, shoulders/shirt, neck, face, ears, hair, glasses frames if any, nose, and `brows` inside it), `eyes-open`, `eyes-closed`, `mouth-0` … `mouth-3` (closed line → slightly open → open → wide, same centre point). Flat fills only, no gradients, no filters. Keep the placeholder's comment block, updated to say it's Chris's likeness.

- [ ] **Step 3: Preview as an Artifact and iterate**

Load the `artifact-design` skill, then publish a small HTML page showing the composed avatar (body + eyes-open + mouth-0) large, plus a strip of the four mouth levels and the blink, side by side with nothing else. Do not put the reference photo in the artifact. Iterate on Chris's feedback until he approves the likeness.

- [ ] **Step 4: Rebuild layers and re-check**

```bash
python scripts/build_avatar.py
python -m pytest tests/test_build_avatar.py -v
```
View `body.png` and `mouth-3.png` with the Read tool. Re-run Task 6 Steps 2–3 and send Chris the new `scratch/avatar-test/preview.mp4` for a final look at bubble size (144 px on a 720p frame).

- [ ] **Step 5: Commit**

```bash
git add assets/avatar/avatar.svg assets/avatar/png
git commit -m "Avatar: Chris's likeness replaces the placeholder (approved via Artifact preview)"
```

---

### Task 8: YouTube disclosure line and documentation

**Files:**
- Modify: `scripts/stage_youtube_text.py` (around lines 600–615, the `narration_line` and its `out_lines.append`)
- Modify: `docs/production-pipeline.md` (§0 overview, §1, §6, §8, §14)
- Modify: `CLAUDE.md` (binary-exception note)
- Test: `tests/test_stage_youtube_avatar.py`

**Interfaces:**
- Consumes: `stage_youtube_text.load_video_config(path)`.
- Produces: `avatar_disclosure(main_cfg) -> str | None` in `stage_youtube_text.py`.

- [ ] **Step 1: Write the failing test**

`tests/test_stage_youtube_avatar.py`:
```python
import types

import stage_youtube_text as syt


def test_disclosure_only_with_avatar():
    assert syt.avatar_disclosure(None) is None
    assert syt.avatar_disclosure(types.SimpleNamespace()) is None
    line = syt.avatar_disclosure(types.SimpleNamespace(AVATAR={"ranges": [(0, 30)]}))
    assert line == "Presenter: an illustrated avatar of the author, animated locally from the narration audio."
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python -m pytest tests/test_stage_youtube_avatar.py -v`
Expected: FAIL with `AttributeError: module 'stage_youtube_text' has no attribute 'avatar_disclosure'`.

- [ ] **Step 3: Implement**

In `scripts/stage_youtube_text.py`, add after `load_video_config`:
```python
def avatar_disclosure(main_cfg) -> str | None:
    """Description line for a main video with the avatar overlay (its
    config sets AVATAR). The voice is already disclosed by the narration
    line; this covers the on-screen presenter."""
    if main_cfg is None or getattr(main_cfg, "AVATAR", None) is None:
        return None
    return "Presenter: an illustrated avatar of the author, animated locally from the narration audio."
```
In `main()`, directly after the existing `out_lines.append(narration_line)` in the FULL VIDEO block, add:
```python
    avatar_line = avatar_disclosure(load_video_config(main_config_path) if main_config_path else None)
    if avatar_line:
        out_lines.append(avatar_line)
```
(The Short block is untouched — Phase 1 is main video only.)

- [ ] **Step 4: Run tests**

Run: `python -m pytest tests -v`
Expected: all PASS.

- [ ] **Step 5: Update `docs/production-pipeline.md`**

- **§0 overview:** add steps 1.5, 6a, 6b to the step list, each marked optional ("only when the main config sets `AVATAR`").
- **§1:** new subsection **1.5 Build the avatar mouth track (optional)** after 1.4: what it does (one line), when to re-run (any time the mp3 changes — 6a refuses a stale file), and the command in the tee-to-log block form:
  ```
  { echo; date; echo "=== 1.5 Build avatar mouth track ==="
    cmd=(python scripts/build_avatar_track.py audio/<slug>.mp3)
    echo "\$ ${cmd[*]}"; echo
    time "${cmd[@]}"
    echo
  } 2>&1 | tee -a logs/<slug>.log
  ```
- **§3:** document the optional `AVATAR` dict (copy the block and key meanings from spec §3 "Config"), including Phase 2's `"ranges": [(0, None)]`.
- **§6:** new subsections **6a Render the avatar track** and **6b Overlay the avatar**, each with the tee-to-log command block (6a: `python scripts/render_avatar_track.py --config scripts/video-configs/<slug>.py`; 6b: `python scripts/overlay_avatar.py --config scripts/video-configs/<slug>.py --in preview-motion/<slug>.mp4 --out preview-motion/<slug>-avatar.mp4`), the timings measured in Task 6, the ordering rule (route-walk splices first, overlay last), and "upload `<slug>-avatar.mp4`, not `<slug>.mp4`, when it exists".
- **§8:** note that verification runs against `<slug>-avatar.mp4` when present, plus the range-boundary spot frames from Task 6 Step 5.
- **§14 file reference:** entries for `scripts/avatar_lib.py`, `build_avatar.py`, `build_avatar_track.py`, `render_avatar_track.py`, `overlay_avatar.py`, `assets/avatar/`, `audio/<slug>.avatar.json`, `tests/`.

- [ ] **Step 6: Update `CLAUDE.md`**

In the **Post conventions** images bullet's area (next to the OSM-tile exception wording in **Route animations**), add one sentence: `assets/avatar/png/*.png` (the avatar presenter's rasterised layers, built from `assets/avatar/avatar.svg` by `scripts/build_avatar.py`) are committed — another deliberate exception to the no-binaries rule. Under **Python linting**, add: tests live in `tests/` and run with `python -m pytest tests -v`.

- [ ] **Step 7: Lint, test, commit, push**

```bash
ruff check . && python -m pytest tests -v
git add scripts/stage_youtube_text.py tests/test_stage_youtube_avatar.py docs/production-pipeline.md CLAUDE.md
git commit -m "Avatar: YouTube disclosure line, pipeline steps 1.5/6a/6b documented"
git push
```

- [ ] **Step 8: Tell Chris about the command changes**

His saved command template needs three new optional blocks (1.5, 6a, 6b) and the upload file changes to `<slug>-avatar.mp4` for avatar posts. List them explicitly in the handoff message.
