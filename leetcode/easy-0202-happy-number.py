class Solution:
    def is_happy(self, n: int) -> bool:
        """
        Let k = the number of digits in n
        Time: O(k)
        Space: O(1)
        """
        slow, fast = n, self.sum_square_digits(n)

        while slow != fast:
            fast = self.sum_square_digits(fast)
            fast = self.sum_square_digits(fast)
            slow = self.sum_square_digits(slow)

        return fast == 1

    def sum_square_digits(self, n):
        """
        Let k = the number of digits in n
        Time: O(k)
        Space: O(1)
        """
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
