class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(1)
        """
        small = float("inf")
        large = float("inf")

        for num in nums:
            if num <= small:  # The number is less than both small and large
                small = num
            elif num <= large:  # The number is greater than small but less than large
                large = num
            else:  # The number is greater than small and large
                return True
        return False
