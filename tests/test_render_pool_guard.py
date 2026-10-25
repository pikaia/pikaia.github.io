"""The multi-worker render stops with an error instead of hanging when a worker dies."""
import multiprocessing
import os

import pytest

from watch_video_lib import RenderPoolDied, _iter_pool_results, _pool_health


class FakeIt:
    """imap-style iterator: items, then TimeoutError forever (a stalled pool)."""
    def __init__(self, items):
        self.items = list(items)

    def next(self, timeout=None):
        if self.items:
            return self.items.pop(0)
        raise multiprocessing.TimeoutError


class Done(FakeIt):
    def next(self, timeout=None):
        if not self.items:
            raise StopIteration
        return super().next(timeout)


def test_passes_results_through():
    assert list(_iter_pool_results(Done([1, 2, 3]), lambda: None)) == [1, 2, 3]


def test_raises_when_health_check_fails():
    with pytest.raises(RenderPoolDied, match="worker died"):
        list(_iter_pool_results(FakeIt([1]), lambda: "a worker died"))


def test_raises_after_stall_with_healthy_pool():
    t = iter(range(0, 10_000, 100))
    with pytest.raises(RenderPoolDied, match="no frame arrived"):
        list(_iter_pool_results(FakeIt([]), lambda: None, stall=250, clock=lambda: next(t)))


def _die_on_three(i):
    if i == 3:
        os._exit(1)
    return i


def test_real_pool_with_killed_worker_is_detected():
    ctx = multiprocessing.get_context("spawn")
    with ctx.Pool(2) as pool:
        it = pool.imap(_die_on_three, range(8), chunksize=1)
        with pytest.raises(RenderPoolDied):
            list(_iter_pool_results(it, _pool_health(pool), poll=0.5, stall=30))
