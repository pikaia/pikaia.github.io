import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from retime_video_config import boundary_map, retime_source  # noqa: E402

OLD = [{"text": "A.", "offset_s": 0.0, "duration_s": 3.45},
       {"text": "B.", "offset_s": 3.45, "duration_s": 14.6},
       {"text": "C.", "offset_s": 18.05, "duration_s": 5.0}]
NEW = [{"text": "A.", "offset_s": 0.0, "duration_s": 3.45},
       {"text": "B.", "offset_s": 3.45, "duration_s": 15.0},
       {"text": "C.", "offset_s": 18.45, "duration_s": 5.0}]


def test_maps_schedule_and_total_end():
    src = 'X = 1\nSCHEDULE = [(0.0, 0), (3.45, 1), (18.05, 2)]\nTOTAL_DURATION = 23.05\n'
    out = retime_source(src, boundary_map(OLD, NEW))
    assert "SCHEDULE = [(0.0, 0), (3.45, 1), (18.45, 2)]" in out
    assert "TOTAL_DURATION = 23.45" in out


def test_short_total_on_a_sentence_start_and_multiline_schedule():
    src = 'SCHEDULE = [\n    (0.0, 0),\n    (3.45, 1),\n]\nTOTAL_DURATION = 18.05\n'
    out = retime_source(src, boundary_map(OLD, NEW))
    assert "    (3.45, 1)," in out and "TOTAL_DURATION = 18.45" in out


def test_refuses_off_boundary_time():
    with pytest.raises(ValueError):
        retime_source("SCHEDULE = [(0.0, 0), (5.0, 1)]\nTOTAL_DURATION = 23.05\n", boundary_map(OLD, NEW))


def test_refuses_changed_text():
    with pytest.raises(ValueError):
        boundary_map(OLD, NEW[:2] + [{"text": "D.", "offset_s": 18.45, "duration_s": 5.0}])
