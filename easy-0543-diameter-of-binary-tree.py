from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS solution
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.dfs(root)
        return self.max_diameter

    def dfs(self, root: Optional[TreeNode]) -> int:
        """
        Time: O(n) where n is the number of nodes in the tree
        Space: O(h) where h is the height of the tree
        """
        if root is None:
            return 0

        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)

        # Diameter is the sum of the height of the left and right subtrees
        diameter = left_height + right_height

        # Update the maximum diameter
        self.max_diameter = max(self.max_diameter, diameter)

        return max(left_height, right_height) + 1
