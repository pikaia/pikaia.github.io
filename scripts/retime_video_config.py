"""Move a video config's slide times onto a re-voiced narration's new timing.

When a post is re-narrated with its text unchanged (a pronunciation fix,
a voice change), every sentence keeps its index but its offset_s moves.
Each SCHEDULE time and TOTAL_DURATION was written as an exact timing.json
offset (or, for the main video's TOTAL, the end of the last sentence), so
each one maps to the same sentence's new offset. The old timing is read
from git (HEAD) unless --old-timing names a file.

    python scripts/retime_video_config.py scripts/video-configs/<slug>.py [<slug>-short.py ...]

It refuses, and changes nothing, if the sentence texts differ or a time
does not match an old sentence boundary.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _key(t):
    return round(float(t), 3)


def _fmt(t):
    s = f"{t:.3f}".rstrip("0")
    return s + "0" if s.endswith(".") else s


def _norm(text):
    return text.replace("-", " ")


def boundary_map(old, new):
    """{old time: new time} for every sentence start, plus the end of the narration."""
    # Hyphens are ignored: a name fused for pronunciation since the old
    # narration (Lim Yew Hock -> Lim-Yew-Hock) is still the same sentence.
    if [_norm(s["text"]) for s in old] != [_norm(s["text"]) for s in new]:
        raise ValueError(f"sentence texts differ ({len(old)} old vs {len(new)} new) - the post text changed, so retiming by index is unsafe")
    m = {_key(o["offset_s"]): n["offset_s"] for o, n in zip(old, new)}
    m[_key(old[-1]["offset_s"] + old[-1]["duration_s"])] = round(new[-1]["offset_s"] + new[-1]["duration_s"], 3)
    return m


def retime_source(src, bmap):
    """Return src with SCHEDULE times and TOTAL_DURATION mapped through bmap."""
    def lookup(tok):
        k = _key(tok)
        if k not in bmap:
            raise ValueError(f"time {tok} is not a sentence boundary in the old timing")
        return _fmt(bmap[k])

    sm = re.search(r"^SCHEDULE = \[(.*?)\]$", src, re.M | re.S)
    tm = re.search(r"^TOTAL_DURATION = ([\d.]+)$", src, re.M)
    if not sm or not tm:
        raise ValueError("no SCHEDULE / TOTAL_DURATION found")
    body = re.sub(r"\(\s*([\d.]+)\s*,", lambda m: "(" + lookup(m.group(1)) + ",", sm.group(1))
    out = src[:sm.start(1)] + body + src[sm.end(1):]
    tm = re.search(r"^TOTAL_DURATION = ([\d.]+)$", out, re.M)
    return out[:tm.start(1)] + lookup(tm.group(1)) + out[tm.end(1):]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("configs", nargs="+")
    ap.add_argument("--old-timing", help="old timing.json (default: the committed HEAD version)")
    args = ap.parse_args()
    for cfg in args.configs:
        src = Path(cfg).read_text(encoding="utf-8")
        tj = re.search(r'^TIMING_JSON = "([^"]+)"', src, re.M).group(1)
        new = json.loads((ROOT / tj).read_text(encoding="utf-8"))
        if args.old_timing:
            old = json.loads(Path(args.old_timing).read_text(encoding="utf-8"))
        else:
            old = json.loads(subprocess.run(["git", "show", f"HEAD:{tj}"], cwd=ROOT, capture_output=True,
                                            check=True).stdout.decode("utf-8"))
        try:
            out = retime_source(src, boundary_map(old, new))
        except ValueError as e:
            sys.exit(f"{cfg}: {e}")
        if out == src:
            print(f"{cfg}: unchanged")
            continue
        Path(cfg).write_text(out, encoding="utf-8", newline="")
        t0 = re.search(r"^TOTAL_DURATION = ([\d.]+)$", src, re.M).group(1)
        t1 = re.search(r"^TOTAL_DURATION = ([\d.]+)$", out, re.M).group(1)
        print(f"{cfg}: retimed, TOTAL_DURATION {t0} -> {t1}")


if __name__ == "__main__":
    main()
