# Avatar Shaped Mouths Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Give the avatar four shaped mouth positions (closed m/b/p, lip-on-teeth f/v, pursed oo/w/o, wide ee) timed from Kokoro's own per-phoneme durations, layered on the existing loudness-driven openness.

**Architecture:** A new pure module `scripts/avatar_visemes.py` turns Kokoro phonemes + `pred_dur` into time spans, then into one shape character per video frame, with a per-sentence integrity check against `timing.json`. A thin adapter in the same module loads Kokoro once and patches *our own* pipeline instance's `model.forward_with_tokens` to a durations-only version (no audio decoding). `build_avatar_track.py` writes the shapes into mouth file version 2; `render_avatar_track.py` picks `mouth-0` on silence, else the shape's layer, else the loudness level. Four new SVG mouth layers.

**Tech Stack:** Python 3.12, kokoro 0.9.4 / misaki 0.9.4 (already installed, CPU torch), numpy, Pillow, pytest 8, resvg-py.

**Spec:** `docs/superpowers/specs/2026-10-02-avatar-shaped-mouths-design.md`

## Global Constraints

- Everything runs locally; no external services. Kokoro model is already cached on disk.
- Kokoro duration unit: `UNIT_S = 0.025` (600 samples at 24 kHz). `pred_dur` = one leading boundary entry + one entry per phoneme character Kokoro kept + one trailing boundary entry.
- Kokoro drops phoneme characters not in `model.vocab` (`filter(None, map(vocab.get, phonemes))`) before running; durations pair with the **kept** characters only.
- Integrity tolerance per sentence: `abs(units * 0.025 - duration_s) <= 0.001`.
- Shape table (exact): `M` = `m b p`; `F` = `f v`; `U` = `u ʊ w O Q ɔ ɒ`; `E` = `i ɪ`; everything else `.`. `ː` inherits the previous character's shape; `ˈ ˌ` inherit the next character's shape. Priority `M > F > U > E > .`.
- Per-frame mouth: level `0` → `mouth-0`; else shape in `MFUE` → `mouth-<shape>`; else `mouth-<level>`.
- Mouth file: version 2 adds `shape` (one char per frame, `len(shape) == frames`) and `shape_fallback` (list of sentence indices); `--no-shapes` writes version 1. `load_mouth_file` accepts versions 1 and 2.
- `generate_narration.py` and `watch_video_lib.py` are not modified. The `forward_with_tokens` patch applies only to the pipeline instance `avatar_visemes` builds.
- `ruff check .` clean and `python -m pytest tests -q` green before every commit; the `slow` Kokoro test also passes (`python -m pytest tests -m slow -q`) before each commit touching `avatar_visemes.py`.
- Commit messages end with:
  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: https://claude.ai/code/session_014vyi5DydGd12SnQWie299V
  ```

## Review Focus

1. **A narration whose overrides changed after some sentences were cached** — expect those sentences listed as fallen back and given no shapes, never shapes shifted onto the wrong words. Pinned in Task 1 (`test_compute_shapes_integrity_mismatch_falls_back`).
2. **A phoneme character Kokoro drops (not in its vocab)** — expect durations to pair with the kept characters, not shift by one. Pinned in Task 1 (`test_phoneme_spans_skips_chars_not_in_vocab`).
3. **A long sentence Kokoro splits into several chunks** — expect the second chunk's spans to start where the first ended. Pinned in Task 1 (`test_compute_shapes_multi_chunk_sentence`).
4. **An old version-1 mouth file, or one built with `--no-shapes`** — expect exactly Phase 1's rendering. Pinned in Task 4 (`test_render_v1_track_uses_levels_only`).
5. **A shape landing on a silent frame** — expect the closed `mouth-0`, since silence always wins. Pinned in Task 4 (`test_mouth_layer_for`).

---

## File Structure

| Path | Responsibility |
|---|---|
| `scripts/avatar_visemes.py` (new) | char→shape, Kokoro result → spans, spans → per-frame shapes, per-sentence integrity, Kokoro durations-only adapter |
| `scripts/build_avatar_track.py` (modify) | `--no-shapes`, `--voice`; call `avatar_visemes`; write v2 |
| `scripts/avatar_lib.py` (modify) | `LAYER_NAMES` + 4; `MOUTH_FILE_VERSIONS = (1, 2)`; validate `shape` |
| `scripts/render_avatar_track.py` (modify) | `mouth_layer_for()`; per-frame choice; `compose_avatar` accepts a layer name |
| `assets/avatar/avatar.svg`, `assets/avatar/png/` | 4 new mouth layers |
| `pyproject.toml` | pytest `slow` marker, skipped by default |
| `tests/test_avatar_visemes.py`, `tests/test_avatar_visemes_kokoro.py` (new); `tests/test_avatar_lib.py`, `tests/test_build_avatar_track.py`, `tests/test_render_avatar_track.py`, `tests/test_build_avatar.py` (modify) | tests |
| `docs/production-pipeline.md`, `docs/superpowers/specs/2026-10-02-avatar-presenter-design.md` | docs |

---

### Task 1: Viseme logic (pure)

**Files:**
- Create: `scripts/avatar_visemes.py`
- Test: `tests/test_avatar_visemes.py`

**Interfaces:**
- Consumes: nothing.
- Produces:
  - `UNIT_S: float = 0.025`, `SHAPE_OF: dict[str, str]`, `PRIORITY: dict[str, int]`, `INTEGRITY_TOL_S: float = 0.001`
  - `char_shapes(phonemes: str) -> list[str]`
  - `phoneme_spans(phonemes: str, pred_dur: list[int], start_s: float, vocab: dict | None = None) -> list[tuple[float, float, str]]` (raises `ValueError` on a length mismatch)
  - `frame_shapes(spans, n_frames: int, fps: int) -> str`
  - `compute_shapes(timing: list[dict], synth, n_frames: int, fps: int, vocab: dict | None = None) -> tuple[str, list[int]]` where `synth(text) -> list[tuple[str, list[int]]]` (one `(phonemes, pred_dur)` per Kokoro chunk)

- [ ] **Step 1: Write the failing tests**

`tests/test_avatar_visemes.py`:
```python
import pytest

