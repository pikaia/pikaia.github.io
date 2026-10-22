"""make_pronunciation_samples: each candidate gets its own take, and with the
voice clone on only the cloned audio comes back."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import make_pronunciation_samples as mps  # noqa: E402


class _Lexicon:
    def __init__(self):
        self.golds = {}


class _G2P:
    def __init__(self):
        self.lexicon = _Lexicon()


class _Pipe:
    def __init__(self):
        self.g2p = _G2P()


def _fake_synth(pipe, sentence, voice):
    # The take records which reading was in the lexicon when it was made.
    return "george:" + pipe.g2p.lexicon.golds["TOPACS"]


def test_each_candidate_is_voiced_with_its_own_reading(monkeypatch):
    monkeypatch.setattr(mps.gn, "_synth_one", _fake_synth)
    takes = mps.synth_samples(_Pipe(), "TOPACS", "at TOPACS.", {"A": "a1", "B": "b2"},
                              "bm_george", clone=False)
    assert takes == {"A": "george:a1", "B": "george:b2"}


def test_clone_returns_only_the_cloned_audio(monkeypatch):
    monkeypatch.setattr(mps.gn, "_synth_one", _fake_synth)
    seen = {}

    def fake_clone(sentences, george, paths, ref, use_cache=True):
        seen["george"], seen["use_cache"] = george, use_cache
        return [g.replace("george", "clone") for g in george]

    takes = mps.synth_samples(_Pipe(), "TOPACS", "at TOPACS.", {"A": "a1", "B": "b2"},
                              "bm_george", clone_fn=fake_clone)
    assert takes == {"A": "clone:a1", "B": "clone:b2"}
    assert seen == {"george": ["george:a1", "george:b2"], "use_cache": False}
