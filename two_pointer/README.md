## Two Pointer

We start L pointer at `0` and R pointer at `arr.length - 1`
Increment L or decrement R or both depending on the condition. This repeats until the pointers meet each other.

## Use Case

- Check if array is palindrome.
- Target two sum.

## Example

### Check if array is palindrome

```python
def is_palindrome(word):
    L, R = 0, len(word) - 1
    while L < R:
        if word[L] != word[R]:
            return False
        L += 1
        R -= 1
    return True
```

### Target sum

```python
def target_sum(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]

```

## Complexity

### Time
Time taken is O(N) since we only make one pass through the array.

### Space
We only need few variables to keep track of the left and right pointer.