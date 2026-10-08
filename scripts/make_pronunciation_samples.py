"""Synthesize ear-pick samples for a word's candidate pronunciations.

Each candidate is written to scratch/<slug>-<key>/<name>.wav, spoken in the
sentence given, in the narration voice. The candidate phonemes go straight
into the pipeline's lexicon (pipeline.g2p.lexicon.golds) before each take.
Setting PRONUNCIATION_OVERRIDES after the pipeline is built has no effect,
because _build_pipeline() copies the overrides into the lexicon once; ad hoc
sample scripts that did that produced identical takes for every candidate
(found on the Endau post's "katis", 2026-10-09).

    python scripts/make_pronunciation_samples.py <slug> <key> <word> "<sentence>" NAME=PHONEMES [NAME=PHONEMES ...]

Example:
    python scripts/make_pronunciation_samples.py new-syonan-the-endau-settlement-1943 katis katis \\
        "Each settler got 18 katis of rice." A-catty=kˈatiz B-car=kˈɑːtiz
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_narration as gn  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def parse_candidates(items):
    out = {}
    for item in items:
        name, sep, ph = item.partition("=")
        if not sep or not name or not ph:
            raise SystemExit(f"bad candidate {item!r}: expected NAME=PHONEMES")
        out[name] = ph
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("slug")
    ap.add_argument("key", help="folder suffix, e.g. the word in lower case")
    ap.add_argument("word", help="the token as it appears after rewrites, e.g. Po-Leung-Kok")
    ap.add_argument("sentence")
    ap.add_argument("candidates", nargs="+", help="NAME=PHONEMES")
    ap.add_argument("--voice", default="bm_george")
    args = ap.parse_args()
    cands = parse_candidates(args.candidates)
    if args.word not in args.sentence:
        raise SystemExit(f"{args.word!r} does not appear in the sentence")
    import soundfile as sf
    out = ROOT / "scratch" / f"{args.slug}-{args.key}"
    out.mkdir(parents=True, exist_ok=True)
    pipe = gn._build_pipeline(gn._lang_code_for(args.voice))
    golds = pipe.g2p.lexicon.golds
    for name, ph in cands.items():
        golds[args.word] = ph
        audio = gn._synth_one(pipe, args.sentence, args.voice)
        sf.write(out / f"{name}.wav", audio, 24000)
        print(f"wrote {out / (name + '.wav')}  ({ph}, {len(audio) / 24000:.2f}s)")


if __name__ == "__main__":
    main()
