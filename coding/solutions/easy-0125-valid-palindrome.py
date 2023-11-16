class TwoPointerSolution:
    def is_palindrome(self, s: str) -> bool:
        """
        Time: O(n), where n is the length of s. In the worst case, all characters mut be checked.
        Space: O(1). no additional memory is allocated.
        """

        l = 0
        r = len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


class StringManipulationSolution:
    def is_palindrome(self, s: str) -> bool:
        """
        Time: O(n), where n is the length of s. All characters are checked
        Space: O(n), where n is length of s. A new copy of the input string is created.
        """
        filtered_str = []

        for char in s:
            if char.isalnum():
                filtered_str.append(char.lower())

        filtered_str = "".join(filtered_str)
        return filtered_str == filtered_str[::-1]
