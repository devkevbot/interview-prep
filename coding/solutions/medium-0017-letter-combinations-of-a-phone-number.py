class Solution:
    @staticmethod
    def letter_combinations(digits: str) -> list[str]:
        """
        Let n = the number of digits
        Time: O(4^n * n)
        Space: O(n)
        """

        ans = []

        number_2_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wyxz",
        }

        def backtrack(path: list[str], index: int):
            if len(path) == len(digits):
                ans.append("".join(path))
                return

            letters = number_2_letters[digits[index]]

            for letter in letters:
                path.append(letter)
                backtrack(path, index + 1)
                path.pop()

        if digits:
            backtrack([], 0)

        return ans
