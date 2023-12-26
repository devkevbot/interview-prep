import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Time: O(n), where n is the number of tiles in the board
        Space: O(n)
        """
        BOARD_SIZE = len(board[0])

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        # The key is (row // 3, col // 3)
        squares = collections.defaultdict(set)

        for r in range(BOARD_SIZE):
            for c in range(BOARD_SIZE):
                val = board[r][c]

                if val == ".":
                    continue

                if val in rows[r] or val in cols[c] or val in squares[(r // 3, c // 3)]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True
