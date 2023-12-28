class Solution:
    def removeStars(self, s: str) -> str:
        """
        Let s = the length of the input `s`
        Time: O(s)
        Space: O(s)
        """
        stack = []

        for char in s:
            if char != "*":
                stack.append(char)
            else:
                stack.pop()

        return "".join(stack)
