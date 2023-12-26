from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LevelOrderTraversalSolution:
    @staticmethod
    def right_side_view(root: TreeNode | None) -> list[int]:
        """
        Perform a level-order traversal while capturing the last element in the queue for each level of the tree.

        Let n = the number of nodes in the tree
        Time: O(n)
        Space: O(n)
        """

        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            if q:
                res.append(q[-1].val)
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
