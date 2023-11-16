from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """

        stack = []

        for token in tokens:
            if token == "+":
                second, first = stack.pop(), stack.pop()
                stack.append(first + second)
            elif token == "-":
                second, first = stack.pop(), stack.pop()
                stack.append(first - second)
            elif token == "*":
                second, first = stack.pop(), stack.pop()
                stack.append(first * second)
            elif token == "/":
                second, first = stack.pop(), stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(token))

        return stack.pop()
