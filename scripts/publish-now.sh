#!/usr/bin/env bash
# Publish a post immediately, instead of waiting for its future date or
# the daily scheduled Pages build.
#
#   scripts/publish-now.sh <slug-or-path>
#
# Behaviour:
#   * Already past its date  -> just pushes an empty commit to trigger a
#     Pages rebuild. Nothing about the post changes.
#   * Dated later today / tomorrow (its calendar day has already begun in
#     UTC) -> sets `date:` to 08:00 +0800 of that same day (= 00:00 UTC),
#     which is in the past now. The filename, permalink and gallery link
#     are untouched.
#   * Dated two or more days out -> sets `date:` to the current UTC clock
#     time labelled +0800, renames the post file to today's date, and
#     fixes the companion gallery's `post_url`.
#
# GitHub Pages builds in UTC with no `timezone:` set, so a post's
# permalink day is the UTC date of its `date:` field - that's why the
# same-day case pins the time to 08:00 +0800 (midnight UTC).
#
# NOTE: if a post has already been through the video pipeline its
# permalink is probably referenced in a YouTube description; publishing
# it "now" won't move the day in that case (the same-day branch), but do
# not run this on a post dated far enough ahead to trigger the rename
# unless you also update those external links.
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
  echo "usage: scripts/publish-now.sh [-f] <slug-or-path>" >&2
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

base="$(basename "$post")"                 # 2026-09-05-some-slug.md
old_date="${base:0:10}"                    # 2026-09-05
slug="${base:11}"; slug="${slug%.md}"      # some-slug

cur="$(sed -n 's/^date:[[:space:]]*//p' "$post" | head -1)"
if [ -z "$cur" ]; then
  echo "no 'date:' line in $post" >&2
  exit 1
fi

now_epoch="$(date -u +%s)"
cur_epoch="$(date -u -d "$cur" +%s)"
day8="${cur:0:10} 08:00:00 +0800"
day8_epoch="$(date -u -d "$day8" +%s)"

echo "post:      $post"
echo "date now:  $cur"

if [ "$cur_epoch" -le "$now_epoch" ]; then
  echo "already past its date - triggering a rebuild only."
  git commit --allow-empty -m "Trigger Pages build for ${slug}

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014vyi5DydGd12SnQWie299V"
  git push
  echo
  echo "pushed. live in a few minutes."
  exit 0
fi

changed=("$post")
if [ "$day8_epoch" -le "$now_epoch" ]; then
  new="$day8"
  new_date="$old_date"
  echo "new date:  $new   (same day, permalink unchanged)"
else
  if [ "$force" -ne 1 ] && grep -qE 'youtu\.be/|youtube\.com/' "$post"; then
    echo "refusing: this would move the permalink from /$old_date/ to today, but the" >&2
    echo "post has a Watch widget with YouTube links - the video descriptions almost" >&2
    echo "certainly point at the /$old_date/ URL. Wait for the scheduled build, or" >&2
    echo "re-run with -f if you have updated those links." >&2
    exit 1
  fi
  new="$(date -u '+%Y-%m-%d %H:%M:%S') +0800"
  new_date="${new:0:10}"
  echo "new date:  $new   (moves to today, $old_date -> $new_date)"
fi

tmp="$(mktemp)"
awk -v d="$new" '
  NR==1 && $0=="---" { infm=1; print; next }
  infm && $0=="---"  { infm=0; print; next }
  infm && /^date:/             { print "date: " d; next }
  infm && /^last_modified_at:/ { print "last_modified_at: " d; next }
  { print }
' "$post" > "$tmp"
mv "$tmp" "$post"

if [ "$new_date" != "$old_date" ]; then
  new_post="_posts/${new_date}-${slug}.md"
  git mv "$post" "$new_post"
  echo "renamed:   -> $new_post"
  post="$new_post"; changed=("$new_post")
  gallery="_gallery/${slug}.md"
  if [ -f "$gallery" ]; then
    o="${old_date//-/\/}"; n="${new_date//-/\/}"
    sed -i "s#/${o}/${slug}/#/${n}/${slug}/#g" "$gallery"
    echo "gallery:   /$o/ -> /$n/ in $gallery"
    changed+=("$gallery")
  fi
fi

git add -- "${changed[@]}"
git commit -m "Publish ${slug} now

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_014vyi5DydGd12SnQWie299V"
git push

echo
echo "pushed. live in a few minutes at:"
echo "  https://pikaia.github.io/${new_date//-/\/}/${slug}/"
