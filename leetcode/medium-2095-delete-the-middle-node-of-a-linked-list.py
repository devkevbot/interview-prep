# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        """
        Let n = the length of the linked list
        Time: O(n)
        Space: O(1)
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head.next.next

        # Since slow moves half the speed of fast, when fast reaches the end of the list,
        # slow will be one node before the middle element to remove.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head
