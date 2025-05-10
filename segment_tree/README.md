## Segment Tree

Range sum queries can be found using a prefix array. The query can be completed in `O(1)` time.
But if the array is updated frequetly, it would take `O(N) ` to shift elements.

If we use a segment tree, the update would take `O(logN) ` time but the range query will take `O(logN)` time.

We break the array into segments by a branching factor of two. Each segment/node represent a smaller range (which are indices of array).

```python
class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R
```

Where,
- `sum`, which will keep track of the sum at each node.  
- `right` and `left` pointers to the right and the left - child (similar to binary trees).  
- `L` and `R` denote the left and right boundaries

We split the array recursively and calculate the sum for each segment/node.

```python
def build(nums, L, R):
    if L == R:
        return SegmentTree(nums[L], L, R)

    M = (L + R) // 2
    root = SegmentTree(0, L, R)
    root.left = SegmentTree.build(nums, L, M)
    root.right = SegmentTree.build(nums, M + 1, R)
    root.sum = root.left.sum + root.right.sum
    return root
```

To update an index we need a value and an index. After the value is updated at that index, the sum of all segments (nodes) that include that index in their range needs to be updated i.e. the sum needs to updated along the path till the root.

```python
def update(self, index, val):
    if self.L == self.R:
        self.sum = val
        return

    M = (self.L + self.R) // 2
    if index > M:
        self.right.update(index, val)
    else:
        self.left.update(index, val)
    self.sum = self.left.sum + self.right.sum
```

The range query logic is somewhat similar to the update operation.

```python
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
```

## Complexity

`build()` takes O(N) time, where N is the no. of nodes.  
`update()` takes O(logN) or O(h), where h is the height of the tree.
`range_query()` takes O(logN) time.