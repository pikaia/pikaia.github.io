"""Write a post's pipeline command file from docs/commands/TEMPLATE.txt.

    python scripts/make_command_file.py _posts/<date>-<slug>.md [--force]

Fills in the post path and slug and writes docs/commands/<slug>.txt - every
step from 1.1 to 12, each wrapped in the tee-to-log block, with placeholder
URLs in step 11 and the subtitle path as a comment line. Refuses to overwrite
an existing command file (it may hold pasted URLs) unless --force is given.
"""

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = REPO_ROOT / "docs" / "commands" / "TEMPLATE.txt"


def slug_for(post_path):
    m = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.md$", Path(post_path).name)
    if not m:
        raise SystemExit(f"error: {post_path} isn't named _posts/YYYY-MM-DD-<slug>.md")
    return m.group(1)


def render(post_path, template_text):
    post = Path(post_path).as_posix()
    return template_text.replace("{POST}", post).replace("{SLUG}", slug_for(post))


def write(post_path, force=False, out_dir=None):
    out = Path(out_dir or REPO_ROOT / "docs" / "commands") / f"{slug_for(post_path)}.txt"
    if out.exists() and not force:
        raise SystemExit(f"error: {out} already exists (it may hold pasted URLs). Pass --force to replace it.")
    out.write_text(render(post_path, TEMPLATE.read_text(encoding="utf-8")), encoding="utf-8")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("post", help="_posts/YYYY-MM-DD-<slug>.md")
    ap.add_argument("--force", action="store_true", help="overwrite an existing command file")
    args = ap.parse_args()
    print(f"wrote {write(args.post, args.force)}")


if __name__ == "__main__":
    main()
