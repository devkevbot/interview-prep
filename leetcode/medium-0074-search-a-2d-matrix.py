class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        Let m = the number of rows in the input `matrix`
        Let n = the number of columns in the input `matrix`
        Time: O(log(n * m)) = O(log n + log m)
        Space: O(1)
        """
        top = 0
        bottom = len(matrix) - 1
        mid = None

        while top <= bottom:
            mid = top + (bottom - top) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if top > bottom:
            return False

        row = mid
        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            if target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False
