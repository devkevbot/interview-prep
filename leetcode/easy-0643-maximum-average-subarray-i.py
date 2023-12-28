class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(1)
        """
        if k > len(nums):
            return 0

        curr_sum = 0
        # Compute average for first window of size k
        for i in range(k):
            curr_sum += nums[i]
        curr_avg = curr_sum / k
        max_avg = curr_avg

        for i in range(k, len(nums)):
            curr_sum -= nums[i - k]  # Remove number from trailing window edge
            curr_sum += nums[i]  # Add number to leading window edge
            curr_avg = curr_sum / k
            max_avg = max(max_avg, curr_avg)

        return max_avg
