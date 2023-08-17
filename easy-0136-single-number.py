from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time: O(n), where n is the length of nums
        Space: O(1)
        """
        res = 0

        for num in nums:
            res ^= num

        return res
