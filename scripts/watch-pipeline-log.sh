#!/usr/bin/env bash
# Tail a post's pipeline log (docs/production-pipeline.md's logging
# convention) and emit one line per completed step, plus a separate line
# for any failure - meant to be armed as a Claude Code Monitor watch, so
# Claude gets notified as each manual pipeline step finishes instead of
# needing to be told "step N done" after every one.
#
# Usage:
#   scripts/watch-pipeline-log.sh <slug>
#
# Only starts from the current end of the log (tail -n0), so steps
# already run before this is armed don't replay as events.
set -euo pipefail

slug="${1:?usage: watch-pipeline-log.sh <slug>}"
log="logs/${slug}.log"

if [ ! -f "$log" ]; then
    echo "no log yet at $log - it's created by the first pipeline step you run" >&2
    exit 1
fi

tail -n0 -f "$log" | awk '
  /^=== /            { hdr = $0 }
  /^real[[:space:]]/ { print hdr " -> done (" $0 ")"; fflush() }
  tolower($0) ~ /error|traceback|exception|failed/ {
                        print "FAILURE in " hdr ": " $0; fflush()
                      }
'
