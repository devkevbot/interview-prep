class Solution:
    @staticmethod
    def plus_one(digits: list[int]) -> list[int]:
        """
        Let n = the length of digits.
        Time: O(n)
        Space: O(n)
        """

        result = [digit for digit in digits]

        carry = 1
        for i, value in enumerate(reversed(digits)):
            total = value + carry
            carry = total // 10
            digit = total % 10
            result[len(result) - 1 - i] = digit

        if carry:
            result = [carry] + result

        return result
