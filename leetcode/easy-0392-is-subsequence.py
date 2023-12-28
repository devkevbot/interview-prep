class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Let s = the length of the input `s`
        Let t = the length of the input `t`
        Time: O(t)
        Space: O(1)
        """

        s_pos = 0

        for char in t:
            if s_pos == len(s):
                return True

            if char == s[s_pos]:
                s_pos += 1

        return s_pos == len(s)
