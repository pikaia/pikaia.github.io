import types

from PIL import Image

import watch_video_lib as wvl


def _transparent_png(path):
    im = Image.new("RGBA", (40, 20), (0, 0, 0, 0))          # fully transparent
    im.paste((200, 30, 30, 255), (0, 0, 20, 20))            # left half opaque red
    im.save(path)


def test_load_source_default_is_unchanged(tmp_path):
    _transparent_png(tmp_path / "t.png")
    im = wvl.load_source("t.png", tmp_path)
    assert im.mode == "RGB" and im.getpixel((30, 10)) == (0, 0, 0)   # alpha dropped, as before


def test_load_source_flattens_onto_bg(tmp_path):
    _transparent_png(tmp_path / "t.png")
    im = wvl.load_source("t.png", tmp_path, bg=(255, 255, 255))
    assert im.getpixel((30, 10)) == (255, 255, 255)
    assert im.getpixel((10, 10)) == (200, 30, 30)


def test_prepare_slide_uses_config_image_bg(tmp_path):
    _transparent_png(tmp_path / "t.png")
    cfg = types.SimpleNamespace(IMAGES={"T": "t.png"}, IMAGE_BG={"T": (255, 255, 255)}, _config_dir=tmp_path,
                                SLIDES=[{"img": "T", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3}])
    _, prepared, *_rest, fg, fx, fy = wvl._prepare_slide(cfg, 0, 320, 180)
    assert fg.getpixel((fg.width - 2, fg.height // 2))[:3] == (255, 255, 255)
