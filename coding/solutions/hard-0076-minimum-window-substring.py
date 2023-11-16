import collections


class Solution:
    def min_window(self, s: str, t: str) -> str:
        """
        Let s and t be the lengths of s and t, respectively.
        Time: O(s * t)
        Space: O(t)
        """

        # Can't make a solution
        if len(t) > len(s):
            return ""

        t_chars = collections.defaultdict(int)
        for char in t:
            t_chars[char] += 1

        left = 0
        window = ""

        # O(s)
        for right, val in enumerate(s):
            if val in t_chars:
                t_chars[val] -= 1

            # O(t)
            while self.all_characters_covered(t_chars):
                # Update solution
                if not window or (right - left + 1) < len(window):
                    window = s[left:right + 1]

                # Update left edge of the sliding window
                if s[left] in t_chars:
                    t_chars[s[left]] += 1
                left += 1

        return window

    def all_characters_covered(self, d) -> bool:
        for value in d.values():
            if value > 0:
                return False
        return True
