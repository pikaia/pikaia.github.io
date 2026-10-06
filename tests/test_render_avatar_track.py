import json
import subprocess
import types

from PIL import Image

import avatar_lib as al
import render_avatar_track as rat


def solid_layers(tmp_path, d=64):
    colours = {name: (0, 0, 0, 0) for name in al.LAYER_NAMES}
    colours.update({"body": (0, 0, 255, 255), "mouth-3": (255, 0, 0, 255), "mouth-F": (0, 255, 0, 255)})
    for name, c in colours.items():
        im = Image.new("RGBA", (d, d), (0, 0, 0, 0))
        if c[3]:
            box = (0, 0, d, d) if name == "body" else (d // 4, d // 2, 3 * d // 4, 3 * d // 4)
            im.paste(c, box)
        im.save(tmp_path / f"{name}.png")
    return tmp_path


def test_compose_stacks_mouth_on_body(tmp_path):
    layers = rat.load_layers(32, solid_layers(tmp_path))
    closed = rat.compose_avatar(layers, 0, False)
    wide = rat.compose_avatar(layers, 3, False)
    assert closed.getpixel((16, 20)) == (0, 0, 255, 255)
    assert wide.getpixel((16, 20)) == (255, 0, 0, 255)


def test_with_alpha_scales_only_alpha():
    im = Image.new("RGBA", (2, 2), (10, 20, 30, 200))
    assert rat.with_alpha(im, 0.5).getpixel((0, 0)) == (10, 20, 30, 100)
    assert rat.with_alpha(im, 1.0) is im


def test_blink_frame_set():
    assert rat.blink_frame_set([10, 50]) == {10, 11, 12, 50, 51, 52}


def fake_cfg(tmp_path, avatar=True):
    timing = tmp_path / "t.timing.json"
    track = {"version": 1, "fps": 25, "frames": 50, "duration_s": 2.0, "source": "x",
             "mouth": "0" * 10 + "3" * 40, "blinks": []}
    (tmp_path / "t.avatar.json").write_text(json.dumps(track), encoding="utf-8")
    kw = {"TOTAL_DURATION": 2.0, "TIMING_JSON": str(timing), "WIDTH": 320, "HEIGHT": 180}
    if avatar:
        kw["AVATAR"] = {"ranges": [(0.4, 1.6)], "size": 0.4, "margin": 0.05, "fade": 0.0}
    return types.SimpleNamespace(**kw)


def probe(path, entries):
    return subprocess.run(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
                           "-show_entries", f"stream={entries}", "-of", "csv=p=0", str(path)],
                          check=True, capture_output=True, text=True).stdout.strip()


def test_render_track_frames_and_alpha(tmp_path):
    png_dir = tmp_path / "png"
    png_dir.mkdir()
    solid_layers(png_dir)
    out = tmp_path / "a.mov"
    assert rat.render_track(fake_cfg(tmp_path), out, png_dir) is True
    info = probe(out, "pix_fmt,nb_read_frames")
    assert info == "argb,50"
    frame = tmp_path / "f.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(out), "-vf", "select=eq(n\\,30)",
                    "-frames:v", "1", str(frame)], check=True)
    im = Image.open(frame).convert("RGBA")
    assert im.size == (72, 72)                     # 0.4 * 180
    assert im.getpixel((36, 4))[3] == 255          # visible inside the range
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(out), "-vf", "select=eq(n\\,2)",
                    "-frames:v", "1", str(frame)], check=True)
    assert Image.open(frame).convert("RGBA").getpixel((36, 4))[3] == 0   # transparent before it


def test_render_track_skips_without_avatar(tmp_path):
    assert rat.render_track(fake_cfg(tmp_path, avatar=False), tmp_path / "a.mov") is False
    assert not (tmp_path / "a.mov").exists()


def test_default_track_path():
    from pathlib import Path
    assert rat.default_track_path(Path("scripts/video-configs/foo.py")) == al.REPO_ROOT / "preview-motion/foo-avatar.mov"


