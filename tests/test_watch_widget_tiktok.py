import build_watch_widget as bww

TT = "https://www.tiktok.com/@lesserknownsingapore/video/7550000000000000000"


def test_row_includes_tiktok_button_when_given():
    row = bww.build_row_markup("https://youtu.be/x", "https://youtube.com/shorts/y", "g1", tiktok_url=TT)
    assert f'href="{TT}"' in row and ">TikTok<" in row
    assert row.index("youtube.com/shorts/y") < row.index(TT)       # after the Shorts button


def test_row_without_tiktok_is_unchanged():
    assert bww.build_row_markup("https://youtu.be/x", None, "g1") == \
        bww.build_row_markup("https://youtu.be/x", None, "g1", tiktok_url=None)
    assert "tiktok" not in bww.build_row_markup("https://youtu.be/x", None, "g1").lower()


def test_existing_tiktok_url_is_found_for_reruns():
    row = bww.build_row_markup("https://youtu.be/x", None, "g1", tiktok_url=TT)
    assert bww.find_existing_tiktok_url(row) == TT
    assert bww.find_existing_tiktok_url('<a href="https://youtu.be/x">') is None
