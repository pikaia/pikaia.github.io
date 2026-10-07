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


def test_lip_angle_reads_the_corner_line():
    pts = np.zeros((478, 2), np.float32)
    pts[61], pts[291] = (100, 200), (200, 200)
    assert bpa.lip_angle(pts) == 0.0
    pts[291] = (200, 210)                     # right corner lower = positive (image y down)
    assert 5.6 < bpa.lip_angle(pts) < 5.8


def test_lip_centre_x_is_the_corner_midpoint():
    pts = np.zeros((478, 2), np.float32)
    pts[61], pts[291] = (100, 200), (180, 204)
    assert bpa.lip_centre_x(pts) == 140.0


def test_soft_edge_mask_drops_background_and_stray_blobs():
    # A person-confidence map that never reaches 0 on the background (the
    # segmenter's real behaviour), one large person region and a small stray
    # region: the background and the stray must both come out as 0.
    p = np.full((200, 200), 0.05, np.float32)
    p[60:200, 50:150] = 0.95   # the person
    p[10:30, 10:30] = 0.9      # a stray blob, e.g. a door frame
    m = bpa.soft_edge_mask(p)
    assert m[100, 100] > 0.99          # solid inside
    assert m[5, 190] < 0.01            # no background ghost
    assert m[20, 20] < 0.01            # stray blob removed


def test_crop_centres_on_head_not_mouth():
    s = {"mouth": [400, 600], "eyes_y": 400, "face_w": 200}
    geo = bpa.Geometry(s, (500, 500))
    person = np.zeros((500, 500), np.float32)
    person[:, 160:260] = 1.0           # head spans x 160-259 at half res: centre ~210
    before = geo.crop
    geo.centre_on_head(person)
    assert geo.crop[0] - before[0] == 209 - 200
    assert (geo.crop[0] + geo.crop[2]) // 2 == 209
