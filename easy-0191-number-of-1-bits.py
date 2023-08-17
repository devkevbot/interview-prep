# Bit maniuplation #1
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Time: O(n) where n is the number of bits
        Space: O(1)
        """
        num_bits = 0

        while n > 0:
            num_bits += n & 1
            n //= 2

        return num_bits


# Bit maniuplation #2
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Time: O(n) where n is the number of bits
        Space: O(1)
        """
        num_bits = 0

        while n > 0:
            num_bits += n & 1
            n >>= 1

        return num_bits


# Python built-in
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Time: O(n) where n is the number of bits
        Space: O(n) where n is the number of bits
        """
        return bin(n).count("1")
