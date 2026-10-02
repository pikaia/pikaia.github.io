import stage_youtube_text as syt

ARGS = dict(
    title="Barings, 1995: The Singapore Trading Desk That Broke a 233-Year-Old Bank",
    hook="In February 1995 a trader in Singapore brought down Britain's oldest merchant bank.",
    narration_line="Narration: synthesized voice (Kokoro TTS, open-source, Apache 2.0 license, voice bm_george)",
    avatar_line=None,
    credit_lines=["- Photo by A. Person, CC BY-SA 4.0, via Wikimedia Commons"],
    image_sources="Wikimedia Commons",
)


def test_tiktok_caption_shape():
    text = syt.tiktok_caption(**ARGS)
    lines = text.splitlines()
    assert lines[0] == ARGS["title"]
    assert ARGS["hook"] in text
    assert "Full story: link in bio" in text
    assert "http" not in text                      # TikTok captions don't link
    assert ARGS["narration_line"] in text
    assert "Images (Wikimedia Commons):" in text and ARGS["credit_lines"][0] in text
    assert lines[-1].startswith("#") and "#Singapore" in lines[-1] and "#Shorts" not in text


def test_tiktok_caption_includes_avatar_line_when_given():
    text = syt.tiktok_caption(**{**ARGS, "avatar_line": "Presenter: an illustrated avatar."})
    assert "Presenter: an illustrated avatar." in text


def test_tiktok_caption_over_limit_is_flagged():
    long = syt.tiktok_caption(**{**ARGS, "credit_lines": ["- " + "x" * 100] * 60})
    assert len(long) > syt.TIKTOK_CAPTION_LIMIT
    assert syt.tiktok_over_limit(long) and not syt.tiktok_over_limit(syt.tiktok_caption(**ARGS))
