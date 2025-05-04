## Range Sum Query

We create an array, say, `prefix` such that the value at its `i`th index denotes the running sum of a `nums` subarray that starts from `0` and goes up to and including the `i`th index.

So, given an array [2,-1,3,-3,4], the prefix sum array would be [2,1,4,1,5].

## Use Case

Range sum query in an array or matrix.

## Example

```python
class Prefix:
    def __init__(self, nums):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
    
    def range_sum(self, left, right):
        R = self.prefix[right]
        L = self.prefix[left - 1] if left > 0 else 0
        return (R - L)
```

## Complexity

### Time
Time complexity to build initial prefix sum is `O(N)`. However to calculate range sum it takes `O(1)` no matter how big the array.

### Space
If we don't need the initial array we can overrite it with its prefix sum, which will bring the space complexity down from `O(N)` to `O(1)`.