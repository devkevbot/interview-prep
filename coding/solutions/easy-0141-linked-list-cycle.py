# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def has_cycle(head: ListNode | None) -> bool:
        """
        Let n = the number of nodes in the list.
        Time: O(n) - In the worst case, all elements of the list are traversed once, plus some
        fraction of the list is cycled while fast catches up to slow to detect a cycle.
        Space: O(1) - Only constant memory is used.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
