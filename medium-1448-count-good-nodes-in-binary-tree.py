# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.num_good_nodes = 0

    def good_nodes(self, root: TreeNode) -> int:
        """
        Let n = the number of nodes in the tree
        Time: O(n)
        Space: O(n)
        """

        self.dfs(root, float("-inf"))
        return self.num_good_nodes

    def dfs(self, node: TreeNode | None, curr_max: float | int):
        if node is None:
            return

        if node.val >= curr_max:
            self.num_good_nodes += 1

        curr_max = max(curr_max, node.val)

        self.dfs(node.left, curr_max)
        self.dfs(node.right, curr_max)
