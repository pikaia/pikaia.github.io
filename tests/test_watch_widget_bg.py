import types

import build_watch_widget as bww


def _cfg(**kw):
    base = dict(SLIDES=[{"img": "MAP", "type": "letterbox", "zoom": [1, 1, 1], "pan": [(0.5, 0.5)] * 3},
                        {"img": "PHOTO", "type": "cover", "zoom": [1, 1.05, 1.1], "pan": [(0.5, 0.5)] * 3}])
    base.update(kw)
    return types.SimpleNamespace(**base)


def test_slides_js_carries_image_bg_as_css_colour():
    lines, _, _ = bww.build_slides_js(_cfg(IMAGE_BG={"MAP": (232, 230, 224)}), {"MAP": "u1", "PHOTO": "u2"})
    assert 'bgc: "#e8e6e0"' in lines[0]
    assert "bgc" not in lines[1]


def test_slides_js_without_image_bg_unchanged():
    lines, _, _ = bww.build_slides_js(_cfg(), {"MAP": "u1", "PHOTO": "u2"})
    assert not any("bgc" in line for line in lines)


def test_viewer_js_paints_bgc_behind_letterbox():
    assert "s.bgc" in bww.WATCH_SCRIPT_TAIL
