"""The per-post command file is filled in from the template, safely."""
import pytest

from make_command_file import TEMPLATE, render, write

POST = "_posts/2026-10-04-some-post.md"


def test_template_has_no_leftover_post_details():
    text = TEMPLATE.read_text(encoding="utf-8")
    assert "{SLUG}" in text and "{POST}" in text
    assert not any(u in text for u in ("youtu.be/H", "shorts/2", "video/7"))  # no real URLs


def test_render_fills_slug_and_post():
    out = render(POST, TEMPLATE.read_text(encoding="utf-8"))
    assert "{SLUG}" not in out and "{POST}" not in out
    assert "logs/some-post.log" in out and POST in out


def test_no_subtitle_path_line():
    out = render(POST, TEMPLATE.read_text(encoding="utf-8"))
    assert not [ln for ln in out.splitlines() if ln.lstrip().startswith("#") and ".srt" in ln]


def test_compresses_both_files_for_upload():
    out = render(POST, TEMPLATE.read_text(encoding="utf-8"))
    assert "-crf 26" in out and "+faststart" in out
    assert "preview-motion/some-post-web.mp4" in out
    assert "preview-motion/some-post-short-web.mp4" in out


def test_refuses_to_overwrite(tmp_path):
    write(POST, out_dir=tmp_path)
    with pytest.raises(SystemExit):
        write(POST, out_dir=tmp_path)
    write(POST, force=True, out_dir=tmp_path)


def test_rejects_badly_named_post():
    with pytest.raises(SystemExit):
        render("_posts/no-date.md", "x")


def test_copies_upload_files_to_google_drive():
    out = render(POST, TEMPLATE.read_text(encoding="utf-8"))
    step = out[out.index("=== 9.1 Copy"):]
    step = step[:step.index("tee -a")]
    assert 'dest="G:/My Drive/videos"' in step
    for f in ("preview-motion/some-post-web.mp4", "preview-motion/some-post-short-web.mp4",
              "preview-motion/some-post-thumbnail.jpg", "preview-motion/some-post-short-thumbnail.jpg",
              "audio/some-post.srt", "docs/youtube_helper/some-post-youtube.txt"):
        assert f in step
    # 9.1 is Claude's step after the review, not part of Chris's 4-9 run.
    assert out.index("steps 4 to 9 done, review logs") < out.index("=== 9.1 Copy") < out.index("=== 11. Wire")


def test_clears_google_drive_copies_after_step_12():
    out = render(POST, TEMPLATE.read_text(encoding="utf-8"))
    step = out[out.index("=== 12.1 Clear"):]
    step = step[:step.index("tee -a")]
    assert 'rm -v "G:/My Drive/videos/some-post"*' in step
    assert out.index("=== 11. Wire") < out.index("=== 12.1 Clear")
