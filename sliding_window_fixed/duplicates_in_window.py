def duplicates_in_window(nums, k):
    """
    Find duplicates in a window of size "k"
    Time: O(N * K)
    Space: O(1)
    """
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


def duplicates_in_window(nums, k):
    """
    Find duplicates in a window of size "k"
    Time: O(N)
    Space: O(K)
    """
    L, window = 0, set()
    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False
