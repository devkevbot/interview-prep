class Solution:
    def can_partition(self, nums: list[int]) -> bool:
        """
        Let n = the number of elements in nums
        Time: O(n * 2^n)
        Space: O(2^n)
        """

        # Can't make two equal halves if the sum is odd.
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        # The DP set holds the possible sums of the subsets of the input array.
        dp = {0}

        for num in nums:
            # If any element is larger than target, the remaining elements will not
            # create a large enough sum to create two equal sums.
            if num > target_sum:
                return False

            dp_clone = dp.copy()
            for curr_sum in dp:
                if curr_sum + num == target_sum:
                    return True
                if curr_sum + num < target_sum:
                    dp_clone.add(curr_sum + num)
            dp = dp_clone

        return False
