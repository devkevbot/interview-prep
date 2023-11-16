class Solution:
    @staticmethod
    def search(nums: list[int], target: int) -> int:
        """
        Time: O(log n) where n is the length of nums
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                # Search in left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Search in right half
                else:
                    left = mid + 1
            # Right half is sorted
            elif nums[mid] <= nums[right]:
                # Search in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Search in left half
                else:
                    right = mid - 1

        return -1
