def has_cycle(head) -> bool:
    """
    Check if a linked list has a cycle
    Time: O(N)
    Space: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
