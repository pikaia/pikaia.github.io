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
