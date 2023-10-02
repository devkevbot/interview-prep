from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Let n = # nodes in p
        Let m = # nodes in q
        Time: O(min(n, m))
        Space: O(min(n, m))
        """
        if not p and not q:
            return True

        if (p and not q) or (q and not p):
            return False

        return (
            p.val == q.val
            and self.is_same_tree(p.left, q.left)
            and self.is_same_tree(p.right, q.right)
        )
