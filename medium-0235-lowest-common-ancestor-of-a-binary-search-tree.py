# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class RecursiveSolution:
    def lowest_common_ancestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Time: O(h), where h is the height of the tree
        Space: O(h)
        """
        if p.val < root.val and q.val < root.val:
            return self.lowest_common_ancestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowest_common_ancestor(root.right, p, q)
        return root


class IterativeSolution:
    @staticmethod
    def lowest_common_ancestor(
        root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Time: O(h), where h is the height of tree
        Space: O(1)
        """
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
