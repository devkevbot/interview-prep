class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        Let n = the length of the input `nums`
        Time: O(log n)
        Space: O(1)
        """

        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]
