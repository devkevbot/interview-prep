# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_valid_bst(self, root: TreeNode | None) -> bool:
        """
        Let n = the number of nodes in the tree
        Time: O(n)
        Space: O(n)
        """
        return self.helper(root, float("-inf"), float("inf"))

    def helper(
        self, node: TreeNode | None, min_val: float | int, max_val: float | int
    ) -> bool:
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return self.helper(node.left, min_val, node.val) and self.helper(
            node.right, node.val, max_val
        )
