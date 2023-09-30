class Solution:
    @staticmethod
    def word_break(s: str, word_dict: list[str]) -> bool:
        """
        Let s = the length of the input 's'
        Let w = the number of words in word_dict
        Time: O(s^2 * w)
        Space: O(s)
        """

        # O(s) space
        cache = [False] * (len(s) + 1)
        # Base case
        cache[len(s)] = True

        # O(s) time
        for i in reversed(range(len(s))):
            # O(w) time
            for word in word_dict:
                end = i + len(word)

                # O(s) time to compute s[..] == word
                if end <= len(s) and s[i:end] == word:
                    cache[i] = cache[end]
                if cache[i]:
                    break

        return cache[0]
