# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SlowRecursiveSolution:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        Let n = the length of either preorder or inorder (they are the same length)
        Time: O(n^2)
        Space: O(n)
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        # Mid is the index that divides the left and right subtrees
        # O(n)
        mid = inorder.index(preorder[0])

        # Construct left subtree
        root.left = self.build_tree(preorder[1 : mid + 1], inorder[:mid])

        # Construct right subtree
        root.right = self.build_tree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
