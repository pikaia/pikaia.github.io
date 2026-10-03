import re
import types
from pathlib import Path

from PIL import Image

import watch_video_lib as wvl

W, H = 1080, 1920
# TikTok's caption/username overlay (and YouTube Shorts' title row) cover
# roughly the bottom 22% of a 9:16 frame.
PLATFORM_OVERLAY_TOP = 0.78
# load_captions() caps a caption at 100 chars; a full-length one with wide
# letters is the tallest caption a Short can show (three lines).
WORST_CASE = "Mmm WWW the Barings trader in Singapore hid his huge losses in an error account numbered 88888 now"
DOC = Path(__file__).resolve().parent.parent / "docs" / "production-pipeline.md"


def caption_bottom(cfg):
    frame = Image.new("RGB", (W, H), (0, 0, 0))
    out = wvl.apply_caption(frame, 1.0, W, H, cfg, [{"offset_s": 0.0, "duration_s": 5.0, "text": WORST_CASE}])
    bbox = out.convert("L").point(lambda v: 255 if v > 200 else 0).getbbox()
    assert bbox is not None
    return bbox[3]


def test_worst_case_is_a_full_length_caption():
    assert len(WORST_CASE) <= 100


def test_default_short_caption_clears_platform_overlays():
    assert caption_bottom(types.SimpleNamespace(BURN_CAPTIONS=True)) < PLATFORM_OVERLAY_TOP * H


def test_template_short_caption_clears_platform_overlays():
    # The -short.py template in docs/production-pipeline.md section 3 uses a
    # bigger font; its CAPTION_Y_FRAC must still clear the overlay.
    y_fracs = {float(v) for v in re.findall(r"^CAPTION_Y_FRAC = ([\d.]+)", DOC.read_text(encoding="utf-8"), re.M)}
    assert y_fracs, "template no longer shows CAPTION_Y_FRAC"
    for y in y_fracs:
        cfg = types.SimpleNamespace(BURN_CAPTIONS=True, CAPTION_FONT_RATIO=0.032,
                                    CAPTION_MAX_WIDTH_FRAC=0.86, CAPTION_Y_FRAC=y)
        bottom = caption_bottom(cfg)
        assert bottom < PLATFORM_OVERLAY_TOP * H, f"CAPTION_Y_FRAC = {y} puts caption bottom at {bottom}px"


def test_caption_font_is_arial_not_the_fallback():
    # Without Arial, load_font() falls back to PIL's built-in default font
    # (itself a FreeTypeFont, but loaded from memory at a fixed small size),
    # and the safe-zone tests above would pass without proving anything.
    font = wvl.load_font(38)
    assert "arial" in str(getattr(font, "path", "")).lower() and font.size == 38
