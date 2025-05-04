def longest_subarray_same_value(nums):
    """
    Longest subarray with same values
    Time: O(N)
    Space: O(1)
    """
    L, max_length = 0, 0
    for R in range(len(nums)):
        if nums[R] != nums[L]:
            L = R
        max_length = max(max_length, R - L + 1)
    return max_length


print(longest_subarray_same_value([1, 2, 2, 3, 3, 3, 3, 4, 4, 5]))  # 4
