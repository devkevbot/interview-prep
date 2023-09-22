class BitShiftSolution:
    @staticmethod
    def hamming_weight(n: int) -> int:
        """
        Let b = the number of bits in the input
        Time: O(b) where b is the number of bits
        Space: O(1)
        """
        num_ones = 0

        while n > 0:
            num_ones += n & 1
            n >>= 1

        return num_ones


class BuiltInSolution:
    @staticmethod
    def hamming_weight(n: int) -> int:
        """
        Let b = the number of bits in the input
        Time: O(b)
        Space: O(b)
        """
        return bin(n).count("1")
