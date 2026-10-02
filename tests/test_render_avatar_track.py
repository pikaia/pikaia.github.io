import json
import subprocess
import types

from PIL import Image

import avatar_lib as al
import render_avatar_track as rat


def solid_layers(tmp_path, d=64):
    colours = {"body": (0, 0, 255, 255), "eyes-open": (0, 0, 0, 0), "eyes-closed": (0, 0, 0, 0),
               "mouth-0": (0, 0, 0, 0), "mouth-1": (0, 0, 0, 0), "mouth-2": (0, 0, 0, 0),
               "mouth-3": (255, 0, 0, 255)}
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
