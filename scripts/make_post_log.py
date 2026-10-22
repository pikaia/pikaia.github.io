"""Write docs/post-log.md: every post with its title, original posting date
and its revisions, from the git history.

    python scripts/make_post_log.py

A commit that touches one post (or a handful) is listed under each post it
touched, with its commit subject as the note. A commit that touches many
posts at once (a site-wide rollout, e.g. the Listen widget or the photo
galleries) is listed once, under "Site-wide changes", instead of repeating
under every post. Re-run it at step 12 of each post so the log keeps up.
"""
import re
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "post-log.md"
SITE_WIDE = 4        # a commit touching this many posts or more is a site-wide change
NOTE_LEN = 140
SGT = timezone(timedelta(hours=8))


def git_log():
    """[(hash, date, subject, [(status, old path, new path)])], newest first."""
    out = subprocess.run(
        ["git", "log", "--format=@@%h|%aI|%s", "--name-status", "-M", "--", "_posts"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    commits = []
    for block in out.split("@@")[1:]:
        head, *rows = block.strip().split("\n")
        h, stamp, subject = head.split("|", 2)
        date = datetime.fromisoformat(stamp).astimezone(SGT).strftime("%Y-%m-%d")  # commits carry UTC
        changes = []
        for row in rows:
            parts = row.split("\t")
            if len(parts) < 2:
                continue
            old, new = parts[1], parts[-1]
            if new.startswith("_posts/") or old.startswith("_posts/"):
                changes.append((parts[0][0], old, new))
        commits.append((h, date, subject, changes))
    return commits


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    fm = text.split("---", 2)[1] if text.startswith("---") else ""

    def get(key):
        m = re.search(rf'^{key}:\s*"?(.*?)"?\s*$', fm, re.M)
        return m[1] if m else ""
    return get("title"), get("date"), get("last_modified_at")


def short_note(subject, title):
    """The commit subject, minus a leading "<Name> post:" label, cut at a word."""
    note = re.sub(r"^[^:]{1,60}\bposts?:\s*", "", subject)
    note = note[0].upper() + note[1:] if note else subject
    if len(note) > NOTE_LEN:
        note = note[:NOTE_LEN].rsplit(" ", 1)[0].rstrip(",;:-") + "..."
    return note


def build(commits, posts):
    """posts: {path: (title, date, last_modified)} for the posts that exist now."""
    # Walk newest to oldest, mapping each path a post has had to its current path.
    alias = {p: p for p in posts}
    per_post = {p: [] for p in posts}
    site_wide = []
    for h, date, subject, changes in commits:
        touched = set()
        for status, old, new in changes:
            current = alias.get(new)
            if status == "R" and current:
                alias[old] = current
            if current in posts:
                touched.add(current)
        if len(touched) >= SITE_WIDE:
            site_wide.append((date, subject, len(touched)))
        else:
            for p in touched:
                per_post[p].append((date, h, subject))
    lines = ["# Post log", "",
             "Every post on the site, newest first, with the date it was first posted and "
             "its revisions since. Generated from the git history by "
             "`scripts/make_post_log.py`; don't edit by hand, re-run the script.", "",
             f"Changes that touched {SITE_WIDE} or more posts at once are listed once, under "
             "[Site-wide changes](#site-wide-changes), not under each post.", ""]
    for p in sorted(posts, key=lambda p: (posts[p][1], p), reverse=True):
        title, date, modified = posts[p]
        revs = per_post[p][:-1]          # the oldest commit created the post
        lines.append(f"## {title}")
        lines.append("")
        meta = f"First posted {date[:10]}"
        if modified[:10] and modified[:10] != date[:10]:
            meta += f" · last updated {modified[:10]}"
        lines.append(f"{meta} · `{Path(p).name}`")
        lines.append("")
        if revs:
            for d, h, s in revs:
                lines.append(f"- {d}: {short_note(s, title)} (`{h}`)")
        else:
            lines.append("- No revisions yet.")
        lines.append("")
    lines += ["## Site-wide changes", ""]
    for d, s, n in site_wide:
        lines.append(f"- {d}: {short_note(s, '')} ({n} posts)")
    return "\n".join(lines) + "\n"


def main():
    posts = {f"_posts/{p.name}": front_matter(p) for p in sorted((ROOT / "_posts").glob("*.md"))}
    OUT.write_text(build(git_log(), posts), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} - {len(posts)} posts")


if __name__ == "__main__":
    main()
