class Solution:
    def __init__(self):
        self.left = 0
        self.right = -1

    def longest_palindrome(self, s: str) -> str:
        """
        Let n = the length of the input string s
        Time: O(n^2)
        Space: O(1)
        """

        for i in range(len(s)):
            # Odd-length palindromes
            self.find_palindromes(s, i, i)
            # Even-length palindromes
            self.find_palindromes(s, i, i + 1)
        return s[self.left : self.right + 1]

    def find_palindromes(self, s: str, l: int, r: int) -> None:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            curr_length = r - l + 1
            stored_length = self.right - self.left + 1
            if curr_length > stored_length:
                self.left = l
                self.right = r
            l -= 1
            r += 1
