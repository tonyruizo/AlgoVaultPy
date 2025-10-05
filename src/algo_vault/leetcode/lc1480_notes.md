# LC1480 – Running Sum of 1d Array

**Source:** https://leetcode.com/problems/running-sum-of-1d-array/  
**Tags:** arrays, prefix-sum  
**Difficulty:** Easy

## Complexity
- Time: O(n)
- Space: O(n) 

## Edge Cases
- Empty: `[] → []`
- Single element: `[5] → [5]`
- Mixed signs: `[1, -1, 2, -2] → [1, 0, 2, 0]`

## Tests Covered
- `test_empty_returns_empty` (empty list)
- `test_inputs` (includes the problem’s sample and mixed signs)

## Alternatives / Notes
- In-place prefix sum if mutation is allowed.
- For streams, maintain running total only.

