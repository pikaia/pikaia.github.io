#!/usr/bin/env bash
# Undo scripts/publish-early.sh: restore a post's scheduled `date:` and
# remove the temporary `permalink:` / `scheduled_date:` front-matter keys,
# then commit + push.
#
#   scripts/publish-early-reset.sh [-f] <slug-or-path>
#
# The live URL does not change: publish-early.sh pinned `permalink:` to the
# URL the scheduled date produces, so dropping the pin and restoring the
# date leave the address exactly where it was.
#
# Run this AFTER the scheduled date has passed. If you run it while the
# scheduled date is still in the future, the post will drop off the live
# site until that date arrives, because GitHub Pages does not build
# future-dated posts. The script refuses to do that unless you pass -f.
set -euo pipefail

cd "$(dirname "$0")/.."

force=0
arg=""
for a in "$@"; do
  case "$a" in
    -f|--force) force=1 ;;
    *) arg="$a" ;;
  esac
done
if [ -z "$arg" ]; then
  echo "usage: scripts/publish-early-reset.sh [-f] <slug-or-path>" >&2
  exit 1
fi

if [ -f "$arg" ]; then
  post="$arg"
else
  matches=(_posts/*"${arg%.md}"*.md)
  if [ ! -e "${matches[0]}" ]; then
    echo "no post under _posts/ matches '$arg'" >&2
    exit 1
  fi
  if [ "${#matches[@]}" -ne 1 ]; then
    printf 'ambiguous - %d posts match:\n' "${#matches[@]}" >&2
    printf '  %s\n' "${matches[@]}" >&2
    exit 1
  fi
  post="${matches[0]}"
fi

base="$(basename "$post")"
slug="${base:11}"; slug="${slug%.md}"

sched="$(sed -n 's/^scheduled_date:[[:space:]]*//p' "$post" | head -1 | tr -d '\r')"
if [ -z "$sched" ]; then
  echo "$post has no 'scheduled_date:' key - it is not in early-publish state." >&2
  exit 1
fi

now_epoch="$(date -u +%s)"
sched_epoch="$(date -u -d "$sched" +%s)"
if [ "$sched_epoch" -gt "$now_epoch" ] && [ "$force" -ne 1 ]; then
  echo "refusing: ${slug}'s scheduled date $sched is still in the future." >&2
  echo "Resetting now would REMOVE it from the live site until that date," >&2
  echo "because GitHub Pages does not build future-dated posts." >&2
  echo "Wait until after $sched, or re-run with -f if you really mean it." >&2
  exit 1
fi

echo "post:           $post"
echo "restoring date: $sched"

tmp="$(mktemp)"
awk -v sched="$sched" '
  NR==1 && $0=="---" { infm=1; print; next }
  infm && ($0=="---" || $0=="---\r") { infm=0; print; next }
  infm && /^date:/           { print "date: " sched; next }
  infm && /^scheduled_date:/ { next }
  infm && /^permalink:/      { next }
  { print }
' "$post" > "$tmp"
mv "$tmp" "$post"

git add -- "$post"
git commit -m "Restore scheduled date for ${slug} (${sched%% *})

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014vyi5DydGd12SnQWie299V"
git push

echo
echo "pushed. ${slug} is back on its scheduled date ${sched%% *} and stays at the same URL."
