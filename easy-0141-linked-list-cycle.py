from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Time: O(n) - In the worst case, all elements of the list are traversed once, plus some
        fraction of the list is cycled while fast catches up to slow to detect a cycle.
        Space: O(1) - Only constant memory is used.
        """
        if not head:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
