class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs_recursive(root, target):
    # Check if the root is the target node
    if root.val == target:
        return root

    # Recursively search the left subtree
    if root.left:
        left_result = dfs_recursive(root.left, target)
        if left_result:
            return left_result

    # Recursively search the right subtree
    if root.right:
        right_result = dfs_recursive(root.right, target)
        if right_result:
            return right_result

    # If we reach this point, the target node was not found
    return None


def dfs_iterative(root, target):
    # Create a stack to store nodes to visit
    stack = [root]

    # Loop until the stack is empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # Check if the node is the target node
        if node.val == target:
            return node

        # Add the node's right child to the stack if it exists
        if node.right:
            stack.append(node.right)

        # Add the node's left child to the stack if it exists
        if node.left:
            stack.append(node.left)

    # If we reach this point, the target node was not found
    return None


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(dfs_recursive(root, 5).val)  # Output: 5
    print(dfs_iterative(root, 5).val)  # Output: 5