def test_mouth_layer_for():
    # Quiet sounds (the hiss of f, the closure of m/b) read as silent to the
    # loudness meter; a shape only exists inside a spoken sound, so it wins.
    assert rat.mouth_layer_for(0, "F") == "mouth-F"
    assert rat.mouth_layer_for(0, ".") == "mouth-0"       # a real pause stays closed
    assert rat.mouth_layer_for(2, "F") == "mouth-F"
    assert rat.mouth_layer_for(2, ".") == "mouth-2"
    assert rat.mouth_layer_for(3, "M") == "mouth-M"


def test_compose_accepts_layer_name(tmp_path):
    layers = rat.load_layers(32, solid_layers(tmp_path))
    assert rat.compose_avatar(layers, "mouth-F", False).getpixel((16, 20)) == (0, 255, 0, 255)


def _track_cfg(tmp_path, **track_over):
    timing = tmp_path / "t.timing.json"
    track = {"version": 1, "fps": 25, "frames": 50, "duration_s": 2.0, "source": "x",
             "mouth": "3" * 50, "blinks": []}
    track.update(track_over)
    (tmp_path / "t.avatar.json").write_text(json.dumps(track), encoding="utf-8")
    return types.SimpleNamespace(TOTAL_DURATION=2.0, TIMING_JSON=str(timing), WIDTH=320, HEIGHT=180,
                                 AVATAR={"ranges": [(0, None)], "size": 0.4, "margin": 0.05, "fade": 0.0})


def _frame_rgb(path, n, tmp_path):
    f = tmp_path / f"f{n}.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-vf", f"select=eq(n\\,{n})",
                    "-frames:v", "1", str(f)], check=True)
    return Image.open(f).convert("RGBA").getpixel((36, 45))      # inside the mouth box at 72 px


def test_render_v2_track_uses_shapes(tmp_path):
    png = tmp_path / "png"
    png.mkdir()
    solid_layers(png)
    cfg = _track_cfg(tmp_path, version=2, shape="F" * 25 + "." * 25, shape_fallback=[])
    out = tmp_path / "a.mov"
    rat.render_track(cfg, out, png)
    assert _frame_rgb(out, 10, tmp_path)[:3] == (0, 255, 0)      # shape F wins over level 3
    assert _frame_rgb(out, 40, tmp_path)[:3] == (255, 0, 0)      # no shape -> level 3


def test_render_v1_track_uses_levels_only(tmp_path):
    png = tmp_path / "png"
    png.mkdir()
    solid_layers(png)
    out = tmp_path / "a.mov"
    rat.render_track(_track_cfg(tmp_path), out, png)
    assert _frame_rgb(out, 10, tmp_path)[:3] == (255, 0, 0)


def test_hold_keys_absorbs_short_runs():
    keys = list("aaabbaaaccccd")
    assert rat.hold_keys(keys, 1) == keys
    assert rat.hold_keys(keys, 3) == list("aaaaaaaacccc" + "c")


def test_hold_keys_keeps_first_frame():
    assert rat.hold_keys(list("ab"), 3) == list("aa")


def frame_px(out, n, xy, tmp_path):
    frame = tmp_path / f"f{n}.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(out), "-vf", f"select=eq(n\\,{n})",
                    "-frames:v", "1", str(frame)], check=True)
    return Image.open(frame).convert("RGBA").getpixel(xy)[:3]


def test_render_track_photo_style_eases_between_mouths(tmp_path):
    png_dir = tmp_path / "png"
    png_dir.mkdir()
    solid_layers(png_dir)
    cfg = fake_cfg(tmp_path)
    cfg.AVATAR = {"ranges": [(0, 2.0)], "size": 0.4, "margin": 0.05, "fade": 0.0,
                  "style": "photo", "ease": 0.5, "hold": 1}
    out = tmp_path / "a.mov"
    assert rat.render_track(cfg, out, png_dir) is True
    # the mouth switches from closed (body blue shows) to wide (red) at frame 10
    assert frame_px(out, 9, (36, 50), tmp_path) == (0, 0, 255)
    r, _, b = frame_px(out, 10, (36, 50), tmp_path)
    assert 100 < r < 160 and 100 < b < 160          # halfway, not a hard cut
    assert frame_px(out, 30, (36, 50), tmp_path) == (255, 0, 0)
