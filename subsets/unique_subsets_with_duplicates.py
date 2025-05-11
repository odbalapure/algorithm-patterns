def unique_subsets_with_duplicates(nums):
    """
    Given list of duplicate elements, return all possible distinct subsets
    Time: O(N * 2^N)
    Space: O(N)
    """
    nums.sort()
    curr_set, subsets = [], []
    helper(0, nums, curr_set, subsets)
    return subsets


def helper(i, nums, curr_set, subsets):
    if i >= len(nums):
        subsets.append(curr_set.copy())
        return

    curr_set.append(nums[i])
    helper(i + 1, nums, curr_set, subsets)

    curr_set.pop()
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    helper(i + 1, nums, curr_set, subsets)


print(
    unique_subsets_with_duplicates([1, 2, 3])
)  # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
