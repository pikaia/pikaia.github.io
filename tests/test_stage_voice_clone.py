import json

import stage_youtube_text as syt


def test_no_sidecar_means_kokoro(tmp_path):
    line = syt.narration_disclosure("bm_george", tmp_path / "missing.voice.json")
    assert line == "Narration: synthesized voice (Kokoro TTS, open-source, Apache 2.0 license, voice bm_george)"
    assert syt.narration_disclosure("bm_george") == line


def test_sidecar_without_clone_means_kokoro(tmp_path):
    p = tmp_path / "x.voice.json"
    p.write_text(json.dumps({"voice": "bm_george", "clone": None}), encoding="utf-8")
    assert syt.narration_disclosure("bm_george", p).startswith("Narration: synthesized voice")


def test_openvoice_sidecar_discloses_clone(tmp_path):
    p = tmp_path / "x.voice.json"
    p.write_text(json.dumps({"voice": "bm_george", "clone": "openvoice"}), encoding="utf-8")
    line = syt.narration_disclosure("bm_george", p)
    assert line.startswith("Narration: an AI clone of the author's voice")
    assert "OpenVoice" in line and "MIT license" in line
