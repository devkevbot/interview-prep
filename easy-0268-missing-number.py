from typing import List


# Sum approach
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time: O(n) - must sum the input array
        Space: O(1)
        """
        # Gauss's formula
        expected_sum = (len(nums) * (len(nums) + 1)) // 2

        given_sum = sum(nums)

        return expected_sum - given_sum


# XOR approach
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        # Create list which contains both the given numbers and the the nubmers which should be present in the range.
        # Example [3, 0, 1] + [0, 1, 2, 3]
        all_numbers = nums + [i for i in range(len(nums) + 1)]

        res = 0

        for num in all_numbers:
            res ^= num

        return res
