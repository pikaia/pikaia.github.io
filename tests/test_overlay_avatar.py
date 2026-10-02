import subprocess
import types

import pytest
from PIL import Image

import overlay_avatar as oa


def make_main(path, audio=True):
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=0x00ff00:s=320x180:r=25:d=2"]
    if audio:
        cmd += ["-f", "lavfi", "-i", "sine=frequency=220:d=2", "-c:a", "aac"]
    cmd += ["-c:v", "libx264", "-pix_fmt", "yuv420p", str(path)]
    subprocess.run(cmd, check=True)


def make_track(path):
    # 72x72 opaque red bubble, all 50 frames.
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "color=c=0xff0000:s=72x72:r=25:d=2",
                    "-vf", "format=argb", "-c:v", "qtrle", "-pix_fmt", "argb", str(path)], check=True)


def cfg():
    return types.SimpleNamespace(TOTAL_DURATION=2.0, TIMING_JSON="audio/x.timing.json", WIDTH=320, HEIGHT=180,
                                 AVATAR={"ranges": [(0, None)], "size": 0.4, "margin": 0.05})


def grab(path, n, tmp_path):
    f = tmp_path / f"g{n}.png"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-vf", f"select=eq(n\\,{n})",
                    "-frames:v", "1", str(f)], check=True)
    return Image.open(f).convert("RGB")


def test_build_overlay_cmd_keeps_audio_optional():
    cmd = oa.build_overlay_cmd("in.mp4", "a.mov", "out.mp4", 10, 20)
    assert "0:a?" in cmd and "-c:a" in cmd and "copy" in cmd
    assert any("overlay=x=10:y=20" in c for c in cmd)


def test_overlay_places_bubble(tmp_path):
    main, track, out = tmp_path / "m.mp4", tmp_path / "a.mov", tmp_path / "o.mp4"
    make_main(main)
    make_track(track)
    assert oa.overlay(cfg(), main, track, out) is True
    im = grab(out, 25, tmp_path)
    # bottom-right: d=72, m=9 -> x=239, y=99; centre ~ (275, 135)
    r, g, b = im.getpixel((275, 135))
    assert r > 200 and g < 60
    r, g, b = im.getpixel((40, 40))
    assert g > 200 and r < 60
    streams = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=codec_type",
                              "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout.split()
    assert streams.count("audio") == 1


def test_overlay_without_audio(tmp_path):
    main, track, out = tmp_path / "m.mp4", tmp_path / "a.mov", tmp_path / "o.mp4"
    make_main(main, audio=False)
    make_track(track)
    assert oa.overlay(cfg(), main, track, out) is True
    assert out.exists()


def test_overlay_refuses_in_equals_out(tmp_path):
    main = tmp_path / "m.mp4"
    make_main(main)
    with pytest.raises(ValueError, match="overwrite"):
        oa.overlay(cfg(), main, tmp_path / "a.mov", main)


def test_overlay_missing_track_names_step(tmp_path):
    main = tmp_path / "m.mp4"
    make_main(main)
    with pytest.raises(FileNotFoundError, match="6a"):
        oa.overlay(cfg(), main, tmp_path / "nope.mov", tmp_path / "o.mp4")


def test_overlay_skips_without_avatar(tmp_path):
    c = cfg()
    del c.AVATAR
    assert oa.overlay(c, tmp_path / "m.mp4", tmp_path / "a.mov", tmp_path / "o.mp4") is False
