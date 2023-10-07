class Solution:
    @staticmethod
    def max_subarray(nums: list[int]) -> int:
        """
        Time: O(n), where n is the length of the input
        Space: O(1)
        """

        best_sum = nums[0]
        curr_sum = 0

        for x in nums:
            curr_sum = max(0, curr_sum)
            curr_sum += x
            best_sum = max(best_sum, curr_sum)

        return best_sum
