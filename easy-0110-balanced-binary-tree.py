from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Two-pass solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n^2), where n is the number of nodes in three
        Space: O(h), where h is the height of the tree
        """
        if root is None:
            return True

        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)

        return (
            abs(left_depth - right_depth) < 2
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def depth(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0

        return 1 + max(self.depth(root.left), self.depth(root.right))


# One-pass approach
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time: O(n), where n is the number of nodes in tree
        Space: O(h), where h is the height of the tree
        """
        if root is None:
            return True

        return self.helper(root)[1]

    def helper(self, root: Optional[TreeNode]):
        if root is None:
            return [-1, True]

        left = self.helper(root.left)
        right = self.helper(root.right)

        height = 1 + max(left[0], right[0])
        balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1

        return [height, balanced]
