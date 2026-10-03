"""Letterbox and chart slides that hold still by design aren't flagged JERKY."""
from watch_video_lib import static_slide_kind


def test_pinned_letterbox_is_static():
    assert static_slide_kind({"type": "letterbox", "zoom": [1.0, 1.04, 1.08], "pan": [(0.5, 0.5)] * 3}) == "letterbox"


def test_letterbox_with_moving_pan_is_checked_normally():
    assert static_slide_kind({"type": "letterbox", "pan": [(0.4, 0.5), (0.5, 0.5), (0.6, 0.5)]}) is None


def test_chart_is_static():
    assert static_slide_kind({"type": "chart"}) == "chart"


def test_cover_is_checked_normally():
    assert static_slide_kind({"type": "cover", "pan": [(0.5, 0.5)] * 3}) is None
