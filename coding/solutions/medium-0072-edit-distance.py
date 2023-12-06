class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Let m = the length of word1
        Let n = the length of word2
        Time: O(mn)
        Space: O(mn)
        """
        rows = len(word1)
        cols = len(word2)

        # table[r][c] = the number of edit operations required when considering word1[r:] and word2[c:]
        table = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for c in range(cols + 1):
            table[0][c] = c
        for r in range(rows + 1):
            table[r][0] = r

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if word1[r - 1] != word2[c - 1]:
                    table[r][c] = (
                        # min of replace, delete, insert
                        min(table[r - 1][c - 1], table[r - 1][c], table[r][c - 1])
                        + 1
                    )
                else:
                    table[r][c] = table[r - 1][c - 1]

        return table[rows][cols]
