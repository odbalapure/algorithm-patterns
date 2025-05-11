## Subset

If we have two sets A and B, Set A is subset to Set B if all of its elements are found in Set B.
Also, any set is a subset of itself and an empty set is a subset of every set.
Order is not important in subsets, but the elements within a set must be distinct.

```css
                    []
                 /      \
              [1]       []
             /   \      /   \
         [1,2]  [1]   [2]   []
         /  \   / \   / \   / \
   [1,2,3][1,2][1,3][1][2,3][2][3][]
```

**NOTE**: If there are duplicates in the array, we sort the array and iterate over it to compare adjacent elements to avoid duplicates in a subset.

## Use Case
- Given list of distinct elements, return all possible distinct subsets.
- Given list containing duplicate elements, return all possible distinct subsets.

## Complexity

### Time

We build a recursive tree to explore all possible subsets. For every decision we make, we can either include or not include the current element. This results in a branching factor or `2` ad height of `n`.

The overall time complexity is `O(N * 2^N)`.

### Space

If we ignore the space required to store the end result, the space complexity will be `O(N)`. The space needed to store the current subset is propotional to the length of the input list `nums`.