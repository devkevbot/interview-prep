# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_subtree(self, root: TreeNode | None, sub_root: TreeNode | None) -> bool:
        """
        Time: O(n * m), where n is the number of nodes in the full tree and m is the number of nodes in the sub root
        Space: O(h), where h is the minimum of height of the full tree and the sub root tree
        """
        # If the full tree is empty, nothing can be its subtree
        if root is None:
            return False

        # A null node is always a subtree
        if sub_root is None:
            return True

        return (
                self.is_same_tree(root, sub_root)
                or self.is_subtree(root.left, sub_root)
                or self.is_subtree(root.right, sub_root)
        )

    def is_same_tree(self, a: TreeNode | None, b: TreeNode | None) -> bool:
        if not a and not b:
            return True

        if (a and not b) or (b and not a):
            return False

        return (
                a.val == b.val
                and self.is_same_tree(a.left, b.left)
                and self.is_same_tree(a.right, b.right)
        )
