"""Insert the "Listen" audio-narration widget into a post, right after the
first back-link, matching the placement used on the chopsticks post.

Local dev tool only - not part of the deployed Jekyll site.

Usage:
    python scripts/insert_listen_widget.py _posts/<file>.md <slug>
"""
import sys

BACK_LINK_LINE = "[← Back to all posts](/)"

WIDGET_TEMPLATE = '''<div id="listen-widget" role="button" tabindex="0" aria-label="Play audio narration of this post" style="display: inline-flex; flex-direction: column; align-items: center; cursor: pointer; gap: 0.2em; margin: 0.5em 0 1.5em 0; user-select: none;">
  <span id="listen-icon" aria-hidden="true" style="display: inline-flex; align-items: center; justify-content: center; width: 2.4em; height: 2.4em; border-radius: 50%; border: 1px solid #888; font-size: 1.3em;">&#127911;</span>
  <span style="font-size: 0.7em; text-transform: uppercase; letter-spacing: 0.05em; opacity: 0.75;">Listen</span>
  <audio id="listen-audio" preload="none" style="display: none;">
    <source src="/audio/{slug}.mp3" type="audio/mpeg">
  </audio>
</div>

<script>
(function () {{
  var widget = document.getElementById('listen-widget');
  var icon = document.getElementById('listen-icon');
  var audio = document.getElementById('listen-audio');

  function setIcon(playing) {{
    icon.innerHTML = playing ? '&#10074;&#10074;' : '&#127911;';
  }}

  function toggle() {{
    if (audio.paused) {{
      audio.play();
    }} else {{
      audio.pause();
    }}
  }}

  widget.addEventListener('click', toggle);
  widget.addEventListener('keydown', function (e) {{
    if (e.key === 'Enter' || e.key === ' ') {{
      e.preventDefault();
      toggle();
    }}
  }});
  audio.addEventListener('play', function () {{ setIcon(true); }});
  audio.addEventListener('pause', function () {{ setIcon(false); }});
  audio.addEventListener('ended', function () {{ setIcon(false); }});
}})();
</script>'''


def main() -> None:
    post_path, slug = sys.argv[1], sys.argv[2]
    with open(post_path, "r", encoding="utf-8") as f:
        text = f.read()

    if 'id="listen-widget"' in text:
        print(f"SKIP (already has widget): {post_path}")
        return

    idx = text.find(BACK_LINK_LINE)
    if idx == -1:
        print(f"SKIP (no back-link found): {post_path}")
        return

    insert_at = idx + len(BACK_LINK_LINE)
    widget = WIDGET_TEMPLATE.format(slug=slug)
    new_text = text[:insert_at] + "\n\n" + widget + text[insert_at:]

    with open(post_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"OK: {post_path}")


if __name__ == "__main__":
    main()
