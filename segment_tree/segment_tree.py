class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return
        M = (self.L + self.R) // 2
        if M > index:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum

    def range_query(self, L, R):
        if self.left == L and self.right == R:
            return self.sum

        M = (self.L + self.R) // 2
        if L > M:
            return self.right.range_query(L, R)
        elif R <= M:
            return self.left.range_query(L, R)
        else:
            return self.left.range_sum(L, M) + self.right.range_sum(M + 1, R)


nums = [5, 3, 7, 1, 4, 2]
tree = SegmentTree.build(nums, 0, len(nums) - 1)
print(tree.sum)  # 22
