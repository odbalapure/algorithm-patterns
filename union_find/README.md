## Union Find

It can be used to find disjoint sets, detect cycles in a graph.
> Usually DFS does solve these kind of problems in almost the same time complexity.

Union Find is a `forest of trees`. Eg: If we have 4 nodes initially each one of them is a disjoint set implemented as a hashmap because each node holds reference to its parent.

### Find

Find takes `n` as an argument and return its root parent. We use the `parent` hashmap where the key is the vertex itself and the value is the parent.

By traversing up the tree we can find the root parent.

```python
def find(self, n):
    if n != self.parent[n]:
        self.parent[n] = self.find(self.parent[n])
    return self.parent[n]
```

**NOTE**: `self.parent[n] = self.find(self.parent[n])` performs the path  compression to reduce the time complexity. This is an amortized operation.

### Union

Union takes two vertices and determines if a union can be performed.

```python
def union(self, n1, n2):
    p1, p2 = self.find(n1), self.find(n2)
    if p1 == p2:
        return False

    if self.rank[p1] > self.rank[p2]:
        self.par[p2] = p1
    elif self.rank[p1] < self.rank[p2]:
        self.par[p1] = p2
    else:
        self.par[p1] = p2
        self.rank[p2] += 1
    return True
```

Union is performed the following way:
- If 2 vertices share the same root/parent; union cannot be performed.
- If `n1` and `n2` have parents `p1` and `p2`, If `p1`'s rank is higher than `p2`, `p2` becomes the child of `p1`
- If `p2`'s rank is higher than `p1`, `p1` becomes the child of `p2`

## Complexity

For `find` operation the worst case will be `O(N)` if the tree is skewed, it could look like a linked list.

For `union` the time taken will `O(M ∗ α(n))`, where `M` is the total no. of edges. So total time taken will `O(M)`.

NOTE: `α` is called as [Inverse Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function), which is very slow growing function and considered to be constant for all practical purposes.
