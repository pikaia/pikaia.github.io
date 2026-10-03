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
# Show each shape one frame before its sound: lips close before an "m" is
# heard. Measured 2026-10-02 against synthesized audio, raw-duration sound
# times sit 0-50 ms after the real onset of a voiced sound (Kokoro's own
# word timestamps shift a further 75 ms earlier, too early), so 40 ms lead
# lands within ~10 ms of the onset.
SHAPE_LEAD_S = 0.04

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


def compute_shapes(timing, synth, n_frames, fps, vocab=None, lead_s=SHAPE_LEAD_S, provenance=None):
    """(shape string, fallen-back sentence indices). timing is timing.json's
    list of {text, offset_s, duration_s}; synth(text) returns one
    (phonemes, pred_dur) per Kokoro chunk. A sentence whose durations
    don't add up to its real length, or don't pair with its phonemes,
    gets no shapes (the mouth falls back to loudness there). Every shape
    shows lead_s early (see SHAPE_LEAD_S).

    provenance(text, duration_s) -> True / False / None, if given, must
    return True for a sentence to get shapes: the length check alone can't
    see an override change that moves sounds around but keeps the total
    length (see cache_provenance)."""
    spans, fallback = [], []
    for idx, sent in enumerate(timing):
        if provenance is not None and provenance(sent["text"], sent["duration_s"]) is not True:
            fallback.append(idx)
            continue
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
    # Shift earlier by lead_s; a shape in the first lead_s of the audio
    # starts at 0 but keeps its full length rather than vanishing.
    spans = [(max(0.0, t0 - lead_s), max(0.0, t0 - lead_s) + (t1 - t0), shape) for t0, t1, shape in spans]
    return frame_shapes(spans, n_frames, fps), fallback


def cache_provenance(voice="bm_george", cache_dir=None):
    """check(text, duration_s) for compute_shapes: was this sentence's audio
    made with today's pronunciation overrides? generate_narration's cache
    key covers the sentence, voice and every override whose word appears
    in it, so an entry under today's key with the right sample count means
    re-running Kokoro now reproduces that audio's timing. True = yes,
    False = cached audio has another length, None = no entry (an override
    changed since, or the cache was cleared) - both of the last two mean
    re-run step 1.2 before trusting shapes for that sentence."""
    import sys
    from pathlib import Path

    import numpy as np

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import generate_narration as gn

    cache_dir = Path(cache_dir) if cache_dir else Path(gn._CACHE_DIR)
    lang_code = gn._lang_code_for(voice)

    def check(text, duration_s):
        path = cache_dir / f"{gn._sentence_cache_key(text, voice, lang_code)}.npy"
        if not path.exists():
            return None
        n = np.load(path, mmap_mode="r").shape[0]
        return abs(n / gn.SAMPLE_RATE - duration_s) <= INTEGRITY_TOL_S

    return check


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
