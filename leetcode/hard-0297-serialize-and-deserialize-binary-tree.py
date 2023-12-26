# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root) -> str:
        """
        Let n = the number of nodes in the tree
        Time: O(n)
        Space: O(n)
        """
        path = []

        def preorder_traversal(node: TreeNode):
            if not node:
                path.append("NULL")
                return

            path.append(str(node.val))
            preorder_traversal(node.left)
            preorder_traversal(node.right)

        preorder_traversal(root)
        return ",".join(path)

    def deserialize(self, data) -> TreeNode:
        """
        Let n = the number of nodes in data
        Time: O(n)
        Space: O(n)
        """
        nodes = data.split(",")

        def unpack_values(i) -> tuple[TreeNode | None, int]:
            if nodes[i] == "NULL":
                return None, i + 1

            node = TreeNode(int(nodes[i]))
            i += 1
            node.left, i = unpack_values(i)
            node.right, i = unpack_values(i)
            return node, i

        return unpack_values(0)[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
