class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Let n = the length of word1
        Let m = the length of word2
        Time: O(n + m)
        Space: O(n + m)
        """
        p1 = 0
        p2 = 0

        res = []

        use_word1 = True
        while p1 < len(word1) and p2 < len(word2):
            if use_word1:
                res.append(word1[p1])
                p1 += 1
            else:
                res.append(word2[p2])
                p2 += 1
            use_word1 = not use_word1

        while p1 < len(word1):
            res.append(word1[p1])
            p1 += 1

        while p2 < len(word2):
            res.append(word2[p2])
            p2 += 1

        return "".join(res)
