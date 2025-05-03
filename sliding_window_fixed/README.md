## Sliding Window

The idea of having a fixed window is to maintain two pointers that `k` apart from each other and fit a certain constraint.

## Use Case

Given array return true if two elements within a window of size `k` are equal.

## Example

### Brute Force

The outer loop will loop `n` times and inner loop repeats `k`, where `n <= k` we end up with `O(n * k)`.

```python
def duplicates_in_windo(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False
```

### Optimal

Maintain a hash set to store elements in the current window. When the set's size goes beyond `k`, we can shift left pointer and remove the element that is no longer in the window.

```python
def duplicates_in_window(nums, k):
    L, window = 0, set()
    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False

```

## Complexity

### Time
Time taken is O(N) because we only perform a single pass on the array, hashset allows O(1) lookup.

### Space
Space taken is O(k) becauase we are storing at most `k` distinct elements in our hashset.