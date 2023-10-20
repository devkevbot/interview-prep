class Solution:
    @staticmethod
    def solve(board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Let n = number of rows
        Let m = number of columns
        Time: O(n * m)
        Space: O(n * m)
        """
        if not board or not board[0]:
            return

        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture(r: int, c: int):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            for dr, dc in directions:
                capture(r + dr, c + dc)

        # 1. Convert un-surrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in (0, ROWS - 1) or c in (0, COLS - 1)):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X) and un-capture un-surrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
