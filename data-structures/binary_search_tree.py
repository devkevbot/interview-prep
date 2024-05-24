"""
Binary Search Tree Implementation
"""


class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    """
    Invariant:
    - Each node can have [0, 2] children.
    - The value in each node must be >= any values in its left subtree.
    - The Value in each node must be <= any values in its right subtree.
    - Each node has a unique value.
    """

    def __init__(self) -> None:
        self.root = None

    def search_iterative(self, val):
        """
        Time: O(n), where n is the number of nodes in the tree. In the worst
        case, we need to search every node in a skewed tree.
        Space: O(1) since we don't recurse or use any auxiliary memory.
        """
        curr = self.root

        while curr is not None:
            if val == curr.val:
                break
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def search_recursive(self, val):
        """
        Time: O(n), where n is the number of nodes in the tree. In the worst
        case, we need to search every node in a skewed tree.
        Space: O(n), where n is the number of nodes in the tree. In the worst
        case, the depth of recursion is equal to the height of the tree, which
        will be n.
        """
        return self.search_recursive_helper(self.root, val)

    def search_recursive_helper(self, root, val):
        if root is None:
            return None

        if val == root.val:
            return root
        elif val < root.val:
            return self.search_recursive_helper(root.left, val)
        else:
            return self.search_recursive_helper(root.right, val)

    def insert_iterative(self, val):
        """
        Time: O(n), where n is the number of nodes in the tree. In the worst case,
        we need to insert into the bottom of a skewed tree.
        Space: O(1) since we don't recurse or create any auxiliary data structures.
        """
        if self.root is None:
            self.root = TreeNode(val)
            return self.root

        curr = self.root

        while curr is not None:
            if val < curr.val:
                if curr.left is None:
                    curr.left = TreeNode(val)
                    break
                curr = curr.left
            elif val > curr.val:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    break
                curr = curr.right

        return self.root

    def insert_recursive(self, val):
        """
        Time: O(n), where n is the number of nodes in the tree. In the worst case,
        we need to insert into the bottom of a skewed tree.
        Space: O(n), where n is the number of nodes in the tree. In the worst case,
        the depth of recursion is equal to the height of the tree, which will be
        n.
        """
        return self.insert_recursive_helper(self.root, val)

    def insert_recursive_helper(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root

        if val < root.val:
            root.left = self.insert_recursive_helper(root.left, val)
        elif val > root.val:
            root.right = self.insert_recursive_helper(root.right, val)

        return root

    def delete_recurive(self, key):
        return self.delete_recursive_helper(self.root, key)

    def delete_recursive_helper(self, root, key):
        """
        Time: O(n), where n is the number of nodes in the tree. In the worst case,
        we need to delete a node at the bottom of a skewed tree.
        Space: O(n), where n is the number of nodes in the tree. In the worst case,
        the depth of recursion is equal to the height of the tree, which will be
        n.
        """
        if root is None:
            return None

        if root.val == key:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.find_successor(root)
            root.val = successor.val
            root.right = self.delete_recursive_helper(root.right, successor.val)
            return root
        elif key < root.val:
            root.left = self.delete_recursive_helper(root.left, key)
        elif key > root.val:
            root.right = self.delete_recursive_helper(root.right, key)

        return root

    def find_successor(self, root):
        # Step right once, then go as left as possible
        curr = root.right
        while curr is not None and curr.left is not None:
            curr = curr.left
        return curr

    def find_predecessor(self, root):
        # Step left once, then go as right as possible
        curr = root.left
        while curr is not None and curr.right is not None:
            curr = curr.right
        return curr
