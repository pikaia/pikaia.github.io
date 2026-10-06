import json

import numpy as np
import pytest

import avatar_lib as al
import build_photo_avatar as bpa


def spec(**over):
    s = {"shots": {k: f"{k}.jpg" for k in bpa.SHOTS}, "mouth": [1000, 1200], "eyes_y": 900, "face_w": 600}
    s.update(over)
    return s


def test_load_spec_ok(tmp_path):
    p = tmp_path / "s.json"
    p.write_text(json.dumps(spec()), encoding="utf-8")
    assert bpa.load_spec(p)["face_w"] == 600


@pytest.mark.parametrize("bad", [
    {"shots": {"rest": "r.jpg"}},
    {"mouth": None},          # face_w and eyes_y without mouth: all three or none
])
def test_load_spec_rejects_incomplete(tmp_path, bad):
    s = spec(**bad)
    if s.get("mouth") is None:
        del s["mouth"]
    p = tmp_path / "s.json"
    p.write_text(json.dumps(s), encoding="utf-8")
    with pytest.raises(ValueError):
        bpa.load_spec(p)


def test_every_layer_has_a_source():
    built = {"body", "eyes-open", "mouth-0"} | set(bpa.SHOT_LAYERS.values())
    assert built == set(al.LAYER_NAMES)


def test_colour_ring_stays_above_the_mouth_line():
    geo = bpa.Geometry(spec(), (1100, 900))
    assert geo.mouth_ring.any()
    assert not geo.mouth_ring[geo.my:, :].any()          # never reaches the chin or shirt
    assert not (geo.mouth_ring & (geo.mouth > 0.05)).any()


def test_to_layer_is_a_512_circle():
    rgb = np.full((400, 400, 3), 128, np.float32)
    im = bpa.to_layer(rgb, np.ones((400, 400)), (0, 0, 400, 400))
    assert im.size == (512, 512) and im.mode == "RGBA"
    assert im.getpixel((256, 256))[3] == 255
    assert im.getpixel((2, 2))[3] == 0


def test_shots_json_is_complete():
    s = bpa.load_spec(bpa.SPEC)
    assert set(s["shots"]) == set(bpa.SHOTS)


def test_load_spec_allows_landmark_measurement(tmp_path):
    s = spec()
    for k in ("mouth", "eyes_y", "face_w"):
        del s[k]
    p = tmp_path / "s.json"
    p.write_text(json.dumps(s), encoding="utf-8")
    assert "mouth" not in bpa.load_spec(p)
