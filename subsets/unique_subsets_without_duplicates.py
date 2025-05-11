def unique_subsets_without_duplicates(nums):
    """
    Given list of distinct elements, return all possible distinct subsets
    Time: O(N * 2^N)
    Space: O(N)
    """
    curr_set, subsets = [], []
    helper(0, nums, curr_set, subsets)
    return subsets


def helper(i, nums, curr_set: list, subsets: list):
    if i >= len(nums):
        subsets.append(curr_set.copy())
        return

    curr_set.append(nums[i])
    helper(i + 1, nums, curr_set, subsets)

    curr_set.pop()
    helper(i + 1, nums, curr_set, subsets)


print(
    unique_subsets_without_duplicates([1, 2, 3])
)  # [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
