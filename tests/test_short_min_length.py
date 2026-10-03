import types

import pytest

import watch_video_lib as wvl


def _short(**kw):
    base = dict(WIDTH=1080, HEIGHT=1920, BURN_CAPTIONS=True, TOTAL_DURATION=65.0)
    base.update(kw)
    return types.SimpleNamespace(**base)


def test_short_over_a_minute_passes():
    wvl.validate_short_config(_short(), "scripts/video-configs/post-short.py")


def test_short_of_a_minute_or_less_is_refused(capsys):
    with pytest.raises(SystemExit):
        wvl.validate_short_config(_short(TOTAL_DURATION=60.0), "scripts/video-configs/post-short.py")
    err = capsys.readouterr().err
    assert "60" in err and "TikTok" in err


def test_older_short_can_opt_out():
    wvl.validate_short_config(_short(TOTAL_DURATION=42.0, SHORT_UNDER_A_MINUTE_OK=True),
                              "scripts/video-configs/post-short.py")


def test_main_video_configs_are_not_affected():
    wvl.validate_short_config(types.SimpleNamespace(TOTAL_DURATION=30.0), "scripts/video-configs/post.py")


def test_every_existing_short_config_still_validates():
    from pathlib import Path
    for p in sorted(Path("scripts/video-configs").glob("*-short.py")):
        wvl.validate_short_config(wvl.load_config(p), p)
