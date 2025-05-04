## Fast & Slow Pointers

The idea is to have two pointers i.e. `fast` and `slow`.
Both the pointers will move at different speeds.
Both of them might start from the same position or different based on the condition.
The loop terminates if `fast` reaches the end of the list or `fast` and `slow` pointer meet.
In sliding window problems, the pointers may stop based on a condition like a sum or window size.

## Use Case

- Find middle of a linked list.
- Check if a linked list has a cycle.
- Check if a linked list has a cycle and return the head of the loop.

## Examples

### Find middle of a linked list

```python
def middle_linked_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

> **NOTE**: If the linked list is of even size, it returns the `2nd` of the two middle nodes.

### Check if a loop exists in a linked list

```python
def has_cycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Find the start of the cycle in a linked list

```python
def cycle_start(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None

    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
```

## Complexity

### Time
Overall time taken is `O(N)` after ignoring smaller arbitrary values.

### Space
We need fast/slow pointers that take up constant space i.e. `O(1)`.