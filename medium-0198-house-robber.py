class Solution:
    @staticmethod
    def rob(nums: list[int]) -> int:
        """
        Let n = the length of nums
        Time: O(n)
        Space: O(1)
        """

        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2
