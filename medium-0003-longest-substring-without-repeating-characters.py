class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        """
        Time: O(n), where is length of the input string
        Space: O(n)
        """

        seen = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)

        return longest
