import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def invert_tree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Let n = the number of nodes in the tree.
        Time: O(n), all nodes of the tree are visited.
        Space: O(n), in the worst case, the tree is completely vertical
        """
        if not root:
            return None

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        root.left, root.right = root.right, root.left

        return root


class IterativeSolution:
    @staticmethod
    def invert_tree(root: TreeNode | None) -> TreeNode | None:
        """
        Let n = the number of nodes in the tree.
        Time: O(n), all nodes of the tree are visited.
        Space: O(n), at most n / 2 nodes are in the queue
        """
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                continue

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
