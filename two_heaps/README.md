## Two Heaps

Two heaps are maintained, a **max heap** and a **min heap**.
Both the heaps are roughly the same size.

```python
class Median:
    def __init__(self):
        self.small, self.large = [], []
```

To insert a new element to the max heap (`min`).
If max heap is greater in size, remove an element from it and insert it in min heap
If min heap is greater in size, remove an element from it and insert it in max heap

```python
def insert(self, num):
    # Push to the max heap and swap with min heap if needed.
    heapq.heappush(self.small, -1 * num)
    if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
        val = -1 * heapq.heappop(self.small)
        heapq.heappush(self.large, val)

    # Handle uneven size
    if len(self.small) > len(self.large) + 1:
        val = -1 * heapq.heappop(self.small)
        heapq.heappush(self.large, val)
    if len(self.large) > len(self.small) + 1:
        val = heapq.heappop(self.large)
        heapq.heappush(self.small, -1 * val)
```

Median can be found based on the size of the heaps.

```python
def get_median(self):
    if len(self.small) > len(self.large):
        return -1 * self.small[0]
    elif len(self.large) > len(self.small):
        return self.large[0]
    # For even # of elements, return avg of two middle nums
    return (-1 * self.small[0] + self.large[0]) / 2
```

## Use Case

- Find median of a data stream
- Running median for sliding window

## Complexity

### Time

Insertion takes `O(log N)` time whereas calculating the median takes `O(1)` time.

### Space

`O(N)` where N is the no. of elements in the stream.