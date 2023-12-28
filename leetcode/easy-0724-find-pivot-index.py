class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(n)
        """
        n = len(nums)

        prefix_sum = 0
        prefix_sums = [0] * n

        for i in range(n):
            prefix_sums[i] = prefix_sum
            prefix_sum += nums[i]

        suffix_sum = 0
        suffix_sums = [0] * n

        for i in reversed(range(n)):
            suffix_sums[i] = suffix_sum
            suffix_sum += nums[i]

        for i in range(n):
            if prefix_sums[i] == suffix_sums[i]:
                return i

        return -1
