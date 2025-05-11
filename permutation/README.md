## Permutations

We can take a **permutation** of a set of elements by creating an ordered arrangement of those elements.
Eg: For a set {1, 2, 3}, we can have the following permutations:
```
{1, 2, 3} or {3, 2, 1} or {1, 3, 2}
```

Unlike combination we intend to use all the elements from the given set.

For an array `[1, 2, 3, 4]` there are `24` or `(4!)` permutations.

### Recursion

For {1, 2, 3}, we generate permutations without including 1. This would generate {2, 3} and {3, 2}.

To include 1, insert 1 at each index of {2, 3} and {3, 2}.

The resulting permutations would be
```
{1,2,3}, {2,1,3}, {2,3,1} and {1,3,2}, {3,1,2}, {3,2,1}
```

```python
def permutations(nums):
    return helper(0, nums)

def helper(i, nums):
    if i == len(nums):
        return [[]]

    res_perms = []
    perms = helper(i + 1, nums)
    for p in perms:
        for j in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(j, nums[i])
            res_perms.append(p_copy)
    return res_perms
```

### Iteration

We iterate over `nums` instead of making recursive calls.

```python
def permutations(nums):
    perms = [[]]

    for n in nums:
        next_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                next_perms.append(p_copy)
        perms = next_perms
    return perms
```

## Complexity

### Time

There are `N!` permutationsm and the outer loops over a permutation of length `N`. Also the inner loop runs `N` times. So, the time taken will be `O(N! * N^2)`.

### Space

It will be `O(N! * N)` because we're storing N! different permutations, and each permutation contains `N` elements.