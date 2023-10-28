class Solution:
    @staticmethod
    def search_matrix(matrix: list[list[int]], target: int) -> bool:
        """
        Let n = the number of rows
        Let m = the number of cols

        Time: O(log(n * m))
        Space: O(1)
        """

        top = 0
        bottom = len(matrix) - 1
        mid = -1

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

        row = matrix[mid]

        left = 0
        right = len(row) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if row[mid] == target:
                return True
            if target < row[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False
