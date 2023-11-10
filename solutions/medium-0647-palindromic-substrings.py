class Solution:
    def count_substrings(self, s: str) -> int:
        """
        Let n = the length of the input string
        Time: O(n^2)
        Space: O(1)
        """

        count = 0
        for i in range(len(s)):
            # Count odd-length palindromes
            # Example: for "aaab", start at the first 'a'
            count += self.count_palindromes(s, i, i)
            # Count even-length palindromes
            # Example: for "aaab", consider both the first and second 'a' to start
            count += self.count_palindromes(s, i, i + 1)
        return count

    def count_palindromes(self, s: str, l: int, r: int) -> int:
        count = 0
        # Expand outward to find more palindromes while the string is palindromic
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
