from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Time: O(c * b), where c is the number of values from 0 to n (inclusive) and b is the number of bits in an integer
        Space: O(c), where c is the number of values from 0 to n (inclusive)
        """
        res = []

        for i in range(n + 1):
            count = self.num_ones(i)
            res.append(count)

        return res

    def num_ones(self, n: int) -> int:
        """
        Time: O(b) where b is the number of bits in n
        Space: O(1)
        """
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1
        return count
