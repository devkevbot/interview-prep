class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.refs = 0

    def add_word(self, word):
        cur = self
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.is_word = True

    def remove_word(self, word):
        cur = self
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1


class Solution:
    @staticmethod
    def find_words(board: list[list[str]], words: list[str]) -> list[str]:
        """
        Let m = the number of rows
        Let n = the number of columns
        Time: O(mn * 4^(mn))
        """

        root = TrieNode()
        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r: int, c: int, node: TrieNode, word: str):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r, c) in visit
            ):
                return

            visit.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                node.is_word = False
                res.add(word)
                root.remove_word(word)

            for dr, dc in directions:
                dfs(r + dr, c + dc, node, word)

            # Backtracking is over: remove the position
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
