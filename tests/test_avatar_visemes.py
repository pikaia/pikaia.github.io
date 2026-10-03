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
    shape, fallback = av.compute_shapes(timing, synth, 5, 25, lead_s=0.0)
    # "m" in sentence b spans 0.125-0.15 s -> frame 3
    assert shape == "...M." and fallback == []


def test_compute_shapes_integrity_mismatch_falls_back():
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1},
              {"text": "b", "offset_s": 0.1, "duration_s": 0.2}]   # b's audio is longer than its phonemes say
    synth = _synth_from({"a": [("ma", [1, 1, 1, 1])], "b": [("mɑ", [1, 1, 1, 1])]})
    shape, fallback = av.compute_shapes(timing, synth, 8, 25, lead_s=0.0)
    assert fallback == [1]
    assert "M" in shape[:2] and "M" not in shape[2:]


def test_compute_shapes_multi_chunk_sentence():
    timing = [{"text": "long", "offset_s": 0.0, "duration_s": 0.2}]
    synth = _synth_from({"long": [("ta", [1, 1, 1, 1]), ("tm", [1, 1, 1, 1])]})
    shape, fallback = av.compute_shapes(timing, synth, 5, 25, lead_s=0.0)
    # second chunk starts at 0.1 s; its "m" is at 0.15-0.175 s -> frames 3 (0.12-0.16) and 4 (0.16-0.20)
    assert shape == "...MM" and fallback == []


def test_compute_shapes_unpairable_result_falls_back():
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1}]
    synth = _synth_from({"a": [("mab", [1, 1, 1, 1])]})          # 3 chars but only 2 inner durations
    shape, fallback = av.compute_shapes(timing, synth, 3, 25, lead_s=0.0)
    assert fallback == [0] and shape == "..."


def test_compute_shapes_leads_the_sound_by_one_frame():
    # Lips have to be shut before an "m" is heard, so shapes show 40 ms early
    # (measured 2026-10-02: raw-duration onsets sit 0-50 ms after the shape
    # would otherwise appear). "m" at 0.125-0.15 s -> shown 0.085-0.11 s -> frame 2.
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1},
              {"text": "b", "offset_s": 0.1, "duration_s": 0.1}]
    synth = _synth_from({"a": [("ta", [1, 1, 1, 1])], "b": [("mɑ", [1, 1, 1, 1])]})
    assert av.SHAPE_LEAD_S == 0.04
    assert av.compute_shapes(timing, synth, 5, 25)[0] == "..M.."


def test_compute_shapes_lead_clamps_at_zero():
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.075}]
    synth = _synth_from({"a": [("m", [0, 1, 2])]})              # "m" at 0.0-0.025 s
    assert av.compute_shapes(timing, synth, 2, 25)[0] == "M."


def test_compute_shapes_rejects_same_length_resynthesis_via_provenance():
    # A changed override can keep a sentence's total length while moving its
    # sounds around; the length check can't see that, the provenance check can.
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1},
              {"text": "b", "offset_s": 0.1, "duration_s": 0.1}]
    synth = _synth_from({"a": [("ma", [1, 1, 1, 1])], "b": [("mɑ", [1, 1, 1, 1])]})
    verdicts = {"a": True, "b": False}
    shape, fallback = av.compute_shapes(timing, synth, 8, 25, lead_s=0.0,
                                        provenance=lambda text, dur: verdicts[text])
    assert fallback == [1] and "M" not in shape[2:]


def test_compute_shapes_unknown_provenance_falls_back():
    timing = [{"text": "a", "offset_s": 0.0, "duration_s": 0.1}]
    synth = _synth_from({"a": [("ma", [1, 1, 1, 1])]})
    shape, fallback = av.compute_shapes(timing, synth, 3, 25, lead_s=0.0, provenance=lambda text, dur: None)
    assert fallback == [0] and shape == "..."


def test_cache_provenance(tmp_path):
    import numpy as np
    import generate_narration as gn
    check = av.cache_provenance("bm_george", cache_dir=tmp_path)
    key = gn._sentence_cache_key("Hello there.", "bm_george", gn._lang_code_for("bm_george"))
    assert check("Hello there.", 0.5) is None                      # never synthesized with today's overrides
    np.save(tmp_path / f"{key}.npy", np.zeros(12000, np.float32))  # 0.5 s at 24 kHz
    assert check("Hello there.", 0.5) is True
    assert check("Hello there.", 0.6) is False
