"""Chart slide: the live time readout and the x-axis tick options."""
from watch_video_lib import chart_time_label, compose_chart_frame


def test_year_label_rounds_to_whole_year():
    assert chart_time_label(2009.6) == "2010"
    assert chart_time_label(1943.2, "year") == "1943"


def test_month_label_reads_fractional_year():
    assert chart_time_label(1942.704, "month") == "Sep 1942"
    assert chart_time_label(1943.633, "month") == "Aug 1943"
    assert chart_time_label(1945.493, "month") == "Jun 1945"
    assert chart_time_label(1944.999, "month") == "Dec 1944"


def _slide(**extra):
    slide = {"type": "chart", "data": [(1942.7, 0), (1945.5, 30)],
             "x_range": (1942.5, 1945.75), "y_range": (0, 35), "y_tick_step": 5}
    slide.update(extra)
    return slide


def test_short_range_chart_renders_with_yearly_ticks_and_month_label():
    frame = compose_chart_frame(_slide(x_tick_step=1, time_label="month"), 320, 180, 0, 0.5)
    assert frame.size == (320, 180)


def test_yearly_ticks_draw_more_than_default():
    default = compose_chart_frame(_slide(), 320, 180, 0, 0.0)
    yearly = compose_chart_frame(_slide(x_tick_step=1), 320, 180, 0, 0.0)
    assert default.tobytes() != yearly.tobytes()