import avatar_visemes as av


def test_char_shapes_table():
    assert av.char_shapes("mbpfvuʊwOQɔɒiɪta ,") == list("MMMFFUUUUUUUEE....")


def test_char_shapes_length_and_stress_inheritance():
    # "two" = tˈuː : stress takes the next char (u -> U), length mark takes the previous (U)
    assert av.char_shapes("tˈuː") == [".", "U", "U", "U"]
    # stress before a consonant with no shape stays "."
    assert av.char_shapes("ˈtɑ") == [".", ".", "."]


def test_phoneme_spans_timing():
    # leading boundary 2 units, then f(3) I(4) v(2), trailing boundary 1
    spans = av.phoneme_spans("fIv", [2, 3, 4, 2, 1], start_s=1.0)
    assert spans == [(pytest.approx(1.05), pytest.approx(1.125), "F"),
                     (pytest.approx(1.225), pytest.approx(1.275), "F")]


def test_phoneme_spans_skips_chars_not_in_vocab():
    vocab = {"f": 1, "I": 2, "v": 3}          # "#" isn't in Kokoro's vocab, so it got no duration
    spans = av.phoneme_spans("f#Iv", [2, 3, 4, 2, 1], start_s=0.0, vocab=vocab)
    assert [s[2] for s in spans] == ["F", "F"]
    assert spans[1][0] == pytest.approx(0.225)


def test_phoneme_spans_length_mismatch_raises():
    with pytest.raises(ValueError, match="pred_dur"):
        av.phoneme_spans("fIv", [2, 3, 4, 1], start_s=0.0)


def test_frame_shapes_sub_frame_closure_still_shows():
    # a 25 ms "b" inside frame 1 (0.04-0.08 s at 25 fps)
    assert av.frame_shapes([(0.045, 0.07, "M")], 4, 25) == ".M.."


def test_frame_shapes_span_ending_on_boundary_does_not_spill():
    assert av.frame_shapes([(0.04, 0.08, "U")], 4, 25) == ".U.."


def test_frame_shapes_priority():
    spans = [(0.0, 0.08, "E"), (0.05, 0.06, "M"), (0.0, 0.04, "U")]
    assert av.frame_shapes(spans, 3, 25) == "UM."


def _synth_from(table):
    return lambda text: table[text]


def test_compute_shapes_places_sentences_at_their_offsets():
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1},
              {"text": "b", "offset_s": 0.1, "duration_s": 0.1}]
    synth = _synth_from({"a": [("ta", [1, 1, 1, 1])], "b": [("mɑ", [1, 1, 1, 1])]})
    shape, fallback = av.compute_shapes(timing, synth, 5, 25)
    # "m" in sentence b spans 0.125-0.15 s -> frame 3
    assert shape == "...M." and fallback == []


def test_compute_shapes_integrity_mismatch_falls_back():
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1},
              {"text": "b", "offset_s": 0.1, "duration_s": 0.2}]   # b's audio is longer than its phonemes say
    synth = _synth_from({"a": [("ma", [1, 1, 1, 1])], "b": [("mɑ", [1, 1, 1, 1])]})
    shape, fallback = av.compute_shapes(timing, synth, 8, 25)
    assert fallback == [1]
    assert "M" in shape[:2] and "M" not in shape[2:]


def test_compute_shapes_multi_chunk_sentence():
    timing = [{"text": "long", "offset_s": 0.0, "duration_s": 0.2}]
    synth = _synth_from({"long": [("ta", [1, 1, 1, 1]), ("tm", [1, 1, 1, 1])]})
    shape, fallback = av.compute_shapes(timing, synth, 5, 25)
    # second chunk starts at 0.1 s; its "m" is at 0.15-0.175 s -> frames 3 (0.12-0.16) and 4 (0.16-0.20)
    assert shape == "...MM" and fallback == []


def test_compute_shapes_unpairable_result_falls_back():
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1}]
    synth = _synth_from({"a": [("mab", [1, 1, 1, 1])]})          # 3 chars but only 2 inner durations
    shape, fallback = av.compute_shapes(timing, synth, 3, 25)
    assert fallback == [0] and shape == "..."
```

- [ ] **Step 2: Run to verify failure**

Run: `python -m pytest tests/test_avatar_visemes.py -q`
Expected: collection error, `ModuleNotFoundError: No module named 'avatar_visemes'`.

- [ ] **Step 3: Implement**

`scripts/avatar_visemes.py`:
```python
"""Mouth shapes (visemes) for the avatar from Kokoro's own phoneme timings.

See docs/superpowers/specs/2026-10-02-avatar-shaped-mouths-design.md.
Kokoro predicts one duration per phoneme character (pred_dur, in 25 ms
units, with a boundary entry at each end); that's deterministic, so
re-running a sentence's text from timing.json recovers exactly when each
sound happens in the existing audio - checked per sentence against its
real duration. Loudness (build_avatar_track.py) still decides how open
the mouth is; these shapes override it for m/b/p, f/v, oo/w/o and ee.
"""

