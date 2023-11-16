class Solution:
    @staticmethod
    def jump(nums: list[int]) -> int:
        """
        Let n = the length of nums
        Time: O(n)
        Space: O(1)
        """

        min_jumps = 0
        # left and right represent the boundaries of where we can currently jump from
        left = 0
        right = 0

        while right < len(nums) - 1:
            farthest_jump = 0
            for i in range(left, right + 1):
                farthest_jump = max(farthest_jump, i + nums[i])
            left = right + 1
            right = farthest_jump
            min_jumps += 1

        return min_jumps
