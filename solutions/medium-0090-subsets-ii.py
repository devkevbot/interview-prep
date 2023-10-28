class Solution:
    def subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        """
        Time: O(n * 2 ^ n), where n is the length of nums
        Space: O(n * 2 ^ n)
        """

        # Sorting allows us to skip duplicates later on
        nums.sort()

        subset = []
        powerset = []

        self.helper(0, nums, subset, powerset)

        return powerset

    def helper(self, i, nums, subset, powerset):
        if i == len(nums):
            powerset.append(subset.copy())
            return

        # Decision to include the current number
        subset.append(nums[i])
        self.helper(i + 1, nums, subset, powerset)

        # Decision to not include the current number
        subset.pop()
        # Skip duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, subset, powerset)
