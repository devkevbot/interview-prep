from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """
        Time: O(n log n), where n is the size of nums
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1
