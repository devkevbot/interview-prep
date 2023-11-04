class Solution:
    @staticmethod
    def move_zeroes(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Let n = the length of nums
        Time: O(n)
        Space: O(1)
        """
        swap_pos = 0

        for i, n in enumerate(nums):
            if n != 0:
                nums[swap_pos] = n
                swap_pos += 1

        for i in range(swap_pos, len(nums)):
            nums[i] = 0