import math

UNIT_S = 0.025  # one pred_dur unit = 600 samples at 24 kHz
INTEGRITY_TOL_S = 0.001

SHAPE_OF = {
    **dict.fromkeys("mbp", "M"),        # lips closed
    **dict.fromkeys("fv", "F"),         # lower lip on upper teeth
    **dict.fromkeys("uʊwOQɔɒ", "U"),    # pursed / rounded
    **dict.fromkeys("iɪ", "E"),         # wide
}
PRIORITY = {"M": 4, "F": 3, "U": 2, "E": 1, ".": 0}
LENGTH_MARK = "ː"
STRESS_MARKS = "ˈˌ"


def char_shapes(phonemes):
    out = [SHAPE_OF.get(c, ".") for c in phonemes]
    for i, c in enumerate(phonemes):
        if c == LENGTH_MARK and i > 0:
            out[i] = out[i - 1]
    for i in range(len(phonemes) - 1, -1, -1):
        if phonemes[i] in STRESS_MARKS and i + 1 < len(phonemes):
            out[i] = out[i + 1]
    return out


def phoneme_spans(phonemes, pred_dur, start_s, vocab=None):
    """[(t0, t1, shape)] for one Kokoro chunk, shape '.' spans omitted.
    pred_dur = [leading boundary, one per kept char..., trailing boundary];
    vocab (the model's) drops the chars Kokoro dropped before running."""
    chars = [c for c in phonemes if vocab is None or vocab.get(c)]
    if len(pred_dur) != len(chars) + 2:
        raise ValueError(f"pred_dur has {len(pred_dur)} entries for {len(chars)} phoneme chars "
                         f"(expected chars + 2)")
    shapes = char_shapes("".join(chars))
    t = start_s + pred_dur[0] * UNIT_S
    spans = []
    for shape, d in zip(shapes, pred_dur[1:-1]):
        t1 = t + d * UNIT_S
        if shape != ".":
            spans.append((t, t1, shape))
        t = t1
    return spans


def frame_shapes(spans, n_frames, fps):
    """One char per frame: the highest-priority shape overlapping the
    frame's [i/fps, (i+1)/fps) window, so a sub-frame 'b' still shows."""
    out = ["."] * n_frames
    for t0, t1, shape in spans:
        f0 = max(0, math.floor(t0 * fps + 1e-9))
        f1 = min(n_frames - 1, math.ceil(t1 * fps - 1e-9) - 1)
        for f in range(f0, f1 + 1):
            if PRIORITY[shape] > PRIORITY[out[f]]:
                out[f] = shape
    return "".join(out)


def compute_shapes(timing, synth, n_frames, fps, vocab=None):
    """(shape string, fallen-back sentence indices). timing is timing.json's
    list of {text, offset_s, duration_s}; synth(text) returns one
    (phonemes, pred_dur) per Kokoro chunk. A sentence whose durations
    don't add up to its real length, or don't pair with its phonemes,
    gets no shapes (the mouth falls back to loudness there)."""
    spans, fallback = [], []
    for idx, sent in enumerate(timing):
        results = synth(sent["text"])
        units = sum(sum(d) for _, d in results)
        if abs(units * UNIT_S - sent["duration_s"]) > INTEGRITY_TOL_S:
            fallback.append(idx)
            continue
        t, sent_spans = sent["offset_s"], []
        try:
            for phonemes, d in results:
                sent_spans += phoneme_spans(phonemes, d, t, vocab)
                t += sum(d) * UNIT_S
        except ValueError:
            fallback.append(idx)
            continue
        spans += sent_spans
    return frame_shapes(spans, n_frames, fps), fallback
```

- [ ] **Step 4: Run to verify pass**

Run: `python -m pytest tests/test_avatar_visemes.py -q`
Expected: all PASS.

- [ ] **Step 5: Lint and commit**

```bash
ruff check .
git add scripts/avatar_visemes.py tests/test_avatar_visemes.py
git commit -m "Avatar shapes: phoneme->shape mapping, spans, per-frame shapes, integrity check + tests"
```

---

### Task 2: Kokoro durations-only adapter + slow test

**Files:**
- Modify: `scripts/avatar_visemes.py` (append)
- Modify: `pyproject.toml`
- Test: `tests/test_avatar_visemes_kokoro.py`

**Interfaces:**
- Consumes: `generate_narration._build_pipeline(lang_code)`, `generate_narration._lang_code_for(voice)` (both exist, `scripts/generate_narration.py:2068,2087`); Task 1's `compute_shapes`, `UNIT_S`.
- Produces: `kokoro_synth(voice: str = "bm_george") -> tuple[synth, dict]` — `synth(text) -> list[tuple[str, list[int]]]`, plus the model's `vocab`.

- [ ] **Step 1: Register the marker**

Append to `pyproject.toml`:
```toml

[tool.pytest.ini_options]
# The slow tests load the Kokoro model (~20 s). Skipped by default;
# run them with: python -m pytest tests -m slow
markers = ["slow: loads the Kokoro TTS model (~20 s)"]
addopts = "-m 'not slow'"
```
Run: `python -m pytest tests -q` — Expected: same pass count as before, no errors.

- [ ] **Step 2: Write the failing slow test**

`tests/test_avatar_visemes_kokoro.py`:
```python
import pytest

