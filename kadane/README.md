## Kadane's Algorithm

Its an algorithm is a greedy or dynamic programming algorithm that can be used on an array.
Used to calculate the max. sum subarray ending at particular position and typically runs in O(n) time.

## Use Case

- Find a non empty subarray with maximum sum.
- Find the size of the size of the maximum sum subarray.

## Examples

### Brute Force

Go through every single subarray and calculate the sum, while keeping track of the maximum sum.

```python
def max_sum_subarray(nums):
    maxSum = nums[0]
    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum
```

### Optimization using Kadane's algorithm

The intuition behind Kadane's algorithm is that:
- If all elements are positive, the max. sum subarray is the entire array.
- If we ever have a negative sum subarray, that's the case we want to avoid.

```python
def max_sum_subarray(nums):
    curr_sum, max_sum = 0, nums[0]
    for num in nums:
        curr_sum = max(curr_sum, 0)
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

This algorithm works in a single pass, hence the complexity comes down to linear time.

### Sliding window variant

```python
def max_sum_subarray_length(nums):
    max_sum = nums[0]
    curr_sum = 0
    max_l, max_r = 0, 0
    L = 0

    for R in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            L = R

        curr_sum += nums[R]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_l, max_r = L, R

    return [max_l, max_r]
```

## Complexity

### Time
Time taken is O(N) since we only make one pass through the array.

### Space
We only need few variables to keep track of the maximum and current sum.