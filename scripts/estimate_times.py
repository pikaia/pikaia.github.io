"""Rough time estimate for a group of pipeline steps, printed before they run.

    python scripts/estimate_times.py <slug> 1      # steps 1.1-2 (narration)
    python scripts/estimate_times.py <slug> 4-9    # steps 4-9 (renders)

A guess, not a promise: each step's rate (seconds of work per second of
narration) is the median of the last few posts' logs/*.log runs, scaled to
this post's length. The two renders also scale with the worker count, which
watch_video_lib picks from free memory at render time - so the estimate uses
the memory free *now*, and closing Chrome before step 6 can shorten it.
Falls back to built-in rates when there are no logs (logs/ isn't committed).
"""

import argparse
import re
import statistics
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from watch_video_lib import _available_memory_gb  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
WORDS_PER_SECOND = 2.35  # narration pace, measured on seven posts (2.23-2.45)
RECENT = 8               # how many posts' logs to take the median over

# key -> (label, unit, fallback rate). Units: "main"/"short" = per second of
# that video; "main_w"/"short_w" = worker-seconds per second (divided by the
# worker count); "both" = per second of main + Short; "const" = flat seconds.
STEPS = {
    "1.2": ("Narration audio", "main", 0.6),
    "1.5": ("Avatar mouth track", "main", 0.045),
    "5": ("Smoothness check", "main", 1.0),
    "6": ("Main video render", "main_w", 3.8),
    "6a": ("Avatar track", "main", 0.03),
    "6b": ("Avatar overlay", "main", 0.2),
    "7.1S": ("Short smoothness check", "short", 1.3),
    "7.2S": ("Short render", "short_w", 5.5),
    "8.1": ("Frame count check", "both", 0.04),
    "8.4": ("Compress the main video", "main", 0.09),
    "8.4S": ("Compress the Short", "short", 0.12),
}
GROUPS = {
    "1": ["1.1", "1.2", "1.3", "1.4", "1.5", "2"],
    "4-9": ["4", "5", "6", "6a", "6b", "7.1S", "7.2S", "8.1", "8.2", "8.2S", "8.3", "8.4", "8.4S", "9"],
}
CONST_SECONDS = 2


def step_key(header):
    """'7.2 Render the Short' -> '7.2S'; '8.1 Verify ... (auto-covers the Short)' -> '8.1'."""
    key = header.split()[0].rstrip(".")
    if "(Short)" in header or re.search(r"\bthe Short( for|$)", header):
        key += "S"
    return key


def parse_log(text):
    """Every timed step in a log as (key, seconds, workers or None)."""
    runs = []
    for block in re.split(r"(?m)^=== ", text)[1:]:
        header = block.split(" ===")[0]
        real = re.findall(r"(?m)^real\t(\d+)m([\d.]+)s", block)
        if not real:
            continue
        workers = re.findall(r"across (\d+) workers", block) or re.findall(r"with (\d+) worker\(s\)", block)
        runs.append((step_key(header), int(real[-1][0]) * 60 + float(real[-1][1]),
                     int(workers[-1]) if workers else None))
    return runs


def config_duration(path):
    m = re.search(r"(?m)^TOTAL_DURATION\s*=\s*([\d.]+)", path.read_text(encoding="utf-8")) if path.exists() else None
    return float(m.group(1)) if m else None


def units(unit, main, short, workers):
    """The quantity a step's rate multiplies, or None if it can't be known."""
    if unit in ("main_w", "short_w") and not workers:
        return None
    base = {"main": main, "short": short, "main_w": main, "short_w": short,
            "both": (main or 0) + (short or 0) if main else None}[unit]
    if not base:
        return None
    return base / workers if unit.endswith("_w") else base


def history_rates(log_dir, cfg_dir):
    """key -> list of rates from the most recent RECENT logs that ran that step."""
    rates = {k: [] for k in STEPS}
    for log in sorted(Path(log_dir).glob("*.log"), key=lambda p: p.stat().st_mtime, reverse=True):
        main = config_duration(Path(cfg_dir) / f"{log.stem}.py")
        short = config_duration(Path(cfg_dir) / f"{log.stem}-short.py")
        per_log = {}
        for key, secs, workers in parse_log(log.read_text(encoding="utf-8", errors="replace")):
            if key not in STEPS:
                continue
            u = units(STEPS[key][1], main, short, workers)
            if not u:
                continue
            # 1.2 reruns hit the per-sentence cache, so keep its slowest run
            # (the full synthesis); for everything else the last run counts.
            if key == "1.2" and key in per_log:
                per_log[key] = max(per_log[key], secs / u)
            else:
                per_log[key] = secs / u
        for key, rate in per_log.items():
            if len(rates[key]) < RECENT:
                rates[key].append(rate)
    return rates