import avatar_visemes as av

SENT = "Five hundred and two of them moved over to Singapore, where Leeson kept his books."


@pytest.mark.slow
def test_kokoro_shapes_land_on_the_right_words():
    synth, vocab = av.kokoro_synth("bm_george")
    results = synth(SENT)
    duration = sum(sum(d) for _, d in results) * av.UNIT_S
    n = int(duration * 25)
    shape, fallback = av.compute_shapes([{"text": SENT, "offset_s": 0.0, "duration_s": duration}],
                                        synth, n, 25, vocab)
    assert fallback == []
    # word timings from the 2026-10-02 probe: Five 0.25-0.55 s, two 1.31-1.51 s, moved 1.93-2.28 s
    assert "F" in shape[6:8]        # the f of "five"
    assert "F" in shape[11:14]      # the v at the end of "five"
    assert "U" in shape[33:38]      # the oo of "two"
    assert shape[48] == "M"         # the m of "moved"
```

- [ ] **Step 3: Run to verify failure**

Run: `python -m pytest tests/test_avatar_visemes_kokoro.py -m slow -q`
Expected: FAIL with `AttributeError: module 'avatar_visemes' has no attribute 'kokoro_synth'`.

- [ ] **Step 4: Implement**

Append to `scripts/avatar_visemes.py`:
```python


def kokoro_synth(voice="bm_george"):
    """(synth, vocab) for compute_shapes. Loads Kokoro once through
    generate_narration's own pipeline builder (same pronunciation
    overrides), then swaps *this pipeline's* model.forward_with_tokens
    for a durations-only copy of Kokoro 0.9.4's: the same steps up to
    pred_dur, minus the audio decoder. Identical pred_dur, a fraction of
    the time (Barings' 68 sentences: ~8 s). Returns silent audio of the
    right length so the pipeline's own bookkeeping is unchanged."""
    import sys
    from pathlib import Path

    import torch

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import generate_narration as gn

    pipeline = gn._build_pipeline(gn._lang_code_for(voice))
    model = pipeline.model

    def durations_only(input_ids, ref_s, speed=1):
        input_lengths = torch.full((input_ids.shape[0],), input_ids.shape[-1],
                                   device=input_ids.device, dtype=torch.long)
        text_mask = torch.arange(input_lengths.max()).unsqueeze(0).expand(
            input_lengths.shape[0], -1).type_as(input_lengths)
        text_mask = torch.gt(text_mask + 1, input_lengths.unsqueeze(1)).to(model.device)
        bert_dur = model.bert(input_ids, attention_mask=(~text_mask).int())
        d_en = model.bert_encoder(bert_dur).transpose(-1, -2)
        d = model.predictor.text_encoder(d_en, ref_s[:, 128:], input_lengths, text_mask)
        x, _ = model.predictor.lstm(d)
        duration = torch.sigmoid(model.predictor.duration_proj(x)).sum(axis=-1) / speed
        pred_dur = torch.round(duration).clamp(min=1).long().squeeze()
        return torch.zeros(int(pred_dur.sum()) * 600), pred_dur

    model.forward_with_tokens = durations_only

    def synth(text):
        with torch.inference_mode():
            return [(r.phonemes, [int(v) for v in r.pred_dur.reshape(-1).tolist()])
                    for r in pipeline(text, voice=voice, split_pattern=None)
                    if r.pred_dur is not None]

    return synth, model.vocab
```

- [ ] **Step 5: Run to verify pass**

Run: `PYTHONIOENCODING=utf-8 python -m pytest tests/test_avatar_visemes_kokoro.py -m slow -q`
Expected: PASS (~20 s). If a frame-index assertion is off by one frame against real output, print `shape[0:60]` and the word timings (`r.tokens` start/end, as in `scratch/viseme-probe/probe.py`), then fix whichever is wrong — the expectation or the code — and ledger the ruling.

Then: `python -m pytest tests -q` — Expected: all fast tests pass, the slow test deselected.

- [ ] **Step 6: Lint and commit**

```bash
ruff check .
git add scripts/avatar_visemes.py pyproject.toml tests/test_avatar_visemes_kokoro.py
git commit -m "Avatar shapes: Kokoro durations-only adapter + slow real-model test"
```

---

### Task 3: Mouth file version 2 (step 1.5)

**Files:**
- Modify: `scripts/avatar_lib.py` (`MOUTH_FILE_VERSION` area and `load_mouth_file`)
- Modify: `scripts/build_avatar_track.py` (`build_track`, `main`)
- Test: `tests/test_avatar_lib.py`, `tests/test_build_avatar_track.py` (append)

**Interfaces:**
- Consumes: Task 1 `compute_shapes`; Task 2 `kokoro_synth`.
- Produces:
  - `avatar_lib.MOUTH_FILE_VERSIONS = (1, 2)` (replaces the `MOUTH_FILE_VERSION` check in `load_mouth_file`; `MOUTH_FILE_VERSION = 1` stays as the loudness-only version)
  - `build_track(samples, sr, fps, duration_s, slug, source, shapes: tuple[str, list[int]] | None = None) -> dict` — version 2 with `shape`, `shape_fallback` when `shapes` given
  - CLI: `build_avatar_track.py audio/<slug>.mp3 [--fps 25] [--out PATH] [--no-shapes] [--voice bm_george]`

- [ ] **Step 1: Write the failing tests**

Append to `tests/test_avatar_lib.py`:
```python


