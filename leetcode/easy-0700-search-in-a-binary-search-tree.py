# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """
        Let n = the number of nodes in the binary search tree
        Time: O(n)
        Space: O(1)
        """
        curr = root
        while curr:
            if curr.val == val:
                return curr
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr
