"""--clone openvoice: lengths, cache keys and the converter round trip (faked)."""
import json

import numpy as np
import pytest
import soundfile as sf

import generate_narration as gn


def test_match_length_pads_and_trims_within_a_frame():
    a = np.ones(1000, dtype=np.float32)
    assert len(gn._match_length(a, 1200, "s")) == 1200
    assert gn._match_length(a, 1200, "s")[-1] == 0
    assert len(gn._match_length(a, 900, "s")) == 900


def test_match_length_stops_on_drift_over_a_frame():
    a = np.ones(gn.SAMPLE_RATE, dtype=np.float32)
    with pytest.raises(SystemExit, match="Pillai"):
        gn._match_length(a, gn.SAMPLE_RATE - int(0.05 * gn.SAMPLE_RATE), "Pillai was born")


def test_clone_key_depends_on_reference_and_differs_from_george():
    k = gn._sentence_cache_key("Hello there.", "bm_george", "b")
    a, b = gn._clone_cache_key(k, "aaa"), gn._clone_cache_key(k, "bbb")
    assert a != b and k not in (a, b)
    assert a == gn._clone_cache_key(k, "aaa")


def test_clone_round_trip_with_fake_converter(tmp_path, monkeypatch):
    monkeypatch.setattr(gn, "_CACHE_DIR", str(tmp_path / "cache"))
    ref = tmp_path / "ref.wav"
    sf.write(ref, np.zeros(2400, dtype=np.float32), 24000)
    george = [np.full(4800, 0.1, dtype=np.float32), None, np.full(2400, 0.1, dtype=np.float32)]
    paths = [str(tmp_path / f"{k}.npy") for k in ("a" * 32, "b" * 32, "c" * 32)]
    calls = []

    def fake_run(cmd, check):
        calls.append(cmd)
        jobs = json.load(open(cmd[cmd.index("--manifest") + 1], encoding="utf-8"))
        for job in jobs:  # 'converted' = half volume, 5 ms short
            a, sr = sf.read(job["in"], dtype="float32")
            sf.write(job["out"], a[:-120] * 0.5, sr)

    out = gn.clone_openvoice(["one.", "two.", "three."], george, paths, str(ref), run=fake_run)
    assert out[1] is None
    assert [len(x) for x in (out[0], out[2])] == [4800, 2400]
    assert out[0][0] == pytest.approx(0.05, abs=1e-3)
    # Second run: everything comes from the clone cache, no converter call.
    out2 = gn.clone_openvoice(["one.", "two.", "three."], george, paths, str(ref), run=fake_run)
    assert len(calls) == 1 and np.array_equal(out2[0], out[0])


def test_clone_flag_is_off_by_default():
    import inspect
    assert inspect.signature(gn.synthesize_with_timing).parameters["clone"].default is None
