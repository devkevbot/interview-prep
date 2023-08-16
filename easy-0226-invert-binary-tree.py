from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time: O(n), all n nodes of the tree are visited.
        Space: O(n), in the worst case, the tree is completely vertical
        """
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


import collections


# Iterative
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time: O(n), all n nodes of the tree are visited.
        Space: O(n), at most n / 2 nodes are in the queue
        """
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                continue

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
