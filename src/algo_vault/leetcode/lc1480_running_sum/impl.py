from typing import Callable


def running_sum_v1(nums: list[int]) -> list[int]:
    """
    Returns runningSum[i] = sum(nums[0..i]) for each i.

    Parameters:
         nums: list[int]
    Returns:
        list[int]: An array of the running sum of nums.
    """
    result: list[int] = []
    total: int = 0

    for i in nums:
        total += i
        result.append(total)

    return result


def running_sum_comprehension(nums: list[int]) -> list[int]:
    total = 0
    return [total := total + i for i in nums]


"""
Implement Alternative Approach Function (for test):
"""

IMPLEMENTATIONS: list[Callable[[list[int]], list[int]]] = [running_sum_v1, running_sum_comprehension]
