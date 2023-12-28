class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Let s = the length of the input `s`
        Time: O(s)
        Space: O(1)
        """
        if k > len(s):
            return 0

        vowels = {"a", "e", "i", "o", "u"}

        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
        max_count = curr_count

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                curr_count -= 1
            if s[i] in vowels:
                curr_count += 1
            max_count = max(max_count, curr_count)

        return max_count
