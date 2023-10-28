# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveInorderTraversalSolution:
    @staticmethod
    def kth_smallest(root: TreeNode | None, k: int) -> int:
        """
        Let n = the number of nodes in the tree
        Time: O(n), we visit every node
        Space: O(n), we store every non-null node's value
        """

        # In-order traversal => [1, 2, 3, 4, 5, 6], if k = 3, then output = res[k-1] = 3
        # In-order traversal => [1, 2, 3, 4], if k = 1, then output = res[k-1] = 1
        def inorder_traversal(root: TreeNode | None, nodes: list[int]):
            if not root:
                return

            inorder_traversal(root.left, nodes)
            nodes.append(root.val)
            inorder_traversal(root.right, nodes)

        nodes = []
        inorder_traversal(root, nodes)
        return nodes[k - 1]


class IterativeInorderTraversalSolution:
    @staticmethod
    def kth_smallest(root: TreeNode | None, k: int) -> int:
        """
        Let n = the number of nodes in the tree
        Let h = the height of the tree. In the worst case, h = n, in the average case h = log n
        Time: O(h + k), where
        Space: O(h)
        """
        stack = []

        while root:
            stack.append(root)
            root = root.left

        while k > 0:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val

            right = node.right
            while right:
                stack.append(right)
                right = right.left
