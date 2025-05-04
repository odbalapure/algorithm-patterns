## Sliding Window Variable Size

This is a variation of sliding window, where we don't have a fixed window size and need to keep expanding our window as long as our window meets a certain constraint.

## Use Case

- Find the maximum length subarray with same value in each position.
- Find the minimum length subarray with sum >= target.

## Example

### Find length of longest subarray with same values

```python
def longest_subaray_same_value(nums):
    max_length, L = 0, 0
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        max_length = max(max_length, R - L + 1)
    return max_length
```

### Find the minimum length subarray with sum >= target

```python
def min_subarray_sum_greater_equal_target(nums, target):
    L, min_length, total = 0, float("inf"), 0
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            min_length = min(min_length, R - L + 1)
            total -= nums[L]
            L += 1
    return 0 if min_length == float("inf") else min_length
```

## Complexity

### Time
Time taken is `O(N)` as we are making a single pass on the array

### Space
Space is `O(1)` as we are using variables to keep track of the pointers and sum