class Solution:
    @staticmethod
    def max_product(nums: list[int]) -> int:
        """
        Let n = the length of nums
        Time: O(n)
        Space: O(1)
        """

        # (min, max)
        prev = (nums[0], nums[0])
        global_max = nums[0]

        for i in range(1, len(nums)):
            prev_min, prev_max = prev

            curr_min = min(prev_min * nums[i], prev_max * nums[i], nums[i])
            curr_max = max(prev_min * nums[i], prev_max * nums[i], nums[i])

            global_max = max(global_max, curr_max)

            prev = (curr_min, curr_max)

        return global_max
