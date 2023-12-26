class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Let n = the length of s1
        Let m = the length of s2
        Time: O(n * m)
        Space: O(n * m)
        """
        dp = {}
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            # i + j is always equal to the current position of s3

            # try to use character from s1
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j):
                return True
            # try to use character from s2
            if j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1):
                return True

            dp[(i, j)] = False
            return False

        return dfs(0, 0)
