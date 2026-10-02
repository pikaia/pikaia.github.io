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
