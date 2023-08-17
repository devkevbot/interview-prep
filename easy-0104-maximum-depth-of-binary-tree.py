from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My DFS solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n), where n is the number of nodes in the tree
        Space: O(h), where h is the height of the tree
        """

        def traverse(root: Optional[TreeNode], depth):
            if root is None:
                return depth

            left_depth = traverse(root.left, depth + 1)
            right_depth = traverse(root.right, depth + 1)
            return max(left_depth, right_depth)

        return traverse(root, 0)


# Shorter DFS solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
