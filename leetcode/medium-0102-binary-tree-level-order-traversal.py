from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time: O(n), where n is the number of nodes in the tree
        Space: O(n), where n is the number of nodes in the tree
        """
        levels = []

        queue = collections.deque([root])

        while queue:
            level = []
            count = len(queue)

            while count > 0:
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

                count -= 1

            if level:
                levels.append(level)

        return levels