def test_load_mouth_file_accepts_v2_with_shape(tmp_path):
    p = _write_track(tmp_path / "x.avatar.json", version=2, shape="." * 250, shape_fallback=[])
    assert al.load_mouth_file(p, 25, 10.0)["shape"] == "." * 250


def test_load_mouth_file_rejects_short_shape(tmp_path):
    p = _write_track(tmp_path / "x.avatar.json", version=2, shape="." * 249, shape_fallback=[])
    with pytest.raises(ValueError, match="shape"):
        al.load_mouth_file(p, 25, 10.0)


def test_load_mouth_file_rejects_unknown_version(tmp_path):
    p = _write_track(tmp_path / "x.avatar.json", version=3)
    with pytest.raises(ValueError, match="version"):
        al.load_mouth_file(p, 25, 10.0)
```
Append to `tests/test_build_avatar_track.py`:
```python


def test_build_track_with_shapes_is_v2():
    samples = np.concatenate([np.zeros(SR, np.float32), tone(1.0, 0.4)])
    shape = "." * 25 + "M" * 25
    track = bat.build_track(samples, SR, 25, 2.0, "slug", "audio/slug.mp3", shapes=(shape, [3]))
    assert track["version"] == 2
    assert track["shape"] == shape and track["shape_fallback"] == [3]


def test_build_track_without_shapes_stays_v1():
    track = bat.build_track(np.zeros(SR, np.float32), SR, 25, 1.0, "s", "audio/s.mp3")
    assert track["version"] == 1 and "shape" not in track


def test_cli_no_shapes_writes_v1(tmp_path):
    mp3 = tmp_path / "clip.mp3"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "sine=frequency=220:sample_rate=16000:d=1",
                    str(mp3)], check=True)
    subprocess.run(["python", "scripts/build_avatar_track.py", str(mp3), "--no-shapes"], check=True)
    import json
    assert json.loads((tmp_path / "clip.avatar.json").read_text(encoding="utf-8"))["version"] == 1


def test_cli_shapes_without_timing_json_errors(tmp_path):
    mp3 = tmp_path / "clip.mp3"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "sine=frequency=220:sample_rate=16000:d=1",
                    str(mp3)], check=True)
    r = subprocess.run(["python", "scripts/build_avatar_track.py", str(mp3)], capture_output=True, text=True)
    assert r.returncode != 0 and "timing.json" in r.stderr and "--no-shapes" in r.stderr
```
Also update the existing `test_cli_end_to_end` in the same file to pass `--no-shapes` (its synthetic mp3 has no `timing.json`): change `["python", "scripts/build_avatar_track.py", str(mp3)]` to `["python", "scripts/build_avatar_track.py", str(mp3), "--no-shapes"]`.

- [ ] **Step 2: Run to verify failure**

Run: `python -m pytest tests/test_avatar_lib.py tests/test_build_avatar_track.py -q`
Expected: the new tests FAIL (`version 2 != 1`, `unexpected keyword argument 'shapes'`, unrecognized `--no-shapes`).

- [ ] **Step 3: Implement `avatar_lib`**

In `scripts/avatar_lib.py`, after `MOUTH_FILE_VERSION = 1` add:
```python
# 1 = loudness only; 2 adds a per-frame "shape" string (M F U E or .) from
# avatar_visemes.py. The renderer reads both.
MOUTH_FILE_VERSIONS = (1, 2)
```
In `load_mouth_file`, replace the version check:
```python
    if data.get("version") != MOUTH_FILE_VERSION:
        raise ValueError(f"{path}: version {data.get('version')} != {MOUTH_FILE_VERSION} - {rerun}")
```
with:
```python
    if data.get("version") not in MOUTH_FILE_VERSIONS:
        raise ValueError(f"{path}: version {data.get('version')} not one of {MOUTH_FILE_VERSIONS} - {rerun}")
```
and after the `len(data["mouth"])` check add:
```python
    if "shape" in data and len(data["shape"]) != data["frames"]:
        raise ValueError(f"{path}: shape has {len(data['shape'])} entries but frames={data['frames']} - {rerun}")
```

- [ ] **Step 4: Implement `build_avatar_track`**

Replace `build_track` with:
```python
def build_track(samples, sr, fps, duration_s, slug, source, shapes=None):
    """shapes: (shape string, fallen-back sentence indices) from
    avatar_visemes.compute_shapes, or None for a loudness-only (v1) file."""
    n_frames = int(duration_s * fps)  # same count watch_video_lib.render() uses
    levels = debounce(quantise(normalise(frame_rms(samples, sr, fps, n_frames))))
    track = {
        "version": MOUTH_FILE_VERSION,
        "fps": fps,
        "frames": n_frames,
        "duration_s": round(duration_s, 3),
        "source": source,
        "mouth": "".join(str(v) for v in levels),
        "blinks": blink_schedule(slug, n_frames, fps),
    }
    if shapes is not None:
        shape, fallback = shapes
        track.update(version=2, shape=shape, shape_fallback=fallback)
    return track
```
In `main()`, add the arguments after `--out`:
```python
    ap.add_argument("--no-shapes", action="store_true",
                    help="loudness only (version 1 file); skips loading Kokoro")
    ap.add_argument("--voice", default="bm_george", help="the narration's Kokoro voice (default bm_george)")
