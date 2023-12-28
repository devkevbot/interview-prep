class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Let n = the length of the input `s`
        Time: O(n)
        Space: O(n)
        """
        words = list(s.split(" "))
        words = map(lambda w: w.strip(), words)
        words = list(filter(lambda w: w != "", words))
        words.reverse()
        return " ".join(words)
