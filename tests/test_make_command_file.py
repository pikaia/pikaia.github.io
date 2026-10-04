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


def test_subtitle_path_is_a_comment():
    out = render(POST, TEMPLATE.read_text(encoding="utf-8"))
    srt_lines = [ln for ln in out.splitlines() if ln.strip().endswith('.srt"')]
    assert srt_lines and all(ln.lstrip().startswith("#") for ln in srt_lines)


def test_refuses_to_overwrite(tmp_path):
    write(POST, out_dir=tmp_path)
    with pytest.raises(SystemExit):
        write(POST, out_dir=tmp_path)
    write(POST, force=True, out_dir=tmp_path)


def test_rejects_badly_named_post():
    with pytest.raises(SystemExit):
        render("_posts/no-date.md", "x")
