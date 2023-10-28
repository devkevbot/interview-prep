class Solution:
    @staticmethod
    def solve_n_queens(n: int) -> list[list[str]]:
        """
        Let n =
        Time: O(n!)
        Space: O(n)
        """

        # A queen can move any number of squares vertically, horizontally, or diagonally.

        # Backtracking formula:
        # - What is the stopping condition? => n queens placed without conflict
        # - What "paths" can be taken? => for some position r,c can place queen or not
        # - How to undo a path if it doesn't work? => reset board to "."

        solutions = []
        col_seen = set()
        pos_diag_seen = set()  # left to right, bottom to top ((row + col) sum is constant along the diagonal)
        neg_diag_seen = set()  # left to right, top to bottom ((row - col) sum is constant along the diagonal)

        def can_place_queen(row: int, col: int):
            if col in col_seen:
                return False
            if (row + col) in pos_diag_seen:
                return False
            if (row - col) in neg_diag_seen:
                return False
            return True

        def backtrack(row: int, n: int, board: list[list[str]]):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return

            # Try every column in this row
            for col in range(n):
                if can_place_queen(row, col):
                    col_seen.add(col)
                    pos_diag_seen.add(row + col)
                    neg_diag_seen.add(row - col)
                    board[row][col] = 'Q'

                    backtrack(row + 1, n, board)

                    board[row][col] = '.'
                    col_seen.remove(col)
                    pos_diag_seen.remove(row + col)
                    neg_diag_seen.remove(row - col)

        backtrack(0, n, [["."] * n for _ in range(n)])
        return solutions
