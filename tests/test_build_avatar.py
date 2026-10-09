import pytest
from PIL import Image, ImageChops

import avatar_lib as al
import build_avatar as ba


def test_layer_svg_hides_other_layers():
    import xml.etree.ElementTree as ET
    out = ba.layer_svg(al.SVG_PATH.read_text(encoding="utf-8"), "mouth-2")
    styles = {el.get("id"): el.get("style") for el in ET.fromstring(out).iter() if el.get("id") in al.LAYER_NAMES}
    assert styles.pop("mouth-2") is None
    assert set(styles.values()) == {"display:none"} and len(styles) == len(al.LAYER_NAMES) - 1


def test_layer_svg_missing_layer_errors():
    with pytest.raises(ValueError, match="mouth-3"):
        ba.layer_svg('<svg xmlns="http://www.w3.org/2000/svg"><g id="body"/></svg>', "body")


def test_build_layers(tmp_path):
    paths = ba.build_layers(al.SVG_PATH, tmp_path, size=128)
    assert [p.stem for p in paths] == al.ALL_LAYER_NAMES
    imgs = {p.stem: Image.open(p) for p in paths}
    for im in imgs.values():
        assert im.size == (128, 128) and im.mode == "RGBA"
    assert imgs["body"].getpixel((64, 64))[3] == 255          # opaque centre
    assert imgs["body"].getpixel((1, 1))[3] == 0              # transparent outside circle
    assert imgs["eyes-open"].getpixel((64, 64))[3] == 0       # eyes layer is only the eyes
    assert ImageChops.difference(imgs["mouth-0"], imgs["mouth-3"]).getbbox() is not None


def test_motion_parts_recompose_the_still_face(tmp_path):
    ba.build_layers(al.SVG_PATH, tmp_path, size=128)
    L = {n: Image.open(tmp_path / f"{n}.png").convert("RGBA") for n in al.ALL_LAYER_NAMES}
    still = L["body"].copy()
    still.alpha_composite(L["eyes-open"])
    still.alpha_composite(L["mouth-2"])
    parts = L["back"].copy()
    for n in ["head", "brows", "pupils", "glasses", "mouth-2", "rim"]:
        parts.alpha_composite(L[n])
    import numpy as np
    # Edges where the head meets the background anti-alias slightly
    # differently when drawn as separate layers; nothing a viewer can see.
    a, b = np.asarray(still).astype(int), np.asarray(parts).astype(int)
    seen = a[..., 3] > 32
    d = np.abs(a - b).max(axis=2)[seen]
    assert (d > 8).mean() < 0.005 and d.max() <= 64


def test_nested_layer_renders_alone():
    import xml.etree.ElementTree as ET
    out = ba.layer_svg(al.SVG_PATH.read_text(encoding="utf-8"), "head")
    styles = {el.get("id"): el.get("style") for el in ET.fromstring(out).iter() if el.get("id") in al.ALL_LAYER_NAMES}
    assert styles["head"] is None and styles["body"] is None      # itself and its ancestor stay
    assert styles["back"] == styles["brows"] == styles["rim"] == styles["mouth-0"] == "display:none"
