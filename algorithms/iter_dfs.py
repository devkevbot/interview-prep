"""
Iterative Depth-first Search Implementation
"""

from typing import List


class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    """
    Time: O(n)
    Space: O(n)
    """

    stack = []
    curr = root

    while curr or len(stack) > 0:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.val)
            curr = curr.right


def inorder_alternate(root: TreeNode) -> List[int]:
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # inorder: left -> root -> right
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
    return res


def preorder(root):
    """
    Time: O(n)
    Space: O(n)
    """

    stack = []
    curr = root

    while curr or len(stack) > 0:
        if curr:
            # Print self first
            print(curr.val)
            if curr.right:
                # We will visit the right subtree after we're done with the left
                # subtree
                stack.append(curr.right)
            curr = curr.left
        else:
            # Go to the right subtree
            curr = stack.pop()


def preorder_alternate(root: TreeNode) -> List[int]:
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # preorder: root -> left -> right
                stack.append((node.right, False))
                stack.append((node.left, False))
                stack.append((node, True))
    return res


def postorder(root):
    """
    Time: O(n)
    Space: O(n)
    """

    stack = [root]
    visit = [False]
    while len(stack) > 0:
        curr, visited = stack.pop(), visit.pop()
        if curr:
            if visited:
                print(curr.val)
            else:
                # Self last
                stack.append(curr)
                visit.append(True)

                # Right 2nd
                stack.append(curr.right)
                visit.append(False)

                # Left 1st
                stack.append(curr.left)
                visit.append(False)


def postorder_alternate(root: TreeNode) -> List[int]:
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()  # the last element
        if node:
            if visited:
                res.append(node.val)
            else:  # postorder: left -> right -> root
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res


if __name__ == "__main__":
    four = TreeNode(4, None, None)
    five = TreeNode(5, None, None)
    two = TreeNode(2, four, None)
    three = TreeNode(3, None, five)
    one = TreeNode(1, two, three)

    inorder(one)
    res = inorder_alternate(one)
    print(f"Inorder {res}")
    print()

    preorder(one)
    res = preorder_alternate(one)
    print(f"Preorder {res}")
    print()

    postorder(one)
    res = postorder_alternate(one)
    print(f"Postorder {res}")
    print()
