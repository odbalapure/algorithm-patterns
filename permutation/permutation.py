def permutations(nums):
    """
    Find all possible permutations of an array
    Time: O(N^2 * N!)
    Space: O(N * N!)
    """

    def helper(i, nums):
        if i == len(nums):
            return [[]]

        res_perms = []
        perms = helper(i + 1, nums)
        for p in perms:
            for j in range(len(p) + 1):
                perm_copy = p.copy()
                perm_copy.insert(j, nums[i])
                res_perms.append(perm_copy)
        return res_perms

    return helper(0, nums)


print(
    permutations([1, 2, 3, 4])
)  # [[1, 2, 3, 4], [2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1], [1, 3, 2, 4], [3, 1, 2, 4], [3, 2, 1, 4], [3, 2, 4, 1], [1, 3, 4, 2], [3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1], [1, 2, 4, 3], [2, 1, 4, 3], [2, 4, 1, 3], [2, 4, 3, 1], [1, 4, 2, 3], [4, 1, 2, 3], [4, 2, 1, 3], [4, 2, 3, 1], [1, 4, 3, 2], [4, 1, 3, 2], [4, 3, 1, 2], [4, 3, 2, 1]]


def permutations_iterative(nums):
    """
    Find all possible permutations of an array iteratively
    Time: O(N^2 * N!)
    Space: O(N * N!)
    """
    perms = [[]]

    for n in nums:
        next_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                next_perms.append(pCopy)
        perms = next_perms
    return perms


print(
    permutations_iterative([1, 2, 3, 4])
)  # [[1, 2, 3, 4], [2, 1, 3, 4], [2, 3, 1, 4], [2, 3, 4, 1], [1, 3, 2, 4], [3, 1, 2, 4], [3, 2, 1, 4], [3, 2, 4, 1], [1, 3, 4, 2], [3, 1, 4, 2], [3, 4, 1, 2], [3, 4, 2, 1], [1, 2, 4, 3], [2, 1, 4, 3], [2, 4, 1, 3], [2, 4, 3, 1], [1, 4, 2, 3], [4, 1, 2, 3], [4, 2, 1, 3], [4, 2, 3, 1], [1, 4, 3, 2], [4, 1, 3, 2], [4, 3, 1, 2], [4, 3, 2, 1]]
