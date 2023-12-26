class Solution:
    @staticmethod
    def rob(nums: list[int]) -> int:
        """
        Let n = the number of houses to rob
        Time: O(n)
        Space: O(1)
        """

        def helper(_nums: list[int]):
            rob1, rob2 = 0, 0
            for n in _nums:
                rob1, rob2 = rob2, max(rob2, rob1 + n)
            return rob2

        # Edge case: no houses
        if not nums:
            return 0

        # Edge case: only one house
        if len(nums) == 1:
            return nums[0]

        return max(
            helper(nums[1:]),  # Exclude the 0th house and pick the last house
            helper(nums[:-1]),  # Exclude the last house and pick the 0th house
        )
