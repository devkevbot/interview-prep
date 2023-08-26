from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
        """
        Time: O(logn), where n is the number of input elements
        Space: O(1)
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return True

            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Time: O(log(m * n)), where m is the number of rows and n is the number of columns
        Space: O(1)
        """
        if len(matrix) == 0:
            return False

        NUM_ROWS = len(matrix)

        start_row = 0
        end_row = NUM_ROWS - 1
        mid_row = -1

        # Step 1: Find which row to perform the binary search on to find the target.
        # O(logm)
        while start_row <= end_row:
            mid_row = start_row + (end_row - start_row) // 2

            if target > matrix[mid_row][-1]:
                start_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                end_row = mid_row - 1
            else:
                break

        # In this condition, the value was not in the matrix since a suitable row could not be found.
        if start_row > end_row:
            return False

        # Step 2: Find the target within the row it should belong to.
        # Olog(n)
        return self.binarySearch(matrix[mid_row], target)
