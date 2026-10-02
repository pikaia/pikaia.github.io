import types

import stage_youtube_text as syt


def test_disclosure_only_with_avatar():
    assert syt.avatar_disclosure(None) is None
    assert syt.avatar_disclosure(types.SimpleNamespace()) is None
    line = syt.avatar_disclosure(types.SimpleNamespace(AVATAR={"ranges": [(0, 30)]}))
    assert line == "Presenter: an illustrated avatar of the author, animated locally from the narration audio."
