from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root, target):
    # Check if the root is the target node
    if root.val == target:
        return root

    # Create a queue to store nodes to visit
    queue = deque([root])

    # Loop until the queue is empty
    while queue:
        # Get the next node from the queue
        node = queue.popleft()

        # Check if the node is the target node
        if node.val == target:
            return node

        # Add the node's children to the queue if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # If we reach this point, the target node was not found
    return None


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(bfs(root, 5).val)  # Output: 5
