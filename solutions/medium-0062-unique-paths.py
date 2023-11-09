from itertools import product


class Solution:
    @staticmethod
    def unique_paths(m, n):
        """
        Time: O(m * n)
        Space: O(n)
        """

        # Columns
        dp = [1] * n

        for _, j in product(range(1, m), range(1, n)):
            # We are only accessing the same column from previous row which can be given by dp[j]
            # and the previous column of current row which can be given by dp[j-1]
            dp[j] += dp[j - 1]

        return dp[-1]
