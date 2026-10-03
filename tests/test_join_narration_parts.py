import subprocess
import sys
from pathlib import Path

import pytest

import join_narration_parts as jnp


def _tone(path, seconds):
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"sine=frequency=220:d={seconds}",
                    "-c:a", "libmp3lame", str(path)], check=True)


def _dur(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True, check=True).stdout
    return float(out)


def test_no_parts_is_a_harmless_no_op(tmp_path, capsys):
    out = tmp_path / "post.mp3"
    _tone(out, 1)
    before = out.read_bytes()
    assert jnp.join(out) is False
    assert out.read_bytes() == before
    assert "nothing to join" in capsys.readouterr().out


def test_parts_are_found_in_numeric_order(tmp_path):
    for n in (10, 2, 1):
        (tmp_path / f"post.part{n}.mp3").write_bytes(b"")
    assert [p.name for p in jnp.find_parts(tmp_path / "post.mp3")] == ["post.part1.mp3", "post.part2.mp3", "post.part10.mp3"]


def test_joins_parts_into_the_narration(tmp_path):
    _tone(tmp_path / "post.part1.mp3", 1)
    _tone(tmp_path / "post.part2.mp3", 2)
    assert jnp.join(tmp_path / "post.mp3") is True
    assert abs(_dur(tmp_path / "post.mp3") - 3) < 0.2


def test_refuses_to_overwrite_an_existing_narration(tmp_path):
    _tone(tmp_path / "post.mp3", 1)
    _tone(tmp_path / "post.part1.mp3", 2)
    with pytest.raises(SystemExit, match="--force"):
        jnp.join(tmp_path / "post.mp3")
    assert jnp.join(tmp_path / "post.mp3", force=True) is True
    assert abs(_dur(tmp_path / "post.mp3") - 2) < 0.2


def test_cli_no_parts_exits_zero(tmp_path):
    r = subprocess.run([sys.executable, "scripts/join_narration_parts.py", str(tmp_path / "post.mp3")],
                       capture_output=True, text=True)
    assert r.returncode == 0 and "nothing to join" in r.stdout
    assert not Path(tmp_path / "post.mp3").exists()
