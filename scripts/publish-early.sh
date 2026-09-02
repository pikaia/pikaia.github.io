#!/usr/bin/env bash
# Publish a future-dated post to the LIVE site now, without giving up the
# date it is scheduled for.
#
#   scripts/publish-early.sh <slug-or-path>
#
# Why this is needed: GitHub Pages builds from _config.yml, which has no
# `future:` setting, so a post whose `date:` is still ahead of the build
# clock is skipped entirely until that date arrives (the daily scheduled
# build then picks it up). That is the delay between committing a post and
# seeing it live.
#
# This script forces it live early:
#   * moves `date:` to the current time (now in the past, so Jekyll emits it)
#   * pins `permalink:` to the URL the scheduled date would have produced,
#     so the post's address does NOT move
#   * stashes the original date in a `scheduled_date:` front-matter key
#   * commits + pushes, which triggers a Pages build within a minute or two
#
# Undo it with:
#   scripts/publish-early-reset.sh <slug>
# which restores the scheduled `date:` and drops the `permalink:` /
# `scheduled_date:` keys. Because the permalink was pinned to the scheduled
# date, the live URL is identical before, during and after - so this is
# safe to run even after the video pipeline has baked the URL into a
# YouTube description.
#
# See also scripts/publish-now.sh, which is the other tool for this: it
# permanently moves a far-future post to today and renames its file. Use
# publish-now.sh when you have decided the post should simply come out
# today; use publish-early.sh when you want it visible now but still
# "belonging" to its scheduled date.
set -euo pipefail

cd "$(dirname "$0")/.."

arg="${1:-}"
if [ -z "$arg" ]; then
  echo "usage: scripts/publish-early.sh <slug-or-path>" >&2
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

base="$(basename "$post")"                 # 2026-09-08-some-slug.md
slug="${base:11}"; slug="${slug%.md}"      # some-slug

if grep -qE '^scheduled_date:' "$post"; then
  echo "$post already looks published-early (it has a scheduled_date: key)." >&2
  echo "Run scripts/publish-early-reset.sh $slug first if you want to redo it." >&2
  exit 1
fi
if grep -qE '^permalink:' "$post"; then
  echo "$post already has an explicit permalink: line - refusing to touch it." >&2
  echo "Sort this one out by hand." >&2
  exit 1
fi

cur="$(sed -n 's/^date:[[:space:]]*//p' "$post" | head -1 | tr -d '\r')"
if [ -z "$cur" ]; then
  echo "no 'date:' line in $post" >&2
  exit 1
fi

now_epoch="$(date -u +%s)"
cur_epoch="$(date -u -d "$cur" +%s)"

if [ "$cur_epoch" -le "$now_epoch" ]; then
  echo "$post is already dated in the past - nothing to stash."
  echo "Pushing an empty commit to trigger a fresh Pages build."
  git commit --allow-empty -m "Trigger Pages build for ${slug}

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014vyi5DydGd12SnQWie299V"
  git push
  echo
  echo "pushed. live in a few minutes."
  exit 0
fi

url="/$(date -u -d "$cur" '+%Y/%m/%d')/${slug}/"
now="$(date -u '+%Y-%m-%d %H:%M:%S') +0000"

echo "post:             $post"
echo "scheduled date:   $cur"
echo "pinned permalink: $url"
echo "temporary date:   $now"

tmp="$(mktemp)"
awk -v now="$now" -v sched="$cur" -v url="$url" '
  NR==1 && $0=="---" { infm=1; print; next }
  infm && ($0=="---" || $0=="---\r") { infm=0; print; next }
  infm && /^date:/ && !seen {
    seen=1
    print "date: " now
    print "scheduled_date: " sched
    print "permalink: " url
    next
  }
  { print }
' "$post" > "$tmp"
mv "$tmp" "$post"

git add -- "$post"
git commit -m "Publish ${slug} early (scheduled ${cur%% *})

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014vyi5DydGd12SnQWie299V"
git push

echo
echo "pushed. live in a few minutes at:"
echo "  https://pikaia.github.io${url}"
echo
echo "once the scheduled date ${cur%% *} has passed, run:"
echo "  scripts/publish-early-reset.sh ${slug}"
echo "(resetting BEFORE that date removes the post from the live site"
echo " until the date arrives - pass -f only if you really mean to.)"
