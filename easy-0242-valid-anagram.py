import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(s + t) - In the worst case, all letters in s and t must be iterated through
        Space: O(s) - The letter in s are always stored in a Counter
        """
        if len(s) != len(t):
            return False

        letters_in_s = collections.Counter(s)

        for letter in t:
            if letter not in letters_in_s:
                return False

            if letters_in_s[letter] == 0:
                return False

            letters_in_s[letter] -= 1

        return True
