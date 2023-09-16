class CountingSolution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        """
        Let s = the length of s
        Let t = the length of t
        Time: O(s + t)
        Space: O(1)
        """

        # O(26) space
        chars = [0] * 26

        # O(s) time
        for char in s:
            chars[ord(char) - ord("a")] += 1
        # O(t) time
        for char in t:
            chars[ord(char) - ord("a")] -= 1

        # O(26) time
        for count in chars:
            if count != 0:
                return False
        return True


class SortingSolution:
    @staticmethod
    def is_anagram(s: str, t: str) -> bool:
        """
        Let s = the length of s
        Let t = the length of t
        Time: O(s log s + t log t)
        Space: O(1)
        """
        return sorted(s) == sorted(t)
