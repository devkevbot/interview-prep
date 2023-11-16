# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Iterative
class Solution:
    @staticmethod
    def merge_two_lists(
        list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        """
        Time: O(n + m), where n is the length of list1 and m is the length of list 2
        Space: O(1)
        """
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next
