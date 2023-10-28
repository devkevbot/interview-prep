# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    @staticmethod
    def copy_random_list(head: Node | None) -> Node | None:
        """
        Let n = the number of nodes in the list
        Time: O(n)
        Space: O(n)
        """

        if not head:
            return None

        # Create new node copies that don't yet point to the other new nodes
        curr = head
        while curr:
            copied = Node(x=curr.val, next=curr.next, random=curr.random)
            curr.next = copied
            curr = copied.next

        # Update .next and .random references to point at the new nodes
        curr = head.next
        while curr:
            curr.random = curr.random.next if curr.random else None
            curr.next = curr.next.next if curr.next else None
            curr = curr.next

        return head.next
