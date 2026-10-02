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
    assert bat.quantise(np.array([0.0, 0.07, 0.08, 0.44, 0.45, 0.84, 0.85, 1.0])) == [0, 0, 1, 1, 2, 2, 3, 3]


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
    subprocess.run(["python", "scripts/build_avatar_track.py", str(mp3), "--no-shapes"], check=True)
    import json
    data = json.loads((tmp_path / "clip.avatar.json").read_text(encoding="utf-8"))
    assert data["frames"] == len(data["mouth"])
    assert abs(data["duration_s"] - 3.0) < 0.1
    assert data["mouth"][:20] == "0" * 20


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
