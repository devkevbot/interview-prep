class Solution:
    @staticmethod
    def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
        """
        Let n = the number of rows
        Let m = the number of columns
        Time: O(n * m)
        Space: O(n * m)
        """

        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, visited: set, prev_height: int):
            # Since we're going from border cells to inner cells, we must look for heights which are >=
            if (r, c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prev_height:
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Perform DFS starting at the top and bottom borders
        for col in range(COLS):
            dfs(0, col, pacific, heights[0][col])
            dfs(ROWS - 1, col, atlantic, heights[ROWS - 1][col])

        # Perform DFS starting at the left and right borders
        for row in range(ROWS):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, COLS - 1, atlantic, heights[row][COLS - 1])

        res = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res
