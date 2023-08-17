class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time: O(1), the number of iterations doesn't depend on n and only constant operations are performed.
        Space: O(1)
        """
        res = 0
        num_bits = 32

        while num_bits > 0:
            # Extract the right-most bit from n
            mask = n & 1

            # Shift left to ensure that the following bitwise OR operation affects the correct bit.
            # In the end, the first bit that is extracted will be the left-most bit of the result.
            res <<= 1
            res |= mask

            # Move the input right so the next bit can be extracted
            n >>= 1
            num_bits -= 1

        return res
