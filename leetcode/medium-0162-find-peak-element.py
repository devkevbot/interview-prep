class BinarySearchSolution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(log n)
        Space: O(1)
        """
        low = 0
        high = len(nums) - 1

        while low < high:
            mid1 = low + (high - low) // 2
            mid2 = mid1 + 1
            # Move low or high in the direction of upward change between the two midpoints
            if nums[mid1] < nums[mid2]:
                low = mid2
            else:
                high = mid1

        return low


class LinearSolution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        Let n = the length of the input `nums`
        Time: O(n)
        Space: O(1)
        """
        for i in range(len(nums)):
            left_neighbour = float("-inf") if i == 0 else nums[i - 1]
            right_neighbour = float("-inf") if i == len(nums) - 1 else nums[i + 1]
            if left_neighbour < nums[i] and right_neighbour < nums[i]:
                return i
