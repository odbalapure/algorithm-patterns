def cycle_start(head):
    """
    Find a the start of the cycle in a linked list
    Time: O(N)
    Space: O(1)
    """
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
