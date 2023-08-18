from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n), where n is the length of nums
        Space: O(n)
        """
        # [1, 2, 3, 4]
        # [2*3*4, 1*3*4, 1*2*4, 1*2*3] = [24, 12, 8, 6]

        # Prefix
        # [1,1,2,6]
        prefix_product = 1
        prefixes = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix_product *= nums[i - 1]
            prefixes[i] = prefix_product

        # Suffix
        # [24,12,4,1]
        suffix_product = 1
        suffixes = [1] * len(nums)

        for i in reversed(range(0, len(nums) - 1)):
            suffix_product *= nums[i + 1]
            suffixes[i] = suffix_product

        result = []
        for i in range(len(nums)):
            result.append(prefixes[i] * suffixes[i])

        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n), where n is the length of nums
        Space: O(n) (or O(1) if the space require to produce the output doesn't count)
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
