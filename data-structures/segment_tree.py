"""
Segment Tree Implementation
"""


class SegmentTree:
    def __init__(self, total, L, R) -> None:
        self.sum = total
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child
        self.L = L  # The left range boundary
        self.R = R  # The right range boundary

    @staticmethod
    def build(nums, L, R):
        """
        Time: O(n) for n nodes
        """
        if L == R:
            return SegmentTree(nums[L], L, R)

        M = (L + R) // 2

        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index, val):
        """
        Time: O(logn)
        """
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2

        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)

        self.sum = self.left.sum + self.right.sum

    def rangeQuery(self, L, R):
        """
        Time: O(logn)
        """
        if L == self.L and R == self.R:
            return self.sum

        M = (self.L + self.R) // 2

        if L > M:
            return self.right.rangeQuery(L, R)
        elif R <= M:
            return self.left.rangeQuery(L, R)
        else:
            return self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R)


if __name__ == "__main__":
    nums = [5, 3, 7, 1, 4, 2]
    s = SegmentTree.build(nums, 0, len(nums) - 1)

    assert s.rangeQuery(0, 5) == sum(nums)
    assert s.rangeQuery(0, 1) == 8
    assert s.rangeQuery(4, 5) == 6
