class Solution:
    @staticmethod
    def find_min(nums: list[int]) -> int:
        """
        Time: O(log n) where n is length of nums
        Space: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If this condition is t rue, we know that the pivot between the rotated and non-rotated segments
            # must be somewhere to the right of mid.
            if nums[mid] > nums[right]:
                left = mid + 1
            # Since the middle value is <= the right value, we don't want to discard the middle value
            # because it is possible for it to store a smaller value than at least one other index
            # in the list.
            else:
                right = mid

        return nums[left]
