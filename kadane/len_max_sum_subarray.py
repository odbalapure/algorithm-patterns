def max_sum_subarray_length(nums):
    """
    Length of maximum sum subarray
    Time: O(N)
    Space: O(1)
    """
    max_sum = nums[0]
    curr_sum = 0
    max_l, max_r = 0, 0
    L = 0

    for R in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            L = R

        curr_sum += nums[R]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_l, max_r = L, R

    return [max_l, max_r]
