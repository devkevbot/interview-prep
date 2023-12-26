class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        """
        Let n = the number of nodes
        Let k = the input k
        Time: O(n)
        Space: O(n / k)
        """

        # Check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        # Reverse the group
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # After reverse, we know that `head` is the tail of the group.
        # And `curr` is the next pointer in original linked list order
        head.next = self.reverse_k_group(curr, k)
        return prev
