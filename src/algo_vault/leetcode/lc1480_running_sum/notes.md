# LC1480 – Running Sum of 1d Array

**Source:** https://leetcode.com/problems/running-sum-of-1d-array/  
**Tags:** arrays, prefix-sum  
**Difficulty:** Easy

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

**Example:**<br>
*Input*: nums = [1, 2, 3,4]<br>
*Output*: [1, 3, 6, 10]

Explanation: Running sum is obtained as follows: [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4].

## Edge Cases

- Empty: `[] -> []`
- Single element: `[5] -> [5]`
- Problem example: `[1, 2, 3, 4] -> [1, 3, 6, 10]`
- Mixed signs: `[1, -1, 2, -2] -> [1, 0, 2, 0]`

## Complexity

- Time: O(n)
- Space: O(n) 