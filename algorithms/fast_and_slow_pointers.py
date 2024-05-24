"""
Fast and slow pointer implementations
"""

from typing import Optional


class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def middle_of_linked_list(node: Optional[Node]):
    """
    Finds the middle node of an acyclic linked list, if any, and returns it.

    This functions use a slow & fast pointer approach.

    Odd-length linked lists will always have the exact middle node returned.
    Even-length linked lists will have the "2nd middle" returned.
    - Note: we could augment our algorithm to return the "1st middle" by
    starting the fast pointer one position ahead of the slow pointer.
    """
    slow = node
    fast = node

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    # Edge case: no nodes
    mid = middle_of_linked_list(None)
    assert mid == None

    # Edge case: single node
    first = Node(1)
    mid = middle_of_linked_list(first)
    assert mid == first

    # 2 nodes
    first = Node(1)
    second = Node(2)
    first.next = second
    mid = middle_of_linked_list(first)
    print(mid.val)

    # 3 nodes
    first = Node(1)
    second = Node(2)
    first.next = second
    third = Node(3)
    second.next = third
    mid = middle_of_linked_list(first)
    print(mid.val)

    # 4 nodes
    first = Node(1)
    second = Node(2)
    first.next = second
    third = Node(3)
    second.next = third
    four = Node(4)
    third.next = four
    mid = middle_of_linked_list(first)
    print(mid.val)
