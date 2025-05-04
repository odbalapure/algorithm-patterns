def min_subarray_sum_greater_equal_target(nums, target):
    """
    Min. length subarray where sum >= target
    Assume that all values are positive
    Time: O(N)
    Space: O(1)
    """
    L, min_length, total = 0, float("inf"), 0
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            min_length = min(min_length, R - L + 1)
            total -= nums[L]
            L += 1
    return 0 if min_length == float("inf") else min_length


print(min_subarray_sum_greater_equal_target([2, 3, 1, 2, 4, 3], 6))  # [4, 3] = 7
