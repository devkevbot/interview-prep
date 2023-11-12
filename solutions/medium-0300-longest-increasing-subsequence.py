class Solution:
    def length_of_lis(self, nums: list[int]) -> int:
        """
        Let n = the length of the input numbers
        Time: O(n^2)
        Space: O(1)
        """

        # Longest increasing subsequence ending at each index
        dp = [1] * len(nums)

        max_length = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_length = max(max_length, dp[i])

        return max_length
