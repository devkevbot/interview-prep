class Solution:
    @staticmethod
    def exist(board: list[list[str]], word: str) -> bool:
        """
        Let n = the number of tiles in the board
        Let k = the length of the word to find
        Time: O(n * 3^k)
        Space: O(k)
        """

        # Edge case: empty board
        if not board:
            return False

        N_ROWS = len(board)
        N_COLS = len(board[0])

        # Edge case: not enough letters in the board
        if len(word) > (N_ROWS * N_COLS):
            return False

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(path: str, r: int, c: int, index: int, visited) -> bool:
            visited.add((r, c))

            # Optimization: stop exploring if the current letter can't be used to spell the word
            if board[r][c] != word[index]:
                return False

            # Stop case: possible word candidate
            if len(path) == len(word):
                return path == word

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Skip position: out of bounds
                if nr < 0 or nr == N_ROWS or nc < 0 or nc == N_COLS:
                    continue

                # Skip position: already visited
                if (nr, nc) in visited:
                    continue

                if backtrack(path + board[nr][nc], nr, nc, index + 1, visited):
                    return True

                # Direction didn't work out - remove from visited
                visited.remove((nr, nc))

            return False

        for row in range(N_ROWS):
            for col in range(N_COLS):
                if backtrack(board[row][col], row, col, 0, set()):
                    return True

        return False
