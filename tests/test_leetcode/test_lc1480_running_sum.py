import pytest
from algo_vault.leetcode.lc1480_running_sum import running_sum


def test_empty_returns_empty():
    assert running_sum([]) == []

@pytest.mark.parametrize("arr, expected", [
    ([5], [5]),
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, -1, 2, -2], [1, 0, 2, 0]),
])
def test_inputs(arr, expected):
    assert running_sum(arr) == expected


