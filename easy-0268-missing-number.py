class Solution:
    @staticmethod
    def missing_number(nums: list[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        # Gauss's formula: The sum from 1 to N is (N)(N+1)/2
        expected_sum = (len(nums) * (len(nums) + 1)) // 2

        # O(n) time to compute sum
        given_sum = sum(nums)

        return expected_sum - given_sum
