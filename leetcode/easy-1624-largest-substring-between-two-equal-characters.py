class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        Let s = the length of the input `s`
        Time: O(s)
        Space: O(26) -> O(1) since character set of input is just lowercase English alphabet
        """
        max_length = -1
        seen_at = {}

        for i, val in enumerate(s):
            if val in seen_at:
                left = seen_at[val]
                right = i
                max_length = max(max_length, right - left - 1)
            else:
                seen_at[val] = i

        return max_length
