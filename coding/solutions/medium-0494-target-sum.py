class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        """
        Let n = the length of nums
        Let t = the sum of the nums array
        Time: O(n * t)
        Space: O(n * t)
        """
        memo = {}  # (index, total) => # of ways

        def dfs(i: int, total: int) -> int:
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in memo:
                return memo[(i, total)]

            memo[(i, total)] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return memo[(i, total)]

        return dfs(0, 0)
