"""Run one pipeline step with its output going only to the post's log (Claude's hand-off mode).

    python scripts/run_step_quiet.py logs/<slug>.log "<section>.<n> <short name>" -- <command> <arg> ...

The same step Chris runs from the command file, minus the console flood: the
log gets exactly what the command file's tee-to-log block would write (blank
line, date, "=== ... ===" header, the echoed "$ command", the output, a
"real ..." timing line, blank line), so scripts/watch-pipeline-log.sh and a
later read of the log see no difference. The console only gets a short
summary:

  - the header, OK/FAILED with the exit code, and the elapsed time;
  - lines that look like a problem (error, warning, traceback, failed,
    review), de-duplicated and capped;
  - the last few lines of output, which is usually the step's own result.

Exits with the command's own exit code. Used when Chris hands the remaining
steps to Claude (docs/production-pipeline.md, "Logging each step"); his own
runs keep the verbose command file unchanged.
"""

import argparse
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

PROBLEM = re.compile(r"\b(error|warning|traceback|exception|failed|review)\b", re.IGNORECASE)
MAX_PROBLEMS = 15
TAIL_LINES = 6
MAX_LINE = 200


def visible_lines(text):
    """Split output into lines as a terminal would show them: a carriage-return
    progress bar keeps only its final state."""
    lines = []
    for raw in text.replace("\r\n", "\n").split("\n"):
        line = raw.rsplit("\r", 1)[-1].rstrip()
        if line:
            lines.append(line[:MAX_LINE])
    return lines


def summarise(title, code, seconds, text):
    lines = visible_lines(text)
    status = "OK" if code == 0 else "FAILED"
    out = [f"=== {title} === -> {status} (exit {code}, {seconds:.1f}s)"]
    seen, problems = set(), []
    for line in lines:
        if PROBLEM.search(line) and line not in seen:
            seen.add(line)
            problems.append(line)
    if problems:
        out.append("problem lines:")
        out += ["  " + p for p in problems[:MAX_PROBLEMS]]
        if len(problems) > MAX_PROBLEMS:
            out.append(f"  (+{len(problems) - MAX_PROBLEMS} more in the log)")
    if lines:
        out.append("last lines:")
        out += ["  " + line for line in lines[-TAIL_LINES:]]
    return "\n".join(out)


def bash_time(seconds):
    return f"{int(seconds // 60)}m{seconds % 60:.3f}s"


def run(log_path, title, cmd):
    log_path = Path(log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    chunks = []
    with open(log_path, "ab") as log:
        header = f"\n{datetime.now().astimezone():%a %b %d %H:%M:%S %Z %Y}\n=== {title} ===\n$ {' '.join(cmd)}\n\n"
        log.write(header.encode("utf8"))
        log.flush()
        start = time.monotonic()
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        except OSError as e:
            data = f"{e}\n".encode("utf8")
            log.write(data)
            chunks.append(data)
            code = 127
        else:
            for chunk in iter(lambda: proc.stdout.read1(65536), b""):
                log.write(chunk)
                log.flush()
                chunks.append(chunk)
            code = proc.wait()
        seconds = time.monotonic() - start
        log.write(f"\nreal\t{bash_time(seconds)}\n\n".encode("utf8"))
    text = b"".join(chunks).decode("utf8", errors="replace")
    return code, summarise(title, code, seconds, text)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("log")
    ap.add_argument("title")
    ap.add_argument("cmd", nargs=argparse.REMAINDER)
    args = ap.parse_args(argv)
    cmd = args.cmd[1:] if args.cmd[:1] == ["--"] else args.cmd
    if not cmd:
        ap.error("no command given after --")
    code, summary = run(args.log, args.title, cmd)
    print(summary)
    return code


if __name__ == "__main__":
    sys.exit(main())
