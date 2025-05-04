class Prefix:
    def __init__(self, nums):
        """
        Create a prefix array
        Time: O(N)
        Space: O(N)
        NOTE: Can mutate the original array to bring down space to O(1)
        """
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def range_sum(self, left, right):
        """
        Range sum query
        Time: O(1)
        Space: O(1)
        """
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left
