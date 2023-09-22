# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def __init__(self):
        self.diameter = 0

    def diameter_of_binary_tree(self, root: TreeNode | None) -> int:
        """
        Let n = the number of nodes in the tree
        Let h = the height of the tree
        Time: O(n)
        Space: O(h)
        """

        self.max_depth(root)
        return self.diameter

    def max_depth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        lst_depth = self.max_depth(root.left)
        rst_depth = self.max_depth(root.right)

        self.diameter = max(self.diameter, lst_depth + rst_depth)

        return 1 + max(lst_depth, rst_depth)
