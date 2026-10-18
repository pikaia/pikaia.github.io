"""--thumbnail picks the right image and frames it at the config's size."""
from types import SimpleNamespace

import pytest
from PIL import Image

from watch_video_lib import compose_thumbnail, thumbnail_slide


def _cfg(tmp_path, **extra):
    Image.new("RGB", (400, 300), (200, 30, 30)).save(tmp_path / "red.png")
    Image.new("RGB", (300, 400), (30, 30, 200)).save(tmp_path / "blue.png")
    base = dict(
        IMAGES={"RED": "red.png", "BLUE": "blue.png"},
        SLIDES=[{"type": "chart"},
                {"img": "RED", "type": "cover", "zoom": [1.1, 1.2, 1.3], "pan": [(0.2, 0.3), (0.5, 0.5), (0.8, 0.5)]},
                {"img": "BLUE", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}],
        _config_dir=str(tmp_path),
    )
    base.update(extra)
    return SimpleNamespace(**base)


def test_default_is_first_image_slide_at_its_opening_keyframe(tmp_path):
    s = thumbnail_slide(_cfg(tmp_path))
    assert s["img"] == "RED" and s["type"] == "cover"
    assert s["zoom"][0] == 1.1 and s["pan"][0] == (0.2, 0.3)


def test_key_string_overrides_default(tmp_path):
    s = thumbnail_slide(_cfg(tmp_path, THUMBNAIL="BLUE"))
    assert s == {"img": "BLUE", "type": "cover", "zoom": [1.0] * 3, "pan": [(0.5, 0.5)] * 3}


def test_dict_override_keeps_given_fields(tmp_path):
    s = thumbnail_slide(_cfg(tmp_path, THUMBNAIL={"img": "BLUE", "type": "letterbox", "pan": (0.5, 0.2)}))
    assert s["type"] == "letterbox" and s["pan"][0] == (0.5, 0.2)


def test_unknown_key_is_refused(tmp_path):
    with pytest.raises(ValueError):
        thumbnail_slide(_cfg(tmp_path, THUMBNAIL="NOPE"))


@pytest.mark.parametrize("size", [(1280, 720), (1080, 1920)])
def test_frame_matches_output_size(tmp_path, size):
    frame, _ = compose_thumbnail(_cfg(tmp_path), *size)
    assert frame.size == size
    assert frame.getpixel((size[0] // 2, size[1] // 2))[0] > 150  # the red image
