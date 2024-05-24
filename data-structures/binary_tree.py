"""
Binary tree implementation
"""

from typing import List
from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def __str__(self) -> str:
        path = self.preorder_traversal()
        return ",".join(path)

    def insert(self, data) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(data)

    def insert_helper(self, data) -> None:
        """
        Insertion algorithm:
        - Perform a level-order traversal until we find a node which has a missing child
        """

        queue = deque([])
        queue.append(self.root)

        while len(queue) > 0:
            curr = queue.popleft()

            if not curr.left:
                curr.left = Node(data)
                break
            else:
                queue.append(curr.left)

            if not curr.right:
                curr.right = Node(data)
                break
            else:
                queue.append(curr.right)

    def preorder_traversal(self) -> List:
        path = []
        self.preorder_traversal_helper(self.root, path)
        return path

    def preorder_traversal_helper(self, node, path) -> None:
        if node is None:
            return

        path.append(f"{node.data}")

        if node.left is not None:
            self.preorder_traversal_helper(node.left, path)
        if node.right is not None:
            self.preorder_traversal_helper(node.right, path)

    def inorder_traversal(self) -> List:
        path = []
        self.inorder_traversal_helper(self.root, path)
        return path

    def inorder_traversal_helper(self, node, path) -> None:
        if node is None:
            return

        if node.left is not None:
            self.inorder_traversal_helper(node.left, path)

        path.append(f"{node.data}")

        if node.right is not None:
            self.inorder_traversal_helper(node.right, path)

    def postorder_traversal(self) -> List:
        path = []
        self.postorder_traversal_helper(self.root, path)
        return path

    def postorder_traversal_helper(self, node, path) -> None:
        if node is None:
            return

        if node.left is not None:
            self.postorder_traversal_helper(node.left, path)

        if node.right is not None:
            self.postorder_traversal_helper(node.right, path)

        path.append(f"{node.data}")

    def bfs(self) -> List:
        path = []
        self.bfs_helper(path)
        return path

    def bfs_helper(self, path) -> None:
        queue = deque([])

        if self.root is not None:
            queue.append(self.root)

        while len(queue) > 0:
            curr = queue.popleft()
            path.append(curr.data)

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)


if __name__ == "__main__":
    b = BinaryTree()
    b.insert(1)
    b.insert(2)
    b.insert(3)
    b.insert(4)
    b.insert(5)
    b.insert(6)
    b.insert(7)

    print(f"Preorder: {b.preorder_traversal()}")
    print(f"Postorder: {b.postorder_traversal()}")
    print(f"Inorder: {b.inorder_traversal()}")

    print(f"BFS: {b.bfs()}")
