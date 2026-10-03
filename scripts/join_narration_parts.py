"""Join split narration pieces into one mp3 (pipeline step 1.4) - safe to run every time.

    python scripts/join_narration_parts.py audio/<slug>.mp3 [--force]

Only needed when step 1.2 stalled and the narration was generated in pieces
by hand. Name the pieces audio/<slug>.part1.mp3, audio/<slug>.part2.mp3, ...
next to where the joined file should go; they are joined in numeric order.

  - No pieces (the normal case, 1.2 finished in one go): prints "nothing to
    join" and exits 0 without touching anything.
  - Pieces, and no audio/<slug>.mp3 yet: joins them into it.
  - Pieces, and audio/<slug>.mp3 already exists: refuses, so leftover pieces
    can't overwrite a good narration. Pass --force if the pieces are the ones
    you want.
"""

import argparse
import re
import subprocess
import tempfile
from pathlib import Path


def find_parts(out_path):
    out_path = Path(out_path)
    pattern = re.compile(re.escape(out_path.stem) + r"\.part(\d+)\.mp3$")
    found = [(int(m.group(1)), p) for p in out_path.parent.glob(f"{out_path.stem}.part*.mp3")
             if (m := pattern.match(p.name))]
    return [p for _, p in sorted(found)]


def join(out_path, force=False):
    """True if pieces were joined, False if there was nothing to join."""
    out_path = Path(out_path)
    parts = find_parts(out_path)
    if not parts:
        print(f"nothing to join - no {out_path.stem}.part*.mp3 pieces next to {out_path} "
              f"(step 1.2 finished in one go). Skipping.")
        return False
    if out_path.exists() and not force:
        raise SystemExit(f"error: {out_path} already exists and {len(parts)} piece(s) were found "
                         f"({', '.join(p.name for p in parts)}). Refusing to overwrite it; pass --force "
                         f"if the pieces are the narration you want, or delete the stale pieces.")
    # ffmpeg's concat demuxer joins mp3s without re-encoding.
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as lst:
        for p in parts:
            lst.write(f"file '{p.resolve().as_posix()}'\n")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst.name,
                    "-c", "copy", str(out_path)], check=True)
    Path(lst.name).unlink(missing_ok=True)
    print(f"joined {len(parts)} piece(s) into {out_path}: {', '.join(p.name for p in parts)}")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out", help="audio/<slug>.mp3")
    ap.add_argument("--force", action="store_true", help="overwrite an existing audio/<slug>.mp3")
    args = ap.parse_args()
    join(args.out, args.force)


if __name__ == "__main__":
    main()
