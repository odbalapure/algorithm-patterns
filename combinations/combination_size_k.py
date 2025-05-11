def combination_size_k(n, k):
    """
    Find "n" possible combination of numbers of size "k"
    Time: O(k * 2^n)
    Space: O(n)
    """

    def helper(i, curr_comb, combs, n, k):
        if len(curr_comb) == k:
            combs.append(curr_comb.copy())
            return

        if i > n:
            return

        curr_comb.append(i)
        helper(i + 1, curr_comb, combs, n, k)

        curr_comb.pop()
        helper(i + 1, curr_comb, combs, n, k)

    combs = []
    helper(1, [], combs, n, k)
    return combs


def combination_size_k_optimized(n, k):
    """
    Find "n" possible combination of numbers of size "k"
    Time: O(k * C(n, k))
    Space: O(n)
    """

    def helper(i, curr_comb, combs, n, k):
        if len(curr_comb) == k:
            combs.append(curr_comb.copy())
            return

        if i > n:
            return

        for j in range(i, n + 1):
            curr_comb.append(j)
            helper(j + 1, curr_comb, combs, n, k)
            curr_comb.pop()

    combs = []
    helper(1, [], combs, n, k)
    return combs


print(
    combination_size_k(5, 2)
)  # [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]

print(
    combination_size_k_optimized(5, 2)
)  # [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]
