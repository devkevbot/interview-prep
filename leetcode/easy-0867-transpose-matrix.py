class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Let m = the # of rows in the input matrix
        Let n = the # of cols in the input matrix
        Time: O(m * n)
        Space: O(m * n)
        """
        m = len(matrix)
        n = len(matrix[0])

        result = [[0] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                result[c][r] = matrix[r][c]

        return result
