from math import log, exp


class BitwiseSolution:
    @staticmethod
    def get_sum(a: int, b: int) -> int:
        """
        Time: O(1)
        Space: O(1)
        """

        # Equivalent to 32 ones in binary. We need a mask to contain our result to 32 bits due
        # to differences in how Python represents negative numbers and how we're choosing to compute
        # the sum.
        mask = 0xFFFFFFFF

        while b != 0:
            # Compute the carry
            tmp = (a & b) << 1
            a = (a ^ b) & mask
            b = tmp & mask

        # Handle negative numbers.
        #
        # Python expects negative numbers to have an infinite amount of leading 1s, but in our computation
        # we only use 32 bits.
        #
        # We first check if "a" is negative, i.e., it is larger than the maximum possible positive number, which
        # is a 0 followed by 31 1s.
        if a > (mask >> 1):
            # XOR with mask will flip the rightmost 32 bits.
            # NOT will flip all bits, which will give us the leading 1s expected by Python's representation of
            # negative numbers.
            return ~(a ^ mask)
        return a


class LogarithmSolution:
    @staticmethod
    def get_sum(a: int, b: int) -> int:
        if a == 0 and b != 0:
            return b
        elif b == 0 and a != 0:
            return a

        return int(log(exp(a) * exp(b)))
