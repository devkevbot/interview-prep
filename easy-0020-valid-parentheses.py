class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time: O(s) - In the worst case, all of the characters in s must be iterated. All work done
        inside the iterations in constant.
        Space: O(n) - In the worst case, all of the characters in s will exist on the stack.
        """

        open_paren = set(["(", "[", "{"])
        pairs = {")": "(", "]": "[", "}": "{"}

        stack = []

        for char in s:
            if char in open_paren:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[char]:
                    return False

        return len(stack) == 0
