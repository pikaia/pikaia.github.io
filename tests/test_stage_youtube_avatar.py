import types

import stage_youtube_text as syt


def test_disclosure_only_with_avatar():
    assert syt.avatar_disclosure(None) is None
    assert syt.avatar_disclosure(types.SimpleNamespace()) is None
    line = syt.avatar_disclosure(types.SimpleNamespace(AVATAR={"ranges": [(0, 30)]}))
    assert line == "Presenter: an illustrated avatar of the author, animated locally from the narration audio."


def test_optional_config_tolerates_missing_or_absent(tmp_path):
    assert syt.optional_config(None) is None
    assert syt.optional_config(tmp_path / "not-written-yet.py") is None
    p = tmp_path / "cfg.py"
    p.write_text('AVATAR = {"ranges": [(0, 30)]}\n', encoding="utf-8")
    assert syt.optional_config(p).AVATAR == {"ranges": [(0, 30)]}
