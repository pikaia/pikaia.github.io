"""Build a Short's re-cut narration audio + timing from the full narration.

    python scripts/build_short_audio.py <slug> <i,j,k,...>

Reads audio/<slug>.mp3 and audio/<slug>.timing.json, extracts the listed
sentence indices (in the order given) with ffmpeg, joins them (via WAV
intermediates, re-encoded to MP3 so the cuts land exactly on the sentence
boundaries), and writes audio/<slug>-short.mp3 plus a re-based
audio/<slug>-short.timing.json carrying the same sentences in Short-local
time. A synopsis Short's config then points its TIMING_JSON at the short
timing file: watch_video_lib derives both the audio path and the burned
captions from it, so the Short's soundtrack is the re-cut, not a prefix
of the full narration.
"""

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    slug, index_arg = sys.argv[1], sys.argv[2]
    indices = [int(x) for x in index_arg.split(",")]
    audio_dir = Path("audio")
    mp3 = audio_dir / f"{slug}.mp3"
    timing = json.loads((audio_dir / f"{slug}.timing.json").read_text(encoding="utf-8"))
    sentences = timing if isinstance(timing, list) else timing["sentences"]

    picked = [sentences[i] for i in indices]
    out_timing = []
    cursor = 0.0
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for n, s in enumerate(picked):
            seg = Path(tmp) / f"seg{n:02d}.wav"
            subprocess.run(
                ["ffmpeg", "-y", "-v", "error", "-ss", f"{s['offset_s']:.3f}",
                 "-t", f"{s['duration_s']:.3f}", "-i", str(mp3), str(seg)],
                check=True)
            parts.append(seg)
            out_timing.append({"text": s["text"], "offset_s": round(cursor, 3),
                               "duration_s": s["duration_s"]})
            cursor += s["duration_s"]
        lst = Path(tmp) / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in parts), encoding="utf-8")
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
             "-acodec", "libmp3lame", "-q:a", "3", str(audio_dir / f"{slug}-short.mp3")],
            check=True)
    (audio_dir / f"{slug}-short.timing.json").write_text(
        json.dumps(out_timing, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(picked)} sentence(s), {cursor:.2f}s -> audio/{slug}-short.mp3 "
          f"+ audio/{slug}-short.timing.json")


if __name__ == "__main__":
    main()
