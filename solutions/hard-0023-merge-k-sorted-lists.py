import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
        """
        Let n = the total number of elements contained in all lists.
        Let k = the total number of lists.
        Time: O(n log k)
        Space: O(k)
        """

        # Due to how Python 3 compares heap elements for equality, we can't just use
        # the `node.val` and `node`. We also need `list_index` to avoid a TypeError.
        h = [(node.val, list_index, node) for list_index, node in enumerate(lists) if node]
        # O(k)
        heapq.heapify(h)

        dummy = ListNode()
        curr = dummy

        # O(n)
        while h:
            # O(log k)
            val, list_index, node = heapq.heappop(h)
            curr.next = node
            curr = curr.next

            if node.next:
                # O(log k)
                heapq.heappush(h, (node.next.val, list_index, node.next))

        return dummy.next
