"""Lowercase pronunciation fixes also cover the capitalised word (titles, sentence starts)."""
from generate_narration import PRONUNCIATION_OVERRIDES, lexicon_overrides


def test_lowercase_entry_gets_capitalised_copy():
    out = lexicon_overrides({"mall": "mˈɔːl"})
    assert out == {"mall": "mˈɔːl", "Mall": "mˈɔːl"}


def test_explicit_capitalised_entry_wins():
    out = lexicon_overrides({"wo": "wˈɔː", "Wo": "wˈQ"})
    assert out["Wo"] == "wˈQ"


def test_non_lowercase_keys_left_alone():
    out = lexicon_overrides({"Kuan": "kwˈɑːn", "PoW": "x"})
    assert out == {"Kuan": "kwˈɑːn", "PoW": "x"}


def test_every_real_lowercase_fix_is_covered_capitalised():
    out = lexicon_overrides()
    for k, v in PRONUNCIATION_OVERRIDES.items():
        if k.islower():
            assert (k[0].upper() + k[1:]) in out
    assert out["Graves"] == PRONUNCIATION_OVERRIDES["graves"]
