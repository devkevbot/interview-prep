from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n), where n is the number of nodes in the input list
        Space: O(1)
        """
        prev = None
        curr = head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head = prev
        return head


# Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n), where n is the number of nodes in the input list
        Space: O(n), where n is the number of nodes in the input list
        """

        # Base case: 0 or 1 node
        if head is None or head.next is None:
            return head

        # Reverse the rest of the list, excluding the current node
        reversed_list_head = self.reverseList(head.next)

        # Add self as the head of the reversed list
        head.next.next = head

        # Set next value to None since the current node could be the last node to reverse
        head.next = None

        return reversed_list_head
