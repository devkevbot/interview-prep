class Solution:
    @staticmethod
    def can_jump(nums: list[int]) -> bool:
        """
        Let n = the length of nums
        Time: O(n)
        Space: O(1)
        """

        target = len(nums) - 1
        for i in reversed(range(len(nums) - 1)):
            if i + nums[i] >= target:
                target = i
        return target == 0
