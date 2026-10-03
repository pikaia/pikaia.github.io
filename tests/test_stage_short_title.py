import stage_youtube_text as syt

LONG = "The Progressive Party: The Colonial-Era Party That Won Singapore's First Elections, Then Vanished"


def test_short_title_keeps_full_title_when_it_fits():
    assert syt.short_title("Barings, 1995: The Desk That Broke a Bank") == "Barings, 1995: The Desk That Broke a Bank #Shorts"


def test_short_title_falls_back_to_the_part_after_the_colon():
    t = syt.short_title(LONG)
    assert t == "The Colonial-Era Party That Won Singapore's First Elections, Then Vanished #Shorts"
    assert len(t) <= syt.YOUTUBE_TITLE_LIMIT


def test_short_title_truncates_at_a_word_when_nothing_else_fits():
    t = syt.short_title("word " * 40)
    assert len(t) <= syt.YOUTUBE_TITLE_LIMIT and t.endswith("… #Shorts") and "wor…" not in t
