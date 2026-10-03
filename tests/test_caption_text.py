"""Fused pronunciation names must not leak into anything a viewer reads."""
import json

from generate_narration import _build_srt, caption_text
from watch_video_lib import load_captions


def test_fused_names_are_unfused():
    assert caption_text("led by Wee-Kheng-Chiang.") == "led by Wee Kheng Chiang."
    assert caption_text("Wee-Kheng-Chiang's fourth son") == "Wee Kheng Chiang's fourth son"
    assert caption_text("Lim-Yew-Hock defeated A. P. Rajah") == "Lim Yew Hock defeated A. P. Rajah"


def test_real_compounds_are_left_alone():
    text = "the Build-To-Order scheme and the Britain-India-Nepal agreement"
    assert caption_text(text) == text


def test_srt_shows_names_as_written():
    srt = _build_srt([{"text": "It was founded by Wee-Kheng-Chiang.", "offset_s": 0.0, "duration_s": 3.0}])
    assert "Wee Kheng Chiang" in srt and "Wee-Kheng" not in srt


def test_video_captions_show_names_as_written(tmp_path):
    timing = tmp_path / "t.timing.json"
    timing.write_text(json.dumps([{"text": "Chua-Keh-Hai was the manager.", "offset_s": 0.0,
                                   "duration_s": 2.0}]), encoding="utf-8")
    assert [c["text"] for c in load_captions(timing)] == ["Chua Keh Hai was the manager."]
