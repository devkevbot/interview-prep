from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time: O(n * m), where n is the number of nodes in the full tree and m is the number of nodes in the subroot
        Space: O(h), where h is the minimum of height of the full tree and the subroot tree
        """
        # If the full tree is empty, nothing can be its subtree
        if root is None:
            return False

        # A null node is always a subtree
        if subRoot is None:
            return True

        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, a, b) -> bool:
        if not a and not b:
            return True

        if (a and not b) or (b and not a):
            return False

        return (
            a.val == b.val
            and self.isSameTree(a.left, b.left)
            and self.isSameTree(a.right, b.right)
        )
