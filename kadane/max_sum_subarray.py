def max_sum_subarray(nums):
    """
    Find max. sum subarray
    Time: O(N^2)
    Space: O(1)
    """
    max_sum = 0
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


print(max_sum_subarray([4, -1, 2, -7, 3, 4]))
