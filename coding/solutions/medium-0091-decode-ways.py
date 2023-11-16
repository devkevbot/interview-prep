class Solution:
    @staticmethod
    def num_decodings(s: str) -> int:
        """
        Let n = the length of s
        Time: O(n)
        Space: O(1)
        """
        dp, dp1, dp2, n = 0, 1, 0, len(s)

        for i in reversed(range(n)):
            # Single digit
            if s[i] != '0':
                dp += dp1

            # Two digits
            if i + 1 < n and (s[i] == '1' or s[i] == '2' and s[i + 1] <= '6'):
                dp += dp2

            dp, dp1, dp2 = 0, dp, dp1

        return dp1
