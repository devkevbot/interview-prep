from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time: O(n), where n is the length of the input
        Space: O(1)
        """

        # This problem is easily solved by applying Kadane's algorithm.
        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum
