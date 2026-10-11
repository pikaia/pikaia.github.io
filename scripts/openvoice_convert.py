"""Re-voice Kokoro sentences towards Chris's reference recording with the
OpenVoice v2 tone-colour converter (option A of
docs/superpowers/specs/2026-10-10-voice-clone-design.md).

Runs inside .venv-openvoice, never the main environment: generate_narration.py
--clone openvoice calls it as a subprocess with a manifest of
{"in": george.wav, "out": converted.wav} pairs. Output is resampled to 24 kHz,
Kokoro's rate, so the caller can splice it in place of the George audio.

    .venv-openvoice/Scripts/python -I scripts/openvoice_convert.py --ref REF.wav
        --manifest jobs.json --se-dir .narration-cache [--src-clips DIR]

Speaker embeddings are cached in --se-dir: Chris's (keyed on the reference
file's sha256) and George's (made once, from --src-clips).
"""
import argparse
import glob
import hashlib
import json
import os
import sys
import tempfile
import time


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", required=True)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--se-dir", required=True)
    ap.add_argument("--src-clips", help="folder of George wavs, used only when George's embedding isn't cached yet")
    ap.add_argument("--tau", type=float, default=0.3)
    args = ap.parse_args()

    os.environ.setdefault("HF_HUB_VERBOSITY", "error")
    import warnings
    warnings.simplefilter("ignore")
    import librosa
    import soundfile as sf
    import torch
    from huggingface_hub import hf_hub_download
    from openvoice.api import OpenVoiceBaseClass, ToneColorConverter

    cfg = hf_hub_download("myshell-ai/OpenVoiceV2", "converter/config.json")
    ck = hf_hub_download("myshell-ai/OpenVoiceV2", "converter/checkpoint.pth")
    # Upstream bug: ToneColorConverter passes enable_watermark on to a base
    # class that rejects it, so build through the base class, no watermark.
    conv = ToneColorConverter.__new__(ToneColorConverter)
    OpenVoiceBaseClass.__init__(conv, cfg, device="cpu")
    conv.watermark_model = None
    conv.version = getattr(conv.hps, "_version_", "v1")
    conv.load_ckpt(ck)
    sr = conv.hps.data.sampling_rate
    os.makedirs(args.se_dir, exist_ok=True)
    # Chunks of Chris's recording are private: a temp folder, deleted on exit.
    tmp_dir = tempfile.TemporaryDirectory()
    tmp = tmp_dir.name

    ref_sha = hashlib.sha256(open(args.ref, "rb").read()).hexdigest()[:16]
    tgt_path = os.path.join(args.se_dir, f"openvoice-target-{ref_sha}.pt")
    if os.path.exists(tgt_path):
        tgt = torch.load(tgt_path)
    else:
        # The whole reading, in 10 s chunks.
        y, ysr = librosa.load(args.ref, sr=None)
        chunks = []
        for i in range(0, max(1, len(y) - 5 * ysr), 10 * ysr):
            p = os.path.join(tmp, f"ref-{i // ysr:04d}.wav")
            sf.write(p, y[i:i + 10 * ysr], ysr)
            chunks.append(p)
        tgt = conv.extract_se(chunks)
        torch.save(tgt, tgt_path)
    src_path = os.path.join(args.se_dir, "openvoice-george.pt")
    if os.path.exists(src_path):
        src = torch.load(src_path)
    else:
        clips = sorted(glob.glob(os.path.join(args.src_clips or "", "*.wav")))
        if not clips:
            sys.exit("openvoice_convert: George's embedding isn't cached; pass --src-clips")
        src = conv.extract_se(clips)
        # Cache it only when it rests on enough of George (a 3-sentence
        # test post would otherwise fix a weak embedding for good).
        if sum(sf.info(c).duration for c in clips) >= 60:
            torch.save(src, src_path)

    jobs = json.load(open(args.manifest, encoding="utf-8"))
    t0 = time.time()
    for n, job in enumerate(jobs, 1):
        audio = conv.convert(audio_src_path=job["in"], src_se=src, tgt_se=tgt, tau=args.tau)
        sf.write(job["out"], librosa.resample(audio, orig_sr=sr, target_sr=24000), 24000)
        sys.stderr.write("+")
        if n % 50 == 0 or n == len(jobs):
            sys.stderr.write(f" {n}/{len(jobs)} converted\n")
        sys.stderr.flush()
    tmp_dir.cleanup()
    print(f"openvoice_convert: {len(jobs)} sentence(s) in {time.time() - t0:.1f}s", file=sys.stderr)


if __name__ == "__main__":
    main()
