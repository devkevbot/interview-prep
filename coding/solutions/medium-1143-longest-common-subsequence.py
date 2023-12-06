class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Let m = the length of text1
        Let n = the length of text2
        Time: O(mn)
        Space: O(mn)
        """

        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

        return dp[m][n]
