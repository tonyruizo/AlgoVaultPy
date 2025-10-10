from typing import Callable

import pytest
from algo_vault.leetcode.lc1480_running_sum.impl import IMPLEMENTATIONS

CASES = [([], []),
         ([5], [5]),
         ([1, 2, 3, 4], [1, 3, 6, 10]),
         ([1, -1, 2, -2], [1, 0, 2, 0])]


@pytest.mark.parametrize("impl", IMPLEMENTATIONS, ids=lambda f: f.__name__)
@pytest.mark.parametrize("arr, expected", CASES)
def test_all_impls(arr: list[int], expected: list[int], impl: Callable[[list[int]], list[int]]) -> None:
    original = arr.copy()
    assert impl(arr) == expected
    assert arr == original