def render_workers(avail_gb):
    """The worker count watch_video_lib.render() would pick right now."""
    import os
    cpu_cap = max(1, min((os.cpu_count() or 2) - 2, 10))
    return cpu_cap if avail_gb is None else min(cpu_cap, max(1, int((avail_gb - 2.0) / 1.7)))


def estimate(group, main, short, workers, rates, avatar=True):
    """[(key, label, seconds)] for the group's steps."""
    out = []
    for key in GROUPS[group]:
        if key in ("6a", "6b") and not avatar:
            continue
        if key.endswith("S") and not short and key.startswith(("7", "8")):
            continue
        if key not in STEPS:
            out.append((key, None, CONST_SECONDS))
            continue
        label, unit, fallback = STEPS[key]
        rate = statistics.median(rates[key]) if rates.get(key) else fallback
        u = units(unit, main, short or 0, workers)
        out.append((key, label, rate * (u or 0)))
    return out


def fmt(secs):
    mins = round(secs / 60)
    if mins < 1:
        return "under 1 min"
    return f"{mins // 60} h {mins % 60:02d} min" if mins >= 60 else f"{mins} min"


def report(rows, header, now=None, slow_render=None):
    lines = [header]
    small = 0.0
    for key, label, secs in rows:
        if label is None or secs < 60:
            small += secs
        else:
            lines.append(f"  {key.rstrip('S'):<5}{label:<26}~{fmt(secs)}")
    if small:
        lines.append(f"  {'':<5}{'other steps':<26}{'' if small < 30 else '~'}{fmt(small)}")
    total = sum(s for _, _, s in rows)
    done = (now or datetime.now()) + timedelta(seconds=total)
    lines.append(f"  Total: about {fmt(total)}, done around {done.strftime('%I:%M %p').lstrip('0')}")
    if slow_render:
        lines.append(f"  (If memory fills up and the render drops to 1 worker, step 6 alone takes ~{fmt(slow_render)}.)")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug")
    ap.add_argument("group", choices=sorted(GROUPS))
    args = ap.parse_args()

    cfg_dir = REPO_ROOT / "scripts" / "video-configs"
    rates = history_rates(REPO_ROOT / "logs", cfg_dir)
    main_cfg = cfg_dir / f"{args.slug}.py"
    main_dur = config_duration(main_cfg)
    short_dur = config_duration(cfg_dir / f"{args.slug}-short.py")
    if main_dur is None:
        from generate_narration import extract_narrative
        posts = sorted((REPO_ROOT / "_posts").glob(f"*-{args.slug}.md"))
        if not posts:
            raise SystemExit(f"error: no _posts/*-{args.slug}.md")
        words = sum(len(p.split()) for p in extract_narrative(posts[-1].read_text(encoding="utf-8")))
        main_dur = words / WORDS_PER_SECOND
    avatar = not main_cfg.exists() or bool(re.search(r"(?m)^AVATAR\s*=", main_cfg.read_text(encoding="utf-8")))

    avail = _available_memory_gb()
    workers = render_workers(avail)
    rows = estimate(args.group, main_dur, short_dur, workers, rates, avatar)
    mem = f", {avail:.1f} GB free now" if avail is not None else ""
    if args.group == "1":
        header = f"Time estimate for steps 1.1-2 (narration about {fmt(main_dur)} long):"
        slow = None
    else:
        header = (f"Time estimate for steps 4-9 (main video {fmt(main_dur)}"
                  f"{f', Short {fmt(short_dur)}' if short_dur else ''}; {workers} render worker(s){mem}):")
        slow = dict((k, t) for k, _, t in estimate("4-9", main_dur, short_dur, 1, rates, avatar))["6"] if workers > 1 else None
    print(report(rows, header, slow_render=slow))
    print("  A rough guess from recent posts' logs.")


if __name__ == "__main__":
    main()
