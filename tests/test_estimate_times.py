"""The step-time estimate parses logs and scales rates sensibly."""
from datetime import datetime

import estimate_times as e
from make_command_file import TEMPLATE

LOG = """
=== 6. Render the main video ===
rendering 15000 frames across 3 workers
real\t15m0.000s

=== 7.2 Render the Short ===
real\t1m40.000s

=== 8.1 Verify frame count (auto-covers the Short) ===
real\t0m28.000s

=== 8.4 Compress the Short for upload ===
real\t0m8.000s
"""


def test_step_keys_mark_short_steps_only():
    assert e.step_key("7.1 Check smoothness (Short)") == "7.1S"
    assert e.step_key("8.4 Compress the Short for upload") == "8.4S"
    assert e.step_key("7.2 Render the Short") == "7.2S"
    assert e.step_key("8.1 Verify frame count (auto-covers the Short)") == "8.1"
    assert e.step_key("5. Check smoothness and review the gap report") == "5"


def test_parse_log_reads_seconds_and_workers():
    runs = e.parse_log(LOG)
    assert runs[0] == ("6", 900.0, 3)
    assert runs[1] == ("7.2S", 100.0, None)


def test_render_scales_with_workers():
    rates = {"6": [4.0]}
    one = dict((k, t) for k, _, t in e.estimate("4-9", 600, 70, 1, rates))
    four = dict((k, t) for k, _, t in e.estimate("4-9", 600, 70, 4, rates))
    assert one["6"] == 2400 and four["6"] == 600


def test_no_avatar_skips_avatar_steps():
    keys = [k for k, _, _ in e.estimate("4-9", 600, 70, 2, {}, avatar=False)]
    assert "6a" not in keys and "6b" not in keys


def test_report_total_and_finish_time():
    out = e.report([("6", "Main video render", 1800), ("4", None, 2)], "hdr", now=datetime(2026, 1, 1, 20, 0))
    assert "~30 min" in out and "done around 8:30 PM" in out


def test_template_runs_estimates_before_each_group():
    text = TEMPLATE.read_text(encoding="utf-8")
    assert text.index("estimate_times.py {SLUG} 1") < text.index("=== 1.1 ")
    assert text.index("estimate_times.py {SLUG} 4-9") < text.index("=== 4. ")
