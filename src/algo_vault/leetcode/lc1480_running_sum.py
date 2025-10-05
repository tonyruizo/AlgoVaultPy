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
