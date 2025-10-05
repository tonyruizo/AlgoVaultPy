"""

1480:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example:
Input: nums = [1,2,3,4]
Output: [1, 3, 6, 10]
Explanation: Running sum is obtained as follows: [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4].

"""


def running_sum(nums: list[int]) -> list[int]:
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
