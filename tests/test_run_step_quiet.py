import sys

import run_step_quiet as rsq


def _py(code):
    return [sys.executable, "-c", code]


def test_log_gets_the_full_block_and_console_gets_a_summary(tmp_path):
    log = tmp_path / "logs" / "post.log"
    code, summary = rsq.run(log, "5. Check smoothness", _py("for i in range(500): print('frame', i)\nprint('ALL SMOOTH')"))
    assert code == 0
    text = log.read_text(encoding="utf8")
    assert "=== 5. Check smoothness ===" in text
    assert "frame 0\n" in text and "frame 499" in text
    assert "\nreal\t0m" in text
    assert summary.startswith("=== 5. Check smoothness === -> OK (exit 0,")
    assert "ALL SMOOTH" in summary
    assert "frame 0" not in summary
    assert len(summary.splitlines()) <= 1 + 1 + rsq.TAIL_LINES


def test_appends_to_an_existing_log(tmp_path):
    log = tmp_path / "post.log"
    log.write_text("earlier step\n", encoding="utf8")
    rsq.run(log, "1.3 Verify", _py("print('12.5')"))
    assert log.read_text(encoding="utf8").startswith("earlier step\n")


def test_failure_surfaces_problem_lines_and_exit_code(tmp_path):
    code, summary = rsq.run(tmp_path / "p.log", "6. Render",
                            _py("import sys\nprint('WARNING: slide 3 short')\nprint('WARNING: slide 3 short')\nraise SystemExit(2)"))
    assert code == 2
    assert "FAILED (exit 2" in summary
    problems = summary.split("problem lines:")[1].split("last lines:")[0]
    assert problems.count("WARNING: slide 3 short") == 1


def test_progress_bar_keeps_only_its_final_state():
    assert rsq.visible_lines("  10%\r  50%\r 100% done\nnext\n\n") == [" 100% done", "next"]


def test_missing_command_is_reported_not_raised(tmp_path):
    code, summary = rsq.run(tmp_path / "p.log", "x", ["no-such-command-xyz"])
    assert code == 127
    assert "FAILED" in summary


def test_main_strips_the_double_dash(tmp_path, capsys):
    code = rsq.main([str(tmp_path / "p.log"), "2. Insert", "--", *_py("print('done')")])
    assert code == 0
    assert "done" in capsys.readouterr().out


def test_problem_words_match_whole_words_only():
    assert rsq.PROBLEM.search("[REVIEW CREDIT] slide 4")
    assert rsq.PROBLEM.search("Traceback (most recent call last):")
    assert not rsq.PROBLEM.search("No unreviewed letter-spelled words found")