```
and replace the `track = build_track(...)` line with:
```python
    duration = probe_duration(mp3)
    shapes = None
    if not args.no_shapes:
        timing_path = mp3.with_suffix(".timing.json")
        if not timing_path.exists():
            sys.exit(f"error: no {timing_path} next to the mp3 - mouth shapes need the narration's "
                     f"timing.json (written by generate_narration.py); pass --no-shapes for loudness only")
        from avatar_visemes import compute_shapes, kokoro_synth
        timing = json.loads(timing_path.read_text(encoding="utf-8"))
        print(f"Loading Kokoro for mouth shapes ({len(timing)} sentences) ...", file=sys.stderr)
        synth, vocab = kokoro_synth(args.voice)
        shapes = compute_shapes(timing, synth, int(duration * args.fps), args.fps, vocab)
        for i in shapes[1]:
            print(f"  sentence {i} fell back to loudness-only (its length no longer matches its "
                  f"phonemes): {timing[i]['text'][:60]!r}", file=sys.stderr)
    track = build_track(decode_mono(mp3), SAMPLE_RATE, args.fps, duration,
                        mp3.stem, mp3.as_posix(), shapes)
```
and after the existing summary `print(...)`, add:
```python
    if "shape" in track:
        sc = Counter(track["shape"])
        shape_spread = "  ".join(f"{k}:{100 * sc.get(k, 0) / total:.0f}%" for k in "MFUE")
        print(f"  mouth shapes {shape_spread}; {len(track['shape_fallback'])} sentence(s) fell back")
```
(Add `"Shapes: ..."` to the module docstring: one line saying shapes are on by default, cost one Kokoro load, `--no-shapes` to skip.)

- [ ] **Step 5: Run to verify pass**

Run: `python -m pytest tests -q`
Expected: all PASS.

- [ ] **Step 6: Lint and commit**

```bash
ruff check .
git add scripts/avatar_lib.py scripts/build_avatar_track.py tests/test_avatar_lib.py tests/test_build_avatar_track.py
git commit -m "Avatar shapes: mouth file v2 (shape + shape_fallback), --no-shapes/--voice + tests"
```

---

### Task 4: Four mouth layers and the renderer

**Files:**
- Modify: `assets/avatar/avatar.svg` (add four groups after `mouth-3`)
- Regenerate: `assets/avatar/png/`
- Modify: `scripts/avatar_lib.py` (`LAYER_NAMES`)
- Modify: `scripts/render_avatar_track.py` (`compose_avatar`, new `mouth_layer_for`, render loop)
- Test: `tests/test_render_avatar_track.py` (fixture + append)

**Interfaces:**
- Consumes: Task 3's v2 mouth file (`shape` key, optional).
- Produces:
  - `LAYER_NAMES` = the 7 existing + `["mouth-M", "mouth-F", "mouth-U", "mouth-E"]`
  - `mouth_layer_for(level: int, shape: str) -> str`
  - `compose_avatar(layers, mouth: int | str, eyes_closed: bool)` — `mouth` is a level (→ `mouth-<level>`) or a layer name

- [ ] **Step 1: Write the failing tests**

In `tests/test_render_avatar_track.py`, replace the `solid_layers` fixture's `colours` dict so it covers every layer name (new mouths transparent except where a test needs them):
```python
def solid_layers(tmp_path, d=64):
    colours = {name: (0, 0, 0, 0) for name in al.LAYER_NAMES}
    colours.update({"body": (0, 0, 255, 255), "mouth-3": (255, 0, 0, 255), "mouth-F": (0, 255, 0, 255)})
    for name, c in colours.items():
        im = Image.new("RGBA", (d, d), (0, 0, 0, 0))
        if c[3]:
            box = (0, 0, d, d) if name == "body" else (d // 4, d // 2, 3 * d // 4, 3 * d // 4)
            im.paste(c, box)
        im.save(tmp_path / f"{name}.png")
    return tmp_path
```
Append:
```python


def test_mouth_layer_for():
    assert rat.mouth_layer_for(0, "F") == "mouth-0"       # silence always closes
    assert rat.mouth_layer_for(2, "F") == "mouth-F"
    assert rat.mouth_layer_for(2, ".") == "mouth-2"
    assert rat.mouth_layer_for(3, "M") == "mouth-M"


def test_compose_accepts_layer_name(tmp_path):
    layers = rat.load_layers(32, solid_layers(tmp_path))
    assert rat.compose_avatar(layers, "mouth-F", False).getpixel((16, 20)) == (0, 255, 0, 255)


def _track_cfg(tmp_path, **track_over):
    timing = tmp_path / "t.timing.json"
    track = {"version": 1, "fps": 25, "frames": 50, "duration_s": 2.0, "source": "x",
             "mouth": "3" * 50, "blinks": []}
    track.update(track_over)
    (tmp_path / "t.avatar.json").write_text(json.dumps(track), encoding="utf-8")
    return types.SimpleNamespace(TOTAL_DURATION=2.0, TIMING_JSON=str(timing), WIDTH=320, HEIGHT=180,
                                 AVATAR={"ranges": [(0, None)], "size": 0.4, "margin": 0.05, "fade": 0.0})


def _frame_rgb(path, n, tmp_path):
    f = tmp_path / f"f{n}.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-vf", f"select=eq(n\\,{n})",
                    "-frames:v", "1", str(f)], check=True)
    return Image.open(f).convert("RGBA").getpixel((36, 45))      # inside the mouth box at 72 px


