class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(log n)
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
