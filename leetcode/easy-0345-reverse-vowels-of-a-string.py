class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Let n = the length of the input `s`
        Time: O(n)
        Space: O(n)
        """

        vowels = {"a", "e", "i", "o", "u"}
        vowel_pos = []

        # Record vowel positions
        for i, char in enumerate(s):
            if char.lower() in vowels:
                vowel_pos.append(i)

        word = list(s)

        l = 0
        r = len(vowel_pos) - 1

        # Swap vowels
        while l < r:
            lpos = vowel_pos[l]
            rpos = vowel_pos[r]
            word[lpos], word[rpos] = word[rpos], word[lpos]

            l += 1
            r -= 1

        return "".join(word)
