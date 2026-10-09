"""The cartoon avatar's motion curves: reproducible, bounded, and tied to the speech."""
import numpy as np

import avatar_motion as am

FPS = 25


def _mouth(n=FPS * 40):
    rng = np.random.default_rng(0)
    m = rng.integers(0, 4, n)
    m[: FPS * 2] = 0          # a pause at the start
    return m


def test_curves_are_reproducible_and_full_length():
    m = _mouth()
    a = am.motion_curves(m, [0, 250, 500, 750], FPS, seed="slug")
    b = am.motion_curves(m, [0, 250, 500, 750], FPS, seed="slug")
    for k in a:
        assert len(a[k]) == len(m)
        assert np.array_equal(a[k], b[k])
    c = am.motion_curves(m, [0, 250, 500, 750], FPS, seed="other")
    assert not np.array_equal(a["head_dx"], c["head_dx"])


def test_amplitudes_stay_small():
    c = am.motion_curves(_mouth(), list(range(0, FPS * 40, 60)), FPS, seed="s")
    assert np.abs(c["head_dx"]).max() <= sum(am.SWAY_X) + am.GLANCE_HEAD + 1e-9
    assert np.abs(c["pupil_dx"]).max() <= am.GLANCE_PUPIL + 1e-9
    assert np.abs(c["tilt"]).max() < 4.5
    assert c["brow_dy"].max() <= 0 and c["brow_dy"].min() >= -am.BROW_LIFT - 1e-9
    assert 0 <= c["breath"].min() and c["breath"].max() <= 1


def test_no_glance_without_sentence_starts():
    c = am.motion_curves(_mouth(), [], FPS, seed="s")
    assert not c["pupil_dx"].any()


def test_glances_begin_at_a_sentence_start():
    starts = list(range(FPS, FPS * 40, FPS * 3))
    c = am.motion_curves(_mouth(), starts, FPS, seed="glance")
    moving = np.flatnonzero(c["pupil_dx"])
    assert len(moving), "expected at least one glance across 13 sentence starts"
    first = moving[0]
    assert any(0 <= first - s <= 1 for s in starts)


def test_silence_means_no_nod():
    m = np.zeros(FPS * 20, dtype=int)
    c = am.motion_curves(m, [], FPS, seed="s")
    assert not c["brow_dy"].any()
    # head_dy is only sway and breathing then
    assert np.abs(c["head_dy"]).max() <= am.SWAY_Y + am.BREATH_RISE + 1e-9


def test_sentence_start_frames():
    timing = {"sentences": [{"offset_s": 0.0}, {"offset_s": 4.3}, {"offset_s": 19.625}]}
    assert am.sentence_start_frames(timing, FPS) == [0, 108, 491]