def test_render_v2_track_uses_shapes(tmp_path):
    png = tmp_path / "png"
    png.mkdir()
    solid_layers(png)
    cfg = _track_cfg(tmp_path, version=2, shape="F" * 25 + "." * 25, shape_fallback=[])
    out = tmp_path / "a.mov"
    rat.render_track(cfg, out, png)
    assert _frame_rgb(out, 10, tmp_path)[:3] == (0, 255, 0)      # shape F wins over level 3
    assert _frame_rgb(out, 40, tmp_path)[:3] == (255, 0, 0)      # no shape -> level 3


def test_render_v1_track_uses_levels_only(tmp_path):
    png = tmp_path / "png"
    png.mkdir()
    solid_layers(png)
    out = tmp_path / "a.mov"
    rat.render_track(_track_cfg(tmp_path), out, png)
    assert _frame_rgb(out, 10, tmp_path)[:3] == (255, 0, 0)
```

- [ ] **Step 2: Run to verify failure**

Run: `python -m pytest tests/test_render_avatar_track.py -q`
Expected: FAIL — `AttributeError: ... 'mouth_layer_for'` and `KeyError: 'mouth-F'` (the fixture writes `mouth-F.png` but `LAYER_NAMES` doesn't load it yet).

- [ ] **Step 3: Add the SVG layers**

In `assets/avatar/avatar.svg`, directly after the `</g>` that closes `<g id="mouth-3">`, add:
```xml
  <!-- shaped mouths (visemes), same centre: M closed lips m/b/p, F lip on
       teeth f/v, U pursed oo/w/o, E wide ee -->
  <g id="mouth-M">
    <path d="M222 338 Q256 330 290 338 Q256 348 222 338 Z" fill="#b5675a"/>
    <path d="M224 338 Q256 341 288 338" fill="none" stroke="#7d3f35" stroke-width="3" stroke-linecap="round"/>
  </g>
  <g id="mouth-F">
    <path d="M226 330 Q256 326 286 330 Q282 346 256 346 Q230 346 226 330 Z" fill="#5a1e1e"/>
    <path d="M228 330 Q256 327 284 330 L283 340 Q256 337 229 340 Z" fill="#f4f1ea"/>
    <path d="M226 341 Q256 353 286 341 Q256 347 226 341 Z" fill="#b5675a"/>
  </g>
  <g id="mouth-U">
    <ellipse cx="256" cy="340" rx="14" ry="13" fill="#5a1e1e" stroke="#b5675a" stroke-width="7"/>
  </g>
  <g id="mouth-E">
    <path d="M214 332 Q256 328 298 332 Q290 350 256 350 Q222 350 214 332 Z" fill="#5a1e1e" stroke="#9a5546" stroke-width="4" stroke-linejoin="round"/>
    <path d="M218 333 Q256 329 294 333 L292 340 Q256 337 220 340 Z" fill="#f4f1ea"/>
  </g>
```
Update the SVG's header comment layer list to `mouth-0..mouth-3, mouth-M, mouth-F, mouth-U, mouth-E`.

- [ ] **Step 4: Extend `LAYER_NAMES` and the renderer**

`scripts/avatar_lib.py`:
```python
LAYER_NAMES = ["body", "eyes-open", "eyes-closed", "mouth-0", "mouth-1", "mouth-2", "mouth-3",
               "mouth-M", "mouth-F", "mouth-U", "mouth-E"]
```
`scripts/render_avatar_track.py` — replace `compose_avatar` with:
```python
def mouth_layer_for(level, shape):
    """Silence always closes the mouth; otherwise a shaped mouth (M F U E)
    beats the loudness level; otherwise the level picks the opening."""
    if level == 0:
        return "mouth-0"
    if shape in ("M", "F", "U", "E"):
        return f"mouth-{shape}"
    return f"mouth-{level}"


def compose_avatar(layers, mouth, eyes_closed):
    """mouth: a loudness level (0-3) or a layer name such as 'mouth-F'."""
    img = layers["body"].copy()
    img.alpha_composite(layers["eyes-closed" if eyes_closed else "eyes-open"])
    img.alpha_composite(layers[mouth if isinstance(mouth, str) else f"mouth-{mouth}"])
    return img
```
In `render_track`, after `mouth = track["mouth"]` add `shape = track.get("shape")`, and replace
```python
            key = (int(mouth[min(i, len(mouth) - 1)]), i in blinking)
```
with
```python
            j = min(i, len(mouth) - 1)
            key = (mouth_layer_for(int(mouth[j]), shape[j] if shape else "."), i in blinking)
