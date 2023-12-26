class Solution:
    @staticmethod
    def rotate(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Let n = the number of elements in the matrix
        Time: O(n)
        Space: O(1)
        """
        n = len(matrix)

        # Transpose:
        # - Traverse the top-left to bottom right diagonal line
        # - Swap elements below the current item with the element to the right of the current item
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse rows
        # - Visit each row
        # - Swap the elements of each row in-place
        for i in range(n):
            l = 0
            r = n - 1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1
