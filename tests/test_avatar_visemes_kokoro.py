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
    # Raw-duration sound times (which match the audio's real onsets, measured
    # 2026-10-02) minus the 40 ms lead: f of "five" ~0.285 s, its v ~0.51 s,
    # the oo of "two" ~1.44-1.54 s, the m of "moved" ~1.81-1.91 s.
    assert "F" in shape[6:9]        # the f of "five"
    assert "F" in shape[11:15]      # the v at the end of "five"
    assert "U" in shape[34:39]      # the oo of "two"
    assert "M" in shape[44:48]      # the m of "moved"
