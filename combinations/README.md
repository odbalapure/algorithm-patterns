## Combination

Combinations are similar to Subsets in that we are choosing elements from set. The order the elements are placed in, does not matter.

The main difference is that a combination is a subset of size `k`, where is less than or equal to the size of the original set.

## Use Case

- Given two integers `N` and `K`, return all possible combinations of `size = K`, choosing values from 1 and `N`.
- Return unique combinations of nums whose sum is equal to a `target`.
- Letter Combinations of a Phone Number.

## Example

### Trivial

We iterate through the array, make a decision to include/exclude the element. We are restricted by the no. of elements we can include in our combination. If the current set length is equal to `k`, we don't go any farther.

```python
def combinations(n, k):
    def helper(i, curr_bomb, combs, n, k):
        if len(curr_bomb) == k:
            combs.append(curr_bomb.copy())
            return
        if i > n:
            return

        # decision to include "i"
        curr_bomb.append(i)
        helper(i + 1, curr_bomb, combs, n, k)
        curr_bomb.pop()

        # decision to NOT include "i"
        helper(i + 1, curr_bomb, combs, n, k)

    combs = []
    helper(1, [], combs, n, k)
    return combs
```

### Optimized

The complexity can be optimized to `(k * C(n, k))`, where `C(n, k)` is the no. of combinations we need to generate.

Insted of chosing which element to include/exclude, we simply choose the elements we want to include.

If we are index `i`, we pick elements from `i + 1` till `N`.

Each combination is generated in ascending sorted order, which is useful because if we generate `[1, 2]` we will never generate the duplicate `[2, 1]`.

```python
def combinations(n, k):
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
```

## Complexity

### Time

Time complexity for navie approach is `O(k * 2^n)`, whereas the optimized apporach takes `O(k * C(n, k))`.

### Space

First approach takes `O(k + n)`and second one takes `O(k)`.

> We ignore the space required to store the end result