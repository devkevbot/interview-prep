import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoubleEndedQueueSolution:
    @staticmethod
    def reorder_list(head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.

        Let n = the length of the list
        Time: O(n)
        Space: O(n)
        """
        queue = collections.deque()

        curr = head.next
        while curr:
            queue.append(curr)
            curr = curr.next

        curr = head
        for i in range(len(queue)):
            if i % 2 == 0:
                node = queue.pop()
            else:
                node = queue.popleft()
            node.next = None
            curr.next = node
            curr = curr.next


class TwoPointerSolution:
    @staticmethod
    def reorder_list(head: ListNode) -> None:
        """
        Let n = the length of the list
        Time: O(n)
        Space: O(1)
        """
        if not head:
            return

        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
