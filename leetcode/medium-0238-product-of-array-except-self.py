class Solution:
    @staticmethod
    def product_except_self(nums: list[int]) -> list[int]:
        """
        Time: O(n), where n is the length of nums
        Space: O(n)
        """
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]

        return res
