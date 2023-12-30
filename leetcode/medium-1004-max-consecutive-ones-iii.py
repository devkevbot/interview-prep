class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(1)
        """

        left = 0
        max_window_size = 0
        num_zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeroes += 1

            if num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            max_window_size = max(max_window_size, right - left + 1)

        return max_window_size
