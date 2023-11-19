class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def __init__(self):
        self.global_max_sum = float("-inf")

    def max_path_sum(self, root: TreeNode | None) -> int | float:
        """
        Let n = the number of nodes in the tree
        Time: O(n)
        Space: O(n)
        """

        self.helper(root)
        return self.global_max_sum

    def helper(self, root: TreeNode | None) -> int | float:
        # If a node is null, the maximum path sum from that node is 0.
        if not root:
            return 0

        # For either subtree, it's only worth including if it would make our current sum larger.
        # Since the tree can contain negative numbers, we don't want to include a subtree sum if
        # it's negative.
        lst_max_sum = max(self.helper(root.left), 0)
        rst_max_sum = max(self.helper(root.right), 0)

        # For the given root, the maximum sum we can make which starts at the root is simply
        # the value of the root, plus the path sums of its subtrees.
        curr_max_sum = root.val + lst_max_sum + rst_max_sum

        self.global_max_sum = max(self.global_max_sum, curr_max_sum)

        # As we go back up the tree, the maximum path sum involving the root can only
        # use the left or right subtree.
        return root.val + max(lst_max_sum, rst_max_sum)
