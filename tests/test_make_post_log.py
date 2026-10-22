"""make_post_log: per-post revisions, site-wide rollouts listed once, renames
followed back to the post's current file."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import make_post_log as mpl  # noqa: E402

A, B = "_posts/2026-01-02-a.md", "_posts/2026-01-01-b.md"
POSTS = {A: ("Post A", "2026-01-02 09:00:00 +0800", "2026-01-05 09:00:00 +0800"),
         B: ("Post B", "2026-01-01 09:00:00 +0800", "2026-01-01 09:00:00 +0800")}


def test_revisions_rollouts_and_renames(monkeypatch):
    monkeypatch.setattr(mpl, "SITE_WIDE", 2)
    commits = [  # newest first, as git log gives them
        ("c4", "2026-01-05", "Post A post: fixed a date", [("M", A, A)]),
        ("c3", "2026-01-04", "Add the Listen widget to every post", [("M", A, A), ("M", B, B)]),
        ("c2", "2026-01-03", "Rename post A", [("R", "_posts/old-a.md", A)]),
        ("c1", "2026-01-02", "Post A draft", [("A", "_posts/old-a.md", "_posts/old-a.md")]),
        ("c0", "2026-01-01", "Post B draft", [("A", B, B)]),
    ]
    out = mpl.build(commits, POSTS)
    a_part = out.split("## Post A")[1].split("## Post B")[0]
    assert "First posted 2026-01-02 · last updated 2026-01-05" in a_part
    assert "- 2026-01-05: Fixed a date (`c4`)" in a_part
    assert "- 2026-01-03: Rename post A (`c2`)" in a_part   # the rename is a revision
    assert "Post A draft" not in a_part                      # the creating commit is not
    assert "Listen widget" not in a_part                     # rollouts go to their own section
    assert "No revisions yet." in out.split("## Post B")[1].split("## Site-wide")[0]
    assert "- 2026-01-04: Add the Listen widget to every post (2 posts)" in out
    assert out.index("## Post A") < out.index("## Post B")    # newest post first


def test_short_note_trims_at_a_word():
    note = mpl.short_note("Labuan post: " + "word " * 60, "")
    assert note.startswith("Word word") and note.endswith("...")
    assert len(note) <= mpl.NOTE_LEN + 3