```

- [ ] **Step 5: Rebuild PNGs and run tests**

```bash
python scripts/build_avatar.py
python -m pytest tests -q
```
Expected: 11 `Wrote ...png` lines; all tests PASS (`test_build_layers` now checks 11 stems).

- [ ] **Step 6: Lint and commit**

```bash
ruff check .
git add assets/avatar/avatar.svg assets/avatar/png scripts/avatar_lib.py scripts/render_avatar_track.py tests/test_render_avatar_track.py
git commit -m "Avatar shapes: four mouth layers (M F U E) + renderer picks shape over level + tests"
```

---

### Task 5: Barings check, preview, Chris's approval

**Files:**
- Create (uncommitted): `scratch/shapes-test/` (mouth files, tracks, preview)
- Possibly modify: `assets/avatar/avatar.svg` + `assets/avatar/png/` (drawing tweaks from Chris)

**Interfaces:**
- Consumes: everything above; the Phase 1 test config `scratch/avatar-test/barings-avatar.py` (exists; `AVATAR` bookends).

- [ ] **Step 1: Build both mouth files for Barings**

```bash
S=barings-1995-the-singapore-trading-desk-that-broke-a-233-year-old-bank
mkdir -p scratch/shapes-test
time python scripts/build_avatar_track.py audio/$S.mp3 --out scratch/shapes-test/shapes.avatar.json
python scripts/build_avatar_track.py audio/$S.mp3 --no-shapes --out scratch/shapes-test/levels.avatar.json
```
Expected: shapes run ~20 s; `0 sentence(s) fell back` (the probe found all 68 match); shape spread roughly 5–15% each for M F U E. Record both in the ledger.

- [ ] **Step 2: Render a 16 s preview, shapes beside loudness-only**

The renderer reads the mouth file named after the config's `TIMING_JSON`, so render each through a tiny scratch config pointing `TIMING_JSON` at a copy:
```bash
for v in shapes levels; do
  cp scratch/shapes-test/$v.avatar.json scratch/shapes-test/$v-x.avatar.json
  cat > scratch/shapes-test/$v.py <<EOF
TOTAL_DURATION = 650.975
TIMING_JSON = "scratch/shapes-test/$v-x.timing.json"
AVATAR = {"ranges": [(0, 20)], "size": 0.4, "fade": 0.3}
EOF
  python scripts/render_avatar_track.py --config scratch/shapes-test/$v.py --out scratch/shapes-test/$v.mov
done
ffmpeg -y -v error -f lavfi -i color=c=0x808080:s=720x400:r=25 \
  -i scratch/shapes-test/levels.mov -i scratch/shapes-test/shapes.mov -i audio/$S.mp3 \
  -filter_complex "[0:v][1:v]overlay=40:56:format=auto[a];[a][2:v]overlay=392:56:format=auto,format=yuv420p[v]" \
  -map "[v]" -map 3:a -t 16 -c:v libx264 -crf 20 -c:a aac -movflags +faststart scratch/shapes-test/compare.mp4
```
(`mouth_path_for_config` maps `scratch/shapes-test/<v>-x.timing.json` → `<v>-x.avatar.json`.) Left = loudness only, right = shaped. Pull frames at 0.4 s and 1.4 s with the Read tool and confirm the right bubble shows F/U where expected.

- [ ] **Step 3: Artifact page for Chris**

Load the `artifact-design` skill. Build a sheet PNG of the four new mouths (each composed on `body` + `eyes-open`, labelled with its sounds and an example word: M "bank", F "five", U "two", E "see") and publish one page with the sheet and `compare.mp4` (via `files`). Ask: do the drawings read as those sounds; does the right-hand bubble look better than the left; anything twitchy?

- [ ] **Step 4: Apply feedback and commit any art changes**

If Chris asks for drawing tweaks, edit the four groups in `assets/avatar/avatar.svg`, re-run `python scripts/build_avatar.py`, rebuild the sheet and republish the same artifact path. Then:
```bash
python -m pytest tests -q && ruff check .
git add assets/avatar/avatar.svg assets/avatar/png
git commit -m "Avatar shapes: mouth drawings tuned after Chris's review"
```
(Skip the commit if nothing changed.)

---

### Task 6: Docs

**Files:**
- Modify: `docs/production-pipeline.md` (§1.5)
- Modify: `docs/superpowers/specs/2026-10-02-avatar-presenter-design.md` (phasing table)

- [ ] **Step 1: Update pipeline §1.5**

In the `### 1.5 Build the avatar mouth track (optional)` section, after the paragraph ending "Commit the `.avatar.json` with the audio in section 12.", add:
```markdown
**Mouth shapes (on by default):** besides how open the mouth is, the
script now picks shaped mouths for the sounds viewers notice - closed
lips on m/b/p, lip on teeth on f/v, pursed on oo/w/o, wide on ee - from
Kokoro's own per-sound timings (`scripts/avatar_visemes.py`). It reads
`audio/<slug>.timing.json`, loads Kokoro once and runs only its duration
step (no audio is made; ~20 s for a 10-minute narration). Each sentence
is checked against its real length in the audio; one that no longer
matches (an override changed after that sentence was cached) **falls
back** to loudness-only and is listed - harmless, but re-running step
1.2 with `--no-cache` and then this step clears it. `--no-shapes` skips
all of this (loudness only, no Kokoro). If the narration voice isn't
`bm_george`, pass `--voice <name>`.
```
And replace the Barings reference spread line with the one measured in Task 5 Step 1, adding the shape spread.

- [ ] **Step 2: Note it in the Phase 1 spec**

In `docs/superpowers/specs/2026-10-02-avatar-presenter-design.md`, in the phasing table row "Later, separate projects", change "phoneme-shaped mouths;" to "phoneme-shaped mouths (**done 2026-10-02**, `docs/superpowers/specs/2026-10-02-avatar-shaped-mouths-design.md`);".

- [ ] **Step 3: Commit**

```bash
python -m pytest tests -q && ruff check .
git add docs/production-pipeline.md docs/superpowers/specs/2026-10-02-avatar-presenter-design.md
git commit -m "Docs: avatar mouth shapes in pipeline step 1.5"
```
