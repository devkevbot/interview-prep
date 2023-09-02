import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LevelOrderTraversalSolution:
    @staticmethod
    def right_side_view(root: Optional[TreeNode]) -> List[int]:
        """
        Perform a level-order traversal while capturing the last element in the queue for each level of the tree.

        Time: O(n), where n is the number of nodes in the tree
        Space: O(n)
        """

        res = []
        queue = collections.deque([root])

        while queue:
            right_most = queue[-1]
            if right_most:
                res.append(right_most.val)

            num_elements = len(queue)
            while num_elements > 0:
                element = queue.popleft()
                num_elements -= 1
                if element:
                    # Only add non-null nodes into the discovery queue
                    if element.left:
                        queue.append(element.left)
                    if element.right:
                        queue.append(element.right)

        return res
