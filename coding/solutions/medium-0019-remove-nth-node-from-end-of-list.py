# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class FastSlowPointerSolution:
    @staticmethod
    def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
        """
        Time: O(n), where n is the number of nodes in the list
        Space: O(1)
        """

        fast = head
        slow = head

        # Advance fast to the nth position to create a gap of size n
        # between slow and fast.
        for _ in range(n):
            fast = fast.next

        # If fast is null, this means we have traversed the entire list
        # (n >= length of list), which means we can't delete anything.
        if not fast:
            return head.next

        # Advance both pointers until fast.next is null.
        # This means that fast will be on the exact last node
        # and slow will be on the node before the one we want to remove.
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
