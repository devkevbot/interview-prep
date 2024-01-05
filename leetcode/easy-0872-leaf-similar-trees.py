# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        """
        Let n = the number of nodes in the first tree
        Let m = the number of nodes in the second tree
        Time: O(n + m)
        Space: O(n + m)
        """
        path1 = []
        path2 = []

        self.inorder_traversal(root1, path1)
        self.inorder_traversal(root2, path2)

        return path1 == path2

    def inorder_traversal(self, node: TreeNode | None, path: list[int]):
        if not node:
            return

        self.inorder_traversal(node.left, path)
        if not node.left and not node.right:
            path.append(node.val)
        self.inorder_traversal(node.right, path)
